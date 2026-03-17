from MobileApps.libs.flows.common.gotham.home import Home
from MobileApps.libs.flows.common.gotham.feedback import Feedback
from MobileApps.libs.flows.common.gotham.about import About
from MobileApps.libs.flows.web.smart.smart_welcome import SmartWelcome
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.value_prop import MobileValueProp
from MobileApps.libs.flows.web.smart.privacy_preferences import PrivacyPreferences
from MobileApps.libs.flows.web.stratus_utility.stratus_utility import StratusUtility
from MobileApps.libs.flows.windows.gotham.gotham_utility import GothamUtility
from MobileApps.libs.flows.common.gotham.account import Account
from MobileApps.libs.flows.common.gotham.privacy_settings import PrivacySettings
from MobileApps.libs.flows.web.hp_connect.hp_connect import WinSmartDashboard
from MobileApps.libs.flows.common.gotham.printers import Printers
from MobileApps.libs.flows.common.gotham.scan import Scan
from MobileApps.libs.flows.common.gotham.printer_settings import PrinterSettings
from MobileApps.libs.flows.common.gotham.print import Print
from MobileApps.libs.flows.common.gotham.pepto import Pepto
from MobileApps.libs.flows.common.gotham.personalize_tiles import PersonalizeTiles
from MobileApps.libs.flows.common.gotham.activity_center import ActivityCenter
from MobileApps.libs.flows.common.gotham.diagnose_fix import DiagnoseFix
from MobileApps.libs.flows.common.gotham.printer_status import PrinterStatus
from MobileApps.libs.flows.common.gotham.cloud_scan import CloudScan
from MobileApps.libs.flows.common.gotham.moobe import Moobe
from MobileApps.libs.flows.common.gotham.system_preferences import SystemPreferences
from MobileApps.libs.flows.common.gotham.pin_hp_smart_to_start import PinHPSmartToStart
from MobileApps.libs.flows.web.smart.dedicated_supplies_page import DedicatedSuppliesPage
from MobileApps.libs.flows.web.shortcuts.shortcuts_create_edit import MobileShortcutsCreateEdit
from MobileApps.libs.flows.web.softfax.softfax_landing import SoftfaxLanding
from MobileApps.libs.flows.web.softfax.softfax_welcome import MobileSoftfaxWelcome
from MobileApps.libs.flows.web.softfax.softfax_offer import SoftfaxOffer
from MobileApps.libs.flows.web.smart.advanced_settings_page import AdvancedSettingsPage
from MobileApps.libs.flows.web.softfax.compose_fax import ComposeFax
from MobileApps.libs.flows.web.help_support.help_support import HelpSupport
from MobileApps.libs.flows.web.cec.custom_engagement_center import CustomEngagementCenter
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from SAF.misc import saf_misc
from SAF.misc import windows_utils
from MobileApps.libs.ma_misc import ma_misc
import pytest
import re
import time
import logging

class FlowContainer(object):
    def __init__(self, driver, web_driver):
        self.driver = driver
        self.web_driver = web_driver
        self.window_name = "web_login"
        self.fd = {
            "home": Home(driver),
            "welcome_web": SmartWelcome(driver),
            "privacy_preference": PrivacyPreferences(driver),
            "hpid": HPID(driver),
            "ows_value_prop": MobileValueProp(driver),
            "gotham_utility": GothamUtility(driver),
            "feedback": Feedback(driver),
            "about": About(driver),
            "account": Account(driver),
            "privacy_settings": PrivacySettings(driver),
            "smart_dashboard": WinSmartDashboard(driver),
            "printers": Printers(driver),
            "scan": Scan(driver),
            "shortcuts": MobileShortcutsCreateEdit(driver),
            "printer_settings": PrinterSettings(driver),
            "print": Print(driver),
            "dedicated_supplies_page": DedicatedSuppliesPage(driver),
            "pepto": Pepto(driver),
            "softfax_landing": SoftfaxLanding(driver),
            "softfax_welcome": MobileSoftfaxWelcome(driver),
            "cec": CustomEngagementCenter(driver),
            "ews": AdvancedSettingsPage(driver),
            "help_support": HelpSupport(driver),
            "activity_center": ActivityCenter(driver),
            "softfax_home": ComposeFax(driver),
            "diagnose_fix": DiagnoseFix(driver),
            "printer_status": PrinterStatus(driver),
            "softfax_offer": SoftfaxOffer(driver),
            "stratus_utility": StratusUtility(driver),
            "system_preferences": SystemPreferences(driver),
            "personalize_tiles": PersonalizeTiles(driver),
            "cloud_scan": CloudScan(driver),
            "pin_to_start": PinHPSmartToStart(driver),
            "moobe": Moobe(driver)
        }
        self.count = 0
        self.stack = self.driver.session_data["request"].config.getoption("--stack")

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************    
    def get_activity_parameter(self):
        if pytest.app_info != "DESKTOP":
            launch_activity = close_activity = None
        else:
            launch_activity = eval("w_const.LAUNCH_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
            close_activity = eval("w_const.CLOSE_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        return launch_activity, close_activity
    
    def go_home(self, username="", password="", create_account=False, skip_choose_printer_dialog=True):
        if self.fd["welcome_web"].verify_welcome_screen(raise_e=False) is not False:
            self.driver.performance.time_stamp("t1")
            self.nav_welcome(username=username, password=password, create_account=create_account, skip_choose_printer_dialog=skip_choose_printer_dialog)
        elif self.fd["home"].verify_home_screen(raise_e=False) is not False:
            if skip_choose_printer_dialog:
                self.skip_choose_a_printer_dialog()
            return True
        else:
            # Reset the app here. Either install/uninstall or clear the cache and restart.
            # Start from welcome page
            self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
            self.driver.ssh.send_command(self.driver.session_data["installer_path"] + "\\Install.ps1 -Force", timeout=60)
            launch_activity = self.get_activity_parameter()[0]
            self.driver.launch_app(launch_activity)
            self.count += 1
            if self.count > 2:
                raise CannotGoHomeException("Could not go to home screen")
            return self.go_home(username=username, password=password, create_account=create_account, skip_choose_printer_dialog=skip_choose_printer_dialog)

    def set_up_a_new_printer_flow(self):
        self.fd["welcome_web"].verify_welcome_screen()
        self.fd["welcome_web"].click_accept_all_btn(change_check={"wait_obj": "accept_all_btn", "invisible": True, "timeout": 10})
        self.fd["ows_value_prop"].verify_windows_ows_value_prop_screen()
        self.fd["ows_value_prop"].select_value_prop_buttons(index=0)
        
    def change_stack_server(self, stack, restart=True):
        """
        Chnage stack server
        """
        logging.info("Start to change HP Smart Stack Server to {}...".format(stack.capitalize()))
        if pytest.app_info == "DESKTOP":
            pytest.default_info = pytest.set_info
        else:
            pytest.default_info = pytest.app_info
        
        app_name = eval("w_const.PACKAGE_NAME." + pytest.default_info)

        if stack == "production":
            actual_stack = "Prod"
        else:
            actual_stack = stack.capitalize()
        stack_config_file = r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name)
        if (fh := self.driver.ssh.remote_open(stack_config_file, mode="r+", raise_e=False)) is not False:
            data = fh.read().decode("utf-8")
            fh.close()
            # current_stack = "Pie" if "<ServerStack>Pie</ServerStack>" in data else "Stage"
            current_stack = "Pie" if "<ServerStack>Pie</ServerStack>" in data else "Stage" if "<ServerStack>Stage</ServerStack>" in data else "Prod"
            logging.info("The Current HP Smart Stack Server is {}".format(current_stack))
            if actual_stack == current_stack:
                #Already on the right stack and restart App to make sure login flow on the external browser
                return True
            data = re.sub(r"(?<=<ServerStack>).*?(?=</ServerStack>)", actual_stack, data)
            fh = self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="w")
            fh.write(data)
            fh.close()

        else:
            with open(ma_misc.get_abs_path(w_const.TEST_DATA.LOGGINGDATA_XML_PATH), "r") as fh:
                logging_data = fh.read()
                logging_data = logging_data.format(actual_stack)
                rfh = self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="w+")
                current_stack = "Pie" if "<ServerStack>Pie</ServerStack>" in rfh  else "Stage" if "<ServerStack>Stage</ServerStack>" in rfh else "Prod"
                logging.info("The Current HP Smart Stack Server is {}".format(current_stack))
                rfh.write(logging_data)
                rfh.close()   
        time.sleep(1)
        if restart:
            #Relaunch app after changing the stack
            self.restart_hp_smart()
            
    def disable_printer_driver_auto_install(self):
        """
        Disable printer driver auto install with below method:
        If you do not want the driver to be installed (during OOBE or PostOOBE when you pick a device from DevicePicker) please add this line to your Logging xml in the <Misc> section.
        <CustomFeatures>DoNotAutoInstallPrinterDriver</CustomFeatures>
        """
        if pytest.app_info == "DESKTOP":
            pytest.default_info = pytest.set_info
        else:
            pytest.default_info = pytest.app_info
        app_name = eval("w_const.PACKAGE_NAME." + pytest.default_info)

        add_content = "    <CustomFeatures>DoNotAutoInstallPrinterDriver</CustomFeatures>\n"
        logging_data_xml_file = r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name)
        fh = self.driver.ssh.remote_open(logging_data_xml_file, mode="r+")
        data = fh.read().decode("utf-8")
        fh.close()

        pos = data.find("  </Misc>")
        new_content = data[:pos] + add_content + data[pos:]
        
        fh = self.driver.ssh.remote_open(logging_data_xml_file, mode="w")
        fh.write(new_content)
        fh.close()
        #Relaunch app after changing the LoggingData.xml file
        time.sleep(1)
        self.restart_hp_smart()

    def restart_hp_smart(self):
        """
        restart hp smart
        """
        logging.info("Start to restart HP Smart...")
        launch_activity, close_activity = self.get_activity_parameter() 
        self.driver.restart_app(launch_activity, close_activity)
        if self.fd["welcome_web"].verify_welcome_screen(raise_e=False) or self.fd["home"].verify_home_screen(raise_e=False):
            time.sleep(3)
            if not self.fd["gotham_utility"].verify_window_visual_state_maximized():
                self.fd["gotham_utility"].click_maximize()
    
    def reset_hp_smart(self):
        """
        Clear app logs in LocalState folder to reset HP Smart.
        """
        logging.info("Start to Reset HP Smart...")
        
        launch_activity, close_activity = self.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        folder_name = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH
        if windows_utils.check_path_exist(self.driver.ssh, folder_name) is True:
            self.driver.ssh.send_command("Get-ChildItem " + folder_name + " | Remove-Item -Recurse -Force", timeout=20, raise_e=False)
        self.driver.launch_app(launch_activity)
        self.fd["welcome_web"].verify_welcome_screen(raise_e=False)
        if not self.fd["gotham_utility"].verify_window_visual_state_maximized():
            self.fd["gotham_utility"].click_maximize()

    def web_password_credential_delete(self):
        cre_sid = 'S-1-15-2-744533573-2444454674-265863901-3215465728-4115286053-1341080355-789689510'
        cre_resource = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Resource"')
        cre_identity = self.driver.ssh.send_command('VaultCmd /listcreds:"Web Credentials" /all | Select-String -Pattern "Identity"')
        cre_resource_list = cre_resource['stdout'].strip().replace('\r\n', '').split('Resource: ')
        cre_identity_list = cre_identity['stdout'].strip().replace('\r\n', '').split('Identity: ')
        web_cre_num = len(cre_resource_list)     
        for i in range(0, web_cre_num):
            self.driver.ssh.send_command('vaultcmd /deletecreds:"Web Credentials" /credtype:"Windows Web Password Credential" /identity:"{0}" /resource:"{1}" /sid:{2}'.format(cre_identity_list[i], cre_resource_list[i], cre_sid))

    def check_gotham_log(self, check_string):
        """
        Check expected string shows in HP Smart log
        """
        logging.info("Start to check string '{}' in HP Smart log file...".format(check_string))
        with self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH) as f:
            data = f.read().decode("utf-8")
        if re.search(check_string, data):
            logging.info("'{}' are found in HP Smart log successfully!".format(check_string))
            return True
        else:
            raise NoSuchElementException("Fail to found '{}' in HP Smart log".format(check_string))

    def check_consent_appinstanceid_log(self):
        """
        Check "initialUrl:" in the logs and the URL contains the correct "consent=" and "appInstanceId=" in the Gotham log
        """
        check_string = 'initialUrl:.*consent=.*appInstanceId=.*'
        self.check_gotham_log(check_string)

    def get_installed_hp_smart_version(self):
        """
        Get the Installed HP Smart version
        """
        info = self.driver.ssh.send_command('get-appxpackage -name {}'.format(w_const.PROCESS_NAME.GOTHAM))
        app_version = info['stdout'].split("\r\n")[6].split(":")[1].strip()[:10]
        return app_version

    def nav_welcome(self, username="", password="", create_account=False, skip_choose_printer_dialog=True):
        self.fd["welcome_web"].click_accept_all_btn(change_check={"wait_obj": "accept_all_btn", "invisible": True, "timeout": 10})
        self.driver.performance.time_stamp("t3")
        # If there's an signed in account, after clicking accept all in welcome page,
        # it'll directly land on home page.
        if self.fd["ows_value_prop"].verify_windows_ows_value_prop_screen(raise_e=False) is not False:
            self.driver.performance.time_stamp("t4")
            if username != "" and password != "":
                self.driver.performance.time_stamp("t5")
                self.fd["ows_value_prop"].select_native_value_prop_buttons(index=1)
                self.handle_web_login(username=username, password=password)
            elif create_account:
                self.fd["ows_value_prop"].select_native_value_prop_buttons(index=1)
                self.handle_web_login(create_account=create_account, from_sign_in=True)
            else:
                self.fd["ows_value_prop"].select_native_value_prop_buttons(index=3)

        self.fd["home"].verify_home_screen(timeout=30)
        self.driver.performance.stop_timer("hpid_login")
        self.driver.performance.time_stamp("t10")

        if skip_choose_printer_dialog:
            self.skip_choose_a_printer_dialog()

        return True

    def skip_choose_a_printer_dialog(self):
        if self.fd["home"].verify_skip_btn(raise_e=False, timeout=15) is not False:
            self.fd["home"].select_skip_btn()

    def verify_hp_id_sign_in_up_page(self, timeout=10, is_sign_up=False):
        if self.fd["hpid"].verify_hpid_popup_window(raise_e=False):
            if not is_sign_up:
                return self.fd["hpid"].verify_hp_id_sign_in(timeout=timeout)
            else:
                return self.fd["hpid"].verify_hp_id_sign_up(timeout=timeout)
        else:
            time.sleep(3)
            self.web_driver.add_window(self.window_name)
            time.sleep(3)
            try:
                self.web_driver.switch_window(self.window_name)
                self.web_driver.set_size("max")
                self.hpid = HPID(self.web_driver, window_name=self.window_name)
                if not is_sign_up:
                    return self.hpid.verify_hp_id_sign_in(timeout=timeout)
                else:
                    return self.hpid.verify_hp_id_sign_up(timeout=timeout)
            except KeyError:
                return False

    def close_hp_id_sign_in_up_page(self):
        """
        Close Sign in / Sign up page from app internal or web page
        """
        if not self.fd["hpid"].verify_hpid_popup_window(raise_e=False):
            self.web_driver.close_window(self.web_driver.current_window)
            self.web_driver.set_size("min")
            self.fd["home"].select_skip_btn()
        else:
            self.fd["gotham_utility"].click_close_pop_up('Popup Window')
        self.fd["home"].verify_home_screen(timeout=60)

    def handle_web_login(self, username="", password="", create_account=False, email=None, from_sign_up=False, from_sign_in=False):
        """
        HP Smart login flow by sign in an exist account or create a new account.
        """
        web_login_flag = False
        self.fd["hpid"] = HPID(self.driver)
        try:
            if not self.fd["hpid"].verify_hpid_popup_window(raise_e=False):
                web_login_flag = True
                time.sleep(3)
                self.web_driver.add_window(self.window_name)
                time.sleep(3)
                self.web_driver.switch_window(self.window_name)
                self.web_driver.set_size("max")
                self.fd["hpid"] = HPID(self.web_driver, window_name=self.window_name)

            if not create_account:
                if from_sign_up:
                    self.fd["hpid"].verify_hp_id_sign_up()
                    self.fd["hpid"].click_sign_in_link_from_create_account()
                self.fd["hpid"].verify_hp_id_sign_in()
                self.fd["hpid"].login(username=username, password=password)
            else:
                if from_sign_in:
                    self.fd["hpid"].verify_hp_id_sign_in()
                    self.fd["hpid"].click_create_account_link()  
                self.fd["hpid"].verify_hp_id_sign_up()
                if not email:
                    return self.fd["hpid"].create_account()
                else:
                    self.fd["hpid"].verify_unable_to_create_account(email=email)
                    web_login_flag= False
        finally:
            if web_login_flag:
                self.web_driver.close_window(self.window_name)
                self.web_driver.set_size("min")

    def sign_in(self, username, password, from_sign_up=False):
        """
        Click My HP account button and sign in from Nav bar
        """
        if not from_sign_up:
            self.fd["home"].select_sign_in_btn()
        else:
            self.fd["home"].select_create_account_btn()
        self.handle_web_login(username=username, password=password, from_sign_up=from_sign_up)

    def create_account(self, create_account=True, email=None, from_sign_in=False):
        """
        Click Create Account button and sign up
        """
        if not from_sign_in:
            self.fd["home"].select_create_account_btn()
        else:
            self.fd["home"].select_sign_in_btn()
        return self.handle_web_login(create_account=create_account, email=email, from_sign_in=from_sign_in)

    def sign_out(self, is_hk_region=False):
        """
        Click Menu -> app settings -> sign out
        """ 
        self.fd["home"].select_app_settings_btn()
        self.fd["home"].select_sign_out_listview()
        self.fd["account"].verify_sign_out_dialog()
        self.fd["account"].select_sign_out_btn()
        if not is_hk_region:
            self.fd["home"].verify_home_screen(timeout=60)
        else:
            self.fd["ows_value_prop"].verify_windows_ows_value_prop_screen(flip=True)

    def search_network_printer(self, printer_obj):
        """
        Search prinrer in device pick screen
        """
        printer_ip_address = printer_obj.p_obj.ipAddress
        printer_ethernet_ip = ""
        if printer_obj.p_con.use_cdm:
            try:
                printer_ethernet_ip = printer_obj.p_con.ethernet_ip_address
            except AttributeError:
                logging.info(f"Ethernet IP address is unavailable for this printer")
            if len(printer_ethernet_ip) != 0:
                printer_ip_address = [printer_ip_address, printer_ethernet_ip]

        logging.info(f"Printer IP Address information: {printer_ip_address}")
        if type(printer_ip_address) is str:
            printer = self.fd["printers"].search_printer(printer_ip_address)
            printer.click()
        else:
            for i in range(len(printer_ip_address)):
                if printer := self.fd["printers"].search_printer(printer_ip_address[i], raise_e=False):
                    logging.info(f"Printer found: {printer_ip_address[i]}")
                    printer_ip_address = printer_ip_address[i]
                    printer.click()
                    break
            else:
                raise NoPrinterFoundException(f"Failed to find printer via wireless and ethernet IP {printer_ip_address}")
        return printer_ip_address

    def search_beaconing_printer(self, printer_obj):
        bonjour_name = printer_obj.get_printer_information()['bonjour name']
        printer_name = bonjour_name[bonjour_name.find("HP ") + 3:bonjour_name.find("series") - 1]
        self.fd["printers"].check_beaconing_printer_show(printer_name)
        printer = self.fd["printers"].search_printer(printer_name, beaconing_printer=True)
        printer.click()
    
    def select_a_printer(self, printer_obj, from_carousel=False, add_new=False, exit_setup=True, beaconing_printer=False):
        """
        Have a printer selected in the main UI.
        Need optimization!
        """
        self.fd["home"].verify_home_screen()
        if not from_carousel:
            self.fd["home"].select_left_add_printer_btn()
        elif add_new:
            self.fd["home"].click_add_new_printer_link()
        else:
            self.fd["home"].click_carousel_add_printer_btn()

        self.fd["printers"].verify_device_picker_screen()

        if beaconing_printer:
            self.search_beaconing_printer(printer_obj)
        else:
            printer_ip_address = self.search_network_printer(printer_obj)
        
        if self.fd["home"].verify_home_screen(raise_e=False) is False and exit_setup:
            if self.fd["moobe"].verify_press_info_btn_dialog(raise_e=False):
                printer_obj.press_info_btn()
            
            try:
                pin_num = printer_obj.get_pin()
                self.enter_printer_pin_number(pin_num)
            except AttributeError:
                 logging.info(f"'DuneUnderwareAppComponent' object has no attribute 'getDefaultDevicePassword'")
            
            if self.fd["printers"].verify_printer_setup_webpage(raise_e=False) and not self.fd["printers"].verify_exit_setup_btn(raise_e=False):
                self.fd["printers"].select_printer_setup_accept_all_btn()

            if self.fd["moobe"].verify_press_info_btn_dialog(raise_e=False):
                printer_obj.press_info_btn()
            self.enter_printer_pin_number(printer_obj.get_pin())

            if self.fd["printers"].verify_exit_setup_btn(raise_e=False):
                self.fd["printers"].select_exit_setup()
                self.fd["printers"].select_pop_up_exit_setup()
                if self.fd["printers"].verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    self.fd["printers"].select_pop_up_exit_setup()
                if self.fd["printers"].verify_install_success_dialog(raise_e=False):
                    self.fd["printers"].click_install_success_dialog_continue_btn()
            if self.fd["home"].verify_firmware_update_available_screen(raise_e=False):
                self.fd["home"].click_firmware_update_available_screen_no_btn()
            self.fd["home"].verify_home_screen()
        if self.fd["home"].verify_not_now(raise_e=False):
            self.fd["home"].select_not_now_skip_btn() # To Handle Upgrade to the new HP dialog/popup
        if not beaconing_printer:
            return printer_ip_address

    def select_a_remote_printer(self, from_carousel=False, add_new=False):
        if not from_carousel:
            self.fd["home"].select_left_add_printer_btn()
        elif add_new:
            self.fd["home"].click_add_new_printer_link()
        else:
            self.fd["home"].click_carousel_add_printer_btn()
        self.fd["printers"].verify_device_picker_screen()
        self.fd["printers"].select_remote_printer()
        self.fd["home"].verify_printer_add_to_carousel()
        
    def check_toggle_status(self, toggle_btn, toggle_image, num=0.45):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element(toggle_btn))
        cur_img = saf_misc.img_crop(cur_img, 0.87, 0.0, 0.0, 0.0)
        toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + 'privacy/' + toggle_image))
        assert saf_misc.img_comp(cur_img, toggle_img) < num 

    def check_element_background(self, ele, folder_n, comp_image, value=0.7):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element(ele))
        cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, value)
        comp_image = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + folder_n + "/" + comp_image))
        logging.info("Image compare value: {}".format(saf_misc.img_comp(cur_img, comp_image)))
        return saf_misc.img_comp(cur_img, comp_image)

    def save_image(self, ele, folder_n, image_n, value=0.7):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element(ele))
        cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, value)
        cur_img.save(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + folder_n + "/" + image_n))

    def del_shortcuts(self, shortcut_name, del_num=3):
        self.restart_hp_smart()
        self.fd["home"].verify_home_screen()
        self.fd["home"].select_shortcuts_tile()
        self.fd["shortcuts"].verify_shortcuts_screen()
        for _ in range(del_num):    
            for num in range(2, 10):
                if self.fd["shortcuts"].check_shortcut_item_name(num) == "shortcut-card-" + shortcut_name:
                    self.fd["shortcuts"].click_shortcut_option_btn(num)
                    self.fd["shortcuts"].click_delete_btn()
                    self.fd["shortcuts"].click_delete_popup_delete_btn(is_win=True)
                    self.fd["shortcuts"].verify_delete_shortcuts_dialog_disapper()
                    time.sleep(2)
                    break

    def clear_shortcuts_jobs(self, time_out=120):
        """
        Delect all shortcuts jobs
        """
        time_out = time.time() + time_out
        self.restart_hp_smart()
        self.fd["home"].verify_home_screen()
        self.fd["home"].select_shortcuts_tile()
        self.fd["shortcuts"].verify_shortcuts_screen()
        while time.time() < time_out:
            if self.fd["shortcuts"].verify_no_shortcuts_job():
                break
            self.fd["shortcuts"].click_edits_more_option_btn()
            self.fd["shortcuts"].click_delete_btn()
            self.fd["shortcuts"].verify_shortcut_delete_screen()
            self.fd["shortcuts"].click_delete_popup_delete_btn(is_win=True)

    def trigger_printer_status(self, serial_number, ioref_list=False):
        if self.fd["home"].verify_home_screen(raise_e=False) is False:
            self.fd["printer_status"].remove_action_center_file()

            self.fd["home"].select_navbar_back_btn()

        self.fd["home"].select_printer_settings_tile()
        self.fd["printer_settings"].select_printer_status_item()
        time.sleep(2)
        self.fd["home"].select_navbar_back_btn()
        self.fd["printer_status"].enable_printer_status(serial_number, ioref_list)

        self.fd["home"].select_printer_settings_tile()
        time.sleep(2)
        self.fd["printer_settings"].select_printer_status_item()

    def restore_printer_info_country_language(self, pin_num):
        self.fd["home"].select_printer_settings_tile()
        if self.fd["printer_settings"].verify_country_select_item('United States', timeout=10, raise_e=False) is False:
            self.fd["printer_settings"].click_country_dropdown()
            el = self.driver.wait_for_object("country_region_box")
            el.send_keys(Keys.END)
            self.fd["printer_settings"].select_country_item("United States")
            self.fd["printer_settings"].click_set_save_btn()
            if self.fd["printer_settings"].verify_sign_in_to_dialog(raise_e=False) is not False:
                self.fd["printer_settings"].edit_sign_in_password(pin_num)
                self.fd["printer_settings"].click_sign_in_submit_btn()
            self.fd["printer_settings"].verify_country_select_item('United States')
        if self.fd["printer_settings"].verify_language_select_item('English', timeout=10, raise_e=False) is False:
            self.fd["printer_settings"].click_language_dropdown()
            el = self.driver.wait_for_object("language_box")
            el.send_keys(Keys.HOME)
            self.fd["printer_settings"].select_language_item("English")
            self.fd["printer_settings"].click_set_save_btn()
            if self.fd["printer_settings"].verify_sign_in_to_dialog(raise_e=False):
                self.fd["printer_settings"].edit_sign_in_password(pin_num)
                self.fd["printer_settings"].click_sign_in_submit_btn()
            self.fd["printer_settings"].verify_language_select_item('English')

    def enable_print_anywhere_dialog(self, raise_e=True):
        for _ in range(3):
            if self.fd["home"].verify_print_anywhere_dialog(raise_e=False):
                break
            else:
                self.fd["home"].select_printer_settings_tile()
                self.fd["printer_settings"].verify_printer_settings_page()
                self.fd["home"].select_navbar_back_btn()
                time.sleep(2)
        else:
            if raise_e:
                return  NoSuchElementException('POTG optimize dialog does not show')
            else:
                return False
    
    def enter_printer_pin_number(self, pin_number):
        if self.fd["printers"].verify_pin_dialog(raise_e=False):
            self.fd["printers"].input_pin(pin_number)
            self.fd["printers"].select_pin_dialog_submit_btn()
        if self.fd["printers"].verify_pin_dialog(raise_e=False):
            self.fd["printers"].input_pin("12345678")
            self.fd["printers"].select_pin_dialog_submit_btn()

    def remove_hp_smart_driver(self):
        self.driver.ssh.send_command('Remove-Printer -Name "HP Smart Printing*"')
        assert self.verify_hp_smart_driver_install() is False

    def verify_hp_smart_driver_install(self, bonjour_name=False):
        all_printers_name = self.driver.ssh.send_command('Get-WmiObject -Query "SELECT * FROM Win32_Printer" | select-object name')["stdout"]
        assert "HP Smart Printing" in all_printers_name
        if bonjour_name:
           assert bonjour_name in all_printers_name 

    def check_task_scheduler(self, raise_e=False):
        task_list = self.driver.ssh.send_command('Get-ScheduledTask -TaskPath \HP\* | select-object TaskName')["stdout"]
        for task_scheduler in ['Printer Health Monitor', 'Printer Health Monitor Logon']:
            if task_scheduler not in str(task_list):
                if raise_e:
                    return False
                else:
                    raise NoSuchElementException("the task {} is not exist".format(task_scheduler))

    def check_kibana_event(self):
        if self.driver.session_data["request"].config.getoption("--analytics", False):
            base_url = "https://search-xray-x54sy5knolm6hdgr4zwifl5oiu.us-west-2.es.amazonaws.com"
            project_name = "smart"
            with self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH) as f:
                data = f.read().decode("utf-8").replace('\n', '')
            check_event = r"appId: ([a-z0-9-]{36})"
            app_instance_id = re.search(check_event, data).group(1)
            # Wait for the events show on Kibana
            time.sleep(60)
            r_res = self.driver.analytics_container.get_kibana_result(base_url=base_url, project=project_name, session_id=app_instance_id)
            c_res, faildict = self.driver.analytics_container.compare_results(r_res)
            if c_res is False:
                raise KibanaEventNotFoundException(f"Failed to find event from Kibana {faildict}")
            else:
                return True

    def clear_printer_data_flow(self, printer_uuid):
        self.reset_hp_smart()
        self.fd["welcome_web"].click_link("hp_privacy_statement_link")
        close_activity = self.get_activity_parameter()[1]
        self.driver.terminate_app(close_activity)
        self.web_driver.add_window(window_name="web_page")
        self.web_driver.set_size("max")
        self.stratus_utility = StratusUtility(self.web_driver, window_name="web_page")
        self.stratus_utility.unclaimed_printer_flow(printer_uuid)

    def trigger_printer_offline_status(self, printer_obj):
        self.driver.ssh.send_command("netsh wlan disconnect")
        if "DunePrinterInfo" in str(printer_obj.p_obj):
            printer_obj.pp_module._power_off()
            
    def restore_printer_online_status(self, printer_obj):
        request = self.driver.session_data["request"]
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        self.driver.connect_to_wifi(host, user, ssid, password)
        if "DunePrinterInfo" in str(printer_obj.p_obj):
                printer_obj.pp_module._power_on()

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************

class CannotGoHomeException(Exception):
    pass 

class IPAddressMismatch(Exception):
    pass

class NoPrinterFoundException(Exception):
    pass

class KibanaEventNotFoundException(Exception):
    pass
