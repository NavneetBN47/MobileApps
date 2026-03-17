from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare, string_validation
from selenium.webdriver.common.keys import Keys


class PrinterNameAndLocation(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Printer Name and Location Page
    """
    file_path = __file__
    flow_name = "printer_name_location_page"

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################
    
    def enter_printer_name_and_location(self):
        """
        Enter Printer name and location on Give printer name and location page and verify only 32  characters can be entered.
        """
        name = "abcdefghijklmnopqrstuvwxyz1234567"
        location = "123456abcdefghijklmnopqrstuvwxyz1"
        self.driver.click("printer_name")
        self.driver.click("printer_location")
        self.driver.send_keys("printer_name", name)
        self.driver.send_keys("printer_location", location)
        if len(self.driver.get_attribute("printer_name", "value")) != 32:
            raise AssertionError("Input characters disparity with requirment spec")
        if len(self.driver.get_attribute("printer_location", "value")) != 32:
            raise AssertionError("Input characters disparity with requirment spec")
        
    def click_printer_name_and_location_continue_btn(self):
        self.driver.click("buttons_continue")

    def click_printer_name_page_skip_btn(self):
        """
        Click Skip button on enter printer name and printer location.
        """
        self.driver.click("buttons_skip")

    def click_printer_name(self):
        """
        Click printer name input box
        """
        self.driver.click("printer_name")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="printer_name_location_page")
    def verify_printer_name_location_page(self):
        """
        verify printer name input box on Give your printer a name and location page also
        verify printer name and location helper text.
        """
        self.driver.wait_for_object("printer_name_location_page", timeout=30)
        self.driver.wait_for_object("printer_name", timeout=30)
        self.driver.wait_for_object("printer_location")
        self.driver.wait_for_object("name_helper_text")
        self.driver.wait_for_object("location_helper_text")

    @string_validation("header")
    @string_validation("subhead")
    @string_validation("name_label")
    @string_validation("location_label")
    @string_validation("name_helper_text")
    @string_validation("location_helper_text")
    def verify_printer_name_location_header(self, raise_e=False):
        """
        Verify Header description text on Give printer name and location page
        """
        self.driver.wait_for_object("header")

    def verify_printer_name_location_helper_caption_text(self):
        """
        Verify Caption test for printer anme and location Page
        """
        self.driver.wait_for_object("helper_text_caption", displayed=False)