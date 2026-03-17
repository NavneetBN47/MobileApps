# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect printer to WiFi Help Dialog.

@author: ten
@create_date: July 25, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectPrinterHelpDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_printer_help_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectPrinterHelpDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------

    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("to_print_from_content", timeout=timeout, raise_e=raise_e)

    def click_help_dialog_continue_btn(self):
        '''
        This is a method to click Continue Button on Need help connecting printer to Wi-Fi? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[click_help_dialog_continue_btn]-Click Continue button... ")

        self.driver.click("help_dialog_continue_btn", is_native_event=True)

    def click_help_dialog_change_connection_btn(self):
        '''
        This is a method to click Change connection button on Need help connecting printer to Wi-Fi? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[click_help_dialog_change_connection_btn]-Click Change connection button... ")

        self.driver.click("help_dialog_change_connection_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of Need help connecting printer to Wi-Fi? dialog title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_dialog_title]-Get the value of Help dialog_title...  ")

        return self.driver.get_value("help_dialog_title")

    def get_value_of_to_print_from_content(self):
        '''
        This is a method to get value of To print from text on Need help connecting printer to Wi-Fi? Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_to_print_from_content]-Get the value of To print from text...  ")

        return self.driver.get_value("to_print_from_content")

    def get_value_of_change_connection_btn(self):
        '''
        This is a method to get value of Change connection button on Need help connecting printer to Wi-Fi? Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_change_connection_btn]-Get the value of Help dialog Change connection button...  ")

        return self.driver.get_title("help_dialog_change_connection_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Need help connecting printer to Wi-Fi? Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_continue_btn]-Get the value of Help dialog Continue button...  ")

        return self.driver.get_title("help_dialog_continue_btn")

    # -------------------------------Verification Methods---------------
    def verify_connect_printer_to_wifi_help_dialog(self):
        '''
        This is a verification method to check UI strings of Need help connecting printer to Wi-Fi? Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Need help connecting printer to Wi-Fi? Dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='need_help_connecting_printer_to_wifi_dialog')
        assert self.get_value_of_dialog_title() == test_strings['help_dialog_title']
#         assert self.get_value_of_to_print_from_content() == test_strings['to_print_from_content']
        assert self.get_value_of_change_connection_btn() == test_strings['change_connection_btn']
        assert self.get_value_of_continue_btn() == test_strings['help_dialog_continue_btn']
