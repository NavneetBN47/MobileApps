import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB"

toggle_combinations = [[True, True, True, False, True], [True, True, True, False, False]]

class Test_Suite_06_Auth_Plugin_Show_User_Creation_Link_Option(object):
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

    @pytest.fixture(scope="function")
    def login_to_hpid(self):
        self.fc.login_to_hpid(self.hpid_username, self.hpid_pwd)

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_account_creation_not_logged_in(self, entry_point, bool_toggles):
        """
        C28715448: Verify by disabling the Account creation option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Show Account Creation" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Sign In page to load, Account Creation link should not be present
        C28715449: Verify by disabling the Account creation option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Show Account Creation" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Create Account page to load
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        if entry_point == 'signIn':
            assert not self.hpid.verify_create_an_account_page(), "Create an account link should not be present"
        else:
            assert self.hpid.verify_create_an_account_page(), "Create an account link should be present"
        self.system.select_cancel()

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_02_verify_by_disabling_account_creation_logged_in(self, login_to_hpid, entry_point, bool_toggles):
        """
        C28715496: verify by disabling the Account creation option (User has logged in - Sign In)
            - after navigating to Auth Plugin, disable "Show Account Creation" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - existing token gets returned
        C28715497: verify by disabling the Account creation option (User has logged in - Create Account)
            - after navigating to Auth Plugin, disable "Show Account Creation" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - existing token gets returned
        """
        old_token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert old_token == self.auth_plugin.auth_get_token_result()['tokenValue']