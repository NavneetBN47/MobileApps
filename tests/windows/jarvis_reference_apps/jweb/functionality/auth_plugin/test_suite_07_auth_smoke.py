import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const
import json

pytest.app_info = "JWEB"

toggle_combinations_required_fresh_token = [[True, True, True, False, True],[ True, True, True, False, False]]

toggle_combinations_disable_require_fresh_token = [[False, True, True, False, True], [False, True, True, False, False],
                                                  [False, True, True, False, True], [False, True, True, False, False]]

toggle_combinations_enable_account_creation = [[False, True, True, True, True],[False, True, True, True, False],
                                             [False, True, True, True, True], [False, True, True, True, False]]

toggle_combinations_no_interaction = [[False, True, False, False, True], [False, True, False, True, True],
                                     [True, True, False, False, True], [True, True, False, True, True],
                                     [False, True, False, False, False], [False, True, False, True, False],
                                     [True, True, False, False, False], [True, True, False, True, False]]

toggle_combinations = [[False, False, False, False, True], [False, False, False, False, False],
                       [False, False, False, True, True], [False, False, False, True, False], 
                       [False, False, True, False, True], [False, False, True, False, False],
                       [False, False, True, True, True], [False, False, True, True, False],
                       [True, False, False, False, True], [True, False, False, False, False],
                       [True, False, False, True, True], [True, False, False, True, False],
                       [True, False, True, False, True], [True, False, True, False, False],
                       [True, False, True, True, True], [True, False, True, True, False]]                                    

class Test_Suite_07_Auth_Smoke(object):
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
        self.auth_plugin.choose_auth_stack("Stage")
        self.auth_plugin.select_auth_provider_option("StratusUsingBrowser")
        self.driver.restart_app()
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()

    def test_01_verify_response_when_send_token_is_disabled_when_user_is_not_logged_in(self):
        """
        C53045151 - Verify response when send token is disabled when user is not logged in
        """
        self.auth_plugin.select_send_token_options(False)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_send_token_disable_result = self.auth_plugin.auth_send_token_disable_result()
        result = json.loads(auth_send_token_disable_result)
        assert result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('interaction_option', ['sign_in', 'create_account'])
    def test_02_verify_status_token_disable_all_options(self, interaction_option):
        """
        C53045032 - Verify status token disable all options
        """
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.nav_to_auth_sign_in_page(interaction_option)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        error_code_result = self.auth_plugin.verify_error_code_result()
        result = json.loads(error_code_result)
        assert result["error"]["code"] == "networkNotAllowed"
    
    def test_03_verify_disabling_network_access_option(self):
        """
        C53045033 - Verify by disabling the Network access option (User has logged in - access token expired) for combination FFFFT
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, True])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"
    
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_required_fresh_token)
    def test_04_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045043: Verify by disabling the "Require fresh token?" option and specific combinations (user not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is False
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()
       
    def test_05_validate_return_stratus_token_by_disabling_all_the_options(self):
        """
        C53045208 - Validate the return of stratus token by disabling all the options
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        result = json.loads(auth_get_token_result)
        assert result["error"]["code"] == "networkNotAllowed"

    def test_06_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_create_account(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(5)
        assert self.hpid.verify_create_an_account_page() is False   
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()
        
    def test_06_1_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is False
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()

    def test_06_2_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is False 
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_interaction)
    def test_07_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account(self, bool_toggles):
        """
        C53045023: Verify disable user interaction option when user has logged in access token expired create account
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        result = json.loads(auth_get_token_result)
        assert result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_08_verify_by_disabling_the_network_access_option(self, bool_toggles):
        """
        C53045014: Verify by disabling the Network aAccess option (User has logged in and the access token expired-Create Account)
            - after navigating to Auth Plugin, disable "Allow Network access," trying the combination defined in toggle_combinations
            - Select "SignIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting networkNotAllowed error
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        result = json.loads(auth_get_token_result)
        assert result["error"]["code"] == "networkNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_09_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045034 and C57736382: Verify that the existing token is returned when "Allow Network Access?" is disabled
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        result = json.loads(auth_get_token_result)
        assert result["error"]["code"] == "networkNotAllowed"

    def test_10_validate_the_return_of_stratus_token_by_enabling_all_the_options_create_account(self):
        """
        C53045159 - Validate the return of stratus token by enabling all the options - Create Account
        - after navigating to Auth Plugin, enable all of the checkboxes under Auth.getToken()
        - select "Create Account" as User Interaction Entry Point
        - click on Test button under Auth.getToken()
        - expecting successful token generation response
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.nav_to_auth_sign_in_page('create_account')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.auth_plugin.select_pop_up_ok_btn()
        self.fc.switch_to_create_account_window(self.web_driver)
        sleep(8)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        account_details = auth_get_token_result["account"]
        assert 'emailAddress' in account_details
        assert "accountId" in account_details
        assert account_details["emailAddress"] != ""
    
    def test_11_validate_the_return_of_stratus_token_by_enabling_all_the_options_with_blank_token_scopes(self):
        """
        C53045158 - Validate the return of stratus token by enabling all the options with blank token scopes
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.send_text_to_scope_textbox(" ")
        self.auth_plugin.nav_to_auth_sign_in_page('sign_in')
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        account_details = auth_get_token_result["account"]
        assert 'emailAddress' in account_details
        assert "accountId" in account_details
        assert account_details["emailAddress"] != ""

    def test_12_verify_that_orgaware_token_replaced_with_orgless_token(self):
        """
        C53045141: Verify that orgaware token replaced with orgless token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        sleep(3)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        sleep(5)

    def test_13_validate_the_return_of_stratus_token_by_enabling_all_the_options_sign_in(self):
        """
        C53045157 - Validate the return of stratus token by enabling all the options - Sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.nav_to_auth_sign_in_page('sign_in')
        sleep(3)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        sleep(5)

    def test_14_verify_the_behavior_when_user_enters_valid_tenant_id(self):
        """
        C53608646 - Verify the behavior when user enters valid tenant id 
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        sleep(2)
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)

    def test_15_verify_the_behavior_when_a_tenant_id_does_not_associated_with_user_id(self):
        """
        C53045150: Verify the behavior when a tenant id does not associated with user id
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)

    def test_16_verify_the_behavior_when_a_tenant_id_does_not_exists_in_orgless_token(self):
        """
        C53045150: Verify the behavior when a tenant id does not exists in orgless token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)

    def test_17_verify_the_behavior_when_a_user_with_multiple_tenant_ids(self):
        """
        C53045148: Verify the behavior when a user with multiple tenant ids
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        sleep(3)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_require_fresh_token)
    def test_18_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is False
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_enable_account_creation)
    def test_18_1_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is True
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_cancel_btn()