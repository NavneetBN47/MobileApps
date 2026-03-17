# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the enjoying hp smart screen.

@author: ten
@create_date: Jun 23, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class Enjoying_HP_Smart_Dialog(SmartScreens):

    folder_name = "common"
    flow_name = "enjoying_hp_smart_dialog"

    def __init__(self, driver):
        super(Enjoying_HP_Smart_Dialog ,self).__init__(driver)

# -----------------------------Operate Elements--------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click ok button.
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[click_ok_btn]-Click ok_btn... ")

        self.driver.click("ok_btn", is_native_event=True)

    def click_not_now_btn(self):
        '''
        This is a method to click not_nowbutton.
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[click_not_now_btn]-Click not_now_btn... ")

        self.driver.click("no_btn", is_native_event=True)

    def click_yes_btn(self):
        '''
        This is a method to click yes button.
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[click_yes_btn]-Click yes_btn... ")

        self.driver.click("yes_btn", is_native_event=True)

    def click_no_btn(self):
        '''
        This is a method to click no button.
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[click_no_btn]-Click no_btn... ")

        self.driver.click("no_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content_text(self):
        '''
        This is a method to get value of dialog_content_text
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_content_text")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[Enjoying_HP_Smart_Dialog]:[get_value_of_ok_btn]-Get ok_btn..  ")

        return self.driver.get_title("ok_btn")

# -------------------------------Verification Methods---------------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.wait_for_screen_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='enjoying_hp_smart_dialog')
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
        assert self.get_value_of_dialog_content_text() == test_strings['dialog_content']
        assert self.get_value_of_ok_btn() == test_strings['ok_btn']

    def verify_screen_not_display(self):
        if self.driver.wait_for_object("dialog_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen display")
        return True
