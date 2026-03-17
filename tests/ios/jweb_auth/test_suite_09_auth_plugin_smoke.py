from time import sleep
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB_AUTH"

toggle_combinations_disable_require_fresh_token = [[True, True, False, False, True, False], [True, True, False, False, False, False],
                                                   [True, True, True, False, True, False], [True, True, True, False, False, False,]]

toggle_combinations_no_interaction = [[False, True, False, False, True], [False, True, False, True, True],
                                     [True, True, False, False, True], [True, True, False, True, True]]

toggle_combinations_token_expired = [[False, True, False, False, False], [False, True, False, True, False]]
toggle_combinations_token_refreshed = [[True, True, False, False, False], [True, True, False, True, False]]

toggle_combinations_required_fresh_token = [[True, True, False, False, True, False], [ True, True, False, False, False, False]]

toggle_combinations_allow_network_access = [[False, False, False, False, True, False], [False, False, False, False, False, False],
                                            [False, False, True, False, True, False], [False, False, True, False, False, False],
                                            [False, True, False, False, True, False], [False, True, False, False, False, False],
                                            [False, True, True, False, True, False], [False, True, True, False, False, False]]

toggle_combinations = [[False, False, False, False, True], [False, False, False, False, False],
                                [False, False, False, True, True], [False, False, False, True, False], 
                                [False, False, True, False, True], [False, False, True, False, False],
                                [False, False, True, True, True], [False, False, True, True, False],
                                [True, False, False, False, True], [True, False, False, False, False],
                                [True, False, False, True, True], [True, False, False, True, False],
                                [True, False, True, False, True], [True, False, True, False, False],
                                [True, False, True, True, True], [True, False, True, True, False]]

class Test_Suite_09_Auth_Plugin_Smoke(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.jweb_auth_settings = cls.fc.fd["jweb_auth_settings"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_auth_plugin(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    @pytest.fixture()
    def reset_app(self):
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    @pytest.fixture()
    def close_app(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    def test_01_validate_return_of_token_by_enabling_all_option_for_create_account(self):
        """
        C53045159 - Verify the return of token by enabling all options for create account
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.create_account()
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        account_details = result["account"]
        assert "accountId" in account_details

    def test_02_validate_return_of_token_by_enabling_all_option_for_sign_in(self):
        """
        C53045157 - Verify the return of token by enabling all options for sign in
        """
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        account_details = result["account"]
        assert "accountId" in account_details
        assert account_details["emailAddress"] == self.username
        assert account_details["familyName"] == "Smart"

    def test_03_validate_return_of_token_by_enabling_all_option_for_sign_in_with_blank_token_scope(self):
        """
        C53045158 - Verify the return of token by enabling all options for sign in with blank token scope
        """
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.send_text_to_scope_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        account_details = result["account"]
        assert "accountId" in account_details
        assert account_details["emailAddress"] == self.username
        assert account_details["familyName"] == "Smart"

    def test_04_verify_when_user_enters_a_valid_tenant_id_when_the_user_is_not_signed_in(self, reset_app):
        """
        C53608646 - Verify when user enters a valid tenant id when the user is not signed in
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    def test_05_verify_tenant_id_does_not_exit_org_aware_token_property(self, reset_app):
        """
        C53045150 - Verify tenant id does not exit org aware token property    
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"
    
    def test_06_verify_response_when_send_token_is_disabled_when_user_is_not_logged_in(self, reset_app):
        """
        C53045151 - Verify response when send token is disabled when user is not logged in
        """
        self.auth_plugin.select_send_token_options(False)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"
       
    def test_07_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_get_token_test()
        assert self.hpid.verify_create_an_account_page() is False

    def test_07_1_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result

    def test_07_2_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_create_account(self, reset_app):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_get_token_test()
        assert self.hpid.verify_create_an_account_page() is True

    def test_07_3_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_create_account(self, reset_app):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.hpid.verify_create_an_account_page() is True
        
    def test_07_4_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_with_no_option(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        
    def test_07_5_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_with_no_option(self, reset_app):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result

    def test_08_verify_tenant_id_does_not_exit_org_aware_token_property(self, reset_app):
        """
        C53045149 - Verify tenant id does not exit org aware token property  
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("01391dcf-13a2-43c1-bda4-725421850a47")
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_interaction)
    def test_09_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account(self, bool_toggles, reset_app):
        """
        C53045023 - Verify disable user interaction option when user has logged in access token expired create account
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_token_expired)
    def test_09_1_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account(self, bool_toggles):
        """
        C53045023 - Verify disable user interaction option when user has logged in access token expired create account
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_token_refreshed)
    def test_09_2_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account(self, bool_toggles):
        """
        C53045023 - Verify disable user interaction option when user has logged in access token expired create account
        """
        self.fc.call_auth_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    def test_10_verify_if_access_token_is_updated_with_new_org_less_token(self):
        """
        C53045140 - Verify if access token is updated with new org less token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMinimumSecondsUntilExpiration")
        self.auth_plugin.send_text_to_token_lifetime_textbox(36000)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        old_token_value = self.auth_plugin.auth_get_token_result()["tokenValue"]
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        assert old_token_value != self.auth_plugin.auth_get_token_result()["tokenValue"]

    def test_11_validate_return_of_stratus_token_by_disabling_all_options(self, reset_app):
        """
        C53045208: Validate the return of stratus token by disabling all the options
            - Open the Jarvis Auth example on your IOS device
            - Click on Settings symbol
            - Disable all the options
            - Click on Done
            - Click on + symbol next to settings in the app
            - expecting networkNotAllowedError 
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.select_allow_network_access_toggle(False)
        self.jweb_auth_settings.select_show_account_creation_link_toggle(False)
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        result = self.auth_plugin.get_displayed_content()
        assert "Error: networkNotAllowed" in result
    
    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_12_verify_by_disabling_the_network_access_option(self, entry_point, bool_toggles, reset_app):
        """
        C53045014: Verify by disabling the Network aAccess option (User has logged in and the access token expired-Create Account)
            - after navigating to Auth Plugin, disable "Allow Network access," trying the combination defined in toggle_combinations
            - Select "SignIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting networkNotAllowed error
        C53045017: Verify by disabling the Network Access Option (User has logged in and the access token expired-Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "networkNotAllowed"

    def test_13_verify_that_orgaware_token_replaced_with_orgless_token(self, reset_app):
        """
        C53045141: Verify if that the org-aware token is replaced with orglesstoken, if the orgless token has not expired for a valid Tenant ID
            - In the Jarvis Auth example
            - Go to Auth
            - Select user under Auth.getToken()
            - Enable Allow Network Access, Allow User Interaction, Show Account Creation Link
            - Enable TenantID to exchange the token and input a valid ID (2f4981da-9fc2-4dab-8f05-3dfba5b154af)
            - Click on Test
            - Remove tenantId
            - Click on Test
            - Validate that the org-aware token is replaced with orgless token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userInteractionNotAllowed"
    
    def test_14_validate_the_return_of_response_after_signing_to_retrieving_getdevicetoken(self, close_app):
        """"
        C53044966 - Validate the return of response after signing in to retrieving getDeviceToken
        """""
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles([True,True,True,True,True,False])
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.create_account()
        sleep(5)
        self.home.select_accounts_back_button()
        self.home.select_accounts_chevron_btn()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.select_allow_user_interaction_toggle(False)
        self.jweb_auth_settings.select_setting_done_button()
        self.auth_plugin.select_get_device_token_chevron_btn()
        self.jweb_auth_settings.update_get_device_token_resource_textfield()
        self.jweb_auth_settings.select_get_token_btn()
        assert self.jweb_auth_settings.verify_get_device_token_response() == "RESPONSE: Request returned status code 409"
    
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_require_fresh_token)
    def test_15_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles, reset_app):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles(bool_toggles)
        self.jweb_auth_settings.select_start_on_create_account_toggle(False)
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        sleep(5)
        assert self.hpid.verify_hp_id_sign_in(), "Sign in"
    
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_require_fresh_token)
    def test_15_1_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles, reset_app):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles(bool_toggles)
        self.jweb_auth_settings.select_start_on_create_account_toggle(True)
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        sleep(5)
        assert self.hpid.verify_create_an_account_page(), "Create an account"
    
    def test_16_verify_if_the_org_less_token_is_retrived_when_the_user_creates_account_for_the_first_time_tenantid_blank(self, reset_app):
        """
        C53045139 - Verify if the org-less token is retrived when the user creates account for the first time(tenantId:blank)
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "userInteractionNotAllowed"

    def test_17_validate_the_return_of_access_token_after_signing_with_add_listener(self, reset_app):
        """
        C53044902 - Validate the return of access token after signing in with addListener
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.select_token_type_to_request("user")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_required_fresh_token)
    def test_18_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045043: Verify by disabling the "Require fresh token?" option and specific combinations
            - Open the Jarvis Auth example app
            - Click on the Settings symbol
            - Disable the "Require fresh token?" option
            - Try disabling the following combinations:
                - Disable "Start on account creation"
            - Click on Done
            - Click on the + symbol next to settings in the app
            - The app should redirect to the HP Smart app sign-in page
            - On the sign-in page, account creation should not be present
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles(bool_toggles)
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        sleep(5)
        assert not self.hpid.verify_create_an_account_page(), "Account creation link is present on the sign-in page"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_network_access)   
    def test_19_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045034: Verify that the existing token is returned when "Allow Network Access?" is disabled
            - Open the Jarvis Auth example app
            - Click on the account name (logged in previously) displayed under Accounts
            - Click on the settings icon in the top-right corner inside the logged-in account
            - Disable the "Allow Network Access?" option and try disabling the following combinations:
                - [Specify combinations here if needed]
            - Click on Done
            - Under Actions, click on "Get Token" to see the response
            - Validate that the existing token is returned"
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles([True, True, True, False, False, False])
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        self.hpid.login(self.username, self.password)
        self.home.select_accounts_back_button()
        self.home.select_accounts_chevron_btn()
        self.auth_plugin.select_get_token_chevron_btn()
        self.auth_plugin.select_qahp_smart_back_button()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles(bool_toggles)
        self.jweb_auth_settings.select_setting_done_button()
        self.auth_plugin.select_get_token_chevron_btn()
        self.auth_plugin.verify_get_token_contents() is True 

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_network_access)
    def test_20_verify_by_disabling_the_network_access_option(self, bool_toggles, reset_app):
        """
        C53045032: Validate the return of stratus token by disabling all the options (User not yet logged in-Disable account creation link)
            - Open the Jarvis Auth example on your IOS device
            - Click on Settings symbol
            - Disable all the options
            - Click on Done
            - Click on + symbol next to settings in the app
            - expecting networkNotAllowedError 
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles(bool_toggles)
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        result = self.auth_plugin.get_displayed_content()
        assert "Error: networkNotAllowed" in result

    def test_21_verify_by_disabling_the_network_access_option(self):
        """
        C53045033: Validate the return of stratus token by disabling all the options (User has logged in-access token expired)
            Verify that "networkNotAllowed" error is displayed when "Allow Network Access?" is disabled
            - Open the Jarvis Auth example app
            - Click on the account name (logged in previously) displayed under Accounts
            - Click on the settings icon in the top-right corner inside the logged-in account
            - Disable the "Allow Network Access?" option and try disabling the combinations
            - Click on Done
            - Under Actions, click on "Get Token" to see the response
            - Validate that the "networkNotAllowed" error is displayed
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles([False, False, False, False, True, False])
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        result = self.auth_plugin.get_displayed_content()
        assert "Error: networkNotAllowed" in result

    def test_22_validate_return_of_stratus_token_by_enabling_all_the_options(self):
        """
        C53044962: Validate the return of stratus token by enabling all the options (create account)
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        self.jweb_auth_settings.control_auth_toggles([True, True, True, True, False, False])
        self.jweb_auth_settings.select_setting_done_button()
        self.home.select_top_bar_button('Add', raise_e=False)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.create_account()
        sleep(5)
        self.home.select_accounts_back_button()
        self.auth_plugin.verify_get_account_content() is True