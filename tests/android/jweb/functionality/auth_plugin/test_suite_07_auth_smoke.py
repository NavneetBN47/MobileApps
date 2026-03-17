import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.resources.const.web.const import WEBVIEW_URL
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
 
pytest.app_info = "JWEB"

toggle_combinations = [[True, True, True, False, True], [True, True, True, False, False]]

toggle_combinations = [[False, False, False, False, True], [False, False, False, False, False],
                       [False, False, False, True, True], [False, False, False, True, False], 
                       [False, False, True, False, True], [False, False, True, False, False],
                       [False, False, True, True, True], [False, False, True, True, False],
                       [True, False, False, False, True], [True, False, False, False, False],
                       [True, False, False, True, True], [True, False, False, True, False],
                       [True, False, True, False, True], [True, False, True, False, False],
                       [True, False, True, True, True], [True, False, True, True, False]]

toggle_combinations_no_interaction = [[False, True, False, False, True], [False, True, False, True, True],
                                     [True, True, False, False, True], [True, True, False, True, True],
                                     [False, True, False, False, False], [False, True, False, True, False],
                                     [True, True, False, False, False], [True, True, False, True, False]]
                                
toggle_combinations_disable_require_fresh_token = [[False, True, True, False, True],[False, True, True, False, False],
                                                [False, True, True, False, True], [False, True, True, False, False]]

toggle_combinations_enable_account_creation = [[False, True, True, False, True],[False, True, True, True, False],
                                                [False, True, True, True, True], [False, True, True, True, False]]

toggle_combinations_required_fresh_token = [[True, True, True, False, True], [ True, True, True, False, False]]

toggle_combinations_allow_user_interaction = [[False, True, False, False, True], [False, True, False, False, False],
                                             [False, True, False, True, True], [False, True, False, True, False]]

toggle_combinations_allow_user_interaction_1 = [[True, True, False, False, True], [True, True, False, True,True]]

toggle_combinations_allow_user_interaction_2 = [[True, True, False, False, False], [True, True, False, True, False]]

toggle_combinations_user_has_logged_in_user_interaction = [[True, True, False, False, True], [True, True, False, True, True]]

toggle_combinations_disable_network_access = [[False, False, False, False, True], [False, False, False, False, False],
                                              [False, False, False, True, True], [False, False, False, True, False], 
                                              [False, False, True, False, True], [False, False, True, False, False],
                                              [False, False, True, True, True], [False, False, True, True, False],
                                              [True, False, False, False, True], [True, False, False, False, False],
                                              [True, False, False, True, True], [True, False, False, True, False],
                                              [True, False, True, False, True], [True, False, True, False, False],
                                              [True, False, True, True, True], [True, False, True, True, False]]

toggle_combinations_no_refresh = [[False, False, False, False, True], [False, False, False, False, False],
                                 [False, False, False, True, True], [False, False, False, True, False],
                                 [False, False, True, False, True], [False, False, True, False, False],
                                 [False, False, True, True, True], [False, False, True, True, False]]

class Test_Suite_07_Auth_Smoke(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        cls.hpid_url = cls.fc.hpid_url 
       
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

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_auth_plugin(self):
        """
        Launch application and navigate to Auth Plugin
        """
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("auth")
    
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_the_network_access_option(self, bool_toggles):
        """
        C53045014: Verify by disabling the Network aAccess option (User has logged in and the access token expired-Create Account)
            - after navigating to Auth Plugin, disable "Allow Network access," trying the combination defined in toggle_combinations
            - Select "createAccount" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting networkNotAllowed error
        """
        self.auth_plugin.select_auth_logout_test(delay=3)
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn"
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_02_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045034: Verify that the existing token is returned when "Allow Network Access?" is disabled
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_interaction)
    def test_03_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account(self, bool_toggles):
        """
        C53045023: Verify disable user interaction option when user has logged in access token expired create account
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    def test_04_validate_return_stratus_token_by_disabling_all_the_options(self):
        """
        C53045208 - Validate the return of stratus token by disabling all the options
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    def test_05_validate_return_stratus_token_by_enabling_all_the_options(self):
        """
        C53044962 - Validate the return of stratus token by enabling all the options (create account)
        """
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()  
        sleep(12) 
        self.driver.wait_for_context(self.hpid_url, timeout=60) 
        sleep(10)
        self.hpid.create_account()
        sleep(10)
        assert "tokenValue" in self.auth_plugin.auth_get_token_result()

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_require_fresh_token)
    def test_06_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        assert self.hpid.verify_login(self.hpid_username_1, self.hpid_pwd_1) is True
    
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_enable_account_creation)
    def test_06_1_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        assert self.hpid.verify_create_an_account_page() is True

    def test_07_verify_if_the_org_less_token_is_retrived_when_the_user_creates_account_for_the_first_time_tenantid_blank(self):
        """
        C53045139 - Verify if the org-less token is retrived when the user creates account for the first time(tenantId:blank)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(7)
        assert "tenantId" in self.auth_plugin.auth_get_token_result()
        
    def test_08_verify_tenant_id_does_not_exit_org_aware_token_property(self):
        """
        C53045150 - Verify tenant id does not exit org aware token property    
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("8b524804-059f-4f99-a7e4-e003de93b1eb")
        self.auth_plugin.select_auth_get_token_test()
        assert self.hpid.verify_create_an_account_page() is False
    
    def test_08_1_verify_tenant_id_does_not_exit_org_aware_token_property(self):
        """
        C53045150 - Verify tenant id does not exit org aware token property    
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        assert "invalidOption" or "orgwaretokenfailed" in self.auth_plugin.select_auth_get_token_test()
    
    def test_09_verify_that_orgaware_token_replaced_with_orgless_token(self):
        """
        C53045141: Verify if that the org-aware token is replaced with orglesstoken, if the orgless token has not expired for a valid Tenant ID
        """
        self.auth_plugin.control_auth_token_switches([False, True, False, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("2f4981da-9fc2-4dab-8f05-3dfba5b154af")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"
    
    def test_10_verify_the_behavior_when_a_tenant_id_does_not_associated_with_user_id(self):
        """
        C53045149: Verify the behavior when a tenant id does not associated with user id
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("01391dcf-13a2-43c1-bda4-725421850a47")
        self.auth_plugin.select_auth_get_token_test()
        assert self.hpid.verify_create_an_account_page() is False

    def test_10_1_verify_the_behavior_when_a_tenant_id_does_not_associated_with_user_id(self):
        """
        C53045149: Verify the behavior when a tenant id does not associated with user id
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("01391dcf-13a2-43c1-bda4-725421850a47")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        assert "invalidOption" or "orgwaretokenfailed" in self.auth_plugin.select_auth_get_token_test()

    def test_11_verify_by_disabling_the_network_access_option(self):
        """
        C53045033: Validate the return of stratus token by disabling all the options (User has logged in-access token expired)
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, True])
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_required_fresh_token)
    def test_12_verify_by_disabling_account_creation_option(self, bool_toggles):
        """
        C53045043: Verify by disabling the "Require fresh token?" option and specific combinations (user not yet logged in)
        """
        self.auth_plugin.select_auth_logout_test(delay=3)
        assert self.auth_plugin.auth_logout_result()["error"]["code"] == "accountNotLoggedIn"
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        assert self.hpid.verify_hp_id_sign_in() is not False

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction)
    def test_13_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_1)
    def test_13_1_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result() 
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_2)
    def test_13_2_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction)
    def test_13_3_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_1)
    def test_13_4_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result() 
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_2)
    def test_13_5_verify_by_disabling_user_interaction_option(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    def test_14_validate_the_log_out_method_after_signing_or_create_account_set_subscriber(self):
        """
        C53044915 - Validate the log out method after signing or create account- Set Subscriber
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        sleep(5)
        self.auth_plugin.select_auth_logout_test(delay=3)
        assert self.auth_plugin.auth_logout_result() == {}

    def test_15_verify_response_when_send_token_is_disabled_when_user_is_not_logged_in(self):
        """
        C53045151 - Verify response when send token is disabled when user is not logged in
        """
        self.auth_plugin.select_send_token_options("False")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    def test_16_verify_when_user_enters_a_valid_tenant_id_when_the_user_is_not_signed_in(self):
        """
        C53608646 - Verify when user enters a valid tenant id when the user is not signed in
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("2f4981da-9fc2-4dab-8f05-3dfba5b154af")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "invalidOption"
        assert self.auth_plugin.auth_get_token_result()['error']['reason'] == "Tenant ID is not allowed"

    def test_17_validate_return_of_token_by_enabling_all_option_for_create_account(self):
        """
        C53045159 - Verify the return of token by enabling all options for create account
        """
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()  
        sleep(10)
        self.driver.wait_for_context(self.hpid_url, timeout=60)
        sleep(10)
        self.hpid.create_account()
        sleep(8)
        result = self.auth_plugin.auth_get_token_result()
        assert "tokenValue" in result, "Token value not found in the result"

    def test_18_validate_return_of_token_by_enabling_all_option_for_sign_in(self):
        """
        C53045157 - Verify the return of token by enabling all options for sign in
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()  
        sleep(10)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.JWEB, timeout=25)
        result = self.auth_plugin.auth_get_token_result()
        assert "tokenValue" in result, "Token value not found in the result"

    def test_19_validate_return_of_token_by_enabling_all_option_for_sign_in_with_blank_token_scope(self):
        """
        C53045158 - Verify the return of token by enabling all options for sign in with blank token scope
        """
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.send_text_to_scope_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.JWEB, timeout=25)
        result = self.auth_plugin.auth_get_token_result()
        assert "tokenValue" in result, "Token value not found in the result"
    
    def test_20_validate_return_of_access_token(self):
        """
        C53044904: Validate the return of access token after creating account
        """
        self.auth_plugin.select_auth_logout_test()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_user_interaction_entry_point('createAccount')
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
    
    def test_21_validate_the_return_of_access_token_after_signing_with_add_subscriber(self):
        """
        C53044916 - Validate the return of access token after signing with addListener
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.select_token_type_to_request("user")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        sleep(10)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        sleep(10)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == True

    def test_22_validate_the_return_of_access_token_after_signing_with_unsubscribe(self):
        """
        C53044917 - Validate the return of access token after signing in with unsubscribe
        """
        self.auth_plugin.select_auth_remove_listener_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.select_token_type_to_request("user")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        sleep(10)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        sleep(10)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_logout_test()

    def test_23_verify_the_behavior_when_a_user_with_multiple_tenant_ids(self):
        """
        C53045148: Verify the behavior when a user with multiple tenant ids
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        sleep(5)
        self.auth_plugin.send_text_to_tenant_id_textbox("8b524804-059f-4f99-a7e4-e003de93b1eb")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "invalidOption"
        assert self.auth_plugin.auth_get_token_result()['error']['reason'] == "Tenant ID is not allowed"

    def test_24_verify_if_access_token_is_updated_with_new_org_less_token(self):
        """
        C53045140 - Verify if access token is updated with new org less token
        """
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMinimumSecondsUntilExpiration")
        self.auth_plugin.send_text_to_token_lifetime_textbox(36000)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.driver.wait_for_context(self.hpid_url, timeout=50)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        old_token_value = self.auth_plugin.auth_get_token_result()["tokenValue"]
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        assert old_token_value != self.auth_plugin.auth_get_token_result()["tokenValue"]

    def test_25_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_user_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        assert self.hpid.verify_create_an_account_page() is False

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_user_has_logged_in_user_interaction)
    def test_26_verify_by_disabling_the_user_interaction_option_user_has_logged_in_non_expired_access_token_create_account(self, bool_toggles):
        """
        C53045024 - Verify by disabling the User interaction option(User has logged in-non-expired access token-Create account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "userInteractionNotAllowed"

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    def test_27_verify_status_token_disable_all_options(self, entry_point):
        """
        C53045032 - Verify status token disable all options
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_network_access)
    def test_28_verify_by_disabling_the_network_access_option(self, entry_point, bool_toggles):
        """
        C53045017: Verify by disabling the Network Access Option (User has logged in and the access token expired-Create Account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == "networkNotAllowed"

    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_refresh)
    def test_29_verify_disabled_network_non_expired_token_valid_options(self, bool_toggles):
        """
        C53045018: Verify by disabling the Network Access Option (User has logged in - non-expired access token - Create Account)
        """
        self.auth_plugin.select_auth_logout_test()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_user_interaction_entry_point('createAccount')
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.auth_plugin.select_user_interaction_entry_point("createAccount")
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result(), 'Token value not returned from Auth.getToken()'
        assert self.auth_plugin.auth_get_token_result()['tokenValue'] == token, "Token value changed"