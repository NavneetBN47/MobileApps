# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Account/Suppliles.

@author: Ivan
@create_date: Nov 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ActivityCenterAccount(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_account"

    def __init__(self, driver):
        super(ActivityCenterAccount, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait View Notifications screen shows correctly after clicking Account/Supplies item on Activity Center flyout.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterAccount]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("your_most_recent_notifications_will_appear_here_text", timeout=timeout, raise_e=raise_e)

    def get_value_of_view_notifications_screen_title(self):
        '''
        This is a method to get value of View Notifications screen title
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterAccount]:[get_value_of_view_notifications_screen_title]-Get the value of View Notifications screen title...  ")

        return self.driver.get_title("view_notifications_screen_title")

    def get_value_of_view_all_your_recent_account_notifications_text(self):
        '''
        This is a method to get value of View all your recent account notifications text on View Notifications screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterAccount]:[get_value_of_view_all_your_recent_account_notifications_text]-Get the value of View all your recent account notifications text...  ")

        return self.driver.get_value("view_all_your_recent_account_notifications_text")

    def get_value_of_your_most_recent_notifications_will_appear_here_text(self):
        '''
        This is a method to get value of Your most recent notifications will appear here text on View Notifications screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterAccount]:[get_value_of_your_most_recent_notifications_will_appear_here_text]-Get the value of Your most recent notifications will appear here text...  ")

        return self.driver.get_value("your_most_recent_notifications_will_appear_here_text")

# -------------------------------Verification Methods-------------------------------
    def verify_view_notifications_screen(self):
        '''
        This is a verification method to check UI strings of View Notifications screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of View Notifications screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='view_notifications_screen')
        assert self.get_value_of_view_notifications_screen_title() == test_strings['view_notifications_screen_title']
        assert self.get_value_of_view_all_your_recent_account_notifications_text() == test_strings['view_all_your_recent_account_notifications_text']
        assert self.get_value_of_your_most_recent_notifications_will_appear_here_text() == test_strings['your_most_recent_notifications_will_appear_here_text']
