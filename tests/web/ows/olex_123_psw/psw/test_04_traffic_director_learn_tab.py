import time
import pytest

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.enroll = False
        self.stack = request.config.getoption("--stack")
        self.traffic_director = self.fc.fd["traffic_director"]
        self.printer_oid, self.printer_programs = self.fc.get_printer_oid_and_program(self.traffic_director.printer_sku[self.printer_profile])
        

        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_id=3626111&group_order=asc&display_deleted_cases=0
        """
    def test_01_traffic_director_bat_flow(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.hpid.handle_privacy_popup()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_watch_video_btn()
        self.traffic_director.verify_printer_features_btn()
        self.traffic_director.verify_get_help_btn()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_hp_support_button_tab()
        if "hp+" in self.printer_programs:
             self.traffic_director.verify_hp_plus_and_instant_ink_sidemenu_btn()
        self.traffic_director.verify_printer_parts()
        self.traffic_director.verify_hp_support_button_tab()
        self.traffic_director.click_get_help_btn_sidemenu()
        self.traffic_director.verify_get_help_tab()
        self.traffic_director.click_printer_features_btn_sidemenu()
        self.traffic_director.verify_printer_parts()
        if "hp+" in self.printer_programs:
             self.traffic_director.click_hp_plus_and_instant_ink_sidemenu_btn()
             self.traffic_director.verify_hp_plus_instant_ink_tab()
             self.traffic_director.click_instant_ink_learn_more_url()
             self.traffic_director.verify_instant_ink_page()
        self.traffic_director.click_hp_support_button_tab()
        self.traffic_director.verify_hp_support_product_page()
        self.traffic_director.click_hp_support_product_page()
        self.driver.add_window("product_support")
        self.driver.switch_window("product_support")
        url = self.driver.current_url
        if "support" not in url or self.printer_oid not in url:
                raise AssertionError(f"Expecting 'support' and printer_oid '{self.printer_oid}' in url, got: {url}")
        self.driver.close_window("product_support")