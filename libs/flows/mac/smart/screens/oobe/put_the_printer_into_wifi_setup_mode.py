# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Put the printer into setup mode screen

@author: Ivan
@create_date: Sep 06, 2021
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class PutThePrinterIntoWifiSetupMode(SmartScreens):
    folder_name = "oobe"
    flow_name = "put_the_printer_into_wifi_setup_mode"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PutThePrinterIntoWifiSetupMode, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("exit_setup_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_put_the_printer_into_wifi_setup_mode_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[wait_for_put_the_printer_into_wifi_setup_mode_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("change_printer_btn", timeout=timeout, raise_e=raise_e)

    def click_exit_setup_btn(self):
        '''
        This is a method to click Exit Setup button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_exit_setup_btn]-Click Exit Setup button.. ")

        self.driver.click("exit_setup_btn", is_native_event=True)

    def click_hp_support_btn(self):
        '''
        This is a method to click HP Support button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_hp_support_btn]-Click HP Support button.. ")

        self.driver.click("hp_support_btn", is_native_event=True)

    def click_find_my_printer_btn(self):
        '''
        This is a method to click Find my printer button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_find_my_printer_btn]-Click Find my printer button.. ")

        self.driver.click("find_my_printer_btn", is_native_event=True)

    def click_one_btn(self):
        '''
        This is a method to click One button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_one_btn]-Click One button.. ")

        self.driver.click("one_btn", is_native_event=True)

    def click_two_btn(self):
        '''
        This is a method to click Two button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_two_btn]-Click Two button.. ")

        self.driver.click("two_btn", is_native_event=True)

    def click_three_btn(self):
        '''
        This is a method to click Three button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_three_btn]-Click Three button.. ")

        self.driver.click("three_btn", is_native_event=True)

    def click_four_btn(self):
        '''
        This is a method to click Four button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_four_btn]-Click Four button.. ")

        self.driver.click("four_btn", is_native_event=True)

    def click_change_printer_btn(self):
        '''
        This is a method to click Change Printer button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_change_printer_btn]-Click Change Printer button.. ")

        self.driver.click("change_printer_btn", is_native_event=True)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[click_continue_btn]-Click Continue button.. ")
        self.click_two_btn()
        sleep(2)
        if not self.driver.is_enable("continue_btn"):
            self.click_four_btn()
            sleep(2)
        self.driver.click("continue_btn", is_native_event=True)

    def get_value_of_put_the_printer_into_wifi_setup_mode_screen_title(self):
        '''
        This is a method to get value of Put the printer into setup mode screen title.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_put_the_printer_into_wifi_setup_mode_screen_title]-Get the contents of Put the printer into setup mode screen title...  ")

        return self.driver.get_title("put_the_printer_into_wifi_setup_mode_screen_title")

    def get_value_of_if_the_software_is_unable_text(self):
        '''
        This is a method to get value of If the software is unable text on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_if_the_software_is_unable_text]-Get the contents of If the software is unable text...  ")

        return self.driver.get_value("if_the_software_is_unable_text")

    def get_value_of_for_same_models_text(self):
        '''
        This is a method to get value of For same models text on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_for_same_models_text]-Get the contents of For same models text...  ")

        return self.driver.get_value("for_same_models_text")

    def get_value_of_after_resetting_setup_mode_text(self):
        '''
        This is a method to get value of After resetting setup mode text on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_after_resetting_setup_mode_text]-Get the contents of After resetting setup mode text...  ")

        return self.driver.get_value("after_resetting_setup_mode_text")

    def get_value_of_find_my_printer_text(self):
        '''
        This is a method to get value of Find my printer text on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_find_my_printer_text]-Get the contents of Find my printer text...  ")

        return self.driver.get_value("find_my_printer_text")

    def get_value_of_exit_setup_btn(self):
        '''
        This is a method to get value of Exit Setup button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_exit_setup_btn]-Get the contents of Exit Setup button...  ")

        return self.driver.get_title("exit_setup_btn")

    def get_value_of_hp_support_btn(self):
        '''
        This is a method to get value of HP Support button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_hp_support_btn]-Get the contents of HP Support button...  ")

        return self.driver.get_title("hp_support_btn")

    def get_value_of_find_my_printer_btn(self):
        '''
        This is a method to get value of Find my printer button on Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        logging.debug("[PutThePrinterIntoWifiSetupMode]:[get_value_of_find_my_printer_btn]-Get the contents of Find my printer button...  ")

        return self.driver.get_title("find_my_printer_btn")

# -------------------------------Verification Methods--------------------------
    def verify_put_the_printer_into_wifi_setup_mode_screen(self):
        '''
        This is a verification method to check the string UI of Put the printer into setup mode screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check the string UI of Put the printer into setup mode screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='put_the_printer_into_wifi_setup_mode_screen')
        assert self.get_value_of_put_the_printer_into_wifi_setup_mode_screen_title() == test_strings['put_the_printer_into_wifi_setup_mode_screen_title']
        assert self.get_value_of_if_the_software_is_unable_text() == test_strings['if_the_software_is_unable_text']
        assert self.get_value_of_for_same_models_text() == test_strings['for_same_models_text']
        assert self.get_value_of_after_resetting_setup_mode_text() == test_strings['after_resetting_setup_mode_text']
        assert self.get_value_of_find_my_printer_text() == test_strings['find_my_printer_text']
        assert self.get_value_of_exit_setup_btn() == test_strings['exit_setup_btn']
        assert self.get_value_of_hp_support_btn() == test_strings['hp_support_btn']
        assert self.get_value_of_find_my_printer_btn() == test_strings['find_my_printer_text']
