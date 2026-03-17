# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for We could't connect to your printer dialog.

@author: Ivan
@create_date: Feb 05, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class WeCouldNotConnectToYourPrinter(SmartScreens):

    folder_name = "oobe"
    flow_name = "we_could_not_connect_to_your_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WeCouldNotConnectToYourPrinter, self).__init__(driver)

# -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("we_could_not_connect_to_your_printer_image", timeout=timeout, raise_e=raise_e)

    def click_retry_btn(self):
        '''
        This is a method to Click Retry button on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[click_retry_btn]-Click Retry button.. ")

        self.driver.click("retry_btn", is_native_event=True)

    def click_try_wifi_btn(self):
        '''
        This is a method to Click Try Wi-Fi button on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[click_try_wifi_btn]-Click Try Wi-Fi button.. ")

        self.driver.click("try_wifi_btn", is_native_event=True)

    def get_value_of_we_could_not_connect_to_your_printer_title(self):
        '''
        This is a method to get the value of title on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[get_value_of_we_could_not_connect_to_your_printer_title]-Get the contents of title...  ")

        return self.driver.get_value("we_could_not_connect_to_your_printer_title")

    def get_value_of_we_could_not_connect_to_your_printer_content(self):
        '''
        This is a method to get the value of Content on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[get_value_of_we_could_not_connect_to_your_printer_content]-Get the contents of Content...  ")

        return self.driver.get_value("we_could_not_connect_to_your_printer_content")

    def get_value_of_try_wifi_btn(self):
        '''
        This is a method to get the value of Try Wi-Fi button on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[get_value_of_try_wifi_btn]-Get the contents of Try Wi-Fi button...  ")

        return self.driver.get_title("try_wifi_btn")

    def get_value_of_retry_btn(self):
        '''
        This is a method to get the value of Retry button on We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotConnectToYourPrinter]:[get_value_of_retry_btn]-Get the contents of Retry button...  ")

        return self.driver.get_title("retry_btn")

# -------------------------------Verification Methods-----------------------------
    def verify_we_could_not_connect_to_your_printer_dialog(self):
        '''
        This is a verification method to check UI strings of We could't connect to your printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of We could't connect to your printer dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='we_could_not_connect_to_your_printer')
        assert self.get_value_of_we_could_not_connect_to_your_printer_title() == test_strings['we_could_not_connect_to_your_printer_title']
        assert self.get_value_of_we_could_not_connect_to_your_printer_content() == test_strings['we_could_not_connect_to_your_printer_content']
        assert self.get_value_of_try_wifi_btn() == test_strings['try_wifi_btn']
        assert self.get_value_of_retry_btn() == test_strings['retry_btn']
