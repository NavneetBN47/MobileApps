# encoding: utf-8
'''
check No USB dialog

@author: ten
@create_date: Aug 23, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class NoUSBDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "no_usb_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(NoUSBDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_image", timeout=timeout, raise_e=raise_e)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get the value of No USB dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[get_value_of_dialog_title]-Get the contents of No USB dialog title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content(self):
        '''
        This is a method to get the value of No USB dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[get_value_of_dialog_content]-Get the contents of No USB dialog content...  ")

        return self.driver.get_value("dialog_content")

    def get_value_of_more_help_btn(self):
        '''
        This is a method to get the value of More Help button on No USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[get_value_of_more_help_btn]-Get the contents of More Help button...  ")

        return self.driver.get_title("more_help_btn")

    def get_value_of_done_btn(self):
        '''
        This is a method to get the value of Done button on No USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[get_value_of_done_btn]-Get the contents of Done button...  ")

        return self.driver.get_title("done_btn")

    def click_more_help_btn(self):
        '''
        This is a method to Click More Help button on No USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[click_more_help_btn]-Click More Help button.. ")

        self.driver.click("more_help_btn")

    def click_done_btn(self):
        '''
        This is a method to Click Done button on No USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[click_done_btn]-Click Done button.. ")

        self.driver.click("done_btn")

# -------------------------------Verification Methods--------------------------------------------
    def verify_no_usb_dialog(self):
        '''
        This is a verification method to check UI strings of No USB dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of No USB dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_usb_dialog')
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
        assert self.get_value_of_dialog_content() == test_strings['dialog_contents']
        assert self.get_value_of_more_help_btn() == test_strings['more_help_btn']
        assert self.get_value_of_done_btn() == test_strings['done_btn']
