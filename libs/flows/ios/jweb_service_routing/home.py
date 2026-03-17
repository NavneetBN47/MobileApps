from MobileApps.libs.flows.ios.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow

class Home(JwebServiceRoutingFlow):
    flow_name = "home"

    def select_service_routing_tab_btn(self):
        """
        Selects the native service routing page in the bottom navigation bar
        """
        self.driver.click("service_routing_tab_btn")

    def select_weblet_tab_btn(self):
        """
        Selects the weblet page in the bottom navigation bar
        """
        self.driver.click("weblet_tab_btn", timeout=5)

    def select_service_routing_settings_btn(self):
        """
        From the native service routing page, select the settings btn 
        """
        self.driver.click("settings_btn")
    
    def select_service_routing_stack_btn(self):
        """
        From the service routing settings page, select the cell which changes the stack options
        """
        self.driver.click("change_stack_btn")

    def change_service_routing_stack(self, option):
        """
        From the change stack page, select the option provided as a parameter 
        """
        option = option.capitalize()
        
        if option not in ['Mock', 'Local', 'Dev', 'Pie', 'Staging', 'Production']:
            raise ValueError("stack option:{} not present within options".format(option))

        self.driver.click("stack_option", format_specifier=[option])