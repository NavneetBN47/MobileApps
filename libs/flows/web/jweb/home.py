from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
from time import sleep

class Home(JwebFlow):
    flow_name = "home"

    def select_menu(self):
        """
        clicks the menu button
        """
        self.driver.click("menu_btn")

    def select_plugins_tab_from_menu(self):
        """
        clicks the plugins tab from the menu 
        """
        self.driver.click("expand_plugins_menu_btn")

    def select_custom_plugins_tab_from_menu(self):
        """
        click the custom plugins tab from the menu
        """
        self.driver.click("expand_custom_plugins_menu_btn")

    def select_plugin_from_home(self, plugin_name):
        """
        from app homepage, navigate to plugin_name
        """
        plugin_name = plugin_name.lower()
        self.select_menu()
        if plugin_name in ["app", "auth", "auth_browser", "device", "eventing", "event_service", "service_routing", "logger", "printer"]:
            plugin_name = plugin_name.split('_')[0] + ''.join(x.capitalize() or '_' for x in plugin_name.split('_')[1:])
            if not self.driver.wait_for_object("plugin_link", format_specifier=[plugin_name], raise_e=False, timeout=3):
                self.select_plugins_tab_from_menu()
            self.driver.click("plugin_link", format_specifier=[plugin_name.split('_')[0] + ''.join(x.capitalize() or '_' for x in plugin_name.split('_')[1:])])
        elif plugin_name == "settings":
            if not self.driver.wait_for_object("plugin_link", format_specifier=[plugin_name], raise_e=False, timeout=3):
                self.select_custom_plugins_tab_from_menu()
            self.driver.click("plugin_link", format_specifier=[plugin_name.split('_')[0] + ''.join(x.capitalize() or '_' for x in plugin_name.split('_')[1:])])
        else:
            raise ValueError("{} not a valid plugin name".format(plugin_name))
        self.driver.click("close_menu_btn", raise_e=False)

    def verify_menu_button(self):
        """
        verifies the menu button
        """
        return self.driver.wait_for_object("menu_btn", raise_e=False)

    def verify_main_page(self):
        """
        verifies presently at the main page of the application
        """
        return self.driver.wait_for_object("main_page_div", raise_e=False)

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
        self.driver.click("stack_option", format_specifier=['DEV'])
        
    def select_enforce_navigation_toggle(self):
        """
        set the enforce navigation toggle to value
        """
        self.driver.click("enforce_whitelist_toggle")