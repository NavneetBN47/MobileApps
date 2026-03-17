from MobileApps.libs.flows.ios.jweb_auth.jweb_auth_flow import JwebAuthFlow

class JWebAuthSettings(JwebAuthFlow):
    flow_name = "jweb_auth_settings"

    def change_auth_provider(self, auth_provider_option):
        """
        From the JWeb Auth Settings page, click on the auth provider cell menu option and select the :auth_provider_option:
        :auth_provider_option: must be either 'stratus' or 'oneCloud'
        """
        if auth_provider_option not in ["stratus", "oneCloud"]:
            raise ValueError("Invalid auth provider option: {}".format(auth_provider_option))
        self.driver.click("auth_provider_cell_menu_option")
        self.driver.click("auth_provider_option", format_specifier=[auth_provider_option])

    def select_allow_network_access_toggle(self, toggle=True):
        """
        Toggles the 'Allow Network Access' switch
        """
        self.driver.check_box("allow_network_access_toggle", uncheck=not toggle)
    
    def select_allow_user_interaction_toggle(self, toggle=True):
        """
        Toggles the 'Allow User Interaction' switch
        """
        self.driver.check_box("allow_user_interaction_toggle", uncheck=not toggle)

    def select_show_account_creation_link_toggle(self, toggle=True):
        """
        Toggles the 'Show Account Creation Link' switch
        """
        self.driver.check_box("show_account_creation_link_toggle", uncheck=not toggle)

    def select_start_on_create_account_toggle(self, toggle=True):
        """
        Toggles the 'Start on Create Account' switch
        """
        self.driver.check_box("start_on_create_account_toggle", uncheck=not toggle)
    
    def select_skip_token_refresh_toggle(self, toggle=True):
        """
        Toggles the 'Skip Token Refresh' switch
        """
        self.driver.check_box("skip_token_refresh_toggle", uncheck=not toggle)
    
    def select_ucde_audience_toggle(self, toggle=True):
        """
        Toggles the 'UCDE Audience' switch
        """
        self.driver.check_box("ucde_audience_toggle", uncheck=not toggle)
    
    def select_setting_done_button(self):
        """
        From settings page, click done button 
        """
        self.driver.click("done_button")

    def select_back_btn(self):
        """
        From settings page, click back button
        """
        self.driver.click("back_btn")
    
    def update_get_device_token_resource_textfield(self):
        """
        From settings page, modify get device token resource textfield
        """
        self.driver.click("get_device_token_resource_textfield")
        self.driver.send_keys("get_device_token_resource_textfield", "d4fb89b5-d997-459a-9fd9-84f893c6e0e9")
    
    def select_get_token_btn(self):
        """
        From settings page, click get token button
        """
        self.driver.click("get_token_btn")
    
    def verify_get_device_token_response(self):
        """
        From settings page, verify get device token response
        """
        return self.driver.get_attribute("get_device_token_response","text")

    def control_auth_toggles(self, toggle_values):
        """
        Toggles the following switches based on the True/False values passed in the list:
            - Allow Network Access
            - Allow User Interaction
            - Show Account Creation Link
            - Start on Create Account
            - Skip Token Refresh
            - UCDE Audience
 
        :param toggle_values: List of boolean values [allow_network_access, show_account_creation_link, allow_user_interaction, skip_token_refresh]
        """
        if len(toggle_values) != 6:
            raise ValueError("Toggle_values must be a list of 6 boolean values.")
 
        # Toggle switches based on the values provided
        self.select_allow_network_access_toggle(toggle=toggle_values[0])
        self.select_allow_user_interaction_toggle(toggle=toggle_values[1])
        self.select_show_account_creation_link_toggle(toggle=toggle_values[2])
        self.select_start_on_create_account_toggle(toggle=toggle_values[3])
        self.select_skip_token_refresh_toggle(toggle=toggle_values[4])
        self.select_ucde_audience_toggle(toggle=toggle_values[5])