# encoding: utf-8
'''
Description: It defines operations of element and verification methods for Add Shortcut screen.

@author: Ivan
@create_date: Jun 29, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class AddShortcutScreen(SmartScreens):

    folder_name = "shortcuts"
    flow_name = "add_shortcut_screen"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(AddShortcutScreen, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Add Shortcut screen load.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("create_your_own_shortcut_link", timeout=timeout, raise_e=raise_e)

    def click_add_shortcut_screen_back_btn(self):
        '''
        This is a method to click Back button on Add Shortcut screen.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[click_add_shortcut_screen_back_btn]-Click Back button... ")

        self.driver.click("add_shortcut_screen_back_btn", is_native_event=True)

    def click_add_shortcut_screen_help_btn(self):
        '''
        This is a method to click Help button on Add Shortcut screen.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[click_add_shortcut_screen_help_btn]-Click Help button... ")

        self.driver.click("add_shortcut_screen_help_btn", is_native_event=True)

    def click_create_your_own_shortcut_link(self):
        '''
        This is a method to click Create Your Own Shortcut link on Add Shortcut screen.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[click_create_your_own_shortcut_link]-Click Create Your Own Shortcut link... ")

        self.driver.click("create_your_own_shortcut_link", is_native_event=True)

    def click_save_to_google_driver_link(self):
        '''
        This is a method to click Save to Google Driver link on Add Shortcut screen.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[click_save_to_google_driver_link]-Click Save to Google Driver link... ")

        self.driver.click("save_to_google_driver_link", is_native_event=True)

    def click_print_email_and_save_link(self):
        '''
        This is a method to click Print Email and Save link on Add Shortcut screen.
        :parameter:
        :return:
        '''
        logging.debug("[AddShortcutScreen]:[click_print_email_and_save_link]-Click Print Email and Save link... ")

        self.driver.click("print_email_and_save_link", is_native_event=True)
