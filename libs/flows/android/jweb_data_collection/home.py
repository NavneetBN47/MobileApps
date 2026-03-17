from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow


class Home(JwebDataCollectionFlow):
    flow_name = "home"

    def select_data_collection_service_tab(self):
        """
        clicks the data collection service button in the bottom navigation bar
        """
        self.driver.click("data_collection_service_tab_nav")

    def select_retargeting_data_tab(self):
        """
        clicks the retargeting data button in the bottom navigation bar
        """
        self.driver.click("retargeting_data_tab_nav")

    def select_cached_bindings_tab(self):
        """
        clicks the cached bindings button in the bottom navigation bar
        """
        self.driver.click("cached_bindings_tab_nav", delay=4)

    def select_filter_cdm_ledm_tab(self):
        """
        clicks the filter CDM/LEDM button in the bottom navigation bar
        """
        self.driver.click("filter_cdm_ledm_tab_nav")

    def select_webview_tab(self):
        """
        clicks the weblet in the bottom navigation bar
        """
        self.driver.click("webview_tab_nav")

    def select_settings_tab(self):
        """
        clicks the settings btn in the top right of any Data Collection Page
        """
        self.driver.click("settings_btn")