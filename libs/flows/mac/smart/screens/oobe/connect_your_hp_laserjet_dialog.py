# encoding: utf-8
'''
check connect your HP laserjet dialog

@author: ten
@create_date: Aug 22, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectYourHPLaserJetDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "connect_your_hp_laserjet_dialog"

    def __init__(self, driver):
        super(ConnectYourHPLaserJetDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_image", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        Click continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of Connect Your HP LaserJet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content(self):
        '''
        This is a method to get value of Connect Your HP LaserJet dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_dialog_content]-Get the contents of contents_1...  ")

        return self.driver.get_value("dialog_content")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect Your HP LaserJet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_continue_btn]-Get the contents of continue_btn...  ")

        return self.driver.get_title("continue_btn")

#  -------------------------------Verification Methods------------------------
    def verify_connect_your_hp_laserjet_dialog(self):
        '''
        This is a verification method to check UI strings of Connect Your HP LaserJet Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect Your HP LaserJet Dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_your_hp_laserjet_dialog')
        assert self.get_value_of_dialog_title() == test_strings['dialog_title']
#         assert self.get_value_of_dialog_content() == test_strings['dialog_content']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']
