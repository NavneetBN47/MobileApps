# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on screens during OWS_Yeti flow.

@author: Ivan
@create_date: Oct 23, 2020
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from time import sleep


class OWS_Yeti(SmartScreens):
    folder_name = "oobe"
    flow_name = "ows_yeti"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(OWS_Yeti, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self):
        '''
        This is a method to wait for screen loaded.
        :parameter:
        :return:
        '''
        pass

    def wait_for_select_your_country_or_region_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Select your country or region screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_select_your_country_or_region_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("select_your_country_or_region_content", timeout=timeout, raise_e=raise_e)

    def wait_for_set_printer_language_and_country_or_region_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Set printer language and country or region screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_set_printer_language_and_country_or_region_screen__load]-Wait for screen loading... ")

        return self.driver.wait_for_object("set_printer_language_and_country_or_region_screen_language_textfield", timeout=timeout, raise_e=raise_e)

    def wait_for_get_more_value_from_your_printing_experience_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Get more value from your printing experience screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_get_more_value_from_your_printing_experience_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_thank_you_for_choosing_hp_plus_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Thank you for choosing HP+ screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_thank_you_for_choosing_hp_plus_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("get_more_value_from_your_printing_experience_learn_more_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_create_hp_account_or_sign_in_to_register_your_printer_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Create an HP account or sign in to register your printer screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_get_more_value_from_your_printing_experience_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_get_more_value_from_your_printing_experience_title(self):
        '''
        This is a method to get the value of Get more value from your printing experience screen title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_get_more_value_from_your_printing_experience_title]-Get the value of screen title... ")

        return self.driver.get_title("get_more_value_from_your_printing_experience_title")

    def get_value_of_get_more_value_from_your_printing_experience_content(self):
        '''
        This is a method to get the value of Get more value from your printing experience screen content.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_get_more_value_from_your_printing_experience_content]-Get the value of screen content... ")

        return self.driver.get_title("get_more_value_from_your_printing_experience_content")

    def get_value_of_get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn(self):
        '''
        This is a method to get the value of Do not Activate HP+ button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_get_more_value_from_your_printing_experience_title]-Get the value of Do not Activate HP+ button... ")

        return self.driver.get_title("get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn")

    def get_value_of_get_more_value_from_your_printing_experience_learn_more_btn(self):
        '''
        This is a method to get the value of Learn More button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_get_more_value_from_your_printing_experience_title]-Get the value of Learn More button... ")

        return self.driver.get_title("get_more_value_from_your_printing_experience_learn_more_btn")

    def get_value_of_get_more_value_from_your_printing_experience_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_get_more_value_from_your_printing_experience_title]-Get the value of Continue button... ")

        return self.driver.get_title("get_more_value_from_your_printing_experience_continue_btn")

    def click_select_your_country_or_region_first_item(self):
        '''
        This is a method to Select first item on Select your country or region screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_select_your_country_or_region_first_item]-Select the first country item... ")

        self.driver.click("select_your_country_or_region_first_item", is_native_event=True)

    def click_select_your_country_or_region_united_states_item(self):
        '''
        This is a method to Select United States item on Select your country or region screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_select_your_country_or_region_united_states_item]-Select United States item... ")
#         self.driver.scroll_on_app()

        sleep(2)
        self.driver.click("select_your_country_or_region_united_states_item", is_native_event=True)

    def click_select_your_country_or_region_continue_btn(self):
        '''
        This is a method to click Continue button on Select your country or region screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_select_your_country_or_region_continue_btn]-Click Continue button... ")

        self.driver.click("select_your_country_or_region_continue_btn", is_native_event=True)

    def click_set_printer_language_and_country_or_region_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Set printer language and country or region screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_set_printer_language_and_country_or_region_screen_continue_btn]-Click Continue button... ")

        self.driver.click("set_printer_language_and_country_or_region_screen_continue_btn", is_native_event=True)

    def click_get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn(self):
        '''
        This is a method to click Do not Activate HP+ button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn]-Click Do not Activate HP+ button... ")

        self.driver.click("get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn", is_native_event=True)

    def click_get_more_value_from_your_printing_experience_learn_more_btn(self):
        '''
        This is a method to click Learn More button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_get_more_value_from_your_printing_experience_learn_more_btn]-Click Learn More button... ")

        self.driver.click("get_more_value_from_your_printing_experience_learn_more_btn", is_native_event=True)

    def click_get_more_value_from_your_printing_experience_continue_btn(self):
        '''
        This is a method to click Continue button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_get_more_value_from_your_printing_experience_continue_btn]-Click Continue button... ")

        self.driver.click("get_more_value_from_your_printing_experience_continue_btn", is_native_event=True)

    def click_sign_in_btn(self):
        '''
        This is a method to click sign_in_btn on Create an HP account or sign in to register your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_sign_in_btn]-Click sign_in_btn button... ")

        self.driver.click("sign_in_btn", is_native_event=True)

    def click_create_account_btn(self):
        '''
        This is a method to click create_account_btn on Create an HP account or sign in to register your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_create_account_btn]-Click create_account_btn... ")

        self.driver.click("create_account_btn", is_native_event=True)

    def click_skip_warranty_and_account_activation_btn(self):
        '''
        This is a method to click skip_warranty_and_account_activation_btn on Create an HP account or sign in to register your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_skip_warranty_and_account_activation_btn]-Click skip_warranty_and_account_activation_btn... ")

        self.driver.click("skip_warranty_and_account_activation_btn", is_native_event=True)

    def wait_for_your_printer_to_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for your_printer_to_dialog screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_your_printer_to_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("for_your_printer_to_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_are_you_sure_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Are you sure you don't want to activate HP+? dialog load after click continue button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_are_you_sure_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("are_you_sure_dialog_decline_hp_plus_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_are_you_sure_dialog_title(self):
        '''
        This is a method to get the value of Are you sure you don't want to activate HP+? dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_title]-Get the value of dialog title... ")

        return self.driver.get_value("are_you_sure_dialog_title")

    def get_value_of_are_you_sure_dialog_content_you_will_only(self):
        '''
        This is a method to get the value of You will only get... text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_you_will_only]-Get the value of You will only get... text... ")

        return self.driver.get_value("are_you_sure_dialog_content_you_will_only")

    def get_value_of_are_you_sure_dialog_content_six_free_months(self):
        '''
        This is a method to get the value of Six free months... text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_six_free_months]-Get the value of Six free months... text... ")

        return self.driver.get_value("are_you_sure_dialog_content_six_free_months")

    def get_value_of_are_you_sure_dialog_content_an_additional_year(self):
        '''
        This is a method to get the value of An additional year... text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_an_additional_year]-Get the value of An additional year... text... ")

        return self.driver.get_value("are_you_sure_dialog_content_an_additional_year")

    def get_value_of_are_you_sure_dialog_content_access_to_exclusive(self):
        '''
        This is a method to get the value of Access to exclusive... text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_access_to_exclusive]-Get the value of Access to exclusive... text... ")

        return self.driver.get_value("are_you_sure_dialog_content_access_to_exclusive")

    def get_value_of_are_you_sure_dialog_content_join_hp_to_keep(self):
        '''
        This is a method to get the value of Join HP to keep... text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_join_hp_to_keep]-Get the value of Join HP to keep... text... ")

        return self.driver.get_value("are_you_sure_dialog_content_join_hp_to_keep")

    def get_value_of_are_you_sure_dialog_content_select(self):
        '''
        This is a method to get the value of Select text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_select]-Get the value of Continue button... ")

        return self.driver.get_value("are_you_sure_dialog_content_select")

    def get_value_of_are_you_sure_dialog_content_back_to_offer(self):
        '''
        This is a method to get the value of Back to offer text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_back_to_offer]-Get the value of Continue button... ")

        return self.driver.get_value("are_you_sure_dialog_content_back_to_offer")

    def get_value_of_are_you_sure_dialog_content_to_reconsider(self):
        '''
        This is a method to get the value of to reconsider text on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_content_to_reconsider]-Get the value of Continue button... ")

        return self.driver.get_value("are_you_sure_dialog_content_to_reconsider")

    def get_value_of_are_you_sure_dialog_back_to_offer_btn(self):
        '''
        This is a method to get the value of Back to offer button on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_back_to_offer_btn]-Get the value of Continue button... ")

        return self.driver.get_title("are_you_sure_dialog_back_to_offer_btn")

    def get_value_of_are_you_sure_dialog_decline_hp_plus_btn(self):
        '''
        This is a method to get the value of Decline HP+ button on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_are_you_sure_dialog_decline_hp_plus_btn]-Get the value of Continue button... ")

        return self.driver.get_title("are_you_sure_dialog_decline_hp_plus_btn")

    def click_are_you_sure_dialog_back_to_offer_btn(self):
        '''
        This is a method to click Back to offer button on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_are_you_sure_dialog_back_to_offer_btn]-Click Back to offer button... ")

        self.driver.click("are_you_sure_dialog_back_to_offer_btn", is_native_event=True)

    def click_are_you_sure_dialog_title(self):
        '''
        This is a method to click Are you sure you don't want to activate HP+? dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_are_you_sure_dialog_title]-Click screen title... ")

        self.driver.click("are_you_sure_dialog_content_you_will_only", is_native_event=True)

    def click_are_you_sure_dialog_decline_hp_plus_btn(self):
        '''
        This is a method to click Decline HP+ button on Are you sure you don't want to activate HP+? dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_are_you_sure_dialog_decline_hp_plus_btn]-Click Decline HP+ button... ")
#         self.driver.scroll_on_app()
        sleep(1)
        self.driver.click("are_you_sure_dialog_decline_hp_plus_btn", is_native_event=True)

    def wait_for_printer_dynamic_security_notice_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Printer Dynamic Security notice screen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_printer_dynamic_security_notice_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_dynamic_security_notice_screen_continue_btn", timeout=timeout, raise_e=raise_e)

    def click_printer_dynamic_security_notice_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Printer Dynamic Security notice screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_printer_dynamic_security_notice_screen_continue_btn]-Click Continue button... ")

        self.driver.click("printer_dynamic_security_notice_screen_continue_btn", is_native_event=True)

    def click_activate_HP_btn(self):
        '''
        This is a method to click activate_HP_btn.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_activate_HP_btn]-Click Activate HP+ button... ")
#         self.driver.scroll_on_app()
        sleep(1)
        self.driver.click("activate_HP_btn", is_native_event=True)

    def wait_for_learn_more_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Learn more screen load after click Learn More button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_learn_more_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("learn_more_screen_hp_plus_overview", timeout=timeout, raise_e=raise_e)

    def get_value_of_learn_more_screen_title(self):
        '''
        This is a method to get the value of Learn more screen title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_title]-Get the value of Learn more screen title... ")

        return self.driver.get_value("learn_more_screen_title")

    def get_value_of_learn_more_screen_hp_plus_overview(self):
        '''
        This is a method to get the value of HP+ Overview text on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_hp_plus_overview]-Get the value of HP+ Overview text... ")

        return self.driver.get_value("learn_more_screen_hp_plus_overview")

    def get_value_of_learn_more_screen_hp_plus_requirements(self):
        '''
        This is a method to get the value of HP+ Requirements text on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_hp_plus_requirements]-Get the value of HP+ Requirements text... ")

        return self.driver.get_value("learn_more_screen_hp_plus_requirements")

    def get_value_of_learn_more_screen_print_plans(self):
        '''
        This is a method to get the value of Print Plans text on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_print_plans]-Get the value of Print Plans text... ")

        return self.driver.get_value("learn_more_screen_print_plans")

    def get_value_of_learn_more_screen_forest_first_printing(self):
        '''
        This is a method to get the value of Forest First Printing text on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_forest_first_printing]-Get the value of Forest First Printing text... ")

        return self.driver.get_value("learn_more_screen_forest_first_printing")

    def get_value_of_learn_more_screen_back_btn(self):
        '''
        This is a method to get the value of Back button on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_learn_more_screen_back_btn]-Get the value of Back button... ")

        return self.driver.get_title("learn_more_screen_back_btn")

    def click_learn_more_screen_back_btn(self):
        '''
        This is a method to click Back button on Learn more screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_learn_more_screen_back_btn]-Click Back button... ")

        self.driver.click("learn_more_screen_back_btn", is_native_event=True)

    def wait_for_you_agree_to_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for "For your printer to operate after activating HP+, you agree to" dialog load after click skip button on Get more value from your printing experience screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_you_agree_to_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_agree_to_dialog_content_by_activating", timeout=timeout, raise_e=raise_e)

    def get_value_of_you_agree_to_dialog_title(self):
        '''
        This is a method to get the value of "For your printer to operate after activating HP+, you agree to" dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_title]-Get the value of dialog title... ")

        return self.driver.get_value("you_agree_to_dialog_title")

    def get_value_of_you_agree_to_dialog_content_sign_in(self):
        '''
        This is a method to get the value of Sign in text on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_content_sign_in]-Get the value of Sign in text... ")

        return self.driver.get_value("you_agree_to_dialog_content_sign_in")

    def get_value_of_you_agree_to_dialog_content_connect_your_printer(self):
        '''
        This is a method to get the value of Connect your printer text on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_content_connect_your_printer]-Get the value of Connect your printer text... ")

        return self.driver.get_value("you_agree_to_dialog_content_connect_your_printer")

    def get_value_of_you_agree_to_dialog_content_use_only(self):
        '''
        This is a method to get the value of Use only text on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_content_use_only]-Get the value of Use only text... ")

        return self.driver.get_value("you_agree_to_dialog_content_use_only")

    def get_value_of_you_agree_to_dialog_content_by_activating(self):
        '''
        This is a method to get the value of By activating text on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_content_by_activating]-Get the value of By activating text... ")

        return self.driver.get_value("you_agree_to_dialog_content_by_activating")

    def get_value_of_you_agree_to_dialog_activate_hp_plus_btn(self):
        '''
        This is a method to get the value of Activate HP+ button on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_activate_hp_plus_btn]-Get the value of Activate HP+ button... ")

        return self.driver.get_title("you_agree_to_dialog_activate_hp_plus_btn")

    def click_you_agree_to_dialog_activate_hp_plus_btn(self):
        '''
        This is a method to click Activate HP+ button on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_you_agree_to_dialog_activate_hp_plus_btn]-Click Activate HP+ button... ")

        self.driver.click("you_agree_to_dialog_activate_hp_plus_btn", is_native_event=True)

    def wait_for_welcome_to_hp_plus_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Welcome to HP+ screen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_welcome_to_hp_plus_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("welcome_to_hp_plus_screen_content_enjoy_your", timeout=timeout, raise_e=raise_e)

    def wait_for_free_ink_plan_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Welcome to HP+ screen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_free_ink_plan_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("free_ink_plan_contents_1", timeout=timeout, raise_e=raise_e)

    def wait_for_welcome_of_flex_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Welcome to flexscreen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_welcome_to_flex_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("welcome_of_flex_screen_content_1", timeout=timeout, raise_e=raise_e)

    def wait_for_are_you_sure_to_skip_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Welcome to HP+ screen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_are_you_sure_to_skip_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("are_you_sure_to_skip_dialog_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_welcome_to_hp_plus_screen_title(self):
        '''
        This is a method to get the value of Welcome to HP+ screen title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_welcome_to_hp_plus_screen_title]-Get the value of screen title... ")

        return self.driver.get_value("welcome_to_hp_plus_screen_title")

    def get_value_of_welcome_to_hp_plus_screen_content_enjoy_your(self):
        '''
        This is a method to get the value of Enjoy your 2-year HP warranty text on Welcome to HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_welcome_to_hp_plus_screen_content_enjoy_your]-Get the value of Enjoy your 2-year HP warranty text... ")

        return self.driver.get_value("welcome_to_hp_plus_screen_content_enjoy_your")

    def get_value_of_welcome_to_hp_plus_screen_content_let_redeem(self):
        '''
        This is a method to get the value of Let's redeem your free ink text on Welcome to HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_welcome_to_hp_plus_screen_content_let_redeem]-Get the value of Let's redeem your free ink text... ")

        return self.driver.get_value("welcome_to_hp_plus_screen_content_let_redeem")

    def get_value_of_welcome_to_hp_plus_screen_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Welcome to HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_welcome_to_hp_plus_screen_continue_btn]-Get the value of Continue button... ")

        return self.driver.get_title("welcome_to_hp_plus_screen_continue_btn")

    def click_welcome_to_hp_plus_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Welcome to HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_welcome_to_hp_plus_screen_continue_btn]-Click Continue button... ")

        self.driver.click("welcome_to_hp_plus_screen_continue_btn", is_native_event=True)

    def click_welcome_screen_of_flex_continue_btn(self):
        '''
        This is a method to click Continue button on Welcome to welcome_screen_of_flex.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_welcome_screen_of_flex_continue_btn]-Click Continue button... ")

        self.driver.click("welcome_screen_of_flex_continue_btn", is_native_event=True)

    def click_free_ink_plan_skip_free_ink_btn(self):
        '''
        This is a method to click free_ink_plan_skip_free_ink_btn.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_free_ink_plan_skip_free_ink_btn]-Click Skip button... ")

        self.driver.click("free_ink_plan_skip_free_ink_btn", is_native_event=True)

    def click_free_ink_plan_continue_btn(self):
        '''
        This is a method to click free_ink_plan_continue_btn.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_free_ink_plan_continue_btn]-Click Skip button... ")

        self.driver.click("free_ink_plan_continue_btn", is_native_event=True)

    def click_yes_skip_offer_btn(self):
        '''
        This is a method to click free_ink_plan_continue_btn.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_yes_skip_offer_btn]-Click yes Skip offer button... ")

        self.driver.click("yes_skip_offer_btn", is_native_event=True)

    def wait_for_unable_to_register_the_printer_to_your_account_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Unable to Register the printer to your account screen load.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_unable_to_register_the_printer_to_your_account_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("exit_setup_btn", timeout=timeout, raise_e=raise_e)

    def click_exit_setup_btn(self):
        '''
        This is a method to click Exit Setup button on Unable to Register the printer to your account screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_exit_setup_btn]-Click Exit Setup button... ")

        self.driver.click("exit_setup_btn", is_native_event=True)
        if self.wait_for_unable_to_register_the_printer_to_your_account_screen_load(timeout=5, raise_e=False):
            self.driver.click("exit_setup_btn", is_native_event=True)

    def click_get_support_btn(self):
        '''
        This is a method to click Get Support button on Unable to Register the printer to your account screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_get_support_btn]-Click Get Support button... ")

        self.driver.click("get_support_btn", is_native_event=True)

    # For Horizon Printer
    def click_thank_you_for_choosing_hp_plus_screen_learn_more_btn(self):
        '''
        This is a method to click Learn More button on Thank you for choosing HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_thank_you_for_choosing_hp_plus_screen_learn_more_btn]-Click Learn More button... ")

        self.driver.click("get_more_value_from_your_printing_experience_learn_more_btn", is_native_event=True)

    def click_thank_you_for_choosing_hp_plus_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Thank you for choosing HP+ screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_thank_you_for_choosing_hp_plus_screen_continue_btn]-Click Continue button... ")

        self.driver.click("get_more_value_from_your_printing_experience_continue_btn", is_native_event=True)

    def wait_for_you_agree_to_dialog_for_horizon_yeti_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for "For your HP+ printer to operate, you agree to" dialog load after click Continue button on Thank you for choosing HP+ printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_you_agree_to_dialog_for_horizon_yeti_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_agree_to_dialog_for_horizon_yeti_content_by_confirming", timeout=timeout, raise_e=raise_e)

    def get_value_of_you_agree_to_dialog_for_horizon_yeti_title(self):
        '''
        This is a method to get the value of "For your HP+ printer to operate, you agree to" dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yeti_title]-Get the value of dialog title... ")

        return self.driver.get_value("you_agree_to_dialog_for_horizon_yeti_title")

    def get_value_of_you_agree_to_dialog_for_horizon_yeti_content_sign_in(self):
        '''
        This is a method to get the value of Sign in text on "For your HP+ printer to operate, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yeti_content_sign_in]-Get the value of Sign in text... ")

        return self.driver.get_value("you_agree_to_dialog_for_horizon_yeti_content_sign_in")

    def get_value_of_you_agree_to_dialog_for_horizon_yeti_content_connect_your_printer(self):
        '''
        This is a method to get the value of Connect your printer text on "For your HP+ printer to operate, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yeti_content_connect_your_printer]-Get the value of Connect your printer text... ")

        return self.driver.get_value("you_agree_to_dialog_for_horizon_yeti_content_connect_your_printer")

    def get_value_of_you_agree_to_dialog_for_horizon_yeti_content_use_only(self):
        '''
        This is a method to get the value of Use only text on "For your HP+ printer to operate, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yeti_content_use_only]-Get the value of Use only text... ")

        return self.driver.get_value("you_agree_to_dialog_for_horizon_yeti_content_use_only")

    def get_value_of_you_agree_to_dialog_for_horizon_yetig_content_by_confirming(self):
        '''
        This is a method to get the value of By confirming text on "For your HP+ printer to operate, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yetig_content_by_confirming]-Get the value of By confirming text... ")

        return self.driver.get_value("you_agree_to_dialog_for_horizon_yeti_content_by_confirming")

    def get_value_of_you_agree_to_dialog_confirm_btn(self):
        '''
        This is a method to get the value of Confirm button on "For your HP+ printer to operate, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[get_value_of_you_agree_to_dialog_for_horizon_yeti_confirm_btn]-Get the value of Confirm button... ")

        return self.driver.get_title("you_agree_to_dialog_for_horizon_yeti_confirm_btn")

    def click_you_agree_to_dialog_for_horizon_yeti_confirm_btn(self):
        '''
        This is a method to click Confirm button on "For your printer to operate after activating HP+, you agree to" dialog.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_you_agree_to_dialog_for_horizon_yeti_confirm_btn]-Click Confirm button... ")

        self.driver.click("you_agree_to_dialog_for_horizon_yeti_confirm_btn", is_native_event=True)

    def wait_for_activate_hp_plus_for_smart_printing_capabilities_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Activate HP+ for smart printing capabilities screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_activate_hp_plus_for_smart_printing_capabilities_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activate_hp_plus_for_smart_printing_capabilities_screen_do_not_activate_hp_plus_btn", timeout=timeout, raise_e=raise_e)

    def click_activate_hp_plus_for_smart_printing_capabilities_screen_do_not_activate_hp_plus_btn(self):
        '''
        This is a method to click Do not activate HP+ button on Activate HP+ for smart printing capabilities screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_activate_hp_plus_for_smart_printing_capabilities_screen_do_not_acTivate_hp_plus_btn]-Click Do not activate HP+ button... ")

        self.driver.click("activate_hp_plus_for_smart_printing_capabilities_screen_do_not_activate_hp_plus_btn", is_native_event=True)

    def click_activate_hp_plus_for_smart_printing_capabilities_screen_learn_more_btn(self):
        '''
        This is a method to click Learn more button on Activate HP+ for smart printing capabilities screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_activate_hp_plus_for_smart_printing_capabilities_screen_learn_more_btn]-Click Learn more button... ")

        self.driver.click("activate_hp_plus_for_smart_printing_capabilities_screen_learn_more_btn", is_native_event=True)

    def click_activate_hp_plus_for_smart_printing_capabilities_screen_continue_btn(self):
        '''
        This is a method to click Continue button on Activate HP+ for smart printing capabilities screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_activate_hp_plus_for_smart_printing_capabilities_screen_continue_btn]-Click Do not activate HP+ button... ")

        self.driver.click("activate_hp_plus_for_smart_printing_capabilities_screen_continue_btn", is_native_event=True)

    def wait_for_by_activating_hp_plus_you_agree_to_the_following_requirements_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for By activating HP+ you agree to the following requirements screen loaded.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_by_activating_hp_plus_you_agree_to_the_following_requirements_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("by_activating_hp_plus_you_agree_to_the_following_requirements_screen_content_1", timeout=timeout, raise_e=raise_e)

    def click_by_activating_hp_plus_you_agree_to_the_following_requirements_screen_activate_hp_plus_button(self):
        '''
        This is a method to click Activate HP+ button on By activating HP+ you agree to the following requirements screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_by_activating_hp_plus_you_agree_to_the_following_requirements_screen_activate_hp_plus_button]-Click Activate HP+ button... ")

        self.driver.click("by_activating_hp_plus_you_agree_to_the_following_requirements_screen_activate_hp_plus_button", is_native_event=True)

    def wait_for_this_printer_is_already_enrolled_in_hp_instant_ink_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for This printer is already enrolled in hp instant ink screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_this_printer_is_already_enrolled_in_hp_instant_ink_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("this_printer_is_already_enrolled_in_hp_instant_ink_screen_title", timeout=timeout, raise_e=raise_e)

    def click_this_printer_is_already_enrolled_in_hp_instant_ink_screen_ok_btn(self):
        '''
        This is a method to click OK button on This printer is already enrolled in hp instant ink screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_this_printer_is_already_enrolled_in_hp_instant_ink_screen_ok_btn]-Click OK button... ")

        self.driver.click("this_printer_is_already_enrolled_in_hp_instant_ink_screen_ok_btn", is_native_event=True)
        if self.wait_for_this_printer_is_already_enrolled_in_hp_instant_ink_screen_load(raise_e=False):
            self.driver.click("this_printer_is_already_enrolled_in_hp_instant_ink_screen_ok_btn", is_native_event=True)

    def wait_for_something_went_wrong_please_try_again_later_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Something went wrong, Please try again later screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_something_went_wrong_please_try_again_later_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("something_wnet_wrong_please_try_again_later_screen", timeout=timeout, raise_e=raise_e)

    def click_something_wnet_wrong_please_try_again_later_screen_ok_btn(self):
        '''
        This is a method to click OK button on Something went wrong, Please try again later screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_something_wnet_wrong_please_try_again_later_screen_ok_btn]-Click OK button... ")

        self.driver.click("something_wnet_wrong_please_try_again_later_screen_ok_btn", is_native_event=True)
        if self.wait_for_something_went_wrong_please_try_again_later_screen_load(raise_e=False):
            self.driver.click("something_wnet_wrong_please_try_again_later_screen_ok_btn", is_native_event=True)

    def wait_for_lets_load_paper_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Let's load paper screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[wait_for_lets_load_paper_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("lets_load_paper_screen_skip_loading_paper_btn", timeout=timeout, raise_e=raise_e)

    def click_lets_load_paper_screen_skip_loading_paper_btn(self):
        '''
        This is a method to click Skip loading paper button on Let's load paper screen.
        :parameter:
        :return:
        '''
        logging.debug("[OWS_Yeti]:[click_lets_load_paper_screen_skip_loading_paper_btn]-Click OK button... ")

        self.driver.click("lets_load_paper_screen_skip_loading_paper_btn", is_native_event=True)

# -------------------------------Verification Methods-------------------------------------------------
    def verify_get_more_value_from_your_printing_experience_screen(self):
        '''
        This is a verification method to check UI strings of Get More value from your printing experience screen. (For 3M Yeti printer)
        :parameter:
        :return:
        '''
        self.wait_for_get_more_value_from_your_printing_experience_load(120)
        logging.debug("Start to verify UI string of Get More value from your printing experience screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='get_more_value_from_your_printing_experience_screen')
        assert self.get_value_of_get_more_value_from_your_printing_experience_title() == test_strings['get_more_value_from_your_printing_experience_title']
        assert self.get_value_of_get_more_value_from_your_printing_experience_content() == test_strings['get_more_value_from_your_printing_experience_content']
        assert self.get_value_of_get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn() == test_strings['get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn']
        assert self.get_value_of_get_more_value_from_your_printing_experience_learn_more_btn() == test_strings['get_more_value_from_your_printing_experience_learn_more_btn']
        assert self.get_value_of_get_more_value_from_your_printing_experience_continue_btn() == test_strings['get_more_value_from_your_printing_experience_continue_btn']

    def verify_thank_you_for_choosing_hp_plus_screen(self):
        '''
        This is a verification method to check UI strings of Thank you for Choosing HP+ screen. (For Horizon Yeti printer)
        :parameter:
        :return:
        '''
        self.wait_for_thank_you_for_choosing_hp_plus_screen_load(120)
        logging.debug("Start to verify UI string of Thank you for Choosing HP+ screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='thank_you_for_choosing_hp_plus_screen')
        assert self.get_value_of_get_more_value_from_your_printing_experience_title() == test_strings['thank_you_for_choosing_hp_plus_screen_title']
        assert self.get_value_of_get_more_value_from_your_printing_experience_content() == test_strings['thank_you_for_choosing_hp_plus_screen_content']
        assert self.get_value_of_get_more_value_from_your_printing_experience_learn_more_btn() == test_strings['thank_you_for_choosing_hp_plus_screen_learn_more_btn']
        assert self.get_value_of_get_more_value_from_your_printing_experience_continue_btn() == test_strings['thank_you_for_choosing_hp_plus_screen_continue_btn']

    def verify_are_you_sure_you_dont_want_to_activate_hp_plus_dialog(self):
        '''
        This is a verification method to check UI strings of Are you sure you don't want to activate HP+? dialog
        :parameter:
        :return:
        '''
        self.wait_for_are_you_sure_dialog_load()
        logging.debug("Start to verify UI string of Are you sure you don't want to activate HP+? dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='are_you_sure_dialog')
        assert self.get_value_of_are_you_sure_dialog_title() == test_strings['are_you_sure_dialog_title']
        assert self.get_value_of_are_you_sure_dialog_content_you_will_only() == test_strings['are_you_sure_dialog_content_you_will_only']
        assert self.get_value_of_are_you_sure_dialog_content_six_free_months() == test_strings['are_you_sure_dialog_content_six_free_months']
        assert self.get_value_of_are_you_sure_dialog_content_an_additional_year() == test_strings['are_you_sure_dialog_content_an_additional_year']
        assert self.get_value_of_are_you_sure_dialog_content_access_to_exclusive() == test_strings['are_you_sure_dialog_content_access_to_exclusive']
        assert self.get_value_of_are_you_sure_dialog_content_join_hp_to_keep() == test_strings['are_you_sure_dialog_content_join_hp_to_keep']
        assert self.get_value_of_are_you_sure_dialog_content_select() == test_strings['are_you_sure_dialog_content_select']
        assert self.get_value_of_are_you_sure_dialog_content_back_to_offer() == test_strings['are_you_sure_dialog_content_back_to_offer']
        assert self.get_value_of_are_you_sure_dialog_content_to_reconsider() == test_strings['are_you_sure_dialog_content_to_reconsider']
        assert self.get_value_of_are_you_sure_dialog_back_to_offer_btn() == test_strings['are_you_sure_dialog_back_to_offer_btn']
        assert self.get_value_of_are_you_sure_dialog_decline_hp_plus_btn() == test_strings['are_you_sure_dialog_decline_hp_plus_btn']

    def verify_learn_more_screen(self):
        '''
        This is a verification method to check UI strings of Learn more screen
        :parameter:
        :return:
        '''
        self.wait_for_learn_more_screen_load()
        logging.debug("Start to verify UI string of Learn more screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='learn_more_screen')
        assert self.get_value_of_learn_more_screen_title() == test_strings['learn_more_screen_title']
        assert self.get_value_of_learn_more_screen_hp_plus_overview() == test_strings['learn_more_screen_hp_plus_overview']
        assert self.get_value_of_learn_more_screen_hp_plus_requirements() == test_strings['learn_more_screen_hp_plus_requirements']
        assert self.get_value_of_learn_more_screen_print_plans() == test_strings['learn_more_screen_print_plans']
        assert self.get_value_of_learn_more_screen_forest_first_printing() == test_strings['learn_more_screen_forest_first_printing']
        assert self.get_value_of_learn_more_screen_back_btn() == test_strings['learn_more_screen_back_btn']

    def verify_you_agree_to_dialog(self):
        '''
        This is a verification method to check UI strings of "For your printer to operate after activating HP+, you agree to" dialog. (For 3M Yeti printer)
        :parameter:
        :return:
        '''
        self.wait_for_you_agree_to_dialog_load()
        logging.debug("Start to verify UI string of For your printer to operate after activating HP+, you agree to dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='you_agree_to_dialog')
        assert self.get_value_of_you_agree_to_dialog_title() == test_strings['you_agree_to_dialog_title']
        assert self.get_value_of_you_agree_to_dialog_content_sign_in() == test_strings['you_agree_to_dialog_content_sign_in']
        assert self.get_value_of_you_agree_to_dialog_content_connect_your_printer() == test_strings['you_agree_to_dialog_content_connect_your_printer']
        assert self.get_value_of_you_agree_to_dialog_content_use_only() == test_strings['you_agree_to_dialog_content_use_only']
        assert self.get_value_of_you_agree_to_dialog_content_by_activating() == test_strings['you_agree_to_dialog_content_by_activating']
        assert self.get_value_of_you_agree_to_dialog_activate_hp_plus_btn() == test_strings['you_agree_to_dialog_activate_hp_plus_btn']

    def verify_you_agree_to_dialog_for_horizon_yeti(self):
        '''
        This is a verification method to check UI strings of "For your HP+ printer to operate, you agree to" dialog. (For Horizon Yeti printer)
        :parameter:
        :return:
        '''
        self.wait_for_you_agree_to_dialog_for_horizon_yeti_load()
        logging.debug("Start to verify UI string of For your printer to operate after activating HP+, you agree to dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='you_agree_to_dialog_for_horizon_yeti')
        assert self.get_value_of_you_agree_to_dialog_for_horizon_yeti_title() == test_strings['you_agree_to_dialog_title']
        assert self.get_value_of_you_agree_to_dialog_for_horizon_yeti_content_sign_in() == test_strings['you_agree_to_dialog_content_sign_in']
        assert self.get_value_of_you_agree_to_dialog_for_horizon_yeti_content_connect_your_printer() == test_strings['you_agree_to_dialog_content_connect_your_printer']
        assert self.get_value_of_you_agree_to_dialog_for_horizon_yeti_content_use_only() == test_strings['you_agree_to_dialog_content_use_only']
        assert self.get_value_of_you_agree_to_dialog_for_horizon_yetig_content_by_confirming() == test_strings['you_agree_to_dialog_content_by_confirming']
        assert self.get_value_of_you_agree_to_dialog_confirm_btn() == test_strings['you_agree_to_dialog_confirm_btn']

    def verify_welcome_to_hp_plus_screen(self):
        '''
        This is a verification method to check UI strings of Welcome to HP+ screen
        :parameter:
        :return:
        '''
        self.wait_for_welcome_to_hp_plus_screen_load()
        logging.debug("Start to verify UI string of Welcome to HP+ screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='welcome_to_hp_plus_screen')
        assert self.get_value_of_welcome_to_hp_plus_screen_title() == test_strings['welcome_to_hp_plus_screen_title']
        assert self.get_value_of_welcome_to_hp_plus_screen_content_enjoy_your() == test_strings['welcome_to_hp_plus_screen_content_enjoy_your']
        assert self.get_value_of_welcome_to_hp_plus_screen_content_let_redeem() == test_strings['welcome_to_hp_plus_screen_content_let_redeem']
        assert self.get_value_of_welcome_to_hp_plus_screen_continue_btn() == test_strings['welcome_to_hp_plus_screen_continue_btn']
