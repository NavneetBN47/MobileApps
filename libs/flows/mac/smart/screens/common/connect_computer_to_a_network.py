# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on connect computer to a network.

@author: ten
@create_date: Nov 23, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectComputerToANetwork(SmartScreens):

    folder_name = "common"
    flow_name = "connect_computer_to_a_network"

    def __init__(self, driver):
        super(ConnectComputerToANetwork, self).__init__(driver)

#    ---------------------------Operate Elements---------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ConnectComputerToANetwork]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("open_network_btn", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click continue button on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork:[click_continue_btn]-Click continue button... ")

        self.driver.click("continue_btn_enabled", is_native_event=True)

    def click_open_network_btn(self):
        '''
        This is a method to click Open network button on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork:[click_open_network_btn]-Click Open network button... ")

        self.driver.click("open_network_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_this_computer_is_not_currently_text(self):
        '''
        This is a method to get value of This computer is not currently text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_this_computer_is_not_currently_text]-Get value of This computer is not currently text...  ")

        return self.driver.get_value("this_computer_is_not_currently_text")

    def get_value_of_to_change_your_wifi_network_text(self):
        '''
        This is a method to get value of To change your wifi network text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_to_change_your_wifi_network_text]-Get value of To change your wifi network text...  ")

        return self.driver.get_value("to_change_your_wifi_network_text")

    def get_value_of_open_network_btn(self):
        '''
        This is a method to get value of Open network button on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_open_network_btn]-Get value of Open network button...  ")

        return self.driver.get_title("open_network_btn")

    def get_value_of_select_wifi_from_the_connection_list_text(self):
        '''
        This is a method to get value of Select wifi from the connection list text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_select_wifi_from_the_connection_list_text]-Get value of Select wifi from the connection list text...  ")

        return self.driver.get_value("select_wifi_from_the_connection_list_text")

    def get_value_of_choose_your_wifi_network_text(self):
        '''
        This is a method to get value of Choose your wifi network text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_choose_your_wifi_network_text]-Get value of Choose your wifi network text...  ")

        return self.driver.get_value("choose_your_wifi_network_text")

    def get_value_of_after_connecting_to_wifi_text(self):
        '''
        This is a method to get value of After connecting to wifi text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_after_connecting_to_wifi_text]-Get value of After connecting to wifi text...  ")

        return self.driver.get_value("after_connecting_to_wifi_text")

    def get_value_of_note_if_you_cant_connect_text(self):
        '''
        This is a method to get value of Note if you can't connect text on Connect computer to a network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_note_if_you_cant_connect_text]-Get value of Note if you can't connect text...  ")

        return self.driver.get_value("note_if_you_cant_connect_text")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of continue_btn
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToANetwork]:[get_value_of_continue_btn]-Get continue_btn...  ")

        return self.driver.get_title("continue_btn_disabled")

# -------------------------------Verification Methods---------------------------------------
    def verify_connect_computer_to_a_network_screen(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.wait_for_screen_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_computer_to_a_network')
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
        assert self.get_value_of_this_computer_is_not_currently_text() == test_strings['this_computer_is_not_currently_text']
        assert self.get_value_of_to_change_your_wifi_network_text() == test_strings['to_change_your_wifi_network_text']
        assert self.get_value_of_open_network_btn() == test_strings['open_network_btn']
        assert self.get_value_of_select_wifi_from_the_connection_list_text() == test_strings['select_wifi_from_the_connection_list_text']
        assert self.get_value_of_choose_your_wifi_network_text() == test_strings['choose_your_wifi_network_text']
        assert self.get_value_of_after_connecting_to_wifi_text() == test_strings['after_connecting_to_wifi_text']
        assert self.get_value_of_note_if_you_cant_connect_text() == test_strings['note_if_you_cant_connect_text']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']
