import re
import time
import json
import pytest
import logging
import xml.etree.ElementTree as ET
import os
import requests
from urllib.parse import urljoin

from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.windows.const import SUPPLY_VALIDATION

from MobileApps.libs.flows.web.hpx.scan import Scan
from MobileApps.libs.flows.web.hpx.print import Print
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.hpx.devices_mfe import DevicesMFE
from MobileApps.libs.flows.windows.hpx_rebranding.audio import Audio
from MobileApps.libs.flows.windows.hpx.utility.api_utility import APIUtility
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.web.hpx.devices_details_pc_mfe import DevicesDetailsPCMFE
from MobileApps.libs.flows.web.hpx.devices_support_pc_mfe import DevicesSupportPCMFE
from MobileApps.libs.flows.windows.hpx_rebranding.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx_rebranding.utility.property_utilities import PropertyUtilities
from MobileApps.libs.flows.web.hpx.devices_details_printer_mfe import DevicesDetailsPrinterMFE
from MobileApps.libs.flows.windows.hpx_rebranding.hppk import HPPK
from MobileApps.libs.flows.web.hpx.print import Print
from MobileApps.libs.flows.web.hpx.printables import Printables
from MobileApps.libs.flows.web.hpx.hp_cloud_scan import HPCloudScan
from MobileApps.libs.flows.web.hpx.printer_status import PrinterStatus
from MobileApps.libs.flows.web.hpx.add_printer import AddPrinter
from MobileApps.libs.flows.web.hpx.shortcuts import Shortcuts
from MobileApps.libs.flows.web.hpx.mobilefax import MobileFax
from MobileApps.libs.flows.web.hpx.diagnose_fix import DiagnoseFix
from MobileApps.libs.flows.web.hpx.printer_settings import PrinterSettings
from MobileApps.libs.flows.windows.hpx_rebranding.display_control import DisplayControl
from MobileApps.libs.flows.web.hpx.hpx_fuf import HpxFUF
from MobileApps.libs.flows.windows.hpx_rebranding.touchpad import Touchpad
from MobileApps.libs.flows.windows.hpx_rebranding.dock_station import DockStation
from MobileApps.libs.flows.windows.hpx_rebranding.gestures import Gestures
from MobileApps.libs.flows.windows.hpx_rebranding.wellbeing import Wellbeing
from MobileApps.libs.flows.windows.hpx_rebranding.battery import Battery
from MobileApps.libs.flows.windows.hpx_rebranding.energy_consumption import EnergyConsumption
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_common import HPXRebrandingCommon
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_utility import HPXRebrandingUtility
from MobileApps.libs.flows.windows.hpx_rebranding.system_control import SystemControl
from MobileApps.libs.flows.windows.hpx_rebranding.presence_sensing import PresenceSensing
from MobileApps.libs.flows.windows.hpx_rebranding.smart_experience import SmartExperience
from MobileApps.libs.flows.windows.hpx_rebranding.pen_control import PenControl
from MobileApps.libs.flows.windows.hpx_rebranding.video_control import VideoControl
from MobileApps.libs.flows.windows.hpx_rebranding.context_aware import ContextAware
from MobileApps.libs.flows.windows.hpx_rebranding.hp_go import HPGo
from MobileApps.libs.flows.windows.hpx_rebranding.css import CSS
from MobileApps.libs.flows.windows.hpx_rebranding.profile import Profile
from MobileApps.libs.flows.windows.hpx_rebranding.feedback import Feedback
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_settings import HPXSettings
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_support import HPXSupport
from MobileApps.libs.flows.windows.hpx_rebranding.virtual_assistant import VirtualAssistant
from MobileApps.libs.flows.windows.hpx_rebranding.accessibility import Accessibility
from MobileApps.libs.flows.windows.hpx_rebranding.app_consents import AppConsents
from MobileApps.libs.flows.windows.hpx_rebranding.device_card import DeviceCard
from MobileApps.libs.flows.windows.hpx_rebranding.bell_icon import BellIcon
from MobileApps.libs.flows.windows.hpx_rebranding.supplies_status import SuppliesStatus
from MobileApps.libs.flows.windows.hpx_rebranding.aic import Aic
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc import windows_utils
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.windows.hpx_rebranding.task_group import TaskGroup
from MobileApps.libs.flows.windows.hpx_rebranding.smart_displays import SmartDisplays
from MobileApps.libs.one_simulator.printer_simulation import create_simulator_printer_from_api
from MobileApps.libs.flows.windows.hpx_rebranding.for_you_page import ForYouPage
from MobileApps.libs.flows.windows.hpx_rebranding.add_device import AddDevice
from MobileApps.libs.ma_misc.live_printer import LivePrinter
from selenium.webdriver.common.keys import Keys

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        # Cache for MFE locale files to avoid repeated network calls
        self._mfe_locale_cache = {}
        self.fd = {
                   "devicesMFE": DevicesMFE(driver),
                   "devicesDetailsMFE": DevicesDetailsPrinterMFE(driver),
                   "scan": Scan(driver),
                   "print": Print(driver),
                   "printables": Printables(driver),
                   "hp_cloud_scan": HPCloudScan(driver),
                   "printer_status": PrinterStatus(driver),
                   "addprinter": AddPrinter(driver),
                   "shortcuts": Shortcuts(driver),
                   "mobilefax": MobileFax(driver),
                   "diagnosefix": DiagnoseFix(driver),
                   "printersettings": PrinterSettings(driver),
                   "audio": Audio(driver),
                   "hppk": HPPK(driver),
                   "devices_details_pc_mfe": DevicesDetailsPCMFE(driver),
                   "devices_support_pc_mfe": DevicesSupportPCMFE(driver),
                   "display_control": DisplayControl(driver),
                   "hpx_rebranding_common": HPXRebrandingCommon(driver),
                   "hpx_rebranding_utility": HPXRebrandingUtility(driver),
                   "hpx_fuf": HpxFUF(driver),
                   "touchpad": Touchpad(driver),
                   "dock_station": DockStation(driver),
                   "gestures": Gestures(driver),
                   "wellbeing": Wellbeing(driver),
                   "battery": Battery(driver),
                   "energy_consumption": EnergyConsumption(driver),
                   "system_control": SystemControl(driver),
                   "presence_sensing": PresenceSensing(driver),
                   "smart_experience": SmartExperience(driver),
                   "wellbeing": Wellbeing(driver),
                   "pen_control":PenControl(driver),
                   "video_control": VideoControl(driver),
                   "context_aware": ContextAware(driver),
                   "hp_go": HPGo(driver),
                   "css": CSS(driver),
                   "profile": Profile(driver),
                   "feedback": Feedback(driver),
                   "hpx_settings": HPXSettings(driver),
                   "hpx_support": HPXSupport(driver),
                   "virtual_assistant": VirtualAssistant(driver),
                   "accessibility": Accessibility(driver),
                   "app_consents": AppConsents(driver),
                   "device_card": DeviceCard(driver),
                   "bell_icon": BellIcon(driver),
                   "hpid": HPID(driver),
                   "supplies_status": SuppliesStatus(driver),
                   "aic": Aic(driver),
                   "task_group": TaskGroup(driver),
                   "smart_displays": SmartDisplays(driver),
                   "registry_utilities": RegistryUtilities(driver.ssh),
                   "for_you_page": ForYouPage(driver),
                   "add_device": AddDevice(driver), 
                   "live_printer": LivePrinter(driver)
                   }

    @property
    def flow(self):
        return self.fd

    def launch_app(self, skip=False):
        self.driver.launch_app()
        if not skip:
            if self.fd["hpx_fuf"].verify_accept_cookies_button_show():
                self.fd["hpx_fuf"].click_accept_cookies_button()
            if self.fd["hpx_fuf"].verify_camera_yes_button_show():
                self.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
                if self.fd["hpx_fuf"].verify_camera_yes_button_show():
                    self.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        if self.fd["hpx_fuf"].verify_privacy_page_heading_show():
            self.fd["hpx_fuf"].click_privacy_page_heading()
            time.sleep(2)
            self.swipe_window(direction="down", distance=4)
            self.fd["devicesMFE"].swipe_to_end()
        # if self.fd["hpx_fuf"].verify_continue_update_button_show():
        #     self.fd["hpx_fuf"].click_continue_update_button()
        #     time.sleep(5)
        # if self.fd["hpx_fuf"].verify_continue_update_button_show():
        #     self.fd["hpx_fuf"].click_continue_update_button()
        #     time.sleep(5)
        # if self.fd["hpx_fuf"].verify_cancel_update_button_show():
        #     self.fd["hpx_fuf"].click_cancel_update_button()
        #     time.sleep(5)
        if self.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fd["hpx_fuf"].click_accept_all_button()
            time.sleep(5)
        if self.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fd["hpx_fuf"].click_continue_as_guest_button()
            time.sleep(5)
        if not skip:
            if self.fd["hpx_fuf"].verify_what_is_this_dialog_show():
                self.fd["hpx_fuf"].click_what_is_new_skip_button()
        self.fd["devicesMFE"].maximize_the_hpx_window()

    def close_app(self):
        self.driver.terminate_app()
        time.sleep(5)

    def restart_app(self):
        self.driver.restart_app()

    def restart_hpx(self):
        for attempt in range(3):
            if pytest.app_info == "HPX":
                self.close_app()
                time.sleep(10)
                self.driver.launch_app()
            else:
                self.close_myHP()
                time.sleep(10)
                self.launch_myHP_command()
            assert self.is_app_open() is True, "My HP App does not launch successfully!"
            
            # Verify device card shows up, retry once if failed
            if self.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(timeout=120, raise_e=False):
                self.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()
                time.sleep(5)
                self.fd["devices_details_pc_mfe"].click_back_devices_button()
            if self.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
                self.fd["devicesMFE"].maximize_the_hpx_window()
                logging.info(f"HPX restarted successfully on attempt {attempt + 1} time")
                return
            
            if attempt <= 1:
                logging.warning(f"Device card not shown after {attempt + 1} attempt restart, retrying...")
        
        # Final verification with raise_e=True on second attempt
        self.fd["devicesMFE"].verify_device_card_show_up()

    def reset_hpx(self, printer_obj):
        if pytest.app_info == "HPX":
            self.close_app()
        else:
            self.close_myHP()
        time.sleep(5)
        self.reset_myHP_app_through_command()
        # Copy SharedSettings.json file to simulate Migration flow for adding printer.
        self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/SharedSettings.json"), w_const.TEST_DATA.HPX_SHARED_JSON_PATH + "\\" + "SharedSettings.json")
        # Copy properties.json to LocalState folder to enable ITG/STG build logging level
        remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        # self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/properties.json"), remote_artifact_path + "properties.json")
        time.sleep(2)
        if "pie" not in self.driver.session_data['request'].config.getoption("--stack").lower():
            # Copy LoggingData.xml and properties.json.dat files to enable production logging level
            self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/properties.json.dat"), remote_artifact_path + "properties.json.dat")
            self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/LoggingData_prod.xml"), remote_artifact_path + "\\Logs\\" + "LoggingData.xml")

        if pytest.app_info == "HPX":
            self.driver.launch_app()
        self.launch_hpx_to_home_page()

        self.add_a_printer(printer_obj=printer_obj)

    def launch_hpx_to_home_page(self):
        if pytest.app_info == "DESKTOP":
            # Appium driver will not launch myHP app when app info set to DESKTOP, so use command to launch myHP here.
            self.launch_myHP_command()
        if self.fd["hpx_fuf"].verify_privacy_page_heading_show():
            self.fd["hpx_fuf"].click_privacy_page_heading()
            time.sleep(2)
            self.swipe_window(direction="down", distance=4)
            self.fd["devicesMFE"].swipe_to_end()
        if self.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fd["hpx_fuf"].click_accept_all_button()
            time.sleep(5)
        if self.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fd["hpx_fuf"].click_continue_as_guest_button()
            time.sleep(5)
        self.fd["devicesMFE"].maximize_the_hpx_window()
        if self.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(timeout=120, raise_e=False):
            self.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()
            time.sleep(5)
            self.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fd["devicesMFE"].verify_device_card_show_up()
        logging.info("Launch to HPX home page successfully.")

    def check_files_exist(self, destination_file, source_file):
        check_destination_file = self.driver.ssh.send_command("Test-Path " + destination_file)
        s_file = ma_misc.get_abs_path(source_file)
        if "True" not in check_destination_file['stdout']:
            logging.info(f"{destination_file} does not exist. Start to copy file.")
            self.driver.ssh.send_file(s_file, destination_file)
        else:
            logging.info(f"{destination_file} already exists.")
    
    def refresh_device_mfe(self):
        return self.fd["devicesMFE"].refresh_device_mfe()

    def maximize_window(self):
        self.driver.maximize_window()

    def is_myHP_installed(self):
        result = self.driver.ssh.send_command('powershell "Get-AppxPackage *myHP*"')
        returnbool = "AD2F1837.myHP" in result["stdout"]
        return returnbool

    def uninstall_app(self):
        self.driver.ssh.send_command("Stop-Process -Force -name HP.myHP", raise_e=False, timeout=20)
        time.sleep(3)
        self.driver.ssh.remove_app("*myHP*", timeout=80)

    def install_app(self, install_path):
        time.sleep(5)
        task_utilities = TaskUtilities(self.driver.ssh)
        task_utilities.restart_fusion_service()
        time.sleep(5)
        app_path = install_path + '\\Install.ps1'
        self.driver.ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File {app_path} -Force" /sc once /st 00:00 /f', timeout=60)
        self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
        time.sleep(10)
        file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\LocalCache"'
        file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
        max_attempts = 25
        for _ in range(max_attempts):
            if file_exist:
                break
            time.sleep(10)
            file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
        time.sleep(10)
        self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)

    def re_install_app(self, install_path):
        time.sleep(5)
        self.uninstall_app()
        time.sleep(15)
        self.install_app(install_path)
    
    def intial_environment(self):
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\registration\\device_registration_request.xml',  raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\registration\\device_registration_response.xml', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\registration\\registration_subset.xml', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\registration\\full_registration_request.xml', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\registration\\full_registration_response.xml', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\Settings\\settings.dat', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\TempState\\myHP\\PulsarAnalyticsLog.txt', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\SharedServices\\shared_store.dat',raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell REG delete HKLM\\SOFTWARE\\Policies\\HP\\Consent /f', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell REG ADD HKLM\\SOFTWARE\\HP\\Bridge /v registration_oobe_sleep /t REG_DWORD /d 1280 /f',raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im SysInfoCap.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im AppHelperCap.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im NetworkCap.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Remove-Item -Path C:\\ProgramData\\HP\\SharedServices\\shared_store.dat',raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Start-Service -Name HPNetworkCap', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Start-Service -Name HPAppHelperCap', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell Start-Service -Name HPSysInfoCap', raise_e=False, timeout=10)
        time.sleep(30)

    def is_app_open(self):
        result = self.driver.ssh.send_command("tasklist.exe")
        returnbool = "HP.HPX" in result["stdout"]
        return returnbool

    def get_app_version(self, install_path):
        version = install_path.split("_")[3]
        return version
    
    def turn_on_hp_privacy_page(self, ssh):
        re = RegistryUtilities(ssh)
        if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
            re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        
        if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
            re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")

        if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")

    def click_login_page(self):
        if self.fd["hp_login"].verfiy_login_page_show():
            self.fd["hp_login"].close_login_page()
    
    def install_audio_standalone_app(self):
        app_path = "C:\\build\\HPAudioCenter_1.51.339.0_x64.appxbundle_Windows10_PreinstallKit\\c41e3bdae63c47bcbb2511a09e7cecbd.appxbundle"
        if "HPAudio" in app_path:
            self.driver.ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell Add-AppxPackage -Path {app_path} -ForceApplicationShutdown" /sc once /st 00:00 /f', timeout=60)   
            self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
            time.sleep(10)
            file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.HPAudioCenter_1.51.339.0_x64__v10z8vjag6ke6"'
            file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            max_attempts = 5
            for _ in range(max_attempts):
                if file_exist:
                    break
                time.sleep(10)
                file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            time.sleep(10)
            self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)

    def install_audio_standalone_app_for_commercial_machine(self):
        app_path = "C:\\build\\BangOlufsenAudioControl_1.51.339.0_x64.appxbundle_Windows10_PreinstallKit\\9297435f796b4acd9b8af72e5022e3d6.appxbundle"
        if "BangOlufsenAudioControl" in app_path:
            self.driver.ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell Add-AppxPackage -Path {app_path} -ForceApplicationShutdown" /sc once /st 00:00 /f', timeout=60)   
            self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
            time.sleep(10)
            file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.BangOlufsenAudioControl_v10z8vjag6ke6"'
            file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            max_attempts = 5
            for _ in range(max_attempts):
                if file_exist:
                    break
                time.sleep(10)
                file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            time.sleep(10)
            self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)
    
    def install_audio_standalone_app_with_path(self):
        self.driver.ssh.send_command('powershell.exe -ExecutionPolicy Bypass -File "C:\\build\HPAudioControl_19H1_2.51.339.99_Test\\Install.ps1" -Force',timeout=30, raise_e=False)
                
    def uninstall_audio_standalone_app(self):
        self.driver.ssh.send_command('powershell "Remove-AppxPackage -Package "AD2F1837.HPAudioCenter_1.51.339.0_x64__v10z8vjag6ke6"', timeout=40, raise_e=False)

    def uninstall_audio_standalone_app_for_commercial_machine(self):
        self.driver.ssh.send_command('powershell "Get-AppxPackage *BangOlufsenAudioControl* | Remove-AppxPackage"', timeout=60, raise_e=False)
        
    def set_privacy_consents(self, registry_path, registry_list):

        for registry_value in registry_list:
            if self.re.get_value(registry_path, registry_value[0], registry_value[1]) is False:
                self.re.update_value(registry_path, registry_value[0], registry_value[1])
    

    def re_install_app_and_skip_fuf(self, path):
        self.re_install_app_and_skip_login_page(path)
        if self.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fd["hp_privacy_setting"].click_decline_all_button()

        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()
            
    def install_audio_standalone_and_skip_fuf(self, path):
        self.install_audio_standalone()
        time.sleep(5)
        self.re_install_app(path)
        time.sleep(5)
        self.launch_app()

        self.click_login_page()
        if self.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fd["hp_privacy_setting"].click_decline_all_button()

        assert self.fd["hp_registration"].verify_skip_button_show() is True
        self.fd["hp_registration"].click_skip_button()

    def re_install_app_and_skip_login_page(self, path):

        self.re_install_app(path)
        time.sleep(3)
        self.launch_app()
        time.sleep(3)
        self.click_login_page()
        time.sleep(2)
        
    def re_install_app_launch_myHP(self, path):
        self.re_install_app(path)
        time.sleep(3)
        self.launch_myHP()

    def launch_myHP_command(self):
        try:
            self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout=80)
        except Exception as e:
            logging.info("Failed to launch myHP through command, trying from start menu")
            self.fd["accessibility"].open_app_from_start_menu("HP", open_app=True)

    def launch_myHP(self, skip=False, terminate_hp_background_apps=False):
        self.minimize_all_apps()
        try:
            self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout=40)
        except Exception as e:
            logging.info("Failed to launch myHP through command, trying from start menu")
            self.fd["accessibility"].open_app_from_start_menu("HP", open_app=True)
        if not skip:
            if self.fd["hpx_fuf"].verify_camera_yes_button_show():
                self.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
                if self.fd["hpx_fuf"].verify_camera_yes_button_show():
                    self.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        if self.fd["hpx_fuf"].verify_privacy_page_heading_show():
            self.fd["hpx_fuf"].click_privacy_page_heading()
            time.sleep(2)
            self.swipe_window(direction="down", distance=4)
        if self.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fd["hpx_fuf"].click_accept_all_button()
            time.sleep(5)
        if self.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fd["hpx_fuf"].click_continue_as_guest_button()
            time.sleep(5)
        self.fd["devicesMFE"].maximize_the_hpx_window()
        if not skip:
            if self.fd["hpx_fuf"].verify_what_is_this_dialog_show():
                self.fd["hpx_fuf"].click_what_is_new_skip_button()
            self.reopen_hp_app_for_blank_screen(terminate_hp_background_apps)

    def launch_myHP_and_skip_fuf(self, terminate_hp_background_apps=False):
        try:
            self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout=40)
        except Exception as e:
            logging.info("Failed to launch myHP through command, trying from start menu")
            self.fd["accessibility"].open_app_from_start_menu("HP", open_app=True)
        time.sleep(3)
        if self.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fd["hpx_fuf"].click_accept_all_button()
            time.sleep(10)
        if self.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fd["hpx_fuf"].click_continue_as_guest_button()
            time.sleep(10)
        self.fd["devicesMFE"].maximize_the_hpx_window()
        self.reopen_hp_app_for_blank_screen(terminate_hp_background_apps)    

    def launch_myHP_hotkey(self):
        self.driver.ssh.send_command("Start-Process hpx://support/device")

    def launch_hotkey(self, custom_protocol):
        self.driver.ssh.send_command("Start-Process {}".format(custom_protocol))

    def initial_hpx_printer_env(self):
        self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/SharedSettings.json"), w_const.TEST_DATA.HPX_SHARED_JSON_PATH + "\\" + "SharedSettings.json")

        remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_stage"]:
            self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/properties_stg.json"), remote_artifact_path + "properties.json")
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie"]:
            self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/properties.json"), remote_artifact_path + "properties.json")

    def initial_hpx_support_env(self):
        re = RegistryUtilities(self.driver.ssh)
        remote_artifact_path = "{}\\{}\\LocalState\\".format(
            w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if self.driver.ssh.check_directory_exist(remote_artifact_path, create=False, raise_e=False):
            self.driver.ssh.remove_file_with_suffix(remote_artifact_path, ".json") 
            logging.info("remove json file in LocalState")
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", "244") 
            
    def install_bundle(self, app_location):
        try:
            extra_install_ls_result = [x for x in self.driver.ssh.send_command("ls " + app_location + " -Name")["stdout"].split("\r\n") if ".msixbundle" in x]
            extra_installer_file = extra_install_ls_result[0]
        except AttributeError:
            extra_installer_file = ""               
        self.driver.ssh.install_bundle(app_location + "\\" + extra_installer_file)
        return app_location

    def remove_file(self, path):
        self.driver.ssh.send_command("Remove-Item -LiteralPath '{}' -Force -Recurse".format(path), raise_e=False, timeout=10)
        
    def verify_hpx_support_folder(self):
        sftp = self.driver.ssh.client.open_sftp()
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\HPSAAppLauncher.exe") 
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\HPSALauncher.exe")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\HPSACommand.dll")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\OCChat\\Microsoft.Web.WebView2.Core.dll")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\OCChat\\Microsoft.Web.WebView2.Wpf.dll")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\OCChat\\OCChat.exe")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\OCChat\\runtimes\\win-x64\\native\\WebView2Loader.dll")
        sftp.stat(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH + "\\OCChat\\runtimes\\win-x86\\native\\WebView2Loader.dll")

    def get_file_version(self, file_path):
        file_version = self.driver.ssh.send_command("(Get-Item '{}').VersionInfo.FileVersion".format(file_path))
        return file_version['stdout'].strip()

    def load_simulate_file(self, file_path):
        file_content = saf_misc.load_json(file_path)
        return file_content

    def initial_supportcore(self):
        hp_support = {}
        hp_support["@hp-af/feature-switch/overrides"] = {"supporthome-core" : True}
        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = self.driver.ssh.remote_open(remote_path, "w+")
        json.dump(hp_support, fh)
        fh.close()
        if self.driver.session_data['request'].config.getoption("--stack") in ["production"]:
            self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')  

    def initial_environment(self):
        pass
        # pu = PropertyUtilities(self.driver.ssh)
        # pu.copy_simulate_file()
        # if self.driver.session_data['request'].config.getoption("--stack") in ["production"]:
        #     self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')  
    
    def set_featureflags(self, flag_dict):
        pu = PropertyUtilities(self.driver.ssh)
        pu.set_featureflags(flag_dict)
        if self.driver.session_data['request'].config.getoption("--stack") in ["production"]:
            self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')  

    def initial_feature(self):
        hp_support = {}    
        file_content = self.load_simulate_file(ma_misc.get_abs_path("/resources/test_data/hpsa/simulate/properties.json"))
        features = file_content.get('@hp-af/feature-switch/overrides')

        if self.driver.session_data['request'].config.getoption("--test-RN"):
            features["supporthome-core"] = True

        hp_support["@hp-af/feature-switch/overrides"] = features 
        if  self.driver.session_data['request'].config.getoption("--portal-env") is not None:
            portal = self.driver.session_data['request'].config.getoption("--portal-env")    
            if portal in ['stg']:
                hp_support["@env/SUPPORT_URL"] = "https://hpx.stage.portalshell.int.hp.com"
            elif portal in ['itg']:
                hp_support["@env/SUPPORT_URL"] = "https://hpx.pie.portalshell.int.hp.com"

        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = self.driver.ssh.remote_open(remote_path, "w+")
        logging.info("properties.json=" + str(hp_support))
        logging.info("have supporthome-core:" + str(str(hp_support).find("supporthome-core") > 0))
        logging.info("have SUPPORT_URL section:" + str(str(hp_support).find("https://hpx.stage.portalshell.int.hp.com") > 0))
        json.dump(hp_support, fh) 
        fh.close()

        self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')  

    def update_hpx_support_deviceinfo(self, section, key, value):
        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        
        if self.driver.ssh.check_file(remote_path):

            with self.driver.ssh.remote_open(remote_path,'r') as f:
                fc = f.read()  
                file_data=json.loads(fc)
                if section in ["@hp-support/deviceInfo"]:
                    device_info = json.loads(file_data["@hp-support/deviceInfo"])
                    device_info[key] = value
                    device_info = json.dumps(device_info, indent=4)
                    file_data["@hp-support/deviceInfo"] = device_info
                else:
                    file_data[section] = value
                data=json.dumps(file_data, indent=4)
                f.close()
                remote_file = self.driver.ssh.remote_open(remote_path,mode="w")
                remote_file.write(data)
                remote_file.close()
                stack = self.driver.session_data['request'].config.getoption("--stack")
                if stack in ["production"]:
                    self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')   

    def click_accept_all_btn_privacy(self):
        self.restart_app()
        if self.fd["hp_privacy_setting"].verify_accept_all_btn_privacy():
            self.fd["hp_privacy_setting"].click_accept_all_btn_privacy()

    def initial_simulate_warranty_file(self, file_path, testrail_id, env, simulate_name, stack=None ):
        file_content = self.load_simulate_file(file_path)
        device_info = file_content[testrail_id][env]
        device_info = json.dumps(device_info)
        hp_support = {}
        if file_content[testrail_id][env].get('errorMessage') != None:
            hp_support["errorMessage"] = file_content[testrail_id][env].get('errorMessage')
        if file_content[testrail_id][env].get('warrantyStartDate') != None:
            hp_support["warrantyStartDate"] = file_content[testrail_id][env].get('warrantyStartDate')
        if file_content[testrail_id][env].get('warrantyEndDate') != None:
            hp_support["warrantyEndDate"] = file_content[testrail_id][env].get('warrantyEndDate')
        if file_content[testrail_id][env].get('status') != None:
            hp_support["status"] = file_content[testrail_id][env].get('status')
        if file_content[testrail_id][env].get('statusCode') != None:
            hp_support["statusCode"] = file_content[testrail_id][env].get('statusCode')
        if file_content[testrail_id][env].get('carepack') != None:
            hp_support["carepack"] = file_content[testrail_id][env].get('carepack')
        if file_content[testrail_id][env].get('msgCodes') != None:
            hp_support["msgCodes"] = file_content[testrail_id][env].get('msgCodes')
        if file_content[testrail_id][env].get('userCheckDate') != None:
            hp_support["userCheckDate"] = file_content[testrail_id][env].get('userCheckDate')
        remote_path = "{}\\{}\\LocalState\\{}".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX, simulate_name)
        fh = self.driver.ssh.remote_open(remote_path, "w+")
        json.dump(hp_support, fh)
        fh.close()
        if stack == "production":
            self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')

    def get_ccls_services(self, build_type, product_big_series_oid, product_name_oid, product_series_oid, lang_country="en-US"):
        service_list = []
        api_utility = APIUtility(build_type)
        data = api_utility.post_get_work_hours(product_big_series_oid, product_name_oid, product_series_oid, lang_country)
        ccls_data = json.loads(data.text)
        contact_options = ccls_data['ContactOptionsFull']
        for contact_option in contact_options:
            service_title = contact_option['serviceTitle']
            service_list.append(service_title)
        return service_list

    def verify_hp_id_sign_in(self, web_driver=None):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ['production_NA']:
            return self.fd["hpid"].verify_hp_id_sign_in()
        elif stack in ['stage', 'pie', 'production']:
            window_name = "hpx_login"
            time.sleep(3)
            web_driver.wait_for_new_window(timeout=20)
            web_driver.add_window(window_name)
            time.sleep(3)
            try:
                web_driver.switch_window(window_name)
                self.hpid = HPID(web_driver, window_name=window_name)
                return self.hpid.verify_hp_id_sign_in()
            except KeyError:
                return False
    
    def hpx_sign_in_advanced_account(self, web_driver=None):
        """
        Login with adv account to test advanced scan with stage/prod build.
        """
        detected_stack = self.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(w_const.HPX_ACCOUNT.account_details_path))["adv_scan_stg"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(w_const.HPX_ACCOUNT.account_details_path))["adv_scan_prod"]
        sign_in_email, sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
        self.sign_in(sign_in_email, sign_in_password, web_driver=web_driver, send_before_click=False)
        self.fd["devicesMFE"].verify_login_successfully()
        if self.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(raise_e=False):
            self.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()
            time.sleep(5)
            self.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fd["devicesMFE"].verify_device_card_show_up()

    def click_dialog_close_btn(self, web_driver=None):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ['production_NA']:
            self.fd["hpid"].click_popup_close_btn()
        elif stack in ['stage', 'pie', 'production']:
            window_name = "hpx_login"
            time.sleep(3)
            web_driver.add_window(window_name)
            time.sleep(3)
            web_driver.switch_window(window_name)
            web_driver.close_window(web_driver.current_window)
    
    def verify_sign_in(self, web_driver=None):
        self.fd["navigation_panel"].select_my_hp_account_btn()
        return self.verify_hp_id_sign_in(web_driver)
    
    def click_profile_button(self):
        self.fd["devicesMFE"].click_profile_button()

    def stop_hpsysinfo_fusion_services(self):
        self.driver.ssh.send_command('Stop-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    def start_hpsysinfo_fusion_services(self):
        self.driver.ssh.send_command('Start-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    def get_hpsysinfo_fusion_services(self):
        return self.driver.ssh.send_command('Get-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    def stop_hpanalytics_fusion_services(self):
        self.driver.ssh.send_command('Stop-Service -Name HpTouchpointAnalyticsService', raise_e=False, timeout=10)

    def start_hpanalytics_fusion_services(self):
        self.driver.ssh.send_command('Start-Service -Name HpTouchpointAnalyticsService', raise_e=False, timeout=10)           

    def sign_out(self, web_driver=None, hpx_logout=False):
        if hpx_logout:
            self.fd["hpx_settings"].sign_out_from_settings() 
            self.fd["devicesMFE"].verify_logout_successfully()
        else:
            stack = self.driver.session_data['request'].config.getoption("--stack")
            time.sleep(15)
            self.fd["navigation_panel"].select_my_hp_account_btn()
            logged_in = self.fd["navigation_panel"].verify_fly_out_sign_in_page()
            if logged_in:
                self.fd["navigation_panel"].select_my_hp_sign_out_btn()
            else:
                if stack in ['NA']:
                    time.sleep(3)
                    self.fd["hpid"].click_popup_close_btn()
                    time.sleep(3)
                elif stack in ['stage', 'pie', 'production', 'production_NA']:
                    window_name = "hpx_login"
                    web_driver.wait_for_new_window(timeout=20)
                    web_driver.add_window(window_name)   
                    time.sleep(3)
                    web_driver.switch_window(window_name)             
                    web_driver.close_window(web_driver.current_window)            

    def sign_in(self, username, password, web_driver=None, user_icon_click=True, sign_in_from_profile=False, send_before_click=True, min_win=False):
        window_name = "hpx_login"
        if user_icon_click:
            if sign_in_from_profile:
                self.fd["devices_support_pc_mfe"].select_my_hp_account_btn()
            else:
                self.fd["devicesMFE"].select_my_hp_account_btn()        
        web_driver.wait_for_new_window(timeout=20)
        time.sleep(3)
        web_driver.add_window(window_name)
        time.sleep(3)
        web_driver.switch_window(window_name)
        time.sleep(3)
        web_driver.set_size("max")
        self.hpid = HPID(web_driver, window_name=window_name)
        self.hpid.login(username, password, send_before_click=send_before_click)  
        time.sleep(5)
        open_myhp_alert = self.fd["css"].verify_open_myhp_alert()
        if open_myhp_alert:
            self.fd["css"].click_open_myhp_alert_btn()
        else:
            logging.info("No myHP alert present")
        if min_win is False:
            web_driver.close_window(web_driver.current_window)
        elif min_win is True:
            web_driver.set_size("min")

    def hpx_sign_in_flow(self, web_driver=None):
        detected_stack = self.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(w_const.HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(w_const.HPX_ACCOUNT.account_details_path))["hpid"]
        sign_in_email, sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
        self.sign_in(sign_in_email, sign_in_password, web_driver=web_driver, send_before_click=False)
        self.fd["devicesMFE"].verify_login_successfully()
        if self.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(raise_e=False):
            self.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()
            time.sleep(5)
            self.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fd["devicesMFE"].verify_device_card_show_up()

    def chrome_data_cleanup(self):
        self.driver.ssh.send_command('Stop-Process -Name "chrome" -Force -ErrorAction SilentlyContinue', raise_e=False)
        commands = [
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\*"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Storage\\*"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data"'
        ]
        for cmd in commands:
            self.driver.ssh.send_command('Remove-Item -Path ' + cmd + ' -Recurse -Force')
            time.sleep(1)
        logging.info("Chrome user data cleanup complete.")

    def create_account_from_webpage(self, web_driver=None):
        window_name = "hpx_signup"   
        try:
            web_driver.wait_for_new_window(timeout=20)
            web_driver.set_size("max")
            web_driver.add_window(window_name)
            time.sleep(3)
            web_driver.switch_window(window_name)
            time.sleep(3)
            self.hpid = HPID(web_driver, window_name=window_name)
            if self.hpid.verify_create_account_link(raise_e=False):
                self.hpid.click_create_account_link()
            time.sleep(5)
            self.hpid.create_account()
        finally:
            web_driver.set_size("min") 

    def update_properties(self,language):
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = open(ma_misc.get_abs_path("/resources/test_data/hpx/locale/temp.json"),"r") 
        data = fh.read()         
        file_data=json.loads(data)
        file_data["@hp-af/localization/current-locale"] = language
        data=json.dumps(file_data, indent=4)
        fh.close()
        remote_file = self.driver.ssh.remote_open(self.remote_artifact_path+"properties.json",mode="w")
        remote_file.write(data)
        remote_file.close()
        if language == "zh-Hant-HK" or language == "sr-LATN-rs":
            properties_dat_file = ma_misc.get_abs_path("/resources/test_data/hpx/locale/zh_hant_hk_sr_latn_rs_properties.json.dat")
            self.driver.ssh.send_file(properties_dat_file, self.remote_artifact_path + "properties.json.dat")
        elif language == "zh-Hans" or language == "zh-Hant":
            properties_dat_file = ma_misc.get_abs_path("/resources/test_data/hpx/locale/zh_hans_zh_hant_properties.json.dat")
            self.driver.ssh.send_file(properties_dat_file, self.remote_artifact_path + "properties.json.dat")
        else:
            properties_dat_file = ma_misc.get_abs_path("/resources/test_data/hpx/locale/properties.json.dat")
            self.driver.ssh.send_file(properties_dat_file, self.remote_artifact_path + "properties.json.dat")
    
    def myhp_login_startup_for_localization_scripts(self,language):
        self.update_properties(language)
        self.close_app()
        self.launch_app()
        time.sleep(6)
        if bool (self.fd["hp_registration"].verify_hpone_page_show()):
            self.fd["hp_registration"].click_hpone_page_skip_btn()

        if bool (self.fd["hp_registration"].verify_registration_page_is_display()):
            self.driver.swipe(direction="down", distance=3)
            if self.fd["hp_registration"].verify_skip_button_show():
                self.fd["hp_registration"].click_skip_button()
            else:
                logging.info("skip button not available")
        else:
            logging.info("registration page not displayed")
        if bool (self.fd["dropbox"].verify_dropbox_header_show()):
            self.fd["dropbox"].click_skip_button() 
        else:
            logging.info("Dropbox page not displayed")  
        if "Maximize HP" == self.fd["devices"].verify_window_maximize():
            self.fd["devices"].maximize_app()
        self.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fd["navigation_panel"].click_PC_device_menu()

    def get_winsystemlocale(self):
        result = self.driver.ssh.send_command("(Get-UICulture).Name")
        if result['stdout'].strip() in ["en-US"]:
            result = self.driver.ssh.send_command("(Get-WinHomeLocation).GeoId")
            if result['stdout'].strip() == "205":
                return "ar-SA"
            elif result['stdout'].strip() == "227":
                return "th-TH"        
            else:
                return "en-US"
        else:
            return result['stdout'].strip()
    
    def update_hpx_support_locale(self, language):
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = open(ma_misc.get_abs_path("/resources/test_data/hpsa/simulate/temp.json"),"r") 
        data = fh.read()         
        file_data=json.loads(data)
        file_data["@hp-af/localization/current-locale"] = language
        file_data["@hp-support/region"] = language.split("-")[1]
        fh.close()

        remote_file = self.driver.ssh.remote_open(self.remote_artifact_path+"properties.json",mode="r")
        remote_file_data = json.load(remote_file)
        remote_file_data.update(file_data)
        remote_file.close()

        remote_file = self.driver.ssh.remote_open(self.remote_artifact_path+"properties.json",mode="w")
        json.dump(remote_file_data, remote_file, indent=4)
        remote_file.close()
        
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ["production"]:
            self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')
    
    def select_country(self, country_code, current_locale=None):
        time.sleep(3)
        country_name = self.click_countrylist(country_code, current_locale)
        time.sleep(3)
        self.fd["devices_support_pc_mfe"].select_country_by_country_name(country_name)   
    
    def click_countrylist(self, country_code, current_locale=None):
        if current_locale is None:
            system_locale = self.get_winsystemlocale().strip()
            country_name = ma_misc.load_json_file("resources/test_data/hpsa/locale/country_list.json")[system_locale][country_code]
        else:
            country_name = ma_misc.load_json_file("resources/test_data/hpsa/locale/country_list.json")[current_locale][country_code]
        self.fd["devices_support_pc_mfe"].click_country_list()
        return country_name

    #This close method is created to close app from desktop 
    def close_myHP(self):
        if self.is_app_open():
            self.driver.ssh.send_command("Stop-Process -Force -name HP.HPX")

    def kill_hpx_process(self):
        if "HP.HPX" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command('powershell taskkill /f /im HP.HPX.exe', raise_e=False, timeout=10)

    def kill_chrome_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im chrome.exe', raise_e=False, timeout=10)
    
    def restart_myHP(self, skip=False):
        self.close_myHP()
        time.sleep(3)
        self.launch_myHP(skip=skip)
 
    def update_win_language(self,language):
        self.driver.ssh.send_command('Set-WinUserLanguageList '+language+' -Force',timeout=60)
    
    def enable_dark_mode(self):
        self.driver.ssh.send_command('New-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force', timeout=90, raise_e=False)
        self.driver.ssh.send_command('New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name SystemUsesLightTheme -Value 0 -Type Dword -Force', timeout=90, raise_e=False)
        time.sleep(2)

    def disable_dark_mode(self):
        self.driver.ssh.send_command('Set-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 1 -Type Dword -Force', timeout=90, raise_e=False)
        self.driver.ssh.send_command('Set-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name SystemUsesLightTheme -Value 1 -Type Dword -Force', timeout=90, raise_e=False)
        time.sleep(2)

    def enable_location_access(self):
        # Run these powershell command to enable hpx printer location permission on windows.
        self.driver.ssh.send_command('Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" -Name "Value" -Value "Allow" -Force', raise_e=False)
        self.driver.ssh.send_command('Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" -Name "Value" -Value "Allow" -Force', raise_e=False)
        self.driver.ssh.send_command('$path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location\AD2F1837.myHP_v10z8vjag6ke6"; New-Item -Path $path -Force -ErrorAction SilentlyContinue; Set-ItemProperty -Path $path -Name "Value" -Value "Allow" -Force', raise_e=False)
        time.sleep(2)

    def click_pc_support(self):
        self.fd["navigation_panel"].navigate_to_pc_device()
        self.fd["devices"].click_support_btn()

    def navigate_to_support(self):
        self.fd["navigation_panel"].navigate_to_support()
        self.skip_hpone_signin_popup()

    def navigate_to_settings(self):
        self.fd["navigation_panel"].navigate_to_settings()

    def click_support_control_card(self):
        self.fd["home"].click_support_control_card()
        self.skip_hpone_signin_popup()

    def click_support_btn(self):
        self.fd["devices"].click_support_btn()
        self.skip_hpone_signin_popup()

    def skip_hpone_signin_popup(self):
        wmi=WmiUtilities(self.driver.ssh)
        is_grogu = wmi.is_grogu()
        if is_grogu:
            stack = self.driver.session_data['request'].config.getoption("--stack")
            if stack in ['production_NA']:
                logged_in=self.fd["hpid"].verify_hp_id_sign_in(raise_e=False,timeout=15)
                if logged_in:
                    self.fd["hpid"].click_dialog_close_btn()
                    
    def press_ctrlkey(self, keys_to_send):
        self.driver.press_ctrlkey(keys_to_send) 
        
    def open_system_settings_sound(self):
        self.driver.ssh.send_command('powershell start ms-settings:sound')    
    
    def open_system_setting(self):
        self.driver.ssh.send_command('powershell start ms-settings:')

    def open_system_settings_notifications(self):
        self.driver.ssh.send_command('powershell start ms-settings:notifications')

    def kill_camera_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im HPPresenceVideo.exe', raise_e=False, timeout=10)

    def skip_video_control_first_use_flow(self):
        assert bool(self.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.close_myHP()
        time.sleep(2)
        assert bool(self.fd["video_control"].verify_tutorial_next_button_show()) is True
        self.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fd["video_control"].verify_lets_get_your_show()) is True
        assert bool(self.fd["video_control"].verify_tutorial_next_button_show()) is True
        self.fd["video_control"].click_tutorial_next_button() 
        time.sleep(3)

    def get_hardwareinfo(self, param_key):
        try:
            output = self.driver.ssh.send_command('powershell "Get-Content -Path C:\\Users\\exec\\platform.txt"')
            platform_name = output['stdout'].strip().replace('\r\n', '')

            if not platform_name:
                logging.info("platformName is missing")

            json_data = ma_misc.load_json_file("resources/test_data/hpx/hardwareData.json")
            param_value = json_data[platform_name][param_key]

            if param_value is None or param_value.strip() == '':
                logging.info("paramKey has no value")

            if param_key not in json_data[platform_name]:
                logging.info("Invalid paramKey")

            return param_value
        except ValueError as e:
            raise ValueError("Add platform name").with_traceback(e.__traceback__)
        except KeyError as e:
            raise KeyError("Add value for parameter").with_traceback(e.__traceback__)
        except Exception as e:
            raise Exception("Add parameter key").with_traceback(e.__traceback__)          
    
    def web_password_credential_delete(self):
        # cre_sid = 'S-1-15-2-550980512-1981161223-2389782880-1638197054-2770089683-749402770-3456998262'
        cre_package_sid = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Package Sid"')
        cre_resource = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Resource"')
        cre_identity = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Identity"')
        cre_package_sid_list = cre_package_sid['stdout'].strip().replace('\r\n', '').split('Package Sid: ')
        cre_resource_list = cre_resource['stdout'].strip().replace('\r\n', '').split('Resource: ')
        cre_identity_list = cre_identity['stdout'].strip().replace('\r\n', '').split('Identity: ')
        web_cre_num = len(cre_resource_list)     
        for i in range(1, web_cre_num):
            # if cre_package_sid_list[i] == cre_sid:
            #     self.driver.ssh.send_command('vaultcmd /deletecreds:"Web Credentials" /credtype:"Windows Web Password Credential" /identity:"{0}" /resource:"{1}" /sid:{2}'.format(cre_identity_list[i], cre_resource_list[i], cre_sid))
            self.driver.ssh.send_command('vaultcmd /deletecreds:"Web Credentials" /credtype:"Windows Web Password Credential" /identity:"{0}" /resource:"{1}" /sid:{2}'.format(cre_identity_list[i], cre_resource_list[i], cre_package_sid_list[i]))
        # remote_path = "{}\\{}\\LocalState\\AsyncStorage.db".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        # self.remove_file(remote_path)

    def ensure_web_password_credentials_cleared(self, max_attempts=2):
        """
        Delete all 'Web Credentials' saved by HP from Windows Credential Manager for the current user,
        and assert that they have been fully removed.
        Retries up to max_attempts if credentials persist.
        """
        self.close_myHP()  # Ensure myHP is closed before attempting to delete credentials
        time.sleep(3)  # Wait a moment to ensure all processes are closed
        hp_patterns = ["hp", "hpid", "hpx", "myhp", "hp.com", "hppsdk", "hppsdk.com"]
        for attempt in range(max_attempts):
            cre_resource = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Resource"')
            cre_identity = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Identity"')
            cre_package_sid = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Package Sid"')

            cre_resource_list = cre_resource['stdout'].strip().replace('\r\n', '').split('Resource: ')
            cre_identity_list = cre_identity['stdout'].strip().replace('\r\n', '').split('Identity: ')
            cre_package_sid_list = cre_package_sid['stdout'].strip().replace('\r\n', '').split('Package Sid: ')

            web_cre_num = min(len(cre_resource_list), len(cre_identity_list), len(cre_package_sid_list))

            if web_cre_num <= 1:
                return

            deleted_any = False
            for i in range(1, web_cre_num):
                resource = cre_resource_list[i].lower()
                if any(pattern in resource for pattern in hp_patterns):
                    result = self.driver.ssh.send_command(
                        'vaultcmd /deletecreds:"Web Credentials" /credtype:"Windows Web Password Credential" /identity:"{0}" /resource:"{1}" /sid:{2}'.format(
                            cre_identity_list[i], cre_resource_list[i], cre_package_sid_list[i]
                        )
                    )
                    logging.info("vaultcmd deletecreds result: %s", result)
                    if "Credentials deleted successfully." in result.get("stdout", ""):
                        logging.info("Credential deleted successfully for identity: {}, resource: {}, sid: {}".format(
                            cre_identity_list[i], cre_resource_list[i], cre_package_sid_list[i]
                        ))
                        deleted_any = True
                    elif "Credential deletion error: Element not found." in result.get("stdout", ""):
                        logging.warning("Credential not found for deletion (may have already been deleted): identity: {}, resource: {}, sid: {}".format(
                            cre_identity_list[i], cre_resource_list[i], cre_package_sid_list[i]
                        ))
                    time.sleep(2)
            if deleted_any:
                remote_path = "{}\\{}\\LocalState\\AsyncStorage.db".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
                self.remove_file(remote_path)
                return
            time.sleep(2)
    
    
    def close_windows_settings_panel(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', raise_e=False, timeout=15)
    
    def processing_localization_language(self, translation_file, language, module):
        try:
            lang_settings = ma_misc.load_json_file(translation_file)[language]["translation"][module]
        except KeyError:
            try:
                language = language[0:2]
                lang_settings = ma_misc.load_json_file(translation_file)[language]["translation"][module]
            except KeyError:
                language = "sr-Latn-RS"
                lang_settings = ma_misc.load_json_file(translation_file)[language]["translation"][module]
        
        return lang_settings

    def uninstall_hp_privacy_settings_app(self):
        self.driver.ssh.send_command('powershell "Remove-AppxPackage -Package AD2F1837.HPPrivacySettings_1.3.10.0_x64__v10z8vjag6ke6"', timeout=30)
        time.sleep(5)
        
    def install_hp_privacy_settings_app(self):
        app_path = "C:\\build\\HPPrivacySettings_1.3.10.0_x64.appxbundle_Windows10_PreinstallKit\\4dd6bf7481694ccbb75d911400291257.appxbundle"      
        if "HPPrivacySettings" in app_path:
            self.driver.ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell Add-AppxPackage -Path {app_path} -ForceApplicationShutdown" /sc once /st 00:00 /f', timeout=60)   
            self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
            time.sleep(10)
            file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.HPPrivacySettings_v10z8vjag6ke6\\LocalCache"'
            file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            max_attempts = 5
            for _ in range(max_attempts):
                if file_exist:
                    break
                time.sleep(10)
                file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            time.sleep(10)
            self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)

    def system_control_cmd(self) :
        result = self.driver.ssh.send_command("powershell 'c:\\Users\\exec\\Desktop\\wmicmd\\wmicmd /cmd=1 /cmdtype=0x4c /size=0'", timeout =10)
        for line in result["stdout"].split("\r\n"):
            if "OutData[Data]: " in line:
                logging.info("OutData[Data]: " + line.split(" ")[1].strip().replace(",", ""))
                return line.split(" ")[1].strip().replace(",", "")

    def swipe_window(self,direction,distance,script_swipe=True):
        el = self.fd["pen_control"].scroll_window_locator()
        self.driver.swipe(anchor_element=el, direction=direction, distance=distance, script_swipe=script_swipe)

    def get_printer_info_from_xml_file(self):
        print_info = {}
        remote_path = "{}\\{}\\LocalState\\RecentDeviceList.xml".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = self.driver.ssh.remote_open(remote_path, "r+")
        data = fh.read().decode("utf-8")
        fh.close()
        root = ET.fromstring(data)
        info_list = ['SerialNumber', 'DisplayName', 'ModelName', 'HostName', 'ProductNumber']
        for device in root.findall('DeviceDataContract'):
            info = {}
            serial_number = None
            for key in info_list:
                elem = device.find(key)
                info[key] = elem.text if elem is not None else None
                if key == 'SerialNumber':
                    serial_number = elem.text if elem is not None else None
            if serial_number:
                print_info[serial_number] = info
        logging.info("Printer Information: {}".format(print_info))
        return print_info
        
    def get_printer_name(self, printer_obj):
        printer_name = printer_obj.get_printer_information()['bonjour name'].split('[')[0].strip()
        printer_name = re.findall(r'\d+', printer_name)[0]
        return printer_name
    
    def get_product_number(self, printer_obj):
        product_number = printer_obj.get_printer_information()['product number']
        return product_number
    
    def launch_module_using_deeplink(self,deep_link):
        command = 'powershell Start-Process "{}"'.format(deep_link)
        self.driver.ssh.send_command(command, timeout=10)

    def kill_msstore_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im WinStore.App.exe', raise_e=False, timeout=10)

    def open_hdr_settings(self):
        self.driver.ssh.send_command('powershell start ms-settings:display-hdr')

    def start_hp_networkcap_exe(self):
        self.driver.ssh.send_command('Start-Service -Name "HP Network HSA Service"', raise_e=False, timeout=10)

    def stop_hp_networkcap_exe(self):
        self.driver.ssh.send_command('Stop-Service -Name "HP Network HSA Service"', raise_e=False, timeout=10)

    def start_hp_apphelpercap_exe(self):
        self.driver.ssh.send_command('Start-Service -Name "HP App Helper HSA Service"', raise_e=False, timeout=10)

    def stop_hp_apphelpercap_exe(self):
        self.driver.ssh.send_command('Stop-Service -Name "HP App Helper HSA Service"', raise_e=False, timeout=10)
    
    def get_machine_type(self):
        machine_type = self.driver.ssh.send_command('(Get-WmiObject -Class Win32_OperatingSystem).OSArchitecture.Split(" ")[0]', timeout = 80)
        return machine_type['stdout']
    
    def get_windows_serial_number(self):
        result = self.driver.ssh.send_command('Get-CimInstance -ClassName Win32_BIOS | Select-Object -Property SerialNumber', timeout = 80)
        lines = result['stdout'].strip().split('\n')
        serial_number = lines[2].strip()
        return serial_number

    def change_system_region_to_india(self):
        self.driver.ssh.send_command("PowerShell Set-WinHomeLocation -GeoID 89", timeout=30, raise_e=False)

    def change_system_region_to_china(self):
        self.driver.ssh.send_command("PowerShell Set-WinHomeLocation -GeoID 45", timeout = 30, raise_e=False )

    def change_system_region_to_united_states(self):
        self.driver.ssh.send_command("PowerShell Set-WinHomeLocation -GeoID 244", timeout = 30, raise_e=False )

    def install_video_apps_from_ms_store_for_disney(self, app, locator, user_name="myhp_monthly@outlook.com", password="hpjs1234"):
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(5)
        self.fd["display_control"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(3)
        if self.fd["display_control"].is_sign_in_present():
            self.fd["display_control"].click_on_sign_in_msstore()
            if self.fd["display_control"].is_continue_button_on_sign_in_page_present():
                self.fd["display_control"].click_microsoft_account_button_on_sign_in_page()
                self.fd["display_control"].click_continue_button_on_sign_in_page()
            time.sleep(5)
            self.fd["display_control"].enter_email_address(user_name)
            time.sleep(15)
            self.fd["display_control"].click_next_button_on_sign_in_page()
            self.fd["display_control"].enter_password(password)
            time.sleep(15)
            self.fd["display_control"].click_next_button_first_time_signin()
            self.fd["display_control"].click_signin_button_on_sign_in_page()
            self.fd["display_control"].verify_next_button_first_time_signin()
            self.fd["display_control"].click_next_button_first_time_signin()
        else:
            time.sleep(10)
            self.fd["display_control"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(5)
        self.fd["display_control"].ms_store_search_box(app)
        time.sleep(5)
        self.fd["display_control"].click_install_app(locator)
        time.sleep(5)
        if self.fd["display_control"].wait_for_object("install_button_to_install_app_from_ms_store"): 
            self.fd["display_control"].install_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("get_button_to_install_app_from_ms_store"):
            self.fd["display_control"].click_get_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_owned_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_owned_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_new_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_new_app_from_ms_store()
        time.sleep(40)
        self.fd["display_control"].click_signout_button_on_sign_in_page()
    
    def kill_msstore_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im WinStore.App.exe', raise_e=False, timeout=10)        
    
    def install_video_apps_from_ms_store(self, app, locator):
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=15)
        time.sleep(5)
        self.fd["display_control"].ms_store_search_box(app)
        time.sleep(5)
        self.fd["display_control"].click_install_app(locator)
        time.sleep(5)
        if self.fd["display_control"].wait_for_object("install_button_to_install_app_from_ms_store"): 
            self.fd["display_control"].install_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("get_button_to_install_app_from_ms_store"):
            self.fd["display_control"].click_get_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_owned_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_owned_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_new_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_new_app_from_ms_store()
        #need some time to install the app after click
        time.sleep(15)
        self.kill_tencent_video_process()
        time.sleep(2)
        self.kill_iqiyi_video_process()
        time.sleep(2)
        self.kill_disney_video_process()
        time.sleep(2)

    def get_system_brightness_value(self):
        result = self.driver.ssh.send_command('powershell (Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightness).CurrentBrightness', timeout = 80)
        lines = result['stdout'].strip().split('\n')
        logging.info("Brightness: {}".format(lines))
        brightness = lines[0].strip()
        return brightness

    def set_system_brightness_value(self):
        brightness = int(self.get_system_brightness_value())
        if brightness==100:
            brightness = 50
        else:
            brightness = brightness + 1
        logging.info("Setting brightness to: {}".format(brightness))
        self.driver.ssh.send_command('(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {})'.format(brightness), timeout = 80)
    
    def open_system_settings_display(self):
        self.driver.ssh.send_command('powershell start ms-settings:display')
        if "Maximize Settings" == self.fd["display_control"].verify_settings_window_maximize():
            self.fd["display_control"].maximize_settings_window()
 
        
    def kill_tencent_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im QQLive.exe', raise_e=False, timeout=10)

    def kill_iqiyi_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im QyClient.exe', raise_e=False, timeout=10)  
        
    def kill_disney_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)

    def disable_windows_camera(self):
        self.driver.ssh.send_command("powershell 'C:\\Users\\exec\\desktop\\disable_camera.ps1' -Verb runAs", timeout=30)
        
    def enable_windows_camera(self):
        self.driver.ssh.send_command("powershell 'C:\\Users\\exec\\desktop\\enable_camera.ps1' -Verb runAs", timeout=30)    

    def open_camera_hdr_settings(self):
        self.driver.ssh.send_command('cmd /c "start ms-settings:camera"', raise_e=False, timeout=20)
        if "Maximize Settings" == self.fd["smart_experience"].verify_settings_window_maximize():
            self.fd["display_control"].maximize_settings_window()

    def kill_tencent_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im QQLive.exe', raise_e=False, timeout=10)  
 
    def kill_iqiyi_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im iQIYI.exe', raise_e=False, timeout=10)  

    def capture_feature_byte(self):
        stack_config_file = r"C:\hp\bin\RStone.ini"
        fh=self.driver.ssh.remote_open(stack_config_file, mode="r+", raise_e=False)
        data = fh.read().decode("utf-8").splitlines()
        fh.close()
        logging.info("RStone.ini file content: " + data[18])
        return data[18]
       
    def kill_poly_camera_lens(self):
        self.driver.ssh.send_command('powershell taskkill /f /im  PolyCameraPro.exe', raise_e=False, timeout=10)

    def windows_setting_page_to_unistall_apps(self, app):
        self.driver.ssh.send_command("start ms-settings:appsfeatures", timeout = 60)
        self.fd["video_control"].click_installedapps_searchbar(app)
        time.sleep(2)
        self.fd["video_control"].verify_threedots_option()
        self.fd["video_control"].click_threedots_option()
        time.sleep(2)
        self.fd["video_control"].verify_uninstall_option()
        self.fd["video_control"].click_uninstall_option()
        if self.fd["video_control"].verify_uninstall_confirmation_option():
            self.fd["video_control"].click_uninstall_confirmation_option()
        else:
            logging.info("Uninstall confirmation option not available")
            self.fd["video_control"].click_uninstall_option()
        time.sleep(70) 
        self.close_windows_settings_panel()

    def install_camera_apps_from_ms_store(self, user_name="myhp_monthly@outlook.com", password="hpjs1234"):
        self.fd["video_control"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(3)
        if self.fd["video_control"].is_sign_in_present():
            self.fd["video_control"].click_on_sign_in_msstore()
            if self.fd["video_control"].is_continue_button_on_sign_in_page_present():
                self.fd["video_control"].click_microsoft_account_button_on_sign_in_page()
                self.fd["video_control"].click_continue_button_on_sign_in_page()
            time.sleep(5)
            self.fd["video_control"].enter_email_address(user_name)
            time.sleep(15)
            self.fd["video_control"].click_next_button_on_sign_in_page()
            self.fd["video_control"].enter_password(password)
            time.sleep(15)
            self.fd["video_control"].click_next_button_first_time_signin()
            self.fd["video_control"].click_signin_button_on_sign_in_page()
            self.fd["video_control"].verify_next_button_first_time_signin()
            self.fd["video_control"].click_next_button_first_time_signin()
        else:
            time.sleep(10)
            self.fd["video_control"].click_on_profile_icon_to_sign_in_msstore()

    def uninstall_msboard_app(self):
        self.driver.ssh.send_command('powershell "Get-AppxPackage Microsoft.Whiteboard | Remove-AppxPackage"')
    
    def enabled_in_logging_data_file(self):
        log_file = w_const.TEST_DATA.HPX_APP_LOG_PATH + "\\Logs\\LoggingData.xml"
        if (fh := self.driver.ssh.remote_open(log_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            if "<Enabled>false</Enabled>" in data:
                data = re.sub("<Enabled>false</Enabled>", "<Enabled>true</Enabled>", data)
            fh = self.driver.ssh.remote_open(log_file, mode="w")
            fh.write(data)
            fh.close()

    def check_hpx_default_stack(self):
        """
        Check and return hpx default stack from LoggingDate.xml file
        """
        log_file = w_const.TEST_DATA.HPX_APP_LOG_PATH + "\\Logs\\LoggingData.xml"
        fh = self.driver.ssh.remote_open(log_file, mode="r+")
        data = fh.read().decode("utf-8")
        fh.close()

        actual_stack = "Pie" if "<ServerStack>Pie</ServerStack>" in data else "Stage" if "<ServerStack>Stage</ServerStack>" in data else "Prod"
        logging.info("The Current HPX Stack Server is {}".format(actual_stack))
        return actual_stack
    
    def add_a_printer(self, printer_obj):
        """
        Add a printer via IP address by clicking Add printer plus icon from Device Card screen
        """
        printer_name = printer_obj.get_printer_information()['model name']
        logging.info("Start to add printer --- Printer Name: {}".format(printer_name))
        self.fd["devicesMFE"].click_add_button()
        self.fd["addprinter"].verify_add_device_panel()
        self.fd["addprinter"].click_choose_printer_button()
        self.fd["addprinter"].verify_progress_bar()
        if self.fd["addprinter"].verify_no_printers_screen(timeout=10, raise_e=False):
            self.fd["addprinter"].click_add_using_ip_address_btn()
        time.sleep(3)
        self.fd["addprinter"].click_input_textbox()
        printer_ip_address = self.search_network_printer(printer_obj)
        self.fd["addprinter"].select_printer(printer_ip_address)
        if self.fd["addprinter"].verify_auto_install_driver_to_print(raise_e=False):
            self.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
            if self.fd["addprinter"].verify_auto_install_driver_done(timeout=5, raise_e=False):
                self.fd["addprinter"].click_continue_btn()
            else:
                self.fd["addprinter"].click_top_exit_setup_btn()
                if self.fd["addprinter"].verify_setup_incomplete_dialog(raise_e=False):
                    self.fd["addprinter"].click_setup_incomplete_dialog_exit_setup_btn()
                    if self.fd["addprinter"].verify_printer_setup_is_incomplete_dialog(raise_e=False):
                        self.fd["addprinter"].click_printer_setup_is_incomplete_dialog_ok_btn()
            self.fd["devicesDetailsMFE"].verify_printer_device_page(printer_name, timeout=30)
            self.fd["devicesDetailsMFE"].click_top_back_btn()
        else:  
            logging.info("Restart App to show printers.")
            self.restart_hpx()
        self.fd["devicesMFE"].scroll_to_printer(printer_name)
        if self.fd["devicesMFE"].verify_windows_dummy_printer(printer_name, timeout=30, raise_e=False):
            logging.info(f"{printer_name} added successfully.")
            process_output = self.driver.ssh.send_command("Get-Process")["stdout"]
            process_names = ["PSADriverApp", "HPPrinterHealthMonitor", "HPAudioControl_19H1"]
            for pname in process_names:
                if pname in process_output:
                    self.driver.ssh.send_command(f'Stop-Process -Name "{pname}"')
        else:
            raise NoPrinterFoundException(f'{printer_name} failed to add.')   

    def search_network_printer(self, printer_obj):
        """
        Search printer in device pick screen
        """
        printer_ip_address = printer_obj.get_printer_information()['ip address']
        # printer_ip_address = printer_obj.p_obj.ipAddress
        # printer_ethernet_ip = ""
        # if printer_obj.p_con.use_cdm:
        #     try:
        #         printer_ethernet_ip = printer_obj.p_con.ethernet_ip_address
        #     except AttributeError:
        #         logging.info(f"Ethernet IP address is unavailable for this printer")
        #     if len(printer_ethernet_ip) != 0:
        #         printer_ip_address = [printer_ip_address, printer_ethernet_ip]

        logging.info(f"Printer IP Address information: {printer_ip_address}")
        if type(printer_ip_address) is str:
            self.fd["addprinter"].search_printer(printer_ip_address)
        else:
            for i in range(len(printer_ip_address)):
                if self.fd["addprinter"].search_printer(printer_ip_address[i], raise_e=False):
                    logging.info(f"Printer found: {printer_ip_address[i]}")
                    printer_ip_address = printer_ip_address[i]
                    break
            else:
                raise NoPrinterFoundException(f"Failed to find printer via wireless and ethernet IP {printer_ip_address}")
        return printer_ip_address

    def initialize_printer(self, printer_config=None):
        sys_config = ma_misc.load_system_config_file()
        if "printer_power_config" in sys_config:
            db_info = sys_config.get("database_info", None)
            p_obj = p_driver_factory.get_printer(sys_config["printer_power_config"], db_info=db_info)
            p_obj.set_mech_mode(mech=False)
            p_obj_info = p_obj.get_printer_information()
            logging.info("Initialize Printer Info:\n {}".format(p_obj_info))
            return p_obj
        elif "oneSimulator" in sys_config:
            pp_info = sys_config["oneSimulator"]
            oneSimulatorServer = pp_info.get("server_ip")
            modelName = printer_config
            isUSB = pp_info.get("isUSB", False)
            p_obj = create_simulator_printer_from_api(oneSimulatorServer, modelName, isUSB)
            return p_obj

    def trigger_printer_offline_status(self, printer_obj):
        self.driver.ssh.send_command("netsh wlan disconnect")
        if "DunePrinterInfo" in str(printer_obj.p_obj):
            printer_obj.pp_module._power_off()
        time.sleep(5)
            
    def restore_printer_online_status(self, printer_obj):
        request = self.driver.session_data["request"]
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        self.driver.connect_to_wifi(host, user, ssid, password)
        if "DunePrinterInfo" in str(printer_obj.p_obj):
                printer_obj.pp_module._power_on()
        time.sleep(5)

    def ms_store_app_update(self, user_name="myhp_rebrand_prod@outlook.com", password="hpjs1234"):
        self.fd["devicesMFE"].click_profile_and_settings_icon_button_lzero_page()
        self.fd["devicesMFE"].click_navigation_bar_settings_card_arrow_lzero_page()
        
        # Use SSH version directly as it's more reliable
        ssh_version = self.fd["display_control"].verify_myhp_app_version().strip()
        app_version = ssh_version.split(".")[:-1]  # Remove last segment (.0)
        app_version = ".".join(app_version)
        
        logging.info(f"App Version (from SSH): '{app_version}'")
        #To close older version of the app during OTA testing
        self.driver.ssh.send_command("Stop-Process -Force -name HP.myHP")
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(15)    
        self.fd["display_control"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(3)
        if self.fd["display_control"].is_sign_in_present():
            self.fd["display_control"].click_on_sign_in_msstore()
            if self.fd["display_control"].is_continue_button_on_sign_in_page_present():
                self.fd["display_control"].click_microsoft_account_button_on_sign_in_page()
                self.fd["display_control"].click_continue_button_on_sign_in_page()
            time.sleep(5)
            self.fd["display_control"].enter_email_address(user_name)
            time.sleep(10)
            self.fd["display_control"].click_next_button_on_sign_in_page()
            self.fd["display_control"].enter_password(password)
            time.sleep(10)
            self.fd["display_control"].click_next_button_first_time_signin()
            self.fd["display_control"].click_signin_button_on_sign_in_page()
            self.fd["display_control"].verify_next_button_first_time_signin()
            self.fd["display_control"].click_next_button_first_time_signin()
        else:
            time.sleep(10)
            self.fd["display_control"].click_on_profile_icon_to_sign_in_msstore()
        self.fd["display_control"].verify_downloads_and_updates_button()
        self.fd["display_control"].click_downloads_and_updates_button()
        time.sleep(5)
        self.fd["display_control"].click_get_updates_button()
        time.sleep(120)  # Waiting for the updates to complete
        self.kill_msstore_process()
        return app_version

    
    def ota_app_after_update(self):                   
        time.sleep(20)
        app_version_before = self.ms_store_app_update()
        self.launch_myHP()  
        time.sleep(20)        
        self.fd["devicesMFE"].click_profile_and_settings_icon_button_lzero_page()
        time.sleep(5)
        self.fd["devicesMFE"].click_navigation_bar_settings_card_arrow_lzero_page()
        time.sleep(2)
        
        # Use SSH version directly as UI version is unreliable
        ssh_version = self.fd["display_control"].verify_myhp_app_version().strip()
        app_version = ssh_version
        
        # Remove trailing .0 from versions if present for comparison (handles format differences)
        app_version_clean = app_version.rstrip(".0") if app_version.endswith(".0") else app_version
        
        # Debug prints to see the versions
        print(f"App Version (from SSH): '{app_version}' (clean: '{app_version_clean}')")
        
        if app_version_before is not None:
            app_version_before_clean = app_version_before.rstrip(".0") if app_version_before.endswith(".0") else app_version_before
            assert app_version_before_clean != app_version_clean, (f"App version is same: App version before ({app_version_before}) - current app version ({app_version})")
        else:
            logging.warning("App version before update was not captured; skipping comparison.")
        time.sleep(3)
        self.fd["devicesMFE"].click_navigation_bar_menu_arrow_lzero_page()
        self.fd["devicesMFE"].click_navigation_bar_close_button_arrow_lzero_page()

    def exit_hp_app_and_msstore(self):
        self.fd["devicesMFE"].click_minimize_app()
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        self.fd["display_control"].click_signout_button_on_sign_in_page()
        time.sleep(5)
        self.fd["devicesMFE"].click_myhp_on_task_bar()
        self.kill_msstore_process()
        self.close_myHP()    

    def kill_calculator_app_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im CalculatorApp.exe', raise_e=False, timeout=10)    

    def maximize_and_verify_device_card(self):
        if "Maximize HP" == self.fd["devicesMFE"].verify_window_maximize():
            self.fd["devicesMFE"].maximize_app()
        # Check if device card is present on L0 page
        if self.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
            logging.info("App launched on L0 page - clicking device card to navigate to L1")
            self.fd["devicesMFE"].click_device_card()
        else:
            logging.info("App launched directly on L1 page or no device card present - moving forward")    

        
    
    def open_winodws_power_sleep_page(self):
        self.driver.ssh.send_command('powershell start ms-settings:powersleep', raise_e=False, timeout=10)
    
    def get_windows_system_name(self):
        result = self.driver.ssh.send_command('powershell hostname', timeout = 20)
        return result['stdout'].strip()

    
    def maximize_and_click_card_lzero_page(self, card_type):
        if "Maximize HP" == self.fd["devicesMFE"].verify_window_maximize():
            self.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        if card_type == "device":
            self.fd["devicesMFE"].verify_device_card_show_up()
            self.fd["devicesMFE"].click_device_card()
        elif card_type == "pen":
            self.swipe_window(direction="down", distance=4)
            self.fd["devicesMFE"].verify_pen_card_show()
            self.fd["devicesMFE"].click_pen_card()
        elif card_type == "dock":
            self.fd["devicesMFE"].verify_dock_station_card_show()
            self.fd["devicesMFE"].click_dock_station_card()
        time.sleep(3)

    def check_and_navigate_to_my_pen_page(self):
        self.swipe_to_top()
        if not self.fd["pen_control"].verify_radial_menu_card():
            logging.info("Radial Menu card is not visible. Check if Pen Card is visible")
            if not self.fd["devicesMFE"].verify_pen_card_show():
                logging.info("Pen card isn't visible. Re-launching app")
                self.close_myHP()
                self.launch_myHP()
                time.sleep(3)
            logging.info("Pen card is visible, clicking pen card")
            self.maximize_and_click_card_lzero_page("pen")

    def check_and_navigate_to_customize_buttons_page(self):
        self.swipe_window(direction="up", distance=50)
        title = self.fd["pen_control"]. get_pen_ltwo_page_title()
        if title == 'Upper barrel button' or title == "Lower barrel button" or title == "Top button - Single press" or title == "Top button - Double press" or title == "Top button - Long press":
                self.fd["pen_control"].click_customize_back_button()
        elif title == "Customize buttons":
            time.sleep(1)                
        else:
            if self.fd["pen_control"].verify_customize_buttons():
                self.fd["pen_control"].click_customize_buttons()
            else:
                self.check_and_navigate_to_my_pen_page()
                self.fd["pen_control"].click_customize_buttons()

    def reset_hp_application(self):
        time.sleep(5)
        self.close_myHP()
        time.sleep(10)
        self.fd["display_control"].my_hp_app_reset("Apps: HP")
        self.fd["display_control"].click_app_settings_tab()
        time.sleep(5)
        if "Maximize Settings" == self.fd["display_control"].verify_settings_window_maximize():
            self.fd["display_control"].maximize_settings_window()
        self.swipe_window(direction="down", distance=7)
        time.sleep(5)
        self.fd["display_control"].click_app_reset_button()
        time.sleep(20)
        self.close_windows_settings_panel()
        time.sleep(20)
        self.launch_myHP()

    def reset_myHP_app_through_command(self, launch_app=False):
        self.driver.ssh.send_command("Get-AppxPackage *myHP* | Reset-AppxPackage", timeout = 60)
        time.sleep(15)
        if launch_app:
            try:
                self.launch_myHP_command()
            except Exception as e:
                logging.info("Failed to launch myHP through command, trying from start menu")
                self.fd["accessibility"].open_app_from_start_menu("HP", open_app=True)

    def navigate_to_pen_control_lone_page_and_click_restore_default_btn(self):
        for i in range(3):
            if self.fd["pen_control"].wait_for_object("customize_buttons") is False:
                self.fd["devicesMFE"].click_back_button_rebranding()
            else:
                self.fd["pen_control"].scroll_to_element("restore_default_button_lone_page")
                self.fd["pen_control"].click_restore_default_button_lone_page()
                self.fd["pen_control"].click_restore_default_continue_button_lone_page()                


    def swipe_to_top(self):
        self.swipe_window(direction="up", distance=80)

    def check_and_navigate_to_my_dock_page(self):
        self.swipe_to_top()
        if not self.fd["dock_station"].verify_dock_station_icon_show_up():
            logging.info(f"Dock station image is not visible. Check if Dock Card is visible")
            if not self.fd["devicesMFE"].verify_dock_station_card_show():
                logging.info(f"Dock Station card isn't visible. Re-launching app")
                self.close_app()
                self.launch_myHP()
                time.sleep(3)
            logging.info("Dock station card is visible, clicking the card")
            self.maximize_and_click_card_lzero_page("dock")
    
    def click_uncheck_allow_hdr_games_video_chkbox_in_setting(self):
        self.driver.send_keys("search_box_in_windows_setting","HDR")
        self.driver.click("hdr_option_in_settings")
        if "Maximize Settings" == self.fd["display_control"].verify_settings_window_maximize():
            self.fd["display_control"].maximize_settings_window()
        #make hdr toggle on if off
        if self.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == '0':
            self.fd["display_control"].click_display_control_hdr_toggle_window_setting()
        if self.driver.get_attribute("battery_option_in_setting_under_hdr_option_in_setting","ExpandCollapse.ExpandCollapseState") == "Collapsed":
            self.driver.click("battery_option_in_setting_under_hdr_option_in_setting")
        if self.fd["display_control"].get_state_hdr_chk_box_in_system_settings() == '1':
            self.fd["display_control"].click_turn_off_hdr_chk_box_in_system_settings()
        
 
    def uninstall_disney_plus_app(self):
        self.driver.ssh.send_command('powershell "Remove-AppxPackage -Package Disney.37853FC22B2CE_2024.3.211.0_neutral__6rarf9sa4v8jt"', timeout=40, raise_e=False)
        time.sleep(15)
    
    def get_windows_system_module_name(self):
        result = self.driver.ssh.send_command('powershell "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty Model"', timeout = 20)
        return result['stdout'].strip()

    def add_capture_logs_file(self):
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        properties_file = ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/capture_logs/properties.json")
        time.sleep(2)
        self.driver.ssh.send_file(properties_file, self.remote_artifact_path + "properties.json")
        time.sleep(2)
        properties_dat_file = ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/capture_logs/properties.json.dat")
        time.sleep(2)
        self.driver.ssh.send_file(properties_dat_file, self.remote_artifact_path + "properties.json.dat")
    

    def copy_rebrand_logs_with_timestamp(self):
        self.driver.ssh.send_command('powershell -NoProfile New-Item -ItemType Directory -Path "$env:USERPROFILE\\Desktop\\rebrand_logs" -Force', timeout=10, raise_e=False)
        time.sleep(2)
        self.driver.ssh.send_command('Copy-Item "C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\LocalState\\log.txt" -Destination "$env:USERPROFILE\\Desktop\\rebrand_logs\\log_$(Get-Date -Format \'yyyyMMdd_HHmmss\').txt"',timeout=10, raise_e=False)

    def reset_app(self):
        self.close_myHP()
        """
        Reset the HP app by removing its data and cache.
        """
        self.driver.ssh.send_command('powershell "Get-AppxPackage *myHP* | Reset-AppxPackage"', timeout=30, raise_e=False)
        time.sleep(60)
        self.launch_myHP()
    
    def consent_managed_registry_key(self, ssh, condition=True):
        re = RegistryUtilities(ssh)
        if condition == True:
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True") 
        elif condition == False:
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "False") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "False")

    def app_managed_registry_key(self, ssh, condition=True):
        re = RegistryUtilities(ssh)
        if condition == True:
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent\\Applications\\HP App", "Managed", "True") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent\\Applications\\HP App", "Managed", "True") 
        elif condition == False:
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent\\Applications\\HP App", "Managed", "False") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent\\Applications\\HP App", "Managed", "False")

    def consent_allow_marketing(self, ssh, condition="Accepted"):
        re = RegistryUtilities(ssh)
        if condition == "Accepted":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        elif condition =="Unknown":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown")
        elif condition == "Rejected":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")

    def consent_allow_product_enhancement(self, ssh, condition="Accepted"):
        re = RegistryUtilities(ssh)
        if condition == "Accepted":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        elif condition == "Unknown":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        elif condition == "Rejected":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected")

    def consent_allow_support(self, ssh, condition="Accepted"):
        re = RegistryUtilities(ssh)
        if condition == "Accepted":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        elif condition == "Unknown":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Unknown") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Unknown")
        elif condition == "Rejected":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")

    def kill_edge_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im msedge.exe', raise_e=False, timeout=10)

    def launch_app_without_fuf(self):
        self.driver.launch_app()

    def get_screenshot_comparison_result (self, method_to_call, *args, **kwargs):
        """
        Calls the provided method and extracts the screenshot comparison result.

        If the method returns a tuple (e.g., when using a screenshot comparison context-manager),
        this function returns the second element of the tuple, which is the image comparison result.
        If the method returns a single value, this function returns None.

        Args:
            method_to_call: The method to invoke (e.g., self.fc.fd["pen_control"].wait_and_verify_customize_buttons)
            *args: Positional arguments for the method
            **kwargs: Keyword arguments for the method

        Returns:
            The screenshot comparison result (True/False), or None if not available.
        """
        result = method_to_call(*args, **kwargs)
        
        # Handle both tuple and single return cases
        return result[1] if isinstance(result, tuple) else None

    def install_DTS_sound_unbind_apps_from_ms_store(self, app, locator):
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(5)
        self.fd["display_control"].ms_store_search_box(app)
        time.sleep(5)
        self.fd["audio"].click_install_app(locator)
        time.sleep(5)
        if self.fd["display_control"].wait_for_object("install_button_to_install_app_from_ms_store"): 
            self.fd["display_control"].install_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("get_button_to_install_app_from_ms_store"):
            self.fd["display_control"].click_get_button_to_install_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_owned_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_owned_app_from_ms_store()
        if self.fd["display_control"].wait_for_object("install_button_to_install_new_app_from_ms_store"):
            self.fd["display_control"].install_button_to_install_new_app_from_ms_store()
        time.sleep(100)
        self.kill_msstore_process()
        time.sleep(2)

    def kill_dts_sound_unbound_app_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im DTSSoundUnbound2.exe', raise_e=False, timeout=10)
     
    def uninstall_dts_sound_unbound_app(self):
        self.driver.ssh.send_command('powershell "Get-AppxPackage DTSInc.DTSSoundUnbound | Remove-AppxPackage"', timeout=40, raise_e=False)
        time.sleep(15)

    def validate_supplies_status_headers_home_page(self, title, icon, type):
        """
        Validate the supplies status headers on the home page.
        """
        self.fd["supplies_status"].verify_printer_status_alert_present()
        if type == "error":
            if self.fd["supplies_status"].verify_printer_status_error_alert_strings(title):
                self.fd["supplies_status"].verify_printer_status_error_alert_icon_home_page(icon)
                return True
            else:
                return False
        elif type == "warning":
            if self.fd["supplies_status"].verify_printer_status_warning_alert_strings(title):
                self.fd["supplies_status"].verify_printer_status_warning_alert_icon_home_page(icon)
                return True
            else:
                return False
        elif type == "info":
            if self.fd["supplies_status"].verify_printer_status_information_alert_strings(title):
                self.fd["supplies_status"].verify_printer_status_information_alert_icon_home_page(icon)
                return True
            else:
                return False

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

    def verify_detailed_body_about_printer_status_alert(self, body):
        """
        Verify the detailed information about the printer status alert.
        """
        if self.fd["supplies_status"].verify_detailed_info_about_printer_status_alert(body):
            logging.info("Detailed information about the printer status alert is verified successfully.")
            return True
        else:
            logging.error("Detailed information about the printer status alert is not verified.")
            return False

    def verify_supplies_status_buttons_after_clicked_alert(self):
        """
        Verify the supply status buttons after clicking the alert.
        """
        self.fd["supplies_status"].verify_printer_information_btn()
        self.fd["supplies_status"].verify_network_information_btn()
        self.fd["supplies_status"].verify_printer_advanced_settings_btn()
        self.fd["supplies_status"].verify_printer_reports_btn()
        self.fd["supplies_status"].verify_print_quality_tools_btn()
    

    def clear_rebrand_logs_on_desktop(self):
        ps_cmd = (
            "powershell -NoProfile -Command "
            "\"$p = Join-Path $env:USERPROFILE 'Desktop\\rebrand_logs'; "
            "if (Test-Path $p) { "
            "Get-ChildItem -Path $p -Force | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue "
            "}\""
        )
        self.driver.ssh.send_command(ps_cmd, timeout=20, raise_e=False)

    def open_system_settings_notifications(self):
        self.driver.ssh.send_command('powershell start ms-settings:notifications')
    
    def open_high_contrast_themes_settings(self):
        self.driver.ssh.send_command("Start-Process ms-settings:easeofaccess-highcontrast")

    def get_system_control_mode(self):
        result=self.driver.ssh.send_command("powershell Get-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power\\User\\PowerSchemes'")

        lines = result['stdout'].strip().split('\n')
        logging.info("System Control Mode: {}".format(result['stdout'].strip()))
        
        # Check if specific GUIDs are present in the output
        output = result['stdout'].strip()
        if "ded574b5-45a0-4f42-8737-46345c09c238" in output:
            return "Best Performance"
        elif "961cc777-2547-4f9d-8174-7d86181b8a7a" in output:
            return "Best Power Efficiency"
        elif "00000000-0000-0000-0000-000000000000" in output:
            return "Balanced"
        else:
            return "Unknown"

    def start_hp_hsaserivce(self):
        self.driver.ssh.send_command('Start-Service -Name "HP System Info HSA Service"', raise_e=False, timeout=10)

    def stop_hp_hsaserivce(self):
        self.driver.ssh.send_command('Stop-Service -Name "HP System Info HSA Service"', raise_e=False, timeout=10)
    
    def restart_app_navigate_to_hp_go(self):
        self.restart_myHP()
        self.maximize_and_verify_device_card()
        time.sleep(2)
        self.fd["hp_go"].scroll_to_element("hp_go_card_on_pcdevice_page")
        self.fd["devices_details_pc_mfe"].click_hp_go_card()
    
    def get_machine_cpu_usage(self):
        result = self.driver.ssh.send_command('(Get-CimInstance -ClassName Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average', raise_e=False, timeout=20)
        return float(result["stdout"].strip())
    
    def get_memory_usage_percentage(self):
        result = self.driver.ssh.send_command('powershell "(Get-Counter \'\\Memory\\% Committed Bytes In Use\').CounterSamples.CookedValue"', raise_e=False, timeout=20)
        return float(result["stdout"].strip())
        
    def get_clipboard_content(self):
        return self.driver.get_clipboard_contents()
        
    def change_remote_tv_language(self, language):
        self.driver.ssh.client.exec_command(f'powershell Set-WinUserLanguageList "{language}" -Force -Wa SilentlyContinue')

    def reopen_hp_app_for_blank_screen(self, terminate_hp_background_apps=False):
        if self.fd["devicesMFE"].verify_profile_and_settings_icon_button_lzero_page()==False:
            logging.info("Re-launching app to get back to home page")
            #Closing app directly with "x" button as PS command doesn't work sometimes when blank screen issue happens
            self.fd["devicesMFE"].click_close_app()
            
            # Try position 0 first, if wrong app launches then try position 1
            try:
                # First try position 0
                self.fd["aic"].click_search_bar_on_windows()
                self.fd["aic"].search_bar_on_windows("Apps: HP", navigate_down=0)
                time.sleep(3)
                # Clicks the top left HP title to dismiss the windows overlay (start/search menu window) after App is launched
                self.fd["device_card"].click_hp_app_window_title()
                
                # Check if correct HP app launched
                if self.fd["devicesMFE"].verify_profile_and_settings_icon_button_lzero_page() is not False:
                    logging.info("HP app launched successfully from first position")
                    return  # Exit if correct app launched
                
                # Wrong app launched, close it and try position 1
                logging.info("Wrong app launched at position 0, trying position 1")
                self.fd["aic"].press_alt_f4_to_close_app()
                time.sleep(1)
                
                if terminate_hp_background_apps == True:
                    self.terminate_conflicting_hp_processes()
                    self.fd["aic"].click_search_bar_on_windows()
                    self.fd["aic"].search_bar_on_windows("Apps: HP") # Relaunch HP via taskbar search box (for blank screen issue)
                    self.fd["css"].verify_bell_icon_show_up()
                    self.fd["device_card"].click_hp_app_window_title()
                else:
                    # Now try position 1
                    self.fd["aic"].click_search_bar_on_windows()
                    self.fd["aic"].search_bar_on_windows("Apps: HP", navigate_down=1)
                    time.sleep(3)
                
            except Exception as e:
                logging.warning(f"Error launching HP app: {e}")


    def add_registry_key_for_battery_manager(self, ssh):
        logging.info("Adding registry key for battery manager")
        ssh.send_command('New-Item -Path "HKLM:\\Software\\HP\\HP App" -Force', raise_e=False)
        result = self.fd["registry_utilities"].add_key("HKEY_LOCAL_MACHINE\\Software\\HP\\HP App", "BatteryEnabled", "true", "String")

    def remove_registry_key_for_battery_manager(self, ssh):
        logging.info("Removing registry key for battery manager")
        result = self.fd["registry_utilities"].delete_key("HKEY_LOCAL_MACHINE\\Software\\HP\\HP App", "BatteryEnabled")

    def verify_and_navigate_battery_page(self):
        self.swipe_to_top()
        if not self.fd["battery"].verify_battery_information_title_ltwo():
            logging.info("Battery manager page is not opened, using navigation method")
            self.restart_myHP()
            time.sleep(2)
            self.maximize_and_verify_device_card()
            time.sleep(3)
            self.swipe_window(direction="down", distance=2)
            self.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            time.sleep(2)
        else:
            logging.info("Battery manager page is already opened")

    def close_windows_explorer_app(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name explorer -Force', raise_e=False, timeout=10)

    def open_windows_terminal(self):
        self.driver.ssh.send_command('powershell Start-Process "C:\\Users\\exec\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe"', raise_e=False, timeout=10)

    def close_windows_terminal(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name WindowsTerminal -Force', raise_e=False, timeout=10)

    def set_windows_contrast_theme_from_settings(self, theme_name):
        self.fd["devicesMFE"].click_minimize_app()
        self.open_high_contrast_themes_settings()
        self.fd["pen_control"].set_contrast_theme_from_settings(theme_name)
        time.sleep(2)
        self.fd["pen_control"].close_settings_window()
        time.sleep(2)
        self.fd["devicesMFE"].click_myhp_on_task_bar()  

    def navigate_to_pen_card_and_get_pen_name(self):
        self.check_and_navigate_to_my_pen_page()
        pen_name = self.fd["pen_control"].get_pen_name_on_lone_page()
        logging.info(f"Connected pen name: {pen_name}")
        return pen_name

    def check_and_navigate_to_display_control_page(self):
        self.swipe_to_top()
        if self.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
            self.maximize_and_verify_device_card()
            if "Restore HP" == self.fd["devicesMFE"].verify_window_maximize():
                self.fd["devicesMFE"].maximize_app()
                time.sleep(2)
        if not self.fd["display_control"].verify_display_control_brightness_slider_ltwo_page():
            logging.info("Brightness Slider is not visible. Check if Display Control Card is visible")
            self.swipe_window(direction="down", distance=6) 
            if not self.fd["devices_details_pc_mfe"].validate_display_control_lone_page():
                logging.info("Display Control card isn't visible. Re-launching app")
                self.close_myHP()
                self.launch_myHP()
                time.sleep(3)
                self.maximize_and_verify_device_card()
                self.swipe_window(direction="down", distance=6) 
            logging.info("Display Control card is visible, clicking Display Control card")
            self.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        if "Restore HP" == self.fd["devicesMFE"].verify_window_maximize():
            self.fd["devicesMFE"].maximize_app()
            time.sleep(2)
        self.fd["display_control"].click_title_bar()

    def close_msstore_app(self):
        self.driver.ssh.send_command('powershell "Get-Process -Name WinStore.App -ErrorAction SilentlyContinue | Stop-Process -Force"', raise_e=False, timeout=10)

    def terminate_conflicting_hp_processes(self):
        """ Prepare HP automation test environment by terminating conflicting HP services """
        self.driver.ssh.send_command('powershell taskkill /f /im HPPrivacySettings.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im PSADriverApp.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im HPPerformanceTuneup.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im HPAudioControl_19H1.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('Stop-Process -Name "HP Desktop Support Utilities" -Force -ErrorAction SilentlyContinue', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im HPOSCheck.exe', raise_e=False, timeout=10)
        self.driver.ssh.send_command('powershell taskkill /f /im HPPrinterHealthMonitor.exe', raise_e=False, timeout=10)
        
    def navigate_back_with_verification(self, flow_name, verify_method, max_retries=3):
        """
        Navigate back using back button with verification and retry logic.
        
        Args:
            flow_name: Name of the flow (e.g., "devices_details_pc_mfe")
            verify_method: Name of the verification method (e.g., "verify_battery_manager_card_lone")
            max_retries: Maximum number of retry attempts (default: 2)
        
        Example:
            self.fc.navigate_back_with_verification("flow_name", "method_name")
        """
        self.fd["devicesMFE"].click_back_button_rebranding()
        for _ in range(max_retries):
            if getattr(self.fd[flow_name], verify_method)():
                break
            else:
                self.fd["devicesMFE"].click_back_button_rebranding()
    
    def get_app_instance_id(self):
        """
        Reads the AsyncStorage.db file from the Windows device over SSH,
        extracts the application-instance-id UUID, and returns it.
        Deletes the temporary copy afterwards.
        """
        src = r"$env:LOCALAPPDATA\Packages\AD2F1837.myHP_v10z8vjag6ke6\LocalState\AsyncStorage.db"
        dst = r"$env:TEMP\AsyncStorage_copy.db"

        copy_cmd = (
            f'powershell -Command "Copy-Item -Path \'{src}\' -Destination \'{dst}\' -Force"'
        )
        result = self.driver.ssh.send_command(copy_cmd, timeout=30)
        if result.get("stderr"):
            raise Exception(f"Copy failed: {result['stderr']}")
        # Base64 read temp copy
        ps_cmd = f'powershell -Command "[Convert]::ToBase64String([IO.File]::ReadAllBytes(\'{dst}\'))"'
        base_64 = self.driver.ssh.send_command(ps_cmd, timeout=60)
        if base_64.get("stderr"):
            raise Exception(f"Read failed: {base_64['stderr']}")
        # Decode and parse UUID
        data = base64.b64decode(base_64["stdout"].strip())
        match = re.search(rb"application-instance-id([0-9a-fA-F-]{36})", data)
        if not match:
            raise Exception("application-instance-id not found inside DB")
        uuid_value = match.group(1).decode()
        # Cleanup temp file
        delete_cmd = f'powershell -Command "Remove-Item -Path \'{dst}\' -Force"'
        self.driver.ssh.send_command(delete_cmd, timeout=10)
        return uuid_value
    
    def get_installed_app_path(self, app_name="HP"):
        """
        Returns the install path of a UWP app over SSH given a partial app name.
        Raises exceptions if the app is not found or the SSH command fails.
        """
        # PowerShell command
        cmd_path = (f'powershell -Command "Get-AppxPackage -Name \'*{app_name}*\' | 'f'Select-Object -ExpandProperty InstallLocation"')
        result_path = self.driver.ssh.send_command(cmd_path, timeout=20)
        if result_path.get("stderr"):
            raise Exception(f"Failed to get app path: {result_path['stderr'].strip()}")
        install_path = result_path.get("stdout", "").strip()
        if not install_path:
            raise Exception(f"App with name containing '{app_name}' not found.")
        return install_path

    def close_hp_app_using_alt_f4(self):
        self.fd["aic"].press_alt_f4_to_close_app()
    
    def close_and_restart_myhp_app(self):
        self.close_myHP()
        self.fd["device_card"].handle_feature_unavailable_popup(timeout=5)
        self.launch_myHP_command()
        self.fd["device_card"].handle_feature_unavailable_popup(timeout=5)
        self.fd["devicesMFE"].maximize_the_hpx_window()
    
    def minimize_all_apps(self):
        logging.info("Minimizing all apps before test")
        time.sleep(0.5)
        self.driver.send_keys("search_bar_on_windows", Keys.META + "d")

            
    

    def set_proxy_on_remote_windows(self, http_proxy, https_proxy=None, bypass_list=None):
        https_proxy = https_proxy or http_proxy

        self.driver.ssh.send_command(
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f',
            timeout=30
        )
        self.driver.ssh.send_command(
            f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyServer /t REG_SZ /d "{http_proxy}" /f',
            timeout=30
        )  
        if bypass_list:
            self.driver.ssh.send_command(
                f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyOverride /t REG_SZ /d "{bypass_list}" /f',
                timeout=30
            )
        whoami = self.driver.ssh.send_command('whoami', timeout=10)
        print("Remote whoami:", whoami)
        reg_query = self.driver.ssh.send_command(
        'reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"', timeout=10)
        print("Registry Internet Settings:", reg_query)
        print("Remote system and WinINET proxy set successfully.")
        return True
    
    def select_device(self, index=0):
        self.restart_app()
        self.maximize_window()
        # if self.fd["hpx_fuf"].verify_continue_update_button_show():
        #     self.fd["hpx_fuf"].click_continue_update_button()
        #     time.sleep(5)
        # if self.fd["hpx_fuf"].verify_continue_update_button_show():
        #     self.fd["hpx_fuf"].click_continue_update_button()
        #     time.sleep(5)
        # if self.fd["hpx_fuf"].verify_cancel_update_button_show():
        #     self.fd["hpx_fuf"].click_cancel_update_button()
        #     time.sleep(5)
        if self.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fd["hpx_fuf"].click_accept_all_button()
        if self.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fd["hpx_fuf"].click_what_is_new_skip_button()
        # self.fd["devicesMFE"].click_device_card_by_index(index)

    def relaunch_and_reload_myhp(self):
        if self.is_app_open():
            logging.info("App is already open, closing it first.")
            self.close_myHP()
        for _ in range(3):
            logging.info("Launching myHP app...")
            self.launch_myHP_command()
            if not self.is_app_open():
                logging.warning("myHP app not launched, retrying...")
                continue
            if self.fd["devicesMFE"].verify_profile_and_settings_icon_button_lzero_page() is not False:
                logging.info("myHP app launched successfully & homepage loaded successfully...")
                self.fd["css"].maximize_hp()
                break
            self.close_myHP()

    def verify_whther_app_is_on_printer_card_page(self):
        if self.fd["devicesMFE"].verify_device_card_show_up() is not False:
            self.fd["supplies_status"].verify_printer_card_present()
        elif self.fd["device_card"].verify_device_details_page():
            self.fd["device_card"].click_pc_devices_back_button()
            self.fd["devicesMFE"].verify_device_card_show_up()
            self.fd["supplies_status"].verify_printer_card_present()
        else:
            self.relaunch_and_reload_myhp()
            assert self.fd["devicesMFE"].verify_device_card_show_up()
            assert self.fd["supplies_status"].verify_printer_card_present()
        logging.info("Application is on printer card page now.")

    def consent_transfer_out_consent_required(self, ssh, condition="True"):
        re = RegistryUtilities(ssh)
        if condition == "True":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True")
        elif condition == "False":
            if re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "False") is False:
                re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "False")
                
    def add_and_switch_to_new_window(self, web_driver=None, window_name="new_window"):
        """Wait for new browser window, add it, and switch to it."""
        web_driver.wait_for_new_window(timeout=20)
        web_driver.add_window(window_name)
        web_driver.switch_window(window_name)
        if web_driver.current_window.title().lower() == window_name.lower():
            logging.info(f"Successfully switched to window '{window_name}' with title '{web_driver.current_window.title().lower()}'")
            return True
        else:
            logging.error(f"Failed to switch to window '{window_name}' with title '{web_driver.current_window.title().lower()}'")
            return False


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************

class NoPrinterFoundException(Exception):
    pass
