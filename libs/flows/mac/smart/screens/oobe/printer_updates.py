# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on "Printer Updates" screen.

@author: Ivan
@create_date: Oct 08, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class PrinterUpdates(SmartScreens):

    folder_name = "oobe"
    flow_name = "printer_updates"

    def __init__(self, driver):
        super(PrinterUpdates, self).__init__(driver)

#  ----------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("apply_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of Printer Updates screen title.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_screen_title]-Get the value of Printer Updates screen title...  ")

        return self.driver.get_title("printer_updates_screen_title")

    def get_value_of_printer_updates_screen_content_1(self):
        '''
        This is a method to get the value of Printer update can improve text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_printer_updates_screen_content_1]-Get the value of content on Printer Updates screen...  ")

        return self.driver.get_value("printer_updates_screen_content_1")

    def get_value_of_printer_updates_screen_content_2(self):
        '''
        This is a method to get the value of Printer update can improve text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_printer_updates_screen_content_2]-Get the value of content on Printer Updates screen...  ")

        return self.driver.get_value("printer_updates_screen_content_2")

    def get_value_of_printer_updates_screen_content_3(self):
        '''
        This is a method to get the value of Printer update can improve text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_printer_updates_screen_content_3]-Get the value of content on Printer Updates screen...  ")

        return self.driver.get_title("printer_updates_screen_content_3")

    def get_value_of_auto_update_recommended_option(self):
        '''
        This is a method to get the value of Auto update recommended text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_auto_update_recommended_option]-Get the value of Auto update recommended text...  ")

        return self.driver.get_title("auto_update_recommended_option")

    def get_value_of_auto_update_recommended_option_content(self):
        '''
        This is a method to get the value of Automatically check for and install new updates text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_auto_update_recommended_option_content]-Get the value of Automatically check for and install new updates text...  ")

        return self.driver.get_value("auto_update_recommended_option_content")

    def get_value_of_notify_option(self):
        '''
        This is a method to get the value of Notify text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_notify_option]-Get the value of Notify text...  ")

        return self.driver.get_title("notify_option")

    def get_value_of_notify_option_content(self):
        '''
        This is a method to get the value of Automatically check for new updates and notify text on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_notify_option_content]-Get the value of Automatically check for new updates and notify text...  ")

        return self.driver.get_value("notify_option_content")

    def get_value_of_apply_btn(self):
        '''
        This is a method to get the value of Apply button on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[get_value_of_apply_btn]-Get the value of WIFI printer content - 2...  ")

        return self.driver.get_title("apply_btn")

    def click_auto_update_check_box(self):
        '''
        This is a method to click Auto Update check box on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[click_auto_update_check_box]-Click Auto Update check box... ")

        self.driver.click("auto_update_check_box", is_native_event=True)

    def click_notify_check_box(self):
        '''
        This is a method to click Notify check box on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[click_notify_check_box]-Click Notify check box... ")

        self.driver.click("notify_check_box", is_native_event=True)

    def click_apply_btn(self):
        '''
        This is a method to click Apply button on Printer Updates screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterUpdates]:[click_apply_btn]-Click Apply button... ")

        self.driver.click("apply_btn")

#   -----------------------------Verification Methods-----------------------------------------
    def verify_printer_updates_screen(self):
        '''
        This is a verification method to check UI strings of Printer Updates screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Printer Updates screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_updates_screen')
        assert self.get_value_of_screen_title() == test_strings['printer_updates_screen_title']
        assert self.get_value_of_printer_updates_screen_content_1() == test_strings['printer_updates_screen_content_1']
        assert self.get_value_of_printer_updates_screen_content_2() == test_strings['printer_updates_screen_content_2']
        assert self.get_value_of_printer_updates_screen_content_3() == test_strings['printer_updates_screen_content_3']
        assert self.get_value_of_auto_update_recommended_option() == test_strings['auto_update_recommended_option']
        assert self.get_value_of_auto_update_recommended_option_content() == test_strings['auto_update_recommended_option_content']
        assert self.get_value_of_notify_option() == test_strings['notify_option']
        assert self.get_value_of_notify_option_content() == test_strings['notify_option_content']
        assert self.get_value_of_apply_btn() == test_strings['apply_btn']
