from MobileApps.libs.flows.ios.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow
import time
import datetime

class Home(JwebDocProviderFlow):
    flow_name = "home"

    def select_doc_provider_tab(self):
        """
        Selects the doc provider page in the bottom navigation bar
        """
        self.driver.click("doc_provider_tab_nav")

    def select_event_history_tab(self):
        """
        Selects the event history page in the bottom navigation bar
        """
        self.driver.click("event_history_tab_nav")

    def select_weblet_tab(self):
        """
        Selects the weblet page in the bottom navigation bar
        """
        self.driver.click("weblet_tab_nav")

    def verify_doc_provider_open(self):
        """
        Ensure that the Doc Provider App is open
        """
        app_window = self.driver.wait_for_object("application_window", raise_e=False, timeout=3)
        if app_window is False:
            return False
        return "JarvisDocProviderExample" == self.driver.wait_for_object("application_window").text