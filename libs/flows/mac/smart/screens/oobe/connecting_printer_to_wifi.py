# encoding: utf-8
'''
ConnectingPrintertoWiFi screen

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectingPrintertoWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "connecting_printer_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectingPrintertoWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_image", timeout=timeout, raise_e=raise_e)

    def wait_for_error_dialog_load(self, timeout=30, raise_e=True):
        '''
       This is a method to wait for Could not connect to the Wi-Fi network dialog or Unable to set up your printer at this time dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[wait_for_error_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("error_dialog_content", timeout=timeout, raise_e=raise_e)

    def get_value_of_connecting_printer_to_wifi_title(self):
        '''
        This is a method to get the value of Connecting printer to WiFi title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_connecting_printer_to_wifi_title]-Get the contents of connecting_printer_to_wifi_title...  ")

        return self.driver.get_value("connecting_printer_to_wifi_title")

    def get_value_of_you_must_stay_text(self):
        '''
        This is a method to get the value of you must stay text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_you_must_stay_text]-Get the contents of you must stay text...  ")

        return self.driver.get_value("you_must_stay_text")

    def get_value_of_printer_name(self):
        '''
        This is a method to get the value of Printer name on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_printer_name]-Get the contents of Printer name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_router_name(self):
        '''
        This is a method to get the value of Router name on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_router_name]-Get the contents of Router name...  ")

        return self.driver.get_value("router_name")

    def get_value_of_finding_the_printer_text(self):
        '''
        This is a method to get the value of Finding the printer text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_finding_the_printer_text]-Get the contents of Finding the printer text...  ")

        return self.driver.get_value("finding_the_printer_text")

    def get_value_of_configure_the_printer_text(self):
        '''
        This is a method to get the value of Configure the printer text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_configure_the_printer_text]-Get the contents of Configure the printer text...  ")

        return self.driver.get_value("configure_the_printer_text")

    def get_value_of_join_the_network_text(self):
        '''
        This is a method to get the value of Join the network text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_join_the_network_text]-Get the contents of Join the network text...  ")

        return self.driver.get_value("join_the_network_text")

    def get_value_of_finish_connections_text(self):
        '''
        This is a method to get the value of Finish connections text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_finish_connections_text]-Get the contents of Finish connections text...  ")

        return self.driver.get_value("finish_connections_text")

    def get_value_of_error_dialog_title(self):
        '''
        This is a method to get the value of Could not connect to the Wi-Fi network dialog or Unable to set up your printer at this time dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_error_dialog_title]-Get the value of error dialog title...  ")

        return self.driver.get_value("error_dialog_title")

    def get_value_of_error_dialog_content(self):
        '''
        This is a method to get the value of Could not connect to the Wi-Fi network dialog or Unable to set up your printer at this time dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_could_not_connect_to_the_wifi_network_dialog_content]-Get the value of Could not connect to the Wi-Fi network dialog content...  ")

        return self.driver.get_value("error_dialog_content")

    def get_value_of_error_dialog_footer_btn(self):
        '''
        This is a method to get the value of Try Again button on Could not connect to the Wi-Fi network dialog or Continue button on Unable to set up your printer at this time dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_could_not_connect_to_the_wifi_network_dialog_try_again_btn]-Get the value of Try Again button...  ")

        return self.driver.get_title("error_dialog_footer_btn")

    def click_error_dialog_footer_btn(self):
        '''
        This is a method to click Try Again button on Could not connect to the Wi-Fi network dialog or Continue button on Unable to set up your printer at this time dialog
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[click_could_not_connect_to_the_wifi_network_dialog_try_again_btn]-Click Try Again button or Continue button... ")

        self.driver.click("error_dialog_footer_btn", is_native_event=True)

# -------------------------------Verification Methods-------------------------------------------------
    def verify_connecting_printer_to_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Connecting printer to WiFi screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connecting printer to WiFi screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connecting_printer_to_wifi_screen')
        assert self.get_value_of_connecting_printer_to_wifi_title() == test_strings['connecting_printer_to_wifi_title']
        assert self.get_value_of_you_must_stay_text() == test_strings['you_must_stay_text']
#         assert self.get_value_of_printer_name() == 
#         assert self.get_value_of_router_name() == 
#         assert self.get_value_of_finding_the_printer_text() == test_strings['finding_the_printer_text']
#         assert self.get_value_of_configure_the_printer_text() == test_strings['configure_the_printer_text']
#         assert self.get_value_of_join_the_network_text() == test_strings['join_the_network_text']
#         assert self.get_value_of_finish_connections_text() == test_strings['finish_connections_text']

    def verify_could_not_connect_to_the_wifi_network_dialog(self):
        '''
        This is a verification method to check UI strings of Could not connect to the Wi-Fi network dialog
        :parameter:
        :return:
        '''
        self.wait_for_error_dialog_load(600)
        logging.debug("Start to verify UI string of Could not connect to the Wi-Fi network dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='could_not_connect_to_the_wifi_network_dialog')
        assert self.get_value_of_error_dialog_title() == test_strings['error_dialog_title']
        assert self.get_value_of_error_dialog_content() == test_strings['error_dialog_content']
        assert self.get_value_of_error_dialog_footer_btn() == test_strings['error_dialog_footer_btn']

    def verify_unable_to_set_up_your_printer_at_this_time_dialog(self):
        '''
        This is a verification method to check UI strings of Unable to set up your printer at this time dialog
        :parameter:
        :return:
        '''
        self.wait_for_error_dialog_load(60)
        logging.debug("Start to verify UI string of Unable to set up your printer at this time dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='unable_to_set_up_your_printer_at_this_time_dialog')
        assert self.get_value_of_error_dialog_title() == test_strings['error_dialog_title']
        assert self.get_value_of_error_dialog_content() == test_strings['error_dialog_content']
        assert self.get_value_of_error_dialog_footer_btn() == test_strings['error_dialog_footer_btn']

