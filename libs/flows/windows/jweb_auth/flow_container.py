from MobileApps.libs.flows.windows.jweb_auth.home import Home
from MobileApps.libs.flows.windows.jweb_auth.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import windows_utils
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.fd = {"home": Home(driver),
                   "auth_plugin": AuthPlugin(driver),
                   "hpid": HPID(driver, context={'url':'login'})}

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

    def call_auth_interaction_entry_point(self, entry_point):
        """
        Go to home screen; Navigate to auth plugin, then; Select specifically entry point.
        """
        self.fd['auth_plugin'].nav_to_auth_sign_in_page(entry_point)

    def verify_create_account_page(self, web_driver=None):
        window_name = "create_account"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.verify_create_an_account_page()
        web_driver.close_window(web_driver.current_window)

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

    def verify_with_pop_up_along_with_token_value(self, username, password, web_driver=None):
        """
        Handle authentication flow - login via popup if appears, then get token result.
        Returns token result dict for test case to validate.
        """
        try:
            logging.info("Switching to sign-in window")
            self.switch_to_sign_in_window(username, password, web_driver)
            logging.info("Switched to sign-in window - completed")
        except Exception as e:
            logging.info(f"No browser navigation occurred: {e}")
            logging.info("Proceeding with UI result instead")
        
        # Get token result and return to test case for assertions
        return self.fd['auth_plugin'].auth_get_token_result()
    
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

    def verify_sign_in_page(self, web_driver=None):
        """
        Switch to browser and Verify the sign-in page
        """
        window_name = "auth_login"
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.verify_hp_id_sign_in()
        web_driver.close_window(web_driver.current_window)

    def verify_with_pop_up_along_with_token_value_for_create_account(self, web_driver=None):
        """
        Handle create account flow - create account via popup if appears, then get token result.
        Returns token result dict for test case to validate.
        """
        try:
            self.switch_to_create_account_window(web_driver)
            logging.info("Switched to create account window - completed")
        except Exception as e:
            logging.info(f"No browser navigation occurred: {e}")
            logging.info("Proceeding with UI result instead")
        
        # Get token result and return to test case for assertions
        return self.fd['auth_plugin'].auth_get_token_result()