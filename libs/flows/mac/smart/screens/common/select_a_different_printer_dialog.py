# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the select a different printer dialog

@author: ten
@create_date: Jun 11, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class SelectDifferentprinterDialog(SmartScreens):

    folder_name = "common"
    flow_name = "select_a_different_printer_dialog"

    def __init__(self, driver):
        super(SelectDifferentprinterDialog, self).__init__(driver)

#   ----------------------------Operate Elements--------------------------------------------
    def wait_for_screen_load(self,timeout=30,raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[SelectDifferentprinterDialog]:[wait_for_to_select_a_different_printer_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click ok btn
        :parameter:
        :return:
        '''
        logging.debug("[SelectDifferentprinterDialog]:[click_ok_btn-Click 'ok' button... ")

        self.driver.click("ok_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[SelectDifferentprinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[SelectDifferentprinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_content")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[SelectDifferentprinterDialog]:[get_value_of_ok_btn]-Get the contents of ok_btn ...  ")

        return self.driver.get_title("ok_btn")

#    ---------------------------Verification Methods-----------------------------------
    def verify_ui_strings(self, host_name):
        '''
        This is a verification method to check UI strings of select a different printer dialog 
        :parameter:
        :return:
        '''
        logging.debug("Start to check UI strings of select a different printer dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='select_a_different_printer_dialog')
        self.wait_for_screen_load()
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
        assert self.get_value_of_dialog_content() == host_name + test_strings['dialog_content']
        assert self.get_value_of_ok_btn() == test_strings['ok_btn']

    def verify_dialog_disappear(self, timeout=30):
        '''
        This is a verification method to verify Select Different printer Dialog disappear after click OK button.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object_disappear("dialog_title", timeout=timeout, raise_e=False)
