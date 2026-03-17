import pytest

from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_User_Onboarding_Tiles_Mobile_Fax(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.softfax_home = cls.fc.fd["softfax_home"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")


    @pytest.mark.parametrize("buttons", ["create_account", "sign_in"])
    def test_01_close_sign_in_up_dialog(self, buttons):
        """
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997911
        """
        self.fc.go_home()

        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()

        if buttons == "create_account":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
            self.fc.verify_hp_id_sign_in_up_page(is_sign_up=True)
        else:
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
            self.fc.verify_hp_id_sign_in_up_page()

        self.fc.close_hp_id_sign_in_up_page()

    @pytest.mark.parametrize("buttons", ["sign_in", "close", "create_account"])
    def test_02_user_onboarding_flow_via_mobile_fax_tile(self, buttons):
        """
        Click "Mobile Fax" tile without signed in, verify OWS UCDE value prop shows for Mobile Fax
        (+)Create Account via any locked tile, verify flow continues and the user is onboarded
        Sign in via any Tile, verify flow continues and user is onboarded
        Click "Close" button on the OWS value prop, verify user navigates to Home Page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731302
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731497
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731496
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997910
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)
        self.fc.go_home()

        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()

        if buttons == "create_account":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
            self.fc.handle_web_login(create_account=True)
            self.softfax_landing.verify_mobile_fax_landing_screen(timeout=60)
            self.home.select_navbar_back_btn()
        elif buttons == "sign_in":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
            self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
            self.softfax_home.verify_mobile_fax_home_screen()
            self.home.select_navbar_back_btn()
        elif buttons == "close":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
            self.home.verify_home_screen()

        if buttons in ["create_account", "sign_in"]:
            assert self.home.verify_logged_in() is True
            self.fc.check_consent_appinstanceid_log()
            self.fc.sign_out()
            assert self.home.verify_logged_in() is False
