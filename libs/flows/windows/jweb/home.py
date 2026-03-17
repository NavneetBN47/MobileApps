from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

class Home(JwebFlow):
    flow_name = "home"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_webview_mode(self, webview: int=1, raise_e: bool=False):
        """
        param: webview determines between rendering engine 
            WebView1 (Edge)
            WebView2 (Chromium)
        """
        if webview == 1:
            self.driver.click("webview_one_btn", timeout=3, raise_e=raise_e)
        else: 
            self.driver.click("webview_two_btn", timeout=3, raise_e=raise_e)

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
        if plugin_name not in ['App', 'Auth Browser', 'Auth', 'Data Collection', 'Device', 'Eventing', 'Service Routing', 'Event Service', 'Settings']:
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

########################################################################################################################
#                                                                                                                      #
#                                        VERIFICATION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

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

    def select_custom_plugins_tab_from_menu(self):
        """
        click the custom plugins tab from the menu
        """
        self.driver.click("expand_custom_plugins_menu_btn")

    def select_settings_tab_from_menu(self):
        """
        click the custom plugins tab from the menu
        """
        self.driver.click("settings_menu_btn")

    def select_service_routing_stack_btn(self):
        """
        From the service routing settings page, select the cell which changes the stack options
        """
        self.driver.click("change_stack_btn")

    def change_service_routing_stack(self, option):
        """
        From the change stack page, select the option provided as a parameter 
        """
        option = option.upper()

        if option not in ["LOCAL", "DEV", "PIE", "STAGING", "PRODUCTION", "MOCK", "CUSTOM", "INLINE"]:
            raise ValueError("stack option:{} not available".format(option))
        
        self.select_service_routing_stack_btn()
        self.driver.click("stack_option", format_specifier=[option])

    def select_enforce_navigation_toggle(self):
        """
        set the enforce navigation toggle to value
        """
        self.driver.click("enforce_whitelist_toggle")