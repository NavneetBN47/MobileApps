# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect printer to WiFi screen.

@author: ten
@create_date: July 25, 2019
'''
import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectPrintertoWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_printer_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectPrintertoWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("change_network_link", timeout=timeout, raise_e=raise_e)

    def wait_for_access_wifi_password_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_access_wifi_password_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("access_wifi_password_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_unable_to_access_wifi_password_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_unable_to_access_wifi_password_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("unable_to_access_wifi_password_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_incorrect_pw_text_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Incorrect password text load after inputing incorrect password.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_incorrect_pw_text_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("incorrect_pw_text", timeout=timeout, raise_e=raise_e)

    def click_info_btn(self):
        '''
        This is a method to click Info button on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_info_btn]-Click info button... ")

        self.driver.click("info_btn")

    def click_change_network_link(self):
        '''
        This is a method to click Change Network link on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_change_network_link]-Click Change Network link... ")

        self.driver.click("change_network_link", is_native_event=True)

    def input_enter_wifi_password_box(self, contents):
        '''
        input enter contents in password box
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[enter_wifi_password_box]input-enter_wifi_password_box... ")

        self.driver.send_keys("enter_wifi_password_box", contents)

    def clear_enter_wifi_password_box(self):
        '''
        clear enter contents in password box
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[enter_wifi_password_box]clear-enter_wifi_password_box... ")

        self.driver.clear_text("enter_wifi_password_box")

    def click_access_my_wifi_password_automatically_link(self):
        '''
        This is a method to click Access my WiFi password automatically link on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_access_my_wifi_password_automatically_link]-Click Access my WiFi password automatically link... ")

        self.driver.click("access_my_wifi_password_automatically_link", is_native_event=True)

    def click_connect_btn(self):
        '''
        This is a method to click Connect button on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("connect_btn")

    def click_no_thanks_btn_on_access_wifi_password(self):
        '''
        This is a method to click "No, thanks" button on Access WiFi Password for... dialog
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_no_thanks_btn_on_access_wifi_password]-Click No thanks button... ")

        self.driver.click("access_wifi_password_dialog_no_thanks_btn", is_native_event=True)

    def click_continue_btn_on_access_wifi_password(self):
        '''
        This is a method to click "Continue" button on Access WiFi Password for... dialog
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_continue_btn_on_access_wifi_password]-Click continue button... ")

        self.driver.click("access_wifi_password_dialog_continue_btn", is_native_event=True)

    def get_value_of_connect_printer_to_wifi_title(self):
        '''
        This is a method to get the value of Connect Printer to WiFi title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_title]-Get the contents of Connect Printer to WiFi title...  ")

        return self.driver.get_value("connect_printer_to_wifi_title")

    def get_value_of_connect_printer_to_wifi_printer_name(self):
        '''
        This is a method to get the value of Printer Name on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_printer_name]-Get the contents of Printer Name...  ")

        return self.driver.get_value("connect_printer_to_wifi_printer_name")

    def get_value_of_wifi_network_text(self):
        '''
        This is a method to get the value of WiFi Network text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_wifi_network_text]-Get the contents of WiFi Network text...  ")

        return self.driver.get_value("wifi_network_text")

    def get_value_of_router_name_text(self):
        '''
        This is a method to get the value of Router Name on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_router_name_text]-Get the contents of Router Name...  ")

        return self.driver.get_value("router_name_text")

    def get_value_of_change_network_link(self):
        '''
        This is a method to get the value of Change Network link on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_change_network_link]-Get the contents of Change Network link...  ")

        return self.driver.get_title("change_network_link")

    def get_value_of_enter_wifi_password_text(self):
        '''
        This is a method to get the value of Enter WiFi Password text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_enter_wifi_password_text]-Get the contents of Enter WiFi Password text...  ")

        return self.driver.get_value("enter_wifi_password_text")

    def get_value_of_access_my_wifi_password_automatically_link(self):
        '''
        This is a method to get the value of Access my WiFi password automatically link on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_my_wifi_password_automatically_link]-Get the contents of Access my WiFi password automatically link...  ")

        return self.driver.get_title("access_my_wifi_password_automatically_link")

    def get_value_of_connect_btn(self):
        '''
        This is a method to get the value of Connect button on Connect Printer to WiFi screen
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_btn]-Get the contents of Connect button...  ")

        return self.driver.get_title("connect_btn")

    def get_value_of_incorrect_password_text(self):
        '''
        This is a method to get the value of Incorrect password text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_incorrect_password_text]-Get the contents of incorrectpassword_text ...  ")

        return self.driver.get_value("incorrect_pw_text")

    def get_value_of_access_wifi_password_dialog_title(self):
        '''
        This is a method to get the value of Access WiFi Password dialog title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_title]-Get the contents of access_wifi_password_dialog_title...  ")

        return self.driver.get_value("access_wifi_password_dialog_title")

    def get_value_of_access_wifi_password_dialog_content_1(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_1]-Get the contents of access_wifi_password_dialog_content_1...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_1")

    def get_value_of_access_wifi_password_dialog_content_2(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 2
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_2]-Get the contents of access_wifi_password_dialog_content_2...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_2")

    def get_value_of_access_wifi_password_dialog_content_3(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 3
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_3]-Get the contents of access_wifi_password_dialog_content_3...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_3")

    def get_value_of_access_wifi_password_dialog_content_4(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 4
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_4]-Get the contents of access_wifi_password_dialog_content_4...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_4")

    def get_value_of_access_wifi_password_dialog_no_thanks_btn(self):
        '''
        This is a method to get the value of Access WiFi Password dialog No thanks button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_no_thanks_btn]-Get the contents of No thanks button...  ")

        return self.driver.get_title("access_wifi_password_dialog_no_thanks_btn")

    def get_value_of_access_wifi_password_dialog_continue_btn(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("access_wifi_password_dialog_continue_btn")

    def get_value_of_unable_to_access_wifi_password_dialog_title(self):
        '''
        This is a method to get the value of unable_to_access_wifi_password_dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_unable_to_access_wifi_password_dialog_title]-Get the contents of unable_to_access_wifi_password_dialog_title...  ")

        return self.driver.get_value("unable_to_access_wifi_password_dialog_title")

    def get_value_of_unable_to_access_wifi_password_dialog_ok_btn(self):
        '''
        This is a method to get the value of unable_to_access_wifi_password_dialog_ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_unable_to_access_wifi_password_dialog_ok_btn]-Get the contents of unable_to_access_wifi_password_dialog_ok_btn...  ")

        return self.driver.get_title("unable_to_access_wifi_password_dialog_ok_btn")

    def get_value_of_unable_to_access_wifi_password_dialog_content(self):
        '''
        This is a method to get the value of unable_to_access_wifi_password_dialog_content
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_unable_to_access_wifi_password_dialog_content]-Get the contents of unable_to_access_wifi_password_dialog_content...  ")

        return self.driver.get_value("unable_to_access_wifi_password_dialog_content")

    def click_unable_to_access_wifi_password_dialog_ok_btn(self):
        '''
        This is a method to click Connect button on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_unable_to_access_wifi_password_dialog_ok_btn]-Click unable_to_access_wifi_password_dialog_ok_btn... ")

        self.driver.click("unable_to_access_wifi_password_dialog_ok_btn")

    def wait_for_screen_pc_no_wifi_with_wifi_list_field_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Connect printer to Wi-Fi with Wifi list field screen load while PC has no Wi-Fi connected.
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("refresh_network_list_btn_pc_no_wifi", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_pc_no_wifi_with_wifi_entry_field_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Connect printer to Wi-Fi with Wifi entry field screen load while PC has no Wi-Fi connected.
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("wifi_name_textfield_pc_no_wifi_with_wifi_entry_field", timeout=timeout, raise_e=raise_e)

    def wait_for_refreshing_network_list_text_disappear(self, timeout=120):
        '''
        This is a method to wait Creating preview text disappear.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_refreshing_network_list_text_disappear]-Wait for screen disappear... ")

        return self.driver.wait_for_object_disappear("refreshing_network_list_text_pc_no_wifi", timeout=timeout, raise_e=False)

    def wait_for_incorrect_pw_text_pc_no_wifi_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Incorrect password text load after inputing incorrect password on Connect printer to Wi-Fi screen while PC has no Wi-Fi connected..
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_incorrect_pw_text_pc_no_wifi_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("incorrect_pw_text_pc_no_wifi", timeout=timeout, raise_e=raise_e)

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of title on Connect printer to Wi-Fi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_screen_title]-Get the value of screen_title...  ")

        return self.driver.get_value("connect_printer_to_wifi_screen_title_pc_no_wifi")

    def get_value_of_wifi_name_title(self):
        '''
        This is a method to get the value of Wifi name title on Connect printer to Wi-Fi with wifi list field screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_wifi_name_title]-Get the value of Wifi name title...  ")

        return self.driver.get_value("wifi_name_title_pc_no_wifi")

    def get_value_of_wifi_name_title_with_wifi_entry_field(self):
        '''
        This is a method to get the value of Wifi name title on Connect printer to Wi-Fi with wifi entry field screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_wifi_name_title]-Get the value of Wifi name title...  ")

        return self.driver.get_value("wifi_name_title_pc_no_wifi_with_wifi_entry_field")

    def get_value_of_wifi_password_title(self):
        '''
        This is a method to get the value of Wifi password title on Connect printer to Wi-Fi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_wifi_password_title]-Get the value of Wifi password title...  ")

        return self.driver.get_value("wifi_password_title_pc_no_wifi")

    def get_value_of_refresh_network_list_btn(self):
        '''
        This is a method to get the value of Refresh Network list button on Connect printer to Wi-Fi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_refresh_network_list_btn]-Get the value of Refresh Network list button...  ")

        return self.driver.get_title("refresh_network_list_btn_pc_no_wifi")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Connect printer to Wi-Fi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("continue_btn_pc_no_wifi")

    def get_value_of_incorrect_pw_text_pc_no_wifi(self):
        '''
        This is a method to get the value of Incorrect password text on Connect Printer to WiFi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_incorrect_pw_text_pc_no_wifi]-Get the contents of incorrect password_text ...  ")

        return self.driver.get_value("incorrect_pw_text_pc_no_wifi")

    def click_refresh_btn(self):
        '''
        This is a method to click Refresh button on Connect printer to Wi-Fi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_refresh_btn]-Click refresh button... ")

        self.driver.click("refresh_network_list_btn_pc_no_wifi")

    def choose_wifi_name(self, wifi_name):
        '''
        This is a method to choose Wi-Fi under Wi-Fi list.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[choose_country_dropdown_listitems]-choose any option in country drop down list... ")

        self.driver.click("drop_list_btn_pc_no_wifi")
        sleep(1)
        self.driver.click("wifi_list_pc_no_wifi", format_specifier=[wifi_name], is_native_event=True)

    def input_wifi_name(self, wifi_name):
        '''
        This is a method to input Wi-Fi name on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[input_wifi_name]-input Wi-Fi name... ")

        self.driver.send_keys("wifi_name_textfield_pc_no_wifi_with_wifi_entry_field", wifi_name)

    def input_wifi_password(self, wifi_password):
        '''
        This is a method to input Wi-Fi password on Connect printer to Wi-Fi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[input_wifi_password]-input Wi-Fi password... ")

        self.driver.send_keys("wifi_password_textfield_pc_no_wifi", wifi_password)

    def click_continue_btn(self):
        '''
        This is a method to click Connect button on Connect printer to Wi-Fi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_btn]-Click Connect button... ")

        self.driver.click("continue_btn_pc_no_wifi")

    def wait_for_connect_printer_to_wifi_with_wifi_entry_field_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Connect printer to Wi-Fi with wifi entry field screen load.
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_connect_printer_to_wifi_with_wifi_entry_field_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_printer_to_wifi_with_wifi_entry_field_screen_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_title(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi entry field screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_title]-Get the contents of Connect printer to Wi-Fi with wifi entry field screen title...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_entry_field_screen_title")

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_1(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi entry field screen content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_1]-Get the contents of Connect printer to Wi-Fi with wifi entry field screen content - 1...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_1")

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_2(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi entry field screen content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_2]-Get the contents of Connect printer to Wi-Fi with wifi entry field screen content - 2...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_2")

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_wifi_network_name_exactly_text(self):
        '''
        This is a method to get the value of Enter the wifi network name exactly text on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_wifi_network_name_exactly_text]-Get the contents of Enter the wifi network name exactly text...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_wifi_network_name_exactly_text")

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_password_for_this_wifi_network_text(self):
        '''
        This is a method to get the value of Enter the password for this wifi network text on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_password_for_this_wifi_network_text]-Get the contents of Enter the password for this wifi network text...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_password_for_this_wifi_network_text")

    def get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn]-Get the contents of Continue button...")

        return self.driver.get_title("connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn")

    def click_connect_printer_to_wifi_with_wifi_entry_field_screen_learn_more_text(self):
        '''
        This is a method to click Learn more text on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_printer_to_wifi_with_wifi_entry_field_screen_learn_more_text]-Click Learn more text... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_2")

    def input_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_network_name_textfield(self, wifi_name):
        '''
        This is a method to input Wi-Fi network name on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[input_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_network_name_textfield]-Input Wi-Fi network name...")

        self.driver.send_keys("connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_network_name_textfield", wifi_name)

    def input_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_password_textfield(self, wifi_password):
        '''
        This is a method to input Wi-Fi network password on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[input_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_password_textfield]-Input Wi-Fi network password...")

        self.driver.send_keys("connect_printer_to_wifi_with_wifi_entry_field_screen_enter_wifi_password_textfield", wifi_password)

    def click_connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Connect printer to Wi-Fi with wifi entry field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn]-Click Continue button... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn")

    def wait_for_connect_printer_to_wifi_with_wifi_list_field_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Connect printer to Wi-Fi with wifi list field screen load.
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_connect_printer_to_wifi_with_wifi_list_field_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_printer_to_wifi_with_wifi_list_field_screen_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_title(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi list field screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_title]-Get the contents of Connect printer to Wi-Fi with wifi list field screen title...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_title")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_1(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi list field screen content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_1]-Get the contents of Connect printer to Wi-Fi with wifi list field screen content - 1...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_content_1")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_2(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi list field screen content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_2]-Get the contents of Connect printer to Wi-Fi with wifi list field screen content - 2...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_content_2")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_3(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi list field screen content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_3]-Get the contents of Connect printer to Wi-Fi with wifi list field screen content - 3...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_content_3")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_4(self):
        '''
        This is a method to get the value of Connect printer to Wi-Fi with wifi list field screen content - 4.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_4]-Get the contents of Connect printer to Wi-Fi with wifi list field screen content - 4...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_content_4")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_choose_a_wifi_network_from_the_list_text(self):
        '''
        This is a method to get the value of Choose a wifi network form the list text on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_choose_a_wifi_network_from_the_list_text]-Get the contents of Choose a wifi network form the list text...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_choose_a_wifi_network_from_the_list_text")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_refresh_network_list_btn(self):
        '''
        This is a method to get the value of Refresh network list button on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_refresh_network_list_btn]-Get the contents of Refresh network list button...")

        return self.driver.get_title("connect_printer_to_wifi_with_wifi_list_field_screen_refresh_network_list_btn")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_enter_the_password_text(self):
        '''
        This is a method to get the value of Enter the password text on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_enter_the_password_text]-Get the contents of Enter the password text...")

        return self.driver.get_value("connect_printer_to_wifi_with_wifi_list_field_screen_enter_the_password_text")

    def get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn]-Get the contents of Continue button...")

        return self.driver.get_title("connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn")

    def click_connect_printer_to_wifi_with_wifi_list_field_screen_learn_more_text(self):
        '''
        This is a method to click Learn more text on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_printer_to_wifi_with_wifi_list_field_screen_learn_more_text]-Click Learn more text... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_list_field_screen_content_2")

    def click_connect_printer_to_wifi_with_wifi_list_field_screen_enter_your_wifi_network_manually_text(self):
        '''
        This is a method to click Enter your wifi network manually text on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_printer_to_wifi_with_wifi_list_field_screen_enter_your_wifi_network_manually_text]-Click Enter your wifi network manually text... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_list_field_screen_content_4")

    def choose_connect_printer_to_wifi_with_wifi_list_field_screen_wifi_name_list_item(self, wifi_name):
        '''
        This is a method to choose Wi-Fi under Wi-Fi list on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[choose_connect_printer_to_wifi_with_wifi_list_field_screen_wifi_name_list_item]-choose any option in country drop down list... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_list_field_screen_wifi_name_list_combobox_btn")
        sleep(1)
        self.driver.click("connect_printer_to_wifi_with_wifi_list_field_screen_wifi_name_list_items", format_specifier=[wifi_name], is_native_event=True)

    def input_connect_printer_to_wifi_with_wifi_list_field_screen_wifi_password(self, wifi_password):
        '''
        This is a method to input Wi-Fi password on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[input_wifi_password]-input Wi-Fi password... ")

        self.driver.send_keys("connect_printer_to_wifi_with_wifi_list_field_screen_wifi_password_textfield", wifi_password)

    def click_connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Connect printer to Wi-Fi with wifi list field screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn]-Click Continue button... ")

        self.driver.click("connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn")

    def wait_for_choose_a_24ghz_network_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Choose a 2.4Ghz network dialog load.
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_choose_a_24ghz_network_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("choose_a_24ghz_network_dialog_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_choose_a_24ghz_network_dialog_title(self):
        '''
        This is a method to get the value of Choose a 2.4Ghz Network dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_title]-Get the contents of Choose a 2.4Ghz Network dialog title...")

        return self.driver.get_value("choose_a_24ghz_network_dialog_title")

    def get_value_of_choose_a_24ghz_network_dialog_content_1(self):
        '''
        This is a method to get the value of Choose a 2.4Ghz Network dialog content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_content_1]-Get the contents of Choose a 2.4Ghz Network dialog content - 1...")

        return self.driver.get_value("choose_a_24ghz_network_dialog_content_1")

    def get_value_of_choose_a_24ghz_network_dialog_content_2(self):
        '''
        This is a method to get the value of Choose a 2.4Ghz Network dialog content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_content_2]-Get the contents of Choose a 2.4Ghz Network dialog content - 3...")

        return self.driver.get_value("choose_a_24ghz_network_dialog_content_2")

    def get_value_of_choose_a_24ghz_network_dialog_content_3(self):
        '''
        This is a method to get the value of Choose a 2.4Ghz Network dialog content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_content_3]-Get the contents of Choose a 2.4Ghz Network dialog content - 3...")

        return self.driver.get_value("choose_a_24ghz_network_dialog_content_3")

    def get_value_of_choose_a_24ghz_network_dialog_content_4(self):
        '''
        This is a method to get the value of Choose a 2.4Ghz Network dialog content - 4.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_content_4]-Get the contents of Choose a 2.4Ghz Network dialog content - 4...")

        return self.driver.get_value("choose_a_24ghz_network_dialog_content_4")

    def get_value_of_choose_a_24ghz_network_dialog_ok_btn(self):
        '''
        This is a method to get the value of Ok button on Choose a 2.4Ghz Network dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_choose_a_24ghz_network_dialog_ok_btn]-Get the contents of Ok button...")

        return self.driver.get_title("choose_a_24ghz_network_dialog_ok_btn")

    def click_choose_a_24ghz_network_dialog_ok_btn(self):
        '''
        This is a method to click Ok button on Choose a 2.4Ghz Network dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_choose_a_24ghz_network_dialog_ok_btn]-Click Ok button... ")

        self.driver.click("choose_a_24ghz_network_dialog_ok_btn")

# -------------------------------Verification Methods------------------------
    def verify_access_wifi_password_dialog(self):
        '''
        This is a verification method to check UI strings of Access WiFi Password dialog.
        :parameter:
        :return:
        '''
        self.wait_for_access_wifi_password_dialog_load()
        logging.debug("Start to verify UI string of Access WiFi Password dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='access_wifi_password_dialog')
        assert test_strings['access_wifi_password_dialog_title'] in self.get_value_of_access_wifi_password_dialog_title()
        assert self.get_value_of_access_wifi_password_dialog_content_1() == test_strings['access_wifi_password_dialog_content_1']
        assert self.get_value_of_access_wifi_password_dialog_content_2() == test_strings['access_wifi_password_dialog_content_2']
        assert self.get_value_of_access_wifi_password_dialog_content_3() == test_strings['access_wifi_password_dialog_content_3']
        assert self.get_value_of_access_wifi_password_dialog_content_4() == test_strings['access_wifi_password_dialog_content_4']
        assert self.get_value_of_access_wifi_password_dialog_no_thanks_btn() == test_strings['access_wifi_password_dialog_no_thanks_btn']
        assert self.get_value_of_access_wifi_password_dialog_continue_btn() == test_strings['access_wifi_password_dialog_continue_btn']

    def verify_access_wifi_password_dialog_dismiss(self, timeout=5):
        '''
        This is a verification method to check Access WiFi Password dialog after clicking No Thanks button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("access_wifi_password_dialog_title", timeout=timeout, raise_e=False)

    def verify_unable_to_access_wifi_password_dialog(self):
        '''
        This is a verification method to check UI strings of Unable to access Wi-Fi password dialog.
        :parameter:
        :return:
        '''
        self.wait_for_unable_to_access_wifi_password_dialog_load()
        logging.debug("Start to verify UI string of unable_to_access_wifi_password_dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='unable_to_access_wifi_password_dialog')
        assert self.get_value_of_unable_to_access_wifi_password_dialog_title() == test_strings['unable_to_access_wifi_password_dialog_title']
        assert self.get_value_of_unable_to_access_wifi_password_dialog_ok_btn() == test_strings['unable_to_access_wifi_password_dialog_ok_btn']
        assert self.get_value_of_unable_to_access_wifi_password_dialog_content() == test_strings['unable_to_access_wifi_password_dialog_content']

    def verify_connect_printer_to_wifi_screen(self, printer_name, wifi_name):
        '''
        This is a verification method to check UI strings of Connect Printer To WiFi screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.driver.wait_for_object("info_btn", timeout=30, raise_e=True)
        self.driver.wait_for_object("enable_diable_show_password_btn", timeout=30, raise_e=True)

        logging.debug("Start to verify UI string of Connect Printer To WiFi screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_connect_printer_to_wifi_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_connect_printer_to_wifi_printer_name() == printer_name
        assert self.get_value_of_wifi_network_text() == test_strings['wifi_network_text']
        assert self.get_value_of_router_name_text() == wifi_name
        assert self.get_value_of_change_network_link() == test_strings['change_network_link']
#         assert self.get_value_of_enter_wifi_password_text() == test_strings['enter_wifi_password_text']
        assert self.get_value_of_access_my_wifi_password_automatically_link() == test_strings['access_my_wifi_password_automatically_link']
        assert self.get_value_of_connect_btn() == test_strings['connect_btn']

    def verify_incorrect_password_warning(self):
        '''
        This is a verification method to check UI strings of Incorrect password after input a incorrect password on Connect Printer To WiFi screen.
        :parameter:
        :return:
        '''
        self.wait_for_incorrect_pw_text_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_incorrect_password_text() == test_strings['incorrect_pw_text']

    def verify_incorrect_password_warning_pc_no_wifi(self):
        '''
        This is a verification method to check UI strings of Incorrect password after input a incorrect password on Connect Printer To WiFi screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        self.wait_for_incorrect_pw_text_pc_no_wifi_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_incorrect_pw_text_pc_no_wifi() == test_strings['incorrect_pw_text']

    def verify_connect_printer_to_wifi_with_wifi_list_field_screen_pc_no_wifi(self):
        '''
        This is a verification method to check UI strings of Connect printer to Wi-Fi with wifi list field screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        self.wait_for_refreshing_network_list_text_disappear()
        self.wait_for_screen_pc_no_wifi_with_wifi_list_field_load()
        logging.debug("Start to verify UI string of Connect printer to Wi-Fi with wifi list field screen while PC has no Wi-Fi connected")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_screen_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_wifi_name_title() == test_strings['wifi_name_title']
        assert self.get_value_of_wifi_password_title() == test_strings['wifi_password_title']
        assert self.get_value_of_refresh_network_list_btn() == test_strings['refresh_network_list_btn']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_to_wifi_with_wifi_entry_field_screen_pc_no_wifi(self):
        '''
        This is a verification method to check UI strings of Connect printer to Wi-Fi with wifi entry field screen while PC has no Wi-Fi connected.
        :parameter:
        :return:
        '''
        self.wait_for_refreshing_network_list_text_disappear()
        self.wait_for_screen_pc_no_wifi_with_wifi_entry_field_load()
        logging.debug("Start to verify UI string of Connect printer to Wi-Fi with wifi entry field screen while PC has no Wi-Fi connected")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_screen_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_wifi_name_title_with_wifi_entry_field() == test_strings['enter_the_wifi_network_name_exactly_text']
        assert self.get_value_of_wifi_password_title() == test_strings['wifi_password_title']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_to_wifi_with_wifi_list_field_screen(self):
        '''
        This is a verification method to check UI strings of Connect printer to Wi-Fi screen with 2.4g network wifi list detected.
        :parameter:
        :return:
        '''
        self.wait_for_connect_printer_to_wifi_with_wifi_list_field_screen_load(120)
        logging.debug("Start to verify UI string of Connect printer to Wi-Fi screen with 2.4g network wifi list detected")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_1() == test_strings['choose_a_wifi_network_from_the_list_below_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_2() == test_strings['learn_more_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_3() == test_strings['if_you_cant_find_your_wifi_network_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_content_4() == test_strings['enter_your_wifi_network_manually_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_choose_a_wifi_network_from_the_list_text() == test_strings['wifi_name_title']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_refresh_network_list_btn() == test_strings['refresh_network_list_btn']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_enter_the_password_text() == test_strings['wifi_password_title']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_list_field_screen_continue_btn() == test_strings['continue_btn']

    def verify_connect_printer_to_wifi_with_wifi_entry_field_screen(self):
        '''
        This is a verification method to check UI strings of Connect printer to Wi-Fi screen without 2.4g network wifi list detected.
        :parameter:
        :return:
        '''
        self.wait_for_connect_printer_to_wifi_with_wifi_entry_field_screen_load(120)
        logging.debug("Start to verify UI string of Connect printer to Wi-Fi screen without 2.4g network wifi list detected")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_title() == test_strings['connect_printer_to_wifi_title']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_1() == test_strings['enter_your_wifi_network_below_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_conetnt_2() == test_strings['learn_more_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_wifi_network_name_exactly_text() == test_strings['enter_the_wifi_network_name_exactly_text']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_enter_the_password_for_this_wifi_network_text() == test_strings['wifi_password_title']
        assert self.get_value_of_connect_printer_to_wifi_with_wifi_entry_field_screen_continue_btn() == test_strings['continue_btn']

    def verify_choose_a_24ghz_network_dialog(self):
        '''
        This is a verification method to check UI strings of Choose a 2.4Ghz network dialog.
        :parameter:
        :return:
        '''
        self.wait_for_choose_a_24ghz_network_dialog_load(120)
        logging.debug("Start to verify UI string of Choose a 2.4Ghz network dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_wifi_screen')
        assert self.get_value_of_choose_a_24ghz_network_dialog_title() == test_strings['choose_a_24ghz_network_dialog_title']
        assert self.get_value_of_choose_a_24ghz_network_dialog_content_1() == test_strings['choose_a_24ghz_network_dialog_content_1']
        assert self.get_value_of_choose_a_24ghz_network_dialog_content_2() == test_strings['choose_a_24ghz_network_dialog_content_2']
        assert self.get_value_of_choose_a_24ghz_network_dialog_content_3() == test_strings['choose_a_24ghz_network_dialog_content_3']
        assert self.get_value_of_choose_a_24ghz_network_dialog_content_4() == test_strings['choose_a_24ghz_network_dialog_content_4']
        assert self.get_value_of_choose_a_24ghz_network_dialog_ok_btn() == test_strings['choose_a_24ghz_network_dialog_ok_btn']
