import pytest

pytest.app_info = "JWEB_AUTH"

class Test_Suite_07_Auth_Create_Account(object):

    @pytest.mark.auth
    def test_01_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_create_account_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_create_account_page(self.web_driver) is not False
    
    @pytest.mark.auth
    def test_01_1_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False
    
    @pytest.mark.auth
    def test_01_2_verify_disable_account_creation_option_when_user_has_logged_in_non_expired_access_token_sign_in_C53045214(self):
        """
        C53045214 - Verify disable account creation option when user has logged in non-expired access token sign in
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_sign_in_page(self.web_driver) is not False
    
    @pytest.mark.auth
    def test_02_verify_by_disabling_the_account_creation_option_C53045216(self):
        """
        C53045216 - Verify by disabling the Account creation option(User not yet logged in-Create Account)
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_create_account_page(self.web_driver) is not False
    
    @pytest.mark.auth
    def test_03_verify_by_disabling_the_skip_token_refresh_option_C53045201(self):
        """
        C53045201 - Verify by disabling the Skip token refresh option(User not yet logged in) - Create account
        """
        self.auth_plugin.control_auth_token_switches([True, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        assert self.fc.verify_create_account_page(self.web_driver) is not False