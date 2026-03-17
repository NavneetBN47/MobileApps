# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Unable to reset wifi setup mode dialog.

@author: Ivan
@create_date: Apr 09, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class UnableToResetWifiSetupMode(SmartScreens):
    folder_name = "oobe"
    flow_name = "unable_to_reset_wifi_setup_mode"

    def __init__(self, driver):
        super(UnableToResetWifiSetupMode, self).__init__(driver)

# -------------------------------Operate Elements------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("unable_to_reset_wifi_setup_mode_image", timeout=timeout, raise_e=raise_e)

    def click_show_me_how_btn(self):
        '''
        This is a method to click Show me how button on Unable to reset wifi setup mode dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[click_show_me_how_btn]-Click Show me how button.. ")

        self.driver.click("unable_to_reset_wifi_setup_mode_show_me_how_btn", is_native_event=True)

    def click_try_again_btn(self):
        '''
        This is a method to click Try Again button on Unable to reset wifi setup mode dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[click_try_again_btn]-Click Try Again button.. ")

        self.driver.click("unable_to_reset_wifi_setup_mode_try_again_btn", is_native_event=True)

    def get_value_of_unable_to_reset_wifi_setup_mode_title(self):
        '''
        This is a method to get the value of Unable to reset wifi setup mode dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[get_value_of_unable_to_reset_wifi_setup_mode_title]-Get the contents of Unable to reset wifi setup mode dialog title...  ")

        return self.driver.get_value("unable_to_reset_wifi_setup_mode_title")

    def get_value_of_unable_to_reset_wifi_setup_mode_contents(self):
        '''
        This is a method to get the value of Unable to reset wifi setup mode dialog contents.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[get_value_of_unable_to_reset_wifi_setup_mode_contents]-Get the contents of Unable to reset wifi setup mode dialog contents...  ")

        return self.driver.get_value("unable_to_reset_wifi_setup_mode_contents")

    def get_value_of_unable_to_reset_wifi_setup_mode_show_me_how_btn(self):
        '''
        This is a method to get the value of Show me how button on Unable to reset wifi setup mode dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[get_value_of_unable_to_reset_wifi_setup_mode_show_me_how_btn]-Get the contents of Show me how button..  ")

        return self.driver.get_title("unable_to_reset_wifi_setup_mode_show_me_how_btn")

    def get_value_of_unable_to_reset_wifi_setup_mode_try_again_btn(self):
        '''
        This is a method to get the value of Try Again button on Unable to reset wifi setup mode dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UnableToResetWifiSetupMode]:[get_value_of_unable_to_reset_wifi_setup_mode_try_again_btn]-Get the contents of Try Again button..  ")

        return self.driver.get_title("unable_to_reset_wifi_setup_mode_try_again_btn")

# -------------------------------Verification Methods---------------
    def verify_unable_to_reset_wifi_setup_mode_dialog(self):
        '''
        This is a verification method to check UI strings of Unable to reset wifi setup mode dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of Unable to reset wifi setup mode dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='unable_to_reset_wifi_setup_mode_dialog')
        assert self.get_value_of_unable_to_reset_wifi_setup_mode_title() == test_strings['unable_to_reset_wifi_setup_mode_title']
        assert self.get_value_of_unable_to_reset_wifi_setup_mode_contents() == test_strings['unable_to_reset_wifi_setup_mode_contents']
        assert self.get_value_of_unable_to_reset_wifi_setup_mode_show_me_how_btn() == test_strings['unable_to_reset_wifi_setup_mode_show_me_how_btn']
        assert self.get_value_of_unable_to_reset_wifi_setup_mode_try_again_btn() == test_strings['unable_to_reset_wifi_setup_mode_try_again_btn']
