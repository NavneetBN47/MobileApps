# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Fly-out.

@author: Ivan
@create_date: Jan 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ActivityCenterFlyout(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_flyout"

    def __init__(self, driver):
        super(ActivityCenterFlyout, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Fly-out shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activity_center_shortcuts", timeout=timeout, raise_e=raise_e)

    def wait_for_activity_center_print_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Print list shows correctly on Activity Center Fly-out screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[wait_for_activity_center_print_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activity_center_print", timeout=timeout, raise_e=raise_e)

    def wait_for_activity_center_text_files_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Text File list shows correctly on Activity Center Fly-out screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[wait_for_activity_center_text_files_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activity_center_text_files", timeout=timeout, raise_e=raise_e)

    def click_activity_center_print(self):
        '''
        This is a method to click Print option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_print]-Click Print option... ")

        self.driver.click("activity_center_print", is_native_event=True)

    def click_activity_center_shortcuts(self):
        '''
        This is a method to click Shortcuts option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_shortcuts]-Click Shortcuts option... ")

        self.driver.click("activity_center_shortcuts", is_native_event=True)

    def click_activity_center_text_files(self):
        '''
        This is a method to click Text Files option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_text_files]-Click Text Files option... ")

        self.driver.click("activity_center_text_files", is_native_event=True)

    def click_activity_center_mobile_fax(self):
        '''
        This is a method to click Mobile Fax option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_mobile_fax]-Click Mobile Fax option... ")

        self.driver.click("activity_center_mobile_fax", is_native_event=True)

    def click_activity_center_supplies(self):
        '''
        This is a method to click Supplies option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_supplies]-Click Supplies option... ")

        self.driver.click("activity_center_supplies", is_native_event=True)

    def click_activity_center_account(self):
        '''
        This is a method to click Account option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]]:[click_activity_center_account]-Click Account option... ")

        self.driver.click("activity_center_account", is_native_event=True)

    def get_value_of_activity_center_print(self):
        '''
        This is a method to get value of Print option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_print]-Get the value of Print option ...  ")

        return self.driver.get_title("activity_center_print")

    def get_value_of_activity_center_shortcuts(self):
        '''
        This is a method to get value of Shortcuts option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_shortcuts]-Get the value of Shortcuts option ...  ")

        return self.driver.get_title("activity_center_shortcuts")

    def get_value_of_activity_center_text_files(self):
        '''
        This is a method to get value of Text Files option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_text_files]-Get the value of Text Files option ...  ")

        return self.driver.get_title("activity_center_text_files")

    def get_value_of_activity_center_mobile_fax(self):
        '''
        This is a method to get value of Mobile Fax option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_mobile_fax]-Get the value of Mobile Fax option ...  ")

        return self.driver.get_title("activity_center_mobile_fax")

    def get_value_of_activity_center_supplies(self):
        '''
        This is a method to get value of Supplies option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_supplies]-Get the value of Mobile Fax option ...  ")

        return self.driver.get_title("activity_center_supplies")

    def get_value_of_activity_center_account(self):
        '''
        This is a method to get value of Account option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterFlyout]:[get_value_of_activity_center_account]-Get the value of Mobile Fax option ...  ")

        return self.driver.get_title("activity_center_account")

# -------------------------------Verification Methods-------------------------------
    def verify_activity_center_flyout_screen(self, printer_added=True, text_files=False):
        '''
        This is a verification method to check UI strings of Activity Center Fly-out screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Activity Center Fly-out screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='activity_center_flyout')
        if printer_added:
            self.wait_for_activity_center_print_load()
            assert self.get_value_of_activity_center_print() == test_strings['activity_center_print']
        else:
            self.verify_no_activity_center_print_list()

        if text_files:
            self.wait_for_activity_center_text_files_load()
            assert self.get_value_of_activity_center_text_files() == test_strings['activity_center_text_files']
        else:
            self.verify_no_activity_center_text_files_list()
        assert self.get_value_of_activity_center_shortcuts() == test_strings['activity_center_shortcuts']
        assert self.get_value_of_activity_center_mobile_fax() == test_strings['activity_center_mobile_fax']
        assert self.get_value_of_activity_center_supplies() == test_strings['activity_center_supplies']
        assert self.get_value_of_activity_center_account() == test_strings['activity_center_account'] or self.get_value_of_activity_center_account() == test_strings['activity_center_account_2']

    def verify_no_activity_center_print_list(self, timeout=2):
        '''
        This is a verification method to verify activity center Print list is not show on Activity Center Fly-out screen.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("activity_center_print", timeout=timeout, raise_e=False)

    def verify_no_activity_center_text_files_list(self, timeout=2):
        '''
        This is a verification method to verify activity center Text Files list is not show on Activity Center Fly-out screen.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("activity_center_text_files", timeout=timeout, raise_e=False)

    def verify_dialog_disappear(self, timeout=10):
        '''
        verify Activity Center Fly-out screen disappear after select one of the options.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("activity_center_mobile_fax", timeout=timeout, raise_e=False)
