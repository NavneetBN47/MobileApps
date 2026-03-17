# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Hide Printer dialog.

@author: ten
@create_date: Aug 23, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class HidePrinterDialog(SmartScreens):

    folder_name = "common"
    flow_name = "hide_printer_dialog"

    def __init__(self, driver):
        super(HidePrinterDialog, self).__init__(driver)

# ----------------------------Operate Elements--------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait agreement screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title_1", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_for_owner_printer(self, timeout=30, raise_e=True):
        '''
        This is a method to wait agreement screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title_2", timeout=timeout, raise_e=raise_e)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title_1")

    def get_value_of_dialog_title_for_owner_printer(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title_2")

    def get_value_of_dialog_content_1(self):
        '''
        This is a method to get value of dialog_content
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_dialog_content]-Get the contents of dialog_content ...  ")

        return self.driver.get_value("dialog_content_1")

    def get_value_of_dialog_content_2(self):
        '''
        This is a method to get value of dialog_content
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_dialog_content]-Get the contents of dialog_content...  ")

        return self.driver.get_value("dialog_content_2")

    def get_value_of_dialog_content_3(self):
        '''
        This is a method to get value of dialog_content
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_dialog_content]-Get the contents of dialog_content...  ")

        return self.driver.get_value("dialog_content_3")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_cancel_btn]-Get the contents of cancel_btn ...  ")

        return self.driver.get_title("cancel_btn")

    def get_value_of_go_to_dashboard_btn(self):
        '''
        This is a method to get value of go_to_dashboard_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_go_to_dashboard_btn]-Get the contents of go_to_dashboard_btn ...  ")

        return self.driver.get_title("go_to_dashboard_btn")

    def get_value_of_hide_printer_btn(self):
        '''
        This is a method to get value of hide_printer_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[get_value_of_hide_printer_btn]-Get the contents of hide_printer_btn ...  ")

        return self.driver.get_title("hide_printer_btn")

    def click_cancel_btn(self):
        '''
        This is a method to click cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[click_cancel_btn]-Click cancel_btn... ")

        self.driver.click("cancel_btn", is_native_event=True)

    def click_go_to_dashboard_btn(self):
        '''
        This is a method to click go_to_dashboard_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[click_go_to_dashboard_btn]-go_to_dashboard_btn... ")

        self.driver.click("go_to_dashboard_btn", is_native_event=True)

    def click_hide_printer_btn(self):
        '''
        This is a method to click hide_printer_btn
        :parameter:
        :return:
        '''
        logging.debug("[HidePrinterDialog]:[click_hide_printer_btn]-Click hide_printer_btn... ")

        self.driver.click("hide_printer_btn", is_native_event=True)

#  ----------------------------Verification Methods--------------------------------------
    def verify_hide_printer_dialog_with_2_button(self, printername):
        '''
        This is a verification method to check UI strings of Hide This Printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of hide_printer_dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hide_printer_dialog')
        assert test_strings['dialog_title_1'] + printername + test_strings['dialog_title_2'] == self.get_value_of_dialog_title()
        assert self.get_value_of_dialog_content_1() == test_strings['dialog_content_1']
        assert self.get_value_of_dialog_content_2() == test_strings['dialog_content_2']
        assert self.get_value_of_cancel_btn() == test_strings['cancel_btn']
        assert self.get_value_of_hide_printer_btn() == test_strings['hide_printer_btn']

    def verify_hide_printer_dialog_with_3_button(self):
        '''
        This is a verification method to check UI strings of Hide This Printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_for_owner_printer()
        logging.debug("Start to check UI strings of hide_printer_dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='hide_printer_dialog')
        assert self.get_value_of_dialog_title_for_owner_printer() == test_strings['dialog_title_3']
        assert self.get_value_of_dialog_content_3() == test_strings['dialog_content_3']
        assert self.get_value_of_dialog_content_2() == test_strings['dialog_content_4']
        assert self.get_value_of_cancel_btn() == test_strings['cancel_btn']
        assert self.get_value_of_go_to_dashboard_btn() == test_strings['go_to_dashboard_btn']
        assert self.get_value_of_hide_printer_btn() == test_strings['hide_printer_btn']
 
    def verify_hide_printer_dialog_disappear(self):
        '''
        This is a verification method to check Hide Printer dialog dismiss after clicking cancel button.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("cancel_btn", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")

        return True

