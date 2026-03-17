# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Remove USB Cable screen.

@author: ten
@create_date: Oct 16, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class RemoveUSBCable(SmartScreens):

    folder_name = "oobe"
    flow_name = "remove_usb_cable"

    def __init__(self, driver):
        super(RemoveUSBCable, self).__init__(driver)

    #  -----------------------------Operate Elements------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("remove_usb_cable_screen_image", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Remove USB Cable screen.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("remove_usb_cable_screen_continue_btn")

    def get_value_of_remove_usb_cable_screen_title(self):
        '''
        This is a method to get the value of Remove USB Cable screen title.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[get_value_of_remove_usb_cable_screen_title]-Get the contents of Remove USB Cable screen title...  ")

        return self.driver.get_value("remove_usb_cable_screen_title")

    def get_value_of_remove_usb_cable_screen_contents_1(self):
        '''
        This is a method to get the value of Remove USB Cable screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[get_value_of_remove_usb_cable_screen_contents_1]-Get the contents of Remove USB Cable screen contents..  ")

        return self.driver.get_value("remove_usb_cable_screen_contents_1")

    def get_value_of_remove_usb_cable_screen_contents_2(self):
        '''
        This is a method to get the value of Remove USB Cable screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[get_value_of_remove_usb_cable_screen_contents_2]-Get the contents of Remove USB Cable screen contents..  ")

        return self.driver.get_value("remove_usb_cable_screen_contents_2")

    def get_value_of_remove_usb_cable_screen_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Remove USB Cable screen.
        :parameter:
        :return:
        '''
        logging.debug("[RemoveUSBCable]:[get_value_of_remove_usb_cable_screen_continue_btn]-Get the contents of Continue button..  ")

        return self.driver.get_title("remove_usb_cable_screen_continue_btn")

    # --------------------Verification Methods------------------------------------------
    def verify_remove_usb_cable_screen(self):
        '''
        This is a verification method to check UI strings of Remove USB Cable screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of Remove USB Cable screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='remove_usb_cable')
        assert self.get_value_of_remove_usb_cable_screen_title() == test_strings['remove_usb_cable_screen_title']
        assert self.get_value_of_remove_usb_cable_screen_contents_1() == test_strings['remove_usb_cable_screen_contents_1']
        assert self.get_value_of_remove_usb_cable_screen_contents_2() == test_strings['remove_usb_cable_screen_contents_2']
        assert self.get_value_of_remove_usb_cable_screen_continue_btn() == test_strings['remove_usb_cable_screen_continue_btn']
