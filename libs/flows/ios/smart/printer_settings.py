import logging
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class PrinterSettings(SmartFlow):
    flow_name = "printer_settings"

    # Printer Settings screen
    DYNAMIC_OPTION_TEXT = "_shared_dynamic_text"
    DYNAMIC_OPTION_BUTTON = "_shared_dynamic_button"
    PS_BACK_BUTTON = "_shared_back_arrow_btn"
    PS_SCREEN_TITLE = "printer_settings_screen_title"
    PS_STATUS_TITLE = "printer_status_title"
    PS_STATUS_READY = "printer_status_ready"
    PS_PRINT_ANYWHERE = "print_anywhere"
    PS_REMOTE_PRINTING = "remote_printing"
    PS_PRINT_FROM_OTHER_DEVICES = "print_from_other_devices"
    PS_SELECT_A_DIFFERENT_PRINTER = "select_a_different_printer"
    PS_SUPPORTED_SUPPLIES = "supported_supplies"
    PS_RENAME_MY_PRINTER = "rename_my_printer"
    PS_TRAY_AND_PAPER = "tray_and_paper"
    PS_QUIET_MODE = "quiet_mode"
    PS_PRINTER_REPORTS = "printer_reports"
    PS_PRINT_QUALITY_TOOLS = "print_quality_tools"
    PS_ALIGNMENT_MAINTENANCE = "alignment_maintenance"
    PS_PRINTER_INFORMATION = "printer_information"
    PS_NETWORK_INFORMATION = "network_information"
    PS_ADVANCED_SETTINGS = "advanced_settings"
    PS_SHORTCUTS = "shortcuts"  # Only appears for specific printers like Novelli
    PS_FORGET_THIS_PRINTER = "forget_this_printer"
    SAVE_BUTTON = "_shared_save_btn"
    RENAME_PRINTER_NAME_TEXT_FIELD = "rename_printer_text_field"
    RENAME_PRINTER_CHARACTERS_TEXT = "characters_left_text"
    RENAME_PRINTER_NOTE = "renaming_printer_note"
    SEND_LINK_BUTTON = "send_link_button"
    ON_RADIO_BUTTON = "on_radio_btn"
    OFF_RADIO_BUTTON = "off_radio_btn"
    PRINT_BUTTON = "print_btn"
    PQ_TOOLS_ALIGN_BUTTON = "align_btn"
    PQ_TOOLS_CLEAN_BUTTON = "clean_btn"
    PQ_TOOLS_CLEAN_PRINTHEAD = ["clean_printhead"]
    PQ_TOOLS_ALIGN_PRINTER = ["align_printer"]
    NETWORK_INFO_DIRECT_CONNECTION_NAME = "direct_connection_name"
    NETWORK_INFO_BONJOUR_NAME = "bonjour_name"
    WIFI_DIRECT_FIND_PRINTER_PIN = "find_printer_txt"

    REPORT_NETWORK_CONFIG = "network_configuration"
    REPORT_PRINT_QUALITY = "print_quality_report"
    REPORT_WIRELESS_TEST = "wireless_test_report"
    REPORT_WEB_ACCESS = "web_access_report"
    REPORT_PRINTER_STATUS = "printer_status_report"

    PS_RENAME_PRINTER_UI_ELEMENTS = [
        PS_BACK_BUTTON,
        SAVE_BUTTON,
        RENAME_PRINTER_NAME_TEXT_FIELD,
        RENAME_PRINTER_CHARACTERS_TEXT,
        RENAME_PRINTER_NOTE
    ]

    PS_SCREEN_OPTIONS = [
        PS_BACK_BUTTON,
        PS_STATUS_TITLE,
        PS_STATUS_READY,
        PS_PRINT_FROM_OTHER_DEVICES,
        PS_SELECT_A_DIFFERENT_PRINTER,
        PS_SUPPORTED_SUPPLIES,
        PS_RENAME_MY_PRINTER,
        PS_PRINT_ANYWHERE,
        PS_REMOTE_PRINTING,
        PS_TRAY_AND_PAPER,
        PS_QUIET_MODE,
        PS_PRINTER_REPORTS,
        PS_PRINT_QUALITY_TOOLS,
        PS_PRINTER_INFORMATION,
        PS_NETWORK_INFORMATION,
        PS_ADVANCED_SETTINGS,
        PS_FORGET_THIS_PRINTER
    ]

    TRAY_AND_PAPER_UI_ELEMENTS = [PS_BACK_BUTTON, "tray", "status", "paper_size", "paper_type",
                                  "_shared_cancel", "apply_btn", "advanced_btn"]
    QUITE_MODE_UI_ELEMENTS = [PS_BACK_BUTTON, "apply_btn", "_shared_cancel", "on_radio_btn", "off_radio_btn"]
     # all the printer states
    PRINTER_STATES = ["ready", "out of paper", "jam in printer", "the tray is open", "error on the printer",
                      "cartridge low", "cartridges missing", "in power save", "shutting down",
                      "single cartridge mode", "see printer front panel", "tray empty or open"]
    # available printer languages in the environment
    PRINTER_LANGUAGES = ["English", "Português", "Norsk", "Dansk", "Nederlands", "Deutsch", "Español", "Français"]

    def verify_printer_settings_screen(self, raise_e=False):
        return self.driver.wait_for_object("printer_settings_screen_title", raise_e=raise_e)

    def verify_printer_status(self, status):
        return self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=[status],
                                           raise_e=False) is not False

    def verify_ui_elements(self, ui_elements, button_label=None):
        for element in ui_elements:
            try:
                option_displayed = self.driver.wait_for_object(element)
            except (TimeoutException, NoSuchElementException):
                option_displayed = self.driver.scroll(element, raise_e=False) is not False
            if not option_displayed:
                logging.error(element + " - not displayed/not applicable")
            else:
                if button_label is not None:
                    c = self.driver.find_object(self.DYNAMIC_OPTION_BUTTON,
                                                format_specifier=[self.get_text_from_str_id(element)])
                    if str(c.get_attribute("label")) == str(self.get_text_from_str_id(button_label)) and \
                            str(c.get_attribute("enabled")).lower() == "true":
                        logging.info(c.get_attribute("name") + " - " + button_label + " button enabled")
                    else:
                        logging.error(c.get_attribute("name") + " - " + button_label + " button enabled")

    def verify_printer_status_screen(self, status):
        """
        :param status: Expected Printer Status
        :return:
        """
        if not self.verify_printer_status(status):
            raise Exception("Printer Status is not " + status)
        else:
            self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=[status]).click()
            sleep(2)
            ui_elements = ["printer_status_title", "printer_status_ready_text", self.PS_BACK_BUTTON]
            self.verify_printer_status(status)
            self.verify_ui_elements(ui_elements)

    def go_to_print_from_other_devices_screen(self):
        self.driver.scroll(self.PS_PRINT_FROM_OTHER_DEVICES, direction="up").click()
        sleep(2)

    def verify_print_from_other_device_screen_ui_elements(self):
        print_from_other_device_screen_ui_elements = ["print_from_other_devices_screen_title",
                                                      "123_hp_com_link", "send_link_btn"]
        self.verify_ui_elements(print_from_other_device_screen_ui_elements)

    def go_to_123_hp_com_page_and_navigate_back(self):
        self.driver.wait_for_object("123_hp_com_link").click()
        sleep(2)
        # Verify Print from other devices link opened
        self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=['Complete setup using HP Smart'])
        self.driver.wait_for_object("_shared_close").click()
        sleep(2)
        self.driver.wait_for_object("print_from_other_devices_screen_title")

    def ps_select_send_link(self, raise_e=True):
        return self.driver.click("send_link_btn", raise_e=raise_e)

    def verify_link_sent_screen_ui_elements(self):
        self.driver.wait_for_object("link_sent")
        self.driver.wait_for_object("send_another_link_btn")

    def select_select_a_different_printer(self):
        self.driver.wait_for_object(self.PS_SELECT_A_DIFFERENT_PRINTER).click()

    def verify_rename_printer_screen(self):
        return self.driver.wait_for_object(self.RENAME_PRINTER_NAME_TEXT_FIELD, timeout=20, raise_e=False) is not False

    def edit_printer_name_and_save(self, name):
        self.driver.click(self.RENAME_PRINTER_NAME_TEXT_FIELD)
        self.driver.clear_text(self.RENAME_PRINTER_NAME_TEXT_FIELD)
        self.driver.send_keys(self.RENAME_PRINTER_NAME_TEXT_FIELD, name)
        self.driver.wait_for_object(self.SAVE_BUTTON).click()
        sleep(2)

    def get_radio_button_value(self, radio_button):
        result = self.driver.get_attribute(radio_button, "value")
        return int(result) if result.isnumeric() else result

    def find_ui_element_exists(self, element):
        return self.driver.scroll(element, raise_e=False) is not False

    def select_ui_option(self, ui_option, verify_nav=True):
        try:
            self.driver.wait_for_object(ui_option, timeout=15)
        except (TimeoutException, NoSuchElementException):
            self.driver.scroll(ui_option, timeout=10)
        self.driver.click(ui_option)
        if not verify_nav:
            return True
        sleep(5)
        if ui_option == self.NETWORK_INFO_DIRECT_CONNECTION_NAME:
            self.driver.wait_for_object("_shared_dynamic_navigation_bar_wifi_direct")
        else:
            self.driver.wait_for_object("_shared_dynamic_navigation_bar",format_specifier=[self.get_text_from_str_id(ui_option)])
        return True

    def select_ok_btn(self, raise_e=False):
        self.driver.click("ok_btn", raise_e=raise_e, timeout=5)

    def get_ethernet_status(self):
        if self.driver.scroll("ethernet_info_title", raise_e=False) is not False:
            return str(self.driver.get_attribute("ethernet_status_cell", attribute="label", raise_e=False)).lower()
        else:
            return False

    def verify_title_and_get_value(self, element_title):
        element = self.driver.scroll("network_info", format_specifier=[element_title], raise_e=False)
        if element is not False:
            return str(element.get_attribute("label"))
        else:
            return element

    def verify_ui_option_displayed(self, ui_option, invisible=False):
        return self.driver.wait_for_object(ui_option, raise_e=False, invisible=invisible) is not False

    def go_to_wi_fi_direct(self):
        self.driver.scroll("wi_fi_direct_txt").click()
        self.driver.wait_for_object("wi_fi_direct_title", timeout=20)

    def select_clean_btn(self):
        """
        Click on Clean button on Print Quality Tools screen
        """
        self.driver.click("clean_btn")

    def select_printer_reports_report_btn(self, report_name):
        """
        Click on one of 5 types of report button
        :param report_name: class constant variable:
                        REPORT_PRINTER_STATUS
                        REPORT_DEMO_PAGE
                        REPORT_NETWORK_CONFIG
                        REPORT_PRINT_QUALITY
                        REPORT_WIRELESS_TEST
                        REPORT_ACCESS_REPORT
        """
        self.driver.click("report_print_btn", format_specifier=[self.driver.return_str_id_value(report_name)])

    def verify_printer_report_by_name(self, report_name, invisible=False, raise_e=True):
        """
        Verify each report on Printer Reports screen is visiable or invisible
        :param report_name:
           REPORT_PRINTER_STATUS
           REPORT_DEMO_PAGE
           REPORT_NETWORK_CONFIG
           REPORT_PRINT_QUALITY
           REPORT_WIRELESS_TEST
           REPORT_ACCESS_REPORT
        :param invisible: True or False
        :param raise_e:
        """
        return self.driver.wait_for_object("info_cell_title", timeout=15, format_specifier=[self.driver.return_str_id_value(report_name)], invisible=invisible, raise_e=raise_e)

    def verify_printer_status_popup(self, raise_e=True, timeout=10):
        """
        Verify Printer Status popup after clicking on Print button
        """
        return self.driver.wait_for_object("printer_status_title", raise_e=raise_e, timeout=timeout)

    def verify_clean_printhead_popup(self):
        """
        Verify Clean Printhead popup after clicking on Clean button
        """
        self.driver.wait_for_object("cleaning_printhead_popup")

    def verify_processing_popup(self):
        """
        Verify Processing popup after clicking on Supported supplies
        """
        self.driver.wait_for_object("processing_popup")

    def verify_clean_printhead(self, invisible=False, raise_e=True):
        """
        Verify Clean Printhead on Printer Quality Tools screen is visiable or invisible
        """
        return self.driver.wait_for_object("cleaning_printhead_item", invisible=invisible, raise_e=raise_e)
    
    def select_and_submit_pin_code(self, pin_code):
        """
        Select pin textbox and submit pid when required.
        Args:
            pin_code (str): Pin code to be used
        """
        self.driver.send_keys("find_printer_txt", pin_code)
        self.driver.click("submit_pin_code")
    
    def verify_support_supplies_screen_or_ink_trial_btn(self, raise_e=False):
        """
        Verify Supported Supplies screen or Instant Ink Trial button
        """
        return self.driver.wait_for_object("supported_supplies_screen_title", raise_e=raise_e) or self.driver.wait_for_object("try_instant_ink_btn", raise_e=raise_e)

    def verify_network_info_page(self):
        """
        Verify the network information page is present
        """
        self.driver.wait_for_object("network_information")

    def verify_printer_info_page(self):
        """
        Verify the printer information page is present
        """
        self.driver.wait_for_object("printer_information")
