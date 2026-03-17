import json

from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

class BrowserPlugin(JwebFlow):
    project = "jweb"
    flow_name = "browser_plugin"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_browser_test(self):
        """
        Selects the test btn from the auth browser plugin tab
        """
        self.driver.click("browser_test_btn")

    def select_redirect_link(self):
        """
        After selecting the test btn, select the redirect link on the pop-up
        """
        self.driver.click("pretend_auth_redirect_link")

    def get_browser_sign_in_result_text(self):
        """
        :return: text under result after completing test
        """
        return self.driver.wait_for_object("browser_test_result").get_attribute("Name")