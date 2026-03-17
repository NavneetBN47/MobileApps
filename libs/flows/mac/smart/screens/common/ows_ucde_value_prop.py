# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on ows ucde value prop screen

@author: ten
@create_date: Nov 11, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class OwsUcdeValueProp(SmartScreens):

    folder_name = "common"
    flow_name = "ows_ucde_value_prop"

    def __init__(self, driver):
        super(OwsUcdeValueProp, self).__init__(driver)

#   -----------------------------Operate Elements------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[OwsUcdeValueProp]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("close_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_screen_content_1(self):
        '''
        This is a method to get value of screen_content_1
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("screen_content_1")

    def get_value_of_screen_content_2(self):
        '''
        This is a method to get value of screen_content_2
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("screen_content_2")

    def get_value_of_create_account_btn(self):
        '''
        This is a method to get value of create_account_btn
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[get_value_of_create_account_btn]-Get the contents of create_account_btn ...  ")

        return self.driver.get_title("create_account_btn")

    def get_value_of_sign_in_btn(self):
        '''
        This is a method to get value of sign_in_btn
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[get_value_of_sign_in_btn]-Get the contents of sign_in_btn ...  ")

        return self.driver.get_title("sign_in_btn")

    def get_value_of_close_btn(self):
        '''
        This is a method to get value of close_btn
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[get_value_of_close_btn]-Get the contents of close_btn ...  ")

        return self.driver.get_value("close_btn")

    def click_create_account_btn(self):
        '''
        This is a method to click create account button on Ows Ucde Value Prop.
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[click_create_account_btn]-Click create account button... ")

        self.driver.click("create_account_btn")

    def click_sign_in_btn(self):
        '''
        This is a method to click sign in button on Ows Ucde Value Prop.
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[click_sign_in_btn]-Click sign in button... ")

        self.driver.click("sign_in_btn")

    def click_close_btn(self):
        '''
        This is a method to click close button on Ows Ucde Value Prop.
        :parameter:
        :return:
        '''
        logging.debug("[OwsUcdeValueProp]:[click_close_btn]-Click close button... ")

        self.driver.click("close_btn")

#   ----------------------------Verification Methods------------------------------------------
    def verify_ows_ucde_value_prop_screen_button_strings(self):
        '''
        This is a verification method to check UI strings of Create account btn/Sign in btn/Close btn on OWS UCDE Value Prop screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of Create account btn/Sign in btn/Close btn on OWS UCDE Value Prop screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')
        assert self.get_value_of_create_account_btn() == test_strings['create_account_btn']
        assert self.get_value_of_sign_in_btn() == test_strings['sign_in_btn']
        assert self.get_value_of_close_btn() == test_strings['close_btn']

    def verify_ows_ucde_value_prop_screen_for_scan(self):
        '''
        This is a verification method to check UI strings of OWS UCDE Value Prop screen after clicking Scan tile on Main Page.
        :parameter:
        :return:
        '''
        self.verify_ows_ucde_value_prop_screen_button_strings()
        logging.debug("Start to check UI strings of OWS UCDE Value Prop screen after clicking Scan tile on Main Page")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')
        assert self.get_value_of_screen_content_1() == test_strings['content1_with_scan']
        assert self.get_value_of_screen_content_2() == test_strings['content2_with_scan']

    def verify_ows_ucde_value_prop_screen_for_print_document(self):
        '''
        This is a verification method to check UI strings of OWS UCDE Value Prop screen after clicking Print Document tile on Main Page.
        :parameter:
        :return:
        '''
        self.verify_ows_ucde_value_prop_screen_button_strings()
        logging.debug("Start to check UI strings of OWS UCDE Value Prop screen after clicking Print Document tile on Main Page")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')
        assert self.get_value_of_screen_content_1() == test_strings['content1_with_print_doc']
        assert self.get_value_of_screen_content_2() == test_strings['content2_with_print_doc']

    def verify_ows_ucde_value_prop_screen_for_print_photo(self):
        '''
        This is a verification method to check UI strings of OWS UCDE Value Prop screen after clicking Print Photo tile on Main Page.
        :parameter:
        :return:
        '''
        self.verify_ows_ucde_value_prop_screen_button_strings()
        logging.debug("Start to check UI strings of OWS UCDE Value Prop screen after clicking Print Photo tile on Main Page")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')
        assert self.get_value_of_screen_content_1() == test_strings['content1_with_print_photo']
        assert self.get_value_of_screen_content_2() == test_strings['content2_with_print_photo']

    def verify_ows_ucde_value_prop_screen_for_shortcuts(self):
        '''
        This is a verification method to check UI strings of OWS UCDE Value Prop screen after clicking Shortcuts tile on Main Page.
        :parameter:
        :return:
        '''
        self.verify_ows_ucde_value_prop_screen_button_strings()
        logging.debug("Start to check UI strings of OWS UCDE Value Prop screen after clicking Shortcuts tile on Main Page")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')
        assert self.get_value_of_screen_content_1() == test_strings['content1_with_shortcuts']
        assert self.get_value_of_screen_content_2() == test_strings['content2_with_shortcuts']

    def verify_ows_ucde_value_prop_screen_for_mobile_fax(self):
        '''
        This is a verification method to check UI strings of OWS UCDE Value Prop screen after clicking Mobile Fax tile on Main Page.
        :parameter:
        :return:
        '''
        self.verify_ows_ucde_value_prop_screen_button_strings()
        logging.debug("Start to check UI strings of OWS UCDE Value Prop screen after clicking Mobile Fax tile on Main Page")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='ows_ucde_value_prop')

        assert self.get_value_of_screen_content_1() == test_strings['content1_with_mobile_fax']
        assert self.get_value_of_screen_content_2() == test_strings['content2_with_mobile_fax']
