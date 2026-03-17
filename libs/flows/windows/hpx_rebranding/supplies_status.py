from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import logging
import re

class SuppliesStatus(HPXRebrandingFlow):
    flow_name = "supplies_status"

    def get_C_cartridge_supplies_status(self):
        return self.driver.wait_for_object("get_C_cartridge_supply_status").get_attribute("Name")

    def get_M_cartridge_supplies_status(self):
        return self.driver.wait_for_object("get_M_cartridge_supply_status").get_attribute("Name")

    def get_Y_cartridge_supplies_status(self):
        return self.driver.wait_for_object("get_Y_cartridge_supply_status").get_attribute("Name")

    def get_K_cartridge_supplies_status(self):
        return self.driver.wait_for_object("get_K_cartridge_supply_status").get_attribute("Name")

    def get_m_cartridge_value(self):
        element = self.driver.wait_for_object("get_m_cartridge_value")
        value = element.get_attribute("Value")
        if value is None:
            value = element.get_attribute("Name")
        return value

    def get_c_cartridge_value(self):
        element = self.driver.wait_for_object("get_c_cartridge_value")
        value = element.get_attribute("Value")
        if value is None:
            value = element.get_attribute("Name")
        return value

    def get_y_cartridge_value(self):
        element = self.driver.wait_for_object("get_y_cartridge_value")
        value = element.get_attribute("Value")
        if value is None:
            value = element.get_attribute("Name")
        return value

    def get_k_cartridge_value(self):
        element = self.driver.wait_for_object("get_k_cartridge_value")
        value = element.get_attribute("Value")
        if value is None:
            value = element.get_attribute("Name")
        return value

    def verify_printer_status_error_alert_strings(self,alert_string):
        self.driver.swipe(direction="down")
        if self.driver.wait_for_object("supply_status_error_message",timeout=30,raise_e=False) == False:
            self.driver.swipe(direction="down")
            self.driver.wait_for_object("supply_status_error_message")
            logging.info("Swiped down to find supply status error message")
        logging.info(f"Validating alert title: {self.get_printer_status_error_alert_strings()} is matched with {alert_string}")
        if self.get_printer_status_error_alert_strings() == alert_string:
            logging.info(f"{alert_string} alert title is present & matched with actual alert title")
            return True
        else:
            logging.error(f"{alert_string} & {self.get_printer_status_error_alert_strings()} is mismatched")
            return False

    def get_printer_status_error_alert_strings(self):
        logging.info(f"Getting printer status error alert strings")
        return self.driver.wait_for_object("supply_status_error_message",timeout=30).get_attribute("Name")

    def verify_printer_status_error_alert_icon_home_page(self, exp_printer_status_icon):
        logging.info("Verifying printer status error alert icon on home page")
        if self.get_printer_status_error_alert_icon_home_page() == exp_printer_status_icon:
            logging.info(f"{exp_printer_status_icon} icon is present in cartridge status")
            return True
        else:
            logging.error(f"Expected:{exp_printer_status_icon} icon is not present in cartridge status")
            logging.error(f"Actual:{self.get_printer_status_error_alert_icon_home_page()} ")
            raise AssertionError(f"{exp_printer_status_icon} icon is not present in cartridge status")

    def get_printer_status_error_alert_icon_home_page(self):
        logging.info("Getting printer status error alert icon on home page")
        return self.driver.wait_for_object("supply_status_icon_error_alert_home_page").get_attribute("Name")

    def get_detailed_info_about_printer_status_alert(self):
        alert_body_text = self.driver.wait_for_object("printer_status_body_text").get_attribute("Name")
        cleaned_alert_body_text = self.clean_alert_strings(alert_body_text)
        return cleaned_alert_body_text

    def clean_alert_strings(self, text):
        """Clean text by removing all types of newlines and escape sequences"""
        if not text:
            return ""

        cleaned_text = text.replace('\\r\\n', ' ')  # JSON escaped CRLF
        cleaned_text = cleaned_text.replace('\\n', ' ')   # JSON escaped LF
        cleaned_text = cleaned_text.replace('\r\n', ' ')  # Actual CRLF
        cleaned_text = cleaned_text.replace('\n', ' ')    # Actual LF
        cleaned_text = cleaned_text.replace('\r', ' ')    # Actual CR
        
        cleaned_text = cleaned_text.replace('\\"', '"')
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = cleaned_text.strip()

        return cleaned_text

    def verify_detailed_info_about_printer_status_alert(self, expected_info):
        cleaned_expected_info = self.clean_alert_strings(expected_info)
        cleaned_alert_body_text = self.get_detailed_info_about_printer_status_alert()

        logging.info(f"Expected (cleaned): {repr(cleaned_expected_info)}")
        logging.info(f"Actual (cleaned): {repr(cleaned_alert_body_text)}")

        if cleaned_alert_body_text == cleaned_expected_info:
            logging.info(f"Detailed Printer Status Error info is correct")
            return True
        else:
            logging.error(f"Text comparison failed!")
            logging.error(f"Expected: {repr(cleaned_expected_info)}")
            logging.error(f"Actual: {repr(cleaned_alert_body_text)}")
            logging.error(f"Length diff: Expected={len(cleaned_expected_info)}, Actual={len(cleaned_alert_body_text)}")
            return False

    def verify_printer_status_warning_alert_strings(self, alert_string):
        self.driver.swipe(direction="down")
        if self.driver.wait_for_object("supply_status_warning_message",timeout=30,raise_e=False) == False:
            self.driver.swipe(direction="down")
            self.driver.wait_for_object("supply_status_warning_message")
            logging.info("Swiped down to find supply status warning message")
        logging.info(f"Validating alert title: {self.get_printer_status_warning_alert_strings()} is matched with {alert_string}")
        if self.get_printer_status_warning_alert_strings() == alert_string:
            logging.info(f"{alert_string} alert is present & is matched with actual alert title")
            return True
        else:
            logging.error(f"{alert_string} & {self.get_printer_status_warning_alert_strings()} alert is mismatched")
            return False

    def get_printer_status_warning_alert_strings(self):
        return self.driver.wait_for_object("supply_status_warning_message",timeout=30).get_attribute("Name")

    def verify_printer_status_warning_alert_icon_home_page(self, exp_printer_status_icon):
        logging.info("Verifying printer status warning alert icon on home page")
        if self.get_printer_status_warning_alert_icon_home_page() == exp_printer_status_icon:
            logging.info(f"{exp_printer_status_icon} icon is present in cartridge status")
            return True
        else:
            logging.error(f"Expected:{exp_printer_status_icon} icon is not present in cartridge status")
            logging.error(f"Actual:{self.get_printer_status_warning_alert_icon_home_page()} ")
            raise AssertionError(f"{exp_printer_status_icon} icon is not present in cartridge status")

    def get_printer_status_warning_alert_icon_home_page(self):
        return self.driver.wait_for_object("supply_status_icon_warning_alert_home_page").get_attribute("Name")

    def verify_printer_status_information_alert_strings(self, alert_string):
        self.driver.swipe(direction="down")
        if self.driver.wait_for_object("supply_status_information_message",timeout=30,raise_e=False) == False:
            self.driver.swipe(direction="down")
            self.driver.wait_for_object("supply_status_information_message")
            logging.info("Swiped down to find supply status information message")
        logging.info(f"Validating alert title: {self.get_printer_status_information_alert_strings()} is matched with {alert_string}")
        if self.get_printer_status_information_alert_strings() == alert_string:
            logging.info(f"{alert_string} alert is present & is matched with actual alert title")
            return True
        else:
            logging.error(f"{alert_string} & {self.get_printer_status_information_alert_strings()} alert is mismatched")
            return False

    def get_printer_status_information_alert_strings(self):
        return self.driver.wait_for_object("supply_status_information_message",timeout=30).get_attribute("Name")

    def verify_printer_status_information_alert_icon_home_page(self, exp_printer_status_icon):
        logging.info("Verifying printer status information alert icon on home page")
        if self.get_printer_status_information_alert_icon_home_page() == exp_printer_status_icon:
            logging.info(f"{exp_printer_status_icon} icon is present in cartridge status")
            return True
        else:
            logging.error(f"Expected:{exp_printer_status_icon} icon is not present in cartridge status")
            logging.error(f"Actual:{self.get_printer_status_information_alert_icon_home_page()} ")
            raise AssertionError(f"{exp_printer_status_icon} icon is not present in cartridge status")

    def get_printer_status_information_alert_icon_home_page(self):
        return self.driver.wait_for_object("supply_status_icon_information_alert_home_page",timeout=30).get_attribute("Name")

    def verify_cartridge_colour_icon(self, colour):
        if colour.upper() == "Y": 
            logging.info(f"Verifying cartridge colour icon is: {self.driver.wait_for_object('cartridge_colour_icon_y', timeout=30).get_attribute('Name')}")
            return self.driver.wait_for_object("cartridge_colour_icon_y").get_attribute("Name") == colour.upper()
        elif colour.upper() == "M":
            logging.info(f"Verifying cartridge colour icon is: {self.driver.wait_for_object('cartridge_colour_icon_m', timeout=30).get_attribute('Name')}")
            return self.driver.wait_for_object("cartridge_colour_icon_m").get_attribute("Name") == colour.upper()
        elif colour.upper() == "C":
            logging.info(f"Verifying cartridge colour icon is: {self.driver.wait_for_object('cartridge_colour_icon_c', timeout=30).get_attribute('Name')}")
            return self.driver.wait_for_object("cartridge_colour_icon_c").get_attribute("Name") == colour.upper()
        elif colour.upper() == "K":
            logging.info(f"Verifying cartridge colour icon is: {self.driver.wait_for_object('cartridge_colour_icon_k', timeout=30).get_attribute('Name')}")
            return self.driver.wait_for_object("cartridge_colour_icon_k").get_attribute("Name") == colour.upper()
   
    def verify_ok_btn(self):
        logging.info("Verifying Primary Button: OK button is present")
        self.driver.wait_for_object("ok_btn")
        return True

    def verify_get_more_help_btn(self):
        logging.info("verifying secondary button get more help button is present")
        self.driver.wait_for_object("get_more_help_btn")
        return True

    def verify_get_supplies_btn(self):
        logging.info("verifying secondary button get supplies button is present")
        self.driver.wait_for_object("get_supplies_btn")
        return True

    def verify_yes_btn(self):
        logging.info("Verifying secondary button: Yes button is present")
        self.driver.wait_for_object("yes_btn")
        return True

    def verify_no_btn(self):
        logging.info("Verifying secondary button: No button is present")
        self.driver.wait_for_object("no_btn")
        return True

    def verify_align_btn(self):
        logging.info("Verifying primary Align button is present")
        self.driver.wait_for_object("align_btn")
        return True

    def verify_continue_btn(self):
        logging.info("Verifying primary Continue button is present")
        self.driver.wait_for_object("continue_btn")
        return True

    def verify_printer_information_btn(self):
        self.driver.wait_for_object("printer_information_btn")
        return True

    def verify_network_information_btn(self):
        self.driver.wait_for_object("network_information_btn")
        return True

    def verify_printer_advanced_settings_btn(self):
        self.driver.wait_for_object("printer_advanced_settings_btn")
        return True

    def verify_printer_reports_btn(self):
        self.driver.wait_for_object("printer_reports_btn")
        return True

    def verify_print_quality_tools_btn(self):
        self.driver.wait_for_object("print_quality_tools_btn")
        return True

    def verify_alert_title_after_clicked(self):
        logging.info("Verifying alert title after clicking on the alert message")
        self.driver.wait_for_object("supply_status_alert_title_clicked", timeout=20)
        logging.info("Alert title is present after clicking on the alert message")
        return self.driver.wait_for_object("supply_status_alert_title_clicked", timeout=20).get_attribute("Name")

    def verify_printer_status_alert_present(self):
        logging.info("Verifying printer status alert is present")
        if not self.driver.wait_for_object("printer_status_alert_group", timeout=30, raise_e=False):
            logging.info("Printer status alert is NOT present")
            return False
        logging.info("Printer status alert is present")
        return True

    def scroll_to_printer_card(self):
        self.driver.swipe(distance=3)
        if not self.driver.wait_for_object("printer_card", raise_e=False):
            self.driver.swipe("printer_card")
        card_element = self.driver.wait_for_object("printer_card", raise_e=False)
        if card_element:
            logging.info("Printer card found")
            return True
        else:
            logging.error("Printer card not found after swiping")
            return False

    def verify_no_printers_found_page(self):
        self.driver.wait_for_object("no_printers_found", timeout=60,raise_e=False)

    def add_printer_by_using_ip_if_no_printers_found(self):
        if self.driver.wait_for_object("add_printer_by_using_ip_btn",timeout=60,raise_e=False) != False:
            logging.info("clicking on add printer by using ip button ")
            self.driver.click("add_printer_by_using_ip_btn")

    def verify_printer_card_present(self):
        logging.info("Verifying printer card is present")
        if self.driver.wait_for_object("printer_card",timeout=30,raise_e=False) == False:
            logging.info("Swiping down to find printer card")
            self.driver.swipe(direction="down")
        self.driver.wait_for_object("printer_card", timeout=30)
        logging.info("Printer card is present")
        return True

    def verify_info_icon_in_pdp(self):
        self.driver.wait_for_object("info_icon_in_pdp")
        return True

    def verify_info_alert_title_in_pdp(self, exp_info_title):
        info_alert_title = self.driver.wait_for_object("info_alert_title_in_pdp").get_attribute("Name")
        if info_alert_title == exp_info_title:
            logging.info(f"Info title in PDP is correct: {info_alert_title}")
            return True
        else:
            logging.error(f"Expected info title in PDP: {exp_info_title}, but got: {info_alert_title}")
            return False
    
    def verify_error_icon_in_pdp(self):
        self.driver.wait_for_object("error_icon_in_pdp")
        return True

    def verify_error_alert_title_in_pdp(self, exp_error_title):
        error_alert_title = self.driver.wait_for_object("error_alert_title_in_pdp").get_attribute("Name")
        if error_alert_title == exp_error_title:
            logging.info(f"Error title in PDP is correct: {error_alert_title}")
            return True
        else:
            logging.error(f"Expected error title in PDP: {exp_error_title}, but got: {error_alert_title}")
            return False
    
    def verify_warning_icon_in_pdp(self):
        self.driver.wait_for_object("warning_icon_in_pdp")
        return True

    def verify_warning_alert_title_in_pdp(self, exp_warning_title):
        warning_alert_title = self.driver.wait_for_object("warning_alert_title_in_pdp").get_attribute("Name")
        if warning_alert_title == exp_warning_title:
            logging.info(f"Warning title in PDP is correct: {warning_alert_title}")
            return True
        else:
            logging.error(f"Expected warning title in PDP: {exp_warning_title}, but got: {warning_alert_title}")
            return False
        
    def verify_get_supplies_page(self, timeout=30, raise_e=True):
        if self.driver.wait_for_object("i_accept_btn", timeout=timeout, raise_e=False):
            self.driver.click("i_accept_btn")
        return self.driver.wait_for_object("get_supplies_for_text", timeout=2, raise_e=raise_e)

################################### click Actions #############################################################

    def click_get_more_help_btn(self):
        self.driver.click("get_more_help_btn")

    def click_get_supplies_btn(self):
        self.driver.click("get_supplies_btn")

    def click_printer_information_btn(self):
        self.driver.click("printer_information_btn")

    def click_network_information_btn(self):
        self.driver.click("network_information_btn")

    def click_printer_advanced_settings_btn(self):
        self.driver.click("printer_advanced_settings_btn")

    def click_printer_reports_btn(self):
        self.driver.click("printer_reports_btn")

    def click_print_quality_tools_btn(self):
        self.driver.click("print_quality_tools_btn")

    def click_ok_btn(self):
        self.driver.wait_for_object("ok_btn")
        self.driver.click("ok_btn")

    def click_supply_status_error_message_btn(self):
        if self.driver.wait_for_object("supply_status_error_message", timeout=30, raise_e=False) == False:
            self.driver.swipe(direction="down")
        self.driver.wait_for_object("supply_status_error_message")
        logging.info("Clicking on supply status error message button")
        self.driver.click("supply_status_error_message")
        logging.info("Clicked on supply status error message button")

    def click_supply_status_warning_message_btn(self):
        if self.driver.wait_for_object("supply_status_warning_message", timeout=30, raise_e=False) == False:
            self.driver.swipe(direction="down")
        self.driver.wait_for_object("supply_status_warning_message")
        logging.info("Clicking on supply status warning message button")
        self.driver.click("supply_status_warning_message")
        logging.info("Clicked on supply status warning message button")

    def click_supply_status_information_message_btn(self):
        if self.driver.wait_for_object("supply_status_information_message", timeout=30, raise_e=False) == False:
            self.driver.swipe(direction="down")
        self.driver.wait_for_object("supply_status_information_message")
        logging.info("Clicking on supply status information message button")
        self.driver.click("supply_status_information_message")
        logging.info("Clicked on supply status information message button")

    def click_printer_card(self):
        self.capture_screenshot(page_name="printer_card")
        if self.driver.wait_for_object("printer_card", timeout=30, raise_e=False) == False:
            self.driver.swipe(direction="down")
        self.driver.wait_for_object("printer_card")
        logging.info("Clicking on printer card")
        self.driver.click("printer_card",change_check={"wait_obj": "pdp_back_btn"},retry=3)
        logging.info("Clicked on printer card")
        self.capture_screenshot(page_name="printer_details_page")

    def click_info_alert_in_pdp(self):
        self.driver.wait_for_object("info_alert_title_in_pdp")
        logging.info("Clicking on info alert title in PDP")
        self.driver.click("info_alert_title_in_pdp")
        logging.info("Clicked on info alert title in PDP")
        self.driver.wait_for_object("printer_status_btn", timeout=30)
        self.capture_screenshot(page_name="printer_status_screen")

    def click_error_alert_in_pdp(self):
        self.driver.wait_for_object("error_alert_title_in_pdp")
        logging.info("Clicking on error alert title in PDP")
        self.driver.click("error_alert_title_in_pdp")
        logging.info("Clicked on error alert title in PDP")
        self.driver.wait_for_object("printer_status_btn", timeout=30)
        self.capture_screenshot(page_name="printer_status_screen")

    def click_warning_alert_in_pdp(self):
        self.driver.wait_for_object("warning_alert_title_in_pdp")
        logging.info("Clicking on warning alert title in PDP")
        self.driver.click("warning_alert_title_in_pdp")
        logging.info("Clicked on warning alert title in PDP")
        self.driver.wait_for_object("printer_status_btn", timeout=30)
        self.capture_screenshot(page_name="printer_status_screen")
