import pytest

pytest.app_info = "JWEB_AUTH"

class Test_Suite_04_Auth_Sign_In(object):

    @pytest.mark.auth
    def test_01_verify_the_behavior_when_user_enters_valid_tenant_id_C53608646(self):
        """
        C53608646 - Verify the behavior when user enters valid tenant id
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id_1)
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids

    @pytest.mark.auth
    def test_02_verify_if_access_token_is_updated_with_new_org_less_token_C53045140(self, login_to_hpid_with_valid_tenant_id):
        """
        C53045140 - Verify if access token is updated with new org less token
        """
        self.auth_plugin.select_token_lifetime_option_btn()
        self.auth_plugin.select_token_lifetime_options("preferredMinimumSecondsUntilExpiration")
        self.auth_plugin.set_time_interval_for_token("36000")
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_03_verify_the_behavior_when_a_user_with_multiple_tenant_ids_C53045148(self):
        """
        C53045148: Verify the behavior when a user with multiple tenant ids
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id_1)
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids

    @pytest.mark.auth
    def test_04_verify_the_behavior_when_a_tenant_id_does_not_associated_with_user_id_C53045149(self, login_to_hpid_with_valid_tenant_id):
        """
        C53045149: Verify the behavior when a tenant id does not associated with user id
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id_1)
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids

    @pytest.mark.auth
    def test_05_verify_the_behavior_when_a_tenant_id_does_not_exists_in_orgless_token_C53045150(self):
        """
        C53045150: Verify the behavior when a tenant id does not associated with user id
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username_1, self.password_1, self.web_driver)
        auth_get_tenant_id_error = self.auth_plugin.auth_get_tenant_id_error()
        assert "This usually indicates that the tenantId is incorrect" in str(auth_get_tenant_id_error)
        assert auth_get_tenant_id_error["error"]["code"] == "invalidOption"