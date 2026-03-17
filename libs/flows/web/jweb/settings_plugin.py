import json
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class SettingsPlugin(JwebFlow):
    flow_name="settings_plugin"

    def select_enforce_navigation_toggle(self, value):
        """
        set the enforce navigation toggle to value
        """
        if str(value).lower() != self.driver.wait_for_object("enforce_navigation_whitelist_toggle").get_attribute("aria-checked").lower():
            self.driver.click("enforce_navigation_whitelist_toggle")

    def select_service_routing_stack_option(self):
        self.driver.click("service_routing_stack_menu")

    def select_clear_cookies_btn(self):
        """
        click clear cookies btn from the settings plugin
        """
        self.driver.click("clear_cookies_btn")