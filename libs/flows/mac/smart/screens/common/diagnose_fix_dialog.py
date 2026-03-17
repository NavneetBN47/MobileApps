# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the Diagnose&Fix Dialog

@author: ten
@create_date: Nov 2, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class Diagnose_Fix_Dialog(SmartScreens):

    folder_name = "common"
    flow_name = "diagnose_fix_dialog"

    def __init__(self, driver):
        super(Diagnose_Fix_Dialog, self).__init__(driver)

#  ----------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_content", timeout=timeout, raise_e=raise_e)
    
    def wait_for_start_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("start_dialog_content_1", timeout=timeout, raise_e=raise_e)
 
    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content(self):
        '''
        This is a method to get value of dialog_content
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dialog_title]-dialog_content...  ")

        return self.driver.get_value("dialog_content")

    def get_value_of_allow_btn(self):
        '''
        This is a method to get value of allow_btn
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_allow_btn]-allow_btn..  ")

        return self.driver.get_title("allow_btn")

    def get_value_of_dont_allow_btn(self):
        '''
        This is a method to get value of dont_allow_btn
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dont_allow_btn]-dont_allow_btn..  ")

        return self.driver.get_title("dont_allow_btn")

    def get_value_of_start_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("start_dialog_title")

    def get_value_of_start_dialog_content_1(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dialog_title]-Get dialog_content...  ")

        return self.driver.get_value("start_dialog_content_1")

    def get_value_of_start_dialog_content_2(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_dialog_title]-Get dialog_content...  ")

        return self.driver.get_value("start_dialog_content_2")

    def get_value_of_off_icon(self):
        '''
        This is a method to get value of off_icon
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_off_icon]-off_icon..  ")

        return self.driver.get_title("off_icon")

    def get_value_of_on_icon(self):
        '''
        This is a method to get value of on_icon
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_on_icon]-on_icon..  ")

        return self.driver.get_title("on_icon")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_cancel_btn]-cancel_btn..  ")

        return self.driver.get_title("cancel_btn")

    def get_value_of_apply_btn(self):
        '''
        This is a method to get value of apply_btn
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[get_value_of_apply_btn]-apply_btn..  ")

        return self.driver.get_title("apply_btn")

    def click_allow_btn(self):
        '''
        This is a method to click allow_btn.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_allow_btn]-Click allow_btn... ")

        self.driver.click("allow_btn", is_native_event=True)

    def click_dont_allow_btn(self):
        '''
        This is a method to click dont_allow_btn.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_dont_allow_btnn]-Click dont_allow_btn... ")

        self.driver.click("dont_allow_btn", is_native_event=True)

    def click_off_icon(self):
        '''
        This is a method to click off_icon.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_off_icon]-Click off_icon... ")

        self.driver.click("off_icon", is_native_event=True)

    def click_on_icon(self):
        '''
        This is a method to click on_icon.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_on_icon]-Click on_icon... ")

        self.driver.click("on_icon", is_native_event=True)

    def click_cancel_btn(self):
        '''
        This is a method to click cancel_btn.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_cancel_btn]-Click cancel_btn... ")

        self.driver.click("cancel_btn", is_native_event=True)

    def click_apply_btn(self):
        '''
        This is a method to click apply_btn.
        :parameter:
        :return:
        '''
        logging.debug("[Diagnose_Fix_Dialog]:[click_apply_btn]-Click apply_btn... ")

        self.driver.click("apply_btn", is_native_event=True)

#   -----------------------------Verification Methods-----------------------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.wait_for_screen_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix_dialog')
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
        assert self.get_value_of_dialog_content() == test_strings['dialog_content']
        assert self.get_value_of_allow_btn() == test_strings['allow_btn']
        assert self.get_value_of_dont_allow_btn() == test_strings['dont_allow_btn']

    def verify_start_dialog_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.wait_for_start_dialog_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix_dialog')
        assert self.get_value_of_start_dialog_title() == test_strings['start_dialog_title']
        assert test_strings['start_dialog_content_1_1'] and test_strings['start_dialog_content_1_2'] in self.get_value_of_start_dialog_content_1()
        assert self.get_value_of_start_dialog_content_2() == test_strings['start_dialog_content_2']
        assert self.get_value_of_off_icon() == test_strings['off_icon']
        assert self.get_value_of_on_icon() == test_strings['on_icon']
        assert self.get_value_of_cancel_btn() == test_strings['cancel_btn']
        assert self.get_value_of_apply_btn() == test_strings['apply_btn']

    def verify_dialog_not_display(self):
        if self.driver.wait_for_object("dialog_content", raise_e=False):
            raise UnexpectedItemPresentException("the screen display")
        return True
