import json
from selenium.common.exceptions import *
from MobileApps.libs.flows.windows.jweb_auth.jweb_auth_plugin_flow import JwebAuthFlow
import logging

class AuthPlugin(JwebAuthFlow):
    flow_name = "auth_plugin"
    
    def control_auth_token_switches(self, values):
        """
        Toggle auth token switches as they appear by passing in a list of five boolean for each toggle
            - Require Fresh Token
            - Allow Network Access
            - Allow User Interaction
            - Show Account Creation Link
            - Skip Token Refresh
        """
        max_attempts = 7
        for attempt in range(max_attempts):
            if self.driver.wait_for_object("auth_plugin_header_title", displayed=True, raise_e=False, timeout=1):
                logging.info(f"Found auth_plugin_header_title on attempt {attempt + 1}")
                break
            else:
                logging.info("auth_plugin_header_title not found, swiping up...")
                logging.info("Swiping up to find auth_plugin_header_title...attempt {}".format(attempt + 1))
                self.driver.swipe(direction="up", distance=4)

        else:
            raise NoSuchElementException("auth_plugin_header_title not found after {} attempts.".format(max_attempts))

        logging.info("Found auth_plugin_header_title, positioning for switches...")
        
        for i, switch in enumerate(["requireFreshToken", "allowNetworkAccess", 
                                    "allowUserInteraction", "showAccountCreationLink", 
                                    "skipTokenRefresh"]):
            list_option_fs = str(values[i]).lower()
            for _ in range(3):
                try:
                    if not self.driver.wait_for_object("auth_token_list_options", format_specifier=[switch, str(values[i]).lower()], raise_e=False, timeout=2):
                        logging.info("Trying to click the auth token switch: {}".format(switch))
                        self.driver.click("auth_token_option_checkbox", format_specifier=[switch, str(values[i]).lower()], displayed=False)
                        logging.info("Clicked the auth token switch: {}".format(switch))
                    self.driver.click("auth_token_list_options", format_specifier=[switch, str(values[i]).lower()], displayed=False)
                    logging.info("Clicked the auth token list options: {}".format(switch))
                    all_found_list_options = self.driver.find_object("auth_token_list_option", format_specifier=[list_option_fs], multiple=True)
                    for j in range(len(all_found_list_options)):
                        automation_id = self.driver.get_attribute("auth_token_list_option", format_specifier=[list_option_fs, str(values[i]).lower()], attribute="AutomationId", index=j)
                        if automation_id and switch in automation_id:
                            self.driver.click("auth_token_list_option", format_specifier=[list_option_fs, str(values[i]).lower()], index=j)
                            break
                    break
                except (NoSuchElementException, TimeoutException):
                    logging.info("Trying to click the auth token switch: {}".format(switch))
                    self.driver.click("auth_token_option_checkbox", format_specifier=[switch, str(values[i]).lower()], displayed=False)
                    logging.info("Clicked the auth token switch: {}".format(switch))
                    
    def select_auth_user_interaction_entry_point_selector(self):
        """
        under Auth.getToken(), selects the user interaction starting point
        """
        if not self.driver.wait_for_object("auth_user_interaction_entry_point_selector", displayed=False, raise_e=False, timeout=2):
            self.driver.click("auth_token_option_checkbox", format_specifier=["userInteractionEntryPoint"], displayed=False)
        try:
            self.driver.click("auth_user_interaction_entry_point_selector", displayed=False)
        except NoSuchElementException:
            self.driver.scroll_element("auth_user_interaction_entry_point_selector", direction="down")
            self.driver.swipe(direction="down")
            self.driver.click("auth_user_interaction_entry_point_selector", displayed=False)

    def nav_to_auth_sign_in_page(self, option):
        """
        under Auth.getToken(), select user interaction entry point from list
        :param option: str value in list for user entry point
        """
        if option not in ["sign_in", "create_account"]:
            raise ValueError("nav to sign in page option:{} not available".format(option))
        
        if self.driver.wait_for_object("auth_user_interaction_entry_point_selector", displayed=False, raise_e=False, timeout=10):
            current_name = self.driver.get_attribute("auth_user_interaction_entry_point_selector", "Name", displayed=False, raise_e=False)
            if current_name and current_name == option:
                logging.info("Auth user interaction entry point selector is already set to: {}".format(option))
                return True

        for _ in range(3):
            self.select_auth_user_interaction_entry_point_selector()
            logging.info("Selecting auth user interaction entry point selector to: {}".format(option))
            if option == "sign_in":
                self.driver.click("auth_sign_in_page_item", displayed=False)
                logging.info("Clicked on sign in page item.")
            elif option == "create_account":
                self.driver.click("auth_create_account_page_item", displayed=False)
                logging.info("Clicked on create account page item.")
            if self.driver.wait_for_object("auth_user_interaction_entry_point_selector_name", format_specifier=[self.driver.current_ui_map["auth_{}_page_item".format(option)]['locator']['name']], raise_e=False):
                logging.info("Successfully selected auth user interaction entry point selector to: {}".format(option))
                break
        else:
            raise NoSuchElementException("Selecting {} page option failed to update selected drop down item".format(option))

    def select_auth_get_token_test(self):
        """
        under Auth.getToken(), click the get_token test button

        :param verify_sign_in_page: ensure that we see the HPID sign_in_textbox after clicking test button 
        """
        self.driver.swipe(direction="down", distance=3)
        self.driver.click("auth_get_token_test_btn", displayed=False, raise_e=False)
        logging.info("Clicked the auth get token test button.")

    def send_text_to_tenant_id_textbox(self, text):
        """
        send text parameter value to the tenant id textbox
        """
        clicked = self.driver.click("auth_tenant_textbox", displayed=False, raise_e=False)
        logging.info("Clicked on tenant ID textbox: {}".format(clicked))

        if not clicked:
            logging.info("Tenant ID textbox not found, clicking the auth token option checkbox to reveal it.")
            self.driver.click("auth_token_option_checkbox", format_specifier=["tenantID"], displayed=False,  raise_e=False)
            logging.info("Clicked the auth token option checkbox to reveal tenant ID textbox.")
            
            # Wait for textbox to appear and scroll if needed
            if not self.driver.wait_for_object("auth_tenant_textbox", timeout=3, raise_e=False):
                logging.info("Tenant ID textbox still not visible, scrolling down to find it.")
                self.driver.swipe(direction="down", distance=2)
            
            self.driver.click("auth_tenant_textbox", displayed=False)
            logging.info("Clicked on tenant ID textbox after revealing it.")
        self.driver.send_keys("auth_tenant_textbox", text)
        logging.info("Sent text to tenant ID textbox: {}".format(text))

    def select_send_token_options(self, value):
        """
        Set "Send Token Options" checkbox to given parameter value 
        """
        self.driver.scroll_element("require_fresh_token", distance=3, time_out=10)
        self.driver.check_box("require_fresh_token", uncheck=not value)

    def auth_get_token_result(self):
        """
        returns the auth get token result as a dictionary
        """
        result = self.driver.get_attribute("auth_get_token_result_txt", "text", displayed=False)
        return json.loads(result)

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

    def change_token_type(self, token_lifetime_option):
        """
        Change the token type based on the given token lifetime option.
        :param token_lifetime_option: The token lifetime option to set
        """
        if token_lifetime_option not in ["preferredMaximumSecondsSinceIssued", "preferredMinimumSecondsUntilExpiration"]:
            raise ValueError("token lifetime option:{} not available, expecting preferredMaximumSecondsSinceIssued or preferredMinimumSecondsUntilExpiration".format(token_lifetime_option))
        self.driver.click("type_token_combobox", displayed=False)
        self.driver.click("token_lifetime_option", format_specifier=[token_lifetime_option])

    def auth_send_token_disable_result(self):
        """
        returns the auth send token disable result
        """
        try:
            if self.driver.wait_for_object("send_token_disable_result", displayed=False, raise_e=False, timeout=10):
                logging.info("Error code result found.")
                result_text = self.driver.get_attribute("send_token_disable_result", "text", displayed=False)
                logging.info("Raw error code result")

                try:
                    result_json = json.loads(result_text)
                    logging.info("Successfully parsed error code result as JSON")
                    return result_json
                except json.JSONDecodeError as json_error:
                    logging.warning("Failed to parse error code result as JSON")
                    logging.info("Returning raw text")
                    return {"error": "json_parse_failed", "raw_text": result_text}
        except NoSuchElementException:
            logging.error("Error occurred while verifying error code result")
            raise NoSuchElementException("Error code result not found.")
    
    def select_logout_btn(self):
        """
        Clicks the logout button in the tests tab
        """
        clicked = self.driver.click("logout_btn", displayed=False, raise_e=False)
        if clicked:
            logging.info("Clicked the logout button successfully.")
            return True
        else:
            logging.error("Failed to click logout button - button not found or not clickable.")
            return False

    def select_create_account_btn(self):
        """
        Clicks the create account button in the tests tab 
        """
        self.driver.click("create_account_btn")

    def verify_orgless_token_contents(self): 
        """ 
        in orgles token text box verify that the field is not empty   
        """
        return not self.driver.wait_for_object("orgless_token_text", timeout=3, raise_e=False) is False

    def send_text_to_scope_textbox(self, text):
        """
        send text parameter value to the auth scope field textbox
        """
        try:
            self.driver.click("token_scopes_checkbox")
            self.driver.clear_text("auth_scope_field_textbox")
            self.driver.send_keys("auth_scope_field_textbox", text)
            logging.info("Sent text to auth scope field textbox: {}".format(text))
        except NoSuchElementException:
            logging.error("Error occurred while sending text to auth scope field textbox")
            raise NoSuchElementException("Auth scope field textbox not found.")

    def select_set_subscriber_btn(self):
        """
        From the Set Event Subscriber() page, select the the Set Subscriber btn 
        """
        try:
            self.driver.scroll_element("set_subscriber_btn", time_out=10)
            logging.info("Scrolled to Set Subscriber button.")
            self.driver.click("set_subscriber_btn")
            logging.info("Clicked the Set Subscriber button successfully.")
        except NoSuchElementException:
            logging.error("Error occurred while clicking Set Subscriber button")
            raise NoSuchElementException("Set Subscriber button not found.")

    def select_auth_logout_test(self):
        """
        clicks the auth logout test 
        :return:
        """
        self.driver.scroll_element("auth_logout_btn", direction="down", distance=9, time_out=20)
        self.driver.click("auth_logout_btn", displayed=False)
    
    def verify_logout_successful_message(self):
        """
        verify that the logout was successful
        :return:
        """
        try:
            self.driver.scroll_element("logout_successful_message", direction="down", time_out=20)
            logging.info("Scrolled to logout successful message.")
            return self.driver.get_attribute("logout_successful_message", "Name",  displayed=False)
        except TimeoutException:
            logging.error("Error occurred while verifying logout successful message")
            raise TimeoutException("Logout successful message not found.")

    def select_auth_logged_in_test(self):
        """
        From the Set Event Subscriber() page, verify the Set Subscriber btn 
        """ 
        try:
            self.driver.scroll_element("set_subscriber_btn", direction="up", distance=6, time_out=10)
            if self.driver.wait_for_object("auth_is_logged_in_test_btn", displayed=False, raise_e=False, timeout=10):
                logging.info("Auth logged in test button found, clicking it.")
                self.driver.click("auth_is_logged_in_test_btn", displayed=False)
                logging.info("Clicked the auth logged in test button successfully.")
            else:
                logging.error("Auth logged in test button not found.")
                self.driver.scroll_element("auth_is_logged_in_test_btn")
                logging.info("Scrolled to find auth logged in test button.")
                self.driver.click("auth_is_logged_in_test_btn")
        except NoSuchElementException:
            logging.error("Error occurred while selecting auth logged in test button")
            raise NoSuchElementException("Auth logged in test button not found.")

    def get_auth_is_logged_in_result(self):
        """
        returns the auth get token result
        :return:
        """
        return self.driver.get_attribute("auth_is_logged_in_result_txt", "text", displayed=False)
    
    def select_set_unsubscriber_btn(self):
        """
        From the Set Event Subscriber() page, select the the Set Unsubscriber btn
        """
        self.driver.swipe(anchor_element="auth_plugin_header_title", direction="up", distance=7)
        self.driver.scroll_element("set_unsubscriber_btn", direction="down", distance=1, time_out=3)
        self.driver.click("set_unsubscriber_btn")
    
    def select_cancel_btn(self):
        """
        Clicks the cancel button in the tests tab 
        """
        clicked = self.driver.click("cancel_btn", displayed=False, raise_e=False)
       
        if clicked:
            logging.info("Clicked the cancel button successfully.")
            return True
        else:
            logging.error("Cancel button not found or not clickable.")
            return False

    def get_auth_is_logged_in_result_false(self):
        """
        returns the auth get token result
        :return:
        """
        result = self.driver.get_attribute("auth_is_logged_in_result_txt_false", "text", displayed=False, raise_e=False)
        return json.loads(result)

    def verify_error_code_result(self):
        """
        verify the error code result
        """
        try:
            if self.driver.wait_for_object("error_code_result", displayed=False, raise_e=False, timeout=10):
                logging.info("Error code result found.")
                result_text = self.driver.get_attribute("error_code_result", "text", displayed=False)
                logging.info("Raw error code result")

                try:
                    result_json = json.loads(result_text)
                    logging.info("Successfully parsed error code result as JSON")
                    return result_json
                except json.JSONDecodeError as json_error:
                    logging.warning("Failed to parse error code result as JSON")
                    logging.info("Returning raw text")
                    return {"error": "json_parse_failed", "raw_text": result_text}

        except NoSuchElementException:
            logging.error("Error occurred while verifying error code result")
            raise NoSuchElementException("Error code result not found.")

    def verify_set_subscriber_result(self, btn):
        """
        Verify the result of the Set Subscriber operation 
        """
        # Swipe up until auth_plugin_header_title is found
        max_attempts = 7
        for attempt in range(max_attempts):
            if self.driver.wait_for_object("auth_plugin_header_title", displayed=True, raise_e=False, timeout=1):
                logging.info(f"Found auth_plugin_header_title on attempt {attempt + 1}")
                break
            else:
                logging.info("auth_plugin_header_title not found, swiping up...attempt {}".format(attempt + 1))
                self.driver.swipe(direction="up", distance=7)
        else:
            raise NoSuchElementException("auth_plugin_header_title not found after {} attempts.".format(max_attempts))
        
        logging.info("Found auth_plugin_header_title, proceeding with subscriber result verification...")
        self.select_set_subscriber_result_dropdown(btn)
        result = self.driver.get_attribute("event_subscriber_result", "text", displayed=False, raise_e=False)
        result_json = json.loads(result)

        if result_json is None:
            logging.info("Event subscriber result not found, scrolling to find it.")
            self.driver.scroll_element("event_subscriber_result", direction="down", distance=4, time_out=10)
            result = self.driver.get_attribute("event_subscriber_result", "text", displayed=False, raise_e=False)
            logging.info("Scrolled to find event subscriber result: {}".format(result))
        return result_json
    
    def send_text_to_additional_authorization_parameters(self, text):
        """
        send text parameter value to the additional authorization parameters field textbox
        """
        self.driver.click("additional_authorization_parameters_checkbox", displayed=False)
        self.driver.click("additional_authorization_parameters_textbox", displayed=False)
        self.driver.send_keys("additional_authorization_parameters_textbox", text)

    def auth_get_tenant_id_error(self):
        """
        returns the auth get tenant id error as a dictionary
        :return: dict
        """
        result = self.driver.get_attribute("auth_get_tenant_id_error", "Name", displayed=False)
        return json.loads(result)

    def verify_user_canceled_error_code_result(self):
        """
        verify the error code result for user canceled
        """
        try:
            if self.driver.wait_for_object("error_code_result", displayed=False, timeout=10):
                logging.info("Error code result found.")
                result = self.driver.get_attribute("error_code_result", "text", displayed=False)
                logging.info(f"Error code result: {result}")
                return result
            else:
                logging.error("Error code result not found.")
                return None
        except NoSuchElementException:
            logging.error("Error occurred while verifying error code result")
            raise NoSuchElementException("Error code result not found.")

    def select_set_subscriber_result_dropdown(self, dropdown_name, raise_e=True):
        """
        From the top navigation bar, select locator btn_name only if not already expanded.
        """
        if dropdown_name not in ["expand_auth_event_dropdown_1", "expand_auth_event_dropdown_2"]:
            raise ValueError(f"{dropdown_name} not a btn available in the top navigation bar")
    
        state = self.driver.get_attribute(dropdown_name, "ExpandCollapse.ExpandCollapseState")
        if state == "Collapsed":
            self.driver.click(dropdown_name, raise_e=raise_e)