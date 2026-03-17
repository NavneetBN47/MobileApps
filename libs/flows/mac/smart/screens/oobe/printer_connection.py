# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Printer Connection screen

@author: Ivan
@create_date: Oct 24, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class PrinterConnection(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_connection"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterConnection, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("not_now_btn", timeout=timeout, raise_e=raise_e)

    def click_not_now_btn(self):
        '''
        This is a method to click not now button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[click_not_now_btn]-Click Not Now button... ")

        self.driver.click("not_now_btn")

    def click_connect_to_wifi_network_btn(self):
        '''
        This is a method to click connect to wifi network button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[click_connect_to_wifi_network_btn]-Click Connect to Wifi network button... ")

        self.driver.click("connect_to_wifi_network_btn")

    def get_value_of_printer_connection_title(self):
        '''
        This is a method to get the value of printer_connection_title.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_printer_connection_title]-Get the value of printer_connection_title...  ")

        return self.driver.get_value("printer_connection_title")

    def get_value_of_printer_connection_content_1(self):
        '''
        This is a method to get the value of printer_connection_content_1
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_printer_connection_content_1]-Get the value of printer_connection_content_1...  ")

        return self.driver.get_value("printer_connection_content_1")

    def get_value_of_printer_connection_content_2(self):
        '''
        This is a method to get the value of printer_connection_content_2.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_printer_connection_content_2]-Get the value of printer_connection_content_2...  ")

        return self.driver.get_value("printer_connection_content_2")

    def get_value_of_printer_connection_content_3(self):
        '''
        This is a method to get the value of printer_connection_content_3.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_printer_connection_content_3]-Get the value of printer_connection_content_3...  ")

        return self.driver.get_value("printer_connection_content_3")

    def get_value_of_not_now_btn(self):
        '''
        This is a method to get the value of not_now button.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_not_now_btn]-Get the value of not_now_btn...  ")

        return self.driver.get_title("not_now_btn")

    def get_value_of_connect_to_wifi_network_btn(self):
        '''
        This is a method to get the value of connect_to_wifi_network_button.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[get_value_of_connect_to_wifi_network_btn]-Get the value of connect_to_wifi_network_btn...  ")

        return self.driver.get_title("connect_to_wifi_network_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_printer_connection_screen(self):
        '''
        This is a verification method to check UI strings of Printer connection screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to verify UI string of Printer connection screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_connection')
        assert self.get_value_of_printer_connection_title() == test_strings['connection_title']
        assert test_strings['content_1_1'] and test_strings['content_1_2'] and test_strings['content_1_3'] in self.get_value_of_printer_connection_content_1()
        assert self.get_value_of_printer_connection_content_2() == test_strings['content_2']
        assert self.get_value_of_printer_connection_content_3() == test_strings['content_3']
        assert self.get_value_of_not_now_btn() == test_strings['not_now_btn']
        assert self.get_value_of_connect_to_wifi_network_btn() == test_strings['connect_to_wifi_network_btn']
