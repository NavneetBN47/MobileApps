# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on "USB detected. Connect printer to Internet for more features" screen.

@author: Ivan
@create_date: Jul 12, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class USBDetected(SmartScreens):

    folder_name = "oobe"
    flow_name = "usb_detected"

    def __init__(self, driver):
        super(USBDetected, self).__init__(driver)

#  ----------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("recommened_text", timeout=timeout, raise_e=raise_e)

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of USB Detected screen title.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_screen_title]-Get the value of USB Detected screen title...  ")

        return self.driver.get_value("screen_title")

    def get_value_of_usb_printer_content_1(self):
        '''
        This is a method to get the value of USB printer content - 1 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_usb_printer_content_1]-Get the value of USB printer content - 1...  ")

        return self.driver.get_value("usb_printer_content_1")

    def get_value_of_usb_printer_content_2(self):
        '''
        This is a method to get the value of USB printer content - 2 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_usb_printer_content_2]-Get the value of USB printer content - 2...  ")

        return self.driver.get_value("usb_printer_content_2")

    def get_value_of_continue_with_usb_btn(self):
        '''
        This is a method to get the value of Continue with USB button on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_continue_with_usb_btn]-Get the value of Continue with USB button...  ")

        return self.driver.get_title("continue_with_usb_btn")

    def get_value_of_recommened_text(self):
        '''
        This is a method to get the value of Recommended text on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_recommened_text]-Get the value of Recommended text...  ")

        return self.driver.get_value("recommened_text")

    def get_value_of_wifi_printer_content_1(self):
        '''
        This is a method to get the value of WIFI printer content - 1 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_wifi_printer_content_1]-Get the value of WIFI printer content - 1...  ")

        return self.driver.get_value("wifi_printer_content_1")

    def get_value_of_wifi_printer_content_2(self):
        '''
        This is a method to get the value of WIFI printer content - 2 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_wifi_printer_content_2]-Get the value of WIFI printer content - 2...  ")

        return self.driver.get_value("wifi_printer_content_2")

    def get_value_of_wifi_printer_content_3(self):
        '''
        This is a method to get the value of WIFI printer content - 3 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_wifi_printer_content_3]-Get the value of WIFI printer content - 3...  ")

        return self.driver.get_value("wifi_printer_content_3")

    def get_value_of_wifi_printer_content_4(self):
        '''
        This is a method to get the value of WIFI printer content - 4 on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_wifi_printer_content_4]-Get the value of WIFI printer content - 4...  ")

        return self.driver.get_value("wifi_printer_content_4")

    def get_value_of_connect_to_wifi_btn(self):
        '''
        This is a method to get the value of Connect to WiFi button on USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[get_value_of_connect_to_wifi_btn]-Get the value of Connect to WiFi button...  ")

        return self.driver.get_title("connect_to_wifi_btn")

    def click_continue_with_usb_btn(self):
        '''
        This is a method to click Continue with USB button on USB Detected screen.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[click_continue_with_usb_btn]-Click Continue with USB button... ")

        self.driver.click("continue_with_usb_btn")

    def click_connect_to_wifi_btn(self):
        '''
        This is a method to click Connect to WiFi button on USB Detected screen.
        :parameter:
        :return:
        '''
        logging.debug("[USBDetected]:[click_connect_to_wifi_btn]-Click Connect to WiFi button... ")

        self.driver.click("connect_to_wifi_btn")

#   -----------------------------Verification Methods-----------------------------------------
    def verify_usb_detected_screen(self):
        '''
        This is a verification method to check UI strings of USB Detected screen for Yeti Flex with Offer printer.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of USB Detected screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='usb_detected_screen')
        assert self.get_value_of_screen_title() == test_strings['screen_title']
        assert self.get_value_of_usb_printer_content_1() == test_strings['usb_printer_content_1']
        assert self.get_value_of_usb_printer_content_2() == test_strings['usb_printer_content_2']
        assert self.get_value_of_continue_with_usb_btn() == test_strings['continue_with_usb_btn']
        assert self.get_value_of_recommened_text() == test_strings['recommened_text']
        assert self.get_value_of_wifi_printer_content_1() == test_strings['wifi_printer_content_1']
        assert self.get_value_of_wifi_printer_content_2() == test_strings['wifi_printer_content_2']
        assert self.get_value_of_wifi_printer_content_3() == test_strings['wifi_printer_content_3']
        assert self.get_value_of_wifi_printer_content_4() == test_strings['wifi_printer_content_4']
        assert self.get_value_of_connect_to_wifi_btn() == test_strings['connect_to_wifi_btn']
