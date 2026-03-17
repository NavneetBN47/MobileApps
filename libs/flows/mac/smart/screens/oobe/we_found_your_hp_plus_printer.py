# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for We found your HP+ printer screen.

@author: Ivan
@create_date: Feb 05, 2021
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class WeFoundYourHPPlusPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "we_found_your_hp_plus_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WeFoundYourHPPlusPrinter, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("we_found_your_hp_plus_printer_image", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        Click continue button
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[click_continue_btn]-Click continue button... ")

        self.driver.click("continue_btn", is_native_event=True)
#         if self.wait_for_screen_load(raise_e=False):
#             self.driver.click("continue_btn", is_native_event=True)

    def get_value_of_we_found_your_hp_plus_printer_title(self):
        '''
        This is a method to get value of We found your HP+ printer screen title.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[get_value_of_we_found_your_hp_plus_printer_title]-Get the contents of We found your HP+ printer screen title...  ")

        return self.driver.get_value("we_found_your_hp_plus_printer_title")

    def get_value_of_hp_plus_printers_require_text(self):
        '''
        This is a method to get value of HP+ Printer require text on We found your HP+ printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[get_value_of_hp_plus_printers_require_text]-Get the contents of HP+ Printer require text ...  ")

        return self.driver.get_value("hp_plus_printers_require_text")

    def get_value_of_keep_the_usb_cord_text(self):
        '''
        This is a method to get value of Keep the USB cord text on We found your HP+ printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[get_value_of_keep_the_usb_cord_text]-Get the contents of Keep the USB cord text...  ")

        return self.driver.get_value("keep_the_usb_cord_text")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on We found your HP+ printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourHPPlusPrinter]:[get_value_of_continue_btn]-Get the contents of Continue button ...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_we_found_your_hp_plus_printer_screen(self):
        '''
        This is a verification method to check UI strings of We found your HP+ printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to verify UI string of We found your HP+ printer screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='we_found_your_hp_plus_printer_screen')
        assert self.get_value_of_we_found_your_hp_plus_printer_title() == test_strings['we_found_your_hp_plus_printer_title']
        assert self.get_value_of_hp_plus_printers_require_text() == test_strings['hp_plus_printers_require_text']
        assert self.get_value_of_keep_the_usb_cord_text() == test_strings['keep_the_usb_cord_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']
