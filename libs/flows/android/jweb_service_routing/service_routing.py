from MobileApps.libs.flows.android.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow

class ServiceRouting(JwebServiceRoutingFlow):
    flow_name = "service_routing"

    def select_settings_btn(self):
        """
        Under the Actions tab, select the Settings link
        """
        self.driver.click("settings_btn")

    def select_settings_checkbox(self, checkbox, value):
        """
        From the settings tab, select the checkbox so that it matches the bool value
        """
        if checkbox not in ['enforce_url_checkbox', 'enable_mocked_data_checkbox']:
            raise ValueError("checkbox name:{} was not valid. read select_settings_checkbox() function for available checkbox values".format("checkbox"))        
        self.driver.check_box(checkbox, uncheck=not value)

    def select_service_routing_stack_btn(self):
        """
        From the service routing settings page, select the cell which changes the stack options
        """
        self.driver.click("change_stack_btn")

    def select_stack(self, option):
        """
        Set JWeb Service Routing App to Stack to :stack:
        """
        option = option.upper()
        if option not in ["PRODUCTION", "STAGE", "PIE", "DEV"]:
            raise ValueError("Stack must be one of PRODUCTION, STAGE, PIE, or DEV. Received: {}".format(option))
        
        self.driver.click("stack_option", format_specifier=[option])