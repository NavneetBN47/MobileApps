import pytest

from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "GOTHAM"
class Test_Suite_04_CEC_Sign_In_No_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.cec = cls.fc.fd["cec"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info_hp_plus = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")
        cls.login_info_ucde = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic")

    def test_01_check_cec_jweb_area_hp_plus(self):
        """
        Check CEC Jweb area (w/ Internet, signedin advanced account, II region, no printer), verify related engagements in CEC Jweb area

        -verify Shortcuts related engagement shows in CEC Jweb area
        -verify DSP related engagement shows in CEC Jweb area

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28780951
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info_hp_plus["email"], self.login_info_hp_plus["password"])

        if self.stack == "pie":
            pytest.skip("Only check this test point for stage Stack, Skip for pie and production stack.")
        self.home.verify_cec_banner()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)  
        # GOTH-25062:DSP related engagement "Never run out & save"" is missing in CEC Jweb area after sign in accounts (HP+ & ucde). 
        self.cec.verify_never_run_out_save_tile()
        self.cec.verify_shortcuts_save_time_tile()
        if self.cec.verify_do_more_with_hp_smart_screen(raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()

        self.fc.sign_out()

    def test_02_restore_hp_smart(self):
        """
        Restore HP Smart for next test case
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

    def test_03_check_cec_jweb_area_ucde(self):
        """
        Check CEC Jweb area (w/Internet, signedin non advanced account, II region, no printer), verify related engagements in CEC Jweb area 

        -verify CEC Jweb area shows with DSP related engagement along with Shortcuts related engagement

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28874327
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info_ucde["email"], self.login_info_ucde["password"])

        if self.stack == "pie":
            pytest.skip("Only check this test point for stage Stack, Skip for pie and production stack.")
        self.home.verify_cec_banner()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
        # GOTH-25062:DSP related engagement "Never run out & save"" is missing in CEC Jweb area after sign in accounts (HP+ & ucde). 
        self.cec.verify_never_run_out_save_tile()
        self.cec.verify_shortcuts_save_time_tile()
        if self.cec.verify_do_more_with_hp_smart_screen(raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()