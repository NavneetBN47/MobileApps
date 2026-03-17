# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the choose a printer sheet.

@author: Sophia
@create_date: May 21, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ChooseAPrinterSheet(SmartScreens):
    folder_name = "common"
    flow_name = "choose_a_printer_sheet"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ChooseAPrinterSheet, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait choose a printer sheet shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("choose_a_printer_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_choose_a_printer_title(self):
        '''
        This is a method to get value of Choose a Printer sheet title.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[get_value_of_choose_a_printer_title]-Get the contents of Choose a Printer sheet title...  ")

        return self.driver.get_value("choose_a_printer_title")

    def get_value_of_the_following_printers_text(self):
        '''
        This is a method to get value of The Following printers text on Choose a Printer sheet.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[get_value_of_the_following_printers_text]-Get the contents of The Following printers text...  ")

        return self.driver.get_value("the_following_printers_text")

    def get_value_of_select_the_printer_text(self):
        '''
        This is a method to get value of Select the printer text on Choose a Printer sheet.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[get_value_of_select_the_printer_text]-Get the contents of Select the printer text...  ")

        return self.driver.get_value("select_the_printer_text")

    def get_value_of_tip_to_add_text(self):
        '''
        This is a method to get value of Tip To Add text on Choose a Printer sheet.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[get_value_of_tip_to_add_text]-Get the contents of Tip To Add text...  ")

        return self.driver.get_value("tip_to_add_text")

    def get_value_of_skip_btn(self):
        '''
        This is a method to get value of Skip button on Choose a Printer sheet.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[get_value_of_skip_btn]-Get the contents of Skip button...  ")

        return self.driver.get_title("skip_btn")

    def select_printer(self, printer_name):
        '''
        This is a method to click the printer name.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[click_beaconing_printer_chose]-click to select printer... ")

        self.driver.click("list_printer_name", format_specifier=[printer_name], is_native_event=True)

    def click_skip_btn(self):
        '''
        This is a method to click skip button.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[click_skip_btn]-Click 'Skip' button... ")

        self.driver.click("skip_btn")

# -------------------------------Verification Methods--------------------------
    def verify_choose_a_printer_sheet(self):
        '''
        This is a verification method to check UI strings of Choose A Printer sheet.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(600)
        logging.debug("Start to verify UI string of Choose A Printer sheet")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='choose_a_print_sheet')
        assert self.get_value_of_choose_a_printer_title() == test_strings['choose_a_printer_title']
        assert self.get_value_of_the_following_printers_text() == test_strings['the_following_printers_text']
        assert self.get_value_of_select_the_printer_text() == test_strings['select_the_printer_text']
        assert self.get_value_of_tip_to_add_text() == test_strings['tip_to_add_text']
        assert self.get_value_of_skip_btn() == test_strings['skip_btn']
