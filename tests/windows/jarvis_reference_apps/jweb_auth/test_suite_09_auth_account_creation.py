import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_user_has_logged_in_non_expired_access_token = [[False, True, False, False, True], [False, True, False, False, False],
                                                                   [False, True, False, True, True], [False, True, False, True, False]]
                                                                   
toggle_combinations_existing_token_is_retrieved = [[True, True, False, False, False], [True, True, False, True, False]]

class Test_Suite_09_Auth_Account_Creation(object):

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_existing_token_is_retrieved)
    def test_01_verify_by_disabling_the_user_interaction_option_user_has_logged_in_non_expired_access_token_create_account_C53045024(self, bool_toggles, logout_from_hpid, login_to_hpid_with_blank_tenant_id):
        """
        C53045024 - Verify by disabling the User interaction option(User has logged in-non-expired access token-Create account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in auth_get_token_result
    
    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_user_has_logged_in_non_expired_access_token)
    def test_01_1_verify_by_disabling_the_user_interaction_option_user_has_logged_in_non_expired_access_token_create_account_C53045024(self, bool_toggles, logout_from_hpid, login_to_hpid_with_blank_tenant_id):
        """
        C53045024 - Verify by disabling the User interaction option(User has logged in-non-expired access token-Create account)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in auth_get_token_result