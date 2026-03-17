import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_disabling_the_user_interaction_option = [[False, True, False, False, True], [False, True, False, False, False],
                                                            [False, True, False, True, True], [False, True, False, True, False], 
                                                            [True, True, False, False, True], [True, True, False, False, False], 
                                                            [True, True, False, True, True], [True, True, False, True, False]]

toggle_combinations_allow_user_interaction_1 = [[True, True, False, False, True], [True, True, False, True,True]]

class Test_Suite_01_Auth_Error_Code(object):

    @pytest.mark.auth
    def test_01_verify_response_when_send_token_is_disabled_when_user_is_not_logged_in_C53045151(self):
        """
        C53045151 - Verify response when send token is disabled when user is not logged in
        """
        self.auth_plugin.select_send_token_options(False)
        self.auth_plugin.select_auth_get_token_test()
        auth_send_token_disable_result = self.auth_plugin.auth_send_token_disable_result()
        assert auth_send_token_disable_result["error"]["code"] == "userInteractionNotAllowed"
    
    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_1)
    def test_02_verify_by_disabling_user_interaction_option_C53045021(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_allow_user_interaction_1)
    def test_02_1_verify_by_disabling_user_interaction_option_C53045021(self, bool_toggles):
        """
        C53045021: Verify by disabling the User interaction option(User has logged in-non-expired access token)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"

    @pytest.mark.auth
    def test_03_validate_return_stratus_token_by_disabling_all_the_options_C53045208(self):
        """
        C53045208 - Validate the return of stratus token by disabling all the options
        """
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "networkNotAllowed"

    @pytest.mark.auth        
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disabling_the_user_interaction_option)
    def test_04_verify_by_disabling_the_user_interaction_option_user_not_yet_logged_in_create_account_C53045022(self, bool_toggles):
        """
        C53045022 - Verify by disabling the User interaction option(User not yet logged in- Create Account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"