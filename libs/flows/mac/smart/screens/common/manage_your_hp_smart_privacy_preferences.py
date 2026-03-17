# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the Manage your HP Smart privacy preferences screen.

@author: ten
@create_date: Jun 7, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.webapp.web_app_screen import WebAppScreen
from time import sleep
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.resources.const.mac.const as smart_const


class ManagePreferences(SmartScreens):
    folder_name = "common"
    flow_name = "manage_your_hp_smart_privacy_preferences"

    def __init__(self, driver):
        super(ManagePreferences, self).__init__(driver)
        self.web_app_screen = WebAppScreen(self.driver)

# -----------------------------Operate Elements-----------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[Manage_Preferences]:[wait_for_screen_load]-Wait for screen loading ...")

        return self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_from_printer_settings(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[Manage_Preferences]:[wait_for_screen_load]-Wait for screen loading ...")

        return self.driver.wait_for_object("save_btn", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click continue_btn on Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_continue_btn]-Click save_btn... ")

        self.driver.click("continue_btn", is_native_event=True)

    def click_back_btn(self):
        '''
        This is a method to click back_btnon Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_back_btn]-Click back_btn... ")

        self.driver.click("back_btn", is_native_event=True)

    def click_back_btn_from_printer_settings(self):
        '''
        This is a method to click back_btnon Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_back_btn]-Click back_btn... ")

        self.driver.click("back_btn_from_printer_settings", is_native_event=True)

    def click_google_analytics_link(self):
        '''
        This is a method to click google_analytics_link on Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_google_analytics_link]-Click google_analytics_link... ")

        self.driver.click("google_analytics_link")

    def click_adobe_analytics_link(self):
        '''
        This is a method to click adobe_analytics_linkon Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_adobe_analytics_link]-Click adobe_analytics_link... ")

        self.driver.click("adobe_analytics_link")
  
    def click_optimizely_link(self):
        '''
        This is a method to click optimizely_link on Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_optimizely_link]-Click optimizely_link... ")

        self.driver.click("optimizely_link")

    def click_learn_more_link(self):
        '''
        This is a method to click learn_more_link on Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_learn_more_link]-Click learn_more_link... ")

        self.driver.click("learn_more_link")

    def click_hp_smart_terms_of_use_link(self):
        '''
        This is a method to click hp_smart_terms_of_use_linkon Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_hp_smart_terms_of_use_link]-Click hp_smart_terms_of_use_link... ")

        self.driver.click("hp_smart_terms_of_use_link")

    def click_end_user_license_agreement_link(self):
        '''
        This is a method to click end_user_license_link on Manage your HP Smart privacy preferences screen.
        :parameter:
        :return:
        '''
        logging.debug("[Manage_Preferences]:[click_end_user_license_link]-Click end_user_license_link... ")

        self.driver.click("end_user_license_agreement_link")

#   ----------------------------Verification Methods----------------------------------------------

    def verify_google_analytics_link(self):
        '''
        This is a verification method to check google_analytics_link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_google_analytics_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.google.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_adobe_analytics_link(self):
        '''
        This is a verification method to check adobe_analytics_link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_adobe_analytics_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.adobe.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_optimizely_link(self):
        '''
        This is a verification method to Optimizely link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_optimizely_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.optimizely.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_learn_more_link(self):
        '''
        This is a verification method to check learn more link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_learn_more_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.hp-smart.cn' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_hp_smart_terms_of_use_link(self):
        '''
        This is a verification method to check adobe privacy link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_hp_smart_terms_of_use_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.hp-smart.cn' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_end_user_license_agreement_link(self):
        '''
        This is a verification method to check adobe privacy link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_end_user_license_agreement_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://support.hp.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_all_the_link(self):
        '''
        This is a verification method to check all the link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("check all the link")
        self.driver.scroll_on_app()
        sleep(2)
        self.verify_google_analytics_link()
        self.verify_adobe_analytics_link()
        self.verify_optimizely_link()
        self.verify_learn_more_link()
        self.verify_hp_smart_terms_of_use_link()
        self.verify_end_user_license_agreement_link()

