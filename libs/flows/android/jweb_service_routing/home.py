from MobileApps.libs.flows.android.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow

class Home(JwebServiceRoutingFlow):
    flow_name = "home"

    def select_service_routing_tab(self):
        """
        Selects the native service routing tab on the bottom navigation bar
        """
        self.driver.click("native_service_routing_tab_btn")

    def select_weblet_tab(self):
        """
        Selects the weblet tab on the bottom navigation bar
        """
        self.driver.click("weblet_tab_btn")