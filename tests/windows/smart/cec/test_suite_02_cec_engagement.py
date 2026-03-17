import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_CEC_Engagement(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.cec = cls.fc.fd["cec"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_to_main_ui_login_add_printer(self):
        """
        Precondition: Login HP account and add printer to Main Page.
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_check_shortcuts_engagement(self):
        """
        Click on Shortcuts engagement tile on CEC Jweb area, verify Shortcuts page shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749326
        """
        if self.stack == 'pie':
            pytest.skip("Shortcut Save time CEC item is only available for stage Stack")
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)

        self.cec.verify_shortcuts_save_time_tile()
        self.cec.click_shortcuts_save_time_tile()
        self.cec.verify_shortcut_save_time_screen()
        self.cec.click_back_btn()
        self.cec.verify_shortcuts_save_time_tile()
        self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()

    def test_03_check_supplies_engagement(self):
        """
        Click on engagement related to supplies on CEC Jweb area, verify DSP page shows
        Check the background of CEC Jweb area, verify it is transparent	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749324
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749154
        """
        if self.stack == 'pie':
            pytest.skip("Never Run out save CEC item is only available for Stage Stack")
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()
        self.cec.verify_never_run_out_save_tile()
        self.cec.click_never_run_out_save_tile()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.wait_for_new_window(timeout=30)
            self.web_driver.add_window("get_supplies")
            sleep(2)
            self.web_driver.switch_window("get_supplies")
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')

        self.home.verify_home_screen()

        check_string = 'Launching DSP flow from the CEC engagement tile'
        self.fc.check_gotham_log(check_string)
