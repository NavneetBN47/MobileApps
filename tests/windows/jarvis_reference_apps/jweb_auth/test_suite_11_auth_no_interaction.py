import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_no_interaction = [[False, True, False, False, True], [False, True, False, True, True],
                                     [True, True, False, False, True], [True, True, False, True, True],
                                     [False, True, False, False, False], [False, True, False, True, False],
                                     [True, True, False, False, False], [True, True, False, True, False]]

class Test_Suite_11_Auth_No_Interaction(object):

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_no_interaction)
    def test_01_verify_disable_user_interaction_option_when_user_has_logged_in_access_token_expired_create_account_C53045023(self, bool_toggles):
        """
        C53045023: Verify disable user interaction option when user has logged in access token expired create account
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "userInteractionNotAllowed"