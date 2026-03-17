import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

pytest.app_info = "JWEB"

all_toggle_combinations = [[False, False, False, False, True], [False, False, False, False, False],
                        [False, False, False, True, True], [False, False, False, True, False],
                        [False, False, True, False, True], [False, False, True, False, False],
                        [False, False, True, True, True], [False, False, True, True, False],
                        [True, False, False, False, True], [True, False, False, False, False],
                        [True, False, False, True, True], [True, False, False, True, False],
                        [True, False, True, False, True], [True, False, True, False, False],
                        [True, False, True, True, True], [True, False, True, True, False]]
toggle_combinations_no_refresh = [[False, False, False, False, True], [False, False, False, False, False],
                        [False, False, False, True, True], [False, False, False, True, False],
                        [False, False, True, False, True], [False, False, True, False, False],
                        [False, False, True, True, True], [False, False, True, True, False]]
toggle_combinations_refresh = [[True, False, False, False, True], [True, False, False, False, False],
                        [True, False, False, True, True], [True, False, False, True, False],
                        [True, False, True, False, True], [True, False, True, False, False],
                        [True, False, True, True, True], [True, False, True, True, False]]

entry_points = ["sign_in", "create_account"]

class Test_Suite_03_Auth_Plugin_Allow_Network_Access_Validation(object):
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
    
    @pytest.mark.parametrize('entry_point', entry_points)
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_refresh)
    def test_01_verify_disabled_network_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698060: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Network Accession," trying the combination defined in toggle_combinations_no_refresh
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting existing token to be returned
        C28698067: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token
    
    @pytest.mark.parametrize('entry_point', entry_points)
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_refresh)
    def test_02_verify_disabled_network_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698060: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Network Accession," trying the combination defined in toggle_combinations_refresh
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting networkNotAllowed error code to be returned
        C28698067: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.get_refreshed_token(token) == token

    @pytest.mark.parametrize('entry_point', entry_points)
    @pytest.mark.parametrize('bool_toggles', all_toggle_combinations)
    def test_03_verify_disabled_network_non_user_logged_valid_options(self, entry_point, bool_toggles):
        """
        C28698058: Verify by disabling the Network Access Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Allow Network Access" checkbox, and try all toggle_combinations for the other options
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting networkNotAllowed error
        C28698063: Verify by disabling the Network Access Option (User not yet logged in - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result['error']['code'] == 'networkNotAllowed'
        