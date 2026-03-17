from MobileApps.libs.flows.android.jweb_value_store.jweb_value_store_flow import JwebValueStoreFlow

class Home(JwebValueStoreFlow):
    flow_name = "home"
    
    def select_native_tab_nav(self):
        """
        From the bottom navigation bar, select the Native button
        """
        self.driver.click("native_tab_nav")

    def select_weblet_tab_nav(self):
        """
        From the bottom navigation bar, select the Weblet button
        """
        self.driver.click("weblet_tab_nav")