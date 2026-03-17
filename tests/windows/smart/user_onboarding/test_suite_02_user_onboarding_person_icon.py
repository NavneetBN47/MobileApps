import pytest

from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_User_Onboarding_Person_Icon(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_sign_up_via_create_account_btn(self):
        """
        User onboarding Sign Up flow (via click "Create Account" button on the person icon flyout)
        Click "Create Account" button on the person icon flyout, verify HPID Sign UP dialog opens in a separate window

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176814
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176715
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176716
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176718
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176719
        """
        self.fc.go_home()
        self.fc.create_account()
        assert self.home.verify_logged_in() is True
        self.fc.check_consent_appinstanceid_log()

        self.fc.sign_out()
        assert self.home.verify_logged_in() is False

    def test_02_sign_in_via_sign_in_btn(self):
        """
        User onboarding Sign in flow (via clicking the "Sign in" button on the person icon flyout)
        *Check on person icon (new user singed in), verify "Manage HP Account" shows on login flyout
        *Check on person icon (new user not signed in), verify "Manage HP Account" doesn't show on login flyout
        Sign out (new user), click on person icon, verify "Manage HP Account" doesn't show on login flyout

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176813
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300350
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300352
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300357  
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)
        self.fc.go_home()

        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        assert self.home.verify_logged_in() is True
        self.fc.check_consent_appinstanceid_log()

        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
    
    def test_03_sign_in_via_already_have_account_link(self):
        """
        User onboarding Sign in flow (via clicking the "Already have account?" link on HPID sign up dialog)

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28722847
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)
        self.fc.go_home()

        self.fc.sign_in(self.login_info["email"], self.login_info["password"], from_sign_up=True)
        assert self.home.verify_logged_in() is True
        self.fc.check_consent_appinstanceid_log()

