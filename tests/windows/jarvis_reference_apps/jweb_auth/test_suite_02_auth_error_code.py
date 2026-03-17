import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_user_has_logged_in_user_interaction = [[True, True, False, False, True], [True, True, False, True, True]]

class Test_Suite_02_Auth_Error_Code(object):

    @pytest.mark.auth        
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_user_has_logged_in_user_interaction)
    def test_01_verify_by_disabling_the_user_interaction_option_user_has_logged_in_non_expired_access_token_create_account_C53045024(self, bool_toggles):
        """
        C53045024 - Verify by disabling the User interaction option(User has logged in-non-expired access token-Create account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"