import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # define flows
        cls.system = cls.fc.fd["system"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        # get test account data
        test_account_1 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]
        cls.hpid_username_1 = test_account_1["username"]
        cls.hpid_pwd_1 = test_account_1["password"]
        # reset and launch the app
        cls.fc.flow_load_home_screen()

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.system.select_cancel(raise_e=False, timeout=1)
        self.fc.navigate_to_auth_plugin()

    def test_01_validate_is_logged_in_method_prior_to_logging_in(self):
        """
        C28698045: Validate Sign In Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and click Test button under Auth.isLoggedIn()
            - expecting value of False, as we aren't logged in
        """
        self.auth_plugin.select_auth_logged_in_test()
        assert not self.auth_plugin.auth_logged_in_result()["value"], "Auth.isLoggedIn() returned True"
    
    def test_02_validate_is_logged_out_method_prior_to_logging_in(self):
        """
        C28698047: Validate Log Out Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, click Test button under Auth.logout()
            - expecting error: "accountNotLoggedIn" as No user is available to logout
        """
        self.auth_plugin.select_auth_logout_test()
        assert 'error' in self.auth_plugin.auth_logout_result(), "Auth.logout() failed to return an error"
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn", "Auth.logout() failed to return accountNotLoggedIn"

    def test_03_validate_logged_in_after_logging_in(self):
        """
        C28698046: Validate Sign In Operation Response (After user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and login.
            - click Test button under Auth.isLoggedIn() after having logged in
            - expecting value of True 
        C28698048: Validate Log Out Operation Response (After user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and login.
            - click on Test button under Auth.logout()
            - expecting an empty object returned denoting a successful logout operation
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_user_interaction_entry_point('signIn')
        self.auth_plugin.select_auth_get_token_test()
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"], "Auth.isLoggedIn() returned False after logging in"
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}, "Auth.logout() failed to log out user"

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
        assert 'error' in self.auth_plugin.auth_get_token_result(), "Auth.getToken() failed to return an error"
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "networkNotAllowed", "Auth.getToken() failed to return networkNotAllowed"

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
        assert 'error' in self.auth_plugin.auth_get_token_result(), "Auth.getToken() failed to return an error"
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userCanceled", "Auth.getToken() failed to return userCanceled"
