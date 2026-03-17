import types
import logging
import time
from MobileApps.libs.ma_misc import ma_misc
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow
from selenium.common.exceptions import ElementNotInteractableException, JavascriptException


class MissingWebDriver(Exception):
    pass

class UnexpectedURLError(Exception):
    pass


class WebFlow(BaseFlow, metaclass=ABCMeta):
    system = "web"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        #Driver: Your appium/selenium driver object
        #Context: When using these are webview flows you should pass in what context
        #The flow should expect to be in 
        #url: The partial/full URL of the window you are expecting to be at after switching to the webivew (appium usages only)
        #Window_name: When using the flow in a multi window setup make sure you pass in the window name the flow is associated io
        super(WebFlow, self).__init__(driver)
        self.logging_ignore_methods.append("wrapper")
        self.wn = window_name
        self.load_web_system_ui()
        if context is not None:
            self.context = context
        self.url = url

    def load_web_system_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map, append=True)
        return True

    def dismiss_connection_not_private(self):
        if self.driver.wait_for_object("_system_chrome_not_private_advanced_btn", timeout=5, raise_e=False):
            self.driver.click("_system_chrome_not_private_advanced_btn")
            self.driver.click("_system_chrome_not_private_proceed_link")
        return True

    def verify_web_page(self, sub_url=None, timeout=60, raise_e=True):
        start_time = time.time()
        while time.time() - start_time <=timeout:
            for window in self.driver.wdvr.window_handles:
                self.driver.wdvr.switch_to.window(window)
                cur_url = self.driver.current_url
                sub_url = self.flow_url if sub_url is None else sub_url 
                if sub_url in cur_url:
                    return True
            time.sleep(5)

        if raise_e:
            raise UnexpectedURLError("Expecting: " + self.flow_url + " got: " + cur_url)
        else:
            return False

    def verify_existed_context(self, context, timeout=10):
        """
        Verify a context in context list or not in timeout
        :return True -> existed. False -> unexisted.
        """
        timeout = time.time() + timeout
        while time.time() < timeout:
            if context in self.driver.wdvr.contexts:
                return True
        return False

    def dismiss_safari_connection_not_private(self):
        if self.driver.wait_for_object("_system_safari_not_private_show_details", timeout=5, raise_e=False):
            self.driver.click("_system_safari_not_private_show_details")
            self.driver.click("_system_safari_not_private_visit_this_website")
        return True

    def clear_browser_data_firefox(self):
        """
        Method for clearing browser data 
        """
        # Clear firefox brwser data method not ready yet.
        self.driver.wdvr.get("about:preferences#privacy")

    def clear_chrome_browsing_data(self):
        """
        Method for Clearing Browsing data for chrome browser
        """
        te = ('return document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("#privacy > settings-privacy-page-index").shadowRoot.querySelector("#privacy").shadowRoot.querySelector("settings-section > settings-clear-browsing-data-dialog-v2").shadowRoot.querySelector("#deleteButton").click()')
        t_ = ('return document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("#basicPage > settings-section:nth-child(12) > settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("#clearButton").click()')
        self.driver.navigate("chrome://settings/clearBrowserData")
        self.handle_browser_alert_present(accept=True)
        time.sleep(2) # Sometimes browser may take a sec to load settings.
        try: # selenium click method retuns Nonetype. Sometimes for chrome Linux te does not work
            self.driver.execute_script(te)
        except (ElementNotInteractableException, JavascriptException):
            self.driver.execute_script(t_)
        logging.info("All Browsing Data Deleted")

    def clear_downloaded_file(self):
        """
        Method for clearing downloaded file on download history page of browser
        """
        close_js_path = ("return document.querySelector('body > downloads-manager').shadowRoot.querySelector('#frb0').shadowRoot.querySelector('#quick-remove').shadowRoot.querySelector('#maskedImage').click();")
        try:
            self.driver.execute_script(close_js_path)
            logging.info("Downloaded file cleared successfully from browser download history")
        except (ElementNotInteractableException, JavascriptException):
            logging.error("Failed to clear downloaded file from browser download history")
    
    def clear_edge_browsing_data(self):
        """
        Method for Clearing Browsing data for edge browser
        """
        self.driver.wdvr.get("edge://settings/clearBrowserData")
        self.driver.click("_system_edge_clear_now_btn")

    def handle_browser_alert_present(self, accept=True, raise_e=False):
        """
        Method for handling browser alert: if browser alert is present accept or dismiss it
        """
        if self.driver.check_if_browser_alert_present(raise_e=raise_e) is True:
            self.driver.accept_or_dismiss_browser_alert(accept=accept)
    
    def get_key_modified_dictionary_from_spec(self, file_name):
        data = ma_misc.load_json_using_absolute_path(file_name)
        return self.add_parent_key_to_child_key(data)
    
    
    def add_parent_key_to_child_key(self, data, parent_key="", result=None):
        """
        This Function will take in a dictionary that may contain dictionaries and lists containing dictionaries modifiy the child key with parents key
        e.g {"jokes":{"bad":1, "good":3}} --> {"jokes_bad":1, "jokes_good":3}
        """
        if result is None:
            result = {}

        if isinstance(data, dict):
            for key, value in data.items():
                modified_key = f"{parent_key}_{key}" if parent_key else key
                if isinstance(value, dict):
                    self.add_parent_key_to_child_key(value, modified_key, result)
                elif isinstance(value, list):
                    for index, item in enumerate(value):
                        self.add_parent_key_to_child_key(item, f"{modified_key}[{index}]", result)
                else:
                    result[modified_key] = value

        elif isinstance(data, list):
            for index, item in enumerate(data):
                self.add_parent_key_to_child_key(item, f"{parent_key}[{index}]", result)

        return result       
        