# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the printer settings scroll area.

@author: Sophia
@create_date: Sep 18, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException

class PrinterSettingScroll(SmartScreens):
    folder_name = "printersettings"
    flow_name = "printer_setting_scroll"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterSettingScroll, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
#     def wait_for_screen_load(self, timeout=30, raise_e=True):
#         '''
#         This is a method to wait for screen shows correctly.
#         :parameter:
#         :return:
#         '''
#         pass

    def wait_for_privacy_preferences_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Privacy Preferences"], timeout=timeout, raise_e=raise_e)

    def wait_for_printer_status_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Printer Status"], timeout=timeout, raise_e=raise_e)

    def wait_for_supply_status_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Supply Status"], timeout=timeout, raise_e=raise_e)

    def wait_for_advanced_setting_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Advanced Settings"], timeout=timeout, raise_e=raise_e)

    def wait_for_printer_anywhere_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Print Anywhere "], timeout=timeout, raise_e=raise_e)

    def wait_for_printer_reports_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Printer Reports"], timeout=timeout, raise_e=raise_e)

    def wait_for_see_what_printing_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["See What`s printing"], timeout=timeout, raise_e=raise_e)

    def wait_for_print_quality_tools_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Print Quality Tools"], timeout=timeout, raise_e=raise_e)

    def wait_for_print_from_other_devices_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Print From Other Devices"], timeout=timeout, raise_e=raise_e)

    def wait_for_network_information_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Network Information"], timeout=timeout, raise_e=raise_e)

    def wait_for_hide_printer_option_load(self, timeout=5, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object("printer_settings_tab_items", format_specifier=["Hide Printer"], timeout=timeout, raise_e=raise_e)

    def click_printer_status_tab(self):
        '''
        This is a method to click print from other devices.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_printer_status_tab]-Click printer_status_tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Printer Status"], is_native_event=True)

    def click_print_anywhere_tab(self):
        '''
        This is a method to click print anywhere tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_anywhere_tab]-Click print anywhere... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Print Anywhere"], is_native_event=True)

    def click_print_anywhere_tab_hp_plus(self):
        '''
        This is a method to click print anywhere tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_anywhere_tab]-Click print anywhere... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Print Anywhere "], is_native_event=True)

    def click_network_information_tab(self):
        '''
        This is a method to click network_information_tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_network_information_tab]-Click network_information_tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Network Information"], is_native_event=True)

    def click_advanced_settings_tab(self):
        '''
        This is a method to click Advanced Settings tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_advanced_settings_tab]-Click Advanced Settings tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Advanced Settings"], is_native_event=True)

    def click_printer_reports_tab(self):
        '''
        This is a method to click Printer Reports tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_printer_reports_tab]-Click Printer Reports tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Printer Reports"], is_native_event=True)

    def click_print_quality_tools_tab(self):
        '''
        This is a method to click Print Quality Tools tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_quality_tools_tab]-Click Print Quality Tools tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Print Quality Tools"], is_native_event=True)

    def click_print_from_other_devices_tab(self):
        '''
        This is a method to click Print From Other Devices tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_forget_this_printer_tab]-Click Print From Other Devices tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Print From Other Devices"], is_native_event=True)

    def click_hide_printer_tab(self):
        '''
        This is a method to click Hide Printer tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_forget_this_printer_tab]-Click Hide Printer tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Hide Printer"], is_native_event=True)

    def click_privacy_preferences_tab(self):
        '''
        This is a method to click Hide Printer tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_Privacy Preferences_tab]-Click Privacy Preferences tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Privacy Preferences"], is_native_event=True)

    def click_supply_status_tab(self):
        '''
        This is a method to click supply status.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_supply_status_tab]-Click supply_status_tab... ")

        self.driver.click("printer_settings_tab_items", format_specifier=["Supply Status"], is_native_event=True)

    def get_value_of_status_text(self):
        '''
        get_value_of_status_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_status_text-Get the contents of status_text ...  ")

        return self.driver.get_value("status_text")

    def get_value_of_printer_status_tab(self):
        '''
        get_value_of_printer_status_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_status_tab-Get the contents of printer_status_tab ...  ")

        return self.driver.get_value("printer_status_tab")

    def get_value_of_supply_status_tab(self):
        '''
        get_value_of_supply_status_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_supply_status_tab-Get the contents of supply_status_tab...  ")

        return self.driver.get_value("supply_status_tab")

    def get_value_of_information_text(self):
        '''
        get_value_of_information_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_information_text-Get the contents of information_text...  ")

        return self.driver.get_value("information_text")

    def get_value_of_printer_information_tab(self):
        '''
        get_value_of_printer_information_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_information_tabGet the contents ofprinter_information_tab ...  ")

        return self.driver.get_value("printer_information_tab")

    def get_value_of_network_information_tab(self):
        '''
        get_value_of_network_information_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_network_information_tab-Get the contents of network_information_tab ...  ")

        return self.driver.get_value("network_information_tab")

    def get_value_of_settings_text(self):
        '''
        get_value_of_settings_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_settings_text-Get the contents of settings_text ...  ")

        return self.driver.get_value("settings_text")

    def get_value_of_printer_anywhere_tab(self):
        '''
        get_value_of_printer_anywhere_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_anywhere_tab-Get the contents of printer_anywhere_tab ...  ")

        return self.driver.get_value("printer_anywhere_tab")

    def get_value_of_advanced_settings_tab(self):
        '''
        get_value_of_advanced_settings_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_advanced_settings_tab-Get the contents of advanced_settings_tab ...  ")

        return self.driver.get_value("advanced_settings_tab")

    def get_value_of_tools_text(self):
        '''
        get_value_of_tools_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_tools_text_tab-Get the contents of tools_text...  ")

        return self.driver.get_value("tools_text")

    def get_value_of_printer_reports_tab(self):
        '''
        get_value_of_printer_reports_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_reports_tab-Get the contents of printer_reports_tab ...  ")

        return self.driver.get_value("printer_reports_tab")

    def get_value_of_print_quality_tools_tab(self):
        '''
        get_value_of_print_quality_tools_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_print_quality_tools_tab-Get the contents of print_quality_tools_tab ...  ")

        return self.driver.get_value("print_quality_tools_tab")

    def get_value_of_manage_text(self):
        '''
        get_value_of_manage_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_manage_text-Get the contents of manage_text...  ")

        return self.driver.get_value("manage_text")

    def get_value_of_print_from_other_devices_tab(self):
        '''
        get_value_of_print_from_other_devices_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_print_from_other_devices_tab-Get the contents of print_from_other_devices_tab...  ")

        return self.driver.get_value("print_from_other_devices_tab")

    def get_value_of_forget_this_printer_tab(self):
        '''
        get_value_of_forget_this_printer_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_forget_this_printer_tab-Get the contents of forget_this_printer_tab...  ")

        return self.driver.get_value("forget_this_printer_tab")

# -------------------------------Verification Methods--------------------------
    def verify_options_state_local_printer(self):
        '''
        verify options state local printer
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.verify_printer_status_tab_is_enabled()
        self.verify_supply_status_tab_is_enabled()
        self.verify_network_information_tab_is_enabled()
        self.verify_advanced_setting_tab_is_enabled()
        self.verify_printer_anywhere_tab_is_hidden()
        self.verify_printer_reports_tab_is_enabled()
        self.verify_print_quality_tools_tab_is_enabled()
        self.verify_print_from_other_devices_tab_is_enabled()
        self.verify_hide_printer_tab_is_enabled()

    def verify_options_state_local_printer_for_offline_printer(self):
        '''
        verify options state local printer offline printer
        :parameter:
        :return:
        '''
        logging.debug("verify_options_state_remote_printer for offline printer")
        self.verify_printer_status_tab_is_enabled()
        self.verify_supply_status_tab_is_enabled()
        self.verify_print_from_other_devices_tab_is_enabled()
        self.verify_hide_printer_tab_is_enabled()

    def verify_options_state_remote_printer(self):
        '''
        verify_options_state_remote_printer
        :parameter:
        :return:
        '''
        logging.debug("verify_options_state_remote_printer")
        self.verify_printer_status_tab_is_hidden()
        self.verify_supply_status_tab_is_enabled()
        self.verify_advanced_setting_tab_is_hidden()
        self.verify_printer_anywhere_tab_is_enabled()
        self.verify_network_information_tab_is_hidden()
        self.verify_printer_reports_tab_is_hidden()
        self.verify_see_what_printing_tab_is_hidden()
        self.verify_print_quality_tools_tab_is_hidden()
        self.verify_print_from_other_devices_tab_is_enabled()
        self.verify_hide_printer_tab_is_enabled()

    def verify_options_state_remote_printer_for_offline_printer(self):
        '''
        verify_options_state_remote_printer offline printer
        :parameter:
        :return:
        '''
        logging.debug("verify_options_state_remote_printer for offline printer")
        self.verify_printer_status_tab_is_hidden()
        self.verify_advanced_setting_tab_is_hidden()
        self.verify_printer_reports_tab_is_hidden()
        self.verify_network_information_tab_is_hidden()
        self.verify_see_what_printing_tab_is_hidden()
        self.verify_print_quality_tools_tab_is_hidden()
        self.verify_print_from_other_devices_tab_is_enabled()
        self.verify_hide_printer_tab_is_enabled()

    def verify_no_print_anywhere_tab(self):
        '''
        This is a verification method to check Print Anywhere tab is not display for Gen1 printer or USB connected printer.
        :parameter:
        :return:
        '''
        assert self.get_value_of_printer_anywhere_tab() != "Print Anywhere"

    def verify_privacy_preferences_option_is_not_available(self):
        '''
        This is a verification method to check privacy preferences option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_privacy_preferences_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_privacy_preferences_option_is_available(self):
        '''
        This is a verification method to check privacy preferences option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_privacy_preferences_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_printer_status_tab_is_hidden(self):
        '''
        This is a verification method to check printer status  option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_printer_status_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_printer_status_tab_is_enabled(self):
        '''
        This is a verification method to check printer status option is not available
        :parameter:
        :return:
        '''
        if not self.wait_for_printer_status_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_supply_status_tab_is_enabled(self):
        '''
        This is a verification method to check supply_status option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_supply_status_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_advanced_setting_tab_is_hidden(self):
        '''
        This is a verification method to check advanced setting option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_advanced_setting_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_advanced_setting_tab_is_enabled(self):
        '''
        This is a verification method to check advanced setting option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_advanced_setting_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_printer_anywhere_tab_is_enabled(self):
        '''
        This is a verification method to check printer anywhere option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_printer_anywhere_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_printer_anywhere_tab_is_hidden(self):
        '''
        This is a verification method to check printer anywhere option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_printer_anywhere_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_printer_reports_tab_is_hidden(self):
        '''
        This is a verification method to check printer reports option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_printer_reports_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_printer_reports_tab_is_enabled(self):
        '''
        This is a verification method to check printer reports option is not available
        :parameter:
        :return:
        '''
        if not self.wait_for_printer_reports_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_see_what_printing_tab_is_hidden(self):
        '''
        This is a verification method to check see what printing option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_see_what_printing_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_see_what_printing_tab_is_enabled(self):
        '''
        This is a verification method to check see what printing option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_see_what_printing_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_print_quality_tools_tab_is_hidden(self):
        '''
        This is a verification method to check print quality tools option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_print_quality_tools_option_load():
            raise UnexpectedItemPresentException("the option is available")

    def verify_print_quality_tools_tab_is_enabled(self):
        '''
        This is a verification method to check print quality tools option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_print_quality_tools_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_print_from_other_devices_tab_is_enabled(self):
        '''
        This is a verification method to check print from other devices option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_print_from_other_devices_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_hide_printer_tab_is_enabled(self):
        '''
        This is a verification method to check hide_printer option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_hide_printer_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_network_information_tab_is_enabled(self):
        '''
        This is a verification method to check network information option is available
        :parameter:
        :return:
        '''
        if not self.wait_for_network_information_option_load():
            raise UnexpectedItemPresentException("the option is not available")

    def verify_network_information_tab_is_hidden(self):
        '''
        This is a verification method to check network information option is not available
        :parameter:
        :return:
        '''
        if self.wait_for_network_information_option_load():
            raise UnexpectedItemPresentException("the option is available")