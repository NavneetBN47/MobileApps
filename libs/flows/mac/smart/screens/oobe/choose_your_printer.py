# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Choose Your Printer screen.

@author: Ivan
@create_date: Sep 07, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ChooseYourPrinter(SmartScreens):

    folder_name = "oobe"
    flow_name = "choose_your_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ChooseYourPrinter, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Choose your printer screen load.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseYourPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_not_listed_btn", timeout=timeout, raise_e=raise_e)

    def select_test_printer(self, printer_name):
        '''
        This is a method to Select your test printer on Choose your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseYourPrinter]:[select_test_printer]-Select your test printer.. ")

        self.driver.click("choose_your_printer_screen_printer_name", format_specifier=[printer_name], is_native_event=True)

    def click_printer_not_listed_btn(self):
        '''
        This is a method to click Click Printer not list button on Choose your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseYourPrinter]:[click_printer_not_listed_btn]-Click Printer not list button.. ")

        self.driver.click("printer_not_listed_btn")

# -------------------------------Verification Methods--------------------------
