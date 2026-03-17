# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on What type of printer are you trying to find screen.

@author: ten
@create_date: July 30, 2019
@update_date: Nov 30, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class WhatTypeOfPrinterAreYouTryingToFind(SmartScreens):
    folder_name = "oobe"
    flow_name = "what_type_of_printer_are_you_trying_to_find"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WhatTypeOfPrinterAreYouTryingToFind, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("what_type_of_printer_are_you_trying_to_find_screen_title", timeout=timeout, raise_e=raise_e)
 
    def wait_for_info_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Info dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[wait_for_info_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("info_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_setup_mode_printer_btn(self):
        '''
        This is a method to click Setup Mode Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_setup_mode_printer_btn]-Click Setup Mode Printer button... ")

        self.driver.click("setup_mode_printer_btn", is_native_event=True)

    def click_setup_mode_printer_info_btn(self):
        '''
        This is a method to click Info button under Setup Mode Printer section on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_setup_mode_printer_info_btn]-Click Info button... ")

        self.driver.click("setup_mode_printer_info_btn", is_native_event=True)

    def click_usb_printer_btn(self):
        '''
        This is a method to click USB Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_usb_printer_btn]-Click USB Printer button... ")

        self.driver.click("usb_printer_btn", is_native_event=True)

    def click_network_printer_btn(self):
        '''
        This is a method to click Network Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_network_printer_btn]-Click Network Printer button... ")

        self.driver.click("network_printer_btn", is_native_event=True)

    def click_network_printer_info_btn(self):
        '''
        This is a method to click Info button under Network Printer section on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_network_printer_info_btn]-Click Info button... ")

        self.driver.click("network_printer_info_btn", is_native_event=True)

    def click_what_type_of_printer_are_you_trying_to_find_screen_back_btn(self):
        '''
        This is a method to click Back button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_what_type_of_printer_are_you_trying_to_find_screen_back_btn]-Click Back button... ")

        self.driver.click("what_type_of_printer_are_you_trying_to_find_screen_back_btn", is_native_event=True)

    def click_info_dialog_ok_btn(self):
        '''
        This is a method to click OK button on Wi-Fi printer initial set up or Wi-Fi reset dialog/Check for network connection dialog after clicking info button on Network Printer section on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[click_info_dialog_ok_btn]-Click OK button... ")

        self.driver.click("info_dialog_ok_btn", is_native_event=True)

    def get_value_of_what_type_of_printer_are_you_trying_to_find_screen_title(self):
        '''
        This is a method to get value of What type of printer are you trying to find screen title.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_what_type_of_printer_are_you_trying_to_find_screen_title]-Get the contents of What type of printer are you trying to find screen title...")

        return self.driver.get_value("what_type_of_printer_are_you_trying_to_find_screen_title")

    def get_value_of_setup_mode_printer_title(self):
        '''
        This is a method to get value of Setup Mode Printer title on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_setup_mode_printer_title]-Get the contents of Setup Mode Printer title...")

        return self.driver.get_value("setup_mode_printer_title")

    def get_value_of_setup_mode_printer_content(self):
        '''
        This is a method to get value of Setup Mode Printer content on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_setup_mode_printer_content]-Get the contents of Setup Mode Printer content...")

        return self.driver.get_value("setup_mode_printer_content")

    def get_value_of_setup_mode_printer_btn(self):
        '''
        This is a method to get value of Setup Mode Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_setup_mode_printer_btn]-Get the contents of Setup Mode Printer button...")

        return self.driver.get_title("setup_mode_printer_btn")

    def get_value_of_usb_printer_title(self):
        '''
        This is a method to get value of USB Printer title on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_usb_printer_title]-Get the contents of USB Printer title...")

        return self.driver.get_value("usb_printer_title")

    def get_value_of_usb_printer_content(self):
        '''
        This is a method to get value of USB Printer content on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_usb_printer_content]-Get the contents of USB Printer content...")

        return self.driver.get_value("usb_printer_content")

    def get_value_of_usb_printer_btn(self):
        '''
        This is a method to get value of USB Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_usb_printer_btn]-Get the contents of USB Printer button...")

        return self.driver.get_title("usb_printer_btn")
    
    def get_value_of_network_printer_title(self):
        '''
        This is a method to get value of Network Printer title on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_network_printer_title]-Get the contents of Network Printer title...")

        return self.driver.get_value("network_printer_title")

    def get_value_of_network_printer_content(self):
        '''
        This is a method to get value of Network Printer content on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_usb_printer_content]-Get the contents of Network Printer content...")

        return self.driver.get_value("network_printer_content")

    def get_value_of_network_printer_btn(self):
        '''
        This is a method to get value of Network Printer button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_network_printer_btn]-Get the contents of Network Printer button...")

        return self.driver.get_title("network_printer_btn")

    def get_value_of_what_type_of_printer_are_you_trying_to_find_screen_back_btn(self):
        '''
        This is a method to get value of Back button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_what_type_of_printer_are_you_trying_to_find_screen_back_btn]-Get the contents of Back button...")

        return self.driver.get_title("what_type_of_printer_are_you_trying_to_find_screen_back_btn")
    
    def get_value_of_info_dialog_title(self):
        '''
        This is a method to get value of Info dialog title after clicking info button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_info_dialog_title]-Get the contents of Info dialog title...")

        return self.driver.get_value("info_dialog_title")

    def get_value_of_info_dialog_content(self):
        '''
        This is a method to get value of Info dialog content after clicking info button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_usb_printer_content]-Get the contents of Info dialog content...")

        return self.driver.get_value("info_dialog_content")

    def get_value_of_info_dialog_ok_btn(self):
        '''
        This is a method to get value of Info dialog OK button after clicking info button on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("[WhatTypeOfPrinterAreYouTryingToFind]:[get_value_of_info_dialog_ok_btn]-Get the contents of Info dialog OK button...")

        return self.driver.get_title("info_dialog_ok_btn")

# -------------------------------Verification Methods----------------------
    def verify_what_type_of_printer_are_you_trying_to_find_screen(self):
        '''
        This is a verification method to check UI strings of What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to verify UI string of What type of printer are you trying to find screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='what_type_of_printer_are_you_trying_to_find_screen')
        assert self.get_value_of_what_type_of_printer_are_you_trying_to_find_screen_title() == test_strings['what_type_of_printer_are_you_trying_to_find_screen_title']
        assert self.get_value_of_setup_mode_printer_title() == test_strings['setup_mode_printer_title']
        assert self.get_value_of_setup_mode_printer_content() == test_strings['setup_mode_printer_content']
        assert self.get_value_of_setup_mode_printer_btn() == test_strings['setup_mode_printer_btn']
        assert self.get_value_of_usb_printer_title() == test_strings['usb_printer_title']
        assert self.get_value_of_usb_printer_content() == test_strings['usb_printer_content']
        assert self.get_value_of_usb_printer_btn() == test_strings['usb_printer_btn']
        assert self.get_value_of_network_printer_title() == test_strings['network_printer_title']
        assert self.get_value_of_network_printer_content() == test_strings['network_printer_content']
        assert self.get_value_of_network_printer_btn() == test_strings['network_printer_btn']
        assert self.get_value_of_what_type_of_printer_are_you_trying_to_find_screen_back_btn() == test_strings['what_type_of_printer_are_you_trying_to_find_screen_back_btn']

    def verify_wifi_printer_initial_set_up_or_wifi_reset_dialog(self):
        '''
        This is a verification method to check UI strings of Wi-Fi printer initial set up or Wi-Fi reset dialog.
        :parameter:
        :return:
        '''
        self.wait_for_info_dialog_load()
        logging.debug("Start to verify UI string of Wi-Fi printer initial set up or Wi-Fi reset dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='wifi_printer_initial_set_up_or_wifi_reset_dialog')
        assert self.get_value_of_info_dialog_title() == test_strings['info_dialog_title']
        assert self.get_value_of_info_dialog_content() == test_strings['info_dialog_content']
        assert self.get_value_of_info_dialog_ok_btn() == test_strings['info_dialog_ok_btn']
       
    def verify_check_for_network_connection_dialog(self):
        '''
        This is a verification method to check UI strings of Check for network connection dialog.
        :parameter:
        :return:
        '''
        self.wait_for_info_dialog_load()
        logging.debug("Start to verify UI string of Check for network connection dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='check_for_network_connection_dialog')
        assert self.get_value_of_info_dialog_title() == test_strings['info_dialog_title']
        assert self.get_value_of_info_dialog_content() == test_strings['info_dialog_content']
        assert self.get_value_of_info_dialog_ok_btn() == test_strings['info_dialog_ok_btn']
         