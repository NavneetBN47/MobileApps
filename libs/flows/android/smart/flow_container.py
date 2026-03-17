import os
import time
import socket
import logging
import datetime
from selenium.common.exceptions import TimeoutException, WebDriverException

from SAF.misc import saf_misc
from SPL.decorator import SPL_decorator
from MobileApps.libs.ma_misc import ma_misc
from SPL.driver.reg_printer import PrinterNotReady
from SAF.exceptions.saf_exceptions import WindowNotFound
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory

from MobileApps.libs.flows.android.google_chrome.google_chrome import GoogleChrome
from MobileApps.libs.flows.android.google_drive.google_drive import GoogleDrive
from MobileApps.libs.flows.android.hpps.hp_print_service import HP_Print_Service
from MobileApps.libs.flows.android.hpps.job_notification import Job_Notification
from MobileApps.libs.flows.android.hpps.trap_door import Trap_Door
from MobileApps.libs.flows.android.hpps.hpps_settings import HPPS_Settings
from MobileApps.libs.flows.android.smart.about import About
from MobileApps.libs.flows.android.smart.app_settings import AppSettings
from MobileApps.libs.flows.android.smart.digital_copy import DigitalCopy
from MobileApps.libs.flows.android.smart.debug_settings import DebugSettings
from MobileApps.libs.flows.android.smart.file_photos import FilePhotos
from MobileApps.libs.flows.android.smart.local_files import LocalFiles
from MobileApps.libs.flows.android.smart.gmail import Gmail
from MobileApps.libs.flows.android.smart.home import Home
from MobileApps.libs.flows.android.smart.how_to_print import HowToPrint
from MobileApps.libs.flows.android.smart.hpx_printer_details import HPXPrinterDetails
from MobileApps.libs.flows.android.smart.hpx_local_photos import HPXLocalPhotos
from MobileApps.libs.flows.android.smart.moobe_awc import MoobeAWC
from MobileApps.libs.flows.android.smart.moobe_ows import MoobeOWS
from MobileApps.libs.flows.android.smart.moobe_setup_complete import MoobeSetupComplete
from MobileApps.libs.flows.android.smart.online_documents import OnlineDocuments
from MobileApps.libs.flows.android.smart.online_photos import OnlinePhotos
from MobileApps.libs.flows.android.smart.personalize import Personalize
from MobileApps.libs.flows.android.smart.local_photos import LocalPhotos
from MobileApps.libs.flows.android.smart.print_preference import PrintPreference
from MobileApps.libs.flows.android.smart.printer_settings import PrinterSettings
from MobileApps.libs.flows.android.smart.printers import Printers
from MobileApps.libs.flows.android.smart.hpx_shortcuts import HpxShortcuts
from MobileApps.libs.flows.android.smart.dev_settings import DevSettings
from MobileApps.libs.flows.android.smart.job_notification import JobNotification
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.softfax.softfax_offer import SoftfaxOffer
from MobileApps.libs.flows.web.softfax.compose_fax import ComposeFax
from MobileApps.libs.flows.web.softfax.contacts import MobileContacts
from MobileApps.libs.flows.web.softfax.send_fax_details import SendFaxDetails
from MobileApps.libs.flows.web.softfax.softfax_welcome import SoftfaxWelcome
from MobileApps.libs.flows.web.softfax.fax_history import MobileFaxHistory
from MobileApps.libs.flows.web.softfax.fax_settings import FaxSettings
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.smart.smart_welcome import SmartWelcome
from MobileApps.libs.flows.web.smart.privacy_preferences import PrivacyPreferences
from MobileApps.libs.flows.web.smart.scribble import Scribble
from MobileApps.libs.flows.web.ows.value_prop import OWSValueProp
from MobileApps.libs.flows.web.smart.shortcuts_notification import ShortcutsNotification
from MobileApps.libs.flows.android.system_flows.sys_flow_factory import system_flow_factory
from MobileApps.libs.flows.android.dropbox.dropbox import Dropbox
from MobileApps.libs.flows.common.smart.smb import AndroidSmb
from MobileApps.libs.flows.common.smart.edit import AndroidEdit
from MobileApps.libs.flows.common.smart.scan import AndroidScan
from MobileApps.libs.flows.android.smart.notification import Notification
from MobileApps.libs.flows.web.help_support.help_support import HelpSupport
from MobileApps.libs.flows.web.smart.smart_printer_consent import SmartPrinterConsent
from MobileApps.libs.flows.web.smart.text_notifications import TextNotificationsAndroid
from MobileApps.libs.flows.web.instant_ink.offers import Offers
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from MobileApps.libs.flows.web.hp_connect.hp_connect_basic_account import HPConnectBasicAccount
from MobileApps.libs.flows.web.hp_connect.help_center import HelpCenter
from MobileApps.libs.flows.web.hp_connect.account import Account
from MobileApps.libs.flows.web.hp_connect.features import Features
from MobileApps.libs.flows.web.hp_connect.printers_users import PrintersUsers
from MobileApps.libs.flows.web.hp_connect.hp_instant_ink import HPInstantInk
from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.libs.flows.web.shortcuts.shortcuts_create_edit import MobileShortcutsCreateEdit
from MobileApps.libs.flows.web.cec.custom_engagement_center import CustomEngagementCenter
from MobileApps.libs.flows.web.smart.redaction import Redaction
from MobileApps.libs.flows.common.smart.preview import AndroidPreview
from MobileApps.libs.flows.android.smart.camera_scan import CameraScan
from MobileApps.libs.flows.android.smart.print_preview import PrintPreview
from MobileApps.libs.flows.android.photos.photos import Photos
from MobileApps.libs.flows.android.smart.print_quality_tools import PrintQualityTools
from MobileApps.resources.const.android import const as a_const
from MobileApps.resources.const.web import const as w_const
from MobileApps.libs.flows.android.smart.supplies_status import SuppliesStatus
from MobileApps.resources.const.android.const import SUPPLY_VALIDATION

#HPX imports 
from MobileApps.libs.flows.web.smart.devices_mfe import DevicesMFE
from MobileApps.libs.flows.web.smart.devices_details_printer_mfe import DevicesDetailsPrinterMFE


class HPIDLoginFail(Exception):
    pass

class HPIDCreateFail(Exception):
    pass

class NotFoundMOOBEConnectWifiType(Exception):
    pass

class FLOW_NAMES():
    ABOUT = "about"
    DEBUG_SETTINGS = "debug_settings"
    LOCAL_FILES = "files"
    GMAIL = "gmail"
    HELP_SUPPORT = "help_support"
    HOME = "home"
    HOW_PRINT = "how_to_print"
    HPX_PRINTERS_DETAILS = "hpx_printers_details"
    MOOBE = "moobe"
    ONLINE_DOCS = "online_documents"
    ONLINE_PHOTOS = "online_photos"
    PERSONALIZE = "personalize"
    LOCAL_PHOTOS = "photos"
    PRINT_PREFERENCE = "print_preference"
    PRINTER_SETTINGS = "printer_settings"
    PRINTERS = "printers"
    SCAN = "scan"
    CAMERA_SCAN = "camera_scan"
    DIGITAL_COPY = "digital_copy"
    MOOBE_AWC = "moobe_awc"
    MOOBE_OWS = "moobe_ows"
    MOOBE_SETUP_COMPLETE = "moobe_setup_complete"
    APP_SETTINGS = "app_settings"
    FILES_PHOTOS = "file_photos"
    DEV_SETTINGS = "Dev Settings"
    EDIT = "edit"
    NOTIFICATION = "notification"
    TEXT_NOTIFICATIONS = "text_notifications"
    COMMON_PREVIEW = "common_preview"
    SMB = "smb"
    REDACTION = "redaction"
    SCRIBBLE = "scribble"
    HPX_LOCAL_PHOTOS = "hpx_local_photos"
    # From another apps
    GMAIL_API = "gmail_api"
    HPPS_TRAPDOOR = "hpps_tradoor"
    HPPS_JOB_NOTIFICATION = "hpps_job_notification"
    HPPS = "hp_print_service"
    HPPS_SETTINGS = "hpps_settings"
    GOOGLE_DRIVE = "google_drive"
    GOOGLE_CHROME = "google_chrome"
    HPID = "hpid"
    GOOGLE_CHROME = "google_chrome"
    SYSTEM_FLOW = "system_flow"
    DROPBOX = "dropbox"
    SOFTFAX_OFFER = "softfax_offer"
    COMPOSE_FAX = "compose_fax"
    SEND_FAX_DETAILS = "send_fax_details"
    SOFTFAX_WELCOME = "softfax_welcome"
    SOFTFAX_FAX_HISTORY = "fax_history"
    SOFTFAX_CONTACTS = "softfax_contacts"
    SOFTFAX_FAX_SETTINGS = "fax_settings"
    UCDE_PRIVACY = "ucde_privacy"
    ANDROID_SETTINGS = "android_settings"
    WEB_SMART_WELCOME = "web_smart_welcome"
    PRIVACY_PREFERENCES = "privacy_preferences"
    OWS_VALUE_PROP = "value_prop"
    PRIVACY_SETTINGS = "privacy_settings"
    SMART_PRINTER_CONSENT = "smart_printer_consent"
    INSTANT_INK_OFFERS = "instant_ink_offer"
    HP_CONNECT = "hp_connect"
    HP_CONNECT_BASIC_ACCOUNT = "hp_connect_basic_account"
    HELP_CENTER = "help_center"
    HP_CONNECT_ACCOUNT = "account"
    HP_CONNECT_FEATURES = "features"
    HP_CONNECT_PRINTERS_USERS = "printers_users"
    HP_CONNECT_HP_INSTANT_INK = "hp_instant_ink"
    INSTANT_INK_VALUE_PROPOSITION = "instant_ink_value_proposition"
    YETI_FLOW_CONTAINER = "yeti_flow_container"
    SHORTCUTS = "shortcuts_create_edit"
    CUSTOM_ENGAGEMENT_CENTER = "custom_engagement_center"
    SHORTCUTS_NOTIFICATION = "shortcuts_notification"
    PRINT_PREVIEW = "print_preview"
    PRINT_QUALITY_TOOLS = "print_quality_tools"
    JOB_NOTIFICATION = "job_notification"
    HPX_SHORTCUTS = "hpx_shortcuts"
    PHOTOS = "photos"
    SUPPLIES_STATUS = "supplies_status"

class TILE_NAMES():
    PRINT_PHOTOS = "_shared_print_photos_tile"
    PRINT_DOCUMENTS = "_shared_print_documents_tile"
    HELP_SUPPORT = "_shared_help_support_tile"
    PRINTER_SCAN = "_shared_printer_scan_tile"
    CAMERA_SCAN = "_shared_camera_scan_tile"
    COPY = "_shared_copy_tile"
    SMART_TASKS = "shared_smart_tasks_tile"
    GET_INK = "_shared_get_ink_tile"
    FAX = "_shared_fax_tile"
    PRINTABLES = "_shared_printables_tile"

class FlowContainer(object):
    def __init__(self, driver, hpid_type="ucde", hpx=False, hpid_claimable=False):
        self.driver = driver
        self.hpx = hpx
        self.hpx_on = False
        self.driver.session_data["smart_state"] = {}  # Stores smart app state info, cleared on app reset
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.set_hpid_account(hpid_type, claimable=hpid_claimable)
        self.pkg_name = a_const.PACKAGE.SMART(self.driver.session_data["pkg_type"])
        self.smart_context = a_const.WEBVIEW_CONTEXT.SMART(self.driver.session_data["pkg_type"])
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)

        self.fd = {
            FLOW_NAMES.ABOUT: About(driver),
            FLOW_NAMES.DEBUG_SETTINGS: DebugSettings(driver),
            FLOW_NAMES.APP_SETTINGS: AppSettings(driver),
            FLOW_NAMES.FILES_PHOTOS:FilePhotos(driver),
            FLOW_NAMES.LOCAL_FILES: LocalFiles(driver),
            FLOW_NAMES.GMAIL: Gmail(driver),
            FLOW_NAMES.HOME: Home(driver),
            FLOW_NAMES.HOW_PRINT: HowToPrint(driver),
            FLOW_NAMES.HPX_PRINTERS_DETAILS: HPXPrinterDetails(driver),
            FLOW_NAMES.ONLINE_DOCS: OnlineDocuments(driver),
            FLOW_NAMES.ONLINE_PHOTOS: OnlinePhotos(driver),
            FLOW_NAMES.PERSONALIZE: Personalize(driver),
            FLOW_NAMES.LOCAL_PHOTOS: LocalPhotos(driver),
            FLOW_NAMES.HPX_LOCAL_PHOTOS: HPXLocalPhotos(driver),
            FLOW_NAMES.PRINT_PREFERENCE: PrintPreference(driver),
            FLOW_NAMES.PRINTER_SETTINGS: PrinterSettings(driver),
            FLOW_NAMES.PRINTERS: Printers(driver),
            FLOW_NAMES.SCAN: AndroidScan(driver),
            FLOW_NAMES.DIGITAL_COPY: DigitalCopy(driver),
            FLOW_NAMES.MOOBE_AWC: MoobeAWC(driver),
            FLOW_NAMES.MOOBE_OWS: MoobeOWS(driver),
            FLOW_NAMES.MOOBE_SETUP_COMPLETE: MoobeSetupComplete(driver),
            FLOW_NAMES.DEV_SETTINGS: DevSettings(driver),
            FLOW_NAMES.EDIT: AndroidEdit(driver),
            FLOW_NAMES.NOTIFICATION: Notification(driver),
            FLOW_NAMES.TEXT_NOTIFICATIONS: TextNotificationsAndroid(driver, context=self.smart_context),
            FLOW_NAMES.COMMON_PREVIEW: AndroidPreview(driver),
            FLOW_NAMES.SMB: AndroidSmb(driver),
            # Third party apps
            FLOW_NAMES.ANDROID_SETTINGS: android_system_flow_factory(driver),
            FLOW_NAMES.GMAIL_API: GmailAPI(credential_path=a_const.TEST_DATA.GMAIL_TOKEN_PATH),
            FLOW_NAMES.HPPS_TRAPDOOR: Trap_Door(driver),
            FLOW_NAMES.HPPS_JOB_NOTIFICATION: Job_Notification(driver),
            FLOW_NAMES.HPPS: HP_Print_Service(driver),
            FLOW_NAMES.HPPS_SETTINGS: HPPS_Settings(driver),
            FLOW_NAMES.GOOGLE_DRIVE: GoogleDrive(driver),
            FLOW_NAMES.HPID: HPID(driver, context={"url": self.hpid_url}),
            FLOW_NAMES.GOOGLE_CHROME: GoogleChrome(driver),
            FLOW_NAMES.SYSTEM_FLOW: system_flow_factory(driver),
            FLOW_NAMES.DROPBOX: Dropbox(driver),
            FLOW_NAMES.SOFTFAX_OFFER: SoftfaxOffer(driver, context=self.smart_context),
            FLOW_NAMES.COMPOSE_FAX: ComposeFax(driver, context=self.smart_context),
            FLOW_NAMES.SEND_FAX_DETAILS:SendFaxDetails(driver, context=self.smart_context),
            FLOW_NAMES.SOFTFAX_WELCOME: SoftfaxWelcome(driver, context=self.smart_context),
            FLOW_NAMES.SOFTFAX_FAX_HISTORY: MobileFaxHistory(driver, context=self.smart_context),
            FLOW_NAMES.SOFTFAX_CONTACTS: MobileContacts(driver, context=self.smart_context),
            FLOW_NAMES.SOFTFAX_FAX_SETTINGS: FaxSettings(driver, context=self.smart_context),
            FLOW_NAMES.UCDE_PRIVACY: UCDEPrivacy(driver, context=self.smart_context),
            FLOW_NAMES.WEB_SMART_WELCOME: SmartWelcome(driver, context=self.smart_context),
            FLOW_NAMES.PRIVACY_PREFERENCES: PrivacyPreferences(driver, context=self.smart_context),
            FLOW_NAMES.SCRIBBLE: Scribble(driver, context=a_const.WEBVIEW_URL.SCRIBBLE),
            FLOW_NAMES.OWS_VALUE_PROP: OWSValueProp(driver, context=self.smart_context),
            FLOW_NAMES.SMART_PRINTER_CONSENT: SmartPrinterConsent(driver, context=self.smart_context),
            FLOW_NAMES.INSTANT_INK_OFFERS: Offers(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT: HPConnect(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT_BASIC_ACCOUNT:HPConnectBasicAccount(driver, context={"url": self.hpid_url}),
            FLOW_NAMES.HELP_CENTER: HelpCenter(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT_ACCOUNT: Account(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT_FEATURES: Features(driver, context=self.smart_context),
            FLOW_NAMES.YETI_FLOW_CONTAINER: YetiFlowContainer(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT_PRINTERS_USERS: PrintersUsers(driver, context=self.smart_context),
            FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK:HPInstantInk(driver, context=self.smart_context),
            FLOW_NAMES.INSTANT_INK_VALUE_PROPOSITION: ValueProposition(driver, context=self.smart_context),
            FLOW_NAMES.SHORTCUTS: MobileShortcutsCreateEdit(driver, context=self.smart_context),
            FLOW_NAMES.CUSTOM_ENGAGEMENT_CENTER: CustomEngagementCenter(driver, context=self.smart_context),
            FLOW_NAMES.REDACTION: Redaction(driver, context=self.smart_context),
            FLOW_NAMES.CAMERA_SCAN: CameraScan(driver),
            FLOW_NAMES.SHORTCUTS_NOTIFICATION: ShortcutsNotification(driver, context=self.smart_context),
            FLOW_NAMES.PRINT_PREVIEW: PrintPreview(driver),
            FLOW_NAMES.PRINT_QUALITY_TOOLS: PrintQualityTools(driver),
            FLOW_NAMES.JOB_NOTIFICATION: JobNotification(driver),
            FLOW_NAMES.HELP_SUPPORT:HelpSupport(driver, context=self.smart_context),
            FLOW_NAMES.HPX_SHORTCUTS: HpxShortcuts(driver),
            FLOW_NAMES.PHOTOS: Photos(driver),
            FLOW_NAMES.SUPPLIES_STATUS: SuppliesStatus(driver)
        }
        self.hpx_fd = {
            "devicesMFE": DevicesMFE(driver, url="/devices/", context=self.smart_context),
            "devices_details_printerMFE": DevicesDetailsPrinterMFE(driver, url="/device-details/", context=self.smart_context)
        }

    @property
    def flow(self):
        return self.fd

    def set_hpid_account(self, a_type, claimable=None, ii_status=None, smart_advance=None, pro=None, force_reset=False, smb=False):
        """
        Set value for hpid account properties
        :param force_reset: Always reset app if account changed.
        NOTE: Resetting app to swap account is much slower than using app settings.
        """
        original_hpid = self.driver.session_data.get("hpid_user", None)
        if smb:
            account_info = ma_misc.get_smb_account_info(self.stack)
            self.driver.session_data["hpid_user"] = account_info["email"]
            self.driver.session_data["hpid_pass"] = account_info["password"]
        else:
            ma_misc.get_hpid_account_info(self.stack, a_type=a_type, claimable=claimable, instant_ink=ii_status, smart_advance=smart_advance, pro=pro, driver=self.driver)

        if original_hpid is not None and original_hpid != self.driver.session_data["hpid_user"]:  # if account changed make sure new account gets signed in
            self.__terminate()
            if force_reset:
                self.reset_app()
                return True
            self.launch_smart()
            if self.fd[FLOW_NAMES.HOME].verify_home_nav(raise_e=False): # if launches to home screen change account via app settings
                if self.stack != "production":
                    self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
                else:
                    self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_APP_SETTINGS_BTN)
                if self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(raise_e=False):
                    self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()
                self.fd[FLOW_NAMES.APP_SETTINGS].click_sign_in_btn()
                self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
                self.driver.wait_for_context(a_const.WEBVIEW_CONTEXT.CHROME)
                self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
                self.fd[FLOW_NAMES.HPID].login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
                if self.fd[FLOW_NAMES.SMB].select_my_printers(raise_e=False):
                    self.fd[FLOW_NAMES.SMB].select_continue()
                self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(self.driver.session_data["hpid_user"], timeout=30, raise_e=True)
            elif self.driver.wait_for_context(self.smart_context, timeout=20, raise_e=False) == (None, None) or not self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen(raise_e=False):
                # if doesnt launch to home or welcome screen reset app
                self.reset_app()
        return True

    def launch_smart(self):
        if self.hpx and self.hpx_on:
            activity = a_const.LAUNCH_ACTIVITY.SMART_HPX
            wait_activity = None
        else:
            activity = a_const.LAUNCH_ACTIVITY.SMART
            wait_activity = None
        return self.driver.start_activity(self.pkg_name, activity, wait_activity = wait_activity)
    
    def launch_setting_app(self):
        pkg_name = a_const.PACKAGE.SETTINGS
        activity = a_const.LAUNCH_ACTIVITY.SETTINGS
        return self.driver.start_activity(pkg_name, activity, wait_activity=None)
    
    def foreground_and_background_smart(self):
        self.driver.press_key_home()
        self.launch_smart()
        

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         GENERAL FUNCTIONS       ---------------------
    # They are used by multiple flows
    def select_back(self, change_check=None):
        """
        Click on Back button of app
        """
        self.driver.click("_share_back_btn", change_check=change_check)

    def clean_up_download_and_pictures_folders(self):
        """
        Clean up Download and Pictures folders
        """
        folders= [a_const.TEST_DATA.MOBILE_DOWNLOAD, a_const.TEST_DATA.MOBILE_PICTURES]
        for folder in folders:
            if self.verify_existed_file("{}/*".format(folder)):
                self.driver.clean_up_device_folder(folder)

    def reset_app(self):
        """
        Reset Android Smart app:
            - Clear cache of Android Smart app
            because after clearing cache, the options in Dev Settings are setup back to default server, so:
                - Setup stack server
                - Turn off Detect leaks (this step is unnecessary as the default one is off now)
                - Enable Authz Credentials
        """
        self.driver.clear_app_cache(self.pkg_name)
        self.driver.session_data["smart_state"].clear()
        self.flow_home_change_stack_server(self.stack)
        if self.hpx:
            self.flow_home_toggle_hpx()
        
    def run_app_background(self, timeout=1):
        """
        Put app in background for sleep time. Then, launch app again at the same screen
        Note: Cannot use background_app() function from appium 
              because it launches to Home screen instead of the screen before putting app in background
        """
        self.driver.wdvr.background_app(-1)  # put app in background without launching again
        time.sleep(timeout)
        self.driver.press_key_switch_app()
        self.driver.click("_share_application_name")

    def check_is_home(self, timeout=10, raise_e=False):
        is_home = False
        if self.hpx:
            try:
                # While trying to get the home screen it asks for the allow permission popup so handling here
                self.fd[FLOW_NAMES.HOME].check_run_time_permission(timeout=3)
                self.driver.wait_for_context(self.smart_context, timeout=50)
                is_home = self.hpx_fd["devicesMFE"].verify_home_nav(timeout=timeout, raise_e=raise_e)
            except WindowNotFound:
                is_home = False
        else:
            is_home = self.fd[FLOW_NAMES.HOME].verify_home_nav(timeout=timeout, raise_e=False)
        return is_home

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self, skip_value_prop=False, skip_hpid_popup=False, create_acc=False, verify_signin=True, accept_all_change_check=False, home_nav_timeout=10):
        """
        Load to Home screen:
            - Start base activity or launch app
            - If current screen is not Home screen, then it is Welcome screen
                + Skip it

        @param skip_value_prop: skip Value Prop screen or not
        @param create_acc: create new acc or sign in into an account
        @param verify_signin: Verify that HPID is signed in, if not signed in signin through app settings on home screen.
        @return: username, password: parameter's value for skip_value_prop = True
        """
        # Make sure current screen is not in customTabActivity of Chrome
        self.__terminate()
        # Make sure current screen is on mobile device home screen
        self.driver.press_key_home()
        self.launch_smart()
        # After start activity, current screen is not Home screen -> Welcome screen -> skip it
        username = None
        password = None
        if not self.check_is_home(timeout=home_nav_timeout) and self.hpx:
            self.fd[FLOW_NAMES.GOOGLE_CHROME].clear_chrome_cache_and_handle_welcome()
            self.launch_smart()
            self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen()
            aa_change_check = {"wait_obj": "accept_all_btn", "invisible": True} if accept_all_change_check else None
            self.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_accept_all_btn(change_check=aa_change_check, retry=3)
            # Taking time to load from welcome screen to home screen
            time.sleep(3)
            if skip_value_prop:
                self.fd[FLOW_NAMES.HOME].click_continue_as_guest()
            else:
                self.fd[FLOW_NAMES.HOME].click_sign_in()
                self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in(skip_hpid_popup=skip_hpid_popup)
                self.fd[FLOW_NAMES.HPID].login()
            # Commenting out this line code until Webview issue gets fixed
            # self.driver.wait_for_context(self.smart_context, timeout=15)            
            # self.check_is_home(timeout=50)
            return     

        if not self.hpx:
            # Clear all data from Google Chrome for clearing HPID token which haven't been logged out.
            self.fd[FLOW_NAMES.GOOGLE_CHROME].clear_chrome_cache_and_handle_welcome()
            self.launch_smart()
            # Assume first launch, need to grant permissions
            if int(self.driver.platform_version) > 11:
                self.fd[FLOW_NAMES.HOME].check_run_time_permission(timeout=3)
                self.launch_smart()
            self.driver.performance.time_stamp("t0")
            # Start skipping welcome screen
            username, password = self.skip_welcome_screen(skip_value_prop=skip_value_prop, create_acc=create_acc, skip_hpid_popup=skip_hpid_popup, accept_all_change_check=accept_all_change_check)
            # From user onboarding to Home screen will take to 40s-50s. And has CR GDG-1768 for tracking this issue
            self.check_is_home(timeout=50)
            self.driver.performance.stop_timer("hpid_login", raise_e=False)
            self.driver.performance.time_stamp("t11")
        if not skip_value_prop:  # expects hpid to be signed in
            if self.hpx and verify_signin:
                if not self.hpx_fd["devicesMFE"].verify_home_loggedin():
                    self.flow_home_sign_in_hpid_account(create_acc=create_acc)
            
            elif verify_signin and self.fd[FLOW_NAMES.HOME].verify_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_PRINTER_SCAN_BTN, invisible=True, raise_e=False):
                self.flow_home_sign_in_hpid_account(create_acc=create_acc)
                self.select_back(change_check={"wait_obj": "notification_btn", "flow_change": "home", "invisible": False})
                
        if username is not None or password is not None:
            return username, password
        
    def flow_hpx_skip_new_hp_app_popup(self):
        self.fd[FLOW_NAMES.HOME].check_run_time_permission(timeout=3)
        try:
            if self.hpx_fd["devicesMFE"].verify_new_hp_app_popup(raise_e=False):
                self.hpx_fd["devicesMFE"].click_new_hp_app_popup_skip()
        except WindowNotFound:
            return True
        return True

    def flow_load_printer_screen_from_value_prop(self):
        """
        Loads the printer screen from value prop screen
        """
        self.__terminate()
        self.driver.press_key_home()
        self.launch_smart()
        if self.driver.wait_for_context(self.smart_context, timeout=20, raise_e=False) == (None, None) or not self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen(raise_e=False):
            self.reset_app()
            self.launch_smart()
            # Comment out this line code until AIOA-15609 get fixed
            # self.driver.wait_for_context(self.smart_context, timeout=20)
        if self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen(raise_e=False):
            self.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_accept_all_btn()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        # Currently HPID take 10-20s to load to value prop screen.
        self.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen()
        self.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=0)

    def skip_welcome_screen(self, skip_value_prop=False, skip_hpid_popup=False, create_acc=False, accept_all_change_check=True):
        """
        Skip Welcome screen
                + Click on Accept All button
                + On Value Prop screen: based on parameter, there are 3 options
                    + Skip this screen -> skip_value_prop = True
                    + (default) Sign in  -> skip_value_prop = False and create_acc = False 
                    + Create Account -> -> skip_value_prop = False and create_acc = True 
        @param skip_value_prop: skip Value Prop screen or not
        @param create_acc: create new acc or sign in into an account
        @return: username, password: value from creating acc. Otherwise, value from hpid account instant
        """
        # Comment out this line code until AIOA-15609 get fixed. Currently Welcome screen switched to Native app after "Connect to the internet" popup
        time.sleep(3)
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen()
        self.driver.performance.time_stamp("t1")
        time.sleep(1)
        aa_change_check = {"wait_obj": "accept_all_btn", "invisible": True} if accept_all_change_check else None
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_accept_all_btn(change_check=aa_change_check, retry=5)
        self.driver.performance.time_stamp("t3")
        #Currently HPID take 30-40s to load to value prop screen.
        self.driver.wait_for_context(self.smart_context, timeout=40)
        self.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(simple=True, timeout=20)
        self.driver.performance.time_stamp("t4")
        username, password = self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"]
        if skip_value_prop:
            #because of new defect AOA-106, we updated scripts to click on Skip for now button to skip ows value prop screen instead of hardware back button from the device
            self.fd[FLOW_NAMES.OWS_VALUE_PROP].select_tertiary_btn()
        else:
            self.fd[FLOW_NAMES.OWS_VALUE_PROP].select_secondary_btn()
            self.driver.performance.time_stamp("t5")
            self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in(skip_hpid_popup=skip_hpid_popup)
            self.driver.performance.time_stamp("t6")
            if create_acc:
                self.fd[FLOW_NAMES.HPID].click_create_account_link()
                username, password = self.fd[FLOW_NAMES.HPID].create_account()
                self.driver.wait_for_context(self.smart_context, timeout=25)
                self.driver.performance.stop_timer("hpid_create_account")
            else:
                self.fd[FLOW_NAMES.HPID].login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
            if self.fd[FLOW_NAMES.SMB].select_my_printers(raise_e=False):
                self.fd[FLOW_NAMES.SMB].select_continue()
        return username, password

    def flow_home_sign_in_hpid_account(self, create_acc=False, accept_all_change_check=False):
        """
        At Home screen, sign in/ create HPID account
            - Go to App Settings
            - Sign in or create HPID account
        End of flow: App Settings screen
        :param create_acc: sign in or create account
        :param username: use for sign in (creat_acc = False)
        :param password: use for sign in (create_acc = False)
        """
        if self.hpx:
            self.hpx_fd["devicesMFE"].click_home_loggedin()
            self.fd["hpid"].login()
            return
        self.flow_load_home_screen(skip_value_prop=True, accept_all_change_check=accept_all_change_check)

        if self.stack != "production":
            self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_APP_SETTINGS_BTN)
        if create_acc:
            self.flow_app_settings_create_hpid()
        else:
            self.flow_app_settings_sign_in_hpid()

    def flow_home_verify_smart_app_on_userboarding(self, create_acc=False):
        """
        Make sure Android Smart on useronboarding.
        If not, sign in to default account
        """
        if self.fd[FLOW_NAMES.HOME].verify_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_PRINTER_SCAN_BTN, invisible=True, raise_e=False):
            self.flow_home_sign_in_hpid_account(create_acc=create_acc)
            self.flow_load_home_screen()

    def flow_home_verify_ready_printer(self, printer_bonjour):
        """
        Verify connected printer ready via:
            - Ready status icon on Home screen
            - if status icon is invisible, go to printer setting for checking
        :param printer_bonjour: bonjour name of printer
        :return:
        """
        if not self.fd[FLOW_NAMES.HOME].verify_ready_printer_status(raise_e=False):
            self.fd[FLOW_NAMES.HOME].load_printer_info()
            self.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_my_printer(printer_bonjour)
            self.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_ready_status()
            self.select_back()

    def flow_home_select_network_printer(self, printer_obj, is_searched=True, is_loaded=True):
        """
        At Home screen, select target printer and return its status
            - Click on Printer icon on navigation bar
            - At printer screen search for the printer's ip
            - Click printer ip
            - Verify Home screen with target printer
            - If printer already selected nothing happens
        :param printer_obj: SPL printer
        :param is_searched: select printer via searching or not.
        :param is_loaded: check whether printer is loaded at the end of flow at home screen
        :param stack: stack server
        :param username: hpid username for logging in. Default: HPID Account in constant of HPID account
        :param password: hpid password for logging in. Default: HPID Account in constant of HPID account
        """
        if printer_obj.p_obj.serialNumber == self.driver.session_data["smart_state"].get("active_printer_serial", None):
            return True
        if not self.hpx:
            self.fd[FLOW_NAMES.HOME].load_printer_selection()
        else:
            self.hpx_fd["devicesMFE"].click_add_button()
            # In Reskin UI There are 3 options to select the printer
            # 1. Setup New Printer
            # 2. Choose an availablle printer
            # 3. Search by Serial Number
            
        self.fd[FLOW_NAMES.PRINTERS].select_printer_option_add_printer()
        self.fd[FLOW_NAMES.PRINTERS].select_printer(printer_obj.p_obj.ipAddress, wifi_direct=False,
                                                    is_searched=is_searched,
                                                    keyword=printer_obj.p_obj.ipAddress)
        
        if self.fd[FLOW_NAMES.HOME].verify_feature_popup(raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_feature_popup_close()
        self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        self.check_is_home()
        if not self.hpx and is_loaded:
            if not self.fd[FLOW_NAMES.HOME].verify_loaded_printer(raise_e=False):
                logging.info("Printer is connected to Wifi: {} ".format(printer_obj.is_connected_to_wifi()))
        self.driver.session_data["smart_state"]["active_printer_serial"] = printer_obj.p_obj.serialNumber

    def flow_home_set_up_printer(self, printer_obj):
        """
        Use to set up a selected printer which hasn't been completed MOOBE successfully.
        This OWS flow is handled on App side only.
        Note: Currently, It is tested on Malbec which is cleaned up via SPL.exit_oobe()
        """
        if self.fd[FLOW_NAMES.HOME].verify_setup_btn(invisible=False, raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_set_up()
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_checking_printer_status_screen(invisible=False)
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_checking_printer_status_screen(invisible=True)
            self.fd[FLOW_NAMES.MOOBE_OWS].skip_enjoy_hp_account_benefit_screen()
            if self.fd[FLOW_NAMES.MOOBE_OWS].verify_hp_instant_ink_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_moobe_ows()
            if self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].verify_setup_complete_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].select_setup_complete_not_now()
            if self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].verify_print_other_devices_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].select_not_right_now()
            self.flow_load_home_screen()
        else:
            logging.info("Printer ({}) is set up completely".format(printer_obj.p_obj.ipAddress))

    def flow_home_load_scan_screen(self, printer_obj, from_tile=True, verify_signin=True):
        """
        From Home screen, load to Scan screen
            - Select target printer
            - Verify ready printer at Home screen
            - Click on Printer Scan for scanning
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Scan icon on navigation bar
        """
        self.reset_app()
        self.flow_load_home_screen(verify_signin=verify_signin)
        self.flow_home_select_network_printer(printer_obj=printer_obj)
        self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        if self.hpx:
            self.hpx_fd["devicesMFE"].click_device_tile()
            self.hpx_fd["devices_details_printerMFE"].click_scan_tile()
    
        elif from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_PRINTER_SCAN_BTN)
        self.fd[FLOW_NAMES.SCAN].dismiss_coachmark(screen="scanner")
        self.fd[FLOW_NAMES.SCAN].verify_scan_screen(source=self.fd[FLOW_NAMES.SCAN].SOURCE_PRINTER_SCAN_OPT)

    def flow_home_scan_single_page(self, printer_obj, from_tile=True, mode=None, verify_signin=True):
        """
        At Home screen, scan a single_page via a scan tile buttons (Scan, Scan to Email, Scan to Cloud)
            - Select  target network printer via Printer button on navigation bar
            - Verify Home screen with ready target printer
            - Click on a scan tile button on Home screen button.
                Dismiss App Permission if mobile device are Android 6.0 or newer
            - Wait until Scan button is able to click.
                Select Scan button.
            - Verify scan is successful
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Scan icon on navigation bar
        :param mode: The scan mode to select.
        """
        self.flow_home_load_scan_screen(printer_obj, from_tile=from_tile, verify_signin=verify_signin)
        if mode:
            self.fd[FLOW_NAMES.SCAN].select_capture_mode(mode)
        self.fd[FLOW_NAMES.SCAN].start_capture()
        self.fd[FLOW_NAMES.SCAN].verify_successful_scan_job()
        self.fd[FLOW_NAMES.SCAN].verify_adjust_screen(timeout=30)

    def flow_home_load_file_screen(self, printer_obj, printer_bonjour_name, file_name, from_tile=True):
        """
        From Home screen, load to My File screen
            - Select target printer
            - Verify ready printer at Home screen
            - Click on Printer Scan for scanning
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Scan icon on navigation bar
        """
        self.flow_load_home_screen()
        if self.fd[FLOW_NAMES.HOME].verify_printer_model_name(printer_bonjour_name, raise_e=False, timeout=15):
            self.flow_home_select_network_printer(printer_obj=printer_obj)
            self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.PRINT_DOCUMENTS))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].PDF_TXT)
        self.fd[FLOW_NAMES.LOCAL_FILES].load_downloads_folder_screen()
        self.fd[FLOW_NAMES.LOCAL_FILES].select_file(file_name=file_name)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_print_size(self.fd[FLOW_NAMES.COMMON_PREVIEW].PRINT_SIZE_4x6, raise_e=False)
    
    def flow_home_load_photo_screen(self, printer_obj, from_tile=True):
        """
        From Home screen, load to My Photo screen
            - Select target printer
            - Verify ready printer at Home screen
            - Click on Print photos tile
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Files & Photos icon on navigation bar
        """
        if self.fd[FLOW_NAMES.HOME].verify_printer_model_name(printer_obj.get_printer_information()["bonjour name"], raise_e=False, timeout=15):
            self.flow_home_select_network_printer(printer_obj=printer_obj)
            self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
            self.flow_home_verify_ready_printer(printer_obj.get_printer_information()["bonjour name"])
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        # Verify scan screen to make sure that printer is connected successfully by visible page size
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].MY_PHOTOS_TXT)

    def flow_home_camera_scan_pages(self, from_tile=True, number_pages=1):
        """
        Create pages via Camera Scan from Home screen (from tiles or bottom navigation bar)
        Steps:
            - From Home screen, load Camera screen from tile or button on bottom naviation bar
            - Select specified mode
            - for each page
             - capture a photo 
             - click done button 
             - click next button on adjust screen
             - click add button on preview screen if another page is needed
        :param from_tile: True -> click on Tile. False -> click on Camera icon on navigation bar
        :param number_pages: number of pages are captured
        """
        # self.flow_home_verify_smart_app_on_userboarding()
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_CAMERA_SCAN_BTN)
        self.flow_camera_scan_capture_photo(number_pages=number_pages, timeout=number_pages * 60 + 90)

    def flow_home_load_shortcuts_screen(self, create_acc=False, printer_obj=None):
        """
        - Load to Home screen
        - Login in HPID in App Settings
        - Click on Smart Tasks tile on Home screen (Enable Smart Task file from Personalize if Smart Tasks tile not on Home screen)
        :param printer_ip
        :param is_searched: True or False (depends on need connect printer or not)
        :param create_acc: True or False

        """
        self.flow_home_sign_in_hpid_account(create_acc=create_acc)
        self.select_back()
        if printer_obj:
            self.flow_home_select_network_printer(printer_obj, is_searched=True)
        self.fd[FLOW_NAMES.HOME].verify_home_nav()
        self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.SMART_TASKS))
        self.driver.wait_for_context(self.smart_context, timeout=15)
        self.fd[FLOW_NAMES.SHORTCUTS].verify_shortcuts_screen(timeout=45)

    def flow_home_load_shortcuts_access_screen(self, printer_bonjour_name, printer_obj):
        """
        - Load to Home screen
        - Login in HPID in App Settings
        - Add a novelli printer from the printer list
        - Click on Printer icon to Printer Settings screen
        - Click on Shortcuts item from Printer Settings
        """
        self.flow_home_sign_in_hpid_account()
        self.select_back()
        if self.fd[FLOW_NAMES.HOME].verify_printer_model_name(printer_bonjour_name, raise_e=False, timeout=15):
            self.flow_home_select_network_printer(printer_obj=printer_obj)
            self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        self.fd[FLOW_NAMES.HOME].load_printer_info()
        self.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_printer_settings_items(self.fd[FLOW_NAMES.PRINTER_SETTINGS].SHORTCUTS, invisible=False)
        self.fd[FLOW_NAMES.PRINTER_SETTINGS].select_printer_setting_opt(self.fd[FLOW_NAMES.PRINTER_SETTINGS].SHORTCUTS)
        # From Printer Settings screen load to Shortcut access webview, it takes around 15-25s to load it
        self.fd[FLOW_NAMES.SHORTCUTS].verify_printer_access_off_message(timeout=25)

    def flow_home_enable_softfax_tile(self):
        """
        Enable SoftFax tile if it is not on Home screen
            - Go to Debug Setting -> enable Softfax
            - Kill app
            - Go to Personalize -> enable Send Fax
            - Go back Home screen and verify this tile display
        :return:
        """
        if self.fd[FLOW_NAMES.HOME].verify_tile(self.driver.return_str_id_value(TILE_NAMES.FAX), invisible=True, raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_personalize_tiles()
            self.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX), on=True)
            self.fd[FLOW_NAMES.PERSONALIZE].select_back()
            self.fd[FLOW_NAMES.HOME].verify_tile(self.driver.return_str_id_value(TILE_NAMES.FAX), invisible=False,
                                                 raise_e=True)
        else:
            logging.info("Send Fax is enable")

    def flow_home_toggle_hpx(self):
        """
        Toggle the HPX MFE in DEV Settings
        """
        self.fd[FLOW_NAMES.DEV_SETTINGS].open_select_settings_page()
        self.fd[FLOW_NAMES.DEV_SETTINGS].toggle_mfe_flow()
        self.hpx_on = True
        return True


    def flow_home_change_stack_server(self, stack):
        """
        Change Stack server in DEV Settings
            - Load Select Setting Page
            - Click on HPC Settings
            - Change Stack
        :param stack:
        """
        if self.driver.session_data["request"].config.getoption("--app-type") == "loggable":
            logging.debug("Loggable builds does not have the dev settings and only run on prod")
            return True

        stacks = {"production": self.fd[FLOW_NAMES.DEV_SETTINGS].PRODUCTION_STACK,
                  "stage": self.fd[FLOW_NAMES.DEV_SETTINGS].STAGE_STACK,
                  "pie": self.fd[FLOW_NAMES.DEV_SETTINGS].PIE_STACK
        }
        webapp_stacks = {
                "pie": self.fd[FLOW_NAMES.DEV_SETTINGS].WEBAPP_PIE_STACK,
                "stage": self.fd[FLOW_NAMES.DEV_SETTINGS].WEBAPP_STAGE_STACK,
                "production": self.fd[FLOW_NAMES.DEV_SETTINGS].WEBAPP_PRODUCTION_STACK
        }
        if self.driver.session_data["smart_state"].get("stack", None) != stack:
            self.fd[FLOW_NAMES.DEV_SETTINGS].open_select_settings_page()
            #Accroding to CR AIOA-15059, we need to add few seconds deplay after we launch developer settings.
            time.sleep(5)
            self.fd[FLOW_NAMES.DEV_SETTINGS].change_stack_server(stacks[stack], webapp_stacks[stack])
            self.driver.session_data["smart_state"]["stack"] = stack

    def flow_home_enable_log_unloggables(self):
        """
        Enable Log Unloggables on DEV settings
        """
        self.fd[FLOW_NAMES.DEV_SETTINGS].open_select_settings_page()
        # Accroding to CR AIOA-15059, we need to add few seconds deplay after we launch developer settings.
        time.sleep(5)
        self.fd[FLOW_NAMES.DEV_SETTINGS].toggle_log_unloggables()

    def flow_home_load_compose_fax_screen(self, create_acc=False, check_onboarding=False):
        """
        From Home, load Compose Fax screen via login/create acc at App Settings.
            - Go To App Settings -> log out acc if there is any acc
            - Set condition for Fax
            - Sign In or create a new acc -> Go back to Home screen
            - Click on Fax tile
            - Verify Compose Fax screen
        :param create_acc: create acc or sign in
        :param check_onboarding: False: go to App Settings for login/create account every time,
                                 True: if app is on user-onboarding, don't need to login/create account from app settings
        """
        if check_onboarding:
            self.flow_load_home_screen(skip_value_prop=True, accept_all_change_check=False)
            self.flow_home_verify_smart_app_on_userboarding(create_acc=create_acc)
        else:
            self.flow_home_sign_in_hpid_account(create_acc=create_acc, accept_all_change_check=False)
            self.select_back()
        self.flow_home_enable_softfax_tile()
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX), is_permission=True)
        # Wait for context of webview is visible in list before switching to webview
        if create_acc:
            self.driver.wait_for_context(a_const.WEBVIEW_URL.SOFTFAX_OFFER, timeout=30)
            if self.fd[FLOW_NAMES.SOFTFAX_OFFER].verify_get_started_screen(raise_e=False):
                self.fd[FLOW_NAMES.SOFTFAX_OFFER].skip_get_started_screen()
            if self.fd[FLOW_NAMES.SOFTFAX_WELCOME].verify_welcome_screen(raise_e=False):
                self.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen()
            self.fd[FLOW_NAMES.COMPOSE_FAX].click_fax_feature_update_compose_new_fax_btn(raise_e=False)
        else:
            #During HPID login process, take 30-45s to laod to Fax hisotry screen or compose fax screen. And has CR GDG-1768 for tracking this issue
            self.driver.wait_for_context(a_const.WEBVIEW_URL.SOFTFAX, timeout=40)
            self.fd[FLOW_NAMES.COMPOSE_FAX].click_fax_feature_update_dismiss_btn(raise_e=False)
            self.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(invisible=False, timeout=10)
            self.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        self.driver.wait_for_context(a_const.WEBVIEW_URL.SOFTFAX, timeout=40)
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_compose_fax_screen(timeout=10)

    def flow_home_log_out_hpid_from_app_settings(self):
        """
        Log out HPID on App Settings if an account is logged in
        """
        self.flow_load_home_screen(skip_value_prop=True)
        if self.stack != "production":
            self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_APP_SETTINGS_BTN)
        # if an HPID account is logged in, sign out
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(timeout=10, raise_e=False):
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()

    def flow_home_log_out_cloud_account (self, cloud_names):
        """
        Log out if the cloud account is logged in before
        From Home screen:
            - Click on file icon on bottom navigation bar
            - Long press on cloud name
            - Click on logout button
        :param cloud_names: element is constant variable of file and photos flow
                    - GOOGLE_DRIVE_TXT
                    - DROPBOX_TXT
                    - FACEBOOK_TXT
                    - INSTAGRAM_TXT
                    - GOOGLE_PHOTOS_TXT
        """
        if isinstance(cloud_names, str):
            cloud_names = [cloud_names]
        self.flow_load_home_screen()
        self.flow_home_verify_smart_app_on_userboarding()
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        for cloud in cloud_names:
            if not self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_not_login(cloud, raise_e=False):
                self.fd[FLOW_NAMES.FILES_PHOTOS].load_logout_popup(cloud)
                self.fd[FLOW_NAMES.FILES_PHOTOS].logout_cloud_item(cloud)
                self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_not_login(cloud)

    def flow_home_load_digital_copy_single_page(self, printer_obj):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
                  otherwise clicking on small "+" button on Home screen
        - click on Copy tile on Home screen
        - Allow access to camera
        - Click on Capture button with manual mode
        """
        self.reset_app()
        self.flow_load_home_screen()
        self.flow_home_select_network_printer(printer_obj, is_searched=True)
        self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        self.flow_home_verify_ready_printer(printer_obj.get_printer_information()["bonjour name"])
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.COPY))
        self.flow_grant_camera_scan_permissions()
        self.fd[FLOW_NAMES.DIGITAL_COPY].select_paper_size(self.fd[FLOW_NAMES.DIGITAL_COPY].PAPER_SIZE_LETTER)
        self.fd[FLOW_NAMES.SCAN].start_capture(change_check=self.fd[FLOW_NAMES.SCAN].COPY_CHANGE_CHECK)

    #   -----------------------         FROM PREVIEW       -----------------------------
    def flow_preview_share_via_gmail(self, to_email, subject, content="", from_email=""):
        """
        From Sharing Using popup, share via gmail:
            - Click on Gmail button on Sharing Using popup
            - At compose Gmail, enter all information
            - Verify that email is sent successfully
        :param from_email:
        :param to_email:
        :param subject:
        :param content:
        """
        #Change subject to separated value for multiple execution parallel
        self.fd[FLOW_NAMES.SYSTEM_FLOW].select_app(self.driver.return_str_id_value("share_gmail_str", project="smart", flow="preview_android"))
        self.flow_gmail_send_email(to_email, subject, content, from_email=from_email)

    def flow_preview_make_printing_job(self, printer_obj, is_from_print_photo_tile=False):
        """
        At Preview screen:
            - Click on Print button
            - Check printing job with HPPS
        :param printer_obj:
        :param jobs:
        """
        if not is_from_print_photo_tile:
            self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_screen()
            self.fd[FLOW_NAMES.COMMON_PREVIEW].select_bottom_nav_btn(self.fd[FLOW_NAMES.COMMON_PREVIEW].PRINT_PREVIEW_BTN)
        self.fd[FLOW_NAMES.PRINT_PREVIEW].verify_print_preview_screen()
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_print_btn()
        if is_from_print_photo_tile:
            self.driver.wdvr.open_notifications()
            # HP Smart printing notification need to take some time to shows on notifications list
            bonjour_name = printer_obj.get_printer_information()['bonjour name']
            self.fd[FLOW_NAMES.JOB_NOTIFICATION].select_print_notification_by_printer_name(bonjour_name)
        else:
            self.fd[FLOW_NAMES.PRINT_PREVIEW].verify_print_preview_screen()
            self.fd[FLOW_NAMES.PRINT_PREVIEW].select_print_job_list_btn()
        self.fd[FLOW_NAMES.JOB_NOTIFICATION].verify_print_jobs_screen()
        self.fd[FLOW_NAMES.JOB_NOTIFICATION].verify_print_job_on_the_list()

    #   -----------------------         FROM GMAIL Compose       -----------------------------
    def flow_gmail_send_email(self, to_email, subject, content="", from_email=None):
        """
        At Compose screen, send an email:
            - Enter valid information into From, To, Subject, and Content
            - Click on Send button
            - Verify that email is sent successfully
        :param from_email:
        :param to_email:
        :param subject:
        :param content:
        :return:
        """
        subject = "{}_{}".format(subject, self.driver.driver_info["desired"]["udid"])
        # Delete the email from previous execution
        if (msg_id := self.fd[FLOW_NAMES.GMAIL_API].search_for_messages(q_from=from_email,
                                                                q_to=to_email,
                                                                q_unread=False,
                                                                q_subject=subject,
                                                                q_content=content,
                                                                timeout=30, raise_e=False)):
            self.fd[FLOW_NAMES.GMAIL_API].delete_email(msg_id)
        # Start to test Gmail
        try:
            f_email = self.fd[FLOW_NAMES.GMAIL].compose_email(to_email=to_email,
                                                          subject_text=subject,
                                                          body_text=content)

            msg_id = self.fd[FLOW_NAMES.GMAIL_API].search_for_messages(q_from=f_email,
                                                                       q_to=to_email,
                                                                       q_unread=True,
                                                                       q_subject=subject,
                                                                       q_content=content,
                                                                       timeout=120,
                                                                       raise_e=True)
            self.fd[FLOW_NAMES.GMAIL_API].delete_email(msg_id)
        except TimeoutException as ex:
            logging.warning(ex.msg)

    #   -----------------------         FROM HPPS APP       -----------------------------
    @SPL_decorator.print_job_decorator()
    def flow_hpps_make_print_job_via_trapdoor_ui(self, printer_obj, jobs=1, skip_agreement=True):
        """
        - Make print job via trap door ui
        - Verify print job on printer and HPPS app
        :param printer_obj: instance GenericPrinter.
        :param file_name:
        :param is_document:
        :return:
        """
        if skip_agreement and self.fd[FLOW_NAMES.HPPS].agree_and_accept_terms_and_condition_if_present():
            self.fd[FLOW_NAMES.HPPS].check_run_time_permission()
        if self.is_printer_ready(printer_obj):
            self.fd[FLOW_NAMES.HPPS_TRAPDOOR].verify_printer_preview_screen()
            self.fd[FLOW_NAMES.HPPS_TRAPDOOR].select_print()
            self.verify_print_job_success(printer_obj, jobs=jobs)
        else:
            raise PrinterNotReady("Printer is not ready for printing job")
        
    def verify_print_job_success(self, printer_obj, jobs=1):
        """
        Verifies that the hpps print job(s) for the specified printer was successful
        :param printer_obj: SPL Printer
        :param jobs: The number of print jobs to verify
        """
        self.driver.wdvr.open_notifications()
        bonjour_name = printer_obj.get_printer_information()['bonjour name']
        bonjour_name = bonjour_name[bonjour_name.find("HP ") + 3:bonjour_name.find("series") - 1]  # remove HP and series out of string
        self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].select_print_notification_by_printer_name(bonjour_name)
        self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].verify_print_jobs_screen()
        for _ in range(jobs):
            self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].get_printing_results_trap_door(timeout=150)

    #   -----------------------         FROM Smart Task       -------------------------------
    def load_create_you_own_shortcuts_screen(self):
        """
        - Click on Add Shortcut button on Shortcuts screen
        - Verify Add Shortcut screen
        - Click on Create your Own Shortcut button
        - Verify Add your own shortcut screen
        """
        self.fd[FLOW_NAMES.SHORTCUTS].click_add_shortcut()
        self.fd[FLOW_NAMES.SHORTCUTS].verify_add_shortcuts_screen()
        self.fd[FLOW_NAMES.SHORTCUTS].click_create_your_own_shortcut_btn()
        self.fd[FLOW_NAMES.SHORTCUTS].verify_add_your_own_shortcut_screen()

    def add_create_you_own_shortcuts_for_email(self, email_address):
        """
        - Click on Email option from Add Shorts screen
        - Verify Add Email screen
        -Type email address
        """
        self.fd[FLOW_NAMES.SHORTCUTS].click_email_btn()
        self.fd[FLOW_NAMES.SHORTCUTS].verify_add_email_screen()
        self.fd[FLOW_NAMES.SHORTCUTS].enter_email_receiver(email_address)

    def add_create_you_own_shortcuts_for_print(self, is_new=True, copies_num="", color_btn="", two_sided_option=""):
        """
        - Click on Print option from Add Shorts screen
        - Verify Add Print screen
        - Select Color & Copies & Two-sided option
        """
        self.fd[FLOW_NAMES.SHORTCUTS].click_print_btn()
        if is_new:
            self.fd[FLOW_NAMES.SHORTCUTS].verify_add_print_screen()
        else:
            self.fd[FLOW_NAMES.SHORTCUTS].verify_edit_print_screen()
        if copies_num:
            self.fd[FLOW_NAMES.SHORTCUTS].select_copies(copies_num)
        if color_btn:
            self.fd[FLOW_NAMES.SHORTCUTS].select_color(color_btn)
        if two_sided_option:
            self.fd[FLOW_NAMES.SHORTCUTS].select_two_sided(two_sided_option)

    def add_create_you_own_shortcuts_for_saving(self, is_new=True, is_google_drive=True):
        """
        - Click on Email option from Add Shorts screen
        - Verify Add Email screen
        -Type email address
        """
        self.fd[FLOW_NAMES.SHORTCUTS].click_save_btn()
        if is_new:
            self.fd[FLOW_NAMES.SHORTCUTS].verify_add_save_screen()
        else:
            self.fd[FLOW_NAMES.SHORTCUTS].verify_edit_save_screen()
        if is_google_drive:
            self.fd[FLOW_NAMES.SHORTCUTS].click_google_drive_checkbox()
        else:
            self.fd[FLOW_NAMES.SHORTCUTS].click_dropbox_checkbox()

    def flow_save_shortcuts(self, shortcuts_name, invisible=True):
        """
        - Click on Add Shortcut button on Shortcuts screen
        - Click on Continue button
        - Verify Settings screen
        - Enter Shortcuts name
        - Click on Save Shortcut button
        - Verify Shortcut saved screen
        """
        self.fd[FLOW_NAMES.SHORTCUTS].click_add_to_shortcut_btn()
        self.fd[FLOW_NAMES.SHORTCUTS].click_continue_btn()
        self.fd[FLOW_NAMES.SHORTCUTS].verify_settings_screen(invisible)
        self.fd[FLOW_NAMES.SHORTCUTS].enter_shortcut_name(shortcuts_name)
        self.fd[FLOW_NAMES.SHORTCUTS].click_save_shortcut_btn()
        self.fd[FLOW_NAMES.SHORTCUTS].verify_shortcut_saved_screen(timeout=15)

    #   -----------------------         FROM Digital Copy       -----------------------------
    # Currently this function only verify Copy send success on App side, Skip for verifying printing job on printer success or not as defect INOS-3861
    def flow_digital_copy_make_copy_job(self, printer_obj, is_color_copy):
        """
        - Make copy job via trap door ui
        - Verify print job on printer and HPPS app
        :param printer_obj: instance GenericPrinter.
        :param is_color_copy: True: Color copy, False: Black copy
        :param printer_obj:
        :param jobs:
        :return:
        """
        if self.is_printer_ready(printer_obj):
            if is_color_copy:
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_color_copy_btn()
            else:
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_black_copy_btn()
            if self.fd[FLOW_NAMES.DIGITAL_COPY].verify_paper_size_mismatch_popup(raise_e=False):
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_ok_btn()
            if self.fd[FLOW_NAMES.DIGITAL_COPY].verify_paper_size_too_large_popup(raise_e=False):
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_cancel_btn()
                self.fd[FLOW_NAMES.DIGITAL_COPY].verify_copy_preview_screen()
            else:
                self.fd[FLOW_NAMES.DIGITAL_COPY].verify_copy_job_finished_screen()
            return True
        raise PrinterNotReady("Current Printer status is {} and not ready for printing job".format(printer_obj.get_printer_status()))

    #   -----------------------         FROM APP SETTINGS       -----------------------------
    def flow_app_settings_sign_in_hpid(self):
        """
        From App Settings: Click on Sign out if an account is signed in
            - Click on Sign In button
            - Log in if HPID log in screen or
              Current account is not usrname, log out and login again
            - Verify App Settings with the same username
        """
        #If HPID is signed in with the expected username
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(self.driver.session_data["hpid_user"], raise_e=False):
            return True
        #Since HPID isn't signed in with the expected username
        #Check if HPID is signed in or not
        elif self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(raise_e=False):
            #Sign out of the existing account because it's signed in
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()
            self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings(timeout=15)

        # Avoid to automatically logged into HPID account. Clear cache Google Chrome
        self.driver.clear_app_cache(a_const.PACKAGE.GOOGLE_CHROME)

        # For Android devices, somehow direct into mobile device home screen instead of app settings screen after clear cache for Google Chrome.
        # We submitted CR AIOA-8868 for this issue. This is temporay fix until the CR get fixed
        if not self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_in_btn(invisible=False, raise_e=False):
            self.reset_app()
            self.flow_load_home_screen(skip_value_prop=True)
            if self.stack != "production":
                self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
            else:
                self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_APP_SETTINGS_BTN)
        self.fd[FLOW_NAMES.APP_SETTINGS].click_sign_in_btn()
        time.sleep(7)
        self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        #Should be a the sign in page now and continue signing in with the account i want
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
        self.fd[FLOW_NAMES.HPID].login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
        if self.fd[FLOW_NAMES.SMB].select_my_printers(raise_e=False):
            self.fd[FLOW_NAMES.SMB].select_continue()
        self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(self.driver.session_data["hpid_user"], timeout=30, raise_e=True)
        return True

    def flow_app_settings_create_hpid(self):
        """
        From App Settings:
            - Sign out account if there is a logged in account
            - Clear cache of Google Chrome to avoid to automatically log in into a HPID account
            - Click on Sign In
            - At HPID's sign up screen, create a new hpid
        :return: credential of new hpid
        """
        # If an HPID account is logged in, click on sign out button
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(timeout=10, raise_e=False):
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()
        # Make sure there is no saved HPID account in cache of Google Chrome which causes automatically logged in
        self.driver.clear_app_cache(a_const.PACKAGE.GOOGLE_CHROME)

        # For Android 7/8/9, somehow direct into mobile device home screen instead of app settings screen after clear cache for Google Chrome
        if not self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_in_btn(invisible=False, raise_e=False):
            self.flow_load_home_screen(skip_value_prop=True)
            if self.stack != "production":
                self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
            else:
                self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_APP_SETTINGS_BTN)
            if self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(timeout=5, raise_e=False):
                self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()

        self.fd[FLOW_NAMES.APP_SETTINGS].click_create_account_btn()
        hpid_username = self.driver.session_data["hpid_user"].split("@")
        hpid_username = "{}+{:%Y_%m_%d_%H_%M_%S}@{}".format(hpid_username[0], datetime.datetime.now(), hpid_username[1])
        time.sleep(4)
        # Handle for welcome screen of Google Chrome
        self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        self.driver.wait_for_context(a_const.WEBVIEW_CONTEXT.CHROME)
        self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_up()
        email, password = self.fd[FLOW_NAMES.HPID].create_account(email=hpid_username)
        #Todo: Wait for designer's reply for updating timeout.
        self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(email, raise_e=False, timeout=40)
        return email, password

    #   -----------------------         FROM Printer       -----------------------------
    def is_printer_ready(self, printer_obj):
        """
        Verify printer is ready for making any job:
            - Check printer assert -> reset printer
            - Check printer ready
        :param printer_obj: printer object (SPL)
        :return: True -> ready. False -> not ready
         """
        printer_obj.check_init_coredump()
        return printer_obj.is_printer_status_ready()

    def get_printer_oobe_name(self, printer_obj, is_ble=True):
        """
        Get Printer's OOBE name for selecting printer in MOOBE process

        Note: If it is a Lebi printer, use the WFD printer name, else use the WFD MAC address.
        :param printer_obj: SPL instance
        :param is_ble: suport ble or not
        """
        if 'lebi' not in printer_obj.p_obj.projectName.lower():
            printer_obj.toggle_wifi_direct(on=True)
            mac_addrr = printer_obj.get_wifi_direct_information()["mac address"]
            printer_obj.toggle_wifi_direct(on=False)    #set printer back to beaconnning mode
            return ":".join([mac_addrr[i:i+2] for i in range(0, len(mac_addrr), 2)])
        else:
            return printer_obj.get_wifi_direct_mac_address().upper()

    def get_moobe_connect_wifi_type(self, printer_obj):
        """
        From printer object, confirm what connect Wi-Fi type of moobe is
        Note": This list of types is from list of printer in Chamber, update it when there is added new type printer.
        :param printer_obj: SPL instance
        :return "awc"/"awc_ble"/"secure_ble"
        """
        types = {"awc": ["novelli_plus", "naplesplus", "corfuplus", "naples", "naples_minus", "naples_super", "palermo_fast"],
                 "awc_ble": ["palermo_minus", "palermo_super", "verona_base", "malbec"],
                 "secure_ble": ["vasari_base", "vasari_plus", "taccola_plus", "lebi_wl_sox"]}

        project_name = printer_obj.p_obj.projectName
        for key in types:
            if project_name[:project_name.rfind("_")] in types[key]:
                return key
        raise NotFoundMOOBEConnectWifiType("{} is not found in list of type".format(project_name))
    
    #   -----------------------      FROM Files & Photos      -----------------------------
    def flow_files_photos_login_facebook(self, label, username, password):
        """
        Pre-condition: At Files & Photos screen
        Logs into a Facebook account and ends at the Files & Photos screen
        :param label: The name of the account, used for selecting the account on the existing fb accounts list
        :param username: Username of the Facebook account, an email address
        :param password: Password of the Facebook account
        """
        if self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_not_login(self.fd[FLOW_NAMES.FILES_PHOTOS].FACEBOOK_TXT, raise_e=False):
            self.fd[FLOW_NAMES.FILES_PHOTOS].select_cloud_item(self.fd[FLOW_NAMES.FILES_PHOTOS].FACEBOOK_TXT)
            self.fd[FLOW_NAMES.ONLINE_PHOTOS].select_fb_account(label, raise_e=False)
            if not self.fd[FLOW_NAMES.FILES_PHOTOS].verify_files_photos_screen(raise_e=False):
                if self.fd[FLOW_NAMES.ONLINE_PHOTOS].verify_fb_login_confirmation_screen(label, raise_e=False):
                    self.fd[FLOW_NAMES.ONLINE_PHOTOS].select_fb_confirmation_continue(label)
                elif self.fd[FLOW_NAMES.ONLINE_PHOTOS].verify_fb_login_screen(raise_e=False):
                    self.fd[FLOW_NAMES.ONLINE_PHOTOS].login_to_fb(username, password)
                elif self.fd[FLOW_NAMES.ONLINE_PHOTOS].verify_fb_password_prompt_screen(raise_e=False):
                    self.fd[FLOW_NAMES.ONLINE_PHOTOS].login_to_fb_at_password_screen(password)
                if self.fd[FLOW_NAMES.ONLINE_PHOTOS].verify_fb_album_screen(raise_e=False):
                    self.driver.press_key_back()
            self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_added_account(self.fd[FLOW_NAMES.FILES_PHOTOS].FACEBOOK_TXT, label)
            logging.info('Signed into Facebook account {}({})'.format(label, username))
        else:
            logging.info("Facebook already signed in")

    #   -----------------------       FROM CAMERA SCAN      -----------------------------
    def flow_camera_scan_capture_photo(self, number_pages=1, timeout=90, chk_bottom_navbar=True):
        """
        Captures images on the camera scan screen.
        Recommended to use this method over camera_scan.capture_photo with batch mode when multiple pages are needed.
        Steps:
         1. Captures a photo in document mode
         2. Selects next on adjust screen
         3. Selects add if number_pages is not met and repeats steps 1 and 2
        :param number_pages: Number of images to capture
        """
        end_time = time.time() + timeout
        preview_img_count = 0
        self.flow_scan_capture(self.fd[FLOW_NAMES.SCAN].SOURCE_CAMERA_OPT)
        self.fd[FLOW_NAMES.SCAN].select_adjust_next_btn()
        self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_screen(chk_bottom_navbar=chk_bottom_navbar)
        preview_img_count = self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_page_info()[1]
        while preview_img_count < number_pages:
            if time.time() > end_time:
                raise TimeoutException("Could not capture {} images within in {} seconds".format(number_pages, timeout))
            self.fd[FLOW_NAMES.COMMON_PREVIEW].select_top_toolbar_btn(self.fd[FLOW_NAMES.COMMON_PREVIEW].ADD_BTN)
            self.fd[FLOW_NAMES.SCAN].start_capture(change_check=self.fd[FLOW_NAMES.SCAN].CAPTURE_CHANGE_CHECKS["document"], timeout=30)
            self.fd[FLOW_NAMES.SCAN].select_adjust_next_btn()
            self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_screen(chk_bottom_navbar=chk_bottom_navbar)
            new_img_count = self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_page_info()[1]
            assert preview_img_count + 1 == new_img_count, "Image count went from {} -> {} instead of incrementing by 1".format(preview_img_count, new_img_count)
            preview_img_count = new_img_count
        assert self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_page_info()[1] == number_pages, f"Page count should be {number_pages}"
        return True

    def flow_grant_camera_scan_permissions(self):
        """
        Handles No Camera Access screen and permission popup
        """
        if self.driver.session_data["smart_state"].get("camera_scan_consent", False):
            return True
        if self.fd[FLOW_NAMES.SCAN].grant_camera_permissions():
            self.fd[FLOW_NAMES.HOME].check_run_time_permission()
            self.driver.session_data["smart_state"]["camera_scan_consent"] = True
            return True
        return False

    # ------------------------------- From Unified Scan ---------------------------------
    def flow_scan_capture(self, source, mode="document", number_pages=1, is_permission=True):
        """
        Captures image(s) and proceeds to subsequent screen(depends on capture mode).
        :param source: The image source to use. Use class constants SOURCE_CAMERA_OPT, SOURCE_PRINTER_SCAN_OPT.
        :param mode: The scan mode to use. Possible values: "photo", "document", "id_card", "book", "multi_item", "batch"
        :param number_pages: The number of images to capture.
        """
        if mode not in self.fd[FLOW_NAMES.SCAN].CAPTURE_CHANGE_CHECKS:
            raise ValueError('{} is not a valid mode, mode must be one of ["photo","document","id_card","book","multi_item","batch"]'.format(mode))
        if source != self.fd[FLOW_NAMES.SCAN].verify_selected_source():
            self.fd[FLOW_NAMES.SCAN].select_source(source)
        if source == self.fd[FLOW_NAMES.SCAN].SOURCE_CAMERA_OPT and is_permission:
            self.flow_grant_camera_scan_permissions()
        self.fd[FLOW_NAMES.SCAN].dismiss_coachmark()
        if not self.fd[FLOW_NAMES.SCAN].verify_selected_capture_mode(mode=mode, raise_e=False):
            self.fd[FLOW_NAMES.SCAN].select_capture_mode(mode)
        if number_pages > 1 and mode not in ["batch", "book"]:
            logging.warning("number_pages > 1 is not valid for mode {}".format(mode))
            number_pages = 1
        if mode == "id_card":
            number_pages = 2
        for i in range(number_pages):
            if mode == "id_card" and source == self.fd[FLOW_NAMES.SCAN].SOURCE_CAMERA_OPT:
                change_check = self.fd[FLOW_NAMES.SCAN].CAPTURE_CHANGE_CHECKS[mode + "_" + source]
            else:
                change_check = self.fd[FLOW_NAMES.SCAN].CAPTURE_CHANGE_CHECKS[mode]
            change_check = change_check[i] if isinstance(change_check, list) else change_check
            self.fd[FLOW_NAMES.SCAN].start_capture(change_check=change_check)
            time.sleep(3)
            if change_check is not None:
                continue
            if source == self.fd[FLOW_NAMES.SCAN].SOURCE_CAMERA_OPT:
                self.fd[FLOW_NAMES.SCAN].verify_capture_progress_icon(invisible=True)
            elif source == self.fd[FLOW_NAMES.SCAN].SOURCE_PRINTER_SCAN_OPT:
                self.fd[FLOW_NAMES.SCAN].verify_capture_button(is_selected=False)
            time.sleep(1)
        if mode in ["batch", "book"]:
            self.fd[FLOW_NAMES.SCAN].select_done()

    #   -----------------------         MOBILE DEVICE       -----------------------------
    def transfer_test_data_to_device(self, file_names, folder=None):
        """
        Transfer test data (.pdf or .jpg files) to mobile device for testing
        :param file_names: list or str (1 file)
        :param dir: The directory to push your file(s) to, if None pushes to TEST_DATA.MOBILE_DOWNLOAD
        """
        folder_path = {"pdf": a_const.TEST_DATA.DOCUMENTS_PDF_FOLDER,
                         "jpg": a_const.TEST_DATA.IMAGES_JPG_FOLDER}
        if isinstance(file_names, str):
            file_names = [file_names]
        if folder is None:
            folder = a_const.TEST_DATA.MOBILE_DOWNLOAD
        for fn in file_names:
            file_ext = fn[fn.rfind(".") + 1: ]
            self.driver.wdvr.push_file("{}/{}".format(folder, fn), source_path=ma_misc.get_abs_path(os.path.join(folder_path[file_ext], fn)))
            logging.debug("Pushed file to {}/{}".format(folder, fn))

    def verify_existed_file(self, file_path):
        """
        Verify a file is existed/non-existed via file_path
        :param file_path
        :return True -> exist. False -> non-exist
        """
        try:
            self.driver.wdvr.execute_script("mobile:shell", {"command": "ls {}".format(file_path)})
            return True
        except WebDriverException:
            return False

    #   -----------------------         SOFTFAX INFORMATION       -----------------------------
    def get_softfax_recipient_info(self):
        """
        To avoid multiple sending fax jobs on one phone number at the same time, each platform is assigned a fake fax number
        if it is not assigned from pytest argument
        """
        recipients = {"12": "recipient_02",
                      "13": "recipient_03",
                      "14": "recipient_06",
                      "11": "recipient_09"}
        current_os = self.driver.platform_version
        recipient_info = saf_misc.load_json(ma_misc.get_abs_path(a_const.TEST_DATA.SOFTFAX_ACCOUNT))["softfax"][recipients[current_os]]
        request = self.driver.session_data["request"]
        recipient_info["phone"] = request.config.getoption("--recipient-phone") if request.config.getoption("--recipient-phone") else recipient_info["phone"]
        recipient_info["code"] = request.config.getoption("--recipient-code") if request.config.getoption("--recipient-code") else recipient_info["code"]
        return recipient_info

    def make_send_fax_job(self, recipient_phone, sender_name, sender_phone):
        """
        Make Send Fax job (doesn't matter that it is successful or not)
        return: full phone number of recipient
        """
        self.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(recipient_phone)
        phone, name, code = self.fd[FLOW_NAMES.COMPOSE_FAX].get_recipient_information()
        self.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn(self.fd[FLOW_NAMES.COMPOSE_FAX].CAMERA_BTN)
        self.flow_camera_scan_capture_photo(chk_bottom_navbar=False)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_title(self.fd[FLOW_NAMES.COMMON_PREVIEW].PREVIEW_TITLE)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_fax_next()
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_compose_fax_screen()
        # Confirmed with developer that 60s here is reasonable as decided by file size
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_uploaded_file(timeout=60)
        self.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(sender_name, sender_phone)
        self.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        self.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_detail_screen()
        return "{} {}".format(code, phone)

    #   -----------------------         MOOBE       -----------------------------
    def flow_home_moobe_connect_printer_to_wifi(self, printer_obj, ssid, password, is_ble=True, is_secure=False, create_acc=False):
        """
        This flow is used for AWC, BLE, and secure BLE printer (without front panel)
        Start from Home screen to connect printer to Wi-Fi via MOOBE steps
        Steps:
            - Load Home screen
            - Load Printer screen from Home
            - CLick on Add Printer 
            - Select OOBE printer on Add Printer screen
            - At Connect Wi-fi screen, enter valid password of ssid and click on Continue button
                + To Android 7, 8, and 9, dismiss turn on bluetooth popup by deny/allow (via enable bluetooth)
            - Go through thermometer to connect printer to wifi
        Expected:
            - Connected screen displays
        
        :param printer_obj: SPL instance
        :param ssid: ssid of network
        :param password: password of ssid
        :param is_ble: Moobe BLE or not
        :param is_secure: True -> check Press button popup for secure BLE printer. False -> ignore this popup
        :param create_acc: signin/create new hpid account
        """
        # Select oobe printer from home screen
        self.flow_home_select_oobe_printer(printer_obj, ssid=ssid, is_ble=is_ble, create_acc=create_acc)

         # Start AWC process
        self.fd[FLOW_NAMES.MOOBE_AWC].connect_printer_to_wifi(ssid, password, is_secure=is_secure, printer_obj=printer_obj)

    def flow_home_select_oobe_printer(self, printer_obj, ssid, is_ble=True, create_acc=False):
        """
        Start from Home scfreen:
            - Go to Printer screen
            - Click on Add printer button on bottom
            - Select target oobe printer on Add Printer screen
        Expected:
            Connect to Wi-Fi screen
        
        :param printer_obj: SPL instance
        :param is_ble: Moobe BLE or not
        :param create_acc: signin/create new hpid account
        """
        self.flow_load_home_screen(create_acc=create_acc)
        self.fd[FLOW_NAMES.HOME].load_printer_selection()
        self.fd[FLOW_NAMES.PRINTERS].select_printer_option_get_started()
        self.fd[FLOW_NAMES.PRINTERS].verify_printer_connection_type_screen()
        self.fd[FLOW_NAMES.PRINTERS].select_wifi_connection()
        self.driver.click("setup_printer_continue_btn")
        try:
            self.fd[FLOW_NAMES.HOME].check_run_time_permission()
            self.fd[FLOW_NAMES.PRINTERS].verify_location_usage_popup()
            self.fd[FLOW_NAMES.PRINTERS].select_location_usage_ok_button()
        except TimeoutException:
            logging.info("Location Usage popup is not displayed")
        time.sleep(5)
        if not is_ble and int(self.driver.platform_version) > 9:
            self.fd[FLOW_NAMES.PRINTERS].select_oobe_awc_printer(self.get_printer_oobe_name(printer_obj, is_ble=is_ble), ssid)
        else:
            self.fd[FLOW_NAMES.PRINTERS].select_oobe_printer(self.get_printer_oobe_name(printer_obj, is_ble=is_ble))

    #   -----------------------      Smart Dashboard       -----------------------------
    def flow_home_smart_dashboard(self):
        """
        1. Load Smart app with hp+ account / ucde account
        2. Click on Account  button on Home screen
        3. Verify Account Summary screen
        :param account_type: ucde / hp+
        """
        self.flow_load_home_screen(verify_signin=True)
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_CREATE_ACCOUNT_BTN)
        self.fd[FLOW_NAMES.SMB].select_manage_hp_account()
        self.fd[FLOW_NAMES.HP_CONNECT].accept_privacy_popup()
        self.fd[FLOW_NAMES.HP_CONNECT].verify_account_summary()

    def flow_home_smart_dashboard_help_center(self):
        """
        1. Load Smart app with hp+ account
        2. Click on Account  button on Home screen
        3. Verify Account Summary screen
        4. Click on Toggle menu button
        5. Click on Help Center button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT].verify_smart_dashboard_menu_screen()
        self.fd[FLOW_NAMES.HP_CONNECT].click_help_center_btn()
        self.fd[FLOW_NAMES.HELP_CENTER].verify_help_center_menu()

    def load_smart_dashboard_help_center_about_hp_smart(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on About HP Smart item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].ABOUT_HP_SMART)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_about_hp_smart()

    def load_smart_dashboard_help_center_hp_plus(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on HP+ item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].HP_PLUS)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_hp_plus()

    def load_smart_dashboard_help_center_print_scan_and_share(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Print, Scan, and Share item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].PRINT_SCAN_AND_SHARE)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_print_scan_and_share()

    def load_smart_dashboard_help_center_printer_and_connection_info(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Printer and Connection information item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].PRINTER_AND_CONNECTION)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_printer_and_connection_information()

    def load_smart_dashboard_help_center_additional_help_and_support(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Additional help and support item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].ADDITIONAL_HELP_AND_SUPPORT)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_additional_help_and_support()

    def load_smart_dashboard_help_center_hp_smart_advance(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on HP Smart Advance item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].HP_SMART_ADVANCE)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_hp_smart_advance()

    def load_edit_screen_through_camera_scan(self):
        """
        1. Load app to camera scan screen
        2. Capture a picture, and lead to Preview screen
        3. Click on Page options button / Edit button
        """
        self.flow_load_home_screen(verify_signin=True)
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_CAMERA_SCAN_BTN)
        self.flow_scan_capture(self.fd[FLOW_NAMES.SCAN].SOURCE_CAMERA_OPT, mode="document", number_pages=1)
        self.fd[FLOW_NAMES.SCAN].verify_adjust_screen()
        self.fd[FLOW_NAMES.SCAN].select_adjust_next_btn()
        self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_preview_screen()
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_page_options_btn(self.fd[FLOW_NAMES.COMMON_PREVIEW].EDIT_BTN)
        self.fd[FLOW_NAMES.HOME].check_run_time_permission()
        self.fd[FLOW_NAMES.EDIT].verify_edit_page_title()

    def load_edit_screen_through_my_photo(self, printer_obj=None):
        """
        1. Load app to My Photo screen
        2. Select a photo from any album
        3. Click on Page options button / Edit button
        """
        self.flow_load_home_screen(verify_signin=True)
        if printer_obj:
            self.flow_home_select_network_printer(printer_obj, is_searched=True)
            self.fd[FLOW_NAMES.HOME].verify_home_nav()
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        if self.fd[FLOW_NAMES.FILES_PHOTOS].verify_limited_access_popup(raise_e=False):
            self.fd[FLOW_NAMES.FILES_PHOTOS].select_continue_btn()
        self.fd[FLOW_NAMES.FILES_PHOTOS].verify_files_photos_screen()
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].MY_PHOTOS_TXT)
        self.fd[FLOW_NAMES.LOCAL_PHOTOS].select_recent_photo_by_index()
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_print_size(self.fd[FLOW_NAMES.COMMON_PREVIEW].PRINT_SIZE_4x6, raise_e=False)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_page_options_btn(self.fd[FLOW_NAMES.COMMON_PREVIEW].EDIT_BTN)
        self.fd[FLOW_NAMES.HOME].check_run_time_permission()
        self.fd[FLOW_NAMES.EDIT].verify_edit_page_title()
    
    def flow_home_smart_dashboard_account_menu(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / Account button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT].click_account_btn()
        self.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT].verify_account_menu_screen()
    
    def flow_home_smart_dashboard_features_menu(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / Features button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_FEATURES].click_solutions_btn()
    
    def flow_home_smart_dashboard_hp_instant_ink(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / HP Instant Ink button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK].click_hp_instant_ink_btn()
        self.fd[FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK].verify_hp_instant_ink_menu_screen()

    def load_two_sided_preview_screen_for_novelli(self, printer_obj, printer_bonjour_name, is_back_screen=False, photo_album="jpg"):
        """
        1. Connect to a novelli printer to smart app
        2. Load app to two sided preview screen through My Photos
        """
        self.flow_load_home_screen(verify_signin=True)
        if self.fd[FLOW_NAMES.HOME].verify_printer_model_name(printer_bonjour_name, raise_e=False, timeout=15):
            self.flow_home_select_network_printer(printer_obj=printer_obj)
            self.fd[FLOW_NAMES.HOME].dismiss_print_anywhere_popup()
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].MY_PHOTOS_TXT)
        self.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index(photo_album)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_title(self.fd[FLOW_NAMES.COMMON_PREVIEW].PRINT_SIZE_TITLE)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_print_size(self.fd[FLOW_NAMES.COMMON_PREVIEW].PRINT_SIZE_4x6_TWO_SIDED)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].verify_two_sided_preview_screen()
        if is_back_screen:
            self.fd[FLOW_NAMES.COMMON_PREVIEW].select_two_sided_page_btn()
    
    def load_edit_screen_for_novelli(self, printer_obj, printer_bonjour_name, edit_option, is_back_screen=False):
        """
        1. Connect to a novelli printer to smart app
        2. Load app to two sided preview screen through My Photos
        3. Select Edit
        4. Select specified edit option
        """
        self.load_two_sided_preview_screen_for_novelli(printer_obj, printer_bonjour_name, is_back_screen=is_back_screen)
        self.fd[FLOW_NAMES.COMMON_PREVIEW].select_page_options_btn(self.fd[FLOW_NAMES.COMMON_PREVIEW].EDIT_BTN)
        self.fd[FLOW_NAMES.EDIT].verify_edit_page_title()
        self.fd[FLOW_NAMES.EDIT].select_edit_main_option(edit_option)
        self.fd[FLOW_NAMES.EDIT].verify_screen_title(edit_option)
    
    def terminate_and_relaunch_smart(self):
        """
        Terminate app and relaunch app
        """
        self.__terminate()
        self.launch_smart()

    def read_supplies_status_json_files(self, ioref, type):
        alert_key = None
        if type == "error":
            alert_data = saf_misc.load_json(ma_misc.get_abs_path(SUPPLY_VALIDATION.ERROR_MESSAGE))
        if type == "warning":
            alert_data = saf_misc.load_json(ma_misc.get_abs_path(SUPPLY_VALIDATION.WARNING_MESSAGE))
        if type == "info":
            alert_data = saf_misc.load_json(ma_misc.get_abs_path(SUPPLY_VALIDATION.INFORM_MESSAGE))
        # Find the key that ends with the alert code
        for key in alert_data[type].keys():
            if key.endswith(str(ioref)):
                alert_key = key
                break
        if not alert_key:
            raise KeyError(f"No alert found for code: {ioref}")
        alert_info = alert_data[type][alert_key]
        self.supply_alert_title = alert_info[f"{alert_key}_header"]
        self.supply_alert_icon = alert_info[f"{type}_icon"]
        self.alert_detailed_info = alert_info["body"]
        return self.supply_alert_title, self.supply_alert_icon, self.alert_detailed_info

    #   -----------------------       Private Methods     -----------------------------
    def __terminate(self):
        """Terminates apps that could affect smart app launching or functionality"""
        terminated_apps = [self.pkg_name, a_const.PACKAGE.GOOGLE_CHROME, a_const.PACKAGE.GOOGLE_PHOTOS, a_const.PACKAGE.HPPS, a_const.PACKAGE.SETTINGS, *a_const.PACKAGE.DOCUMENTS]
        for terminated_app in terminated_apps:
            self.driver.terminate_app(terminated_app)