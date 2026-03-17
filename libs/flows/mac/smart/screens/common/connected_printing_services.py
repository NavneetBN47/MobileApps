# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connected Printing Services screen.

@author:Ivan
@create_date: Aug 27, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectedPrintingServices(SmartScreens):
    folder_name = "common"
    flow_name = "connected_printing_services"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectedPrintingServices, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connected Printing Services screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connected_printing_services_continue_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_connected_printing_services_title(self):
        '''
        This is a method to get value of Connected Printing Services Title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[get_value_of_connected_printing_services_title]-Get value of Connected Printing Services Title...  ")

        return self.driver.get_title("connected_printing_services_title")

    def get_value_of_connected_printing_services_content(self):
        '''
        This is a method to get value of Connected Printing Services Contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[get_value_of_connected_printing_services_content]-Get value of Connected Printing Services Contents...  ")

        return self.driver.get_value("connected_printing_services_content")

    def get_value_of_connected_printing_services_learn_more_link(self):
        '''
        This is a method to get value of Learn More link on Connected Printing Services screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[get_value_of_connected_printing_services_learn_more_link]-Get value of Learn More link...  ")

        return self.driver.get_title("connected_printing_services_learn_more_link")

    def get_value_of_connected_printing_services_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connected Printing Services Screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[get_value_of_connected_printing_services_continue_btn]-Get value of Continue button...  ")

        return self.driver.get_title("connected_printing_services_continue_btn")

    def click_connected_printing_sevices_learn_more_link(self):
        '''
        This is a method to click Learn More link on Connected Printing Services screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[click_connected_printing_sevices_learn_more_link]-Click Learn More link.. ")

        self.driver.click("connected_printing_services_learn_more_link")

    def click_connected_printing_sevices_continue_btn(self):
        '''
        This is a method to click Continue button on Connected Printing Services screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[click_connected_printing_sevices_continue_btn]-Click Continue button.. ")

        self.driver.click("connected_printing_services_continue_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_connected_printing_services_screen(self):
        '''
        This is a verification method to check UI strings of Connected Printing Services screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
#         logging.debug("Start to verify UI string of Connected Printing Services screen")
#         test_strings = smart_utility.get_local_strings_from_table(screen_name='connected_priting_services_screen')
#         assert self.get_value_of_connected_printing_services_title() == test_strings['connected_printing_services_title']
#         assert self.get_value_of_connected_printing_services_content() == test_strings['connected_printing_services_content']
#         assert self.get_value_of_connected_printing_services_learn_more_link() == test_strings['connected_printing_services_learn_more_link']
#         assert self.get_value_of_connected_printing_services_continue_btn() == test_strings['connected_printing_services_continue_btn']
