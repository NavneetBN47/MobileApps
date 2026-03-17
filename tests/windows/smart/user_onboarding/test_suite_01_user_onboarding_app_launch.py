import pytest

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_01_User_Onboarding_App_Launch(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_sign_up_flow(self):
        """
        User onboarding Sign Up flow

        Expected Result:
        Verify flow can be completed without any issue
        Verify the "Exit Setup"/ Home button is not seen during the user onboarding flow
        Verify the user is signed when land on the Main UI
        Verify the "Exit Setup"/ "Home" button is not seen during the user onboarding flow

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997916
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176710
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176717
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997919
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997921
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176713
        """
        self.fc.go_home(create_account=True)

        assert self.home.verify_logged_in() is True

        self.fc.check_consent_appinstanceid_log()

        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
    
    def test_02_sign_in_flow(self):
        """
        User onboarding sign in flow

        Expected Result:
        Verify flow can be completed without any issue
        Verify the "Exit Setup"/ Home button is not seen during the user onboarding flow
        Verify the user is signed when land on the Main UI
        Verify email verification does not show as Email account is used before to sign in via HP Smart

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997915
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176712
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176714
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])

        assert self.home.verify_logged_in() is True

        self.fc.check_consent_appinstanceid_log()

