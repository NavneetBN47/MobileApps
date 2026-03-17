# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connecting printer to WiFi... screen
@author: ten
@create_date: Aug 21, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectToWiFi(SmartScreens):

    folder_name = "oobe"
    flow_name = "connect_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectToWiFi, self).__init__(driver)

# -------------------------------Operate Elements-------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("yes_opt", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_after_select_yes_opt(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[wait_for_screen_load_after_select_yes_opt]-Wait for screen loading... ")

        return self.driver.wait_for_object("select_yes_opt_content_4_3", timeout=timeout, raise_e=raise_e)

    def click_yes_opt(self):
        '''
        This is a method to select Yes opt on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[click_yes_opt]-Select Yes opt.. ")

        self.driver.click("yes_opt")

    def click_no_opt(self):
        '''
        This is a method to select No opt on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[click_no_opt]-Select No opt.. ")

        self.driver.click("no_opt")

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[click_back_btn]-Click Back button.. ")

        self.driver.click("back_btn")

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[click_continue_btn]-Click Continue button.. ")

        self.driver.click("continue_btn")

    def click_here_link(self):
        '''
        This is a method to click Click Here link on Connecting printer to WiFi... screen after select yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[click_click_here_link]-Click click_here_link.. ")

        self.driver.click("select_yes_opt_content_4_3")

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_screen_title]-Get the contents of Connecting printer to WiFi... screen title..  ")

        return self.driver.get_value("screen_title")

    def get_value_of_contents(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_contents]-Get the contents of Connecting printer to WiFi... screen contents..  ")

        return self.driver.get_value("contents")

    def get_value_of_yes_opt(self):
        '''
        This is a method to get the value of Yes opt on Connecting printer to WiFi... screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_yes_opt]-Get the contents of Yes opt..  ")

        return self.driver.get_title("yes_opt")

    def get_value_of_no_opt(self):
        '''
        This is a method to get the value of No opt on Connecting printer to WiFi... screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_no_opt]-Get the contents of No opt..  ")

        return self.driver.get_title("no_opt")

    def get_value_of_select_yes_opt_content_1_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 1-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_1_1]-Get the content of 1-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_1_1")

    def get_value_of_select_yes_opt_content_1_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 1-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_1_2]-Get the content of 1-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_1_2")

    def get_value_of_select_yes_opt_content_2_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_1]-Get the content of 2-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_1")

    def get_value_of_select_yes_opt_content_2_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_2]-Get the content of 2-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_2")

    def get_value_of_select_yes_opt_content_2_3(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-3 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_3]-Get the content of 2-3 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_3")

    def get_value_of_select_yes_opt_content_2_4(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-4 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_4]-Get the content of 2-4 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_4")

    def get_value_of_select_yes_opt_content_2_5(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-5 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_5]-Get the content of 2-5 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_5")

    def get_value_of_select_yes_opt_content_2_6(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-6 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_2_6]-Get the content of 2-6 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_6")

    def get_value_of_select_yes_opt_content_3_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_3_1]-Get the content of 3-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_1")

    def get_value_of_select_yes_opt_content_3_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_3_2]-Get the content of 3-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_2")

    def get_value_of_select_yes_opt_content_3_3(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-3 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_3_3]-Get the content of 3-3 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_3")

    def get_value_of_select_yes_opt_content_4_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 4-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_4_1]-Get the content of 4-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_4_1")

    def get_value_of_select_yes_opt_content_4_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 4-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_4_2]-Get the content of 4-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_4_2")

    def get_value_of_select_yes_opt_content_4_3(self):
        '''
        This is a method to get the value of Click here link on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_select_yes_opt_content_4_3]-Get the content of Click here link..  ")

        return self.driver.get_value("select_yes_opt_content_4_3")

    def get_value_of_back_btn(self):
        '''
        This is a method to get the value of Back button on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_back_btn]-Get the content of Back button..  ")

        return self.driver.get_title("back_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToWiFi]:[get_value_of_continue_btn]-Get the content of Continue button..  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods---------------------------------------------
    def verify_connect_to_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Connect to WiFi screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect to WiFi screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_wifi_screen')
        assert self.get_value_of_screen_title() == test_strings['screen_title']
        assert self.get_value_of_contents() == test_strings['we_like_to_make_sure_content']
        assert self.get_value_of_yes_opt() == test_strings['yes_opt']
        assert self.get_value_of_no_opt() == test_strings['no_opt']
        assert self.get_value_of_back_btn() == test_strings['back_btn']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_to_wifi_screen_select_yes_opt(self):
        '''
        This is a verification method to check UI strings of Connect to WiFi screen after select Yes opt.
        :parameter:
        :return:
        '''
        self.click_yes_opt()
        self.wait_for_screen_load_after_select_yes_opt()
        logging.debug("Start to check UI strings of Connect to WiFi screen after select Yes opt")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_wifi_screen')
        assert self.get_value_of_screen_title() == test_strings['screen_title']
        assert self.get_value_of_contents() == test_strings['use_the_touchscreen_display_content']
        assert self.get_value_of_select_yes_opt_content_1_1() == test_strings['select_yes_opt_content_1_1']
        assert self.get_value_of_select_yes_opt_content_1_2() == test_strings['select_yes_opt_content_1_2']
        assert self.get_value_of_select_yes_opt_content_2_1() == test_strings['select_yes_opt_content_2_1']
        assert self.get_value_of_select_yes_opt_content_2_2() == test_strings['select_yes_opt_content_2_2']
#         assert self.get_value_of_select_yes_opt_content_2_3() == test_strings['']
        assert self.get_value_of_select_yes_opt_content_2_4() == test_strings['select_yes_opt_content_2_4']
#         assert self.get_value_of_select_yes_opt_content_2_5() == test_strings['']
        assert self.get_value_of_select_yes_opt_content_2_6() == test_strings['select_yes_opt_content_2_6']
        assert self.get_value_of_select_yes_opt_content_3_1() == test_strings['select_yes_opt_content_3_1']
        assert self.get_value_of_select_yes_opt_content_3_2() == test_strings['select_yes_opt_content_3_2']
        assert self.get_value_of_select_yes_opt_content_3_3() == test_strings['select_yes_opt_content_3_3']
        assert self.get_value_of_select_yes_opt_content_4_1() == test_strings['select_yes_opt_content_4_1']
        assert self.get_value_of_select_yes_opt_content_4_2() == test_strings['select_yes_opt_content_4_2']
        assert self.get_value_of_select_yes_opt_content_4_3() == test_strings['select_yes_opt_content_4_3']
        assert self.get_value_of_back_btn() == test_strings['back_btn']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']
