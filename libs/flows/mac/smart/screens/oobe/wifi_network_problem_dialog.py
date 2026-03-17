# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on WiFi network problem dialog

@author: Ivan
@create_date: Aug 28, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class WiFiNetworkProblemDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "wifi_network_problem_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WiFiNetworkProblemDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait welcome screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_are_connected_to_content", timeout=timeout, raise_e=raise_e)

    def click_network_btn(self):
        '''
        This is a method to click network button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_network_btn]-Click network_btn.. ")

        self.driver.click("network_btn")

    def click_change_connection_btn(self):
        '''
        This is a method to click change connection button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_change_connection_btn]-Click change_connection_btn.. ")

        self.driver.click("change_connection_btn")

    def click_continue_btn(self):
        '''
        This is a method to click continue button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_title(self):
        '''
        This is a method to get the value of dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_title]-Get the value of title...  ")

        return self.driver.get_value("wifi_network_problem_title")

    def get_value_of_you_are_connected_to_content(self):
        '''
        This is a method to get the value of you_are_connected_to_content.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_you_are_connected_to_content]-Get the contents of you_are_connected_to_content...  ")

        return self.driver.get_value("you_are_connected_to_content")

    def get_value_of_try_one_of_the_following_content(self):
        '''
        This is a method to get the value of try_one_of_the_following_content.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_try_one_of_the_following_content]-Get the contents of you_are_connected_to_content...  ")

        return self.driver.get_value("try_one_of_the_following_content")

    def get_value_of_wifi_network_problem_content_1_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_1.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_1]-Get the contents of wifi_network_problem_content_1_1...  ")

        return self.driver.get_value("wifi_network_problem_content_1_1")

    def get_value_of_wifi_network_problem_content_1_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_2]-Get the contents of wifi_network_problem_content_1_2...  ")

        return self.driver.get_value("wifi_network_problem_content_1_2")

    def get_value_of_wifi_network_problem_content_1_3(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_3
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_3]-Get the contents of wifi_network_problem_content_1_3...  ")

        return self.driver.get_value("wifi_network_problem_content_1_3")

    def get_value_of_wifi_network_problem_content_1_4(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_4
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_4]-Get the contents of wifi_network_problem_content_1_4...  ")

        return self.driver.get_value("wifi_network_problem_content_1_4")

    def get_value_of_wifi_network_problem_content_1_5(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_5
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_5]-Get the contents of wifi_network_problem_content_1_5...  ")

        return self.driver.get_value("wifi_network_problem_content_1_5")

    def get_value_of_network_btn(self):
        '''
        This is a method to get the value of network_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_network_btn]-Get the contents of network_btn...  ")

        return self.driver.get_title("network_btn")

    def get_value_of_or_content(self):
        '''
        This is a method to get the value of or_content
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_or_content]-Get the contents of or_content...  ")

        return self.driver.get_value("or_content")

    def get_value_of_wifi_network_problem_content_2_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_1
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_1]-Get the contents of wifi_network_problem_content_2_1...  ")

        return self.driver.get_value("wifi_network_problem_content_2_1")

    def get_value_of_wifi_network_problem_content_2_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_2]-Get the contents of wifi_network_problem_content_2_2...  ")

        return self.driver.get_value("wifi_network_problem_content_2_2")

    def get_value_of_wifi_network_problem_content_2_3(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_3
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_3]-Get the contents of wifi_network_problem_content_2_3...  ")

        return self.driver.get_value("wifi_network_problem_content_2_3")

    def get_value_of_change_connection_btn(self):
        '''
        This is a method to get the value of change_connection_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_change_connection_btn]-Get the contents of change_connection_btn...  ")

        return self.driver.get_title("change_connection_btn")

    def get_value_of_wifi_network_problem_content_3_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_3_1
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_3_1]-Get the contents of wifi_network_problem_content_3_1...  ")

        return self.driver.get_value("wifi_network_problem_content_3_1")

    def get_value_of_wifi_network_problem_content_3_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_3_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_3_2]-Get the contents of wifi_network_problem_content_3_2...  ")

        return self.driver.get_value("wifi_network_problem_content_3_2")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of continue_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_continue_btn]-Get the contents of continue_btn...  ")

        return self.driver.get_title("continue_btn")

#  -------------------------------Verification Methods------------------------
    def verify_wifi_network_problem_dialog(self):
        '''
        This is a verification method to check UI strings of Wi-Fi Network Problem Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to verify UI string of Wi-Fi Network Problem Dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='wifi_network_problem_dialog')
        assert self.get_value_of_title() == test_strings['wifi_network_problem_title']
        assert self.get_value_of_you_are_connected_to_content() == test_strings['you_are_connected_to_content']
        assert self.get_value_of_try_one_of_the_following_content() == test_strings['try_one_of_the_following_content']
        assert self.get_value_of_wifi_network_problem_content_1_1() == test_strings['wifi_network_problem_content_1_1']
        assert self.get_value_of_wifi_network_problem_content_1_2() == test_strings['wifi_network_problem_content_1_2']
        assert self.get_value_of_wifi_network_problem_content_1_3() == test_strings['wifi_network_problem_content_1_3']
        assert self.get_value_of_wifi_network_problem_content_1_4() == test_strings['wifi_network_problem_content_1_4']
        assert self.get_value_of_wifi_network_problem_content_1_5() == test_strings['wifi_network_problem_content_1_5']
        assert self.get_value_of_network_btn() == test_strings['network_btn']
        assert self.get_value_of_or_content() == test_strings['or_content']
        assert self.get_value_of_wifi_network_problem_content_2_1() == test_strings['wifi_network_problem_content_2_1']
        assert self.get_value_of_wifi_network_problem_content_2_2() == test_strings['wifi_network_problem_content_2_2']
        assert self.get_value_of_wifi_network_problem_content_2_3() == test_strings['wifi_network_problem_content_2_3']
        assert self.get_value_of_change_connection_btn() == test_strings['change_connection_btn']
        assert self.get_value_of_wifi_network_problem_content_3_1() == test_strings['wifi_network_problem_content_3_1']
        assert self.get_value_of_wifi_network_problem_content_3_2() == test_strings['wifi_network_problem_content_3_2']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']
