# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Firmware Update Available screen.

@author: Ivan
@create_date: Dec 09, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class FirmwareUpdateAvailable(SmartScreens):
    folder_name = "common"
    flow_name = "firmware_update_available"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(FirmwareUpdateAvailable, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait save dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FirmwareUpdateAvailable]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("firmware_update_available_screen_content_1", timeout=timeout, raise_e=raise_e)

    def click_firmware_update_available_screen_yes_btn(self):
        '''
        This is a method to click Yes button on Firmware Update Available screen.
        :parameter:
        :return:
        '''
        logging.debug("[FirmwareUpdateAvailable]:[click_firmware_update_available_screen_yes_btn]-Click Yes button... ")

        self.driver.click("firmware_update_available_screen_yes_btn", is_native_event=True)

    def click_firmware_update_available_screen_no_btn(self):
        '''
        This is a method to click No button on Firmware Update Available screen.
        :parameter:
        :return:
        '''
        logging.debug("[FirmwareUpdateAvailable]:[click_firmware_update_available_screen_no_btn]-Click No button... ")

        self.driver.click("firmware_update_available_screen_no_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
