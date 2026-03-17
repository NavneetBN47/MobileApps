import pytest

pytest.app_info = "JWEB_AUTH"

class Test_Suite_10_Auth_Login_Event_change(object):

    @pytest.mark.auth
    def test_01_verify_set_subscriber_when_tenant_id_is_blank_for_stratus(self, navigate_to_auth_plugin_stratus):
        """
        C58654099 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_02_verify_set_subscriber_when_user_exchange_token_from_one_org_another_stratus(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):
        """
        C58654051 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids

    @pytest.mark.auth
    def test_03_verify_payload_in_set_subscriber_event_matches_account_specification(self, navigate_to_auth_plugin_stratus):
        """
        C58654102 - Verify that the payload in the set subscriber event matches the account specification
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"

    @pytest.mark.auth
    def test_04_verify_set_event_subscriber_result_when_user_logout(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_blank_tenant_id):
        """
        C58654103 - Verify the set subscriber result when the user logs out
        """
        self.auth_plugin.select_auth_logout_test()
        auth_logged_in_result =  self.auth_plugin.verify_logout_successful_message()
        assert "Logout Successful" in auth_logged_in_result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"

    @pytest.mark.auth
    def test_05_verify_the_set_subscriber_result_when_user_login_first_time(self, navigate_to_auth_plugin_stratus):
        """
        C58654041 - Verify the set subscriber result when user login first time
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_06_verify_payload_in_set_event_subscriber_method_matches_account_specification_first_login(self, navigate_to_auth_plugin_stratus):
        """
        C58654042 - Verify the payload in setEventSubscriber method matches Account specification-First Login
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        given_name = result["currentAccount"]["givenName"]
        assert given_name == "Admin 1"
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"
        account_id = result["currentAccount"]["accountId"]
        assert account_id == "y48s8jiq97ykimt44jsoda3tsoousbrg"

    @pytest.mark.auth
    def test_07_verify_payload_in_set_event_subscriber_method_matches_account_specification(self, navigate_to_auth_plugin_stratus):
        """
        C58654043 - Verify the payload in setEventSubscriber method matches Account specification
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        given_name = result["currentAccount"]["givenName"]
        assert given_name == "Admin 1"
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"

    @pytest.mark.auth
    def test_08_verify_the_set_subscriber_result_when_user_exchanges_the_token_for_specific_org(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_blank_tenant_id):    
        """
        C58654044 - Verify set event subscriber result- when user exchanges the token for a specific org
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("91547a10-4a36-45b7-b423-8b2baac97976")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        current_account_tenant_id = result_details["currentAccount"]["tenantId"]
        assert current_account_tenant_id == None
        previous_account_tenant_id = result_details["previousAccount"]
        assert previous_account_tenant_id == None

    @pytest.mark.auth
    def test_09_verify_the_behavior_of_a_valid_tenant_id_with_non_expired_org_aware_token(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):
        """
        C58654121 - Verify the behavior of a valid tenant ID with non-expired org-aware token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids
        auth_token = self.auth_plugin.auth_get_token_result()
        old_token_value = auth_token["tokenValue"]
        self.auth_plugin.select_auth_get_token_test()
        verify_auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in verify_auth_get_token_result
        old_token_value != verify_auth_get_token_result["tokenValue"]

    @pytest.mark.auth        
    def test_10_verify_the_response_after_clicking_on_test_twice_under_gettoken_when_token_got_exchanged_from_orgaware_to_orgless(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):    
        """
        C58654100 - Verify the response after clicking on Test twice under getToken(), when token got exchanged from orgaware to orgless
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        previous_account_tenant_id = result["previousAccount"]
        assert previous_account_tenant_id == None
    
    @pytest.mark.auth
    def test_11_verify_the_behaviour_when_tenant_id_exists_with_valid_org_aware_token(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):
        """
        C58654104 - Verify the behaviour when tenant ID exists with valid org-aware token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result
        assert result["tokenOptions"]["tenantID"] in self.expected_tenant_ids
    
    @pytest.mark.auth
    def test_12_verify_if_error_is_displayed_when_there_is_no_access_token_stored_for_a_tenant_id_wrong_tenant_id(self, navigate_to_auth_plugin_stratus):
        """
        C58654105 - Verify if error is displayed when there is no access token stored for a tenant ID ( wrong tenant ID)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username_1, self.password_1, self.web_driver)
        auth_get_tenant_id_error= self.auth_plugin.auth_get_tenant_id_error()
        assert "This usually indicates that the tenantId is incorrect" in str(auth_get_tenant_id_error)
        assert auth_get_tenant_id_error["error"]["code"] == "invalidOption"

    @pytest.mark.auth            
    def test_13_verify_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):
        """
        C58654101 - [Stratus] Verify set event subscriber result- when user logout(orgaware token)
        """
        self.auth_plugin.select_auth_logout_test()
        auth_logged_in_result =  self.auth_plugin.verify_logout_successful_message()
        assert "Logout Successful" in auth_logged_in_result
        result = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        given_name = result["currentAccount"]["givenName"]
        assert given_name == "Admin 1"
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"
    
    @pytest.mark.auth
    def test_14_restart_the_application_and_request_the_access_token(self, navigate_to_auth_plugin_stratus, login_to_hpid_with_valid_tenant_id):
        """
        C58654050 - [Stratus] Restart the application and request the access token.
        """
        self.driver.restart_app()
        self.home.select_top_nav_button("jweb_nav_btn")
        self.home.select_reference_btn()
        self.home.select_plugins_tab_from_menu()
        self.home.select_plugin_from_home("Auth")
        self.auth_plugin.select_auth_get_token_test()
        result = self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        assert 'tokenValue' in result

    @pytest.mark.auth
    def test_15_verify_the_set_subscriber_result_when_user_login_first_time(self, navigate_to_auth_plugin_one_cloud, login_to_hpid_with_blank_tenant_id):    
        """
        C58654106 - [oneCloud] Verify the set subscriber result when user login first time
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        email_address = account_details["currentAccount"]["emailAddress"]
        assert email_address == self.username_1
        given_name = account_details["currentAccount"]["givenName"]
        assert given_name == "Admin 1"
        family_name = account_details["currentAccount"]["familyName"]
        assert family_name == "stage 1"
        tenant_id = account_details["currentAccount"]["tenantId"]
        assert tenant_id == None
        previous_account_tenant_id = account_details["previousAccount"]
        previous_account_tenant_id == None
    
    @pytest.mark.auth
    def test_16_verify_the_payload_in_seteventsubscriber_method_matches_account_specification_first_login(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654107 - [oneCloud] Verify the payload in setEventSubscriber method matches Account specification-First Login
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        assert "stratusId" not in account_details
        assert "tenantId " != "tenantID"
        email_address = account_details["currentAccount"]["emailAddress"]
        assert email_address == "qahpsmart@gmail.com"
        given_name = account_details["currentAccount"]["givenName"]
        assert given_name == "Qahp"
        family_name = account_details["currentAccount"]["familyName"]
        assert family_name == "Smart"
        previous_account = account_details["previousAccount"]
        previous_account == "null"
    
    @pytest.mark.auth
    def test_17_verify_the_set_subscriber_result_when_user_exchanges_the_token_from_1_org_to_other_org(self, navigate_to_auth_plugin_one_cloud):
        """
        C58654115 - Verify set event subscriber result- when user exchanges the token from 1 org to other org
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id_1)
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        current_account = account_details["currentAccount"]
        assert current_account["tenantId"] == "ac1f1f75-2371-44b3-8b15-a0b6771422df"
        previous_account = account_details["previousAccount"]
        assert previous_account is None

    @pytest.mark.auth
    def test_18_verify_the_set_subscriber_result_when_user_exchanges_the_token_from_1_org_to_tenantid_blank(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654116 - Verify set event subscriber result- when user exchanges the token from 1 org to tenantId<blank>
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id_1)
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        current_account = account_details["currentAccount"]
        assert current_account["tenantId"] == "ac1f1f75-2371-44b3-8b15-a0b6771422df"
        previous_account = account_details["previousAccount"]
        assert previous_account is None

    @pytest.mark.auth
    def test_19_verify_the_response_after_clicking_on_test_twice_under_get_token_when_token_got_exchanged_from_orgware_to_orgless(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654117 - [oneCloud]Verify the response after clicking on Test twice under getToken(),
                    when token got exchanged from orgaware to orgless
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        current_account = account_details["currentAccount"]
        assert current_account["tenantId"] == "ac1f1f75-2371-44b3-8b15-a0b6771422df"
        previous_account = account_details["previousAccount"]
        assert previous_account is None

    @pytest.mark.auth
    def test_20_verify_the_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654118 - Verify set event subscriber result- when user logout(orgaware token)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.select_auth_logout_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        current_account = account_details["currentAccount"]
        assert current_account["tenantId"] == "ac1f1f75-2371-44b3-8b15-a0b6771422df"
        previous_account = account_details["previousAccount"]
        assert previous_account is None

    @pytest.mark.auth
    def test_21_verify_the_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654119 - Verify set event subscriber result- when user logout(orgless token)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.select_auth_logout_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        current_account = account_details["currentAccount"]
        assert current_account["accountId"] == "4b4ec6df-9d6e-4cb5-bee2-ef2c4e927fa8"
        previous_account = account_details["previousAccount"]
        assert previous_account is None

    @pytest.mark.auth
    def test_22_restart_the_application_and_request_the_access_token(self, navigate_to_auth_plugin_one_cloud):
        """
        C58654114 - Restart the application and request the access token.
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        previous_account_tenant_id = account_details["currentAccount"]["tenantId"]
        self.driver.restart_app()
        self.auth_plugin.select_logout_btn()
        self.home.select_top_nav_button("jweb_nav_btn")
        self.home.select_reference_btn()
        self.home.select_plugins_tab_from_menu()
        self.home.select_plugin_from_home("Auth")
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        result_details_2 = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details_2 = result_details_2
        current_account_tenant_id = account_details_2["currentAccount"]["tenantId"]
        assert current_account_tenant_id == previous_account_tenant_id
    
    @pytest.mark.auth
    def test_23_verify_set_event_subscriber_result_when_user_exchanges_the_token_for_a_specific_org(self, navigate_to_auth_plugin_one_cloud, login_to_hpid_with_blank_tenant_id):
        """
        C58654108 - [oneCloud] Verify set event subscriber result- when user exchanges the token for a specific org
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result("expand_auth_event_dropdown_1")
        account_details = result_details
        account_id = account_details["currentAccount"]["accountId"]
        assert account_id == "cf950d1d-f0d8-4261-a42d-9dda7c5c5b03"