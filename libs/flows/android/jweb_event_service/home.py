from MobileApps.libs.flows.android.jweb_event_service.jweb_event_service_flow import JwebEventServiceFlow

class Home(JwebEventServiceFlow):
    flow_name = "home"

    def select_publishers_tab(self):
        """
        Selects the input page in the bottom navigation bar
        """
        self.driver.click("publishers_tab_btn")

    def select_subscribers_tab(self):
        """
        Selects the input page in the bottom navigation bar
        """
        self.driver.click("subscribers_tab_btn")

    def select_events_tab(self):
        """
        Selects the input page in the bottom navigation bar
        """
        self.driver.click("events_tab_btn")

    def select_weblet_tab(self):
        """
        Selects the input page in the bottom navigation bar
        """
        self.driver.click("weblet_tab_btn")