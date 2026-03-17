import time
import pytest
import datetime

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup

        self.request = self.driver.session_data["request"]
        self.td_live_ui = self.fc.fd["td_live_ui"]
        self.load_ink = self.td_live_ui.fd["load_ink_td"]
        self.print_calibration = self.td_live_ui.fd["print_calibration"]
        self.scan_calibration = self.td_live_ui.fd["scan_calibration"]
        self.traffic_director = self.fc.fd["traffic_director"]
        self.hp_software = self.td_live_ui.fd["hp_software"]
        self.stack = self.request.config.getoption("--stack")
        self.har = self.request.config.getoption("--har")
        self.normalize_profile = self.traffic_director.normalize_profile(self.printer_profile)

        if self.har:
            self.spec_animation_data = self.fc.load_all_printer_animations(self.normalize_profile)
        else:
            self.spec_animation_data = None        

        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3564380
        """
    def test_01_psw_bat_flow(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.hpid.handle_privacy_popup()
        self.traffic_director.verify_onboarding_center_page()
        if not self.printer_profile.startswith("trillium"):
            self.traffic_director.verify_start_setup_btn()
            self.traffic_director.verify_watch_video_btn()
        self.traffic_director.verify_printer_features_btn()
        self.traffic_director.verify_get_help_btn()
        self.traffic_director.click_start_setup_btn()
        self.td_live_ui.navigate_load_paper_step(self.normalize_profile, self.spec_animation_data)
        self.load_ink.verify_web_page()
        self.load_ink.verify_install_ink_card_image(0)
        self.traffic_director.verify_veneer_stepper()
        self.load_ink.verify_web_page()
        self.traffic_director.click_veneer_stepper_step(1)
        assert self.load_ink.verify_web_page(raise_e=False) is False
        self.traffic_director.click_veneer_stepper_step(2)
        assert self.load_ink.verify_web_page(raise_e=False) is False, "User should not be moved to Load ink page after clicking on veneer stepper step 2"
        self.traffic_director.click_veneer_stepper_step(3)
        assert self.print_calibration.verify_web_page(raise_e=False) is False, "User should not be moved to Print calibration page after clicking on veneer stepper step 3"
        assert self.scan_calibration.verify_web_page(raise_e=False) is False, "User should not be moved to Scan calibration page after clicking on veneer stepper step 3"
        self.traffic_director.click_next_btn()
        self.load_ink.verify_web_page()
        self.traffic_director.click_veneer_stepper_step(3)
        time.sleep(3)
        self.load_ink.verify_web_page()
        self.td_live_ui.navigate_install_ink_step(self.normalize_profile, self.spec_animation_data)
        self.td_live_ui.navigate_alignment_step(self.normalize_profile, self.spec_animation_data)
        if not self.printer_profile.startswith("trillium"):
            self.td_live_ui.navigate_hp_software_step(self.normalize_profile)
            self.hp_software.click_trouble_installing_get_tips_btn()
            self.hp_software.click_trobleshooting_modal_close_btn()
        else:
            self.hp_software.verify_hp_software_page()
            self.hp_software.verify_install_hp_smart_btn()
        if "paas" not in self.printer_profile:
            self.hp_software.click_install_hp_smart_btn()