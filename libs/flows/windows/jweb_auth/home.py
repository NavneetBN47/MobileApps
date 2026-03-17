from MobileApps.libs.flows.windows.jweb_auth.jweb_auth_plugin_flow import JwebAuthFlow
from time import sleep

class Home(JwebAuthFlow):
    flow_name = "home"

    def select_top_nav_button(self, btn_name, raise_e=True):
        """
        From the top navigation bar, select locator btn_name
        """
        if btn_name not in ["tests_nav_btn", "log_nav_btn", "cred_nav_btn", "devices_nav_btn", "messages_nav_btn", "roam_nav_btn", 
                            "jweb_nav_btn", "custom_auth_nav_btn", "push_nav_btn", "options_nav_btn"]:
            raise ValueError("{} not a a btn available in the top navigation bar".format(btn_name))
        self.driver.click(btn_name, raise_e=raise_e)

    def select_create_account(self):
        """ 
        Selects the create account button
        """
        self.driver.click("create_account_btn")

    def select_ok_btn_in_pop_up(self):
        """ 
        Selects the ok button in the pop up
        """
        self.driver.click("ok_btn")
        sleep(8)

    def select_reference_btn(self):
        """ 
        Selects the reference button
        """
        self.driver.click("reference_btn")
        sleep(5)
    
    def select_menu(self, raise_e=False):
        """
        clicks the menu button
        """
        self.driver.click("menu_btn", timeout=3, raise_e=raise_e)

    def select_plugins_tab_from_menu(self):
        """
        clicks the plugins tab from the menu 
        """
        self.driver.click("expand_plugins_menu_btn")

    def select_plugin(self, plugin_name):
        """
        From the expanded plugins tab, select plugin_name
        """
        plugin_name = plugin_name.title()
        if plugin_name not in ['App', 'Auth Browser', 'Auth', 'Data Collection', 'Device', 'Eventing', 'Service Routing', 'Event Service']:
            raise ValueError("{} not present within list of available plugins".format(plugin_name))
        else:
            self.driver.click("plugin_item", format_specifier=[plugin_name])
    
    def select_plugin_from_home(self, plugin_name):
        """
        from app homepage, navigate to plugin_name
        """
        self.select_menu()
        if not self.verify_plugins_are_present():
            self.select_plugins_tab_from_menu()
        self.select_plugin(plugin_name)

    def verify_menu_button(self):
        """
        clicks the menu button
        """
        return self.driver.wait_for_object("menu_btn", timeout=15, raise_e=False)
    
    def verify_plugins_are_present(self):
        """
        From the homepage, verify that we are able to select plugins from the expanded plugins tab
        """
        return self.driver.wait_for_object("plugin_item", format_specifier=["App"], raise_e=False, timeout=1) is not False
    
    def select_stratus_using_browser_option(self):
        """
        Selects the stratus using browser option under the auth provider dropdown.
        """
        self.driver.click("select_auth_provider_option")
        self.driver.click("stratus_using_browser_option")
        
    def select_one_cloud_using_browser_option(self):
        """
        Selects the one cloud using browser option under the auth provider dropdown
        """
        self.driver.click("select_auth_provider_option")
        self.driver.click("one_cloud_using_browser_option")