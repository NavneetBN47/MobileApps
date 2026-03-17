from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Home(JwebDataCollectionFlow):
    flow_name = "home"

    def select_data_collection_tab(self):
        """
        clicks the Data Collection button in the bottom navigation bar
        """
        self.driver.click("data_collection_tab_nav")

    def select_retargeting_data_tab(self):
        """
        clicks the Retargeting Data button in the bottom navigation bar
        """
        self.driver.click("retargeting_data_tab_nav")

    def select_data_valve_tab(self):
        """
        clicks the Data Valve button in the bottom navigation bar
        """
        self.driver.click("data_valve_tab_nav")

    def select_webview_tab(self):
        """
        clicks the weblet button in the bottom navigation bar
        """
        self.driver.click("webview_tab_nav")