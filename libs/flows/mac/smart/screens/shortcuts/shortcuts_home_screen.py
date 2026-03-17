# encoding: utf-8
'''
Description: It defines operations of element and verification methods for Shortcuts Home screen.

@author: Ivan
@create_date: Jun 24, 2021
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ShortcutsHomeScreen(SmartScreens):

    folder_name = "shortcuts"
    flow_name = "shortcuts_home_screen"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ShortcutsHomeScreen, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Shortcuts home screen load.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("shortcuts_home_screen_add_shortcut_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_coach_mark_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Coachmark load on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[wait_for_coach_mark_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("coach_mark_text", timeout=timeout, raise_e=raise_e)

    def wait_for_coach_mark_disappear(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Coachmark disappear on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[wait_for_coach_mark_disappear]-Wait for screen disappear... ")

        return self.driver.wait_for_object_disappear("coach_mark_text", timeout=timeout, raise_e=raise_e)

    def wait_for_shortcuts_empty_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Shortcuts Empty screen load.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[wait_for_shortcuts_empty_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("shortcuts_empty_screen_create_one_touch_shortcuts_text", timeout=timeout, raise_e=raise_e)

    def wait_for_delete_shortcut_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Delete Shortcut dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[wait_for_delete_shortcut_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("delete_shortcut_dialog_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_coach_mark_text(self):
        '''
        This is a method to get value of Coachmark text on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[get_value_of_coach_mark_text]-Get value of Coachmark text...  ")

        return self.driver.get_value("coach_mark_text")

    def get_value_of_shortcut_first_list_item(self):
        '''
        This is a method to get value of the first shortcut item name on Shortcuts home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[get_value_of_shortcut_first_list_item]-Get value of the first shortcut item name...  ")

        return self.driver.get_title("shortcut_first_list_item")

    def click_back_btn(self):
        '''
        This is a method to click Back button on Shortcuts Home screen or Shortcuts Empty screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_back_btn]-Click Back button... ")

        self.driver.click("shortcuts_home_screen_back_btn", is_native_event=True)

    def click_help_btn(self):
        '''
        This is a method to click Help button on Shortcuts Home screen or Shortcuts Empty screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_help_btn]-Click Help button... ")

        self.driver.click("shortcuts_home_screen_help_btn", is_native_event=True)

    def click_add_shortcuts_btn(self):
        '''
        This is a method to click Add Shortcuts button on Shortcuts Home screen or Shortcuts Empty screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_add_shortcuts_btn]-Click Add Shortcuts button... ")

        self.driver.click("shortcuts_home_screen_add_shortcut_btn", is_native_event=True)

    def click_specified_shortcut(self, shortcut_name):
        '''
        This is a method to click Specified Shortcut on Shortcut home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_specified_shortcut]-Click Specified Shortcut... ")

        self.driver.click("shortcut_list_item", format_specifier=[shortcut_name], is_native_event=True)

    def click_three_vertical_dotes_btn(self):
        '''
        This is a method to click the three vertical dotes button for the first shortcuts item on Shortcuts Home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_three_vertical_dotes_btn]-Click three vertical dotes button... ")

        self.driver.click("three_vertical_dotes_btn", is_native_event=True)

    def click_flyout_menu_start_item(self):
        '''
        This is a method to click the Start item on flyout menu after clicking three vertical dotes button for the first shortcuts item on Shortcuts Home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_flyout_menu_start_item]-Click Start item... ")

        self.driver.click("flyout_menu_start_item", is_native_event=True)

    def click_flyout_menu_edit_item(self):
        '''
        This is a method to click the Edit item on flyout menu after clicking three vertical dotes button for the first shortcuts item on Shortcuts Home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_flyout_menu_edit_item]-Click Edit item... ")

        self.driver.click("flyout_menu_edit_item", is_native_event=True)

    def click_flyout_menu_delete_item(self):
        '''
        This is a method to click the Delete item on flyout menu after clicking three vertical dotes button for the first shortcuts item on Shortcuts Home screen.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_flyout_menu_delete_item]-Click Delete item... ")

        self.driver.click("flyout_menu_delete_item", is_native_event=True)

    def click_delete_dialog_yes_delete_btn(self):
        '''
        This is a method to click Yes, Delete button on Delete Shortcut dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_delete_dialog_yes_delete_btn]-Click Yes, Delete button... ")

        self.driver.click("delete_dialog_yes_delete_btn", is_native_event=True)

    def click_delete_dialog_no_cancel_btn(self):
        '''
        This is a method to click No, Cancel button on Delete Shortcut dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_delete_dialog_no_cancel_btn]-Click No, Cancel button... ")

        self.driver.click("delete_dialog_no_cancel_btn", is_native_event=True)

    def click_coach_mark_close_btn(self):
        '''
        This is a method to click Coachmark Close button on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_coach_mark_close_btn]-Click Coachmark Close button... ")

        self.driver.click("coach_mark_close_btn", is_native_event=True)

    def click_coach_mark_right_arrow_btn(self):
        '''
        This is a method to click Coachmark Right arrow button on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_coach_mark_right_arrow_btn]-Click Coachmark Right arrow button... ")

        self.driver.click("coach_mark_right_arrow_btn", is_native_event=True)

    def click_coach_mark_left_arrow_btn(self):
        '''
        This is a method to click Coachmark Left arrow button on Shortcuts home screen with a new user.
        :parameter:
        :return:
        '''
        logging.debug("[ShortcutsHomeScreen]:[click_coach_mark_left_arrow_btn]-Click Coachmark Left arrow button... ")

        self.driver.click("coach_mark_left_arrow_btn", is_native_event=True)
