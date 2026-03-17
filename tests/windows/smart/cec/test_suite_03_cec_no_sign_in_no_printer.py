import pytest

from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "GOTHAM"
class Test_Suite_03_CEC_No_Sign_In_No_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.cec = cls.fc.fd["cec"]
        cls.hpid = cls.fc.fd["hpid"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_check_cec_jweb_banner(self):
        """
        Check CEC Jweb area (firs time app launch), verify CEC Jweb shows on main UI
        Check the number of engagements in CEC Jweb area, verify only 3 engagements tiles show at a time
        Check the title of CEC Jweb area on main UI , verify "Do More with HP Smart" shows  

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749147
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749152
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749340
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749336
        """
        self.fc.go_home()
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()

    def test_02_check_cec_jweb_area(self):
        """
        Check CEC Jweb area (w/Internet, not signed in, II region, no printer), verify related engagements in CEC Jweb area
        verify DSP and signin/create account related engagements along with Shortcuts related engagement show in CEC Jweb area

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28780942
        """
        if self.stack == "pie":
            pytest.skip("Only check this test point for stage Stack, Skip for pie and production stack.")
        self.home.verify_cec_banner()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
        self.cec.verify_unlock_cloud_features_tile()
        self.cec.verify_never_run_out_save_tile()
        self.cec.verify_shortcuts_save_time_tile()
        if self.cec.verify_do_more_with_hp_smart_screen(raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()

    # Blocked by HPXAPPS-14006: [Stage][Automation Only] Incorrect screen shows after clicking "Unlock cloud features" cec item from CEC Jweb area.
    # @pytest.mark.parametrize("buttons", ["back", "create_account", "sign_in"])
    # def test_03_check_unlock_cloud_features_tile(self, buttons):
    #     """
    #     Click on engagement related to singin/create account on CEC Jweb area, verify user can singing/create HPID account sucessfully

    #     TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28978823
    #     """
    #     self.home.verify_cec_banner()
    #     if self.cec.verify_see_all_btn(raise_e=False):
    #         self.cec.click_see_all()
    #         self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
    #     self.cec.verify_unlock_cloud_features_tile()
    #     self.cec.click_unlock_cloud_features_tile()
    #     self.cec.verify_create_account_or_sign_in_screen()
    #     if buttons == "back":
    #         self.cec.click_back_btn_on_sign_in_or_create_account_screen()
    #         if self.cec.verify_do_more_with_hp_smart_screen(raise_e=False):
    #             self.cec.click_back_btn_do_more_with_hp_smart_screen()
    #     elif buttons == "create_account":
    #         self.cec.click_create_account_btn()
    #         self.fc.handle_web_login(create_account=True)
    #     elif buttons == "sign_in":
    #         self.cec.click_sign_in_btn()
    #         self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
    #     self.home.verify_home_screen(timeout=20)
        
    #     if buttons in ["create_account", "sign_in"]:
    #         assert self.home.verify_logged_in() is True
    #         self.fc.sign_out()
    #         assert self.home.verify_logged_in() is False
    #         self.fc.web_password_credential_delete()
    #         self.fc.restart_hp_smart()
