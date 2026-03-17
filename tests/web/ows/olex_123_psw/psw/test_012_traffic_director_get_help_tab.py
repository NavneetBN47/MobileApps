import pytest
import logging
import time

pytest.app_info = "POOBE"

class Test_validate_get_help_btn(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser_type = request.config.getoption("--browser-type")
        self.traffic_director = self.fc.fd["traffic_director"]
        
        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=4330019
        """
    
    def test_01_validate_get_help_btn(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_three_tabs_in_header()
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_watch_video_btn()
        self.get_help_btn_common_functions()
        self.fc.verify_get_help_connectivity_content()
        self.fc.verify_hp_support_button_on_get_help_btn()
        url = self.traffic_director.td_url.split("/")
        url[-1] = "403X3A"
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, url='/'.join(url))
        self.fc.fd["hpid"].verify_privacy_popup()
        self.get_help_btn_common_functions()
        self.traffic_director.click_get_help_subtab_hp_smart_installation()
        self.traffic_director.verify_get_help_hp_smart_installation_content()
        self.traffic_director.click_supported_os_drop_down_on_subtab_hp_smart_installantion()
        self.traffic_director.verify_supported_os_drop_down_content()
        self.traffic_director.click_install_on_windows_drop_down()
        self.traffic_director.verify_install_on_windows_content()
        self.traffic_director.click_install_on_macOS_drop_down()
        self.traffic_director.verify_install_on_macOS_content()
        self.traffic_director.click_install_on_mobile_drop_down()
        self.traffic_director.verify_install_on_mobile_content()
        self.traffic_director.click_use_hp_smart_chromeos_drop_down()
        self.traffic_director.verify_use_hp_smart_chromeos_content()
        self.traffic_director.click_supported_os_drop_down_on_subtab_hp_smart_installantion()
        self.traffic_director.click_install_on_windows_drop_down()
        self.traffic_director.click_install_on_macOS_drop_down()
        self.traffic_director.click_install_on_mobile_drop_down()
        self.traffic_director.click_use_hp_smart_chromeos_drop_down()
        self.fc.verify_hp_support_button_on_get_help_btn()
        self.traffic_director.click_get_help_subtab_connectivity()
        self.traffic_director.verify_get_help_btn()
        self.traffic_director.verify_get_help_connectivity_subtab_content()
        self.get_help_btn_common_functions()
        self.fc.verify_get_help_connectivity_content()
        self.fc.verify_hp_support_button_on_get_help_btn()     
        
    ################## Private Function ############
    
    def get_help_btn_common_functions(self):
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab()
        self.traffic_director.click_get_help_btn()
        self.traffic_director.verify_get_help_btn()
        self.traffic_director.verify_get_help_btn()
        self.traffic_director.verify_get_help_connectivity_subtab_content()
        self.traffic_director.click_setup_tab()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.click_get_help_btn()
        self.traffic_director.verify_get_help_btn()