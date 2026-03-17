import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
import MobileApps.resources.const.windows.const as w_const
import json
import logging

pytest.app_info = "JWEB"

class Test_Suite_08_Auth_Plugin_Login_Event_Scenarios(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, jweb_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        cls.web_driver = utility_web_session
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.stack = request.config.getoption("--stack")
        cls.home.click_maximize()
 
        test_account = cls.fc.get_jweb_login_event_test_data(cls.stack)
        cls.username = test_account["account_01"]["username"]
        cls.password = test_account["account_01"]["password"]
        cls.tenant_id = test_account["account_01"]["tenant_id"]
        cls.username_1 = test_account["account_02"]["username"]
        cls.password_1 = test_account["account_02"]["password"]

    @pytest.fixture()
    def login_to_hpid(self):
        self.fc.login_to_hpid(self.username, self.password, self.web_driver)
     
    @pytest.fixture(scope="function")
    def navigate_to_auth_plugin_stratus(self):
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
        self.auth_plugin.choose_auth_stack("Stage")
        self.auth_plugin.select_auth_provider_option("StratusUsingBrowser")
        self.driver.restart_app()
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
 
    @pytest.fixture(scope="function")
    def navigate_to_auth_plugin_one_cloud(self):
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
        self.auth_plugin.choose_auth_stack("Stage")
        self.auth_plugin.select_auth_provider_option("OneCloudUsingBrowser")
        self.driver.restart_app()
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
    
    def test_01_restart_the_application_and_request_the_access_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654050 - [Stratus] Restart the application and request the access token.
        """
        self.auth_plugin.select_set_subscriber_btn
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("91547a10-4a36-45b7-b423-8b2baac97976")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
    
    def test_01_1_restart_the_application_and_request_the_access_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654050 - [Stratus] Restart the application and request the access token.
        """
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
    
    def test_02_verify_set_subscriber_when_user_exchange_token_from_one_org_another_stratus(self, navigate_to_auth_plugin_stratus):
        """
        C58654051 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        sleep(5)
        self.auth_plugin.send_text_to_tenant_id_textbox("91547a10-4a36-45b7-b423-8b2baac97976")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        
    def test_02_1_verify_set_subscriber_when_user_exchange_token_from_one_org_another_stratus(self, navigate_to_auth_plugin_stratus):
        """
        C58654051 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        sleep(5)
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        result = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result)
        current_account_tenant_id = account_details["currentAccount"]["tenantId"]
        current_account_tenant_id == "66e7a414-cef9-41df-bd26-ca943b4330d4"
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        previous_account_tenant_id == "91547a10-4a36-45b7-b423-8b2baac97976"

    def test_03_verify_the_response_after_clicking_on_test_twice_under_gettoken_when_token_got_exchanged_from_orgaware_to_orgless(self, navigate_to_auth_plugin_stratus):    
        """
        C58654100 - Verify the response after clicking on Test twice under getToken(), when token got exchanged from orgaware to orgless
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("91547a10-4a36-45b7-b423-8b2baac97976")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
    
    def test_03_1_verify_the_response_after_clicking_on_test_twice_under_gettoken_when_token_got_exchanged_from_orgaware_to_orgless(self, navigate_to_auth_plugin_stratus):
        """
        C58654100 - Verify the response after clicking on Test twice under getToken(), when token got exchanged from orgaware to orgless
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.fc.call_auth_interaction_entry_point("sign_in")
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        result = self.auth_plugin.verify_set_subscriber_result()
        assert "null" in result
        
    def test_04_verify_the_behaviour_when_tenant_id_exists_with_valid_org_aware_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654104 - Verify the behaviour when tenant ID exists with valid org-aware token
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
    
    def test_05_verify_if_error_is_displayed_when_there_is_no_access_token_stored_for_a_tenant_id_wrong_tenant_id(self, navigate_to_auth_plugin_stratus):
        """
        C58654105 - Verify if error is displayed when there is no access token stored for a tenant ID ( wrong tenant ID)
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("invalid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        sleep(5)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        result = json.loads(auth_get_token_result)
        assert 'tokenValue' in result
    
    def test_06_verify_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654101 - [Stratus] Verify set event subscriber result- when user logout(orgaware token)
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
    
    def test_06_1_verify_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654101 - [Stratus] Verify set event subscriber result- when user logout(orgaware token)
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.select_auth_logout_test()
        auth_logged_in_result =  self.auth_plugin.verify_logout_successful_message()
        assert "Logout Successful" in auth_logged_in_result
        sleep(8)
        result = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result)
        current_account_result = account_details["currentAccount"]
        assert current_account_result == None
        tenant_id = account_details["previousAccount"]["tenantId"]
        assert tenant_id == "353e0b01-eb18-4b96-8523-496a684e0aa4"
    
    def test_07_verify_set_subscriber_when_tenant_id_is_blank_for_stratus(self, navigate_to_auth_plugin_stratus):
        """
        C58654099 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
 
    def test_08_verify_the_set_subscriber_result_when_user_login_first_time(self, navigate_to_auth_plugin_stratus):
        """
        C58654041 - Verify the set subscriber result when user login first time
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        logging.info("Selecting auth get token test")
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)

    def test_09_verify_the_payload_in_seteventsubscriber_method_matches_account_specification_first_login(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654107 - [oneCloud] Verify the payload in setEventSubscriber method matches Account specification-First Login
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
    
    def test_09_1_verify_the_payload_in_seteventsubscriber_method_matches_account_specification_first_login(self, navigate_to_auth_plugin_one_cloud):
        """
        C58654107 - [oneCloud] Verify the payload in setEventSubscriber method matches Account specification-First Login
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        sleep(5)
        result = self.auth_plugin.verify_set_subscriber_result()
        sleep(3)
        account_details = json.loads(result) 
        assert "stratusId" not in account_details
        assert "tenantId " != "tenantID"
        email_address = account_details["currentAccount"]["emailAddress"]
        assert email_address == self.username
        given_name = account_details["currentAccount"]["givenName"]
        assert given_name == "Qahp"
        family_name = account_details["currentAccount"]["familyName"]
        assert family_name == "Smart"
        account_id = account_details["currentAccount"]["accountId"]
        assert account_id == "4b4ec6df-9d6e-4cb5-bee2-ef2c4e927fa8"
        previous_account_tenant_id = account_details["previousAccount"]
        previous_account_tenant_id == "null"
 
    def test_10_verify_the_set_subscriber_result_when_user_exchanges_the_token_from_1_org_to_other_org(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654115 - Verify set event subscriber result- when user exchanges the token from 1 org to other org
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("8f5eb960-60d9-495f-964e-5611625b8589")
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_details)
        current_account_tenant_id = account_details["currentAccount"]["tenantId"]
        assert current_account_tenant_id == "8f5eb960-60d9-495f-964e-5611625b8589"
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        assert previous_account_tenant_id == "a7672052-b088-4436-8876-16c841712848"
 
    def test_11_verify_the_set_subscriber_result_when_user_exchanges_the_token_from_1_org_to_tenantid_blank(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654116 - Verify set event subscriber result- when user exchanges the token from 1 org to tenantId<blank>
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result_detail = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_detail)
        current_account_tenant_id = account_details["currentAccount"]["tenantId"]
        assert current_account_tenant_id == "a7672052-b088-4436-8876-16c841712848"
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        assert previous_account_tenant_id == None
 
    def test_12_verify_the_response_after_clicking_on_test_twice_under_get_token_when_token_got_exchanged_from_orgware_to_orgless(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654117 - [oneCloud]Verify the response after clicking on Test twice under getToken(),
                    when token got exchanged from orgaware to orgless
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        result_detail = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_detail)
        current_account_tenant_id = account_details["currentAccount"]["tenantId"]
        assert current_account_tenant_id == "a7672052-b088-4436-8876-16c841712848"
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        assert previous_account_tenant_id == None
 
    def test_13_verify_the_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654118 - Verify set event subscriber result- when user logout(orgaware token)
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_logout_test()
        sleep(8)
        result_details = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_details)
        current_account_tenant_id = account_details["currentAccount"]
        assert current_account_tenant_id == None
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        assert previous_account_tenant_id == "a7672052-b088-4436-8876-16c841712848"  
 
    def test_14_verify_the_set_event_subscriber_result_when_user_logout_orgaware_token(self, navigate_to_auth_plugin_one_cloud):    
        """
        C58654119 - Verify set event subscriber result- when user logout(orgless token)
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_logout_test()
        sleep(8)
        result_details = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_details)
        current_account_tenant_id = account_details["currentAccount"]
        assert current_account_tenant_id == None
        previous_account_tenant_id = account_details["previousAccount"]["tenantId"]
        assert previous_account_tenant_id == None

    def test_15_verify_set_event_subscriber_result_when_user_logout(self, navigate_to_auth_plugin_stratus, login_to_hpid):
        """
        C58654103 - Verify the set subscriber result when the user logs out
        """
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.select_auth_logout_test()
        auth_logged_in_result =  self.auth_plugin.get_logout_notification_text()
        assert "Logout Successful" in auth_logged_in_result
        result = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result)
        current_account_details = account_details["currentAccount"]
        assert current_account_details == None
    
    def test_16_verify_the_set_subscriber_result_when_user_login_first_time(self, navigate_to_auth_plugin_one_cloud, login_to_hpid):
        """
        C58654106 - [oneCloud] Verify the set subscriber result when user login first time
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        result = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result)
        email_address = account_details["currentAccount"]["emailAddress"]
        assert email_address == self.username
        given_name = account_details["currentAccount"]["givenName"]
        assert given_name == "Qahp"
        family_name = account_details["currentAccount"]["familyName"]
        assert family_name == "Smart"
        account_id = account_details["currentAccount"]["accountId"]
        assert account_id == "4b4ec6df-9d6e-4cb5-bee2-ef2c4e927fa8"
        tenant_id = account_details["currentAccount"]["tenantId"]
        assert tenant_id == None
        previous_account_tenant_id = account_details["previousAccount"]
        previous_account_tenant_id == None

    def test_17_verify_set_event_subscriber_result_when_user_exchanges_the_token_for_a_specific_org(self, navigate_to_auth_plugin_one_cloud, login_to_hpid):
        """
        C58654108 - [oneCloud] Verify set event subscriber result- when user exchanges the token for a specific org
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        sleep(5)
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        result = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result)
        account_id = account_details["currentAccount"]["accountId"]
        print(account_id)
        assert account_id == "cf950d1d-f0d8-4261-a42d-9dda7c5c5b03"

    def test_18_restart_the_application_and_request_the_access_token(self, navigate_to_auth_plugin_one_cloud, login_to_hpid):    
        """
        C58654114 - Restart the application and request the access token.
        """
        self.driver.restart_app()
        self.auth_plugin.select_logout_btn()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        result_details = self.auth_plugin.verify_set_subscriber_result()
        account_details = json.loads(result_details)
        previous_account_tenant_id = account_details["currentAccount"]["tenantId"]
        self.driver.restart_app()
        self.auth_plugin.select_logout_btn()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_additional_authorization_parameters('{"config_id":"59f93866-d28f-4aee-b150-947045966bdc"}')
        self.auth_plugin.select_auth_get_token_test()
        self.fc.verify_with_pop_up_along_with_token_value(self.username_1, self.password_1, self.web_driver)
        self.auth_plugin.verify_set_subscriber_result()
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        result_details_2 = self.auth_plugin.verify_set_subscriber_result()
        account_details_2 = json.loads(result_details_2)
        current_account_tenant_id = account_details_2["currentAccount"]["tenantId"]
        assert current_account_tenant_id == previous_account_tenant_id

    def test_19_verify_the_behavior_of_a_valid_tenant_id_with_non_expired_org_aware_token(self, navigate_to_auth_plugin_stratus):
        """
        C58654121 - Verify the behavior of a valid tenant ID with non-expired org-aware token
        """
        self.driver.restart_app()
        self.auth_plugin.select_logout_btn()
        sleep(5)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        sleep(8)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        result = json.loads(auth_get_token_result)
        old_token_value = result["tokenValue"]
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.auth_plugin.select_pop_up_ok_btn()
        sleep(8)
        self.fc.switch_to_sign_in_window(self.username, self.password, self.web_driver)
        sleep(8)
        auth_get_token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in auth_get_token_result
        result_1 = json.loads(auth_get_token_result)
        assert old_token_value != result_1["tokenValue"]