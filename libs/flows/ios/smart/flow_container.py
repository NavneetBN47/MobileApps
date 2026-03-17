import random
import string
from selenium.common.exceptions import *
from MobileApps.libs.flows.mac.smart.utility import smart_utilities
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.libs.flows.ios.smart.app_settings import AppSettings, MacAppSettings
from MobileApps.libs.flows.ios.smart.box import Box
from MobileApps.libs.flows.ios.smart.camera import Camera
from MobileApps.libs.flows.ios.smart.copy import Copy
from MobileApps.libs.flows.ios.smart.clouds import Clouds
from MobileApps.libs.flows.ios.smart.dropbox import Dropbox
from MobileApps.libs.flows.ios.smart.facebook import Facebook
from MobileApps.libs.flows.ios.smart.files import Files, MacFiles
from MobileApps.libs.flows.ios.smart.gmail import Gmail
from MobileApps.libs.flows.ios.smart.safari import Safari
from MobileApps.libs.flows.ios.smart.home import Home, MacHome
from MobileApps.libs.flows.ios.smart.message import Message
from MobileApps.libs.flows.ios.smart.moobe_awc import MoobeAwc
from MobileApps.libs.flows.ios.smart.moobe_setup_complete import MoobeSetupComplete
from MobileApps.libs.flows.ios.smart.moobe_ows import MoobeOws
from MobileApps.libs.flows.ios.smart.moobe_wac import MoobeWac
from MobileApps.libs.flows.ios.smart.notifications import Notifications
from MobileApps.libs.flows.ios.smart.personalize import Personalize
from MobileApps.libs.flows.ios.smart.profile import Profile
from MobileApps.libs.flows.ios.smart.photos import Photos
from MobileApps.libs.flows.ios.smart.preview import Preview
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings
from MobileApps.libs.flows.ios.smart.printers import Printers
from MobileApps.libs.flows.ios.smart.scan import Scan, MacScan
from MobileApps.libs.flows.ios.smart.support import Support
from MobileApps.libs.flows.ios.smart.shortcuts import Shortcuts
from MobileApps.libs.flows.ios.smart.share import ios_share_flow_factory
from MobileApps.libs.flows.ios.smart.welcome import Welcome
from MobileApps.libs.flows.ios.smart.uma_settings import UMASettings
from MobileApps.libs.flows.ios.smart.feedback import Feedback
from MobileApps.libs.flows.web.softfax.softfax_offer import SoftfaxOffer
from MobileApps.libs.flows.web.softfax.softfax_welcome import MobileSoftfaxWelcome
from MobileApps.libs.flows.web.softfax.compose_fax import MobileComposeFax
from MobileApps.libs.flows.web.softfax.contacts import MobileContacts
from MobileApps.libs.flows.web.softfax.fax_history import MobileFaxHistory
from MobileApps.libs.flows.web.softfax.fax_settings import MobileFaxSettings
from MobileApps.libs.flows.web.softfax.send_fax_details import SendFaxDetails
from MobileApps.libs.flows.web.help_support.help_support import IOSHelpSupport, MacHelpSupport
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.common.smart.edit import IOSEdit
from MobileApps.libs.flows.common.smart.preview import IOSPreview
from MobileApps.libs.flows.common.smart.smb import IOSSmb
from MobileApps.libs.flows.web.smart.scribble import Scribble
from MobileApps.libs.flows.web.privacy_statement.privacy_central import PrivacyCentral
from MobileApps.libs.flows.web.smart.dedicated_supplies_page import DedicatedSuppliesPage
from MobileApps.libs.flows.web.hp_id.hp_id import HPID, MacHPID
from MobileApps.libs.flows.web.ows.value_prop import MobileValueProp, MacValueProp
from MobileApps.libs.flows.web.smart.smart_welcome import IosSmartWelcomeNative, SmartWelcome
from MobileApps.libs.flows.web.smart.privacy_preferences import PrivacyPreferences, MacPrivacyPreferencesNative
from MobileApps.libs.flows.web.ows.ucde_privacy import MobileUCDEPrivacy
from MobileApps.libs.flows.web.shortcuts.shortcuts_create_edit import MobileShortcutsCreateEdit, MACShortcutsCreateEdit
from MobileApps.libs.flows.web.hp_connect.hp_connect import IOSHPConnect, MacHPConnect
from MobileApps.libs.flows.web.hp_connect.printers_users import PrintersUsers
from MobileApps.libs.flows.web.hp_connect.account import Account
from MobileApps.libs.flows.web.hp_connect.features import Features
from MobileApps.libs.flows.web.hp_connect.help_center import IOSHPCHelpCenter
from MobileApps.libs.flows.web.hp_connect.hp_instant_ink import HPInstantInk
from MobileApps.libs.flows.web.shortcuts.shortcuts_create_edit import MobileShortcutsCreateEdit
from MobileApps.libs.flows.web.cec.custom_engagement_center import CustomEngagementCenter
from MobileApps.libs.flows.web.printables.printables import Printables
from MobileApps.libs.flows.web.smart.redaction import IOSRedaction
from MobileApps.libs.flows.web.smart.text_extract import TextExtract
from MobileApps.libs.flows.web.smart.mac_browser_popup_flow import MacBrowserPopupFlow
from MobileApps.libs.flows.web.smart.shortcuts_notification import ShortcutsNotification
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const

from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

from SPL.decorator import SPL_decorator
from SPL.driver.reg_printer import *

import pytest
import os

class FlowContainer(object):
    def __init__(self, driver, web_driver=None):
        self.driver = driver
        self.web_driver = web_driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)
        self.hpx = False
        self.fd = {
            "box": Box(driver),
            "camera": Camera(driver),
            "copy": Copy(driver),
            "clouds": Clouds(driver),
            "dropbox": Dropbox(driver),
            "facebook": Facebook(driver),
            "message": Message(driver),
            "moobe_awc": MoobeAwc(driver),
            "moobe_setup_complete": MoobeSetupComplete(driver),
            "moobe_ows": MoobeOws(driver),
            "moobe_wac": MoobeWac(driver),
            "notifications": Notifications(driver),
            "personalize": Personalize(driver),
            "photos": Photos(driver),
            "preview": Preview(driver),
            "common_preview": IOSPreview(driver),
            "printer_settings": PrinterSettings(driver),
            "printers": Printers(driver),
            "share": ios_share_flow_factory(driver),
            "welcome": Welcome(driver),
            "gmail_api": GmailAPI(credential_path=w_const.TEST_DATA.GMAIL_TOKEN_PATH),
            "edit": IOSEdit(driver),
            "smb": IOSSmb(driver),
            "feedback": Feedback(driver),
            "smb": IOSSmb(driver)
        }
        if pytest.platform == "IOS":
            fd_ios = {
                "home": Home(driver),
                "app_settings": AppSettings(driver),
                "safari": Safari(driver),
                "ios_system": ios_system_flow_factory(driver),
                "redaction": IOSRedaction(driver, context={"url": w_const.WEBVIEW_URL.REDACTION}),
                "scribble": Scribble(driver, context={"url": w_const.WEBVIEW_URL.SCRIBBLE}),
                "hpid": HPID(driver, context={"url": self.hpid_url}),
                "softfax_offer": SoftfaxOffer(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX_OFFER}),
                "softfax_welcome": MobileSoftfaxWelcome(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "softfax_compose_fax": MobileComposeFax(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "softfax_fax_history": MobileFaxHistory(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "fax_settings": MobileFaxSettings(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "send_fax_details": SendFaxDetails(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "softfax_contacts": MobileContacts(driver, context={"url": w_const.WEBVIEW_URL.SOFTFAX}),
                "dedicated_supply_levels": DedicatedSuppliesPage(driver, context={"url": w_const.WEBVIEW_URL.DEDICATED_SUPPLY_LEVEL}),
                "help_support": IOSHelpSupport(driver, context=-1),
                "ows_welcome": OWSWelcome(driver, context=-1),
                "privacy_statement": PrivacyCentral(driver, context=-1),
                "ows_value_prop": MobileValueProp(driver, context={"url": w_const.WEBVIEW_URL.VALUE_PROP}),
                "welcome_web": IosSmartWelcomeNative(driver, context={"url": w_const.WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type)}),
                "privacy_preferences": PrivacyPreferences(driver, context=-1),
                "ucde_privacy": MobileUCDEPrivacy(driver, context=-1),
                "hp_connect": IOSHPConnect(driver, context=-1),
                "hpc_printers_users": PrintersUsers(driver, context=-1),
                "hpc_account": Account(driver, context=-1),
                "hpc_features": Features(driver, context=-1),
                "hpc_help_center": IOSHPCHelpCenter(driver, context=-1),
                "hpc_instant_ink": HPInstantInk(driver, context=-1),
                "text_extract": TextExtract(driver, context={"url": w_const.WEBVIEW_URL.TEXT_EXTRACT}),
                "shortcuts": MobileShortcutsCreateEdit(driver, context=-1),
                "hpx_shortcuts": Shortcuts(driver),
                "cec_home": CustomEngagementCenter(driver, context=w_const.WEBVIEW_URL.CEC),
                "cec": CustomEngagementCenter(driver, context=-1),
                "printables": Printables(driver, context=-1),
                "scan": Scan(driver),
                "gmail": Gmail(driver),
                "files": Files(driver),
                "shortcuts_notification": ShortcutsNotification(driver, context=-1),
                "profile": Profile(driver),
                "uma_settings":UMASettings(driver),
                "support":Support(driver)
            }
            self.fd.update(fd_ios)
        else:
            fd_mac = {
                "home": MacHome(driver),
                "app_settings": MacAppSettings(driver),
                "help_support": MacHelpSupport(driver),
                "privacy_preferences": MacPrivacyPreferencesNative(driver),
                "ows_value_prop": MacValueProp(driver),
                "welcome_web": SmartWelcome(driver),
                "hpid": MacHPID(web_driver),
                "mac_browser_popup_flow": MacBrowserPopupFlow(web_driver),
                "privacy_statement": PrivacyCentral(driver),
                "hp_connect": MacHPConnect(driver),
                "softfax_offer": SoftfaxOffer(driver),
                "softfax_fax_history": MobileFaxHistory(driver),
                "shortcuts": MACShortcutsCreateEdit(driver),
                "scan": MacScan(driver),
                "files": MacFiles(driver),
                "dedicated_supply_levels": DedicatedSuppliesPage(driver),
                "shortcuts_notification": ShortcutsNotification(driver)
            }
            self.fd.update(fd_mac)

    @property
    def flow(self):
        return self.fd

    def change_stack(self, stack,enable_uma_links=False):
        if pytest.platform == "IOS":
            self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
            self.flow["ios_system"].switch_app_stack(stack, i_const.BUNDLE_ID.SMART,hpx_flag=self.hpx)
            if enable_uma_links:
                self.enable_uma_links()
            self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        else:
            self.fd["home"].click_hpsmart_preferences_btn()
            self.fd["home"].click_stacks_dropdown_menu()
            self.fd["home"].select_stack_option_from_dropdown_menu(stack)
            self.driver.restart_app(i_const.BUNDLE_ID.SMART)

    def enable_hpx_web_mfe(self):
        if pytest.platform == "MAC":
            self.fd["home"].click_hpsmart_preferences_btn()
            self.fd["home"].select_hpx_settings_tab()
            self.fd["home"].toggle_hpx_enable_web_mfe_checkbox()
            self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        else:
            pass

    def reset_hp_smart(self):
        if pytest.platform == "IOS":
            self.driver.reset(i_const.BUNDLE_ID.SMART)
        else:
            self.reset_hp_smart_mac()

    ###############################################################################################################
    #
    #                               HOME // WELCOME(moobe) included
    #
    ##############################################################################################################

    def go_home(self, reset=False, stack="pie", button_index=1, username="", password="", create_account=False,
                remove_default_printer=False, enable_hpx_web_mfe=False,skip_sign_in=False, enable_uma_links=False):
        """
         @param button_index: int between 0-2 for the position of the ows value prop button
            - 0: setup printer
            - 1: use hp smart/sign in
            - 2: explore hp smart/skip now
        - From fresh installed app
        - navigate welcome screens
        - navigate ows value prop
        - Verify home
        - remove_default_printer: is default set to True, change to False for HP+ or other test accounts
                   wit printer paired
        """
        stack = stack.lower()
        if reset:
            self.reset_hp_smart()
        if pytest.platform == "MAC":
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
        if pytest.platform == "IOS":
            self.fd["ios_system"].clear_safari_cache()
        if stack != "pie":  # pie stack is default server on both iOS & MAC HP Smart
            self.change_stack(stack,enable_uma_links=enable_uma_links)
        if enable_hpx_web_mfe:
            self.enable_hpx_web_mfe()
        if pytest.platform == "MAC":
            self.fd["home"].enter_full_screen_mode()
        if pytest.platform == "IOS":
            self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.driver.performance.time_stamp("t0")
        if pytest.platform == "IOS":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
        self.fd["welcome_web"].verify_welcome_screen()
        self.driver.performance.time_stamp("t1")
        self.driver.swipe()
        if pytest.platform == "IOS" and self.hpx == False:
            welcome_change_check = {"wait_obj": "welcome_webview", "cc_type": "wait_for_attribute", "wait_attribute": "visible", "displayed": False} 
        else:
            welcome_change_check = {"wait_obj": "accept_all_btn", "invisible":True}
        self.fd["welcome_web"].click_accept_all_btn(change_check=welcome_change_check)
        self.fd["home"].allow_notifications_popup(raise_e=False)
        self.driver.performance.time_stamp("t3")
        if pytest.platform == "IOS":
            # This method check for the allow tracking for advertising info screen
            # Not a defect, designed to display as in-app view
            if self.fd["welcome_web"].verify_permission_for_advertising_screen():
                self.fd["welcome_web"].click_continue_btn()
            self.fd["ios_system"].handle_allow_tracking_popup(raise_e=False)
            self.fd["ios_system"].dismiss_hp_local_network_alert()
            # TODO: waiting on specs for webview timeout GDG-1768
            self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60,raise_e=False)
        if self.hpx:
            if skip_sign_in:
                self.fd["ows_value_prop"].click_continue_as_guest_btn(raise_e=False)
                self.fd["home"].allow_notifications_popup(raise_e=False)
                self.fd["ios_system"].dismiss_hp_local_network_alert()
                return
            else:
                self.fd["home"].click_sign_btn_hpx()
                self.fd["hpid"].login()
                self.fd["home"].allow_notifications_popup(raise_e=False)
                self.fd["ios_system"].dismiss_hp_local_network_alert()
                return
        self.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        self.driver.performance.time_stamp("t4")
        if button_index == 1:
            self.login_value_prop_screen(tile=False, username=username, password=password,
                                        create_account=create_account)
            sleep(1)
            if pytest.platform == "IOS":
                self.clear_popups_on_first_login()
            self.fd["home"].verify_home()
        else:
            self.fd["ows_value_prop"].select_value_prop_buttons(button_index)
            if pytest.platform == "IOS":
                self.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)            
                self.fd["home"].allow_notifications_popup(timeout=15, raise_e=False)
                sleep(2)
                self.dismiss_tap_here_to_start()
            else:
                self.driver.activate_app(i_const.BUNDLE_ID.SMART)
                if self.fd["home"].verify_session_expired_popup(timeout=5):
                    self.fd["home"].select_session_expired_cancel_btn()
                    self.fd["home"].verify_home()
            if remove_default_printer:
                self.remove_default_paired_printer()
    
    def enable_uma_links(self):
        self.fd["ios_system"].launch_ios_settings()
        self.fd["uma_settings"].enable_uma_flag(app=i_const.BUNDLE_ID.SMART)
        self.fd["ios_system"].close_ios_settings()
            
    def verify_create_account_screen(self, reset=False, stack="pie", home=False):
        if not home:
            stack = stack.lower()
            if reset:
                self.reset_hp_smart()
            self.fd["ios_system"].clear_safari_cache()
            if stack != "pie":  # pie stack is default server on iOS HP Smart
                self.change_stack(stack)
            self.driver.launch_app(i_const.BUNDLE_ID.SMART)
            self.driver.wait_for_context(w_const.WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
            self.fd["welcome_web"].verify_welcome_screen()
            self.fd["welcome_web"].click_accept_all_btn()
            if self.fd["welcome_web"].verify_permission_for_advertising_screen():
                self.fd["welcome_web"].click_continue_btn()
            self.fd["ios_system"].handle_allow_tracking_popup(raise_e=False)
            # TODO: waiting on specs for webview timeout GDG-1768
            self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
            self.fd["ows_value_prop"].verify_ows_value_prop_screen()
            self.fd["ows_value_prop"].select_value_prop_buttons(1)
        else:
            self.fd["home"].verify_bottom_navigation_bar_icons(signed_in=False)
            self.fd["home"].select_create_account_icon()
        # TODO: longer wait times in below method are due to existing issue- GDG-1768
        self.driver.wait_for_context(self.hpid_url, timeout=45)
        # TODO - OWS-66489
        if self.fd["hpid"].verify_hp_id_sign_in(raise_e=False):
            self.fd["hpid"].click_create_account_link()
        self.fd["hpid"].verify_hp_id_sign_up()

    def clear_popups_on_first_login(self, timeout=15, smart_task=False, coachmark=True):
        sleep(2)
        self.fd["home"].allow_notifications_popup(timeout=timeout, raise_e=False)
        self.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)
        if smart_task:
            self.fd["home"].close_smart_task_awareness_popup()
        if coachmark:
            self.fd["home"].dismiss_tap_account_coachmark()

    # TODO: longer wait times in below method are due to existing issue- GDG-1768
    def login_value_prop_screen(self, tile=False, username="", password="", create_account=False, webview=True, timeout=60):
        if pytest.platform == "IOS":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=timeout)
        if not (username and password) and not create_account:
            username, password = self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"]
        if webview:
            self.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=tile, timeout=timeout)
            self.fd["ows_value_prop"].select_value_prop_buttons(1, change_check=True)
            self.driver.performance.time_stamp("t5")
        else:
            self.fd["ows_value_prop"].verify_native_value_prop_screen()
            self.fd["ows_value_prop"].select_native_value_prop_buttons(1)
        # TODO: longer wait times in below method are due to existing issue- GDG-1768
        if pytest.platform == "IOS":
            self.driver.wait_for_context(self.hpid_url, timeout=45)
        else:
            self.switch_window_and_modify_wn("hpid", "web_login")
        if pytest.platform == "IOS":
            self.fd["hpid"].verify_hp_id_sign_in()
        self.driver.performance.time_stamp("t6")

        if not create_account:
            self.fd["hpid"].login(username, password)
            if pytest.platform == "IOS" and self.fd["smb"].select_my_printers(raise_e=False):
                self.fd["smb"].select_continue()
        else:
            self.fd["hpid"].click_create_account_link()
            return self.create_new_user_account()
        if pytest.platform == "MAC":
            self.delete_window_and_activate_hp_smart("web_login")

    def login_from_home_screen(self, username="", password=""):
        if not (username and password):
            username, password = self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"]
        self.fd["home"].select_create_account_icon()
        self.driver.wait_for_context(self.hpid_url, timeout=30)
        self.fd["hpid"].click_sign_in_link_from_create_account()
        self.fd["hpid"].verify_hp_id_sign_in()
        self.fd["hpid"].login(username, password)
        if self.fd["smb"].select_my_printers(raise_e=False):
            self.fd["smb"].select_continue()

    def go_to_home_screen(self):
        if pytest.platform == "MAC":
            self.driver.restart_app(i_const.BUNDLE_ID.SMART)
            self.fd["home"].verify_home()
            self.fd["home"].dismiss_tap_account_coachmark()
            return
        if not self.fd["home"].verify_home(raise_e=False):
            self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        if not self.fd["home"].verify_home(raise_e=False):
            self.fd["ios_system"].dismiss_software_update_if_visible()
            self.fd["home"].verify_home_tile(raise_e=True)

    def dismiss_tap_here_to_start(self):
        if self.fd["home"].verify_tap_here_to_start():
            self.fd["home"].select_tap_here_to_start()
            if self.driver.wait_for_object("_shared_cancel", timeout=2, raise_e=False):
                self.fd["home"].select_cancel()
            else:
                self.fd["home"].select_navigate_back()
            self.fd["home"].close_smart_task_awareness_popup()

    def setup_moobe_awc_ble(self, printer_name):
        """
        starts from 'Welcome' screen, ends on 'Connect to Printer Network' screen
        :param printer_name: shortened model name of the printer. i.e. "ENVY 5000 series"
        """
        self.go_home(verify_home=False)
        self.dismiss_tap_here_to_start()
        self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_moobe_printer_from_list(printer_name)
        self.fd["moobe_awc"].pass_weak_bluetooth_connection(timeout=20)

    def setup_moobe_awc_wifi(self, p_obj, app_settings=False, stack="pie"):
        """
        starts from 'Welcome' screen, ends on 'Connect to Printer Network' screen
        :param p_obj: Printer object from SPL. i.e. RegPrinter()
        :param app_settings: default False, set True to go through wifi setup through App Settings tab
        """
        self.go_home(reset=True, stack=stack)
        if app_settings:
            self.fd["home"].select_app_settings()
            self.fd["app_settings"].select_set_up_new_printer_cell()
            self.fd["printers"].handle_bluetooth_popup()
        else:
            self.dismiss_tap_here_to_start()
            self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_add_printer()
        self.fd["printers"].select_set_up_a_new_printer()
        self.fd["printers"].handle_location_popup(selection="allow")
        self.fd["app_settings"].verify_set_up_new_printer_ui_elements()
        self.fd["ios_system"].launch_ios_settings()
        self.fd["ios_system"].select_wifi_menu_item()
        beacon_ssid = p_obj.get_wifi_direct_information()['name']
        self.fd["ios_system"].select_wifi_by_ssid(beacon_ssid, None, security_type="None")
        self.driver.activate_app(i_const.BUNDLE_ID.SMART)

    def moobe_secure_ble(self, printer_name: str, ssid: str, password: str):
        """
        starts from 'Welcome' screen and performs secure BLE steps up to putting printer onto the network
        """
        self.go_home(verify_home=False)
        self.dismiss_tap_here_to_start()
        self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_moobe_printer_from_list(printer_name)
        self.fd["moobe_awc"].handle_location_popup(selection="allow")
        self.fd["moobe_awc"].connect_printer_to_network(ssid)
        self.fd["moobe_awc"].verify_network_loaded(ssid)
        self.fd["moobe_awc"].enter_wifi_pwd(password, press_enter=True)

    def moobe_wac(self, bonjour_name, ssid, dismiss_popup=False):
        """
        starts from 'Welcome' screen and performs WAC steps to connect device to printer
        if the path does not matter, set dismiss_popup to True for better reliability
        :param dismiss_popup: bool True to perform WAC via 'tap here to start' flow, False to go through printer screen
        :param bonjour_name: str printer bonjour name
        :param ssid: str network name 
        """
        if dismiss_popup:
            self.dismiss_tap_here_to_start()
            self.fd["home"].select_get_started_by_adding_a_printer()
            self.fd["printers"].select_moobe_printer_from_list(bonjour_name)
        else:
            self.fd["home"].select_tap_here_to_start()
            if self.fd['printers'].verify_printers_nav(raise_e=False):
                # if there are multiple WAC supported printers in moobe mode
                self.fd["printers"].select_moobe_printer_from_list(bonjour_name)
            else:
                # could fail here if requested printer connection is lost
                self.fd["printers"].verify_found_printer_for_setup(bonjour_name)
                self.fd["printers"].select_continue()
        self.fd["printers"].verify_automatically_put_device_on_network()
        self.fd["printers"].select_yes()
        self.fd["moobe_wac"].verify_accessory_setup(ssid=ssid, accessory_name=bonjour_name)
        self.fd["moobe_wac"].select_next()
        self.fd["moobe_wac"].verify_setup_complete()

    def moobe_connect_printer_to_wifi(self, ssid_name="rd", wifi_password="1213141567890"):
        """
        Starts on 'Connect to Printer Network' screen, ends on "Printer Connected screen" signaling end of AWC
        :param ssid_name: name of the ssid
        :param wifi_password: password for specified ssid:
        """
        self.fd["moobe_awc"].verify_network_loaded(ssid_name)
        self.fd["moobe_awc"].enter_wifi_pwd(wifi_password, press_enter=True)
        self.fd["moobe_awc"].verify_connecting_to_printer()
        retry = False
        try:
            self.fd["moobe_awc"].select_retry_button(timeout=120)
            retry = True
        except TimeoutException:
            logging.info("Retry popup did not occur")
        if retry:
            try:
                self.fd["moobe_awc"].verify_network_loaded(ssid_name)
                self.fd["moobe_awc"].enter_wifi_pwd(wifi_password, press_enter=True)
            except TimeoutException:
                logging.info("Retry button didn't go back to input Wi-Fi password screen")
        if self.fd["moobe_awc"].verify_reconnect_your_device_title():
            self.fd["ios_system"].launch_ios_settings()
            self.fd["ios_system"].select_wifi_menu_item()
            wpa = "WPA2" if self.driver.driver_info['platformVersion'].split(".")[0] == '12' else "WPA2/WPA3"
            self.fd["ios_system"].select_wifi_by_ssid(ssid_name, wifi_password, security_type=wpa)
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
        self.fd["moobe_awc"].verify_printer_connected_screen(timeout=60)

    def add_printer_by_ip(self, printer_ip):
        """
         Starts from Home and adds printer
        """
        if pytest.platform == "IOS":
            self.fd["home"].close_smart_task_awareness_popup()
        self.dismiss_tap_here_to_start()
        if pytest.platform == "IOS" and self.hpx == False:
            self.fd["home"].select_get_started_by_adding_a_printer()
        else:
            self.fd["home"].select_get_started_by_adding_a_printer(handle_popup=False)
        self.fd["printers"].add_printer_ip(printer_ip)
        if pytest.platform == "IOS":
            self.fd["home"].handle_location_popup(raise_e=False)
            self.fd["home"].close_smart_task_awareness_popup()
            self.fd["home"].close_print_anywhere_pop_up()
        if self.hpx:
            self.fd["home"].verify_hpx_home()
        else:
            self.fd["home"].verify_home()
        self.fd["home"].dismiss_tap_account_coachmark()

    def remove_default_paired_printer(self):
        if pytest.platform == "IOS":
            self.fd["home"].allow_notifications_popup(raise_e=False)
            self.fd["home"].handle_location_popup(raise_e=False)
        if not self.fd["home"].verify_add_your_first_printer(raise_e=False):
            try:
                self.fd["home"].remove_printer()
            except NoSuchElementException:
                self.fd["home"].hide_printer()

    def select_printer_from_topbar(self, printer_ip, verify_ga=False):
        self.fd["home"].select_printer_plus_button_from_topbar()
        self.fd["printers"].verify_printers_nav()
        self.fd["printers"].select_add_printer()
        self.fd["printers"].verify_add_printer_screen()
        self.fd["printers"].select_add_printer_using_ip()
        self.fd["printers"].verify_connect_the_printer_screen()
        self.fd["printers"].search_for_printer_directly_using_ip(printer_ip)
        self.fd["printers"].select_is_this_your_printer()
        self.fd["home"].verify_home(ga=verify_ga)

    def create_account_from_homepage(self):
        self.fd["home"].select_create_account_icon()
        return self.create_new_user_account()

    def create_new_user_account(self, timeout=10, coachmark=True):
        if pytest.platform == "IOS":
            self.driver.wait_for_context(self.hpid_url, timeout=timeout)
        #TODO - OWS-66489
        if self.fd["hpid"].verify_hp_id_sign_in(raise_e=False):
            self.fd["hpid"].click_create_account_link()
        email, password = self.fd["hpid"].create_account()
        if pytest.platform == "IOS":
            self.clear_popups_on_first_login(coachmark=coachmark)
        else:
            self.delete_window_and_activate_hp_smart("web_login")
        self.driver.session_data["hpid_user"] = email
        self.driver.session_data["hpid_pass"] = password       
        return email, password

    def create_account_from_tile(self, native=False):
        if pytest.platform == "IOS":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=45)
        if native:
            self.fd["ows_value_prop"].verify_native_value_prop_screen()
            self.fd["ows_value_prop"].select_native_value_prop_buttons(0)
        else:
            self.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=30)
            self.fd["ows_value_prop"].select_value_prop_buttons(0)
        if pytest.platform == "MAC":
            self.switch_window_and_modify_wn("hpid", "web_login")
        if pytest.platform == "MAC":
            result = self.fd["hpid"].create_account()
            self.delete_window_and_activate_hp_smart("web_login")
            return result
        return self.fd["hpid"].create_account()

    def create_account_from_app_settings(self):
        self.fd["home"].select_app_settings()
        self.fd['app_settings'].select_sign_in_option()
        return self.create_new_user_account(timeout=15)    

    ###############################################################################################################
    #
    #                               APP Settings
    #
    ##############################################################################################################

    def go_app_settings_screen_from_home(self, timeout=3):
        if not self.fd["app_settings"].verify_app_settings_screen(timeout=timeout, raise_e=False):
            self.fd["home"].select_settings_icon()

    ################################################################################################################
    #
    #                               Digital COPY
    #
    ###############################################################################################################

    def go_copy_screen_from_home(self):
        self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
        self.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fd["copy"].verify_copy_screen()

    ###############################################################################################################
    #
    #                                   Print Photo
    #
    ##############################################################################################################
    def go_photos_screen_from_home(self):
        if self.fd["photos"].verify_photos_screen():
            return True
        self.go_to_home_screen()
        self.fd["home"].select_documents_icon()
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["photos"].select_albums_tab()
        self.fd["photos"].verify_albums_screen()
        self.fd["photos"].select_recents_or_first_option()
        self.fd["photos"].verify_photos_screen()

    def select_multiple_photos_to_preview(self, no_of_photos=2):
        self.go_photos_screen_from_home()
        self.fd["photos"].select_multiple_photos(end=no_of_photos)
        self.fd["photos"].verify_multi_selected_photos_screen()
        self.fd["photos"].select_next_button(change_check={"wait_obj":"next_btn", "invisible":True} if pytest.platform == "MAC" else None)
        sleep(2)
        self.fd["common_preview"].select_print_size(raise_e=False)
        self.fd["common_preview"].verify_title(IOSPreview.PREVIEW_TITLE)

    def navigate_to_transform_screen(self):
        self.fd["common_preview"].go_to_print_preview_pan_view(pan_view=False)
        self.fd["common_preview"].select_transform_options(IOSPreview.PREVIEW_IMAGE)

    ###############################################################################################################
    #
    #                                          FILES // DOCUMENTS
    #
    ###############################################################################################################

    def go_hp_smart_files_screen_from_home(self, select_tile=False):
        if self.fd["files"].verify_hp_smart_files_screen(timeout=5, raise_e=False):
            return True
        self.go_to_home_screen()
        if select_tile:
            self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        else:
            self.fd["home"].select_documents_icon()
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["files"].verify_files_screen()
        self.fd["files"].select_hp_smart_files_folder_icon()
        self.fd["files"].verify_hp_smart_files_screen()

    def go_hp_smart_files_and_delete_all_files(self):
        if pytest.platform == "IOS":
            self.go_hp_smart_files_screen_from_home()
            self.fd["files"].delete_all_hp_smart_files()
        else:
            smart_utilities.delete_all_hp_smart_files(self.driver.session_data["ssh"])

    def scan_and_save_file_in_hp_smart_files(self, printer_obj, file_name, no_of_pages=2, file_type="PDF",
                                             go_home=True):
        self.go_scan_screen_from_home(printer_obj)
        self.add_multi_pages_scan(no_of_pages)
        btn = IOSPreview.SHARE_SAVE_TITLE if pytest.platform == "IOS" else MacScan.SHARE_BTN
        self.save_file_to_hp_smart_files_and_go_home(file_name, btn, file_type, go_home=go_home)

    ###############################################################################################################
    #
    #                              SCANNER  //  PREVIEW
    #
    ###############################################################################################################

    def go_scan_screen_from_home(self, printer_obj):
        """
        :param printer_obj: Printer object to connect
        :param select_scan_tile: Default is False, Set to True to select Scan Tile
        :return:
        """
        p = printer_obj.get_printer_information()
        if self.fd["scan"].verify_preview_button_on_scan_screen(raise_e=False):
            return True
        self.go_to_home_screen()
        if self.fd["home"].verify_printer_added() is False:
            self.add_printer_by_ip(printer_ip=p["ip address"])
        sleep(2)
        self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        # close coach marks
        if self.fd["scan"].verify_second_close_btn():
            self.fd["scan"].select_second_close_btn()
        self.fd["scan"].verify_scanner_screen()

    def send_and_verify_email(self, from_email_id, to_email_id, subject="", content=""):
        subject = "{}_{}".format(subject, self.driver.driver_info["udid"])
        if pytest.platform == "IOS":
            self.fd["gmail"].compose_and_send_email(to_email=to_email_id, subject_text=subject)
        else:
            smart_utilities.compose_and_send_email(ssh=self.driver.session_data["ssh"], to_email=to_email_id, subject_text=subject)
        time.sleep(5)
        try:
            msg_id = self.fd["gmail_api"].search_for_messages(q_from=from_email_id, q_to=to_email_id, q_unread=True,
                                                            q_subject=subject, q_content=content, timeout=300)
            msg = self.fd["gmail_api"].gmail.get_message(msg_id[0]["id"])
            self.fd["gmail_api"].delete_email(msg_id)
        except TypeError:
            if pytest.platform == "MAC":
                smart_utilities.close_mail_app(ssh=self.driver.session_data["ssh"])
            raise TypeError("Email not found")
        if pytest.platform == "MAC":
            smart_utilities.close_mail_app(ssh=self.driver.session_data["ssh"])
        return msg

    def add_multi_pages_scan(self, no_of_pages):
        for page in range(1, no_of_pages + 1):
            self.fd["scan"].select_scan_job()
            self.fd["common_preview"].nav_detect_edges_screen()
            self.fd["common_preview"].verify_preview_screen()
            if page == no_of_pages:
                break
            else:
                self.fd["common_preview"].select_add_page()

    def create_and_save_file_using_camera_scan_and_go_home(self, file_name, file_type="jpg"):
        self.go_camera_screen_from_home()
        self.multiple_manual_camera_capture(1)
        self.fd["common_preview"].verify_preview_screen()
        self.save_file_to_hp_smart_files_and_go_home(file_name, IOSPreview.SHARE_SAVE_TITLE, file_type=file_type)

    def navigate_to_share_save_screen(self, printer_obj, option="", use_str_id=True):
        if not self.fd["common_preview"].verify_title(IOSPreview.SHARE_SAVE_TITLE, raise_e=False, use_str_id=use_str_id):
            self.go_scan_screen_from_home(printer_obj)
            if option == "Photo":
                self.fd["scan"].verify_an_element_and_click(Scan.PHOTO, raise_e=True)
            elif option == "Document":
                self.fd["scan"].verify_an_element_and_click(Scan.DOCUMENT, raise_e=True)
            self.fd["scan"].select_scan_job_button()
            if pytest.platform == "IOS":
                self.fd["common_preview"].nav_detect_edges_screen()
                self.fd["common_preview"].verify_preview_screen()
                self.fd["common_preview"].select_bottom_nav_btn(IOSPreview.SHARE_SAVE_TITLE)
                self.fd["common_preview"].verify_title(IOSPreview.SHARE_SAVE_TITLE)
            else:
                # Navigating to the share screen on mac since we never call this method to save a file on mac
                # Saving a file to HP Smart Files is also done on the share screen
                self.fd["scan"].verify_top_navbar_button_and_click(MacScan.SHARE_BTN)
                self.fd["common_preview"].verify_title(IOSPreview.SHARE_TITLE, use_str_id=use_str_id)

    def load_text_extract(self, printer=None, from_preview=False, pages=1, to_text_edit=True):
        """
        Loads the text extract screen
        :param printer: The printer to scan with. If not specified uses camera
        :param from_preview: Capture images in document mode and load text extract from preview screen
        :param pages: The number of pages to load, ignored if from_preview=False
        :param to_text_edit: Select continue button on initial text extract screen
        """
        if printer:
            self.go_scan_screen_from_home(printer)
        else:
            self.go_camera_screen_from_home()
        self.fd["camera"].select_preset_mode(self.fd["camera"].DOCUMENT if from_preview else self.fd["camera"].TEXT_EXTRACT)
        if from_preview:
            self.add_multi_pages_scan(pages)
            self.fd["common_preview"].select_top_toolbar_btn(self.fd["common_preview"].TEXT_EXTRACT_BTN)
        else:
            self.fd["camera"].select_capture_btn()
        self.fd["common_preview"].verify_text_extract_screen(timeout=40)
        if to_text_edit:
            self.fd["common_preview"].select_continue()
            self.fd["text_extract"].verify_text_extract_screen()

    # ------------------------------------------------------CAMERA---------------------------------------------------- #

    def go_camera_screen_from_home(self, tile=False):
        if not self.fd["home"].verify_home_tile():
            self.go_to_home_screen()
        if tile:
            self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        else:
            self.fd["home"].select_scan_icon()
        self.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fd["camera"].verify_second_close_btn(timeout=5):
            self.fd["camera"].select_second_close_btn()
        if not self.fd["camera"].verify_camera_adjust_text_to_capture_image(timeout=5, raise_e=False):
            self.fd["camera"].select_source_button()
            self.fd["camera"].select_source_option(self.fd["camera"].OPTION_CAMERA)
        if self.fd["camera"].verify_second_close_btn(timeout=5):
            self.fd["camera"].select_second_close_btn()
        self.fd["camera"].verify_camera_screen()

    def capture_image_and_go_to_preview(self, verify_messages=True):
        self.fd["scan"].select_scan_job_button(verify_messages=verify_messages)
        self.fd["common_preview"].nav_detect_edges_screen()
        self.fd["common_preview"].verify_preview_screen()

    def multiple_manual_camera_capture(self, number, flash_option=i_const.FLASH_MODE.FLASH_OFF, preview_title=IOSPreview.PREVIEW_TITLE, use_str_id=True):
        """
        Precondition: start on the Camera flow
        :param number: number of images to take
        :param flash_option: flash mode for the camera
        :return: None
        """
        if self.fd["camera"].verify_second_close_btn():
            self.fd["camera"].select_second_close_btn()
        self.fd["camera"].capture_manual_photo_by_camera(flash_option)
        for _ in range(number - 1):
            self.fd["common_preview"].verify_title(preview_title, use_str_id=use_str_id, timeout=15)
            self.fd["common_preview"].select_add_page()
            self.fd["camera"].capture_manual_photo_by_camera(flash_option)
        self.fd["common_preview"].dismiss_feedback_popup(timeout=5)
        self.fd["common_preview"].verify_title(preview_title, use_str_id=use_str_id)

    ###############################################################################################################
    #
    #                              SHARE  //  SAVE //
    #
    ###############################################################################################################

    def save_file_to_hp_smart_files_and_go_home(self, file_name, option, file_type="jpg", go_home=True):
        """
        :param file_name: File name to rename file
        :param option:Select Save or Share option from tool bar and corresponding button
        :return:
        """
        if pytest.platform == "IOS":
            if not self.fd["common_preview"].verify_title(option, raise_e=False):
                self.fd["common_preview"].select_bottom_nav_btn(option)
        else:
            if not self.fd["common_preview"].verify_title(IOSPreview.SHARE_TITLE, raise_e=False):
                self.fd["scan"].verify_top_navbar_button_and_click(option, raise_e=False)
        self.fd["common_preview"].dismiss_file_types_coachmark(timeout=3)
        self.fd["common_preview"].rename_file(file_name)
        file_types = {
            "jpg": self.fd["common_preview"].IMAGE_JPG,
            "PDF": self.fd["common_preview"].BASIC_PDF,
            "PNG": self.fd["common_preview"].IMAGE_PNG,
            "TIF": self.fd["common_preview"].IMAGE_TIF,
            "HEIF": self.fd["common_preview"].IMAGE_HEIF,
            "docx": self.fd["common_preview"].WORD_DOCUMENT,
            "txt": self.fd["common_preview"].PLAIN_TXT
        }
        self.fd["common_preview"].select_file_type(file_types[file_type])
        if pytest.platform == "IOS":
            self.fd["common_preview"].select_button(IOSPreview.SHARE_SAVE_BTN)
        else:
            self.fd["common_preview"].verify_an_element_and_click(IOSPreview.CONTINUE_BUTTON)
        self.fd["share"].verify_share_popup()
        self.save_file_and_handle_pop_up(go_home=go_home)

    def save_file_and_handle_pop_up(self, go_home=False):
        self.fd["share"].select_save_to_hp_smart()
        self.fd["common_preview"].verify_file_saved_pop_up()
        if go_home:
            self.fd["common_preview"].click_go_to_home_button()
            if pytest.platform == "IOS":
                self.fd["home"].close_print_anywhere_pop_up()
            self.fd["home"].verify_home_tile()
            if pytest.platform == "MAC":
                self.fd["home"].enter_full_screen_mode()
        else:
            self.fd["common_preview"].dismiss_file_saved_popup()
            self.fd["common_preview"].verify_title(IOSPreview.PREVIEW_TITLE)

    ###############################################################################################################
    #
    #                             Print// Print Settings
    #
    ###############################################################################################################

    def select_a_file_and_go_to_print_preview(self, file_name, file_type="pdf", select_tile=True):
        self.go_hp_smart_files_screen_from_home(select_tile)
        self.fd["files"].select_a_file("{}.{}".format(file_name, file_type))
        self.fd["common_preview"].go_to_print_preview_pan_view()

    def scan_and_go_to_print_preview_pan_view(self, printer_obj):
        self.go_scan_screen_from_home(printer_obj)
        # Close the coach marks to capture scan
        if self.fd["scan"].verify_second_close_btn():
            self.fd["scan"].select_second_close_btn()
        self.fd["scan"].select_scan_job_button()
        self.fd["common_preview"].nav_detect_edges_screen()
        self.fd["common_preview"].verify_preview_screen()
        self.fd["common_preview"].go_to_print_preview_pan_view()

    @SPL_decorator.print_job_decorator()
    # Long wait time is to verify print job completion
    def select_print_button_and_verify_print_job(self, printer_obj, timeout=70):
        """
        On Print Preview Page, press print button and verify print success on HP smart and printer
        :param printer_obj:
        :return:
        """
        self.fd["common_preview"].select_print_size(raise_e=False)
        printer_status = printer_obj.get_printer_status()
        if printer_obj.is_printer_status_ready():
            if not self.fd["common_preview"].verify_button(IOSPreview.PRINT_BTN):
                self.fd["common_preview"].select_bottom_nav_btn(IOSPreview.PRINT_BTN)
            sleep(5)
            self.fd["common_preview"].dismiss_print_preview_coachmark()
            if pytest.platform == "IOS":
                self.fd["common_preview"].select_button(IOSPreview.PRINT_BTN)
            else:
                self.driver.click_using_frame(IOSPreview.PRINT_BTN)
            self.fd["common_preview"].verify_job_sent_and_reprint_buttons_on_print_preview(timeout=timeout)
        else:
            raise PrinterNotReady("Printer is NOT ready. Printer Status is: {}".format(printer_status))

    def select_and_get_print_option_value(self, print_option, value, scroll=False):
        self.fd["common_preview"].verify_an_element_and_click(print_option, scroll=scroll)
        self.fd["common_preview"].select_static_text(value)
        self.fd["common_preview"].select_navigate_back()
        self.fd["common_preview"].verify_button(IOSPreview.PRINT_BTN)
        return self.fd["common_preview"].get_option_selected_value(print_option)


    ###############################################################################################################
    #
    #                              Printer Settings screen
    #
    ###############################################################################################################

    def go_to_printer_settings_screen(self, printer_obj):

        p = printer_obj.get_printer_information()
        if self.fd["printer_settings"].verify_printer_settings_screen(raise_e=False):
            return True
        self.go_to_home_screen()
        if self.fd["home"].verify_printer_added() is False:
            self.add_printer_by_ip(printer_ip=p["ip address"])
        self.fd["home"].close_smart_task_awareness_popup()
        # Tap printer icon and go to printer settings screen
        self.fd["home"].click_on_printer_icon()
        if self.fd["printer_settings"].verify_allow_while_using_app(raise_e=False):
            self.fd["printer_settings"].handle_location_popup()
        self.fd["printer_settings"].verify_printer_settings_screen(raise_e=True)

    ###############################################################################################################
    #
    #                                     Edit Feature
    #
    ###############################################################################################################

    def go_to_edit_screen_with_printer_scan_image(self, printer_obj):
        if self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE) is False:
            self.go_scan_screen_from_home(printer_obj)
            self.fd["scan"].select_scan_job_button()
            sleep(2)
            self.fd["preview"].nav_detect_edges_screen()
            self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    def go_to_edit_screen_with_camera_scan_image(self, no_of_images=1):
        if self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE) is False:
            self.go_camera_screen_from_home(tile=True)
            self.multiple_manual_camera_capture(no_of_images)
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    def get_preview_img_and_go_to_edit_screen(self):
        self.select_multiple_photos_to_preview(no_of_photos=1)
        preview_image = self.fd["preview"].preview_img_screenshot()
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()
        return preview_image

    def go_to_edit_screen_with_selected_photo(self, no_of_photos=1):
        if self.fd["common_preview"].verify_title(IOSPreview.PREVIEW_TITLE, raise_e=False) is False:
            self.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.fd["common_preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    ###############################################################################################################
    #
    #                                     Preview Landing screen
    #
    ###############################################################################################################

    def verify_preview_screen_and_go_home(self):
        self.fd["edit"].select_edit_done()
        self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fd["preview"].select_navigate_back()
        self.fd["preview"].select_yes_go_home_btn()

    def select_a_file_and_go_to_preview_screen(self, file_name, file_type, select_tile=False):
        self.go_hp_smart_files_screen_from_home(select_tile)
        self.fd["files"].select_a_file("{}.{}".format(file_name, file_type))

    ###############################################################################################################
    #
    #                                     Soft Fax
    #
    ###############################################################################################################

    def add_mobile_fax_tile(self):
        self.fd["home"].select_personalize_btn()
        self.fd["personalize"].verify_personalize_screen()
        self.fd["personalize"].toggle_switch_by_name(self.fd["personalize"].MOBILE_FAX_SWITCH, on=True)
        self.fd["personalize"].select_done()
        self.fd["home"].close_smart_task_awareness_popup()
        self.dismiss_tap_here_to_start()
        self.fd["home"].verify_home()

    def nav_to_compose_fax(self, new_user=False):
        """
        Method used to reach compose new fax screen.

        Args:
            new_user (bool, optional): True if new user needs to be created. Defaults to False.
        """
        self.nav_to_fax_history_screen(new_user=new_user)
        if not new_user:
            self.fd["softfax_fax_history"].click_compose_new_fax()
            sleep(2)
            self.fd["softfax_compose_fax"].verify_compose_fax_screen()
            
    def nav_to_fax_history_screen(self, new_user=False):
        """
        Method used to navigate to the fax history screen

        Args:
            new_user (bool, optional): True if new user is needed, False otherwise
        """
        
        if self.fd["home"].verify_home(raise_e=False) is False:
            self.go_to_home_screen()
        if self.fd["home"].verify_tile_displayed(i_const.HOME_TILES.TILE_MOBILE_FAX) is False:
            self.add_mobile_fax_tile()
        self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_MOBILE_FAX)
        # Login screen briefly appears then disappears, we need to check twice
        login_screen, _ = self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=10, raise_e=False)
        if login_screen is not None:
            sleep(3)
            login_screen, _ = self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=10, raise_e=False)
            if login_screen is not None:
                self.login_value_prop_screen(tile=True)
        if new_user:
            self.verify_fax_welcome_screens_and_nav_compose_fax()
        else:
            self.driver.wait_for_context(w_const.WEBVIEW_URL.SOFTFAX, timeout=30)
            self.fd["softfax_compose_fax"].click_fax_feature_update_dismiss_btn(raise_e=False)
            self.fd["softfax_fax_history"].verify_fax_history_screen()

    def delete_multiple_fax_records(self, draft_tab=False, first_run=True, go_home=True):
        """
        Recursive method that calls itself until all records of
        the SENT/DRAFT are deleted.
        The method should be called from fax history screen in order to work properly.
        """
        # Get to fax history screen
        if first_run:
            self.nav_to_fax_history_screen()
            self.fd["softfax_fax_history"].verify_fax_history_screen()
        # Check if the method is used for sent or draft tabs and select the needed tab.
        if draft_tab:
            self.fd["softfax_fax_history"].select_tab(self.fd["softfax_fax_history"].DRAFT_TAB)
            needed_locator_tab = "draft_record_date_txt"
        else:
            needed_locator_tab = "sent_record_date_txt"
        # Switch to webview context
        if "WEBVIEW" not in self.driver.context:
            self.driver.switch_to_webview(webview_url='sws')
        # Reach the edit fax history
        empty_list_locator = "empty_draft_message" if draft_tab else "empty_sent_fax_message"
        empty_list_check = self.driver.wait_for_object(empty_list_locator, timeout=3, raise_e=False)
        # If the list of faxes is empty, skip the deletion.
        if not empty_list_check:
            self.fd["softfax_fax_history"].load_fax_edit_screen_from_fax_history(draft_tab=draft_tab)
            self.fd["softfax_fax_history"].verify_edit_screen()
            # Get each present fax displayed on screen
            fax_list_elements = self.driver.find_object(needed_locator_tab, multiple=True, raise_e=False)
            # Select faxes from list
            for element_index, _ in enumerate(fax_list_elements):
                self.driver.click(needed_locator_tab, index=element_index)
            # Delete the selected records
            self.driver.click("edit_delete_btn")
            self.driver.click("delete_popup_delete_btn")
            # Call the method again to delete remaining emails
            self.delete_multiple_fax_records(draft_tab=draft_tab, first_run=False, go_home=go_home)
        if go_home:
            self.go_home(reset=True, stack=self.stack, button_index=1)

    def recipient_info_for_os(self):
        """
        Assigning recipient for iOS version to avoid over stepping
        """
        recipients = {
                "15": "recipient_09",
                "16": "recipient_02",
                "17": "recipient_09"
                }
        device_os = self.driver.platform_version
        recipient_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.SOFTFAX_ACCOUNT))["softfax"][recipients[device_os]]
        return recipient_info

    def select_file_from_hp_smart_files(self, file_name, file_type="pdf"):
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["files"].verify_files_screen()
        self.fd["files"].select_hp_smart_files_folder_icon()
        self.fd["files"].verify_hp_smart_files_screen()
        self.fd["files"].select_a_file("{}.{}".format(file_name, file_type))

    def select_photo_from_photo_picker(self, no_of_photos=1, select_all_files=True):
        self.fd["photos"].select_allow_access_to_photos_popup()
        if select_all_files:
            self.fd["files"].select_all_files_image()
        else:
            self.fd["photos"].select_albums_tab()
        self.fd["photos"].select_recents_or_first_option()
        self.fd["photos"].verify_photos_screen()
        self.fd["photos"].select_multiple_photos(end=no_of_photos)
        self.fd["photos"].select_next_button(raise_e=False)

    def verify_fax_welcome_screens_and_nav_compose_fax(self):
        self.driver.wait_for_context(w_const.WEBVIEW_URL.SOFTFAX_OFFER, timeout=30)
        self.fd["softfax_offer"].verify_get_started_screen()
        self.fd["softfax_offer"].skip_get_started_screen()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.SOFTFAX, timeout=30)
        self.fd["softfax_welcome"].verify_welcome_screen()
        self.fd["softfax_welcome"].skip_welcome_screen()
        self.fd["softfax_compose_fax"].click_fax_feature_update_compose_new_fax_btn(raise_e=False)
        self.fd["softfax_compose_fax"].verify_compose_fax_screen()

    def delete_contact(self, is_deleted=True):
        self.fd["softfax_contacts"].click_edit_contact_delete()
        self.fd["softfax_contacts"].verify_edit_delete_confirmation_popup()
        self.fd["softfax_contacts"].dismiss_edit_delete_confirmation_popup(is_deleted=is_deleted)

    def delete_all_contacts(self):
        contacts_list = self.fd["softfax_contacts"].get_contact_list()
        if contacts_list is False:
            logging.info("Contact list is empty")
        else:
            for _ in range(len(contacts_list)):
                contact = self.fd["softfax_contacts"].get_contact_list(multiple=False)
                self.fd["softfax_contacts"].select_info_icon(contact)
                self.delete_contact()

    def nav_to_contacts_screen(self):
        if self.fd["softfax_contacts"].verify_contact_screen_title() is False:
            self.fd["softfax_compose_fax"].click_contacts_icon()
            self.fd["softfax_contacts"].verify_contact_screen_title()

    def nav_to_fax_settings_screen(self, fax_settings_option=None, stack="pie"):
        if not self.fd["softfax_compose_fax"].verify_compose_fax_screen(raise_e=False):
            self.nav_to_compose_fax()
        self.fd["softfax_compose_fax"].click_menu_option_btn(self.fd["softfax_compose_fax"].MENU_FAX_SETTINGS_BTN)
        self.fd["softfax_compose_fax"].handle_save_as_draft_popup("save_as_draft_popup_exit_bn")
        self.fd["fax_settings"].verify_fax_settings_screen()
        if fax_settings_option is not None:
            self.fd["fax_settings"].click_fax_settings_option(fax_settings_option)

    # Random utility to generate string
    @staticmethod
    def get_random_str(length=4):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def load_account_and_go_to_smart_dashboard(self, stack="pie", account_type="ucde"):
        account = ma_misc.get_hpid_account_info(stack=stack, a_type=account_type, instant_ink=True)
        self.go_home(reset=True, stack=stack, username=account["email"], password=account["password"])
        self.navigate_to_smart_dashboard()

    def navigate_to_smart_dashboard(self):
        self.fd["home"].select_account_icon()
        self.fd["smb"].verify_account_menu()
        self.fd["smb"].select_manage_hp_account()
        self.fd["hp_connect"].accept_privacy_popup(delay=1)
        self.fd["hp_connect"].verify_account_summary(timeout=40)

    def load_smart_dashboard_help_center(self, stack, account_type):
        self.load_account_and_go_to_smart_dashboard(stack=stack, account_type=account_type)
        self.fd["hp_connect"].click_menu_toggle(change_check={"wait_obj": "close_hamburger_menu_btn"})
        self.fd["hp_connect"].click_help_center_btn()
        self.fd["hpc_help_center"].verify_help_center_menu()

    def load_smart_dashboard_hp_instant_ink(self, stack, account_type):
        self.load_account_and_go_to_smart_dashboard(stack=stack, account_type=account_type)
        self.fd["hp_connect"].click_menu_toggle(change_check={"wait_obj": "close_hamburger_menu_btn"})
        self.fd["hpc_instant_ink"].click_hp_instant_ink_btn()
        self.fd["hpc_instant_ink"].verify_hp_instant_ink_menu_screen()

    def export_app_log_to_files(self, export_method="files"):
        """
        Function to export app logs
        @export method:
        1. files - Export zip file to Files application on iOS device
        2. email - Email zip file to base account
        """
        self.go_to_home_screen()
        self.fd["home"].select_app_settings()
        self.fd["app_settings"].select_share_logs()
        if export_method == "files":
            path = pytest.test_result_folder
            _ ,tail = os.path.split(os.path.split(path)[0])
            self.fd["app_settings"].verify_an_element_and_click("save_to_files", raise_e=True)
            self.fd["app_settings"].verify_an_element_and_click("logs_option", raise_e=True)
            file_name = "Logs_" + tail
            self.fd["app_settings"].rename_file("folder_name", file_name=file_name)
            self.fd["app_settings"].verify_an_element_and_click("done_btn", raise_e=True)
            self.fd["app_settings"].verify_an_element_and_click("save_btn", raise_e=True)
            # Pull file from iOS Files application
            zip = self.driver.wdvr.pull_file("@com.hp.printer.control.dev:documents/" + file_name + ".zip")
            return zip
        else:
            receiver_email = self.driver.session_data["hpid_user"]
            path = pytest.test_result_folder
            _ ,tail = os.path.split(os.path.split(path)[0])
            subject = "Logs_" + tail
            self.fd["app_settings"].send_app_logs_via_email(email=receiver_email, subject=subject)

    ###############################################################################################################
    #
    #                                     Shortcuts
    #
    ###############################################################################################################

    def navigate_to_add_shortcuts_screen(self):
        """
        - Click on Add Shortcut button on Shortcuts screen
        - Verify Add Shortcut screen
        - Click on Create your Own Shortcut button
        - Verify Add your own shortcut screen
        """
        self.navigate_to_shortcuts_screen()
        self.fd["shortcuts"].click_add_shortcut()
        self.fd["shortcuts"].verify_add_shortcuts_screen()
        self.fd["shortcuts"].click_create_your_own_shortcut_btn()
        self.fd["shortcuts"].verify_add_your_own_shortcut_screen()

    def navigate_to_shortcuts_screen(self):
        """
        navigate to shortcuts screen
        """
        self.go_to_home_screen()
        self.fd["home"].select_tile_by_name(i_const.HOME_TILES.TILE_SMART_TASK, change_check={"wait_obj": i_const.HOME_TILES.TILE_SMART_TASK, "invisible": True})
        self.fd["shortcuts"].dismiss_source_select_popup()
        self.fd["shortcuts"].verify_shortcuts_screen(timeout=35)

    def save_shortcut(self, shortcuts_name, invisible=False, click_home=True, is_first_time=False, click_start_shortcut=False):
        if pytest.platform == "IOS":
            self.fd["shortcuts"].click_add_to_shortcut_btn()
            self.fd["shortcuts"].click_continue_btn()
            self.fd["shortcuts"].verify_settings_screen(invisible)
        self.fd["shortcuts"].enter_shortcut_name(shortcuts_name)
        self.fd["shortcuts"].click_save_shortcut_btn()
        self.fd["shortcuts"].verify_shortcut_saved_screen(timeout=15, is_first_time=is_first_time)
        if click_home:
            self.fd["shortcuts"].click_home_btn()
        elif click_start_shortcut:
            self.fd["shortcuts"].click_start_shortcut_btn()

    ###############################################################################################################
    #                                         Novelli
    ###############################################################################################################

    def load_two_sided_preview_screen_for_novelli(self, printer_obj, is_back_screen=False):
        """
        1. Connect to a novelli printer to smart app
        2. Load app to two sided preview screen through My Photos
        """
        p = printer_obj.get_printer_information()
        self.go_to_home_screen()
        self.add_printer_by_ip(printer_ip=p["ip address"])
        self.dismiss_tap_here_to_start()
        self.fd["home"].close_smart_task_awareness_popup()
        self.fd["home"].select_documents_icon()
        self.fd["photos"].select_allow_access_to_photos_popup(allow_access=True)
        self.fd["photos"].select_albums_tab()
        self.fd["photos"].verify_an_element_and_click(self.fd["photos"].RECENT_PHOTOS_TEXT)
        self.fd["photos"].verify_select_photos_btn()
        self.fd["photos"].select_multiple_photos(end=1)
        self.fd["photos"].select_next_button()
        self.fd["preview"].verify_print_size_screen()
        self.fd["preview"].select_print_size_btn(self.fd["preview"].PRINT_SIZE_4x6_TWO_SIDED)
        self.fd["preview"].dismiss_quickly_switch_sides_coachmark()
        self.fd["preview"].verify_two_sided_preview_screen()
        if is_back_screen:
            self.fd["preview"].select_back_button()

    def load_edit_screen_for_novelli(self, printer_obj, edit_option, is_back_screen=False):
        """
        1. Connect to a novelli printer to smart app
        2. Load app to two sided preview screen through My Photos
        3. Select Edit
        4. Select specified edit option
        """
        self.load_two_sided_preview_screen_for_novelli(printer_obj, is_back_screen=is_back_screen)
        self.fd["preview"].select_delete_page_icon()
        self.fd["preview"].select_edit(change_check={"wait_obj": "print_size_screen_title", "invisible": True})
        self.fd["edit"].dismiss_template_coachmark()
        self.fd["edit"].verify_edit_page_title()
        self.fd["edit"].select_edit_main_option(edit_option)
        self.fd["edit"].verify_screen_title(edit_option)
    
    ###############################################################################################################
    #                                                                                                             #
    #                                     Mac Functions                                                           #
    #                                                                                                             #
    ###############################################################################################################
    
    def switch_window_and_modify_wn(self, flow_key, window_name, wait_for_new_window=True):
        self.web_driver.add_window_and_switch(window_name, wait_for_new_window=wait_for_new_window)
        self.fd[flow_key].wn = window_name
    
    def reset_hp_smart_mac(self):
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        smart_utilities.uninstall_app(self.driver)
        smart_utilities.install_hp_smart(self.driver)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
    
    def delete_window_and_activate_hp_smart(self, window_name, close_window=False):
        if close_window:
            self.web_driver.close_window(window_name)
        self.web_driver.switch_window()
        if not close_window:
            self.web_driver.delete_window_from_table(window_name)
        self.driver.activate_app(i_const.BUNDLE_ID.SMART)