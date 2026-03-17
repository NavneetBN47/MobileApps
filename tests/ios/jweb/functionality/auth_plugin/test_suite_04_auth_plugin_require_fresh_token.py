import pytest
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB"

toggle_combinations = [[False, True, True, False, True], [False, True, True, False, False],
                        [False, True, True, True, True], [False, True, True, True, False]]

class Test_Suite_04_Auth_Plugin_Require_Fresh_Token(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup, request):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # define flows
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        # reset and launch the app
        cls.fc.flow_load_home_screen()

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.system.select_cancel(raise_e=False, timeout=1)
        self.fc.navigate_to_auth_plugin()

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('toggle_combination', toggle_combinations)
    def test_01_verify_disabled_require_fresh_token_signin_user_not_logged(self, toggle_combination, entry_point):
        """
        C28711072: Verify by disabling the Require Fresh Token Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Sign In page to load
        C28711073: Verify by disabling the Require Fresh Token Option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Create Account page to load
        """ 
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(toggle_combination)
        self.auth_plugin.select_auth_get_token_test() 
        if entry_point == "signIn":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            assert self.hpid.verify_hp_id_sign_in(), "Sign In page is not loaded"
            self.system.select_cancel()
        else:
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            assert self.hpid.verify_create_an_account_page(), "Create Account page is not loaded"
            self.system.select_cancel()
