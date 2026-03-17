# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect Using USB screen.

@author: ten
@create_date: Aug 14, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectUsingUSB(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_using_usb"

    def __init__(self, driver):
        super(ConnectUsingUSB, self).__init__(driver)

# -------------------------------Operate Elements------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_using_usb_image", timeout=timeout, raise_e=raise_e)

    def wait_for_usb_not_connected_to_printer_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait USB not connected to printer dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[wait_for_usb_not_connected_to_printer_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("usb_not_connected_to_printer_show_me_how_btn", timeout=timeout, raise_e=raise_e)

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_back_btn]-Click Back button.. ")

        self.driver.click("back_btn", is_native_event=True)

    def click_connect_printer_btn(self):
        '''
        This is a method to click Connect Printer button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_connect_printer_btn]-Click Connect printer button.. ")

        self.driver.click("connect_using_usb_connect_printer_btn", is_native_event=True)

    def click_show_me_how_btn(self):
        '''
        This is a method to click Show me how button on USB not connected to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_show_me_how_btn]-Click Show me how button.. ")

        self.driver.click("usb_not_connected_to_printer_show_me_how_btn", is_native_event=True)

    def click_retry_btn(self):
        '''
        This is a method to click Retry button on USB not connected to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_show_me_how_btn]-Click Retry button.. ")

        self.driver.click("usb_not_connected_to_printer_retry_btn", is_native_event=True)

    def get_value_of_connect_using_usb_title(self):
        '''
        This is a method to get the value of Connect Using USB screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_using_usb_title]-Get the contents of Connect Using USB screen title...  ")

        return self.driver.get_value("connect_using_usb_title")

    def get_value_of_connect_using_usb_contents(self):
        '''
        This is a method to get the value of Connect Using USB screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_using_usb_contents]-Get the contents of Connect Using USB screen contents...  ")

        return self.driver.get_value("connect_using_usb_contents")

    def get_value_of_back_btn(self):
        '''
        This is a method to get the value of Back button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_back_btn]-Get the contents of Back button..  ")

        return self.driver.get_title("back_btn")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get the value of Connect Printer button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_printer_btn]-Get the contents of Connect Printer button..  ")

        return self.driver.get_title("connect_using_usb_connect_printer_btn")

    def get_value_of_usb_not_connected_to_printer_title(self):
        '''
        This is a method to get the value of USB not connected to printer dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_usb_not_connected_to_printer_title]-Get the contents of USB not connected to printer dialog title...  ")

        return self.driver.get_value("usb_not_connected_to_printer_title")

    def get_value_of_usb_not_connected_to_printer_contents(self):
        '''
        This is a method to get the value of USB not connected to printer dialog contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_usb_not_connected_to_printer_contents]-Get the contents of USB not connected to printer dialog contents...  ")

        return self.driver.get_value("usb_not_connected_to_printer_contents")

    def get_value_of_usb_not_connected_to_printer_show_me_how_btn(self):
        '''
        This is a method to get the value of Show me how button on USB not connected to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_usb_not_connected_to_printer_show_me_how_btn]-Get the contents of Show me how button..  ")

        return self.driver.get_title("usb_not_connected_to_printer_show_me_how_btn")

    def get_value_of_usb_not_connected_to_printer_retry_btn(self):
        '''
        This is a method to get the value of Retry button on USB not connected to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_usb_not_connected_to_printer_retry_btn]-Get the contents of Retry button..  ")

        return self.driver.get_title("usb_not_connected_to_printer_retry_btn")

# -------------------------------Verification Methods---------------
    def verify_connect_using_usb_screen(self):
        '''
        This is a verification method to check UI strings of Connect Using USB screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect Using USB screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_using_usb_screen')
        assert self.get_value_of_connect_using_usb_title() == test_strings['connect_using_usb_title']
        assert test_strings['connect_using_usb_contents_1'] and test_strings['connect_using_usb_contents_2'] in self.get_value_of_connect_using_usb_contents()
        assert self.get_value_of_back_btn() == test_strings['back_btn']
        assert self.get_value_of_connect_printer_btn() == test_strings['connect_using_usb_connect_printer_btn']

    def verify_usb_not_connected_to_printer_dialog(self):
        '''
        This is a verification method to check UI strings of USB not connected to printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_usb_not_connected_to_printer_dialog_load(600)
        logging.debug("Start to check UI strings of USB not connected to printer dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='usb_not_connected_to_printer_dialog')
        assert self.get_value_of_usb_not_connected_to_printer_title() == test_strings['usb_not_connected_to_printer_title']
        assert self.get_value_of_usb_not_connected_to_printer_contents() == test_strings['usb_not_connected_to_printer_contents']
        assert self.get_value_of_usb_not_connected_to_printer_show_me_how_btn() == test_strings['usb_not_connected_to_printer_show_me_how_btn']
        assert self.get_value_of_usb_not_connected_to_printer_retry_btn() == test_strings['usb_not_connected_to_printer_retry_btn']