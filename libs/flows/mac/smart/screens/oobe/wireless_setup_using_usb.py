# encoding: utf-8
'''
check wireless setup using usb screen

@author: ten
@create_date: Aug 22, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class WirelessSetupUsingUSB(SmartScreens):

    folder_name = "oobe"
    flow_name = "wireless_setup_using_usb"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WirelessSetupUsingUSB, self).__init__(driver)

# -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_image", timeout=timeout, raise_e=raise_e)

    def click_info_btn(self):
        '''
        This is a method to Click info button on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_info_btn]-click_info_btn.. ")

        self.driver.click("info_btn")

    def click_back_btn(self):
        '''
        This is a method to Click back button on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_back_btn]-Click back_btn.. ")

        self.driver.click("back_btn")

    def click_connect_printer_btn(self):
        '''
        This is a method to Click continue button on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("connect_printer_btn")

    def get_value_of_wireless_setup_using_usb_title(self):
        '''
        This is a method to get the value of title on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_wireless_setup_using_usb_title]-Get the contents of wireless_setup_using_usb_title...  ")

        return self.driver.get_value("wireless_setup_using_usb_title")

    def get_value_of_temporarily_connect_this_device_content(self):
        '''
        This is a method to get the value of Temporarily Connect this device content on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_temporarily_connect_this_device_content]-Get the contents of Temporarily Connect this device content...  ")

        return self.driver.get_value("temporarily_connect_this_device_content")

    def get_value_of_connect_the_square_content(self):
        '''
        This is a method to get the value of Connect the Square content on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_connect_the_square_content]-Get the contents of Connect the Square content...  ")

        return self.driver.get_value("connect_the_square_content")

    def get_value_of_back_btn(self):
        '''
        This is a method to get the value of Back button on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_back_btn]-Get the contents of Back button...  ")

        return self.driver.get_title("back_btn")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get the value of Connect Printer button on Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_connect_printer_btn]-Get the contents of Connect Printer button..  ")

        return self.driver.get_title("connect_printer_btn")

# -------------------------------Verification Methods-----------------------------
    def verify_wireless_setup_using_usb_screen(self):
        '''
        This is a verification method to check UI strings of Wireless Setup Using USB screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Wireless Setup Using USB screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='wireless_setup_using_usb')
        assert self.get_value_of_wireless_setup_using_usb_title() == test_strings['wireless_setup_using_usb_title']
        assert self.get_value_of_temporarily_connect_this_device_content() == test_strings['contents_1']
        assert test_strings['contents_2_1'] and test_strings['contents_2_2'] in self.get_value_of_connect_the_square_content()
        assert self.get_value_of_back_btn() == test_strings['back_btn']
        assert self.get_value_of_connect_printer_btn() == test_strings['connect_printer_btn']
