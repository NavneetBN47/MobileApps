import logging
import time
import json
import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx.settings import Settings
from MobileApps.libs.flows.windows.hpx.audio import Audio
from MobileApps.libs.flows.windows.hpx.navigation_panel import NavigationPanel
from MobileApps.libs.flows.windows.hpx.support.support_home import SupportHome
from MobileApps.libs.flows.windows.hpx.support.support_device import SupportDevice
from MobileApps.libs.flows.windows.hpx.support.support_va import SupportVA
from MobileApps.libs.flows.windows.hpx.support.support_onedrive import SupportOnedrive
from MobileApps.libs.flows.windows.hpx.support.support_connectivity import SupportConnectivity
from MobileApps.libs.flows.windows.hpx.support.support_account import SupportAccount
from MobileApps.libs.flows.windows.hpx.support.support_rebranding import SupportRebranding
from MobileApps.libs.flows.windows.hpx.devices import Devices
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.windows.hpx.first_use_flow.hp_registration import HPRegistration
from MobileApps.libs.flows.windows.hpx.first_use_flow.dropbox import Dropbox
from MobileApps.libs.flows.windows.hpx.first_use_flow.hp_privacy_setting import HPPrivacySetting
from MobileApps.libs.flows.windows.hpx.first_use_flow.express_vpn import ExpressVPN
from MobileApps.libs.flows.windows.hpx.first_use_flow.mcafee import Mcafee
from MobileApps.libs.flows.windows.hpx.hp_login import HPLogin
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.api_utility import APIUtility
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.first_use_flow.hp_privacy_CN_setting import HPPrivacySettingCN
from MobileApps.libs.flows.windows.hpx.sanity_check import SanityCheck
from MobileApps.libs.flows.windows.hpx.home import Home
from MobileApps.libs.flows.windows.hpx.rgb_keyboard import RGBKeyboard
from MobileApps.libs.flows.windows.hpx.opd import OPD
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.windows.hpx.display_control import DisplayControl
from MobileApps.libs.flows.windows.hpx.video_control import VideoControl
from MobileApps.libs.flows.windows.hpx.pen_control import PenControl
from MobileApps.libs.flows.windows.hpx.smart_experience import SmartExperience
from MobileApps.libs.flows.windows.hpx.hppk import Hppk
from MobileApps.libs.flows.windows.hpx.pc_connect import PcConnect
from MobileApps.libs.flows.windows.hpx.system_control import SystemControl
import re
from MobileApps.libs.flows.windows.hpx.external_mouse import Mouse
from MobileApps.libs.flows.windows.hpx.external_keyboard import Keyboard
from MobileApps.libs.flows.windows.hpx.context_aware import ContextAware
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.touchpad import Touchpad
from MobileApps.libs.flows.windows.hpx.touchpadhpone import TouchpadHPOne
from MobileApps.libs.flows.windows.hpx.battery import Battery
from MobileApps.libs.flows.windows.hpx.screen_distance import ScreenDistance
from MobileApps.libs.flows.windows.hpx.screen_time import ScreenTime
from MobileApps.libs.flows.windows.hpx.energy_consumption import EnergyConsumption
from MobileApps.libs.flows.windows.hpx.gesture import Gesture
from MobileApps.libs.flows.windows.hpx.wifi_sharing import WifiSharing
from MobileApps.libs.flows.windows.hpx.dock_station import DockStation
from MobileApps.libs.flows.windows.hpx.presence_sensing import PresenceSensing
from MobileApps.libs.flows.windows.hpx.terms_of_use import TermsOfUse
from MobileApps.libs.flows.windows.hpx.vision_ai import VisionAI

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"settings": Settings(driver),
                   "navigation_panel": NavigationPanel(driver),
                   "audio": Audio(driver),
                   "devices": Devices(driver),
                   "hp_registration": HPRegistration(driver),
                   "dropbox": Dropbox(driver),
                   "hp_privacy_setting": HPPrivacySetting(driver),
                   "express_vpn": ExpressVPN(driver),
                   "mcafee": Mcafee(driver),
                   "support_home": SupportHome(driver),
                   "support_device": SupportDevice(driver),
                   "support_va": SupportVA(driver),
                   "support_onedrive": SupportOnedrive(driver),
                   "support_connectivity": SupportConnectivity(driver),
                   "support_account": SupportAccount(driver),
                   "devices": Devices(driver),
                   "hpid": HPID(driver),
                   "hp_login": HPLogin(driver),
                   "hp_privacy_setting_cn": HPPrivacySettingCN(driver),
                   "home": Home(driver),
                   "sanity_check": SanityCheck(driver),
                   "rgb_keyboard":RGBKeyboard(driver),
                   "opd": OPD(driver),
                   "video_control": VideoControl(driver),
                   "display_control": DisplayControl(driver),
                   "pen_control": PenControl(driver),
                   "smart_experience": SmartExperience(driver),
                   "hppk": Hppk(driver),
                   "pc_connect": PcConnect(driver),
                   "system_control": SystemControl(driver),
                   "external_mouse": Mouse(driver),
                   "external_keyboard": Keyboard(driver),
                   "context_aware": ContextAware(driver),
                   "touchpad": Touchpad(driver),
                   "touchpadhpone": TouchpadHPOne(driver),
                   "battery": Battery(driver),
                   "screen_distance": ScreenDistance(driver),
                   "screen_time": ScreenTime(driver),
                   "energy_consumption": EnergyConsumption(driver),
                   "gesture": Gesture(driver),
                   "wifi_sharing": WifiSharing(driver),
                   "dock_station": DockStation(driver),
                   "support_rebranding": SupportRebranding(driver),
                   "presence_sensing": PresenceSensing(driver),
                   "terms_of_use": TermsOfUse(driver),
                   "vision_ai": VisionAI(driver)}

    @property
    def flow(self):
        return self.fd

    def launch_app(self):
        self.driver.launch_app()
        if self.fd["hp_privacy_setting"].verify_accept_all_btn_privacy():
            self.fd["hp_privacy_setting"].click_accept_all_btn_privacy()
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()
        if self.fd["dropbox"].verify_skip_button_show():
            self.fd["dropbox"].click_skip_button()   
        if self.fd["navigation_panel"].verify_updated_pop_window_show():
            self.fd["navigation_panel"].click_update_pop_window_agree_button()    

    def close_app(self):
        self.driver.terminate_app()

    def restart_app(self):
        self.driver.restart_app()
        # if self.fd["hp_registration"].verify_continue_button():
        #     self.fd["hp_registration"].click_continue_button()     

    def maximize_window(self):
        self.driver.maximize_window()

    def is_myHP_installed(self):
        result = self.driver.ssh.send_command('powershell "Get-AppxPackage *myHP*"')
        returnbool = "AD2F1837.myHP" in result["stdout"]
        return returnbool

    def uninstall_app(self):
        self.driver.ssh.remove_app("*myHP*", timeout=60)

    def install_app(self, install_path):
        time.sleep(5)
        task_utilities = TaskUtilities(self.driver.ssh)
        task_utilities.restart_fusion_service()
        time.sleep(5)
        self.driver.ssh.install_app(install_path)

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
        returnbool = "HP.myHP" in result["stdout"]
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

    
    def install_audio_standalone(self):
        self.driver.ssh.send_command('powershell " Add-AppxPackage C:\\build\\HPAudioCenter_1.51.339.0_x64.appxbundle_Windows10_PreinstallKit\\c41e3bdae63c47bcbb2511a09e7cecbd.appxbundle"', timeout=90, raise_e=False)

    def install_audio_standalone_app_with_path(self):
        self.driver.ssh.send_command('powershell.exe -ExecutionPolicy Bypass -File "C:\\build\HPAudioControl_19H1_2.44.298.102_Test\\Install.ps1" -Force',timeout=30, raise_e=False)
                
    def uninstall_audio_standalone(self):
        self.driver.ssh.send_command('powershell " Remove-AppxPackage -Package AD2F1837.HPAudioCenter_1.51.339.0_x64__v10z8vjag6ke6"', timeout=40, raise_e=False)


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
    
    def re_install_app_and_skip_fuf_video_control(self, path):
        self.re_install_app_launch_myHP(path)
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
        time.sleep(8)
        self.launch_myHP()
        time.sleep(3)

    def launch_myHP(self):
        self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout = 60)
        if self.fd["hp_privacy_setting"].verify_accept_all_btn_privacy():
            self.fd["hp_privacy_setting"].click_accept_all_btn_privacy()
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button() 
        if self.fd["dropbox"].verify_skip_button_show():
            self.fd["dropbox"].click_skip_button()   
        if self.fd["navigation_panel"].verify_updated_pop_window_show():
            self.fd["navigation_panel"].click_update_pop_window_agree_button() 
        if self.fd["vision_ai"].verify_yes_button_show():
            self.fd["vision_ai"].click_yes_button_on_let_myhp_access_dialog()
            if self.fd["vision_ai"].verify_yes_button_show():
                self.fd["vision_ai"].click_yes_button_on_let_myhp_access_dialog()
        
    def launch_myHP_hotkey(self):
        self.driver.ssh.send_command("Start-Process hpx://support/device")

    def launch_hotkey(self, custom_protocol):
        self.driver.ssh.send_command("Start-Process {}".format(custom_protocol))

    def initial_hpx_support_env(self):
        re = RegistryUtilities(self.driver.ssh)
        self.close_app()
        self.web_password_credential_delete()
        self.launch_app()
        remote_artifact_path = "{}\\{}\\LocalState\\".format(
            w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if self.driver.ssh.check_directory_exist(remote_artifact_path, create=False, raise_e=False):
            self.driver.ssh.remove_file_with_suffix(remote_artifact_path, ".json") 
            logging.info("remove json file in LocalState")
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", "244") 
        re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected")
        re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "False")
        if self.driver.session_data['request'].config.getoption("--stack") in ["production"]:
            re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected")
            re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowAnalytics", "Rejected")       
            self.initial_feature()
        if self.fd["hp_privacy_setting"].verify_accept_button_show():
            self.fd["hp_privacy_setting"].click_accept_all_button()
        # if self.fd["hp_registration"].verify_continue_button():
        #     self.fd["hp_registration"].click_continue_button()          
        self.disable_dark_mode()
            
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

        features = file_content.get("@hp-af/common-consents/termsOfUseAccepted")
        hp_support["@hp-af/common-consents/termsOfUseAccepted"] = features

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

    def initial_simulate_file(self, file_path, testrail_id, env, stack=None, use_system_locale=True):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        system_locale = self.get_winsystemlocale()
        file_content = self.load_simulate_file(file_path)
        hp_support = {}
        if file_content[testrail_id][env].get('@hp-support/deviceInfo') != None:
            device_info = file_content[testrail_id][env]['@hp-support/deviceInfo']
            device_info = json.dumps(device_info)
            hp_support["@hp-support/deviceInfo"] = device_info
        if file_content[testrail_id][env].get('@env/CLIENT_ID') != None:
            hp_support["@env/CLIENT_ID"] = file_content[testrail_id][env].get('@env/CLIENT_ID')
        if file_content[testrail_id][env].get('@env/CLIENT_SECRET') != None:
            hp_support["@env/CLIENT_SECRET"] = file_content[testrail_id][env].get('@env/CLIENT_SECRET')
        if file_content[testrail_id][env].get('@env/CONFIG_ID') != None:
            hp_support["@env/CONFIG_ID"] = file_content[testrail_id][env].get('@env/CONFIG_ID')
        if file_content[testrail_id][env].get('@hp-af/localization/current-locale') != None:
            if use_system_locale:
                hp_support["@hp-af/localization/current-locale"] = system_locale
            else:
                hp_support["@hp-af/localization/current-locale"] = file_content[testrail_id][env].get('@hp-af/localization/current-locale')
        if file_content[testrail_id][env].get('@hp-support/region') != None:
            if use_system_locale:
                hp_support["@hp-support/region"] = system_locale.split('-')[1]
            else:
                hp_support["@hp-support/region"] = file_content[testrail_id][env].get('@hp-support/region')
        
        if file_content[testrail_id][env].get('@hp-af/feature-switch/overrides') != None:
            feature_info = file_content[testrail_id][env]['@hp-af/feature-switch/overrides']
            hp_support["@hp-af/feature-switch/overrides"] = feature_info 
        else: 
            if self.driver.session_data['request'].config.getoption("--test-RN"):
                feature_info = {"supporthome-core" : True}
                hp_support["@hp-af/feature-switch/overrides"] = feature_info         

        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if self.driver.ssh.check_file(remote_path):

            with self.driver.ssh.remote_open(remote_path,'r') as f:
                fc = f.read()         
                file_data=json.loads(fc)
                hp_support.update(file_data)
        fh = self.driver.ssh.remote_open(remote_path, "w+")
        
        logging.info(fh)
        logging.info("after simulate, properties.json=" + str(hp_support))
        logging.info("have supporthome-core:" + str(str(hp_support).find("supporthome-core") > 0))
        logging.info("have SUPPORT_URL section:" + str(str(hp_support).find("https://hpx.stage.portalshell.int.hp.com") > 0))
        json.dump(hp_support, fh)
        
        fh.close()
        if stack in ["production", "production_NA"]:
            self.driver.ssh.send_command('C:/HPXUpdate_PRO/Set_properties_dat/generate-release-hash-file.ps1')

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

    def click_dialog_close_btn(self, web_driver=None):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ['production_NA']:
            self.fd["hpid"].click_popup_close_btn()
        elif stack in ['stage', 'pie', 'production']:
            window_name = "hpx_login"
            time.sleep(3)
            web_driver.wait_for_new_window(timeout=20)
            web_driver.add_window(window_name)
            time.sleep(3)
            web_driver.switch_window(window_name)
            web_driver.close_window(web_driver.current_window)
    
    def verify_sign_in(self, web_driver=None):
        self.fd["navigation_panel"].select_my_hp_account_btn()
        return self.verify_hp_id_sign_in(web_driver)

    def get_analytics_file_size(self):
        result = self.driver.ssh.send_command('Get-Item "C:\\ProgramData\\HP\\SharedServices\\analytics_10.73_store.dat" | select -ExpandProperty Length')
        return int(result["stdout"])

    def is_analytics_file_exist(self):
        result = self.driver.ssh.send_command('Test-Path "C:\\ProgramData\\HP\\SharedServices\\analytics_10.73_store.dat"')
        return result["stdout"]

    def stop_hpsysinfo_fusion_services(self):
        self.driver.ssh.send_command('Stop-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    def start_hpsysinfo_fusion_services(self):
        self.driver.ssh.send_command('Start-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    def stop_hpanalytics_fusion_services(self):
        self.driver.ssh.send_command('Stop-Service -Name HpTouchpointAnalyticsService', raise_e=False, timeout=10)

    def start_hpanalytics_fusion_services(self):
        self.driver.ssh.send_command('Start-Service -Name HpTouchpointAnalyticsService', raise_e=False, timeout=10)           

    def sign_out(self, web_driver=None):
        #low perfomrance issue, will remove it after issue fixed
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

    def sign_in(self, username, password, web_driver=None, user_icon_click=True):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ['NA']:
            #low perfomrance issue, will remove it after issue fixed
            time.sleep(10)
            if user_icon_click:
                self.fd["navigation_panel"].select_my_hp_account_btn()
            time.sleep(2)
            logged_in = self.fd["navigation_panel"].verify_fly_out_sign_in_page()
            if not logged_in:
                self.fd["hpid"].verify_login(username, password)
            else:
                self.fd["navigation_panel"].select_my_hp_account_btn()
            time.sleep(3)
        elif stack in ['stage', 'pie', 'production', 'production_NA']:
            window_name = "hpx_login"
            if user_icon_click:
                self.fd["navigation_panel"].select_my_hp_account_btn()
            web_driver.wait_for_new_window(timeout=20)
            web_driver.add_window(window_name)
            time.sleep(3)
            web_driver.switch_window(window_name)
            time.sleep(3)
            self.hpid = HPID(web_driver, window_name=window_name)
            self.hpid.login(username, password)  
            time.sleep(5)
            web_driver.close_window(web_driver.current_window)

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
        
    def capture_analytics_event(self,module_name):
        result = self.driver.ssh.send_command('powershell \'C:\\PSSWLogCollector\\myhpinternals_x64\\decrypt_analytics_stores.cmd\' -Verb runAs')
        self.remote_artifact_path = 'C:\\PSSWLogCollector\\myhpinternals_x64\\FusionAnalytics\\analytics_10.73_store.txt'
        event = {}
        fo = self.driver.ssh.remote_open(self.remote_artifact_path, 'rb') 
        bytes_str = fo.read().decode('utf-8', 'ignore')
        bytes_str = bytes_str.strip().replace('"events": [', " ").replace("]", "").strip()[1:-1].strip()[:-1]
        result = re.findall(r'\{.*?\}', bytes_str)
        for res in result:
            data = json.loads(res)
            if module_name in str(data['12']):
                for key, value in data.items():
                    if key in ['2', '3', '4', '11', '12']:
                        event[key] = value
        return event
    
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
        if "Maximize myHP" == self.fd["devices"].verify_window_maximize():
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
        self.fd["support_device"].select_country_by_country_name(country_name)   
    
    def click_countrylist(self, country_code, current_locale=None):
        if current_locale is None:
            system_locale = self.get_winsystemlocale().strip()
            country_name = ma_misc.load_json_file("resources/test_data/hpsa/locale/country_list.json")[system_locale][country_code]
        else:
            country_name = ma_misc.load_json_file("resources/test_data/hpsa/locale/country_list.json")[current_locale][country_code]
        self.fd["support_device"].click_country_list()
        return country_name

    #This close method is created to close app from desktop 
    def close_myHP(self):
        if self.is_app_open():
            self.driver.ssh.send_command("Stop-Process -Force -name HP.myHP", timeout = 15)
        
    def kill_chrome_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im chrome.exe', raise_e=False, timeout=10)
    
    def restart_myHP(self):
        time.sleep(10)
        self.close_myHP()
        time.sleep(3)
        self.launch_myHP()
 
    def update_win_language(self,language):
        self.driver.ssh.send_command('Set-WinUserLanguageList '+language+' -Force',timeout=60)
    
    def enable_dark_mode(self):
        self.driver.ssh.send_command('New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force', timeout=90, raise_e=False)

    def disable_dark_mode(self):
        self.driver.ssh.send_command('Remove-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme', timeout=90, raise_e=False)

    def click_pc_support(self):
        self.navigate_to_PC_device()
        self.fd["devices"].click_support_btn()
    
    def navigate_to_PC_device(self):
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()  
        if self.fd["terms_of_use"].verify_accept_button():
            self.fd["terms_of_use"].click_accept_button()
        self.fd["navigation_panel"].navigate_to_pc_device()

    def navigate_to_support(self):
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()  
        if self.fd["terms_of_use"].verify_accept_button():
            self.fd["terms_of_use"].click_accept_button()  
        self.fd["navigation_panel"].navigate_to_support()
        self.skip_hpone_signin_popup()

    def navigate_to_settings(self):
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()  
        if self.fd["terms_of_use"].verify_accept_button():
            self.fd["terms_of_use"].click_accept_button() 
        self.fd["navigation_panel"].navigate_to_settings()

    def navigate_to_welcome(self):
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button() 
        if self.fd["terms_of_use"].verify_accept_button():
            self.fd["terms_of_use"].click_accept_button() 
        self.fd["navigation_panel"].navigate_to_welcome()

    def click_support_control_card(self):
        if self.fd["hp_registration"].verify_skip_button_show():
            self.fd["hp_registration"].click_skip_button()  
        if self.fd["terms_of_use"].verify_accept_button():
            self.fd["terms_of_use"].click_accept_button() 
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
        self.driver.ssh.send_command('powershell start ms-settings:sound', timeout = 30)
    
    def open_system_setting(self):
        self.driver.ssh.send_command('powershell start ms-settings:')
        
    def kill_camera_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im HPEnhancedCamera.exe', raise_e=False, timeout=10)

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
        
    def kill_myhp_process(self):
        if "HP.myHP" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command('powershell taskkill /f /im HP.myHP.exe', raise_e=False, timeout=10)

    def kill_myhp_desktopextesion_process(self):
         if "DesktopExtension" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command('powershell taskkill /f /im desktopextension.exe', raise_e=False, timeout=10)                  

    def kill_cmd_console_process(self):
        tasklist = self.driver.ssh.send_command('powershell tasklist | findstr /i "OpenConsole.exe"', timeout=10)      
        logging.info(str(tasklist['stdout']))
        pid_list=[]
        for i in tasklist['stdout'].split("OpenConsole.exe"):
            if "Console" in i:
                pid_list.append(i.strip().split(" ")[0])
        logging.info(f"PID {pid_list[-1]}")
        self.driver.ssh.send_command('powershell taskkill /f /pid {}'.format(pid_list[-1]), raise_e=False, timeout=10)
    
    def get_cmd_console_process(self):
        tasklist = self.driver.ssh.send_command('powershell tasklist | findstr /i "OpenConsole.exe"', timeout=10)      
        logging.info(str(tasklist['stdout']))
        pid_list=[]
        for i in tasklist['stdout'].split("OpenConsole.exe"):
            if "Console" in i:
                pid_list.append(i.strip().split(" ")[0])
        logging.info(f"PID {pid_list}")
        return len(pid_list)
    
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
    
    def close_accessibility_insights_tool(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name "AccessibilityInsights"', raise_e=False, timeout=10)
    
    def close_windows_settings_panel(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', raise_e=False, timeout=40)
    
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

    def delete_capture_analytics_files(self):
        self.driver.ssh.send_command('Remove-Item -Path "C:\\PSSWLogCollector\\myhpinternals_x64\\FusionAnalytics" -Recurse -Force', raise_e = False, timeout = 20)
        self.driver.ssh.send_command('Get-ChildItem -Path C:\\ProgramData\\HP\\SharedServices\\ -Filter "sent*.dat" | Remove-Item -Force', raise_e = False, timeout = 20)
        time.sleep(5)
        
    def uninstall_hp_privacy_settings_app(self):
        self.driver.ssh.send_command('powershell "Remove-AppxPackage -Package AD2F1837.HPPrivacySettings_1.3.10.0_x64__v10z8vjag6ke6"', raise_e = False, timeout = 60)
        time.sleep(5)
        
    def install_hp_privacy_settings_app(self):
        self.driver.ssh.send_command('powershell "Add-AppxPackage -Path C:\\build\\HPPrivacySettings_1.3.10.0_x64.appxbundle_Windows10_PreinstallKit\\4dd6bf7481694ccbb75d911400291257.appxbundle"', raise_e = False, timeout = 60)
        time.sleep(5)

    def update_region(self, country_code, country_nation):
        re = RegistryUtilities(self.driver.ssh)
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        re.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)

    def system_control_cmd(self) :
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        for line in result["stdout"].split("\r\n"):
            if "OutData[Data]: " in line:
                logging.info("OutData[Data]: " + line.split(" ")[1].strip().replace(",", ""))
                return line.split(" ")[1].strip().replace(",", "")
            
    def kill_msstore_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im WinStore.App.exe', raise_e=False, timeout=10)        
            
    def change_system_region_to_china(self):
       self.driver.ssh.send_command("PowerShell Set-WinHomeLocation -GeoID 45")

    def change_system_region_to_united_states(self):
       self.driver.ssh.send_command("PowerShell Set-WinHomeLocation -GeoID 244")

    def kill_msedge_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im msedge.exe', raise_e=False, timeout=10) 

    def kill_tencent_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im QQLive.exe', raise_e=False, timeout=10)   

    def kill_iqiyi_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im iQIYI.exe', raise_e=False, timeout=10)  
        
    def kill_disney_video_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)

    def kill_calculator_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im CalculatorApp.exe', raise_e=False, timeout=10)    

    def get_app_brightness_value(self):
        result = self.driver.ssh.send_command("Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness")
        for line in result["stdout"].split("\r\n"):
            if "CurrentBrightness" in line:
                logging.info("CurrentBrightness: " + line.split(":")[1].strip())
                return line.split(" ")[1].strip()
            
    def install_video_apps_from_ms_store(self, app, locator):
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=15)
        time.sleep(5)
        self.fd["home"].ms_store_search_box(app)
        time.sleep(5)
        self.fd["home"].click_install_app(locator)
        time.sleep(5)
        if self.fd["home"].wait_for_object("install_button_to_install_app_from_ms_store"): 
            self.fd["home"].install_button_to_install_app_from_ms_store()
        if self.fd["home"].wait_for_object("get_button_to_install_app_from_ms_store"):
            self.fd["home"].click_get_button_to_install_app_from_ms_store()
        #need some time to install the app after click
        time.sleep(15)
        self.kill_tencent_video_process()
        time.sleep(2)
        self.kill_iqiyi_video_process()
        time.sleep(2)
        self.kill_disney_video_process()
        time.sleep(2)
 
    def uninstall_videos_app_from_ms_store(self, app):
        self.fd["home"].click_search_bar_on_windows()
        time.sleep(3)
        self.fd["home"].search_bar_on_windows_uninstall(app)
        self.fd["home"].verify_uninstall_app_button()
        self.fd["home"].click_uninstall_app_button()
        time.sleep(5)
        self.fd["home"].verify_uninstall_app_pop_up()
        self.fd["home"].click_uninstall_app_pop_up()
        time.sleep(3)
        self.fd["home"].click_back_to_home_from_search_menu()

    def reset_hp_application(self):
        time.sleep(5)
        self.close_myHP()
        time.sleep(10)
        self.fd["home"].my_hp_app_reset("myHP")
        self.fd["home"].click_app_settings_tab()
        time.sleep(5)
        if "Maximize Settings" == self.fd["home"].verify_settings_window_maximize():
            self.fd["home"].maximize_settings_window()
        self.swipe_window(direction="down", distance=7)
        time.sleep(5)
        self.fd["home"].click_app_reset_button()
        time.sleep(5)
        self.close_windows_settings_panel()
        time.sleep(10)
        self.launch_myHP()
        time.sleep(10)
        self.close_myHP()
        time.sleep(10)
        self.launch_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fd["devices"].verify_window_maximize():
            self.fd["devices"].maximize_app()
    
    def close_windows_camera_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im WindowsCamera.exe', raise_e=False, timeout=10)

    def swipe_window(self,direction,distance,script_swipe=True):
        el = self.fd["home"].scroll_window_locator()
        self.driver.swipe(anchor_element=el, direction=direction, distance=distance, script_swipe=script_swipe)
    
    def launch_myHP_for_mat(self):
        self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6", timeout = 60)  
        if self.fd["hp_privacy_setting"].verify_accept_all_btn_privacy():
            self.fd["hp_privacy_setting"].click_accept_all_btn_privacy()

    def disable_camera_service(self):
        self.driver.ssh.send_command("Get-PnpDevice | Where-Object {$_.FriendlyName -like '*Camera*'} | Disable-PnpDevice -Confirm:$false")

    def enable_camera_service(self):
        self.driver.ssh.send_command("Get-PnpDevice | Where-Object {$_.FriendlyName -like '*Camera*'} | Enable-PnpDevice -Confirm:$false")
        
    def launch_myHP_to_audio_control_page(self):
        self.driver.ssh.send_command("Start-Process hpx://pcaudio", timeout = 40)
        time.sleep(25)

    def reset_myhp_app(self):
        self.driver.ssh.send_command("Get-AppxPackage *myHP* | Reset-AppxPackage", timeout = 60)
        time.sleep(10)
        self.launch_myHP()

    def close_calculator_app(self):
        self.driver.ssh.send_command('Stop-Process -Name "CalculatorApp" -Force', timeout = 20)

    def close_standalone_app(self):
        self.driver.ssh.send_command('Get-Process -Name "HPAudioCenter" | Stop-Process -Force', timeout = 20)

    def ms_store_app_update(self, user_name="myhp_rebrand_stg@outlook.com", password="hpjs1234"):
        self.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"
        self.fd["settings"].click_about_tab()
        app_version = self.fd["settings"].get_version_about().strip()
        ssh_version = self.fd["home"].verify_myhp_app_version().strip()
        app_version = app_version.replace("Version","").strip()
        logging.info(f"App Version: '{app_version}'")
        logging.info(f"SSH Version: '{ssh_version}'")
        assert app_version == ssh_version, f"App version mismatch: App version ({app_version}) != SSH version ({ssh_version})"
        self.close_myHP()
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(15)    
        self.fd["home"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(3)
        if self.fd["home"].is_sign_in_present():
            self.fd["home"].click_on_sign_in_msstore()
            if self.fd["home"].is_continue_button_on_sign_in_page_present():
                self.fd["home"].click_microsoft_account_button_on_sign_in_page()
                self.fd["home"].click_continue_button_on_sign_in_page()
            time.sleep(5)
            self.fd["home"].enter_email_address(user_name)
            time.sleep(10)
            self.fd["home"].click_next_button_on_sign_in_page()
            self.fd["home"].enter_password(password)
            time.sleep(10)
            self.fd["home"].click_next_button_first_time_signin()
            self.fd["home"].click_signin_button_on_sign_in_page()
            self.fd["home"].verify_next_button_first_time_signin()
            self.fd["home"].click_next_button_first_time_signin()
        else:
            time.sleep(10)
            self.fd["home"].click_on_profile_icon_to_sign_in_msstore()
        self.fd["home"].verify_downloads_and_updates_button()
        self.fd["home"].click_downloads_and_updates_button()
        time.sleep(5)
        self.fd["home"].click_get_updates_button()
        time.sleep(120)  # Waiting for the updates to complete
        self.kill_msstore_process()
        return app_version

    def ota_app_after_update(self):
        app_version_before=self.ms_store_app_update()
        time.sleep(20)
        self.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"
        self.fd["settings"].click_about_tab()
        app_version = self.fd["settings"].get_version_about()
        app_version = app_version.replace("Version", "").strip()
        print(f"Extracted App Version: {app_version}")
        ssh_version = self.fd["home"].verify_myhp_app_version().strip()
        # Debug prints to see the versions
        print(f"App Version: {app_version}")
        print(f"SSH Version: {ssh_version}")
        assert app_version == ssh_version, f"App version mismatch: App version ({app_version}) != SSH version ({ssh_version})"
        assert app_version_before!=app_version, f"App version is same: App version before ({app_version_before}) - current app version  ({app_version})"
        time.sleep(3)

    def exit_hp_app_and_msstore(self):
        self.fd["devices"].minimize_app()
        time.sleep(10)
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(8)
        self.fd["home"].click_signout_button_on_sign_in_page()
        time.sleep(5)
        self.fd["audio"].click_myhp_on_task_bar()
        self.kill_msstore_process()
        self.uninstall_app()
    
    def open_notepad(self):
        self.driver.ssh.send_command('powershell notepad', raise_e=False, timeout=10)

    def close_notepad(self):
        self.driver.ssh.send_command('powershell taskkill /f /im notepad.exe', raise_e=False, timeout=10)

    def get_hp_hardware_id(self):
        all_hardware_id = self.driver.ssh.send_command('Get-WmiObject win32_PnPSignedDriver | where description -like "*HP Application*" | select HardWareID')["stdout"]
        return all_hardware_id

    def myhp_app_setting_page(self):
        self.driver.ssh.send_command("start ms-settings:appsfeatures", timeout = 60)
        self.fd["home"].click_installedapps_searchbar("myHP")
        time.sleep(2)
        self.fd["home"].verify_threedots_option()
        self.fd["home"].click_threedots_option()
        time.sleep(2)
        self.fd["home"].verify_advanced_option()
        self.fd["home"].click_advanced_option()

    
    def open_app_launch_window(self,install_build_version):
        stack = self.driver.session_data['request'].config.getoption("--stack")
        if stack in ['pie']:
            print("Pie stack")
            self.driver.ssh.send_command('powershell C:\\Users\\exec\\Desktop\\'+install_build_version+'_INTEGRATION_TRACK\\HP.HPX_'+install_build_version+'_Test\\HP.HPX_'+install_build_version+'_x64.msixbundle')
        else:
            logging.info("production stack")
            self.driver.ssh.send_command('powershell C:\\Users\\exec\\Desktop\\'+install_build_version+'_PRODUCTION_TRACK\\HP.HPX_'+install_build_version+'_Test\\HP.HPX_'+install_build_version+'_x64.msixbundle')
    
    def close_app_launch_window(self):
        self.fd["home"].click_close()
    
    def open_system_settings_display(self):
        self.driver.ssh.send_command('powershell start ms-settings:display')

    def install_video_apps_from_ms_store_for_disney(self, app, locator, user_name="myhp_monthly@outlook.com", password="hpjs1234"):
        self.driver.ssh.send_command('powershell Start-Process "ms-windows-store:"', timeout=10)
        time.sleep(5)
        self.fd["home"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(3)
        if self.fd["home"].is_sign_in_present():
            self.fd["home"].click_on_sign_in_msstore()
            if self.fd["home"].is_continue_button_on_sign_in_page_present():
                self.fd["home"].click_microsoft_account_button_on_sign_in_page()
                self.fd["home"].click_continue_button_on_sign_in_page()
            time.sleep(5)
            self.fd["home"].enter_email_address(user_name)
            time.sleep(15)
            self.fd["home"].click_next_button_on_sign_in_page()
            self.fd["home"].enter_password(password)
            time.sleep(15)
            self.fd["home"].click_next_button_first_time_signin()
            self.fd["home"].click_signin_button_on_sign_in_page()
            self.fd["home"].verify_next_button_first_time_signin()
            self.fd["home"].click_next_button_first_time_signin()
        else:
            time.sleep(10)
            self.fd["home"].click_on_profile_icon_to_sign_in_msstore()
        time.sleep(5)
        self.fd["home"].ms_store_search_box(app)
        time.sleep(5)
        self.fd["home"].click_install_app(locator)
        time.sleep(5)
        if self.fd["home"].wait_for_object("install_button_to_install_app_from_ms_store"): 
            self.fd["home"].install_button_to_install_app_from_ms_store()
        if self.fd["home"].wait_for_object("get_button_to_install_app_from_ms_store"):
            self.fd["home"].click_get_button_to_install_app_from_ms_store()
        time.sleep(40)
        self.fd["home"].click_signout_button_on_sign_in_page()
    
    def close_edge_browser(self):
        self.driver.ssh.send_command('powershell taskkill /f /im msedge.exe', raise_e=False, timeout=10)

    def open_power_sleep(self):
        self.driver.ssh.send_command('powershell start ms-settings:powersleep')

    def insert_usb(self):
        self.driver.ssh.send_command('powershell python insert_usb.py', timeout = 120)
        time.sleep(20)

    def remove_usb(self):
        self.driver.ssh.send_command('powershell python remove_usb.py', timeout = 120)
        time.sleep(30)

    def press_mute_button(self):
        self.driver.ssh.send_command('powershell python press_mutebutton.py', timeout = 120)
        time.sleep(20)
    
    def get_current_time(self):
        return self.driver.ssh.send_command('powershell Get-Date -DisplayHint Time')

    def launch_module_using_deeplink(self,deep_link):
        command = 'powershell Start-Process "{}"'.format(deep_link)
        self.driver.ssh.send_command(command, timeout=10)

    def install_audio_standalone_24h2(self):
        self.driver.ssh.send_command('schtasks /create /tn "InstallAppNow" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -Command Add-AppxPackage C:\\build\\HPAudioCenter_1.51.339.0_x64.appxbundle_Windows10_PreinstallKit\\c41e3bdae63c47bcbb2511a09e7cecbd.appxbundle" /sc once /st 00:00 /f', timeout=90, raise_e=False)
        self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"')
        self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f')

    def open_color_filter_setting(self):
        self.driver.ssh.send_command('powershell start ms-settings:easeofaccess-colorfilter')

    def open_hdr_setting(self):
        self.driver.ssh.send_command('powershell start ms-settings:display-hdr')
    
    def verify_settings_page_side_panel(self):
        self.fd["settings"].verify_settings_title()
        self.fd["settings"].verify_manage_privacy_preferences()
        self.fd["settings"].verify_privacy_statement_link()
        self.fd["settings"].verify_about_title()
        self.fd["settings"].verify_version()
        self.fd["settings"].verify_about_userLicenceAgreement()
        self.fd["settings"].verify_terms_of_use()