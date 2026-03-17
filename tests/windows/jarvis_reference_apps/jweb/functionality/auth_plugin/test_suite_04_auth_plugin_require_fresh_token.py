import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

pytest.app_info = "JWEB"

toggle_combinations = [[False, True, True, False, True],[False, True, True, False, False],
                        [False, True, True, True, True], [False, True, True, True, False]]
 
class Test_Suite_04_Auth_Plugin_Require_Fresh_Token(object):
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
    
    @pytest.mark.parametrize('first_toggles', toggle_combinations)
    def test_01_verify_disabled_require_fresh_token_signin_user_not_logged(self, first_toggles):
        """
        C28711072: Verify by disabling the Require Fresh Token Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Sign In page to load
        """ 
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.control_auth_token_switches(first_toggles)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.select_pop_up_ok_btn()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False    
        self.auth_plugin.select_cancel_btn()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userCanceled'

    @pytest.mark.parametrize('second_toggles', toggle_combinations)
    def test_02_verify_disabled_require_fresh_token_create_account_user_not_logged(self, second_toggles):
        """
        C28711073: Verify by disabling the Require Fresh Token Option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Require Fresh Token" checkbox, and try all checkbox combinations defined in toggle_combinations
            - Select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting Create Account page to load
        """ 
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.control_auth_token_switches(second_toggles)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.select_pop_up_ok_btn()
        assert self.fc.verify_create_account_page(self.web_driver) is not False
        self.auth_plugin.select_cancel_btn()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userCanceled'