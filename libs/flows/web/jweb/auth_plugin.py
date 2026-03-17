import json
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class AuthPlugin(JwebFlow):
    flow_name = "auth_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_auth_logged_in_toggle(self):
        """
        toggles the auth open item
        :return:
        """
        self.driver.click("auth_is_logged_in_toggle_item")

    def select_auth_logged_in_test(self, scroll=False, direction="up"):
        """
        clicks the auth logged in test
        :return:
        """
        if scroll:
            found = self.driver.wait_for_object("auth_is_logged_in_test_btn", raise_e=False, timeout=3)
            timeout = time() + 10
            while not found and timeout > time():
                self.driver.swipe(direction=direction)
                found = self.driver.wait_for_object("auth_is_logged_in_test_btn", raise_e=False, timeout=3)
        try:
            self.driver.click("auth_is_logged_in_test_btn", timeout=5)
        except ElementClickInterceptedException:
            self.driver.swipe(direction=direction, per_offset=0.65)
            self.driver.click("auth_is_logged_in_test_btn", timeout=5)

    def auth_logged_in_result(self):
        """
        returns the auth logged in result
        :return:
        """
        el_text = self.driver.get_attribute("auth_is_logged_in_result_txt", "text", timeout=15, displayed=False)
        return json.loads(el_text)

    def select_auth_get_token_open(self):
        """
        clicks the auth get token open
        :return:
        """
        self.driver.click("auth_get_token_open_item")

    def select_auth_get_token_test(self):
        """
        clicks the auth get token test button
        :return:
        """
        self.driver.click("auth_get_token_test_btn", displayed=False)

    def auth_get_token_result(self, raise_e=True):
        """
        returns the auth get token result
        :return:
        """
        get_token_result = self.driver.wait_for_object("auth_get_token_result_txt", timeout=20, raise_e=raise_e)
        if not raise_e and not get_token_result:
            return False
        return json.loads(get_token_result.text)

    def select_auth_get_token_close(self):
        """
        clicks the auth get token close
        :return:
        """
        self.driver.click("auth_get_token_close_item")

    def select_auth_user_interaction_entry_point_selector(self):
        """
        selects the user interaction starting point
        """
        self.driver.check_box("auth_user_interaction_entry_point_checkbox", attribute="aria-checked", uncheck=False)
        self.driver.click("auth_user_interaction_entry_point_selector", change_check={"wait_obj": "list_option_generic"})

    def select_auth_logout_open(self):
        """
        clicks the auth logout open
        :return:
        """
        self.driver.click("auth_logout_open_item")

    def select_auth_logout_test(self, delay=0):
        """
        clicks the auth logout test 
        :return:
        """
        self.driver.click("auth_logout_test_btn", delay=delay)

    def auth_logout_result(self):
        """
        :returns: the auth logout result
        """
        el_text = self.driver.wait_for_object("auth_logout_result_txt").text
        return json.loads(el_text)

    def select_auth_logout_close(self):
        """
        clicks the auth logout close
        :return:
        """
        self.driver.click("auth_logout_close_item")

    def select_auth_add_listener_btn(self):
        """
        clicks the add listener btn
        :return:
        """
        self.driver.click("auth_add_listener_btn")

    def select_auth_remove_listener_btn(self):
        """
        clicks the remove listener btn
        :return:
        """
        self.driver.click("auth_remove_listener_btn")

    def auth_listener_text_result(self):
        """
        :returns: listener text after adding listener to auth plugin
        """
        return json.loads(self.driver.wait_for_object("auth_listener_result_text").text)

    def select_send_token_options(self, value):
        """
        Set "Send Token Options" checkbox to given parameter value 
        """
        self.driver.check_box("auth_send_token_options_switch", attribute="aria-checked", uncheck=not value)

    def control_auth_token_switches(self, values):
        """
        Toggle auth token switches as they appear by passing in a list of five boolean for each toggle
            - Require Fresh Token
            - Allow Network Access
            - Allow User Interaction
            - Show Account Creation Link
            - Skip Token Refresh
        """
        for i, switch in enumerate(["requireFreshToken", "allowNetworkAccess", 
                                    "allowUserInteraction", "showAccountCreationLink", 
                                    "skipTokenRefresh"]):
            try:
                self.driver.check_box("auth_token_option_checkbox", format_specifier=[switch], attribute="aria-checked", uncheck=False)
                self.driver.click("auth_token_list_options", format_specifier=[switch])
                self.driver.click("auth_token_list_option", format_specifier=[switch, str(values[i]).lower()])
            except ElementClickInterceptedException:
                direction = "up" if i == 0 else "down"
                self.driver.swipe(direction=direction, per_offset=0.7)
                self.driver.check_box("auth_token_option_checkbox", format_specifier=[switch], attribute="aria-checked", uncheck=False)
                self.driver.click("auth_token_list_options", format_specifier=[switch])
                self.driver.click("auth_token_list_option", format_specifier=[switch, str(values[i]).lower()])

    def select_add_token_lifetime_option_btn(self):
        """
        Selects the 'Add Token Lifetime Option' button.
        """
        self.driver.check_box("auth_token_option_checkbox", format_specifier=["tokenLifetimeRequirements"], attribute="aria-checked", uncheck=False)
        self.driver.click("token_lifetime_btn")

    def change_token_type(self, token_lifetime_option):
        """
        Change the token type based on the given token lifetime option.
        :param token_lifetime_option: The token lifetime option to set
        """
        if token_lifetime_option not in ["preferredMaximumSecondsSinceIssued", "preferredMinimumSecondsUntilExpiration"]:
            raise ValueError("token lifetime option:{} not available, expecting preferredMaximumSecondsSinceIssued or preferredMinimumSecondsUntilExpiration".format(token_lifetime_option))
        self.driver.click("token_lifetime_type_dropdown")
        self.driver.click("token_lifetime_option", format_specifier=[token_lifetime_option])

    def send_text_to_token_lifetime_textbox(self, text):
        """
        Sends the specified text to the token lifetime textbox.
        :param text: The text to be sent to the textbox.
        """
        self.driver.click("token_lifetime_textbox", displayed=False)
        self.driver.send_keys("token_lifetime_textbox", text)

    def select_delete_token_lifetime_btn(self):
        """
        Selects the 'Delete' button under newly created token lifetime option
        """
        self.driver.click("token_lifetime_delete_btn")

    def select_user_interaction_entry_point(self, option):
        """
        Select specific Token Type to Request from dropdown menu    
        """
        if option not in ["signIn", "createAccount"]:
            raise ValueError("nav to sign in page option:{} not available".format(option))
        self.select_auth_user_interaction_entry_point_selector()
        self.driver.click("list_option", format_specifier=[option])

    def select_token_type_to_request(self, option):
        """
        Select specific Token Type to Request from dropdown menu    
        """
        option = option.lower()
        if option not in ["user", "device"]:
            raise ValueError("nav to sign in page option:{} not available".format(option))
        self.select_token_type_request_drop_down()
        self.driver.click("list_option", format_specifier=[option])
    
    def send_text_to_device_uuid_textbox(self, text):
        """
        From Auth.getToken() send text to Device UUID textbox
        """
        self.driver.check_box("auth_token_option_checkbox", format_specifier=["printerUUID"], attribute="aria-checked", uncheck=False)
        self.driver.send_keys("device_uuid_textbox", text)

    def select_token_type_request_drop_down(self):
        """
        From Auth.getToken() select Token Type to Request drop down menu
        """
        self.driver.click("token_type_request_menu")

    def send_text_to_scope_textbox(self, text):
        """
        send text parameter value to the auth scope field textbox
        """
        self.driver.check_box("auth_token_option_checkbox", format_specifier=["scopes"], attribute="aria-checked", uncheck=False)
        self.driver.selenium.js_clear_text("auth_scope_field_textbox")
        self.driver.send_keys("auth_scope_field_textbox", text)

    def send_text_to_tenant_id_textbox(self, text):
        """
        send text parameter value to the tenant id textbox
        """
        self.driver.check_box("auth_token_option_checkbox", format_specifier=["tenantID"], attribute="aria-checked", uncheck=False)
        self.driver.send_keys("auth_tenant_textbox", text)

    def select_set_set_subscriber_btn(self):
        """
        From the Set Event Subscriber() page, select the the Set Subscriber btn 
        """
        self.driver.click("set_subscriber_btn")
   
    def get_displayed_content(self):
        """
        Get the displayed content from the Auth Plugin      
        """
        return self.driver.get_attribute("error_display", "text")
    
    def select_get_token_chevron_btn(self):
        """
        From accounts page, click get token chevron button  
        """
        self.driver.click("get_token_chevron_btn")
    
    def select_qahp_smart_back_button(self):
        """
        From the get token page, click the back button
        """
        self.driver.click("qahp_smart_back_button")

    def verify_get_token_contents(self): 
        """ 
        in get token tab extract the content to verify whether the screen is empty   
        """
        return not self.driver.wait_for_object("get_token_content", timeout=3, raise_e=False) is False 
    
    def verify_get_account_content(self):
        """
        Get the displayed content from auth plugin
        """
        return not self.driver.wait_for_object("get_account_content", timeout=3, raise_e=False) is False 

    def event_subscriber_result(self):
        """
        returns the event subscriber result
        """
        return json.loads(self.driver.wait_for_object("event_subscriber_result").text)

    def select_app_settings_chevron(self):
        """
        From the auth plugin page, click the app settings chevron button
        """
        self.driver.swipe(direction="down", per_offset=0.7)
        self.driver.click("app_settings")

    def select_auth_provider(self):
        """
        From the auth plugin page, click the auth provider chevron button
        """
        self.driver.click("settings_auth_provider")
    
    def select_auth_provider_option(self, option):
        """ 
        Selects the authentication provider option from the settings menu.
        """
        if option not in ['stratus', 'oneCloud']:
            raise ValueError("{}: is not a option. option must be: 'stratus' or 'oneCloud'")
        
        self.driver.click("settings_auth_provider")
        self.driver.click("settings_auth_provider_menu_item", format_specifier=[option])

########################################################################################################################
#                                                                                                                      #
#                                        VERIFICATION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_at_auth_plugin(self, timeout=3):
        """
        verify that we are currently at the auth plugin page
        :return: bool
        """
        el = self.driver.get_attribute("auth_plugin_header_title", "text", raise_e=False, timeout=timeout, displayed=False)
        return False if el is False else el == 'Auth'

    def verify_logged_in_button(self):
        """
        verifies the loggedin button
        :return: WebElement if found, False otherwise
        """
        return self.driver.wait_for_object("logged_in_open_header_item", raise_e=False) 

    def verify_get_token_button(self):
        """
        verifies the get token button
        :return: WebElement if found, False otherwise
        """
        return self.driver.wait_for_object("auth_get_token_test_btn", raise_e=False)

    def verify_logout_button(self):
        """
        verifies the logout button
        :return: WebElement if found, False otherwise
        """
        return self.driver.wait_for_object("auth_logout_test_btn", raise_e=False)

    def verify_token_lifetime_options(self):
        """
        After opening the Token Lifetime requirements btn, verify the following options are available:
            - Token Lifetime DropDown menu
            - Token Lifetime TextBox
            - Token Lifetime Delete Btn
        """
        self.driver.wait_for_object("token_lifetime_type_dropdown")
        self.driver.wait_for_object("token_lifetime_textbox", displayed=False)
        self.driver.wait_for_object("token_lifetime_delete_btn")