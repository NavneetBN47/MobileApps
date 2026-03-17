import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.resources.const.web.const import WEBVIEW_URL
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Auth_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        cls.hpid_url = cls.fc.hpid_url 
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.chrome = cls.fc.fd["chrome"]
        cls.console = cls.fc.fd["console"]

        test_account_1 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]
        cls.hpid_username_1 = test_account_1["username"]
        cls.hpid_family_name_1 = test_account_1["family_name"]
        cls.hpid_given_name_1 = test_account_1["given_name"]
        cls.hpid_pwd_1 = test_account_1["password"]
        cls.hpid_user_id_1 = test_account_1["user_id"]

        test_account_2 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.hpid_username_2 = test_account_2["username"]
        cls.hpid_family_name_2 = test_account_2["family_name"]
        cls.hpid_given_name_2 = test_account_2["given_name"]
        cls.hpid_pwd_2 = test_account_2["password"]
        cls.hpid_user_id_2 = test_account_2["user_id"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_auth_plugin(self):
        """
        Launch application and navigate to Auth Plugin
        """
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("auth")

    def test_01_verify_auth_signin_logout_result_before_signin(self):
        """
        C28698045: Validate Sign In Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, enable send token option, select type as user, and click Test button under Auth.isLoggedIn()
            - expecting value of False, as we aren't logged in
        C28698047: Validate Log Out Operation Response (Before user is signed in)
            - after navigating to Auth Plugin, click Test button under Auth.logout()
            - expecting error: "accountNotLoggedIn, No user is available to logout"
        """
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == False
        self.auth_plugin.select_auth_logout_test(delay=3)
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn"

    def test_02_verify_auth_signin_logout_result_after_signin(self):
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
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.JWEB, timeout=25)
        assert 'error' not in self.auth_plugin.auth_get_token_result(), "HPID Login returned error {}".format(self.auth_plugin.auth_get_token_result()['error'])
        self.auth_plugin.select_auth_logged_in_test(scroll=True)
        assert self.auth_plugin.auth_logged_in_result()["value"]

        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        assert self.auth_plugin.auth_logout_result() == {}

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    def test_03_verify_status_token_disable_all_options(self, entry_point):
        """
        C28714873: Validate the return of stratus token by disabling all the options - Sign In
            - after navigating to Auth Plugin, disable all of the checkboxes under Auth.getToken()
            - select "SignIn" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting networkNotAllowedError 
        C28714874: Validate the return of stratus token by disabling all the options - Create Account
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "networkNotAllowed"

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    def test_04_verify_closing_browser_result(self, entry_point):
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
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        self.chrome.click_webview_close_btn()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userCanceled"