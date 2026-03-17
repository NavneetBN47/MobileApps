# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for the Install Printer dialog.

@author: Ivan
@create_date: Jul 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility

class InstallPrinterDialog(SmartScreens):
    folder_name = "common"
    flow_name = "install_printer_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InstallPrinterDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("install_printer_dialog_install_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_success_printer_installed_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Success Printer Installed dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_success_printer_installed_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("success_printer_installed_dialog_ok_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_failed_printer_installed_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Failed Printer Installed dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_failed_printer_installed_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("failed_printer_installed_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_install_printer_dialog_later_btn(self):
        '''
        This is a method to click I'll do this later button on Install Printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_install_printer_dialog_later_btn]-Click I'll do this later button... ")

        self.driver.click("install_printer_dialog_later_btn", is_native_event=True)

    def click_install_printer_dialog_install_btn(self):
        '''
        This is a method to click Install Printer button on Install Printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_install_printer_dialog_install_btn]-Click Install Printer button... ")

        self.driver.click("install_printer_dialog_install_btn", is_native_event=True)

    def click_success_printer_installed_dialog_ok_btn(self):
        '''
        This is a method to click OK button on Success Printer installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_success_printer_installed_dialog_ok_btn]-Click OK button... ")

        self.driver.click("success_printer_installed_dialog_ok_btn", is_native_event=True)

    def click_failed_printer_installed_dialog_later_btn(self):
        '''
        This is a method to click I'll do this later button on Failed Printer installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_failed_printer_installed_dialog_later_btn]-Click I'll do this later button... ")

        self.driver.click("failed_printer_installed_dialog_later_btn", is_native_event=True)

    def click_failed_printer_installed_dialog_printer_scanners_btn(self):
        '''
        This is a method to click Printer & Scanners button on Failed Printer installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_failed_printer_installed_dialog_printer_scanners_btn]-Click Printer & Scanners button... ")

        self.driver.click("failed_printer_installed_dialog_printer_scanners_btn", is_native_event=True)

    def get_value_of_install_printer_dialog_title(self):
        '''
        This is a method to get value of Install Printer Dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_printer_dialog_title]-Get value of Install Printer Dialog title...  ")

        return self.driver.get_value("install_printer_dialog_title")

    def get_value_of_install_printer_dialog_content(self):
        '''
        This is a method to get value of Install Printer Dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_printer_dialog_content]-Get value of Install Printer Dialog content...  ")

        return self.driver.get_value("install_printer_dialog_content")

    def get_value_of_install_printer_dialog_check_box(self):
        '''
        This is a method to get value of check box text on Install Printer Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_printer_dialog_check_box]-Get value of check box text...  ")

        return self.driver.get_title("install_printer_dialog_check_box")

    def get_value_of_install_printer_dialog_later_btn(self):
        '''
        This is a method to get value of I'll do this Later button on Install Printer Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_printer_dialog_later_btn]-Get value of I'll do this Later button...  ")

        return self.driver.get_title("install_printer_dialog_later_btn")

    def get_value_of_install_printer_dialog_install_btn(self):
        '''
        This is a method to get value of Install Printer button on Install Printer Dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_printer_dialog_install_btn]-Get value of Install Printer button...  ")

        return self.driver.get_title("install_printer_dialog_install_btn")

    def get_value_of_success_printer_installed_dialog_title(self):
        '''
        This is a method to get value of Success Printer Installed dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_success_printer_installed_dialog_title]-Get value of Success Printer Installed dialog title...  ")

        return self.driver.get_value("success_printer_installed_dialog_title")

    def get_value_of_success_printer_installed_dialog_content(self):
        '''
        This is a method to get value of Success Printer Installed dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_success_printer_installed_dialog_content]-Get value of Success Printer Installed dialog content...  ")

        return self.driver.get_value("success_printer_installed_dialog_content")

    def get_value_of_success_printer_installed_dialog_ok_btn(self):
        '''
        This is a method to get value of OK button on Success Printer Installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_success_printer_installed_dialog_ok_btn]-Get value of Success Printer Installed dialog title...  ")

        return self.driver.get_title("success_printer_installed_dialog_ok_btn")

    def get_value_of_failed_printer_installed_dialog_title(self):
        '''
        This is a method to get value of Failed Printer Installed dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_failed_printer_installed_dialog_title]-Get value of Failed Printer Installed dialog title...  ")

        return self.driver.get_value("failed_printer_installed_dialog_title")

    def get_value_of_failed_printer_installed_dialog_later_btn(self):
        '''
        This is a method to get value of I'll do this later button on Failed Printer Installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_failed_printer_installed_dialog_later_btn]-Get value of I'll do this later button...  ")

        return self.driver.get_title("failed_printer_installed_dialog_later_btn")

    def get_value_of_failed_printer_installed_dialog_printer_scanners_btn(self):
        '''
        This is a method to get value of Printer & Scanners button on Failed Printer Installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_failed_printer_installed_dialog_printer_scanners_btn]-Get value of Printer & Scanners button...  ")

        return self.driver.get_title("failed_printer_installed_dialog_printer_scanners_btn")

# -------------------------------Verification Methods--------------------------
    def verify_install_printer_dialog(self):
        '''
        This is a verification method to check UI strings of Install Printer Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Install Printer Dialog")
#         assert self.get_value_of_install_printer_dialog_title() == ""
#         assert self.get_value_of_install_printer_dialog_content() == ""
#         assert self.get_value_of_install_printer_dialog_check_box() == ""
#         assert self.get_value_of_install_printer_dialog_later_btn() == ""
#         assert self.get_value_of_install_printer_dialog_install_btn() == ""

    def verify_install_printer_dialog_disappear(self, timeout=3):
        '''
        This is a verification method to verify Install Printer Dialog disappear.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("install_printer_dialog_content", timeout=timeout, raise_e=False)

    def verify_success_printer_installed_dialog(self):
        '''
        This is a verification method to check UI strings of Success Printer Installed Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_success_printer_installed_dialog_load()
        logging.debug("Start to check UI strings of Success Printer Installed Dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='install_printer_dialog')
        assert self.get_value_of_success_printer_installed_dialog_title() == test_strings['success_dialog_title']
        assert self.get_value_of_success_printer_installed_dialog_ok_btn() == test_strings['ok_btn']

    def verify_success_printer_installed_dialog_disappear(self, timeout=3):
        '''
        This is a verification method to verify Success Printer Installed Dialog disappear.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("success_printer_installed_dialog_content", timeout=timeout, raise_e=False)

    def verify_failed_printer_installed_dialog(self):
        '''
        This is a verification method to check UI strings of Failed Printer Installed Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_failed_printer_installed_dialog_load()
        logging.debug("Start to check UI strings of Failed Printer Installed Dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='install_printer_dialog')
        assert self.get_value_of_failed_printer_installed_dialog_title() == test_strings['failed_dialog_title']
        assert self.get_value_of_failed_printer_installed_dialog_later_btn() == test_strings['later_btn']
        assert self.get_value_of_failed_printer_installed_dialog_printer_scanners_btn() == test_strings['printer_scanners_btn']

    def verify_failed_printer_installed_dialog_disappear(self, timeout=3):
        '''
        This is a verification method to verify Failed Printer Installed Dialog disappear.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("failed_printer_installed_dialog_title", timeout=timeout, raise_e=False)
