import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB_AUTH"

toggle_combinations_not_logged = [[False, True, False, False, True], [False, True, False, False, False],
                                  [False, True, False, True, True], [False, True, False, True, False],
                                  [True, True, False, False, True], [True, True, False, False, False],
                                  [True, True, False, True, True], [True, True, False, True, False]]
toggle_combinations_refresh = [[True, True, False, False, False], [True, True, False, True, False]]
toggle_combinations_no_refresh = [[False, True, False, False, True], [False, True, False, False, False],
                                  [False, True, False, True, True], [False, True, False, True, False]]
toggle_combinations_no_interaction = [[True, True, False, False, True], [True, True, False, True, True]]

class Test_Suite_03_Auth_Plugin_Allow_User_Interaction(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]
        cls.scope = test_account["scope"]
        cls.resource = test_account["resource"]

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
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
            self.hpid.login(self.username, self.password)

    @pytest.fixture()
    def logout_from_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if self.auth_plugin.auth_logged_in_result()["value"]:
            self.auth_plugin.select_auth_logout_test()

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_refresh)
    def test_01_verify_disabled_user_interaction_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698072: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Allow User Interaction," use the toggle_combinations_no_refresh to select login options
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting existing token to be returned
        C28698079: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_refresh)
    def test_02_verify_disabled_user_interaction_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698072: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Allow User Interaction," use the toggle_combinations_refresh to select login options
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting a existing unexpired token to be returned
        C28698079: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "createAccount" is our User Interaction Entry Point
        """
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_interaction)
    def test_03_verify_disabled_user_interaction_non_expired_token_valid_options(self, entry_point, bool_toggles, login_to_hpid):
        """
        C28698072: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Sign In)
            - after navigating to Auth Plugin, disable "Allow User Interaction," use the toggle_combinations_no_interaction to select login options
            - Select "signIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting userInteractionNotAllowed error
        C28698079: Verify by disabling the User Interaction Option (User has logged in - non-expired access token - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userInteractionNotAllowed'

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_not_logged)
    def test_05_verify_disabled_user_interaction_user_not_logged_valid_options(self, entry_point, bool_toggles, logout_from_hpid):
        """
        C28698070: Verify by disabling the User Interaction Option (User Not Yet Signed In - Sign In)
            - after navigating to Auth Plugin, disable "Allow User Interaction," trying the combination defined in toggle_combinations
            - Select "SignIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting userInteractionNotAllowed error
        C28698073: Verify by disabling the User Interaction Option (User Not Yet Signed In - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userInteractionNotAllowed'
