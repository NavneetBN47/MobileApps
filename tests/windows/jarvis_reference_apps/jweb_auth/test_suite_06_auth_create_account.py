import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations_disable_require_fresh_token = [[False, True, True, False, True],[False, True, True, False, False],
                                                  [False, True, True, False, True], [False, True, True, False, False]]
           
toggle_combinations_enable_account_creation = [[False, True, True, True, True],[False, True, True, True, False],
                                              [False, True, True, True, True], [False, True, True, True, False]]

toggle_combinations_required_fresh_token = [[True, True, True, False, True], [ True, True, True, False, False]]

class Test_Suite_06_Auth_Create_Account(object):

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_disable_require_fresh_token)
    def test_01_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in_C53045040(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False
    
    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_enable_account_creation)
    def test_01_1_verify_by_disabling_the_require_fresh_token_option_user_not_yet_logged_in_C53045040(self, bool_toggles):
        """
        C53045040 - Verify by disabling the Require fresh token option(User not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_create_account_page(self.web_driver) is not False

    @pytest.mark.auth
    def test_02_verify_by_disabling_the_skip_token_refresh_option_C53045200(self):
        """
        C53045200 - Verify by disabling the Skip token refresh option(User not yet logged in) - Sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False
    
    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations_required_fresh_token)
    def test_03_verify_by_disabling_account_creation_option_C53045043(self, bool_toggles):
        """
        C53045043: Verify by disabling the "Require fresh token?" option and specific combinations (user not yet logged in)
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False