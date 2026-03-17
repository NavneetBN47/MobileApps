# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for No printers found screen

@author: Ivan
@create_date: Nov 23, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class NoPrintersFound(SmartScreens):

    folder_name = "common"
    flow_name = "no_printers_found"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(NoPrintersFound, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_printers_found_screen_image", timeout=timeout, raise_e=raise_e)

    def get_value_of_no_printers_found_screen_title(self):
        '''
        This is a method to get the value of No printers found screen title.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[get_value_of_no_printers_found_screen_title]-Get the contents of No printers found screen title...  ")

        return self.driver.get_value("no_printers_found_screen_title")

    def get_value_of_make_sure_the_printer_is_plugged_text(self):
        '''
        This is a method to get the value of Make sure the printer is plugged text on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[get_value_of_make_sure_the_printer_is_plugged_text]-Get the contents of Make sure the printer is plugged text...  ")

        return self.driver.get_value("make_sure_the_printer_is_plugged_text")

    def get_value_of_select_search_again_to_find_text(self):
        '''
        This is a method to get the value of Select search again to find the printer text on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[get_value_of_select_search_again_to_find_text]-Get the contents of Select search again to find the printer text...  ")

        return self.driver.get_value("select_search_again_to_find_text")

    def get_value_of_add_using_ip_address_btn(self):
        '''
        This is a method to get the value of Add Using IP Address button on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[get_value_of_add_using_ip_address_btn]-Get the contents of Add Using IP Address button...  ")

        return self.driver.get_title("add_using_ip_address_btn")

    def get_value_of_search_again_btn(self):
        '''
        This is a method to get the value of Search Again button on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[get_value_of_search_again_btn]-Get the contents of Search Again button...  ")

        return self.driver.get_title("search_again_btn")

    def click_add_using_ip_address_btn(self):
        '''
        This is a method to Click Add Using IP Address button on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[click_add_using_ip_address_btn]-Click  Add Using IP Address button.. ")

        self.driver.click("add_using_ip_address_btn")

    def click_search_again_btn(self):
        '''
        This is a method to Click Search Again button on No printers found screen.
        :parameter:
        :return:
        '''
        logging.debug("[NoPrintersFound]:[click_search_again_btn]-Click Search Again button.. ")

        self.driver.click("search_again_btn")

# -------------------------------Verification Methods--------------------------------------------
    def verify_no_printers_found_screen(self):
        '''
        This is a verification method to check UI strings of No printers found screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of No printers found screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_printers_found')
        assert self.get_value_of_no_printers_found_screen_title() == test_strings['no_printers_found_screen_title']
        assert self.get_value_of_make_sure_the_printer_is_plugged_text() == test_strings['make_sure_the_printer_is_plugged_text']
        assert self.get_value_of_select_search_again_to_find_text() == test_strings['select_search_again_to_find_text']
        assert self.get_value_of_add_using_ip_address_btn() == test_strings['add_using_ip_address_btn']
        assert self.get_value_of_search_again_btn() == test_strings['search_again_btn']
