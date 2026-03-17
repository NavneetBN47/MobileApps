import time
import pytest
import logging

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup

        if self.printer_profile not in self.fc.smb_flowers:
            pytest.skip("Skipping test - printer profile is not in flowers printer list")

        self.request = self.driver.session_data["request"]
        self.browser_type = self.request.config.getoption("--browser-type")
        self.screen_size = self.request.config.getoption("--browser-size")
        self.traffic_director = self.fc.fd["traffic_director"]
        self.stack = self.request.config.getoption("--stack")
        
        self.cherry_skus = {"cherry_ams_row":"8X3D2A", "cherry_emea":"8X3D8A", "cherry_chin":"8X3E6A"}
        self.lotus_skus = {"lotus_ams_row":"8X3F4A", "lotus_emea":"8X3F6A", "lotus_chin":"8X3G4A"}       

        """
        testRail:
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3564380
        """
    
    def test_01_flowers_psw_landing_page(self):
        self._run_psw_landing_page_test(self.traffic_director.sku)
    
    def test_02_cherry_ams_row_psw_landing_page(self):
        if not self.printer_profile.startswith("cherry"):
            pytest.skip("Skipping cherry tests - printer profile is not cherry")
        self._run_psw_landing_page_test(self.cherry_skus["cherry_ams_row"])

    def test_03_cherry_emea_psw_landing_page(self):
        if not self.printer_profile.startswith("cherry"):
            pytest.skip("Skipping cherry tests - printer profile is not cherry")
        self._run_psw_landing_page_test(self.cherry_skus["cherry_emea"])

    def test_04_cherry_chin_psw_landing_page(self):
        if not self.printer_profile.startswith("cherry"):
            pytest.skip("Skipping cherry tests - printer profile is not cherry")
        self._run_psw_landing_page_test(self.cherry_skus["cherry_chin"])

    def test_05_lotus_ams_row_psw_landing_page(self):
        if not self.printer_profile.startswith("lotus"):
            pytest.skip("Skipping lotus tests - printer profile is not lotus")
        self._run_psw_landing_page_test(self.lotus_skus["lotus_ams_row"])

    def test_06_lotus_emea_psw_landing_page(self):
        if not self.printer_profile.startswith("lotus"):
            pytest.skip("Skipping lotus tests - printer profile is not lotus")
        self._run_psw_landing_page_test(self.lotus_skus["lotus_emea"])

    def test_07_lotus_chin_psw_landing_page(self):
        if not self.printer_profile.startswith("lotus"):
            pytest.skip("Skipping lotus tests - printer profile is not lotus")
        self._run_psw_landing_page_test(self.lotus_skus["lotus_chin"])    
    
    
    def _update_sku(self, sku):
        """Helper to navigate to a specific SKU landing page"""
        try:
            url = self.traffic_director.td_url.replace("8X3E3A", sku)
        except AttributeError:
            url = self.traffic_director.td_url.replace("8X3G2A", sku)

        return url

    def _run_psw_landing_page_test(self, sku):
        """Common test steps for PSW landing page verification"""
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, self._update_sku(sku))
        self.traffic_director.verify_enter_delta_program_password()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_landing_page_title()
        self.traffic_director.verify_landing_page_description()
        # start setup btn is Install Drivers btn for flowers
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_country_language_selector_link()
        
        # Get list of files before download
        downloads_folder = f"C:\\Users\\{self.ssh_client.username}\\Downloads"
        list_before_cmd = f"Get-ChildItem '{downloads_folder}' -File 2>$null | Select-Object -ExpandProperty Name"
        result_before = self.ssh_client.send_command(list_before_cmd)
        files_before = set(result_before['stdout'].strip().split('\n')) if result_before['stdout'].strip() else set()
        
        self.traffic_director.click_start_setup_btn()
        curent_url = self.driver.allow_blocked_download(self.screen_size)
        
        # Get list of files after download
        result_after_all = self.ssh_client.send_command(list_before_cmd)
        files_after = set(result_after_all['stdout'].strip().split('\n')) if result_after_all['stdout'].strip() else set()
        
        # Find newly downloaded files
        new_files = files_after - files_before
        
        # Verify HPEasyStart was downloaded by checking file names
        hpeasystart_files = [f for f in new_files if f.startswith("HPEasyStart")]
        
        if not hpeasystart_files:
            # Log only the newly downloaded files
            logging.info(f"HPEasyStart file was not found. Files downloaded in this session: {', '.join(new_files) if new_files else 'None'}")
            raise AssertionError("HPEasyStart file was not downloaded successfully")
        else:
            # Log successful download
            logging.info(f"HPEasyStart file(s) downloaded successfully: {', '.join(hpeasystart_files)}")
        
        # Remove the downloaded file(s)
        self.ssh_client.send_command(f"Remove-Item '{downloads_folder}\\HPEasyStart*' -Force")
        
        # Also remove any unconfirmed files in case download failed
        self.ssh_client.send_command(f"Remove-Item '{downloads_folder}\\Unconfirmed*' -Force")
        
        # Verify file was removed
        check_cmd = f"Get-ChildItem '{downloads_folder}' -Filter 'HPEasyStart*' | Measure-Object | Select-Object -ExpandProperty Count"
        result_verify = self.ssh_client.send_command(check_cmd)
        remaining_count = int(result_verify['stdout'].strip())
        
        if remaining_count > 0:
            raise AssertionError(f"Failed to remove HPEasyStart file(s). {remaining_count} file(s) still exist")
        
        self.traffic_director.clear_downloaded_file()
        self.driver.navigate(curent_url)