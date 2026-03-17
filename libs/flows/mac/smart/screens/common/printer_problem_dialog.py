# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for the printer problem dialog.

@author: Ivan
@create_date: Nov 19, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class PrinterProblemDialog(SmartScreens):
    folder_name = "common"
    flow_name = "printer_problem_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterProblemDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Printer Problem dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_problem_dialog_content", timeout=timeout, raise_e=raise_e)

    def get_value_of_printer_problem_dialog_title(self):
        '''
        This is a method to get value of Printer Problem dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[get_value_of_printer_problem_dialog_title]-Get value of Printer Problem dialog title...  ")

        return self.driver.get_value("printer_problem_dialog_title")

    def get_value_of_printer_problem_dialog_content(self):
        '''
        This is a method to get value of Printer Problem dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[get_value_of_printer_problem_dialog_content]-Get value of Printer Problem dialog content...  ")

        return self.driver.get_value("printer_problem_dialog_content")

    def get_value_of_printer_problem_dialog_return_to_home_btn(self):
        '''
        This is a method to get value of Return to home button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[get_value_of_printer_problem_dialog_return_to_home_btn]-Get value of Return to home button...  ")

        return self.driver.get_title("printer_problem_dialog_return_to_home_btn")

    def get_value_of_printer_problem_dialog_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[get_value_of_printer_problem_dialog_cancel_btn]-Get value of Cancel button...  ")

        return self.driver.get_title("printer_problem_dialog_cancel_btn")

    def get_value_of_printer_problem_dialog_skip_printing_btn(self):
        '''
        This is a method to get value of Skip printing button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[get_value_of_printer_problem_dialog_skip_printing_btn]-Get value of Skip printing button...  ")

        return self.driver.get_title("printer_problem_dialog_skip_printing_btn")

    def click_printer_problem_dialog_return_to_home_btn(self):
        '''
        This is a method to click Return to home button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[click_printer_problem_dialog_return_to_home_btn]-Click Return to home button... ")

        self.driver.click("printer_problem_dialog_return_to_home_btn", is_native_event=True)

    def click_printer_problem_dialog_cancel_btn(self):
        '''
        This is a method to click Cancel button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[click_printer_problem_dialog_cancel_btn]-Click Cancel button... ")

        self.driver.click("printer_problem_dialog_cancel_btn", is_native_event=True)

    def click_printer_problem_dialog_skip_printing_btn(self):
        '''
        This is a method to click Skip Printing button on Printer Problem dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterProblemDialog]:[click_printer_problem_dialog_skip_printing_btn]-Click Skip Printing button... ")

        self.driver.click("printer_problem_dialog_skip_printing_btn", is_native_event=True)


# -------------------------------Verification Methods--------------------------
    def verify_printer_problem_dialog_with_cancel_button(self):
        '''
        This is a verification method to check UI strings of Printer Problem dialog with one button(Cancel)
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Printer Problem dialog with two buttons")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_problem_dialog')
        assert self.get_value_of_printer_problem_dialog_title() == test_strings['printer_problem_dialog_title']
        assert self.get_value_of_printer_problem_dialog_content() == test_strings['dialog_content_cancel']
        assert self.get_value_of_printer_problem_dialog_cancel_btn() == test_strings['printer_problem_dialog_cancel_btn']

    def verify_printer_problem_dialog_with_cancel_and_return_to_home_button(self):
        '''
        This is a verification method to check UI strings of Printer Problem dialog with two buttons(Return to Home, Cancel)
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Printer Problem dialog with two buttons")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_problem_dialog')
        assert self.get_value_of_printer_problem_dialog_title() == test_strings['printer_problem_dialog_title']
        assert self.get_value_of_printer_problem_dialog_content() == test_strings['dialog_content_cancel_and_return_to_home']
        assert self.get_value_of_printer_problem_dialog_return_to_home_btn() == test_strings['printer_problem_dialog_return_to_home_btn']
        assert self.get_value_of_printer_problem_dialog_cancel_btn() == test_strings['printer_problem_dialog_cancel_btn']

    def verify_printer_problem_dialog_with_cancel_and_skip_printing_button(self):
        '''
        This is a verification method to check UI strings of Printer Problem dialog with two buttons(Cancel, Skip Printing)
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Printer Problem dialog with two buttons")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_problem_dialog')
        assert self.get_value_of_printer_problem_dialog_title() == test_strings['printer_problem_dialog_title']
        assert self.get_value_of_printer_problem_dialog_content() == test_strings['dialog_content_cancel_and_skip_printing']
        assert self.get_value_of_printer_problem_dialog_cancel_btn() == test_strings['printer_problem_dialog_cancel_btn']
        assert self.get_value_of_printer_problem_dialog_skip_printing_btn() == test_strings['printer_problem_dialog_skip_printing_btn']

    def verify_printer_problem_dialog_with_cancel_and_return_to_home_and_skip_printing_button(self):
        '''
        This is a verification method to check UI strings of Printer Problem dialog with three buttons(Return to Home, Cancel, Skip Printing)
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Printer Problem dialog with three buttons")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_problem_dialog')
        assert self.get_value_of_printer_problem_dialog_title() == test_strings['printer_problem_dialog_title']
        assert self.get_value_of_printer_problem_dialog_content() == test_strings['dialog_content_cancel_and_return_to_home_and_skip_printing']
        assert self.get_value_of_printer_problem_dialog_return_to_home_btn() == test_strings['printer_problem_dialog_return_to_home_btn']
        assert self.get_value_of_printer_problem_dialog_cancel_btn() == test_strings['printer_problem_dialog_cancel_btn']
        assert self.get_value_of_printer_problem_dialog_skip_printing_btn() == test_strings['printer_problem_dialog_skip_printing_btn']
