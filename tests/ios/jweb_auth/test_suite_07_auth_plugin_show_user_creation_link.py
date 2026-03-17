import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB_AUTH"

toggle_combinations = [[True, True, True, False, True], [True, True, True, False, False]]

class Test_Suite_07_Auth_Plugin_Show_User_Creation_Link_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
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

    @pytest.fixture(scope="function")
    def login_to_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if self.auth_plugin.auth_logged_in_result()["value"] is False:
            self.fc.call_auth_interaction_entry_point("signIn")
            self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
            self.auth_plugin.select_auth_get_token_test()
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
            self.hpid.login(self.username, self.password)
        elif "tokenValue" not in self.auth_plugin.auth_get_token_result():
            self.fc.call_auth_interaction_entry_point("signIn")
            self.auth_plugin.select_auth_get_token_test()

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_account_creation_not_logged_in(self, entry_point, bool_toggles):
        """
        C28715448: Verify by disabling the Account Creation Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Sign In" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting HP Smart sign in page with no account creation button present
        C28715449: Verify by disabling the Account Creation Option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Create Account" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting HP Smart Create Account Page
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        if entry_point == 'signIn':
            assert self.hpid.verify_create_an_account_page() is False
        else:
            assert self.hpid.verify_create_an_account_page() is True
        self.system.select_cancel()

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_02_verify_by_disabling_account_creation_logged_in(self, login_to_hpid, entry_point, bool_toggles):
        """
        C28715448: Verify by disabling the Account Creation Option (User logged in - Sign In)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Sign In" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting existing token to be returned
        C28715449: Verify by disabling the Account Creation Option (User logged in - Create Account)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Create Account" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting existing token to be returned
        """
        old_token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert old_token == self.auth_plugin.auth_get_token_result()['tokenValue']