# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect to the Internet dialog.

@author: Ivan
@create_date: Aug 28, 2020
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectToTheInternetDialog(SmartScreens):

    folder_name = "common"
    flow_name = "connect_to_the_internet_dialog"

    def __init__(self, driver):
        super(ConnectToTheInternetDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connect to the Internet dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_to_the_internet_content", timeout=timeout, raise_e=raise_e)

    def wait_for_spinner_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Spinner screen load after clicking Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[wait_for_spinner_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("spinner_text", timeout=timeout, raise_e=raise_e)

    def get_value_of_spinner_text(self):
        '''
        This is a method to get value of Spinner text on Checking Internet connection screen/Establishing connection screen/Connecting screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_spinner_text]-Get the value of Spinner text...  ")

        return self.driver.get_value("spinner_text")

    def get_value_of_connect_to_the_internet_title(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("connect_to_the_internet_title")

    def get_value_of_connect_to_the_internet_content(self):
        '''
        This is a method to get value of Content on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_content_1]-Get the value of Content - 1...  ")

        return self.driver.get_value("connect_to_the_internet_content")

    def get_value_of_connect_to_the_internet_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("connect_to_the_internet_continue_btn")

    def get_value_of_connect_to_the_internet_back_btn(self):
        '''
        This is a method to get value of Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_back_btn]-Get the value of Back button...  ")

        return self.driver.get_title("back_btn")

    def click_connect_to_the_internet_continue_btn(self):
        '''
        This is a method to click Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[click_connect_to_the_internet_continue_btn]-Click Continue button... ")

        self.driver.click("connect_to_the_internet_continue_btn")

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[click_back_btn]-Click Back button... ")

        self.driver.click("back_btn")

    def wait_for_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connect to the Internet dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[wait_for_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_dialog_load_before_main_ui(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connect to the Internet dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[wait_for_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title_before_main_ui", timeout=timeout, raise_e=raise_e)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content_1(self):
        '''
        This is a method to get value of Connect to text/An Internet connection text on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_content_connect_to_text]-Get the value of Connect to text...  ")

        return self.driver.get_value("dialog_content_1")

    def get_value_of_dialog_content_2(self):
        '''
        This is a method to get value of After connecting text on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_content_after_connecting_text]-Get the value of After connecting text...  ")

        return self.driver.get_value("dialog_content_2")

    def get_value_of_dialog_content_3(self):
        '''
        This is a method to get value of Continue text on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_content_continue_text]-Get the value of Continue text...  ")

        return self.driver.get_value("dialog_content_3")

    def get_value_of_dialog_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("dialog_continue_btn")
    
    def get_value_of_dialog_title_before_main_ui(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("dialog_title_before_main_ui")
    
    def get_value_of_dialog_content_1_before_main_ui(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("dialog_content_1_before_main_ui")
    
    def get_value_of_dialog_content_2_before_main_ui(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("dialog_content_2_before_main_ui")
    
    def get_value_of_dialog_content_3_before_main_ui(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("dialog_content_3_before_main_ui")

    def get_value_of_dialog_continue_btn_before_main_ui(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_dialog_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_title("dialog_continue_btn_before_main_ui")

    def get_value_of_back_btn(self):
        '''
        This is a method to get value of Continue button on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_back_btn]-Get the value of Back button...  ")

        return self.driver.get_title("back_btn")

    def click_dialog_continue_btn(self):
        '''
        This is a method to click Continue button on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[click_dialog_continue_btn]-Click Continue button... ")

        self.driver.click("dialog_continue_btn")

    def click_dialog_continue_btn_before_main_ui(self):
        '''
        This is a method to click Continue button on Connect to the Internet dialog before main page.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[click_dialog_continue_btn]-Click Continue button... ")

        self.driver.click("dialog_continue_btn_before_main_ui")

# -------------------------------Verification Methods-------------------------------
    def verify_connect_to_the_internet_dialog_before_main_ui(self):
        '''
        This is a verification method to check UI strings of Connect to the Internet dialog before main ui.
        :parameter:
        :return:
        '''
        self.wait_for_dialog_load_before_main_ui(60)
        logging.debug("Start to check UI strings of Connect to the Internet dialog before main ui")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_dialog_title_before_main_ui() == test_strings['connect_to_the_internet_title']
        assert self.get_value_of_dialog_content_1_before_main_ui() == test_strings['connect_to_the_internet_content_1_1']
        assert self.get_value_of_dialog_content_2_before_main_ui() == test_strings['connect_to_the_internet_content_2']
        assert self.get_value_of_dialog_content_3_before_main_ui() == test_strings['connect_to_the_internet_content_3']
        assert self.get_value_of_dialog_continue_btn_before_main_ui() == test_strings['connect_to_the_internet_content_3']

    def verify_connect_to_the_internet_dialog_on_main_ui(self):
        '''
        This is a verification method to check UI strings of Connect to the Internet dialog on main ui.
        :parameter:
        :return:
        '''
        self.wait_for_dialog_load(60)
        logging.debug("Start to check UI strings of Connect to the Internet dialog on main ui")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_dialog_title() == test_strings['connect_to_the_internet_title']
        assert self.get_value_of_dialog_content_1() == test_strings['connect_to_the_internet_content_1_1']
        assert self.get_value_of_dialog_content_2() == test_strings['connect_to_the_internet_content_2']
        assert self.get_value_of_dialog_content_3() == test_strings['connect_to_the_internet_content_3']
        assert self.get_value_of_dialog_continue_btn() == test_strings['connect_to_the_internet_content_3']

    def verify_connect_to_the_internet_dialog(self):
        '''
        This is a verification method to check UI strings of Connect to the Internet dialog after main ui.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect to the Internet dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_connect_to_the_internet_title() == test_strings['connect_to_the_internet_title']
        assert self.get_value_of_connect_to_the_internet_content() == test_strings['connect_to_the_internet_content_4']
        assert self.get_value_of_connect_to_the_internet_continue_btn() == test_strings['connect_to_the_internet_content_3']
        assert self.get_value_of_back_btn() == test_strings['back_btn']

    def verify_connect_to_the_internet_dialog_oobe(self):
        '''
        This is a verification method to check UI strings of Connect to the Internet dialog after main ui.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect to the Internet dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_connect_to_the_internet_title() == test_strings['connect_to_the_internet_title']
        assert self.get_value_of_connect_to_the_internet_content() == test_strings['connect_to_the_internet_content']
        assert self.get_value_of_connect_to_the_internet_continue_btn() == test_strings['connect_to_the_internet_content_3']

    def verify_checking_internet_connection_screen(self):
        '''
        This is a verification method to check UI strings of Checking Internet connection screen.
        :parameter:
        :return:
        '''
        self.wait_for_spinner_screen_load()
        logging.debug("Start to check UI strings of Checking Internet connection screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_spinner_text() in test_strings['checking_internet_connection']

    def verify_establishing_connection_screen(self):
        '''
        This is a verification method to check UI strings of Establishing connection screen.
        :parameter:
        :return:
        '''
        self.wait_for_spinner_screen_load()
        logging.debug("Start to check UI strings of Establishing connection screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_spinner_text() == test_strings['establishing_connection']

    def verify_connecting_screen(self):
        '''
        This is a verification method to check UI strings of Connecting screen.
        :parameter:
        :return:
        '''
        self.wait_for_spinner_screen_load()
        logging.debug("Start to check UI strings of Connecting screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
        assert self.get_value_of_spinner_text() == test_strings['connecting']

    def verify_dialog_disappear(self, timeout=10):
        '''
        This is a verification method to check Connect to the Internet dialog disappear after clicking Continue button with Internect connected.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("connect_to_the_internet_title", timeout=timeout, raise_e=False)

    def verify_spinner_screen(self):
        '''
        This is a verification method to check loading screen display
        :parameter:
        :return:
        '''
#         self.verify_checking_internet_connection_screen()
#         self.verify_establishing_connection_screen()
#         sleep(2)
#         self.verify_connecting_screen()
        self.wait_for_spinner_screen_load()
#         logging.debug("Start to check UI strings of Checking Internet connection screen")
#         test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_to_the_internet_dialog')
#         assert self.get_value_of_spinner_text() in test_strings['checking_internet_connection'] or test_strings['establishing_connection'] or test_strings['connecting']
