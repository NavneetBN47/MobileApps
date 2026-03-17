# encoding: utf-8
'''
Description: no printer printer settings dialog

@author: Ten
@create_date: Oct 15, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class HP_Smart_Waring_Dialog(SmartScreens):

    folder_name = "common"
    flow_name = "hp_smart_waring_dialog"

    def __init__(self, driver):
        super(HP_Smart_Waring_Dialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[HP_Smart_Waring_Dialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click ok button.
        :parameter:
        :return:
        '''
        logging.debug("[HP_Smart_Waring_Dialog]:[click_ok_btn]-Click ok_btn... ")

        self.driver.click("ok_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[HP_Smart_Waring_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content_text(self):
        '''
        This is a method to get value of dialog_content_text
        :parameter:
        :return:
        '''
        logging.debug("[HP_Smart_Waring_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_content_text")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[HP_Smart_Waring_Dialog]:[get_value_of_ok_btn]-Get ok_btn..  ")

        return self.driver.get_title("ok_btn")

# -------------------------------Verification Methods---------------------------------------
    def verify_hp_smart_warning_dialog(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()

        logging.debug("Verify strings are translated correctly and matching string table.")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hp_smart_warning_dialog')
        assert self.get_value_of_dialog_title() == test_strings['hp_smart_warning_dialog_title']
        assert self.get_value_of_dialog_content_text() == test_strings['hp_smart_warning_dialog_body']
        assert self.get_value_of_ok_btn() == test_strings['hp_smart_warning_dialog_ok_btn']
