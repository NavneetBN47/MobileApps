from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Home(JwebDataCollectionFlow):
    flow_name = "home"

    def select_top_nav_button(self, btn_name, raise_e=True):
        """
        From the top navigation bar, select locator btn_name
        """
        if btn_name not in ["data_collection_service_nav_btn", "retargeting_data_nav_btn", "settings_nav_btn", "bindings_cache_nav_btn", "filters_nav_btn", "weblet_page_nav_btn", 
                            "requests_nav_btn", "verbose_logs_nav_btn", "queue_nav_btn", "http_proxy_nav_btn", "value_store_nav_btn", "more_nav_btn", "accumulator_nav_btn"]:
            raise ValueError("{} not a a btn available in the top navigation bar".format(btn_name))
        self.driver.click(btn_name, raise_e=raise_e)

    def select_webview_engine(self, engine_name):
        """
        Once reference app is launched, select webview engine "WebView 1 (Default)" or "WebView2" to proceed further
        """
        if engine_name not in ["webview1_edge_engine", "webview2_chromium_engine"]:
            raise ValueError("{} not an engine available in the select webview engine pop-up".format(engine_name))
        self.driver.click(engine_name)