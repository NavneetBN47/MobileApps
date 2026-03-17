import pytest

pytest.app_info = "JWEB_AUTH"

class Test_Suite_08_Auth_Account_Creation(object):

    @pytest.mark.auth
    def test_01_validate_return_stratus_token_by_enabling_all_the_options_C53044962(self):
        """
        C53044962 - Validate the return of stratus token by enabling all the options (create account)
        """
        self.home.select_top_nav_button("tests_nav_btn")
        self.auth_plugin.select_create_account_btn()
        self.fc.switch_to_create_account_window(self.web_driver)
        assert self.auth_plugin.verify_orgless_token_contents() is True
    
    @pytest.mark.auth
    def test_02_validate_the_return_of_stratus_token_by_enabling_all_the_options_create_account_C53045159(self):
        """
        C53045159 - Validate the return of stratus token by enabling all the options - Create Account
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        assert 'emailAddress' in auth_get_token_result
        assert "accountId" in auth_get_token_result
        assert auth_get_token_result["emailAddress"] != ""
    
    @pytest.mark.auth
    def test_03_verify_org_less_token_is_retrived_when_the_user_creates_account_for_the_first_time_tenantId_blank_C53045139(self):
        """
        C53045139 - Verify if the org-less token is retrived when the user creates account for the first time(tenantId:blank)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        assert 'emailAddress' in auth_get_token_result
        assert "accountId" in auth_get_token_result
        assert auth_get_token_result["emailAddress"] != ""
    
    @pytest.mark.auth
    def test_04_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        assert 'emailAddress' in auth_get_token_result
        assert "accountId" in auth_get_token_result
        assert auth_get_token_result["emailAddress"] != ""