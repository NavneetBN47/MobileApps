from time import sleep
import pytest
import json
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB_AUTH"

class Test_Suite_10_Auth_Plugin_Login_Event(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.jweb_auth_settings = cls.fc.fd["jweb_auth_settings"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_auth_plugin(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    @pytest.fixture()
    def reset_app(self):
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    @pytest.fixture()
    def close_app(self):
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
    
    def test_01_verify_set_subscriber_event_result_when_user_exchanges_token_for_specif_org(self, reset_app):
        """
        C58654108 - Verify that the payload in the set subscriber event matches the account specification
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("a7672052-b088-4436-8876-16c841712848")
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result

    def test_02_verify_set_subscriber_when_user_exchange_token_from_one_org_another_stratus(self):
        """
        C58654051 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        sleep(3)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        sleep(5)
        self.hpid.login(self.username, self.password)
        sleep(10)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        self.auth_plugin.send_text_to_tenant_id_textbox("66e7a414-cef9-41df-bd26-ca943b4330d4")
        sleep(3)
        self.auth_plugin.select_auth_get_token_test()
        result = self.auth_plugin.event_subscriber_result()
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"
        tenant_id = result["currentAccount"]["tenantId"]
        assert tenant_id == "66e7a414-cef9-41df-bd26-ca943b4330d4"

    def test_03_verify_set_subscriber_when_tenant_id_is_blank_for_stratus(self, reset_app):
        """
        C58654099 - Verify that the tenant id is blank when the user selects the stratus option
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.send_text_to_tenant_id_textbox("")
        sleep(5)
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(5)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result

    def test_04_verify_payload_in_set_subscriber_event_matches_account_specification(self, reset_app):
        """
        C58654102 - Verify that the payload in the set subscriber event matches the account specification
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(5)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        result = self.auth_plugin.event_subscriber_result()
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"

    def test_05_verify_set_event_subscriber_result_when_user_logout(self):
        """
        C58654103 - Verify the set subscriber result when the user logs out
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}
        result = self.auth_plugin.event_subscriber_result()
        current_account_details = result["currentAccount"]
        assert current_account_details == None

    def test_06_verify_the_set_subscriber_result_when_user_login_first_time(self):    
        """
        C58654106 - [oneCloud] Verify the set subscriber result when user login first time
        """
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Settings', raise_e=False)
        sleep(5)
        self.auth_plugin.select_app_settings_chevron()
        self.auth_plugin.select_auth_provider_option("oneCloud")
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
        sleep(5)
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(8)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(5)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        sleep(8)
        result = self.auth_plugin.event_subscriber_result()
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"

    def test_07_verify_payload_in_set_subscriber_event_matches_account_specification(self, reset_app):
        """
        C58654107 - Verify that the payload in the set subscriber event matches the account specification
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.control_auth_token_switches([False, True, True, False, False])
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(5)
        result = self.auth_plugin.auth_get_token_result()
        assert 'tokenValue' in result
        result = self.auth_plugin.event_subscriber_result()
        email_address = result["currentAccount"]["emailAddress"]
        assert email_address == self.username
        family_name = result["currentAccount"]["familyName"]
        assert family_name == "stage 1"