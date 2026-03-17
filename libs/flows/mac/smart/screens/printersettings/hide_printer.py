# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the forget this printer screen.

@author: ten
@create_date: Nov 20, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class HidePrinter(PrinterSettingScroll, SmartScreens):
    folder_name = "printersettings"
    flow_name = "hide_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(HidePrinter, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print from other devices screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("hide_printer_btn", timeout=timeout, raise_e=raise_e)

    def click_hide_printer_btn(self):
        '''
        This is a method to click HidePrinter button on Forget this printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[click_hide_printer_btn]-Click hide_printer button... ")

        self.driver.click("hide_printer_btn", is_native_event=True)

    def get_value_of_hide_printer_title(self):
        '''
        This is a method to get value of HidePrinter screen title.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[get_value_of_hide_printer_title]-Get value of HidePrinter screen title...  ")

        return self.driver.get_value("hide_printer_title")

    def get_value_of_hide_printer_content_1(self):
        '''
        This is a method to get value of HidePrinterscreen content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[get_value_of_hide_printer_content_1]-Get value of HidePrinter screen content - 1...  ")

        return self.driver.get_value("hide_printer_content_1")

    def get_value_of_hide_printer_content_2(self):
        '''
        This is a method to get value of HidePrinter screen content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[get_value_of_hide_printer_content_2]-Get value of HidePrinter screen content - 2...  ")

        return self.driver.get_value("hide_printer_content_2")

    def get_value_of_hide_printer_content_3(self):
        '''
        This is a method to get value of HidePrinter screen content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[get_value_of_hide_printer_content_3]-Get value of HidePrinter screen content - 3...  ")

        return self.driver.get_value("hide_printer_content_3")

    def get_value_of_hide_printer_btn(self):
        '''
        This is a method to get value of hide_printer button on Forget this printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinter]:[get_value_of_hide_printer_btn]-Get value of HidePrinter button...  ")

        return self.driver.get_title("hide_printer_btn")

# -------------------------------Verification Methods--------------------------
    def verify_ui_string(self):
        '''
        This is a method to check UI strings of hide_printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()

        logging.debug("Start to check UI strings of hide_printer screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hide_printer_screen')
        assert self.get_value_of_hide_printer_title() == test_strings['hide_printer_title']
        assert self.get_value_of_hide_printer_content_1() + self.get_value_of_hide_printer_content_2() + self.get_value_of_hide_printer_content_3() == test_strings['hide_printer_body']
        assert self.get_value_of_hide_printer_btn() == test_strings['hide_printer_btn']
