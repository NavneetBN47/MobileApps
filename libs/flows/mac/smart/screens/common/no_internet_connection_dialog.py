# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on No Internet Connection dialog.

@author: Ivan
@create_date: Oct 12, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class NoInternetConnectionDialog(SmartScreens):

    folder_name = "common"
    flow_name = "no_internet_connection_dialog"

    def __init__(self, driver):
        super(NoInternetConnectionDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait no Internet connection dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_internet_connection_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("no_internet_connection_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents_1
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("no_internet_connnection_contents")

    def get_value_of_network_btn(self):
        '''
        This is a method to get value of Network button on No internet connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_network_btn]-Get the contents of Network button ...  ")

        return self.driver.get_title("network_btn")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on No Internet Connection dialog
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_cancel_btn]-Get the contents of Cancel button ...  ")

        return self.driver.get_title("cancel_btn")

    def get_value_of_retry_ok_btn(self):
        '''
        This is a method to get value of Retry/OK button on No Internet Connection dialog
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_retry_ok_btn]-Get the contents of Retry button ...  ")

        return self.driver.get_title("retry_ok_btn")

    def click_network_btn(self):
        '''
        This is a method to click Network button on No Internet Connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[click_network_btn]-Click Network button... ")

        self.driver.click("network_btn", is_native_event=True)

    def click_cancel_btn(self):
        '''
        This is a method to click Cancel button on No Internet Connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[click_cancel_btn]-Click Cancel button... ")

        self.driver.click("cancel_btn", is_native_event=True)

    def click_retry_ok_btn(self):
        '''
        This is a method to click Retry/OK button on No Internet Connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[click_retry_ok_btn]-Click Retry/OK button... ")

        self.driver.click("retry_ok_btn", is_native_event=True)

# -------------------------------Verification Methods-------------------------------
    def verify_no_internet_connection_with_ok_btn_dialog(self):
        '''
        This is a verification method to check UI strings of No Internet Connection with OK button dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of No Internet Connection with OK button dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_internet_connection_dialog')
        assert self.get_value_of_dialog_title() == test_strings['no_internet_connection_title']
        assert self.get_value_of_dialog_contents() == test_strings['no_internet_connnection_contents']
        assert self.get_value_of_retry_ok_btn() == test_strings['ok_btn']
#         assert self.get_value_of_network_and_internet_btn() == test_strings['network_and_internet_btn']

    def verify_no_internet_connection_with_retry_btn_dialog(self):
        '''
        This is a verification method to check UI strings of No Internet Connection with Retry button dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of No Internet Connection with Retry button dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_internet_connection_dialog')
        assert self.get_value_of_dialog_title() == test_strings['no_internet_connection_title']
        assert self.get_value_of_dialog_contents() == test_strings['no_internet_connnection_contents']
        assert self.get_value_of_cancel_btn() == test_strings['cancel_btn']
        assert self.get_value_of_retry_ok_btn() == test_strings['retry_btn']

    def verify_no_internet_connection_with_network_btn_dialog(self):
        '''
        This is a verification method to check UI strings of No Internet Connection with Network button dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of No Internet Connection with Network button dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_internet_connection_dialog')
        assert self.get_value_of_dialog_title() == test_strings['no_internet_connection_title']
        assert self.get_value_of_dialog_contents() == test_strings['no_internet_connnection_contents']
        assert self.get_value_of_cancel_btn() == test_strings['cancel_btn']
        assert self.get_value_of_retry_ok_btn() == test_strings['retry_btn']
        assert self.get_value_of_network_btn() == test_strings['network_btn']

    def verify_dialog_disappear(self):
        '''
        verify No Internet Connection dialog disappear after clicking OK button.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("no_internet_connection_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen display")
        return True
