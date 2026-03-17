import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

pytest.app_info = "JWEB"
 
entry_points = ["sign_in", "create_account"]
 
class Test_Suite_05_Auth_Plugin_Skip_Token_Refresh(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, jweb_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        cls.web_driver = utility_web_session
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.stack = request.config.getoption("--stack")
        cls.home.click_maximize()
 
        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]
   
    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
        self.auth_plugin.choose_auth_stack(self.stack)
        self.auth_plugin.select_auth_provider_option("StratusUsingBrowser")
        self.driver.restart_app()
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
   
    @pytest.fixture()
    def login_to_hpid(self):
        self.fc.login_to_hpid(self.username, self.password, self.web_driver)
 
    @pytest.fixture()
    def logout_from_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if self.auth_plugin.auth_logged_in_result()["value"] is not False:
            self.auth_plugin.select_auth_logout_test()

    @pytest.mark.parametrize('entry', entry_points)
    def test_01_verify_by_disabling_skip_token_refresh_user_not_logged(self, entry, logout_from_hpid):
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
        if entry == "sign_in":
            self.auth_plugin.select_auth_get_token_test()
            self.auth_plugin.select_pop_up_ok_btn()
            assert self.fc.verify_sign_in_page(self.web_driver) is not False
            self.auth_plugin.select_cancel_btn()
            assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userCanceled'
        elif entry == "create_account":
            self.auth_plugin.select_auth_get_token_test()
            self.auth_plugin.select_pop_up_ok_btn()
            assert self.fc.verify_create_account_page(self.web_driver) is not False
            self.auth_plugin.select_cancel_btn()
            assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userCanceled'

    @pytest.mark.parametrize('entry', entry_points)
    def test_02_verify_by_disabling_skip_token_refresh_user_logged_token_not_expired(self, entry, login_to_hpid):
        """
        C28711746: Verify by disabling the Skip Token Refresh Option (User has logged in - Sign In)
            - user is signed in, disable "Skip Token Refresh" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting existing unexpired token to be returned
        C28711747: Verify by disabling the Skip Token Refresh Option (User has logged in - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
            - expecting existing unexpired token to be returned
        """
        if self.auth_plugin.auth_get_token_result() is False:
            token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry)
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        refreshed_token = self.auth_plugin.get_refreshed_token(token)
        assert refreshed_token == token
