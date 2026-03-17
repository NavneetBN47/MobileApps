import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from time import sleep

pytest.app_info = "JWEB_AUTH"

class Test_Suite_02_Basic_Functionality(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.system = cls.fc.fd["system"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    def test_01_validate_is_logged_in_method_prior_to_logging_in(self):
        """
        C28698045: Validate Sign In Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and click Test button under Auth.isLoggedIn()
            - expecting value of False, as we aren't logged in
        """
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == False

    def test_02_validate_is_logged_out_method_prior_to_logging_in(self):
        """
        C28698046: Validate Sign In Operation Response (After user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and login.
            - click Test button under Auth.isLoggedIn() after having logged in
            - expecting value of True 
        """
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn"

    def test_03_validate_logged_in_after_logging_in(self):
        """
        C28698047: Validate Log Out Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, click Test button under Auth.logout()
            - expecting error: "accountNotLoggedIn, No user is available to logout"
        C28698048: Validate Log Out Operation Response (After user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and login.
            - click on Test button under Auth.logout()
            - expecting an empty object returned denoting a successful logout operation
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_user_interaction_entry_point('signIn')
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.hpid.login(self.username, self.password)
        sleep(5)
        self.auth_plugin.select_auth_logged_in_test()
        sleep(5)
        assert self.auth_plugin.auth_logged_in_result()["value"]
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}

    @pytest.mark.parametrize('interaction_option', ["signIn", "createAccount"])
    def test_04_verify_status_token_disable_all_options(self, interaction_option):
        """
        C28714873: Validate the return of stratus token by disabling all the options - Sign In
            - after navigating to Auth Plugin, disable all of the checkboxes under Auth.getToken()
            - select "SignIn" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting networkNotAllowedError 
        C28714874: Validate the return of stratus token by disabling all the options - Create Account
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_user_interaction_entry_point(interaction_option)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "networkNotAllowed"

    @pytest.mark.parametrize('interaction_option', ["signIn", "createAccount"])
    def test_05_verify_closing_browser_result(self, interaction_option):
        """
        C28698051: Validate the response by closing the browser before Signing In
            - after navigating to Auth Plugin, enable all of the checkboxes under Auth.getToken()
            - select "SignIn" as User Interaction Entry Point, and click Test under Auth.getToken()
            - close the browser once the app redirects to the login page
            - expecting userCanceledLogin error
        C28698052: Validate the response by closing the browser before Creating Account
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_user_interaction_entry_point(interaction_option)
        self.auth_plugin.select_auth_get_token_test()
        self.system.select_cancel()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userCanceled"