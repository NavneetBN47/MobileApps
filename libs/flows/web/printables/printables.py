from MobileApps.libs.flows.web.web_flow import WebFlow
from MobileApps.resources.const.web import const as w_const


class Printables(WebFlow):
    project = "printables"
    flow_name = "printables"
    url = "https://printables-stg.hp.com/us/en"
    
    def verify_printables_title(self):
        """
        Verify the printables title is present in the printables webview
        """
        self.driver.wait_for_context(w_const.WEBVIEW_URL.PRINTABLES)
        self.driver.wait_for_object("printables_title")
