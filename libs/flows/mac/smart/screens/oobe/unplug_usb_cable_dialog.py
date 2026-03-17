# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Unplug USB Cable dialog.

@author: ten
@create_date: Oct 16, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class UnplugUSBCableDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "unplug_usb_cable_dialog"

    def __init__(self, driver):
        super(UnplugUSBCableDialog, self).__init__(driver)

    #  -----------------------------Operate Elements------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[UnplugUSBCableDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("unplug_usb_cable_dialog_image", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Unplug USB Cable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnplugUSBCableDialog]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("unplug_usb_cable_dialog_continue_btn")

    def get_value_of_unplug_usb_cable_dialog_title(self):
        '''
        This is a method to get the value of Unplug USB Cable dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[UnplugUSBCableDialog:[get_value_of_unplug_usb_cable_dialog_title]-Get the contents of Unplug USB Cable dialog title...  ")

        return self.driver.get_value("unplug_usb_cable_dialog_title")

    def get_value_of_unplug_usb_cable_dialog_contents(self):
        '''
        This is a method to get the value of Unplug USB Cable dialog contents.
        :parameter:
        :return:
        '''
        logging.debug("[UnplugUSBCableDialog]:[get_value_of_contents]-Get the contents of contents..  ")

        return self.driver.get_value("unplug_usb_cable_dialog_contents")

    def get_value_of_unplug_usb_cable_dialog_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Unplug USB Cable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnplugUSBCableDialog]:[get_value_of_unplug_usb_cable_dialog_continue_btn]-Get the contents of Continue button..  ")

        return self.driver.get_title("unplug_usb_cable_dialog_continue_btn")

    # --------------------Verification Methods------------------------------------------
    def verify_unplug_usb_cable_dialog(self):
        '''
        This is a verification method to check UI strings of Don't forget to unplug the USB Cable dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Don't forget to unplug the USB Cable dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='dont_forget_to_unplug_the_usb_cable_dialog')
        assert self.get_value_of_unplug_usb_cable_dialog_title() == test_strings['dont_forget_to_unplug_the_usb_cable_dialog_title']
        assert test_strings['dont_forget_to_unplug_the_usb_cable_dialog_contents'] in self.get_value_of_unplug_usb_cable_dialog_contents()
        assert self.get_value_of_unplug_usb_cable_dialog_continue_btn() == test_strings['dont_forget_to_unplug_the_usb_cable_dialog_continue_btn']
