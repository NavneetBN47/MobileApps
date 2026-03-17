import logging
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.windows.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.windows.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.windows.jweb.event_service_plugin import EventServicePlugin
from MobileApps.libs.flows.windows.jweb.device_plugin import DevicePlugin
from MobileApps.libs.flows.windows.jweb.browser_plugin import BrowserPlugin
from MobileApps.libs.flows.windows.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.windows.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.windows.jweb_service_routing.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.resources.const.web.const import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from SAF.misc import windows_utils
import json
import time

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "eventing_plugin": EventingPlugin(driver),
                   "event_service_plugin": EventServicePlugin(driver),
                   "device_plugin": DevicePlugin(driver),
                   "browser_plugin": BrowserPlugin(driver),
                   "hpid": HPID(driver, context="NATIVE_APP"),
                   "auth_plugin": AuthPlugin(driver),
                   "eventing_plugin": EventingPlugin(driver),
                   "service_plugin": ServiceRoutingPlugin(driver)}
        test_account = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]
        self.hpid_username = test_account["username"]
        self.hpid_pwd = test_account["password"]

    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        if not self.fd["home"].verify_menu_button():
            self.driver.launch_app()

    def navigate_to_auth_plugin(self):
        """
        Navigate to the Auth Plugin from the Home screen.
        This method assumes that the app is already launched and the Home screen is displayed.
        """
        self.fd['home'].select_webview_mode(raise_e=False)
        self.fd['home'].select_jweb_reference_btn(raise_e=False)
        self.fd['home'].select_plugin_from_home("auth")
    
    def call_auth_interaction_entry_point(self, entry_point):
        """
        Call the auth interaction entry point to navigate to the sign-in page.
        """
        self.fd['auth_plugin'].nav_to_auth_sign_in_page(entry_point)

    def login_to_hpid(self, username, password, web_driver=None):
        """
        Login to HPID using the test account credentials.
        """
        self.fd["auth_plugin"].select_auth_logged_in_test()
        logged_in_result = self.fd["auth_plugin"].auth_logged_in_result()
        assert 'value' in logged_in_result, "Didn't receive isLoggedIn() value during login_to_hpid()"
        token = self.fd["auth_plugin"].auth_get_token_result()
        if not logged_in_result['value'] or token is False or not "tokenValue" in token:
            self.fd["auth_plugin"].control_auth_token_switches([True, True, True, True, True])
            self.call_auth_interaction_entry_point("sign_in")
            self.fd["auth_plugin"].select_auth_get_token_test()
            sleep(5)
            if self.driver.wait_for_object("pop_up_ok_btn", timeout=5, displayed=False, raise_e=False):
                self.fd['auth_plugin'].select_pop_up_ok_btn()
                sleep(10)
                self.switch_to_sign_in_window(username, password, web_driver)
            else:
                auth_get_token_result = self.fd['auth_plugin'].auth_get_token_result()
                sleep(5)

    def close_jweb_app(self):
        '''
        This is a method to close jarvis reference app.
        :parameter:
        :return:
        '''
        logging.debug("Closing Jarvis App...")
        if self.fd["home"].verify_close_window():
            self.fd["home"].click_close_window()

    def switch_to_sign_in_window(self, username, password, web_driver=None, user_icon_click=True):
        """
        Switch to sign in window and perform login
        """
        window_name = "auth_login"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.login(username, password)
        web_driver.close_window(web_driver.current_window)

    def switch_to_create_account_window(self, web_driver=None, user_icon_click=True):
        """
        Switch to create account window and perform create account
        """
        window_name = "auth_create_account"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.create_account()
        web_driver.close_window(web_driver.current_window)

    def verify_create_account_page(self, web_driver=None):
        window_name = "create_account"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.verify_create_an_account_page()
        web_driver.close_window(web_driver.current_window)

    def verify_sign_in_page(self, web_driver=None):
        window_name = "auth_login"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.verify_hp_id_sign_in()
        web_driver.close_window(web_driver.current_window)

    def get_jweb_auth_test_data(self, stack):
        """
        Get data collection test data based on stack
        :param stack: stack of the test data
        :return: test data
        """
        stack = stack.lower()
        if stack == "staging":
            stack = "stage"
        with open(ma_misc.get_abs_path("resources/test_data/jweb/ios_auth_accounts.json")) as test_data:
            ios_auth_accounts = json.loads(test_data.read())
            if stack in ["stage", "pie"]:
                ios_auth_accounts = ios_auth_accounts[stack]
            elif stack == "dev":
                ios_auth_accounts = ios_auth_accounts["pie"]
            else:
                raise ValueError("Stack must be one of 'stage', 'pie', or 'dev'. Received: {}".format(stack))
        return ios_auth_accounts

    def verify_with_pop_up_along_with_token_value(self, username, password, web_driver=None):
        """
        Verify the pop up along with token value
        """
        if self.driver.wait_for_object("pop_up_ok_btn", timeout=5, displayed=False, raise_e=False):
            self.fd['auth_plugin'].select_pop_up_ok_btn()
            self.switch_to_sign_in_window(username, password, web_driver)
            auth_get_token_result = self.fd['auth_plugin'].auth_get_token_result()
            assert 'tokenValue' in auth_get_token_result
        else:
            auth_get_token_result = self.fd['auth_plugin'].auth_get_token_result()
            assert 'tokenValue' in auth_get_token_result
    
    def get_jweb_login_event_test_data(self, stack):
        """
        Get login event test data based on stack
        """
        stack = stack.lower()
        if stack == "staging":
            stack = "stage"
        with open(ma_misc.get_abs_path("resources/test_data/jweb/windows_auth_accounts.json")) as test_data:
            windows_auth_accounts = json.loads(test_data.read())
            if stack in ["stage", "pie"]:
                windows_auth_accounts = windows_auth_accounts[stack]
            elif stack == "dev":
                windows_auth_accounts = windows_auth_accounts["pie"]
            else:
                raise ValueError("Stack must be one of 'stage', 'pie', or 'dev'. Received: {}".format(stack))
        return windows_auth_accounts

    def verify_with_pop_up_along_with_token_value_for_create_account(self, web_driver=None):
        """
        Verify the pop up along with token value for create account
        """
        if self.driver.wait_for_object("pop_up_ok_btn", timeout=5, displayed=False, raise_e=False):
            self.fd['auth_plugin'].select_pop_up_ok_btn()
            self.switch_to_create_account_window(web_driver)
            auth_get_token_result = self.fd['auth_plugin'].auth_get_token_result()
            assert 'tokenValue' in auth_get_token_result
        else:
            auth_get_token_result = self.fd['auth_plugin'].auth_get_token_result()
            assert 'tokenValue' in auth_get_token_result

    def close_the_window(self, web_driver=None):
        """
        Close the current window
        """
        window_name = "create_account"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        web_driver.close_window(web_driver.current_window)