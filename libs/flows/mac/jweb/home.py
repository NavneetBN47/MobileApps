from MobileApps.libs.flows.mac.jweb.jweb_flow import JwebFlow

class Home(JwebFlow):
    flow_name = "home"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_menu(self):
        """
        clicks the menu button
        :return:
        """
        self.driver.click("menu_btn", timeout=15)

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
        return self.driver.wait_for_object("menu_btn", timeout=2, raise_e=False)
    
    def verify_plugins_are_present(self):
        """
        From the homepage, verify that we are able to select plugins from the expanded plugins tab
        :return: bool
        """
        return self.driver.wait_for_object("plugin_item", format_specifier=["App"], raise_e=False, timeout=1) is not False