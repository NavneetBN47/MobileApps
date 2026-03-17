from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time
import logging

class SuppliesStatus(SmartFlow):
    flow_name = "supplies_status"

    def verify_info_alert_title_in_pdp_screen(self,expected_title):
        self.driver.wait_for_object("info_alert_in_pdp_screen",timeout=30)
        actual_title = self.driver.wait_for_object("info_alert_in_pdp_screen").get_attribute("text")
        logging.info(f"Actual info alert title: {actual_title}")
        logging.info(f"Expected info alert title: {expected_title}")
        if expected_title not in actual_title:
            logging.error("info alert title text does not match expected spec")
            return False
        logging.info("info alert title matches expected spec")
        return True 
    
    def verify_error_alert_title_in_pdp_screen(self,expected_title):
        self.driver.wait_for_object("error_alert_in_pdp_screen",timeout=30)
        actual_title = self.driver.wait_for_object("error_alert_in_pdp_screen").get_attribute("text")
        logging.info(f"Actual error alert title: {actual_title}")
        logging.info(f"Expected error alert title: {expected_title}")
        if expected_title not in actual_title:
            logging.error("Error alert title text does not match expected spec")
            return False
        logging.info("Error alert title matches expected spec")
        return True 

    def verify_warning_alert_title_in_pdp_screen(self,expected_title):
        self.driver.wait_for_object("warning_alert_in_pdp_screen",timeout=30)
        actual_title = self.driver.wait_for_object("warning_alert_in_pdp_screen").get_attribute("text")
        logging.info(f"Actual warning alert title: {actual_title}")
        logging.info(f"Expected warning alert title: {expected_title}")
        if expected_title not in actual_title:
            logging.error("Warning alert title text does not match expected spec")
            return False
        logging.info("Warning alert title matches expected spec")
        return True

    def verify_info_alert_icon_in_pdp_screen(self,expected_icon):
        actual_icon = self.driver.wait_for_object("info_icon_in_pdp_screen").text
        if expected_icon not in actual_icon:
            logging.error("Info icon text does not match expected spec")
            return False
        logging.info("Info icon  matches expected spec")
        return True

    def verify_error_alert_icon_in_pdp_screen(self,expected_icon):
        actual_icon = self.driver.wait_for_object("error_icon_in_pdp_screen").text
        if expected_icon not in actual_icon:
            logging.error("Error icon text does not match expected spec")
            return False
        logging.info("Error icon  matches expected spec")
        return True
    
    def verify_color_icon_in_pdp_screen(self,expected_icon):
        actual_icon = self.driver.wait_for_object("color_icon_in_pdp_screen",timeout=30).text
        if expected_icon+" Ink Color" not in actual_icon:
            logging.error("Color icon text does not match expected spec")
            return False
        logging.info("Color icon  matches expected spec")
        return True

    def verify_warning_alert_icon_in_pdp_screen(self,expected_icon):
        actual_icon = self.driver.wait_for_object("warning_icon_in_pdp_screen").text
        if expected_icon not in actual_icon:
            logging.error("Warning icon text does not match expected spec")
            return False
        logging.info("Warning icon  matches expected spec")
        return True

    def verify_get_more_help_btn(self):
        logging.info("verifying secondary get more help button is present")
        self.driver.wait_for_object("get_more_help_btn")
        return True

    def verify_get_supplies_btn(self):
        logging.info("verifying secondary get supplies button is present")
        self.driver.wait_for_object("get_supplies_btn")
        return True

    def verify_primary_ok_button(self):
        logging.info("verifying primary Ok button is present")
        self.driver.wait_for_object("primary_ok_button")
        return True
        
    def verify_secondary_yes_button(self): 
        logging.info("verifying secondary Yes button is present")
        self.driver.wait_for_object("secondary_yes_button")
        return True

    def verify_secondary_no_button(self):
        logging.info("verifying secondary No button is present")
        self.driver.wait_for_object("secondary_no_button")
        return True

    def verify_secondary_continue_button(self):
        logging.info("verifying secondary Continue button is present")
        self.driver.wait_for_object("secondary_continue_button")
        return True

    def verify_secondary_go_to_hp_instant_ink_button(self):
        logging.info("verifying secondary GO to HP Instant Ink button is present")
        self.driver.wait_for_object("secondary_go_to_hp_instant_ink_button")
        return True

    def verify_primary_align_button(self):
        logging.info("verifying primary Align button is present")
        self.driver.wait_for_object("primary_align_button")
        return True

    def verify_secondary_ok_button(self): 
        logging.info("verifying secondary OK button is present")
        self.driver.wait_for_object("secondary_ok_button")
        return True

############################### Printer Status Screen Methods ###############################
    def click_error_alert_in_pdp_screen(self):
        self.driver.wait_for_object("error_alert_in_pdp_screen").click()
    
    def click_info_alert_in_pdp_screen(self):
        self.driver.wait_for_object("info_alert_in_pdp_screen").click()
    
    def click_warning_alert_in_pdp_screen(self):
        self.driver.wait_for_object("warning_alert_in_pdp_screen").click()

    def verify_myprinter_back_btn(self):
        self.driver.wait_for_object("back_btn_printer_status_screen")

    def verify_alert_severity_icon_printer_status_screen(self):
        self.driver.wait_for_object("alert_severity_icon_printer_status_screen")
        return True

    def get_alert_title_in_printer_status_screen(self):
        return self.driver.wait_for_object("alert_title_printer_status_screen").get_attribute("text")

    def verify_alert_title_in_printer_status_screen(self, expected_title):
        logging.info(f"Actual alert title: {self.get_alert_title_in_printer_status_screen()}")
        logging.info(f"Expected alert title: {expected_title}")
        if self.get_alert_title_in_printer_status_screen() != expected_title:
            logging.error("Alert title text does not match expected spec")
            return False
        return True

    def verify_sms_detailed_body(self,expected_body):
        actual_body = self.driver.wait_for_object("sms_detailed_body").get_attribute("text")
        logging.info(f"Actual SMS detailed body: {actual_body}")
        logging.info(f"Expected SMS detailed body: {expected_body}")
        if actual_body != expected_body:
            logging.error("SMS detailed body text does not match expected spec")
            return False
        return True
