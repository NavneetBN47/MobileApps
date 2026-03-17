# encoding: utf-8
'''
FogetPrinterDialog

@author: ten
@create_date: Sep 23, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_information import PrinterInformation


class FogetPrinterDialog(SmartScreens):

    folder_name = "common"
    flow_name = "forget_printer_dialog"

    def __init__(self, driver):
        super(FogetPrinterDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait agreement screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_contents", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self):
        '''
        This is a method to click cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[click_cancel_btn]-Click cancel_btn... ")

        self.driver.click("cancel_btn", is_native_event=True)

    def click_forget_printer_btn(self):
        '''
        This is a method to click forget_printer_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[click_forget_printer_btn]-Click forget_printer_btn... ")

        self.driver.click("forget_printer_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("dialog_contents")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_cancel_btn]-Get the contents of cancel_btn ...  ")

        return self.driver.get_title("cancel_btn")

    def get_value_of_forget_printer_btn(self):
        '''
        This is a method to get value of forget_printer_btn.
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_forget_printer_btn]-Get the contents of forget_printer_btn ...  ")

        return self.driver.get_title("forget_printer_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_forget_this_printer_dialog(self):
        '''
        This is a verification method to check UI strings of Forget This Printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()

        printer_information_screen = PrinterInformation(self.driver)
        logging.debug("Start to check UI strings of Forget Printer dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='forget_printer_dialog')
#         assert self.get_value_of_dialog_title() == test_strings['forget_printer_dialog_title'] + str(printer_information_screen.get_the_value_of_name()) + "?"
        assert self.get_value_of_dialog_contents() == test_strings['forget_printer_dialog_body']
        assert self.get_value_of_cancel_btn() == test_strings['forget_printer_dialog_cancel_btn']
        assert self.get_value_of_forget_printer_btn() == test_strings['forget_printer_dialog_forget_printer_btn']

    def verify_forget_printer_dialog_disappear(self):
        '''
        This is a verification method to check Forget Printer dialog dismiss after clicking cancel button.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("dialog_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")

        return True
