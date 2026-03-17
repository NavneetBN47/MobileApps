# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the printer home page screen.

@author: Ivan
@create_date: Sep 03, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class AdvancedSettings(SmartScreens):
    folder_name = "printersettings"
    flow_name = "advanced_settings"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(AdvancedSettings, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait EWS screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ews_home_content", timeout=timeout, raise_e=raise_e)

    def wait_for_printer_home_page_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait printer home page item load on printer settings screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_home_page_item", timeout=timeout, raise_e=raise_e)

    def wait_for_sign_in_link_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sign In link item load on printer settings screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_sign_in_link_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_link", timeout=timeout, raise_e=raise_e)

    def wait_for_ews_ip_address_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait EWS IP Address load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_ews_ip_address_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ews_ip_address", timeout=timeout, raise_e=raise_e)

    def wait_for_redirecting_to_secure_page_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Redirecting to Secure Page dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_redirecting_to_secure_page_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("redirecting_to_secure_page_dialog_checkbox", timeout=timeout, raise_e=raise_e)

    def wait_for_settings_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait settings load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_settings_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("settings_content", timeout=timeout, raise_e=raise_e)

    def wait_for_energy_save_mode_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait EWS Energy Save Mode load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_energy_save_mode_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("energy_save_mode_content", timeout=timeout, raise_e=raise_e)

    def wait_for_cant_open_printer_home_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait can't open printer home or EWS page dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_cant_open_printer_home_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("cant_open_printer_home_or_ews_page_title", timeout=timeout, raise_e=raise_e)

    def wait_for_security_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait windows security dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_security_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("security_dialog_administrator_login", timeout=timeout, raise_e=raise_e)

    def wait_for_energy_save_mode_options_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait 10 minutes option on energy save mode screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_energy_save_mode_options_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("energy_save_mode_apply_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_security_dialog_disappear(self, timeout=30, raise_e=True):
        '''
        This is a method to wait windows security dialog disappear.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_security_dialog_disappear]-Wait for screen disappear... ")

        return self.driver.wait_for_object_disappear("security_dialog_administrator_login", timeout=timeout, raise_e=raise_e)

    def wait_for_changes_updated_successfully(self, timeout=30, raise_e=True):
        '''
        This is a method to wait changes password successfully
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_energy_save_mode_options_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ok_button", timeout=timeout, raise_e=raise_e)

    def wait_for_password_box_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Password box load after clicking Password settings.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[wait_for_password_box_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("password_text_edit", timeout=timeout, raise_e=raise_e)

    def click_security_dialog_cancel_btn(self):
        '''
        This is a method to click Cancel button on dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_security_dialog_cancel_btn]-Click Cancel button.. ")

        self.driver.click("security_dialog_cancel_btn", is_native_event=True)

    def click_cant_open_printer_home_or_ews_page_ok_btn(self):
        '''
        This is a method to click OK button on Can't open printer home or ews page dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_cant_open_printer_home_or_ews_page_ok_btn]-Click OK button.. ")

        self.driver.click("cant_open_printer_home_or_ews_page_ok_btn", is_native_event=True)

    def click_home_tile_on_ews(self):
        '''
        This is a method to click Home tile on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_home_tile_on_ews]-Click Home tile.. ")

        self.driver.click("ews_home_content")

    def click_sign_in_link(self):
        '''
        This is a method to click sign in button on dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_sign_in_link]-Click OK button.. ")

        self.driver.click("sign_in_link", is_native_event=True)

    def click_energy_save_mode_on_ews(self):
        '''
        This is a method to click energy save mode group on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_energy_save_mode_on_ews]-Click Energy Save Mode.. ")

        self.driver.click("energy_save_mode_content", is_native_event=True)

    def select_5_minutes_option_on_ews(self):
        '''
        This is a method to select 5 minutes option on energy save mode group on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[select_5_minutes_option_on_ews]-Select 5 minutes option.. ")

        self.driver.click("energy_save_mode_5_minutes_option", is_native_event=True)

    def select_10_minutes_option_on_ews(self):
        '''
        This is a method to select 10 minutes option on energy save mode group on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[select_10_minutes_option_on_ews]-Select 10 minutes option.. ")

        self.driver.click("energy_save_mode_10_minutes_option", is_native_event=True)

    def click_apply_btn(self):
        '''
        This is a method to click apply button on energy save mode group on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_apply_btn]-Click apply button.. ")

        self.driver.click("energy_save_mode_apply_btn", is_native_event=True)

    def click_scan_tile_on_ews(self):
        '''
        This is a method to click Scan tile on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_scan_tile_on_ews]-Click Scan tile.. ")

        self.driver.click("ews_scan_content")

    def click_network_tile_on_ews(self):
        '''
        This is a method to click Network tile on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_network_tile_on_ews]-Click Network tile.. ")

        self.driver.click("ews_network_content")

    def click_tools_tile_on_ews(self):
        '''
        This is a method to click Tools tile on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_tools_tile_on_ews]-Click Tools tile.. ")

        self.driver.click("ews_tools_content")

    def click_settings_tile_on_ews(self):
        '''
        This is a method to click Settings tile on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_settings_tile_on_ews]-Click Settings tile.. ")

        self.driver.click("ews_settings_content", is_native_event=True)

    def click_redirecting_to_secure_page_dialog_checkbox(self):
        '''
        This is a method to click "Do not show this message again" checkbox on Redirecting to Secure Page dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_redirecting_to_secure_page_dialog_checkbox]-Click Do not show this message again checkbox.. ")

        self.driver.click("redirecting_to_secure_page_dialog_checkbox", is_native_event=True)

    def click_redirecting_to_secure_page_dialog_ok_btn(self):
        '''
        This is a method to click OK button on Redirecting to Secure Page dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_redirecting_to_secure_page_dialog_ok_btn]-Click OK button... ")

        self.driver.click("redirecting_to_secure_page_dialog_ok_btn", is_native_event=True)

    def click_security_item_on_settings_page(self, password=False):
        '''
        This is a method to click security item on settings page.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_security_item_on_settings_page]-Click Settings tile.. ")

        self.driver.scroll_on_app()
        sleep(2)
        if password:
            self.driver.click("setting_security_group_with_password", is_native_event=True)
        else:
            self.driver.click("setting_security_group", is_native_event=True)

    def click_password_setting_on_settings_page(self):
        '''
        This is a method to click security item on settings page.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_password_setting_on_settings_page]-Click Settings tile.. ")

        self.driver.click("setting_security_password_setting_link", is_native_event=True)

    def enter_password(self, password):
        '''
        This is a method to enter the password in the security
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[enter_password]-Enter the password in the security dialog... ")

        self.driver.send_keys("password_text_edit", password, press_enter=True)

    def clear_password(self):
        '''
        This is a method to clear the password in the security.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[clear_password]-Enter the password in the security dialog... ")

        self.driver.clear_text("password_text_edit")

    def click_password_box(self):
        '''
        This is a method to clear the password in the security.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_password_box]-Enter the password in the security dialog... ")

        self.driver.click("password_text_edit", is_native_event=True)

    def clear_confirm_password(self):
        '''
        This is a method to clear the password in the security.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[clear_confirm_password]-Enter the password in the security dialog... ")

        self.driver.clear_text("confirm_password_text_edit")

    def confirm_password(self, password):
        '''
        This is a method to enter the password in the security dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[confirm_password]-Enter the password in the security dialog... ")

        self.driver.send_keys("confirm_password_text_edit", password, press_enter=True)

    def click_apply_btn_on_settings(self):
        '''
        This is a method to click apply button on energy save mode group on EWS.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_apply_btn]-Click apply button.. ")

        self.driver.click("apply_btn", is_native_event=True)

    def enter_password_on_dialog(self, password):
        '''
        This is a method to enter the password in the security dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[enter_password_on_dialog]-Enter the password in the security dialog... ")

        self.driver.send_keys("security_dialog_password_edit", password, press_enter=True)

    def click_security_dialog_ok_btn(self):
        '''
        This is a method to click OK button on security dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[click_security_dialog_ok_btn]-Click OK button.. ")

        self.driver.click("security_dialog_ok_btn", is_native_event=True)

    def get_value_of_cant_open_printer_home_or_ews_page_title(self):
        '''
        This is a method to get value of Can't open printer home or ews page dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_cant_open_printer_home_or_ews_page_title]-Get value of Can't open printer home or ews page dialog title...  ")

        return self.driver.get_value("cant_open_printer_home_or_ews_page_title")

    def get_value_of_cant_open_printer_home_or_ews_page_body(self):
        '''
        This is a method to get value of Can't open printer home or ews page dialog body.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_cant_open_printer_home_or_ews_page_body]-Get value of Can't open printer home or ews page dialog body...  ")

        return self.driver.get_value("cant_open_printer_home_or_ews_page_body")

    def get_value_of_cant_open_printer_home_or_ews_page_ok_btn(self):
        '''
        This is a method to get value of OK button on Can't open printer home or ews page dialog.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_cant_open_printer_home_or_ews_page_ok_btn]-Get value of OK button...  ")

        return self.driver.get_title("cant_open_printer_home_or_ews_page_ok_btn")

    def get_value_of_minutes_energy_save_mode(self):
        '''
        This is a method to get value of minutes_energy_save_mode.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_minutes_energy_save_mode]-Get value of minutes_energy_save_mode...  ")

        return self.driver.get_value("energy_save_mode_minutes_content")

    def get_value_of_ip_address(self):
        '''
        This is a method to get value of EWS IP Address.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_ip_address]-Get value of IP Address...  ")

        return self.driver.get_value("ews_ip_address")

    def get_value_of_security_dialog_ip_content(self):
        '''
        This is a method to get value of security_dialog_ip_content.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_ip_content]-Get value of security_dialog_ip_content...  ")

        return self.driver.get_value("security_dialog_ip_content")

    def get_value_of_security_dialog_administrator_login(self):
        '''
        This is a method to get value of security_dialog_administrator_login.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_administrator_login]-Get value of security_dialog_administrator_login...  ")

        return self.driver.get_value("security_dialog_administrator_login")

    def get_value_of_security_dialog_user_name(self):
        '''
        This is a method to get value of security_dialog_user_name.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_user_name]-Get value of security_dialog_user_name...  ")

        return self.driver.get_value("security_dialog_user_name")

    def get_value_of_security_dialog_user_name_admin(self):
        '''
        This is a method to get value of security_dialog_user_name.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_user_name_admin]-Get value of security_dialog_user_name...  ")

        return self.driver.get_value("security_dialog_user_name_edit")

    def get_value_of_security_dialog_password(self):
        '''
        This is a method to get value of security_dialog_password.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_password]-Get value of security_dialog_password...  ")

        return self.driver.get_value("security_dialog_password")

    def get_value_of_security_dialog_cancel_btn(self):
        '''
        This is a method to get value of security_dialog_user_name.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_cancel_btn]-Get value of security_dialog_cancel_btn...  ")

        return self.driver.get_title("security_dialog_cancel_btn")

    def get_value_of_security_dialog_ok_btn(self):
        '''
        This is a method to get value of security_dialog_ok_btn.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_security_dialog_ok_btn]-Get value of security_dialog_ok_btn...  ")

        return self.driver.get_title("security_dialog_ok_btn")

    def get_value_of_sign_in_link(self):
        '''
        This is a method to get value of sign_in_link.
        :parameter:
        :return:
        '''
        logging.debug("[AdvancedSettings]:[get_value_of_sign_in_link]-Get value of security_dialog_password...  ")

        return self.driver.get_value("sign_in_link")

# -------------------------------Verification Methods--------------------------
    def change_energy_save_mode_option(self):
        logging.debug("[AdvancedSettings]:[change_energy_save_mode_option]-Verify energy save mode could be changed to 10 minutes successfully... ")
        self.wait_for_energy_save_mode_item_load()
        self.click_energy_save_mode_on_ews()
        if self.wait_for_redirecting_to_secure_page_dialog_load(raise_e=False):
            self.click_redirecting_to_secure_page_dialog_checkbox()
            self.click_redirecting_to_secure_page_dialog_ok_btn()
        self.wait_for_energy_save_mode_options_page_load()
        self.select_10_minutes_option_on_ews()
        self.click_apply_btn()
        self.click_home_tile_on_ews()
        self.wait_for_energy_save_mode_item_load()
        sleep(2)
        assert self.get_value_of_minutes_energy_save_mode() == "10 min"
        self.click_energy_save_mode_on_ews()
        self.wait_for_energy_save_mode_options_page_load()
        self.select_5_minutes_option_on_ews()
        self.click_apply_btn()
        self.click_home_tile_on_ews()
        self.wait_for_energy_save_mode_item_load()
        sleep(2)
        assert self.get_value_of_minutes_energy_save_mode() == "5 min"

    def verify_ews_ip_address(self, printer_ip):
        '''
        This is a method to verify the EWS IP Address.
        :parameter:
        :return:
        '''
        self.wait_for_ews_ip_address_item_load()
        a = self.get_value_of_ip_address()
        if a != printer_ip:
            raise ValueError("EWS IP Address does not match printer IP Address")
        return True

    def verify_cant_open_printer_home_dialog(self):
        '''
        This is a verification method to check UI strings of Can't open printer home or EWS page dialog.
        :parameter:
        :return:
        '''
        self.wait_for_cant_open_printer_home_dialog()

        logging.debug("Start to check UI strings of Administrator Login Security dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='cant_open_printer_home_or_ews_page_dialog')
        assert self.get_value_of_cant_open_printer_home_or_ews_page_title() == test_strings['cant_open_printer_home_or_ews_page_title']
        assert self.get_value_of_cant_open_printer_home_or_ews_page_body() == test_strings['cant_open_printer_home_or_ews_page_body']
        assert self.get_value_of_cant_open_printer_home_or_ews_page_ok_btn() == test_strings['cant_open_printer_home_or_ews_page_ok_btn']

    def verify_administrator_login_security_dialog(self, ip_address):
        '''
        This is a verification method to check UI strings of Administrator Login Security dialog.
        :parameter:
        :return:
        '''
        self.wait_for_security_dialog_load()

        logging.debug("Start to check UI strings of Administrator Login Security dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='administrator_login_security_dialog')
        assert self.get_value_of_security_dialog_ip_content() == ip_address
        assert self.get_value_of_security_dialog_administrator_login() == test_strings['dialog_title']
        assert self.get_value_of_security_dialog_user_name() == test_strings['dialog_user_name']
        assert self.get_value_of_security_dialog_user_name_admin() == test_strings['dialog_user_name_admin']
        assert self.get_value_of_security_dialog_password() == test_strings['dialog_password']
        assert self.get_value_of_security_dialog_cancel_btn() == test_strings['dialog_cancel_btn']
        assert self.get_value_of_security_dialog_ok_btn() == test_strings['dialog_ok_btn']
