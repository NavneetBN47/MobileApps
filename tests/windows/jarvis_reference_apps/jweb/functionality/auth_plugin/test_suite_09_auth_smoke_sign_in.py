import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const
import json
import logging

pytest.app_info = "JWEB"

class Test_Suite_09_Auth_Smoke_Sign_In(object):
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

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]

    @pytest.fixture()
    def login_to_hpid(self):
        self.fc.login_to_hpid(self.username, self.password, self.web_driver)

    @pytest.fixture()
    def logout_from_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if self.auth_plugin.auth_logged_in_result()["value"]:
            self.auth_plugin.select_auth_logout_test()

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()
        self.auth_plugin.choose_auth_stack("Stage")
        self.auth_plugin.select_auth_provider_option("StratusUsingBrowser")
        self.driver.restart_app()
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.navigation_to_top_of_page()

    def test_01_validate_return_stratus_token_by_enabling_all_the_options(self):
        """
        C53044962 - Validate the return of stratus token by enabling all the options (create account)
        """
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()  
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)

    def test_02_validate_return_of_access_token(self):
        """
        C53044904: Validate the return of access token after creating account
        """
        self.auth_plugin.select_auth_logout_test()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)

    def test_03_verify_org_less_token_is_retrived_when_the_user_creates_account_for_the_first_time_tenantId_blank(self):
        """
        C53045139 - Verify if the org-less token is retrived when the user creates account for the first time(tenantId:blank)
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("create_account")
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value_for_create_account(self.web_driver)

    def test_04_validate_the_log_out_method_after_signing_or_create_account_set_subscriber(self):
        """
        C53044915 - Validate the log out method after signing or create account- Set Subscriber
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        auth_logged_in_result = self.auth_plugin.auth_logout_result()
        assert self.auth_plugin.auth_logout_result() == {}

    def test_05_validate_the_logged_in_method_after_signing_or_create_account_set_subscriber(self):
        """
        C53044916 -Validate the logged in method after signing or create account- Set Subscriber
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        self.auth_plugin.select_auth_logged_in_test()
        sleep(5)
        self.auth_plugin.auth_logged_in_result()
        assert self.auth_plugin.auth_logged_in_result()["value"] == True

    def test_06_validate_the_logged_out_method_after_signing_or_create_account_unsubscribe(self):
        """
        C53044917 - Validate the logged out method after signing or create account - Unsubscribe
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.select_set_subscriber_btn()
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)
        self.auth_plugin.select_un_subscriber_btn()
        sleep(5)
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        auth_logged_out_result = self.auth_plugin.verify_logout_successful_message()
        assert self.auth_plugin.auth_logout_result() == {}

    def test_07_verify_if_access_token_is_updated_with_new_org_less_token(self):
        """
        C53045140 - Verify if access token is updated with new org less token
        """
        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_token_lifetime_option_btn()
        self.auth_plugin.select_token_lifetime_options("preferredMinimumSecondsUntilExpiration")
        self.auth_plugin.set_time_interval_for_token("36000")
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(5)
        self.fc.verify_with_pop_up_along_with_token_value(self.username, self.password, self.web_driver)