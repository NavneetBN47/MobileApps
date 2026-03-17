from MobileApps.libs.flows.ios.jweb.jweb_plugin_flow import JwebPluginFlow

class System(JwebPluginFlow):
    flow_name = "system"

    def select_cancel(self, raise_e=True, timeout=3):
        """
        select 'Cancel' button for native iOS popup
        """
        self.driver.click("cancel_button", timeout=timeout, raise_e=raise_e)

    def select_continue(self):
        """
        select 'Continue' button for native iOS popup
        """
        self.driver.click("continue_button")
