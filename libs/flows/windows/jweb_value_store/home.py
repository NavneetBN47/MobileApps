from MobileApps.libs.flows.windows.jweb_value_store.jweb_value_store_flow import JwebValueStoreFlow

class Home(JwebValueStoreFlow):
    flow_name = "home"

    def select_weblet_tab_nav(self):
        """
        Select the Weblet button from the top navigation options
        """
        self.driver.click("weblet_nav")
