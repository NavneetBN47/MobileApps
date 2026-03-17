import logging
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.common.common_flow import CommonFlow 

class SmartFlow(CommonFlow):
    #Base Flow for all involved platforms
    project = "smart"

    def __init__(self, driver):
        super(SmartFlow, self).__init__(driver, getattr(self, "platform", None))
    
    def verify_an_element_and_click(self, element, timeout=10, format_specifier=[], click=True, scroll=False, delay=0, raise_e=False):
        if scroll:
            element_displayed = self.driver.scroll(element, format_specifier=format_specifier, raise_e=raise_e)
        else:
            element_displayed = self.driver.wait_for_object(element, timeout=timeout, format_specifier=format_specifier, raise_e=raise_e)
        if element_displayed and click:
            self.driver.click(element, format_specifier=format_specifier, delay=delay, raise_e=raise_e)
        return element_displayed
    
    def verify_array_of_elements(self, array_elements, direction="down", scroll_object=None):
        element_missing = []
        for element in array_elements:
            if not self.driver.wait_for_object(element, raise_e=False):
                if not self.driver.scroll(element, direction=direction, scroll_object=scroll_object, raise_e=False):
                    element_missing.append(element)
        if element_missing:
            raise NoSuchElementException("Following options {}:not displayed".format(element_missing))
    
    def get_options_listed(self, option, format_specifier=[]):
        options = []
        options_list = self.driver.find_object(option, format_specifier=format_specifier, multiple=True)
        if len(options_list) < 1:
            raise NoSuchElementException(option + "not displayed")
        for i in range(len(options_list)):
            option_name = options_list[i].get_attribute("name")
            options.append(option_name.encode("ascii", "ignore").decode())
        logging.debug(options)
        return options
    
    def select_navigate_back(self, index=0, delay=None):
        self.driver.click("back_arrow_btn", index=index, delay=delay)
    
    def verify_static_text(self, text_option, raise_e=False):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[text_option], raise_e=raise_e)
    
    def select_static_text(self, text):
        self.driver.click("visible_dynamic_text", format_specifier=[text])
    
    def select_next(self):
        self.driver.click("next_btn")
    
    def select_yes(self):
        self.driver.click("yes_btn")
    
    def select_no(self):
        self.driver.click("no_btn")
    
    def select_close(self):
        self.driver.click("_shared_close")
########################################################################################################################
#                                                                                                                      #
#                                                  Mac Functions                                                       #
#                                                                                                                      #
########################################################################################################################

    def focus_on_hpsmart_window_mac(self, timeout=10):
        """
        Focus on HP Smart window on mac if another window is on top of it
        """
        self.driver.click("hpsmart_window", timeout=timeout)