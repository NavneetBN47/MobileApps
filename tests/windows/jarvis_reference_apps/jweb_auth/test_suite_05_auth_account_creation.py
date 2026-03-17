import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_no_refresh = [[False, True, False, False, True], [False, True, False, False, False],
                                  [False, True, False, True, True], [False, True, False, True, False]]

toggle_combinations_refresh = [[True, True, False, False, False], [True, True, False, True, False]]

toggle_combinations_required_fresh_token = [[True, True, True, False, True], [ True, True, True, False, False]]

class Test_Suite_05_Auth_Sign_In(object):

    @pytest.mark.auth
    def test_01_validating_sign_in_operation_response_before_user_sign_in_C53045153(self):
        """
        C53045153 - Validating sign in operation response(Before user sign in)
        """
        self.auth_plugin.select_auth_logged_in_test()
        auth_get_token_result = self.auth_plugin.get_auth_is_logged_in_result_false()
        assert auth_get_token_result["value"] == False

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_refresh)
    def test_02_verify_by_disabling_user_interaction_option_C53045021(self, bool_toggles, login_to_hpid_with_blank_tenant_id):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_refresh)
    def test_02_1_verify_by_disabling_user_interaction_option_C53045021(self, bool_toggles, login_to_hpid_with_blank_tenant_id):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        token = auth_get_token_result['tokenValue']
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert auth_get_token_result['tokenValue'] == token

    @pytest.mark.auth
    def test_03_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_03_1_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_04_verify_by_disabling_the_account_creation_option_C53045215(self):
        """
        C53045215 - Verify by disabling the Account creation option(User not yet logged in-sign in)
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False

    @pytest.mark.auth
    def test_05_validating_the_response_by_closing_the_browser_before_sign_in_C53045209(self):
        """
        C53045209 - Validating the response by closing the browser before sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_create_account_page(self.web_driver) is not False
        self.auth_plugin.select_cancel_btn()
        assert self.auth_plugin.verify_user_canceled_error_code_result()['error']['code'] == 'userCanceled'