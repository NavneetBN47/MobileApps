# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Print Anywhere screen

@author: ten
@create_date: Sep 10, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
from MobileApps.libs.flows.mac.smart.screens.common.cookie_settings_banner import CookieSettingsBanner
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class Print_Anywhere(PrinterSettingScroll, SmartScreens):

    folder_name = "printersettings"
    flow_name = "print_anywhere"

    def __init__(self, driver):
        super(Print_Anywhere, self).__init__(driver)

#  ------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Print Anywhere with Enabled button screen load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_anywhere_enable_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_print_anywhere_enabled_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Print Anywhere Enabled with Send Link button screen load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_print_anywhere_enabled_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_anywhere_enabled_send_link_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_print_anywhere_enabled_with_manage_access_btn_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Print Anywhere Enabled with Manage Access button screen load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_print_anywhere_enabled_with_manage_access_btn_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_anywhere_enabled_with_manage_access_btn_title", timeout=timeout, raise_e=raise_e)

    def wait_for_print_from_other_devices_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Print form Other Device screen load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_from_other_devices_title", timeout=timeout, raise_e=raise_e)

    def wait_for_print_connected_another_account_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Print Connected Another Account screen load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_connected_to_another_account_title", timeout=timeout, raise_e=raise_e)

    def wait_for_your_privacy_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Your Privacy dialog load
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_your_privacy_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("your_privacy_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_manage_print_anywhere_screen(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Manage print anywhere screen load
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_manage_print_anywhere_screen]-Wait for screen loading... ")

        return self.driver.wait_for_object("manage_print_anywhere_title", timeout=timeout, raise_e=raise_e)

    def wait_for_printer_connect_to_another_account_screen(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Printer connect to another account screen
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_printer_connect_to_another_account_screen]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_connect_to_another_account_title", timeout=timeout, raise_e=raise_e)

    def wait_for_hp_account_unavailable_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for HP Account Unavailable load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_hp_account_unavailable_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("hp_account_unavailable_content", timeout=timeout, raise_e=raise_e)

    def wait_for_collecting_your_printer_status_text_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Collecting your printer status text load.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_collecting_your_printer_status_text_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("collecting_your_printer_status_text", timeout=timeout, raise_e=raise_e)

    def get_value_of_print_anywhere_title(self):
        '''
        This is a method to get value of Print anywhere screen title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_title]-Get the contents of print_anywhere_title ... ")

        return self.driver.get_value("print_anywhere_title")

    def get_value_of_print_anywhere_content(self):
        '''
        This is a method to get value of Print anywhere screen content.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_content]-Get the contents of Print anywhere screen content... ")

        return self.driver.get_value("print_anywhere_content")

    def get_value_of_get_more_help_link(self):
        '''
        This is a method to get value of Get more help link on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_get_more_help_link]-Get the contents of get_more_help_link... ")

        return self.driver.get_title("print_anywhere_get_more_help_link")

    def get_value_of_enable_btn(self):
        '''
        This is a method to get value of Enable button on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_printer_anywhere_btn-Get the contents of print_anywhere_btn... ")

        return self.driver.get_title("print_anywhere_enable_btn")

    def get_value_of_print_anywhere_enabled_title(self):
        '''
        This is a method to get value of Print anywhere enabled title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enable_title]-Get the contents of Print anywhere enabled title... ")

        return self.driver.get_value("print_anywhere_enabled_title")

    def get_value_of_print_anywhere_enabled_content(self):
        '''
        This is a method to get value of Print anywhere enabled content.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enabled_content]-Get the contents of Print anywhere enabled content... ")

        return self.driver.get_value("print_anywhere_enabled_content")

    def get_value_of_print_anywhere_enabled_send_link_btn(self):
        '''
        This is a method to get value of Send link button on Print anywhere enabled screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enabled_send_link_btn]-Get the contents of Send link button... ")

        return self.driver.get_title("print_anywhere_enabled_send_link_btn")

    def get_value_of_print_anywhere_enabled_with_manage_access_btn_title(self):
        '''
        This is a method to get value of Print anywhere enabled with Manage Access button title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enabled_with_manage_access_btn_title]-Get the contents of Print anywhere enabled with Manage Access button title... ")

        return self.driver.get_value("print_anywhere_enabled_with_manage_access_btn_title")

    def get_value_of_print_anywhere_enabled_with_manage_access_btn_content(self):
        '''
        This is a method to get value of Print anywhere enabled with Manage Access button content.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enabled_with_manage_access_btn_content]-Get the contents of Print anywhere enabled with Manage Access button content... ")

        return self.driver.get_value("print_anywhere_enabled_with_manage_access_btn_content")

    def get_value_of_print_anywhere_enabled_with_manage_access_btn_manage_access_btn(self):
        '''
        This is a method to get value of Manage Access button on Print anywhere enabled with Manage Access button screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enabled_with_manage_access_btn_manage_access_btn]-Get the contents of Manage Access button... ")

        return self.driver.get_title("print_anywhere_enabled_with_manage_access_btn_manage_access_btn")

    def get_value_of_print_anywhere_enable_content(self):
        '''
        This is a method to get the value of Accept cookies button on Cookies banner.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enable_content]-Get the contents of print_anywhere_enable_content ...  ")

        return self.driver.get_title("print_anywhere_enable_content")

    def get_value_of_manage_print_anywhere_title(self):
        '''
        This is a method to get the value of Manage print anywhere title on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_print_anywhere_title]-Get the contents of Manage print anywhere title... ")

        return self.driver.get_title("manage_print_anywhere_title")

    def get_value_of_manage_print_anywhere_print_anywhere_allows_text(self):
        '''
        This is a method to get the value of Print anywhere allows text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_print_anywhere_print_anywhere_allows_text]-Get the contents of Print anywhere allows text... ")

        return self.driver.get_value("manage_print_anywhere_print_anywhere_allows_text")

    def get_value_of_share_this_printer_title(self):
        '''
        This is a method to get the value of Share this printer with any HP account user title on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_this_printer_title]-Get the contents of Share this printer with any HP account user title... ")

        return self.driver.get_title("share_this_printer_title")

    def get_value_of_share_this_printer_when_turned_on_text(self):
        '''
        This is a method to get the value of When turned on text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_this_printer_when_turned_on_text]-Get the contents of When turned on text... ")

        return self.driver.get_value("share_this_printer_when_turned_on_text")

    def get_value_of_share_this_printer_when_turned_off_text(self):
        '''
        This is a method to get the value of When turned off text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_this_printer_when_turned_off_text]-Get the contents of When turned off text... ")

        return self.driver.get_value("share_this_printer_when_turned_off_text")

    def get_value_of_share_remote_access_title(self):
        '''
        This is a method to get the value of Share remote access text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_remote_access_title]-Get the contents of Share remote access text... ")

        return self.driver.get_value("share_remote_access_title")

    def get_value_of_share_remote_access_add_btn(self):
        '''
        This is a method to get the value of Add button on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_remote_access_add_btn]-Get the contents of Add button... ")

        return self.driver.get_title("share_remote_access_add_btn")

    def get_value_of_share_remote_access_user_text(self):
        '''
        This is a method to get the value of User text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_remote_access_user_text]-Get the contents of User text... ")

        return self.driver.get_value("share_remote_access_user_text")

    def get_value_of_share_remote_access_access_text(self):
        '''
        This is a method to get the value of Access text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_share_remote_access_access_text]-Get the contents of Access text... ")

        return self.driver.get_value("share_remote_access_access_text")

    def get_value_of_manage_printers_email_title(self):
        '''
        This is a method to get the value of Manage Printer's email text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_title]-Get the contents of Manage Printer's email text... ")

        return self.driver.get_value("manage_printers_email_title")

    def get_value_of_manage_printers_email_print_a_file_remotely_text(self):
        '''
        This is a method to get the value of Print a file remotely text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_print_a_file_remotely_text]-Get the contents of Print a file remotely text... ")

        return self.driver.get_value("manage_printers_email_print_a_file_remotely_text")

    def get_value_of_manage_printers_email_printers_email_text(self):
        '''
        This is a method to get the value of Printer's email text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_printers_email_text]-Get the contents of Print a file remotely text... ")

        return self.driver.get_value("manage_printers_email_printers_email_text")

    def get_value_of_manage_printers_email_email_address_text(self):
        '''
        This is a method to get the value of Email address text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_email_address_text]-Get the contents of Email address text... ")

        return self.driver.get_value("manage_printers_email_email_address_text")

    def get_value_of_manage_printers_email_personalize_text(self):
        '''
        This is a method to get the value of Personalize your printer's email text on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_personalize_text]-Get the contents of Personalize your printer's email text... ")

        return self.driver.get_value("manage_printers_email_personalize_text")

    def get_value_of_manage_printers_email_change_btn(self):
        '''
        This is a method to get the value of Change button on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_manage_printers_email_change_btn]-Get the contents of Change button... ")

        return self.driver.get_title("manage_printers_email_change_btn")

    def get_value_of_printer_connect_to_another_account_title(self):
        '''
        This is a method to get the value of Printer connect to another account title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_printer_connect_to_another_account_title]-Get the value of Printer connect to another account title... ")

        return self.driver.get_value("printer_connect_to_another_account_title")

    def get_value_of_printer_connect_to_another_account_content(self):
        '''
        This is a method to get the value of Printer connect to another account content.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_printer_connect_to_another_account_content]-Get the value of Printer connect to another account content... ")

        return self.driver.get_value("printer_connect_to_another_account_content")

    def get_value_of_printer_connect_to_another_account_ok_btn(self):
        '''
        This is a method to get the value of OK button on Printer connect to another account screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_printer_connect_to_another_account_ok_btn]-Get the value of OK button... ")

        return self.driver.get_title("printer_connect_to_another_account_ok_btn")

    def get_value_of_hp_account_unavailable_title(self):
        '''
        This is a method to get the value of HP Account Unavailable dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_hp_account_unavailable_title]-Get the value of dialog title... ")

        return self.driver.get_value("hp_account_unavailable_title")

    def get_value_of_hp_account_unavailable_content(self):
        '''
        This is a method to get the value of HP Account Unavailable dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_hp_account_unavailable_content]-Get the value of dialog content... ")

        return self.driver.get_value("hp_account_unavailable_content")

    def get_value_of_hp_account_unavailable_cancel_btn(self):
        '''
        This is a method to get the value of Cancel button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_hp_account_unavailable_cancel_btn]-Get the value of Cancel button... ")

        return self.driver.get_title("hp_account_unavailable_cancel_btn")

    def get_value_of_hp_account_unavailable_try_again_btn(self):
        '''
        This is a method to get the value of Try Again button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_hp_account_unavailable_try_again_btn]-Get the value of Try Again button... ")

        return self.driver.get_title("hp_account_unavailable_try_again_btn")

    def get_value_of_your_privacy_dialog_title(self):
        '''
        This is a method to get the value of Your Privacy dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_title]-Get the contents of Your Privacy dialog title... ")

        return self.driver.get_value("your_privacy_dialog_title")

    def get_value_of_your_privacy_dialog_content_1(self):
        '''
        This is a method to get the value of content - 1 on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_content_1]-Get the contents of content - 1 on Your Privacy dialog... ")

        return self.driver.get_value("your_privacy_dialog_content_1")

    def get_value_of_your_privacy_dialog_content_2(self):
        '''
        This is a method to get the value of content - 2 on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_content_2]-Get the contents of content - 2 on Your Privacy dialog... ")

        return self.driver.get_title("your_privacy_dialog_content_2")

    def get_value_of_your_privacy_dialog_content_3(self):
        '''
        This is a method to get the value of content - 3 on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_content_3]-Get the contents of content - 3 on Your Privacy dialog... ")

        return self.driver.get_value("your_privacy_dialog_content_3")

    def get_value_of_your_privacy_dialog_content_4(self):
        '''
        This is a method to get the value of content - 4 on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_content_4]-Get the contents of content - 4 on Your Privacy dialog... ")

        return self.driver.get_title("your_privacy_dialog_content_4")

    def get_value_of_your_privacy_dialog_more_options_btn(self):
        '''
        This is a method to get the value of More Options button on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_more_options_btn]-Get the contents of More Options button on Your Privacy dialog... ")

        return self.driver.get_title("your_privacy_dialog_more_options_btn")

    def get_value_of_your_privacy_dialog_i_accept_btn(self):
        '''
        This is a method to get the value of I Accept button on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_your_privacy_dialog_i_accept_btn]-Get the contents of I Accept button on Your Privacy dialog... ")

        return self.driver.get_title("your_privacy_dialog_i_accept_btn")

    def click_get_more_help_link(self):
        '''
        This is a method to click Get more help link on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_get_more_help_link]-Click get_more_help_link... ")

        self.driver.click("print_anywhere_get_more_help_link", is_native_event=True)

    def click_enable_btn(self):
        '''
        This is a method to click Enable button after sign in on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_enable_btn]-Click enable_btn... ")

        self.driver.click("print_anywhere_enable_btn", is_native_event=True)

    def click_send_link_btn(self):
        '''
        This is a method to click Send Link button on Print anywhere Enabled screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_send_link_btn]-Click Send Link button... ")

        self.driver.click("print_anywhere_enabled_send_link_btn", is_native_event=True)

    def click_manage_access_btn(self):
        '''
        This is a method to click Manage Access button on Print Anywhere Enabled with Manage Access button screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_manage_access_btn]-Click Manage Access button... ")

        self.driver.click("print_anywhere_enabled_with_manage_access_btn_manage_access_btn", is_native_event=True)

    def click_share_this_printer_toggle_btn(self):
        '''
        This is a method to click Share this printer Toggle button on Manage print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_share_this_printer_toggle_btn]-Click Share this printer Toggle button... ")

        self.driver.click("share_this_printer_toggle_btn", is_native_event=True)

    def input_shared_email_address(self, email_address):
        '''
        This is a method to input Shared email address.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[input_shared_email_address]-Input shared email address... ")

        self.driver.send_keys("share_remote_access_email_inputbox", email_address)

    def click_shared_email_address_add_btn(self):
        '''
        This is a method to click Add button after input shared remote access email address.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_shared_email_address_add_btn]-Click Add button... ")

        self.driver.click("share_remote_access_add_btn", is_native_event=True)

    def click_printer_connect_to_another_account_ok_btn(self):
        '''
        This is a method to click OK button on Printer connected to another account screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_printer_connect_to_another_account_ok_btn]-Click OK button... ")

        self.driver.click("printer_connect_to_another_account_ok_btn", is_native_event=True)

    def click_hp_account_unavailable_cancel_btn(self):
        '''
        This is a method to click Cancel button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_hp_account_unavailable_cancel_btn]-Click Cancel button... ")

        self.driver.click("hp_account_unavailable_cancel_btn", is_native_event=True)

    def click_hp_account_unavailable_try_again_btn(self):
        '''
        This is a method to click Try Again button on HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_hp_account_unavailable_try_again_btn]-Click Try Again button... ")

        self.driver.click("hp_account_unavailable_try_again_btn", is_native_event=True)

    def click_your_privacy_dialog_more_options_btn(self):
        '''
        This is a method to click More Options button on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_your_privacy_dialog_more_options_btn]-Click More Options button on Your Privacy dialog... ")

        self.driver.click("your_privacy_dialog_more_options_btn", is_native_event=True)

    def click_your_privacy_dialog_i_accept_btn(self):
        '''
        This is a method to click I Accept button on Your Privacy dialog.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_your_privacy_dialog_i_accept_btn]-Click I Accept button on Your Privacy dialog... ")

        self.driver.click("your_privacy_dialog_i_accept_btn", is_native_event=True)

#   ------------------------------Verification Methods-------------------------------------------
    def verify_print_anywhere_screen(self):
        '''
        This is a method to check UI strings for Print Anywhere screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of Print Anywhere screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_anywhere_screen')
        assert self.get_value_of_print_anywhere_title() == test_strings['print_anywhere_title']
        assert self.get_value_of_print_anywhere_content() == test_strings['use_your_hp_account_content']
        assert self.get_value_of_get_more_help_link() == test_strings['get_more_help_link']
        assert self.get_value_of_enable_btn() == test_strings['enable_btn']

    def verify_print_anywhere_enabled_screen(self):
        '''
        This is a method to check UI strings of Print Anywhere Enabled screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_anywhere_enabled_screen_load(300)
        logging.debug("Start to check UI strings of Print Anywhere Enabled screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_anywhere_screen')
        assert self.get_value_of_print_anywhere_enabled_title() == test_strings['print_anywhere_enabled_title']
        assert self.get_value_of_print_anywhere_enabled_content() == test_strings['print_anywhere_enabled_content']
        assert self.get_value_of_print_anywhere_enabled_send_link_btn() == test_strings['print_anywhere_enabled_send_link_btn']

    def verify_your_privacy_dialog(self):
        '''
        This is a method to check UI strings of Your Privacy dialog.
        :parameter:
        :return:
        '''
        self.wait_for_your_privacy_dialog_load(300)
        logging.debug("Start to check UI strings of Your Privacy dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='your_privacy_dialog')
        assert self.get_value_of_your_privacy_dialog_title() == test_strings['your_privacy_dialog_title']
        assert self.get_value_of_your_privacy_dialog_content_1() == test_strings['your_privacy_dialog_content_1']
        assert self.get_value_of_your_privacy_dialog_content_2() == test_strings['your_privacy_dialog_content_2']
        assert self.get_value_of_your_privacy_dialog_content_3() == test_strings['your_privacy_dialog_content_3']
        assert self.get_value_of_your_privacy_dialog_content_4() == test_strings['your_privacy_dialog_content_4']
        assert self.get_value_of_your_privacy_dialog_more_options_btn() == test_strings['your_privacy_dialog_more_options_btn']
        assert self.get_value_of_your_privacy_dialog_i_accept_btn() == test_strings['your_privacy_dialog_i_accept_btn']

    def verify_print_anywhere_enabled_with_manage_access_btn_screen(self):
        '''
        This is a method to check UI strings of Print Anywhere Enabled with Manage Access button screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_anywhere_enabled_with_manage_access_btn_screen_load(300)
        logging.debug("Start to check UI strings of Print Anywhere Enabled screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_anywhere_screen')
        assert self.get_value_of_print_anywhere_enabled_with_manage_access_btn_title() == test_strings['print_anywhere_enabled_title']
#         assert self.get_value_of_print_anywhere_enabled_with_manage_access_btn_content() == test_strings['print_anywhere_enabled_with_manage_access_btn_content']
        assert self.get_value_of_print_anywhere_enabled_with_manage_access_btn_manage_access_btn() == test_strings['print_anywhere_enabled_with_manage_access_btn_manage_access_btn']

    def verify_manage_print_anywhere_screen(self):
        '''
        This is a method to check UI strings of Manage Print Anywhere screen.
        :parameter:
        :return:
        '''
        self.wait_for_manage_print_anywhere_screen(300)
        cookie_settings_banner = CookieSettingsBanner(self.driver)
        if cookie_settings_banner.wait_for_screen_load(raise_e=False):
            cookie_settings_banner.click_cookie_settings_banner_accept_all_cookies_btn()
        elif self.wait_for_your_privacy_dialog_load(timeout=5, raise_e=False):
            self.verify_your_privacy_dialog()
            self.click_your_privacy_dialog_i_accept_btn()
        logging.debug("Start to check UI strings of Manage Print Anywhere screen")
#         assert self.get_value_of_manage_print_anywhere_title() == u''
#         assert self.get_value_of_manage_print_anywhere_print_anywhere_allows_text() == u''
#         assert self.get_value_of_share_this_printer_title() == u''
#         assert self.get_value_of_share_this_printer_when_turned_on_text() == u''
#         assert self.get_value_of_share_this_printer_when_turned_off_text() == u''
#         assert self.get_value_of_share_remote_access_title() == u''
#         assert self.get_value_of_share_remote_access_add_btn() == u''
#         assert self.get_value_of_share_remote_access_user_text() == u''
#         assert self.get_value_of_share_remote_access_access_text() == u''
#         assert self.get_value_of_manage_printers_email_title() == u''
#         assert self.get_value_of_manage_printers_email_print_a_file_remotely_text() == u''
#         assert self.get_value_of_manage_printers_email_printers_email_text() == u''
#         assert self.get_value_of_manage_printers_email_email_address_text() == u''
#         assert self.get_value_of_manage_printers_email_personalize_text() == u''
#         assert self.get_value_of_manage_printers_email_change_btn() == u''

    def verify_printer_connect_to_another_account_screen(self):
        '''
        This is a method to check UI strings of Printer connect to another account screen.
        :parameter:
        :return:
        '''
        self.wait_for_printer_connect_to_another_account_screen(120)
        logging.debug("Start to check UI strings of Printer connect to another account screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='printer_connected_to_another_account_screen')
        assert self.get_value_of_printer_connect_to_another_account_title() == test_strings['printer_connect_to_another_account_title']
        assert self.get_value_of_printer_connect_to_another_account_content() == test_strings['printer_connect_to_another_account_content']
        assert self.get_value_of_printer_connect_to_another_account_ok_btn() == test_strings['printer_connect_to_another_account_ok_btn']

    def verify_hp_account_unavailable_dialog(self):
        '''
        This is a method to check UI strings of HP Account Unavailable dialog.
        :parameter:
        :return:
        '''
        self.wait_for_hp_account_unavailable_dialog_load()
        logging.debug("Start to check UI strings of HP Account Unavailable dialog")
#         assert self.get_value_of_hp_account_unavailable_title() == u""
#         assert self.get_value_of_hp_account_unavailable_content() == u""
#         assert self.get_value_of_hp_account_unavailable_cancel_btn() == u""
#         assert self.get_value_of_hp_account_unavailable_try_again_btn() == u""
