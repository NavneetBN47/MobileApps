# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect printer using Wi-Fi or Ethernet screen.

@author: ten
@create_date: Nov 3, 2020

@update_author: Ivan
@update_date: Feb 04, 2021
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class ConnectPrinterUsingWifiOrEthernet(SmartScreens):

    folder_name = "oobe"
    flow_name = "connect_printer_using_wifi_or_ethernet"

    def __init__(self, driver):
        super(ConnectPrinterUsingWifiOrEthernet, self).__init__(driver)

#  ----------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("wifi_radio_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of Connect Printer Using WiFi Or Ethernet screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_screen_title]-Get the value of contents...  ")

        return self.driver.get_value("screen_title")

    def get_value_of_to_use_all_features_text(self):
        '''
        This is a method to get the value of To Use all features text on Connect Printer Using WiFi Or Ethernet screen for Yeti Flex printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_to_use_all_features_text]-Get the value of To Use all features text...  ")

        return self.driver.get_value("to_use_all_features_text")

    def get_value_of_how_do_you_want_text(self):
        '''
        This is a method to get the value of How do you want text on Connect Printer Using WiFi Or Ethernet screen for Yeti Flex printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_how_do_you_want_text]-Get the value of How do you want text...  ")

        return self.driver.get_value("how_do_you_want_text")

    def get_value_of_to_set_up_text(self):
        '''
        This is a method to get the value of To set up text on Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_to_set_up_text]-Get the value of To set up text...  ")

        return self.driver.get_value("to_set_up_text")

    def get_value_of_must_text(self):
        '''
        This is a method to get the value of Must text on Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_must_text]-Get the value of Must text...  ")

        return self.driver.get_value("must_text")

    def get_value_of_connect_it_to_the_internet_text(self):
        '''
        This is a method to get the value of Connect it to the internet text on Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_connect_it_to_the_internet_text]-Get the value of Connect it to the internet text...  ")

        return self.driver.get_value("connect_it_to_the_internet_text")

    def get_value_of_select_a_connection_text(self):
        '''
        This is a method to get the value of Select a connection text on Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_select_a_connection_text]-Get the value of Select a connection text...  ")

        return self.driver.get_value("select_a_connection_text")

    def get_value_of_wifi_radio_btn(self):
        '''
        This is a method to get the value of Wi-Fi radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_wifi_radio_btn]-Get the value of Wi-Fi radio button...  ")

        return self.driver.get_title("wifi_radio_btn")

    def get_value_of_wifi_opt_content(self):
        '''
        This is a method to get the value of Wi-Fi opt content after select Wi-Fi opt on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_wifi_opt_content]-Get the value of Wi-Fi opt content after select Wi-Fi opt...  ")

        return self.driver.get_value("wifi_opt_content")

    def get_value_of_ethernet_cable_radio_btn(self):
        '''
        This is a method to get the value of Ethernet Cable radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_ethernet_cable_radio_btn]-Get the value of Ethernet Cable radio button...  ")

        return self.driver.get_title("ethernet_cable_radio_btn")

    def get_value_of_usb_only_radio_btn(self):
        '''
        This is a method to get the value of USB Only radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_usb_only_radio_btn]-Get the value of USB Only radio button...  ")

        return self.driver.get_title("usb_only_radio_btn")

    def get_value_of_usb_only_opt_content(self):
        '''
        This is a method to get the value of USB Only opt content after select USB Only opt on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_usb_only_opt_content]-Get the value of USB Only opt content after select USB Only opt...  ")

        return self.driver.get_value("usb_only_opt_content")

    def get_value_of_note_after_connecting_if_desired_text(self):
        '''
        This is a method to get the value of Note After connecting if desired text on Connect Printer Using WiFi Or Ethernet screen for Yeti Flex printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_note_after_connecting_if_desired_text]-Get the value of Note After connecting if desired text...  ")

        return self.driver.get_value("note_after_connecting_if_desired_text")

    def get_value_of_note_after_connecting_if_needed_text(self):
        '''
        This is a method to get the value of Note After connecting if needed text on Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_note_after_connecting_if_needed_text]-Get the value of Note After connecting if needed text...  ")

        return self.driver.get_value("note_after_connecting_if_needed_text")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[get_value_of_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("continue_btn")

    def click_wifi_radio_btn(self):
        '''
        This is a method to click Wi-Fi radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[click_wifi_radio_btn]-Click Wi-Fi radio button... ")

        self.driver.click("wifi_radio_btn")

    def click_ethernet_cable_radio_btn(self):
        '''
        This is a method to click Ethernet Cable radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[click_ethernet_cable_radio_btn]-Click Ethernet Cable radio button... ")

        self.driver.click("ethernet_cable_radio_btn")

    def click_usb_only_radio_btn(self):
        '''
        This is a method to click USB Only radio button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[click_usb_only_radio_btn]-Click USB Only radio button... ")

        self.driver.click("usb_only_radio_btn")

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Connect Printer Using WiFi Or Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterUsingWifiOrEthernet]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn", is_native_event=True)

#   -----------------------------Verification Methods-----------------------------------------
    def verify_connect_printer_using_wifi_or_ethernet_screen_yeti_flex(self):
        '''
        This is a verification method to check UI strings of Connect Printer Using WiFi Or Ethernet screen for Yeti Flex printer.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.verify_continue_btn_is_disabled()
        logging.debug("Start to verify UI string of Connect Printer Using WiFi Or Ethernet screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_using_wifi_or_ethernet')
        assert self.get_value_of_screen_title() == test_strings['connect_printer_using_wifi_or_ethernet_title']
        assert self.get_value_of_to_use_all_features_text() == test_strings['to_use_all_features_text']
        assert self.get_value_of_how_do_you_want_text() == test_strings['how_do_you_want_text']
        assert self.get_value_of_wifi_radio_btn() == test_strings['wifi_radio_btn']
        assert self.get_value_of_ethernet_cable_radio_btn() == test_strings['ethernet_cable_radio_btn']
        assert self.get_value_of_usb_only_radio_btn() == test_strings['usb_only_radio_btn']
        assert self.get_value_of_note_after_connecting_if_desired_text() == test_strings['note_after_connecting_if_desired_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_using_wifi_or_ethernet_screen_yeti_flex_after_select_wifi_opt(self):
        '''
        This is a verification method to check UI strings of Connect Printer Using WiFi Or Ethernet screen After select Wi-Fi opt.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.verify_continue_btn_is_enabled()
        logging.debug("Start to verify UI string of Connect Printer Using WiFi Or Ethernet screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_using_wifi_or_ethernet')
        assert self.get_value_of_screen_title() == test_strings['connect_printer_using_wifi_or_ethernet_title']
        assert self.get_value_of_to_use_all_features_text() == test_strings['to_use_all_features_text']
        assert self.get_value_of_how_do_you_want_text() == test_strings['how_do_you_want_text']
        assert self.get_value_of_wifi_radio_btn() == test_strings['wifi_radio_btn']
        assert self.get_value_of_wifi_opt_content() == test_strings['wifi_opt_content']
        assert self.get_value_of_ethernet_cable_radio_btn() == test_strings['ethernet_cable_radio_btn']
        assert self.get_value_of_usb_only_radio_btn() == test_strings['usb_only_radio_btn']
        assert self.get_value_of_note_after_connecting_if_desired_text() == test_strings['note_after_connecting_if_desired_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_using_wifi_or_ethernet_screen_yeti_flex_after_select_usb_only_opt(self):
        '''
        This is a verification method to check UI strings of Connect Printer Using WiFi Or Ethernet screen After select USB Only opt.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.verify_continue_btn_is_enabled()
        logging.debug("Start to verify UI string of Connect Printer Using WiFi Or Ethernet screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_using_wifi_or_ethernet')
        assert self.get_value_of_screen_title() == test_strings['connect_printer_using_wifi_or_ethernet_title']
        assert self.get_value_of_to_use_all_features_text() == test_strings['to_use_all_features_text']
        assert self.get_value_of_how_do_you_want_text() == test_strings['how_do_you_want_text']
        assert self.get_value_of_wifi_radio_btn() == test_strings['wifi_radio_btn']
        assert self.get_value_of_ethernet_cable_radio_btn() == test_strings['ethernet_cable_radio_btn']
        assert self.get_value_of_usb_only_radio_btn() == test_strings['usb_only_radio_btn']
        assert self.get_value_of_usb_only_opt_content() == test_strings['usb_only_opt_content']
        assert self.get_value_of_note_after_connecting_if_desired_text() == test_strings['note_after_connecting_if_desired_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_using_wifi_or_ethernet_screen_yeti_e2e(self, ethernet_supported=False):
        '''
        This is a verification method to check UI strings of Connect Printer Using WiFi Or Ethernet screen for Yeti E2E printer.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        sleep(5)
        self.verify_continue_btn_is_enabled()
        logging.debug("Start to verify UI string of Connect Printer Using WiFi Or Ethernet screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_using_wifi_or_ethernet')
        if ethernet_supported is True:
            assert self.get_value_of_screen_title() == test_strings['connect_printer_using_wifi_or_ethernet_title']
        else:
            assert self.get_value_of_screen_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_to_set_up_text() == test_strings['to_set_up_text']
        assert self.get_value_of_must_text() == test_strings['must_text']
        assert self.get_value_of_connect_it_to_the_internet_text() == test_strings['connect_it_to_the_internet_text']
        assert self.get_value_of_select_a_connection_text() == test_strings['select_a_connection_text']
        assert self.get_value_of_wifi_radio_btn() == test_strings['wifi_radio_btn']
        assert self.get_value_of_ethernet_cable_radio_btn() == test_strings['ethernet_cable_radio_btn']
        assert self.get_value_of_note_after_connecting_if_needed_text() == test_strings['note_after_connecting_if_needed_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_continue_btn_is_disabled(self):
        '''
        This is a method to verify continue button is disabled on the screen before select opt.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is disabled on the screen before select opt")

        if self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is enabled")
        return True

    def verify_continue_btn_is_enabled(self):
        '''
        This is a method to verify continue button is enabled on the screen after select opt.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is enabled on the screen after select opt")

        if not self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is disabled")
        return True
