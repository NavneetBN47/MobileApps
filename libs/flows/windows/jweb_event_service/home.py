from MobileApps.libs.flows.windows.jweb_event_service.jweb_event_service_flow import JwebEventServiceFlow

class Home(JwebEventServiceFlow):
    flow_name = "home"

    def select_weblet_btn(self, raise_e=True):
        """
        From the home page, select the 'Weblet' btn towards the top of the screen
        """
        self.driver.click("weblet_btn", raise_e=raise_e)

    def select_nav_back_btn(self):
        """
        From the home page, select the 'Weblet' btn towards the top of the screen
        """
        self.driver.click("nav_back_btn")

    def select_webview_engine(self, engine_name):
        """
        Once reference app is launched, select webview engine "WebView 1 (Default)" or "WebView2" to proceed further
        """
        if engine_name not in ["webview1_edge_engine", "webview2_chromium_engine"]:
            raise ValueError("{} not an engine available in the select webview engine pop-up".format(engine_name))
        self.driver.click(engine_name)

    def select_jweb_reference_btn(self, raise_e: bool=False):
        self.driver.click("jweb_reference_btn", raise_e=raise_e)

    def select_url_go_btn(self, raise_e: bool=False):
        self.driver.click("url_go_btn", raise_e=raise_e)

    def select_menu(self, raise_e=False):
        """
        clicks the menu button
        :return:
        """
        self.driver.click("menu_btn", timeout=3, raise_e=raise_e)

    def select_plugins_tab_from_menu(self):
        """
        clicks the plugins tab from the menu 
        :returns:
        """
        self.driver.click("expand_plugins_menu_btn")

    def select_plugin(self, plugin_name):
        plugin_name = plugin_name.title()
        if plugin_name not in ['App', 'Auth Browser', 'Auth', 'Data Collection', 'Device', 'Eventing', 'Service Routing', 'Event Service']:
            raise ValueError("{} not present within list of available plugins".format(plugin_name))
        else:
            self.driver.click("plugin_item", format_specifier=[plugin_name])
    
    def select_plugin_from_home(self, plugin_name):
        """
        from app homepage, navigate to plugin_name
        :return:
        """
        self.select_menu()
        if not self.verify_plugins_are_present():
            self.select_plugins_tab_from_menu()
        self.select_plugin(plugin_name)

    def verify_menu_button(self):
        """
        clicks the menu button
        :return:
        """
        return self.driver.wait_for_object("menu_btn", timeout=15, raise_e=False)
    
    def verify_plugins_are_present(self):
        """
        From the homepage, verify that we are able to select plugins from the expanded plugins tab
        :return: bool
        """
        return self.driver.wait_for_object("plugin_item", format_specifier=["App"], raise_e=False, timeout=1) is not False