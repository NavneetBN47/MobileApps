# encoding: utf-8
'''
It defines the operations of element and verification methods on OWS Value Prop screen.

@author: Ivan
@create_date: Aug 05, 2020
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class OwsValuePropScreen(SmartScreens):

    folder_name = "common"
    flow_name = "ows_value_prop_screen"

    def __init__(self, driver):
        super(OwsValuePropScreen, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait OWS Value Prop screen load.
        '''
        logging.debug("[OwsValuePropScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ows_value_prop_screen_set_up_a_new_printer_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_set_up_a_new_printer_btn(self):
        '''
        This is a method to get the value of Set up a new printer button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[get_value_of_set_up_a_new_printer_btn]-Get the value of Set up a new printer button...  ")

        return self.driver.get_title("ows_value_prop_screen_set_up_a_new_printer_btn")

    def get_value_of_set_up_a_new_hp_printer_text(self):
        '''
        This is a method to get the value of Set up a new hp printer text on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[get_value_of_set_up_a_new_hp_printer_text]-Get the value of Set up a new hp printer text...  ")

        return self.driver.get_value("set_up_a_new_hp_printer_text")

    def get_value_of_sign_in_btn(self):
        '''
        This is a method to get the value of Sign in button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[get_value_of_sign_in_btn]-Get the value of Sign In button...  ")

        return self.driver.get_title("ows_value_prop_screen_sign_in_btn")

    def get_value_of_create_an_hp_account_text(self):
        '''
        This is a method to get the value of Create an hp account text on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[get_value_of_create_an_hp_account_text]-Get the value of Create an hp account text...  ")

        return self.driver.get_value("create_an_hp_account_text")

    def get_value_of_skip_for_now_btn(self):
        '''
        This is a method to get the value of Skip for now button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[get_value_of_skip_for_now_btn]-Get the value of Skip for now button...  ")

        return self.driver.get_title("ows_value_prop_screen_skip_for_now_btn")

    def click_set_up_a_new_printer_btn(self):
        '''
        This is a method to click Set up a new printer button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[click_set_up_a_new_printer_btn]-Click Set up a new printer button... ")

        self.driver.click("ows_value_prop_screen_set_up_a_new_printer_btn", is_native_event=True)

    def click_sign_in_btn(self):
        '''
        This is a method to click Sign In button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[click_sign_in_btn]-Click Sign In button... ")

#        self.driver.click("ows_value_prop_screen_sign_in_btn", is_native_event=True)
        self.driver.click("ows_value_prop_screen_sign_in_btn")

    def click_skip_for_now_btn(self):
        '''
        This is a method to click Skip for now button on OWS Value Prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[OwsValuePropScreen]:[click_skip_for_now_btn]-Click Skip for now button... ")

        self.driver.click("ows_value_prop_screen_skip_for_now_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
    def verify_ows_value_prop_screen(self):
        '''
        This is a verification method to check UI strings of OWS Value Prop screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        sleep(2)
        logging.debug("Start to check UI strings of OWS Value Prop screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_value_prop_screen')
        assert self.get_value_of_set_up_a_new_printer_btn() == test_strings['set_up_a_new_printer_btn']
        assert self.get_value_of_set_up_a_new_hp_printer_text() == test_strings['set_up_a_new_hp_printer_text']
        assert self.get_value_of_sign_in_btn() == test_strings['sign_in_btn']
        assert self.get_value_of_create_an_hp_account_text() == test_strings['create_an_hp_account_text']
        assert self.get_value_of_skip_for_now_btn() == test_strings['skip_for_now_btn']
