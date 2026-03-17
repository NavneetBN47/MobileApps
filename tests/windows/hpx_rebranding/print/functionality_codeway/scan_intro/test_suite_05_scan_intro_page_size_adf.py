import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_05_Scan_Intro_Page_Size_ADF(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_page_size_adf_C43738410(self):
        """
        Select source to Document Feeder, verify different Page size values can be changed and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738410
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Test printer does not support ADF scan. Skip this test case.")
        
        if self.fc.fd["scan"].get_scan_source_value() != self.fc.fd["scan"].ADF:
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF, "Failed to switch to ADF source"
        assert self.fc.fd["scan"].get_scan_page_size_value() == self.fc.fd["scan"].LETTER, "Default page size is not Letter"
        
        adf_page_sizes = [
            self.fc.fd["scan"].LETTER,
            self.fc.fd["scan"].A4,
            self.fc.fd["scan"].LEGAL,
            self.fc.fd["scan"].ENTIRE_SCAN_AREA,
            self.fc.fd["scan"].X57
        ]

        failed_sizes = []
        
        for index, adf_page_size in enumerate(adf_page_sizes):
            try:
                logging.info(f"Testing page size [{index + 1}/{len(adf_page_sizes)}]: {adf_page_size}")
                
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
                
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PAGESIZE, adf_page_size)
                assert self.fc.fd["scan"].get_scan_page_size_value() == adf_page_size, f"Failed to select page size: {adf_page_size}"
                
                self.fc.fd["scan"].click_scan_btn()
                self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
                
                if index < len(adf_page_sizes) - 1:
                    self.fc.fd["scan"].click_back_arrow()
                    self.fc.fd["scan"].verify_exit_without_saving_dialog()
                    self.fc.fd["scan"].click_yes_btn()
                    self.fc.fd["scan"].verify_scan_btn(timeout=30)
                
                logging.info(f"✓ Page size {adf_page_size} test passed")
                
            except Exception as e:
                logging.error(f"✗ Page size {adf_page_size} test failed: {str(e)}")
                failed_sizes.append({"page_size": adf_page_size, "error": str(e)})
                
                try:
                    self.fc.restart_hpx()
                    self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
                    self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
                    self.fc.fd["devicesDetailsMFE"].click_scan_tile()
                    self.fc.fd["scan"].verify_scan_btn(timeout=30)
                    
                    if self.fc.fd["scan"].verify_source_dropdown_enabled():
                        if self.fc.fd["scan"].get_scan_source_value() != self.fc.fd["scan"].ADF:
                            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
                    logging.info("App state recovered, continuing to next page size...")
                except Exception as recovery_error:
                    logging.error(f"Failed to recover app state: {str(recovery_error)}")
        
        if failed_sizes:
            error_msg = f"\n{len(failed_sizes)} out of {len(adf_page_sizes)} page sizes failed:\n"
            for item in failed_sizes:
                error_msg += f"  - {item['page_size']}: {item['error']}\n"
            raise AssertionError(error_msg)

