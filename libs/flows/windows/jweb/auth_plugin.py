from selenium.common.exceptions import NoSuchElementException, TimeoutException
from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from time import sleep, time
import json
import re
from selenium.common.exceptions import *
import logging

class AuthPlugin(JwebFlow):
    flow_name = "auth_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def navigation_to_top_of_page(self):
        for _ in range(3):
            self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up", distance=3)

    def swipe_to_object(self, obj, format_specifier=[], direction="down"):
        """
        Within Auth Plugin, swipe to an object given a direction
        """
        for _ in range(10):
            if not self.driver.wait_for_object(obj, raise_e=False, format_specifier=format_specifier, timeout=1):
                self.driver.swipe(anchor_element="auth_plugin_header_title", direction=direction)
            else:
                return True
        else:
            return False

    def select_auth_logged_in_test(self):
        """
        under Auth.isLoggedIn(), click the auth logged in test button
        :returns: success of logged_in_test result text
        """
        self.swipe_to_object("auth_logged_in_test_btn")
        self.driver.click("auth_logged_in_test_btn", displayed=False)
        for _ in range(5):
            if self.auth_logged_in_result() is False:
                self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up")
                self.driver.click("auth_logged_in_test_btn", displayed=False)
            else:
                break
        return self.auth_logged_in_result() is not False

    def auth_logged_in_result(self):
        """
        :returns: Auth.isLoggedIn() test result text 
        """
        logged_in_result = self.driver.get_attribute("auth_is_logged_in_result_txt", "Name", displayed=False)
        return False if logged_in_result == 'Result' else json.loads(logged_in_result)

    def select_auth_get_token_test(self):
        """
        under Auth.getToken(), click the get_token test button
        """
        self.swipe_to_object("auth_get_token_test_btn")
        self.driver.click("auth_get_token_test_btn", displayed=False)

    def auth_get_token_result(self):
        """
        :return: Auth.getToken() test result text 
        """
        token_result = self.driver.get_attribute("auth_get_token_result_txt", "Name", displayed=False)
        timer = time() + 10
        while token_result == 'Result':
            sleep(1)
            token_result = self.driver.get_attribute("auth_get_token_result_txt", "Name", displayed=False)
            if timer < time():
                return False
        return False if token_result == 'Result' else json.loads(token_result)

    def get_refreshed_token(self, token=None):
        """
        There can be a ~1 second delay before the token refreshes, this method checks to ensure an old token is not being returned 
        :return: Auth.getToken() test result text. 
        """
        refreshed_token = self.auth_get_token_result()['tokenValue']
        timeout = time() + 16
        while time() < timeout and refreshed_token == token:
            sleep(2)
            refreshed_token = self.auth_get_token_result()['tokenValue']
        return refreshed_token

    def control_auth_token_switches(self, values):
        """
        Toggle auth token switches as they appear by passing in a list of five boolean for each toggle
            - Require Fresh Token
            - Allow Network Access
            - Allow User Interaction
            - Show Account Creation Link
            - Skip Token Refresh
        """
        self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up", distance=5)
        for i, switch in enumerate(["requireFreshToken", "allowNetworkAccess", 
                                    "allowUserInteraction", "showAccountCreationLink", 
                                    "skipTokenRefresh"]):
            list_option_fs = str(values[i]).lower()
            for _ in range(3):
                try:
                    if not self.driver.wait_for_object("auth_token_list_options", format_specifier=[switch, str(values[i]).lower()], raise_e=False, timeout=2):
                        logging.info("Trying to click the auth token switch: {}".format(switch))
                        self.swipe_to_object("auth_token_option_checkbox", format_specifier=[switch, str(values[i]).lower()], direction="down")
                        self.driver.click("auth_token_option_checkbox", format_specifier=[switch, str(values[i]).lower()])
                    self.driver.click("auth_token_list_options", format_specifier=[switch, str(values[i]).lower()])
                    all_found_list_options = self.driver.find_object("auth_token_list_option", format_specifier=[list_option_fs], multiple=True)
                    for j in range(len(all_found_list_options)):
                        if switch in self.driver.get_attribute("auth_token_list_option", format_specifier=[list_option_fs, str(values[i]).lower()], attribute="AutomationId", index=j):
                            self.driver.click("auth_token_list_option", format_specifier=[list_option_fs, str(values[i]).lower()], index=j)
                            break
                    break
                except (NoSuchElementException, TimeoutException):
                    self.swipe_to_object("auth_token_list_option", format_specifier=[list_option_fs])

    def nav_to_auth_sign_in_page(self, option):
        """
        under Auth.getToken(), select user interaction entry point from list
        :param option: str value in list for user entry point
        """
        if option not in ["sign_in", "create_account"]:
            raise ValueError("nav to sign in page option:{} not available".format(option))
        
        if self.driver.wait_for_object("auth_user_interaction_entry_point_selector", displayed=False, raise_e=False, timeout=2):
            if self.driver.get_attribute("auth_user_interaction_entry_point_selector", "Name", displayed=False, raise_e=False) == option:
                return True

        for _ in range(3):
            self.select_auth_user_interaction_entry_point_selector()
            if option == "sign_in":
                self.driver.click("auth_sign_in_page_item", displayed=False)
            elif option == "create_account":
                self.driver.click("auth_create_account_page_item", displayed=False)
            sleep(0.5)
            if self.driver.wait_for_object("auth_user_interaction_entry_point_selector_name", format_specifier=[self.driver.current_ui_map["auth_{}_page_item".format(option)]['locator']['name']], raise_e=False): 
                break
        else:
            raise NoSuchElementException("Selecting {} page option failed to update selected drop down item".format(option))

    def select_auth_user_interaction_entry_point_selector(self):
        """
        under Auth.getToken(), selects the user interaction starting point
        """
        if not self.driver.wait_for_object("auth_user_interaction_entry_point_selector", displayed=False, raise_e=False, timeout=2):
            self.swipe_to_object("auth_token_option_checkbox", format_specifier=["userInteractionEntryPoint"])
            self.driver.click("auth_token_option_checkbox", format_specifier=["userInteractionEntryPoint"], displayed=False)
        
        try:
            self.driver.click("auth_user_interaction_entry_point_selector", displayed=False, change_check={"wait_obj":"auth_user_interaction_entry_point_selector_expanded"})
        except NoSuchElementException:
            self.swipe_to_object("auth_user_interaction_entry_point_selector", direction="up")
            self.driver.click("auth_user_interaction_entry_point_selector", displayed=False, change_check={"wait_obj":"auth_user_interaction_entry_point_selector_expanded"})

    def select_auth_logout_test(self):
        """
        under Auth.logout(), clicks the auth logout test button
        """
        self.swipe_to_object("auth_logout_test_btn")
        self.driver.click("auth_logout_test_btn", displayed=False)

    def auth_logout_result(self):
        """
        :returns: Auth.logout() test result text 
        """
        result = self.driver.get_attribute("auth_logout_result_txt", "Name", displayed=False)
        return json.loads(result)
    
    def select_close_webview_btn(self):
        """
        clicks the exit button in the top right of the spawned center webview login page
        """
        self.driver.click("close_webview_btn")
        self.driver.swipe(direction="up")

    def choose_auth_stack(self, stack):
        """
        Chooses the auth stack from the dropdown in settings.
        :param stack_option: The stack option to select (e.g., "Pie", "Stage", "Prod")
        """
        self.driver.click("auth_settings_btn", displayed=False)
        self.driver.swipe(direction="down")
        self.driver.click("choose_auth_stack", displayed=False)
        self.driver.click("auth_stack_option", format_specifier=[stack], displayed=False)
        self.driver.click("pop_up_close_btn", displayed=False, raise_e=False)

    def select_auth_provider_option(self, option):
        """
        Selects the auth provider option from the dropdown in settings.
        """
        self.driver.click("auth_provider_btn", displayed=False)
        self.driver.click("auth_stratus_option", format_specifier=[option])
        self.driver.click("pop_up_close_btn", displayed=False, raise_e=False)
        self.driver.click("auth_home_btn", displayed=False)

    def select_pop_up_ok_btn(self):
        """
        Clicks the ok button in the pop up
        """
        self.driver.click("pop_up_ok_btn", raise_e=False, displayed=False)

    def select_send_token_options(self, value):
        """
        Set "Send Token Options" checkbox to given parameter value 
        """
        self.swipe_to_object("require_fresh_token")
        self.driver.check_box("require_fresh_token", uncheck=not value)

    def auth_send_token_disable_result(self):
        """
        returns the auth send token disable result
        """
        return self.driver.get_attribute("send_token_disable_result", "text", displayed=False)

    def send_text_to_tenant_id_textbox(self, text):
        """
        send text parameter value to the tenant id textbox
        """
        clicked = self.driver.click("auth_tenant_textbox", displayed=False, raise_e=False)

        if not clicked:
            self.driver.click("auth_token_option_checkbox", format_specifier=["tenantID"], displayed=False,  raise_e=False)
            self.driver.click("auth_tenant_textbox", displayed=False)
        self.driver.send_keys("auth_tenant_textbox", text)

    def verify_error_code_result(self):
        """
        verify the error code result and return it in JSON format
        """ 
        error_result = self.driver.get_attribute("error_code_result", "text", displayed=False)
        return False if error_result == 'Result' else json.loads(error_result)

    def select_cancel_btn(self):
        """
        Clicks the cancel button in the tests tab 
        """
        self.driver.click("cancel_btn")

    def select_set_subscriber_btn(self):
        """
        From the Set Event Subscriber() page, select the the Set Subscriber btn 
        """
        self.swipe_to_object("set_subscriber_btn", direction="up")
        self.driver.click("set_subscriber_btn")

    def verify_logout_successful_message(self):
        """
        verify that the logout was successful
        :return:
        """
        return self.driver.get_attribute("logout_successful_message", "Name",  displayed=False)

    def verify_set_subscriber_result(self):
        """
        Verify the result of the Set Subscriber operation 
        """
        self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up", distance=7)
        result = self.driver.get_attribute("event_subscriber_result", "Name", displayed=False, raise_e=False)

        if result is None:
            self.driver.scroll_element("event_subscriber_result", direction="down", distance=4, time_out=10)
            result = self.driver.get_attribute("event_subscriber_result", "Name", displayed=False, raise_e=False)
        return result

    def send_text_to_scope_textbox(self, text):
        """
        send text parameter value to the auth scope field textbox
        """
        if not self.driver.wait_for_object("token_scopes_checkbox", raise_e=False, timeout=2):
            self.swipe_to_object("token_scopes_checkbox", direction="down")
        
        self.driver.click("token_scopes_checkbox", displayed=False)
        self.driver.click("auth_scope_field_textbox", displayed=False)
        self.driver.clear_text("auth_scope_field_textbox")
        self.driver.send_keys("auth_scope_field_textbox", text)
    
    def send_text_to_additional_authorization_parameters(self, text):
        """
        send text parameter value to the additional authorization parameters field textbox
        """
        self.driver.click("additional_authorization_parameters_checkbox", displayed=False)
        self.driver.click("additional_authorization_parameters_textbox", displayed=False)
        self.driver.send_keys("additional_authorization_parameters_textbox", text)

    def select_token_lifetime_option_btn(self):
        """
        Clicks the token lifetime option button
        """
        self.driver.click("auth_token_option_checkbox", format_specifier=["tokenLifetimeRequirements"], displayed=False)
        self.driver.click("add_token_lifetime_option_btn")

    def select_token_lifetime_options(self, token_lifetime_option):
        """
        Select the token lifetime option from the dropdown.
        """
        if token_lifetime_option not in ["preferredMaximumSecondsSinceIssued", "preferredMinimumSecondsUntilExpiration"]:
            raise ValueError("token lifetime option:{} not available, expecting preferredMaximumSecondsSinceIssued or preferredMinimumSecondsUntilExpiration".format(token_lifetime_option))

        self.driver.click("type_token_combobox", displayed=False)
        self.driver.click("token_lifetime_option", format_specifier=[token_lifetime_option])

    def set_time_interval_for_token(self, text):
        """
        Set the time interval for the token.
        """
        self.driver.click("time_interval_textbox", displayed=False)
        self.driver.send_keys("time_interval_textbox", text)

    def select_un_subscriber_btn(self):
        """
        From the Set Event Subscriber() page, select the the Unsubscribe btn
        """
        self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up", distance=5)
        self.driver.scroll_element("un_subscriber_btn", direction="down", time_out=10)
        self.driver.click("un_subscriber_btn")

    def get_logout_notification_text(self):
        """
        Return text found within the toast pop up
        """
        return self.driver.wait_for_object("logout_toast_text", displayed =False).text

########################################################################################################################
#                                                                                                                      #
#                                        VERIFICATION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_at_auth_plugin(self):
        """
        verify that we are currently at the auth plugin page
        :return: bool
        """
        return self.driver.wait_for_object("auth_plugin_header_title", raise_e=False, timeout=3) is not False