# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Install driver to print screen

@author: Ivan
@create_date: Aug 12, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class InstallDriverToPrint(SmartScreens):

    folder_name = "oobe"
    flow_name = "install_driver_to_print"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InstallDriverToPrint, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Install driver to print screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("add_content", timeout=timeout, raise_e=raise_e)

    def wait_for_install_success_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Success print installed dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[wait_for_install_success_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_can_now_print_to_contents", timeout=timeout, raise_e=raise_e)

    def get_value_of_install_driver_to_print_title(self):
        '''
        This is a method to get the value of Install driver to print screen title.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_install_driver_to_print_title]-Get the contents of screen title...  ")

        return self.driver.get_value("install_driver_to_print_title")

    def get_value_of_launch_title(self):
        '''
        This is a method to get the value of Launch title on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_launch_title]-Get the contents of Launch title...  ")

        return self.driver.get_value("launch_title")

    def get_value_of_launch_content_1(self):
        '''
        This is a method to get the value of Launch content - 1 on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_launch_content_1]-Get the contents of Launch content - 1...  ")

        return self.driver.get_value("launch_content_1")

    def get_value_of_launch_content_2(self):
        '''
        This is a method to get the value of Launch content - 2 on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_launch_content_2]-Get the contents of Launch content - 2...  ")

        return self.driver.get_value("launch_content_2")

    def get_value_of_launch_content_3(self):
        '''
        This is a method to get the value of Launch content - 3 on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_launch_content_3]-Get the contents of Launch content - 3...  ")

        return self.driver.get_value("launch_content_3")

    def get_value_of_select_title(self):
        '''
        This is a method to get the value of Select title on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_select_title]-Get the contents of Select title...  ")

        return self.driver.get_value("select_title")

    def get_value_of_select_content(self):
        '''
        This is a method to get the value of Select content on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_select_content]-Get the contents of Select content...  ")

        return self.driver.get_value("select_content")

    def get_value_of_add_title(self):
        '''
        This is a method to get the value of Add title on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_add_title]-Get the contents of Add title...  ")

        return self.driver.get_value("add_title")

    def get_value_of_add_content(self):
        '''
        This is a method to get the value of Add content on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_add_content]-Get the contents of Add content...  ")

        return self.driver.get_value("add_content")

    def get_value_of_printers_scanners_btn(self):
        '''
        This is a method to get the value of Printers & Scanners button on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_printers_scanners_btn]-Get the contents of Printers & Scanners button...  ")

        return self.driver.get_title("printers_scanners_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("continue_btn")

    def get_value_of_success_print_installed_contents(self):
        '''
        This is a method to get value of Success print installed dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_success_print_installed_contents]-Get the contents of Success print installed dialog content...  ")

        return self.driver.get_value("success_print_installed_contents")

    def get_value_of_you_can_now_print_to_contents(self):
        '''
        This is a method to get value of Success print installed dialog content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_you_can_now_print_to_contents]-Get the contents of Success print installed dialog content - 1...  ")

        return self.driver.get_value("you_can_now_print_to_contents")

    def get_value_of_ok_button(self):
        '''
        This is a method to get value of OK button on Success print install dialog.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_ok_button]-Get the contents of OK button...  ")

        return self.driver.get_title("ok_button")

    def click_ok_btn(self):
        '''
        This is a method to click OK button on Success print installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[click_ok_btn_install_driver_to_print]-Click OK button... ")

        self.driver.click("ok_button")

    def click_printers_scanners_btn(self):
        '''
        This is a method to click Printers & Scanners button on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[DeleteUSBPrinter]:[click_printers_scanners_btn]-Click Printers & Scanners button... ")

        self.driver.click("printers_scanners_btn")

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Install driver to print screen.
        :parameter:
        :return:
        '''
        logging.debug("[DeleteUSBPrinter]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn")

# -------------------------------Verification Methods--------------------------
    def verify_install_driver_to_print_screen(self, printer_name):
        '''
        This is a verification method to check UI strings of Install driver to print screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to verify UI string of Install driver to print screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='install_driver_to_print')
        assert self.get_value_of_install_driver_to_print_title() == test_strings['install_driver_to_print_title']
        assert self.get_value_of_launch_title() == test_strings['launch_title']
        assert self.get_value_of_launch_content_1() == test_strings['launch_content_1']
        assert self.get_value_of_launch_content_2() == test_strings['launch_content_2']
        assert self.get_value_of_launch_content_3() == test_strings['launch_content_3']
        assert self.get_value_of_select_title() == test_strings['select_title']
        assert self.get_value_of_select_content() == test_strings['select_content']
        assert self.get_value_of_add_title() == test_strings['add_title']
        sleep(5)
        assert self.get_value_of_add_content() == test_strings['add_content_1'] + "[" + printer_name + "]" + test_strings['add_content_2']
        assert self.get_value_of_printers_scanners_btn() == test_strings['printers_scanners_btn']
        assert self.get_value_of_continue_btn() == test_strings['continue_btn']

    def verify_success_print_installed_dialog(self):
        '''
        This is a verification method to check UI strings of Success print installed dialog.
        :parameter:
        :return:
        '''
        self.wait_for_install_success_screen_load(300)
        self.driver.wait_for_object("successful_image", timeout=10, raise_e=True)
        logging.debug("Start to verify UI string of Success print installed dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='install_driver_to_print')
        assert self.get_value_of_success_print_installed_contents() == test_strings['success_print_installed_contents']
        assert test_strings['you_can_now_print_to_contents_1'] and test_strings['you_can_now_print_to_contents_2'] in self.get_value_of_you_can_now_print_to_contents()
        assert self.get_value_of_ok_button() == test_strings['ok_button']
