import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from time import sleep

pytest.app_info = "JWEB_AUTH"

class Test_Suite_06_Auth_Plugin_Skip_Token_Refresh(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        # Define flows
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
    
    @pytest.fixture(scope="class", autouse=True)
    def navigate_to_auth_plugin(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
    
    @pytest.fixture()
    def login_to_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if not self.auth_plugin.auth_logged_in_result()["value"]:
            self.fc.call_auth_interaction_entry_point("signIn")
            self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
            self.auth_plugin.select_auth_get_token_test()
            self.driver.wait_for_context(self.fc.hpid_url)
            self.hpid.login(self.username, self.password)
            sleep(5)

    @pytest.mark.parametrize('entry', ["signIn", "createAccount"])
    def test_01_verify_by_disabling_skip_token_refresh_user_not_logged(self, entry):
        """
        C28711736: Verify by disabling the Skip Token Refresh Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Skip Token Refresh" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Sign In page to load
        C28711737: Verify by disabling the Skip Token Refresh Option (User not yet logged in - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point. Expecting Create Account Page to load
        """
        self.fc.call_auth_interaction_entry_point(entry)
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        if entry == "signIn":
            assert self.hpid.verify_hp_id_sign_in() is not False
            self.system.select_cancel()
        else:
            assert self.hpid.verify_create_an_account_page() is not False
            self.system.select_cancel()

    @pytest.mark.parametrize('entry', ["signIn", "createAccount"])
    def test_02_verify_by_disabling_skip_token_refresh_user_logged_token_not_expired(self, entry, login_to_hpid):
        """
        C28711746: Verify by disabling the Skip Token Refresh Option (User has logged in - Sign In)
            - user is signed in, disable "Skip Token Refresh" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting existing Token to be returned
        C28711747: Verify by disabling the Skip Token Refresh Option (User has logged in - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point. expecting existing Token to be returned
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry)
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        refreshed_token = self.auth_plugin.auth_get_token_result()['tokenValue']
        assert refreshed_token == token
