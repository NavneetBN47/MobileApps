from MobileApps.libs.flows.android.jweb.jweb_flow import JwebFlow

class Console(JwebFlow):
    flow_name = "console"

    def get_console_text(self):
        """
        From the bottom console page, return the entire text log output
        """
        return self.driver.wait_for_object("console_text").text
    
    def select_toggle_expand_console(self, expand=False):
        """
        From the bottom console page, use the param :expand: to expand or hide console log
        """
        expanded = self.driver.wait_for_object("console_text", raise_e=False, timeout=2)
        if expand != expanded:
            self.driver.click("toggle_console_btn")
