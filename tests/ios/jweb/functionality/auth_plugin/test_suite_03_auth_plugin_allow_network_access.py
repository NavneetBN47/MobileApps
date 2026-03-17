import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

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

class Test_Suite_03_Auth_Plugin_Allow_Network_Access_Validation(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # define flows
        cls.system = cls.fc.fd["system"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        # get test account data
        test_account = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]
        cls.hpid_username = test_account["username"]
        cls.hpid_pwd = test_account["password"]
        # reset and launch the app
        cls.fc.flow_load_home_screen()

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.system.select_cancel(raise_e=False, timeout=1)
        self.fc.navigate_to_auth_plugin()
    
    @pytest.fixture()
    def login_to_hpid(self):
        self.fc.login_to_hpid(self.hpid_username, self.hpid_pwd)

    @pytest.fixture()
    def logout_from_hpid(self):
        self.fc.logout_from_hpid()
    
    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
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
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result(), 'Token value not returned from Auth.getToken()'
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token, "Token value changed"
    
    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_refresh)
    def test_02_verify_disabled_network_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698060: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Network Accession," trying the combination defined in toggle_combinations_refresh
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting existing unexpired token to be returned
        C28698067: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result(), 'Token value not returned from Auth.getToken()'
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token, "Token value changed"

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', all_toggle_combinations)
    def test_04_verify_disabled_network_non_user_logged_valid_options(self, entry_point, bool_toggles, logout_from_hpid):
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
        assert 'error' in self.auth_plugin.auth_get_token_result(), "Auth.getToken() failed to return an error"
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'networkNotAllowed', "Auth.getToken() failed to return userInteractionNotAllowed"
