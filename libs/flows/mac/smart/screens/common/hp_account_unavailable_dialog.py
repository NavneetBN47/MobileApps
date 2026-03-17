# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on HP Account Unavailable dialog.

@author: Ivan
@create_date: Dec 02, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class HPAccountUnavailableDialog(SmartScreens):

    folder_name = "common"
    flow_name = "hp_account_unavailable_dialog"

    def __init__(self, driver):
        super(HPAccountUnavailableDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait HP Account Unavailable dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("hp_account_unavailable_dialog_contents", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self):
        '''
        This is a method to click Cancel button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[click_cancel_btn]-Click Cancel button... ")

        self.driver.click("hp_account_unavailable_dialog_cancel_btn")

    def click_ok_btn(self):
        '''
        This is a method to click Ok button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[click_ok_btn]-Click Ok button... ")

        self.driver.click("hp_account_unavailable_dialog_ok_btn")

    def click_try_again_btn(self):
        '''
        This is a method to click Try Again button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[click_try_again_btn]-Click Try Again button... ")

        self.driver.click("hp_account_unavailable_dialog_try_again_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("hp_account_unavailable_dialog_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents_1
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("hp_account_unavailable_dialog_contents")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[get_value_of_cancel_btn]-Get the value of Cancel button ... ")

        return self.driver.get_title("hp_account_unavailable_dialog_cancel_btn")

    def get_value_of_try_again_btn(self):
        '''
        This is a method to get value of Try Again button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[get_value_of_try_again_btn]-Get the value of Try Again button ... ")

        return self.driver.get_title("hp_account_unavailable_dialog_try_again_btn")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of OK button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HPAccountUnavailableDialog]:[get_value_of_ok_btn]-Get the value of OK button ... ")

        return self.driver.get_title("hp_account_unavailable_dialog_ok_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_hp_account_unavailable_with_ok_btn_dialog(self):
        '''
        This is a verification method to check UI strings of HP Account Unavailable dialog with OK button.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of HP Account Unavailable dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hp_account_unavailable_dialog')
        assert self.get_value_of_dialog_title() == test_strings['hp_account_unavailable_title']
        assert self.get_value_of_dialog_contents() == test_strings['hp_account_unavailable_body']
        assert self.get_value_of_ok_btn() == test_strings['hp_account_unavailable_ok_btn']

    def verify_hp_account_unavailable_with_try_again_btn_dialog(self):
        '''
        This is a verification method to check UI strings of HP Account Unavailable dialog with Cancel and Try again button.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of HP Account Unavailable dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hp_account_unavailable_dialog')
        assert self.get_value_of_dialog_title() == test_strings['hp_account_unavailable_title']
        assert self.get_value_of_dialog_contents() == test_strings['hp_account_unavailable_body']
        assert self.get_value_of_cancel_btn() == test_strings['hp_account_unavailable_cancel_btn']
        assert self.get_value_of_try_again_btn() == test_strings['hp_account_unavailable_try_again_btn']

    def verify_dialog_disappear(self, timeout=10):
        '''
        verify HP Account Unavailable dialog disappear after clicking Cancel button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("hp_account_unavailable_dialog_contents", timeout=timeout, raise_e=False)
