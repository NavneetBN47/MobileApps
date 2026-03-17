import pytest
from MobileApps.resources.const.android.const import WEBVIEW_URL

pytest.app_info = "JWEB"

class Test_Suite_05_Auth_Plugin_Skip_Token_Refresh(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        cls.hpid_url = cls.fc.hpid_url 
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.console = cls.fc.fd["console"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    def test_01_verify_by_disabling_skip_token_refresh_user_not_logged(self, entry_point):
        """
        C28711736: Verify by disabling the Skip Token Refresh Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Skip Token Refresh" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Sign In page to load
        C28711737: Verify by disabling the Skip Token Refresh Option (User not yet logged in - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point. Expecting Create Account Page to load
        """
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("auth")
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        if entry_point == "signIn":
            self.driver.wait_for_context(self.hpid_url, timeout=50)
            assert self.hpid.verify_hp_id_sign_in() is not False
        else:
            self.driver.wait_for_context(self.hpid_url, timeout=50)
            assert self.hpid.verify_create_an_account_page() is not False