from MobileApps.libs.flows.android.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class Home(JwebDocProviderFlow):
    flow_name = "home"

    def select_doc_provider_tab(self):
        """
        Selects the doc provider tab button in the bottom navigation bar
        """
        self.driver.click("doc_provider_tab_nav")

    def select_event_history_tab(self):
        """
        Selects the event history tab button in the bottom navigation bar
        """
        self.driver.click("event_history_tab_nav")

    def select_weblet_tab(self):
        """
        Selects the weblet tab button in the bottom navigation bar
        """
        self.driver.click("weblet_tab_nav")

    def verify_doc_provider_open(self):
        """
        Ensure that the Doc Provider App is open
        """
        return self.driver.wait_for_object("application_window", raise_e=False, timeout=2) is not False