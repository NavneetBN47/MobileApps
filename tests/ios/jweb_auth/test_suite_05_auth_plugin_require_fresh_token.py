import pytest
from time import sleep
from MobileApps.resources.const.android.const import WEBVIEW_URL

pytest.app_info = "JWEB_AUTH"

toggle_combinations = [[False, True, True, False, True], [False, True, True, False, False],
                       [False, True, True, True, True], [False, True, True, True, False]]

class Test_Suite_05_Auth_Plugin_Require_Fresh_Token(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.hpid_url = cls.fc.hpid_url 
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
    
    @pytest.fixture(scope="class", autouse=True)
    def navigate_to_auth_plugin(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    @pytest.fixture(scope="function", autouse=True)
    def close_safari_window(self):
        self.system.select_cancel(raise_e=False)
    
    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('toggle_combination', toggle_combinations)
    def test_01_verify_disabled_require_fresh_token_signin_user_not_logged(self, toggle_combination, entry_point):
        """
        C28711072: Verify by disabling the Require Fresh Token Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all toggle_combinations for other the options
            - Select "Sign In" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting user to be directed to Sign In page
        C28711073: Verify by disabling the Require Fresh Token Option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all toggle_combinations for other the options
            - Select "Create Account" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting user to be directed to Create Account page
        """ 
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(toggle_combination)
        self.auth_plugin.select_auth_get_token_test() 
        if entry_point == "signIn":
            self.driver.wait_for_context(self.hpid_url, timeout=50)
            assert self.hpid.verify_hp_id_sign_in() is not False
        else:
            self.driver.wait_for_context(self.hpid_url, timeout=50)
            assert self.hpid.verify_create_an_account_page() is not False
