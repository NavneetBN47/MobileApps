# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the install hp smart screen.

@author: ten
@create_date: Jun 10, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class InstallHpSmart(SmartScreens):
    folder_name = "common"
    flow_name = "install_hp_smart"

    def __init__(self, driver):
        super(InstallHpSmart, self).__init__(driver)

# -------------------------------Operate Elements-------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug(
            "[InstallHpSmart]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("hp_smart_installer_title", timeout=timeout, raise_e=raise_e)

    def wait_for_select_destination_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug(
            "[InstallHpSmart]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("go_back_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_installation_type_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug(
            "[InstallHpSmart]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("change_install_location_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_successfull_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug(
            "[InstallHpSmart]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("successfull_screen_title", timeout=timeout, raise_e=raise_e)

    def wait_for_input_password_screen(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug(
            "[InstallHpSmart]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("install_software_btn", timeout=timeout, raise_e=raise_e)


    def click_continue_btn(self):
        '''
        This is a method to click continue button.
        :parameter:
        :return:
        '''
        logging.debug("[InstallHpSmart]:[click_continue_btn]-Click continue_btn... ")

        self.driver.click("continue_btn", is_native_event=True)

    def click_password_text(self):
        '''
        This is a method to click install software button.
        :parameter:
        :return:
        '''
        logging.debug("[InstallHpSmart]:[click_install_software_btn]-Click install_software_btn... ")

        self.driver.click("install_software_btn", is_native_event=True)

    def input_password(self, contents):
        '''
        input password
        :parameter:
        :return:
        '''
        logging.debug("[InstallHpSmart]:[input_password]input_password... ")

        self.driver.send_keys("password_box", contents, press_enter=True)




#-------------------------------Verification Methods------------------------------------------------- 

