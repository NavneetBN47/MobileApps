import pytest

pytest.app_info = "JWEB_AUTH"

class Test_Suite_03_Auth_Sign_In(object):

    @pytest.mark.auth
    def test_01_verify_that_orgaware_token_replaced_with_orgless_token_C53045141(self):
        """
        C53045141: Verify that orgaware token replaced with orgless token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("91547a10-4a36-45b7-b423-8b2baac97976")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        old_token_value = auth_get_token_result["tokenValue"]
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in auth_get_token_result
        old_token_value != auth_get_token_result["tokenValue"]

    @pytest.mark.auth
    def test_02_validate_the_return_of_stratus_token_by_enabling_all_the_options_sign_in_C53045157(self):
        """
        C53045157 - Validate the return of stratus token by enabling all the options - Sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        account_details = auth_get_token_result["account"]
        assert 'emailAddress' in account_details
        assert "accountId" in account_details
        assert account_details["emailAddress"] == self.username_1

    @pytest.mark.auth
    def test_03_validate_the_return_of_stratus_token_by_enabling_all_the_options_with_blank_token_scopes_C53045158(self):
        """
        C53045158 - Validate the return of stratus token by enabling all the options with blank token scopes
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.send_text_to_scope_textbox(" ")
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()  
        account_details = auth_get_token_result["account"]
        assert 'emailAddress' in account_details
        assert "accountId" in account_details
        assert account_details["emailAddress"] == self.username_1

    @pytest.mark.auth
    def test_04_validate_the_log_out_method_after_signing_or_create_account_set_subscriber_C53044915(self):
        """
        C53044915 - Validate the log out method after signing or create account- Set Subscriber
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.select_auth_logout_test()
        auth_logged_out_result =  self.auth_plugin.verify_logout_successful_message()
        assert "Logout Successful" in auth_logged_out_result

    @pytest.mark.auth
    def test_05_validate_the_logged_in_method_after_signing_or_create_account_set_subscriber_C53044916(self):
        """
        C53044916 -Validate the logged in method after signing or create account- Set Subscriber
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.select_auth_logged_in_test()
        auth_get_token_result = self.auth_plugin.get_auth_is_logged_in_result()
        assert auth_get_token_result["value"] == True 

    @pytest.mark.auth
    def test_06_validate_the_logged_out_method_after_signing_or_create_account_unsubscribe_C53044917(self):
        """
        C53044917 - Validate the logged out method after signing or create account - Unsubscribe
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.select_set_unsubscriber_btn()
        self.auth_plugin.select_auth_logout_test()
        auth_logged_out_result =  self.auth_plugin.verify_logout_successful_message()
        assert "Logout Successful" in auth_logged_out_result