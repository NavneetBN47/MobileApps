import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_05_Auth_Plugin_Skip_Token_Refresh(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # define flows
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
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
            assert self.hpid.verify_hp_id_sign_in(), "Sign In page is not loaded"
        else:
            assert self.hpid.verify_create_an_account_page(), "Create Account page is not loaded"
        self.system.select_cancel()

    @pytest.mark.parametrize('entry', ["signIn", "createAccount"])
    def test_02_verify_by_disabling_skip_token_refresh_user_logged_token_not_expired(self, entry, login_to_hpid):
        """
        C28711746: Verify by disabling the Skip Token Refresh Option (User has logged in - Sign In)
            - user is signed in, disable "Skip Token Refresh" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting existing unexpired token to be returned
        C28711747: Verify by disabling the Skip Token Refresh Option (User has logged in - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point. expecting existing unexpired token to be returned
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry)
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result(), 'Token value not returned from Auth.getToken()'
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token, "Token value changed"
