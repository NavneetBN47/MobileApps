from MobileApps.libs.flows.ios.jweb.jweb_plugin_flow import JwebPluginFlow

class Console(JwebPluginFlow):
    flow_name = "console"

    def get_console_text(self):
        """
        From the bottom console page, return the entire text log output
        """
        return self.driver.get_attribute("console_text", "text")

    def select_toggle_expand_console(self, expand=False):
        """
        Select the expand/contract console button
        """
        expanded = self.driver.wait_for_object("console_text", raise_e=False, timeout=2)
        if expand != expanded:
            self.driver.click("toggle_expand_console")
