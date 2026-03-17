import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, jweb_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        cls.web_driver = utility_web_session
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
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

    def test_01_validate_is_logged_in_out_method_prior_to_logging_in(self):
        """
        C28698046: Validate Sign In Operation Response (After user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and login.
            - click Test button under Auth.isLoggedIn() after having logged in
            - expecting value of True 
        C28698045: Validate Sign In Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and click Test button under Auth.isLoggedIn()
            - expecting value of False, as we aren't logged in
        """
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn"
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == False
    
    def test_02_validate_logged_in_after_logging_in(self):
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
        self.auth_plugin.nav_to_auth_sign_in_page('sign_in')
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"]
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}
    
    @pytest.mark.parametrize('interaction_option', ['sign_in', 'create_account'])
    def test_03_verify_status_token_disable_all_options(self, interaction_option):
        """
        C28714873: Validate the return of stratus token by disabling all the options - Sign In
            - after navigating to Auth Plugin, disable all of the checkboxes under Auth.getToken()
            - select "SignIn" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting networkNotAllowedError 
        C28714874: Validate the return of stratus token by disabling all the options - Create Account
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.nav_to_auth_sign_in_page(interaction_option)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == 'networkNotAllowed'
    
    @pytest.mark.parametrize('interaction_option', ['sign_in', 'create_account'])
    def test_04_verify_closing_browser_result(self, interaction_option):
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
        self.auth_plugin.nav_to_auth_sign_in_page(interaction_option)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.select_pop_up_ok_btn()
        self.fc.close_the_window(self.web_driver)
        self.auth_plugin.select_cancel_btn()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userCanceled"