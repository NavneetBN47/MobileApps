from MobileApps.libs.flows.web.web_flow import WebFlow

class MacBrowserPopupFlow(WebFlow):
    flow_name = "mac_browser_popup_flow"
    project = "smart"

    def __init__(self, driver, window_name="main"):
        super(MacBrowserPopupFlow, self).__init__(driver, window_name=window_name)
    
    def verify_an_element_and_click(self, element, format_specifier=[], click=False, delay=0, raise_e=True):
        element_displayed = self.driver.wait_for_object(element, format_specifier=format_specifier, raise_e=raise_e)
        if element_displayed and click:
            self.driver.click(element, format_specifier=format_specifier, delay=delay, raise_e=raise_e)
        return element_displayed