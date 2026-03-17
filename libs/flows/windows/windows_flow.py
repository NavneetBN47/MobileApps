import logging
import time
import os
import pytest
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow
from selenium.webdriver.common.keys import Keys
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from selenium.webdriver.common.action_chains import ActionChains

class WindowsFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "windows"

    def __init__(self, driver):
        super(WindowsFlow, self).__init__(driver)
        self.load_windows_system_ui()

    def load_windows_system_ui(self):
        ui_map = self.load_ui_map(system="WINDOWS", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map, append=True)
        return True

    def click_close_pop_up(self, pop_up_name, raise_e=True):
        """
        Click close window button in the title bar of a pop up
        """
        if not self.driver.wait_for_object("close_pop_up_window_btn", format_specifier=[pop_up_name], raise_e=raise_e):
            logging.info("Pop up window: {} is not found".format(pop_up_name))
            return False
        self.driver.click("close_pop_up_window_btn", format_specifier=[pop_up_name])
        self.driver.swipe(direction="up", distance=2)

    def click_close(self):
        """
        Click close btn
        """
        self.driver.click("_system_close_btn")

    def click_minimize(self):
        """
        Click min btn
        """
        self.driver.click("_system_min_btn")

    def click_maximize(self):
        """
        Click max btn
        """
        self.driver.click("_system_max_btn") 

    # *********************************************************************************
    #                             VERIFICATION FLOWS                                  *
    # *********************************************************************************

    def verify_window_visual_state_maximized(self):
        """
        verifies the window is maximized
        :return: bool
        """
        return self.driver.wait_for_object("window_visual_state_maximized", raise_e=False, timeout=3) is not False

    def verify_windows_version(self):
        """
        Verify the windows version
        return: version
        """
        version = self.driver.ssh.send_command("Get-CimInstance Win32_Operatingsystem | Select-Object -expand Caption")['stdout']
        return version
    
    def click_search_bar_on_windows(self):
        self.driver.click("search_bar_on_windows")

    def search_bar_on_windows(self, app_name, navigate_down=0):
        """
        Search for an app in Windows search bar and launch it.
        
        Args:
            app_name (str): Name of the application to search for
            navigate_down (int): Number of DOWN arrow key presses to navigate to specific result
                                0 = first result (default), 1 = second result, etc.
        """
        self.driver.clear_text("search_bar_on_windows")
        self.driver.send_keys("search_bar_on_windows", app_name)
        time.sleep(1)  # Wait for search results to populate
        
        # Navigate to the desired result position
        for _ in range(navigate_down):
            self.driver.send_keys("search_bar_on_windows", Keys.DOWN)
            time.sleep(0.3)
        
        # Launch the selected result
        self.driver.send_keys("search_bar_on_windows", Keys.ENTER)
        self.driver.send_keys("search_bar_on_windows", Keys.ENTER)

    def press_tab(self, element):
        self.driver.send_keys(element, Keys.TAB)

    def press_reverse_tab(self, element):
        self.driver.send_keys(element, Keys.SHIFT + Keys.TAB)

    def press_enter(self, element):
        self.driver.send_keys(element, Keys.ENTER)

    def press_alt_f4_to_close_app(self):
        el = self.driver.wait_for_object("root_web_area", timeout=10)
        try:
            ActionChains(self.driver.driver).key_down(Keys.ALT).send_keys(Keys.F4).key_up(Keys.ALT).perform()
            time.sleep(2)
        except:
            # Method 2: Alternative approach - focus element and try Alt+F4 directly
            el.click()  # Focus the window first
            time.sleep(1)
            el.send_keys(Keys.ALT, Keys.F4)  # Send keys separately
            time.sleep(2)

    def is_focus_on_element(self,element):
        focus = bool(self.driver.get_attribute(element,"HasKeyboardFocus", raise_e=True, timeout=15))
        logging.info("Focus on element {}: {}".format(element, focus))
        return focus


    def click_microsoft_store_app(self):
        self.driver.click("ms_store_app_open")

    def ms_store_search_box(self,app):
        el = self.driver.wait_for_object("ms_store_search_box", timeout=10)
        el.click()
        el.clear()
        el.send_keys(app)

    def click_install_app(self,locator):
        self.driver.click(locator)

    def wait_for_object(self,locator):
        return self.driver.wait_for_object(locator, raise_e=False)
    
    def install_button_to_install_app_from_ms_store(self):
        self.driver.click("install_button_to_install_app_from_ms_store", timeout = 10)

    def click_get_button_to_install_app_from_ms_store(self):
        self.driver.click("get_button_to_install_app_from_ms_store", timeout = 10)  

    def click_uninstall_app_button(self):
        self.driver.click("uninstall_app_button")   

    def click_uninstall_app_pop_up(self):
        self.driver.click("uninstall_app_pop_up")

    def click_back_to_home_from_search_menu(self):
        self.driver.click("back_to_home_from_search_menu") 

    def my_hp_app_reset(self, app):
        self.driver.click("search_bar_on_windows", timeout = 20)
        time.sleep(5)
        self.driver.clear_text("search_box_on_windows")
        time.sleep(5)
        self.driver.send_keys("search_bar_on_windows", app)
        time.sleep(5)

    def click_app_settings_tab(self):
        self.driver.click("my_hp_system_app_settings", timeout=15)

    def click_app_reset_button(self):
        self.driver.click("app_reset_button" , timeout =10)  
        time.sleep(15)    
        self.driver.click("app_reset_confirm_button")

    def scroll_window_locator(self):
        return self.driver.wait_for_object("scroll_window", timeout=10)    
    
    def verify_settings_window_maximize(self):
        return self.driver.wait_for_object("maximize_settings_window").get_attribute("Name")
    
    def maximize_settings_window(self):
        self.driver.click("maximize_settings_window")
    
    def click_on_profile_icon_to_sign_in_msstore(self):
        self.driver.click("profile_icon_on_msstore", timeout=15)

    def click_on_sign_in_msstore(self):
        self.driver.click("sign_in_to_msstore", timeout=15)

    def is_sign_in_present(self):
        return self.driver.wait_for_object("sign_in_to_msstore", raise_e=False, timeout=15) is not False

    def click_microsoft_account_button_on_sign_in_page(self):
        self.driver.click("microsoft_account_button", timeout=15)
    
    def click_continue_button_on_sign_in_page(self):
        self.driver.click("continue_button_to_msaccount_button", timeout=15)
    
    def is_continue_button_on_sign_in_page_present(self):
        return self.driver.get_attribute("continue_button_to_msaccount_button", "Name", raise_e=False, timeout=15) is not False
    
    def click_next_button_first_time_signin(self):
        if self.driver.get_attribute("next_button_first_time_signin", "Name", raise_e=False, timeout=15) is not False:
            self.driver.click("next_button_first_time_signin", timeout=15)
 
    def verify_next_button_first_time_signin(self):
        return self.driver.get_attribute("next_button_first_time_signin", "Name", raise_e=False, timeout=15) is not False
           
    def enter_email_address(self, email_address):
        """
        send the email address in text field
        :param email_address:
        :return:
        """
        if self.driver.get_attribute("email_text_box", "Name", raise_e=False, timeout=15) is not False:
            self.driver.click("email_text_box", timeout=5)
            self.driver.send_keys("email_text_box", email_address)

    def click_next_button_on_sign_in_page(self):
        self.driver.click("next_button_to_signin_page", timeout=15)     

    def enter_password(self, password):
        """
        clicks in the password text field and send the keys, or clicks "Use my password" if password field is not present
        :param password:
        :return:
        """
        # Check if password text box is present
        if self.driver.wait_for_object("password_text_box", raise_e=False, timeout=5):
            # Password text box is present, enter password
            self.driver.click("password_text_box")
            self.driver.send_keys("password_text_box", password)
        else:
            # Password text box is not present, click "Use my password" button
            self.driver.click("ms_store_use_my_password", timeout=15)
            # Wait for password text box to appear after clicking "Use my password"
            self.driver.wait_for_object("password_text_box", timeout=10)
            self.driver.click("password_text_box")
            self.driver.send_keys("password_text_box", password)    

    def click_signin_button_on_sign_in_page(self):
        if self.driver.get_attribute("signin_button_to_signin", "Name", raise_e=False, timeout=15) is not False:
            self.driver.click("signin_button_to_signin", timeout=15)      

    def click_library_button_on_msstore(self):
        self.driver.click("library_button_on_msstore", timeout=30)    

    def click_library_sort_and_filter_on_msstore(self):
        self.driver.click("library_sort_and_filter_on_msstore", timeout=30)    

    def click_library_sort_by_date_on_msstore(self):
        self.driver.click("library_sort_by_date_on_msstore", timeout=30)
   
    def click_library_myhp_app_option_button(self):
        self.driver.click("library_myhp_app_option_button", timeout=40) 

    def verify_myhp_app_update_option_button_is_present(self):
        self.driver.get_attribute("myhp_app_update_option_button", "Name", raise_e=False, timeout=60) is not False   

    def click_myhp_app_update_option_button(self):
        self.driver.click("myhp_app_update_option_button", timeout=60)

    def click_myhp_app_open_option_button_after_update(self):
        if self.driver.wait_for_object("myhp_app_update_option_retry_button", timeout=15, raise_e=False):
            self.driver.click("myhp_app_update_option_retry_button", timeout=15)
            self.driver.click("myhp_app_open_option_button_after_update", timeout=15) 
        else:
            self.driver.click("myhp_app_open_option_button_after_update", timeout=15)         

    def click_signout_button_on_sign_in_page(self):
        self.driver.click("profile_icon_on_msstore", timeout=15)
        if self.driver.wait_for_object("signout_button", timeout=15, raise_e=False):
            self.driver.click("signout_button", timeout=10)     

    def click_to_install_signed_build(self):
        if(self.driver.wait_for_object("install_signed_build_1", raise_e=False, timeout=30) is not False):
            self.driver.click("install_signed_build_1", timeout=30)
        else:
            self.driver.click("install_signed_build_2", timeout=30)      

    def verify_toggle_for_set_automatically_time_onoroff(self):
        return self.driver.get_attribute("set_time_toggle","Toggle.ToggleState", timeout = 30)
    
    def click_toggle_for_set_automatically_time(self):
        self.driver.click("set_time_toggle", timeout = 40)

    def click_open_tab(self):
        self.driver.click("app_open")  

    def run_command_to_change_date(self,command):
        self.driver.send_keys("run_text_box",command)

    def click_run_ok_tab(self):
        self.driver.click("run_ok_button", timeout = 30)

    def click_get_updates_button(self):
        self.driver.click("get_update_button", timeout = 120)

    def click_back_arrow_msstore(self):
        self.driver.click("back_arrow_button_on_msstore", timeout=15)    

    def verify_myhp_app_version(self):
        result = self.driver.ssh.send_command("powershell.exe 'Get-AppxPackage *myHP* | Select Version'", timeout=10)
        version_output = result.get('stdout', '')
        print(f"SSH Command Output: {version_output}")
        version_lines = version_output.strip().splitlines()
        version = None
        for line in version_lines:
            if line.strip() and 'Version' not in line and '-------' not in line:
                version = line.strip()
                break
        if not version:
            raise ValueError("Version information not found in SSH command output")
        print(f"Extracted SSH Version: '{version}'")
        return version
    
    def verify_library_myhp_app_option_button(self):
        return self.driver.wait_for_object("library_myhp_app_option_button", raise_e=False, timeout=15) is not False
    
    def verify_back_arrow_msstore(self):
        return self.driver.wait_for_object("back_arrow_button_on_msstore", raise_e=False, timeout=15) is not False
    
    def verify_downloads_and_updates_button(self):
        return self.driver.wait_for_object("download_and_updates", raise_e=False, timeout=15) is not False
    
    def click_downloads_and_updates_button(self):
        self.driver.click("download_and_updates", timeout=15)  

    def click_app_folder(self):
        self.driver.click("app_folder", timeout=5)
        self.driver.send_keys("app_folder",Keys.ENTER)
    
    def click_appx_bundle(self):
        self.driver.click("appx_bundle", timeout=5)
        self.driver.send_keys("appx_bundle",Keys.ENTER)
    
    def verify_color_profile_in_display_setting(self):
        return self.driver.wait_for_object("color_profile_in_display_setting", raise_e=False, timeout=15) is not False
    
    def get_mode_in_display_setting(self):
        return self.driver.get_attribute("mode_in_display_setting", "Name", raise_e=False, timeout=15)

    def click_mode_in_display_setting(self):
        self.driver.click("mode_in_display_setting", timeout=15)
    
    def click_select_low_blue_light_in_setting(self):
        self.driver.click("select_low_blue_light_in_setting", timeout=15)

    def verify_uninstall_app_button(self):
        return self.driver.wait_for_object("uninstall_app_button", timeout=5)
    
    def verify_uninstall_app_pop_up(self):
        return self.driver.wait_for_object("uninstall_app_pop_up", timeout=5)
    
    def get_default_color_profile_in_setting(self):
        return self.driver.get_attribute("default_color_profile_in_setting", "Name", raise_e=False, timeout=15)

    def get_entertainment_color_profile_in_setting(self):
        return self.driver.get_attribute("entertainment_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_low_blue_light_color_profile_in_setting(self):
        return self.driver.get_attribute("low_blue_light_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_low_light_color_profile_in_setting(self):
        return self.driver.get_attribute("low_light_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_native_color_profile_in_setting(self):
        return self.driver.get_attribute("native_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_photos_and_videos_color_profile_in_setting(self):
        return self.driver.get_attribute("photos_and_videos_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_printing_and_imaging_color_profile_in_setting(self):
        return self.driver.get_attribute("printing_and_imaging_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_web_rgb_color_profile_in_setting(self):
        return self.driver.get_attribute("web_rgb_color_profile_in_setting", "Name", raise_e=False, timeout=15)
    
    def get_work_color_profile_in_setting(self):
        return self.driver.get_attribute("work_color_profile_in_setting", "Name", raise_e=False, timeout=15)

    def click_installedapps_searchbar(self, app):
        self.driver.get_attribute("installedapps_searchbar", "Name", raise_e=False, timeout=15) is not False
        time.sleep(2)
        self.driver.click("installedapps_searchbar", timeout = 20)
        time.sleep(5)
        self.driver.clear_text("installedapps_searchbar")
        time.sleep(5)
        self.driver.send_keys("installedapps_searchbar", app)
        time.sleep(5)

    def verify_threedots_option(self):
        return self.driver.wait_for_object("threedots_option", raise_e=False, timeout=15) is not False
    
    def verify_advanced_option(self):
        return self.driver.wait_for_object("advanced_option", raise_e=False, timeout=15) is not False

    def click_threedots_option(self):
        self.driver.click("threedots_option", timeout=30)

    def click_advanced_option(self):
        self.driver.click("advanced_option", timeout=30)
        
    def search_bar_on_windows_uninstall(self,app_name):
        self.driver.clear_text("search_bar_on_windows")
        self.driver.send_keys("search_bar_on_windows", app_name)
    
    def select_low_blue_light_color_profile_in_setting(self):
        self.driver.click("low_blue_light_color_profile_in_setting", timeout=5)
    
    def select_native_color_profile_in_setting(self):
        self.driver.click("mode_in_display_setting", timeout = 10)
        self.driver.click("native_color_profile_in_setting", timeout=5)
    
    def select_native_entertainment_profile_in_setting(self):
        self.driver.click("mode_in_display_setting", timeout = 10)
        self.driver.click("entertainment_color_profile_in_setting", timeout=5)
    
    def select_default_color_profile_in_setting(self):
        self.driver.click("mode_in_display_setting", timeout = 10)
        self.driver.click("default_color_profile_in_setting", timeout=5)

    # ----------------Windows Settings(Printers & Scanners)---------------- #
    def click_ps_big_plus_btn(self):
        self.driver.click("add_a_printer_or_scanner_btn")

    def click_ps_printer_list_item_by_name(self, value_name, time_out=120):
        time_out = time.time() + time_out
        while time.time() < time_out:
            if self.driver.wait_for_object("add_printer_item_by_name", format_specifier=[value_name], raise_e=False, timeout=2):
                logging.info("Install printer driver on Win Settings...")
                if self.driver.wait_for_object("add_device_btn", format_specifier=[value_name], raise_e=False, timeout=2):
                    self.click_ps_add_device_btn(value_name) 
                else:
                    self.driver.click("add_printer_item_by_name", format_specifier=[value_name]) # for win10 os
                    if not self.driver.wait_for_object("add_device_btn", format_specifier=[value_name], raise_e=False, timeout=2):
                       self.driver.swipe()
                    self.click_ps_add_device_btn(value_name) 
                # Won't fail if not ready,simulator printer always shows Driver is unavailable)
                if self.verify_ps_printer_ready_text(raise_e=False):
                    logging.info("Printer '{}' status is Ready".format(value_name))
                else:
                    logging.warning("Could not verify 'Ready' status for '{}', but Add device was clicked".format(value_name))
                return True
            else:
                self.driver.swipe(distance=3)
                sleep(1)
        else:
            logging.info("Failed to install '{}' driver on Win Settings".format(value_name))
            return False

    def click_ps_add_device_btn(self, value_name):
        self.driver.click("add_device_btn", format_specifier=[value_name])

    def click_settints_printers_and_scanners_text(self):
        self.driver.click("win_settings_search_box", timeout=10)
        self.driver.send_keys("win_settings_search_box", "Printers")
        self.driver.send_keys("win_settings_search_box", Keys.ENTER)
        if self.driver.wait_for_object("bluetooth_and_devices_text", raise_e=False, timeout=10):
            self.driver.click("bluetooth_and_devices_text", timeout=10)
        self.driver.click("win_settints_printers_and_scanners", timeout=10)

    def verify_target_printer_display(self, value_name, raise_e=True):
        """
        Target printer
        """
        return self.driver.wait_for_object("target_printer", format_specifier=[value_name], raise_e=raise_e)

    def verify_ps_big_plus_btn(self):
        self.driver.wait_for_object("add_a_printer_or_scanner_btn")

    def verify_ps_progress_bar(self):
        self.driver.wait_for_object("printer_add_progress_bar", timeout=60, invisible=True)

    def verify_ps_printer_ready_text(self, raise_e=True):
        self.driver.swipe("add_a_printer_or_scanner_btn", direction="up")
        return self.driver.wait_for_object("add_printer_item_by_name", format_specifier=["Ready"], timeout=120, raise_e=raise_e)

    def select_printer_on_win_settings(self, value_name):
        try:
            if value_name in self.driver.ssh.send_command('Get-Printer')['stdout']:
                logging.info("The printer has already been installed. You don't need to install it again.")
            else:
                self.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized') 
                self.click_settints_printers_and_scanners_text()        
                self.verify_ps_big_plus_btn()
                self.click_ps_big_plus_btn()
                self.verify_ps_progress_bar()
                logging.info("Searching {} in Add a printer or scanner".format(value_name))
                return self.click_ps_printer_list_item_by_name(value_name)    
        finally:
            sleep(2)
            self.driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')

    def get_display_control_hdr_toggle_window_setting_enabled_disable(self):
        return self.driver.get_attribute("display_control_hdr_toggle_window_setting", "IsEnabled",  timeout = 20)
    
    def get_display_control_hdr_toggle_window_setting_toggle_state(self):
        return self.driver.get_attribute("display_control_hdr_toggle_window_setting", "Toggle.ToggleState",  timeout = 20)
    
    def click_display_control_hdr_toggle_window_setting(self):
        self.driver.click("display_control_hdr_toggle_window_setting", timeout = 10)
        
    def click_setting_on_taskbar(self):
        self.driver.click("setting_on_taskbar", timeout = 10)
    
    def get_system_setting_brightness_slider(self):
        return self.driver.get_attribute("system_setting_brightness_slider", "Value.Value",  timeout = 10)
        
    def verify_system_setting_brightness_slider(self):
        return self.driver.wait_for_object("system_setting_brightness_slider",raise_e=False, timeout = 10) is not False
    
    def verify_color_profile_in_display_setting(self):
        return self.driver.wait_for_object("color_profile_in_display_setting",raise_e=False, timeout = 10) is not False
    
    def select_mode_low_blue_light_in_display_setting(self):
        self.driver.click("mode_in_display_setting", timeout = 10)
        self.driver.click("low_blue_light_color_profile_in_setting", timeout = 10)
    
    def select_mode_low_light_color_profile_in_setting(self):
        self.driver.click("mode_in_display_setting", timeout = 10)
        self.driver.click("low_light_color_profile_in_setting", timeout = 10)

    def launch_all_apps(self, apps):
        self.driver.click("search_bar_on_windows")
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", apps)
        time.sleep(5)
        el = self.driver.wait_for_object("search_bar_on_windows", displayed=False, timeout=10)
        el.send_keys(Keys.ENTER)

    def verify_smart_experience_use_video_hdr_in_system_setting_menu_button(self):
        return self.driver.wait_for_object("smart_experience_use_video_hdr_in_system_setting_menu_button", raise_e=False, timeout=15)
    
    def click_smart_experience_use_video_hdr_in_system_setting_menu_button(self):
        self.driver.click("smart_experience_use_video_hdr_in_system_setting_menu_button", timeout = 10)

    def verify_smart_experience_use_system_settings_video_hdr_toggle_switch(self):
        return self.driver.wait_for_object("smart_experience_use_system_settings_video_hdr_toggle_switch", raise_e=False, timeout=15)  
    
    def click_smart_experience_use_system_settings_video_hdr_toggle_switch(self):
        self.driver.click("smart_experience_use_system_settings_video_hdr_toggle_switch", timeout = 10)

    def get_smart_experience_use_system_settings_video_hdr_toggle_switch_state(self):
        return self.driver.get_attribute("smart_experience_use_system_settings_video_hdr_toggle_switch", "Toggle.ToggleState",  timeout = 20)
    
    def verify_iqiyi_app_launch(self):
        return self.driver.wait_for_object("iqiyi_app", raise_e=False, timeout=10)

    def verify_tencent_app_launch(self):
        return self.driver.wait_for_object("tencent_app", raise_e=False, timeout=10)

    def verify_disney_plus_app_launch(self):
        return self.driver.wait_for_object("disney_plus_app", raise_e=False, timeout=10)
    
    def click_to_install_hp_presence_app(self):
        self.driver.click("install_hp_presence_msstore", timeout=10)
        self.driver.wait_for_object("hp_presence_app_installed", raise_e=False, timeout=75) is not False

    def click_to_install_poly_camera_app(self):
        if self.driver.wait_for_object("poly_camera_pro_on_msstore_open", raise_e=False, timeout=10):
            self.kill_msstore_process()
        elif self.driver.wait_for_object("install_poly_camera_msstore", raise_e=False, timeout=10):
                self.driver.click("install_poly_camera_msstore", timeout = 10)
        else:
            self.driver.click("install_hp_presence_msstore", timeout = 10)

    def verify_uninstall_option(self):
        return self.driver.wait_for_object("uninstall_option_on_windows_settings", raise_e=False, timeout=15) is not False

    def click_uninstall_option(self):
        self.driver.click("uninstall_option_on_windows_settings", timeout=30)

    def verify_uninstall_confirmation_option(self):
        return self.driver.wait_for_object("uninstall_confirmation_on_windows_settings", raise_e=False, timeout=15) is not False    

    def click_uninstall_confirmation_option(self):
        self.driver.click("uninstall_confirmation_on_windows_settings", timeout=30)           

    def click_windows_power_mode_dropdown(self):
        self.driver.click("windows_power_mode_dropdown", timeout = 10)

    def get_plugged_in_selected_value(self):
        return self.driver.get_attribute("plugged_in_dropbox_selection", "Name", timeout=10)
    
    def get_windows_setting_myhp_notification_toggle_on_off_status(self):
        return self.driver.get_attribute("windows_setting_myhp_notification_toggle_on_off_status", "Toggle.ToggleState",  timeout = 10)
   
    def click_windows_setting_myhp_notification_toggle(self):
        self.driver.click("windows_setting_myhp_notification_toggle", timeout=10)

    def click_windows_setting_myhp_notification_toggle_on_off_status(self):
        self.driver.click("windows_setting_myhp_notification_toggle_on_off_status", timeout=10)
    
    def click_more_settings_via_blutooth_devices(self):
        self.driver.ssh.send_command('Start-Process ms-settings:devices') 
        #Go to settings --> Bluetooth & devices --> Pen & Windows>>Now click on the option "More settings from device manufacturer"
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        self.driver.click("pen_and_windows_ink_in_blutooth_and_device_settings", timeout=10)
        self.driver.click("more_settings_from_your_device_manufacturer_pen_and_windows_ink", timeout=10)
    
    def verify_get_an_app_open_this_hpx_link_popup(self):
        return self.driver.wait_for_object("get_an_app_open_this_hpx_link_popup", raise_e=False, timeout=15)

    def set_slider_value(self, slider, desired_value):
        slider_element = self.driver.wait_for_object(slider, timeout=30)
        self.driver.click(slider, timeout=20)
        
        current_slider_value = int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20))
        slider_difference = current_slider_value - desired_value

        if slider_difference > 0:
            for _ in range(slider_difference):
                time.sleep(2)
                slider_element.send_keys(Keys.LEFT)
                if int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20)) == desired_value:
                    break
        else:
            for _ in range(abs(slider_difference)):
                time.sleep(2)
                slider_element.send_keys(Keys.RIGHT)
                if int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20)) == desired_value:
                    break
    
    def install_poly_camera_on_commercial_system(self):
        self.driver.ssh.send_command('Start-Process "ms-windows-store://pdp/?productid=9N5T284JMQ5Z"', timeout = 10)
        time.sleep(3)
        self.click_to_install_poly_camera_app()
        time.sleep(20)
    
    def install_button_to_install_owned_app_from_ms_store(self):
        self.driver.click("install_button_to_install_owned_app_from_ms_store", timeout = 10)
    
    def install_button_to_install_new_app_from_ms_store(self):
        self.driver.click("install_button_to_install_new_app_from_ms_store", timeout = 10)

    def get_windows_setting_myhp_page_notification_toggle_on_off_status(self):
        return self.driver.get_attribute("windows_setting_myhp_page_notification_toggle_on_off_status", "Toggle.ToggleState",  timeout = 10)

    def click_windows_setting_myhp_page_notification_toggle_on_off_status(self):
        self.driver.click("windows_setting_myhp_page_notification_toggle_on_off_status", timeout=10)

    def kill_msstore_process(self):
        self.driver.ssh.send_command('powershell taskkill /f /im WinStore.App.exe', raise_e=False, timeout=10)

    def install_hp_presence_commercial_system(self):
        self.driver.ssh.send_command('Start-Process "ms-windows-store://pdp/?productid=xp8bslz2t2wgks"', timeout = 10)
        time.sleep(3)
        self.click_to_install_hp_presence_app()
        time.sleep(55)

    def scroll_to_element(self,element):
        #scroll to the element
        logging.info("scroll to the top first")
        self.driver.swipe(direction="up", distance=50)
        #scroll down to element
        self.scroll_down_to_element(element)
    
    def scroll_down_to_element(self, element):
        # Scroll down to the element only if we know it is below the current view
        logging.info(f"Scrolling down to element: {element}")
        self.driver.scroll_element(element)
        logging.info("swipe one more in case the element is not fully displayed")
        self.driver.swipe(direction="down", distance=1)
        assert self.driver.wait_for_object(element, raise_e=False, timeout=5), f"Element {element} is not displayed after scrolling."
       
    def open_app_from_start_menu(self, app,open_app=False, pin_to_start_menu=False, unpin_from_start_menu=False, pin_to_taskbar_menu=False,unpin_from_taskbar_start_menu=False):
        self.driver.click("start_menu_window_btn", timeout =10)
        self.driver.wait_for_object("search_box_on_windows", timeout=10)
        self.driver.send_keys("search_box_on_windows", app)
        if open_app:
            if self.driver.wait_for_object("open_app_btn_from_start_menu",raise_e=False) is not False:
                self.driver.click("open_app_btn_from_start_menu")
        if pin_to_start_menu:
            if self.driver.wait_for_object("pin_to_start_menu",raise_e=False) is not False:
                self.driver.click("pin_to_start_menu")
        if unpin_from_start_menu:
            if self.driver.wait_for_object("unpin_from_start_menu",raise_e=False) is not False:
                self.driver.click("unpin_from_start_menu")
        if pin_to_taskbar_menu:
            if self.driver.wait_for_object("pin_to_taskbar_from_start_menu", raise_e=False) is not False:
                self.driver.click("pin_to_taskbar_from_start_menu")
        if unpin_from_taskbar_start_menu:
            if self.driver.wait_for_object("unpin_from_taskbar_start_menu", raise_e=False) is not False:
                self.driver.click("unpin_from_taskbar_start_menu")
    
    def get_color_profile_dd_mode_select_box_setting(self):
        return self.driver.get_attribute("color_profile_dd_mode_select_box", "Name", timeout=10)
    
    def get_focus_on_app(self, ele):
        if self.driver.wait_for_object("_system_min_btn", raise_e=False, timeout=10):
            self.driver.click("_system_min_btn")
        #click on task bar
        self.driver.click("myhp_app_icon_on_taskbar")
        if self.driver.wait_for_object("_system_min_btn", raise_e=False, timeout=10):
            self.driver.click(ele)

    def send_shift_f10_on_desktop(self):
        """
        Send Shift+F10 to the desktop to open the context menu
        """
        try:
            # Get the desktop element
            desktop_element = self.driver.wait_for_object("desktop", timeout=5)
            desktop_element.send_keys(Keys.SHIFT, Keys.F10)
            time.sleep(2)
            self.driver.click("display_settings_on_right_click_on_desktop")
            return True
        except Exception as e:
            logging.info(f"Failed to send Shift+F10 to desktop: {e}")
            return False
    
    def click_edge_on_taskbar(self):
        self.driver.click("edge_on_taskbar", timeout=10)
    
    def click_color_filter_radio_btn(self,element_name):
        self.driver.click(element_name, timeout=10)
    
    def set_contrast_theme_from_settings(self,theme_name):
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        self.driver.click("contrast_theme_dd", timeout=10)
        self.driver.click(theme_name, timeout=10)
        logging.info(f"Applying contrast theme: {theme_name}")
        self.driver.wait_for_object("apply_btn_contrast_theme", raise_e=False, timeout=10)
        self.driver.click("apply_btn_contrast_theme", timeout=10)
    
    def hover_on_element(self,element):
        self.driver.hover(element)

    def bring_app_back_to_focus(self):
        # WORKAROUND: The app loses focus and sometimes key presses don't register.
        # Clicking on maximize_app a couple of times brings focus back to the app.        
        self.click_maximize() 
        time.sleep(1)
        self.click_maximize()
        time.sleep(1)

    def set_slider_value_by_keys(self, slider_name, value_to_set, min_value, max_value):
        slider = self.driver.wait_for_object(slider_name)
        raw_val = self.driver.get_attribute(slider_name, "Value.Value", timeout=10)
        logging.info(f"Current text size value: '{raw_val}'")
        current_value = self.extract_value_from_percentage(raw_val, slider_name)
        delta = abs(current_value - value_to_set)
        logging.info(f"Difference between current and desired value: {delta}")
        self.driver.click(slider_name, timeout=20)
        if delta == 0:
            logging.info("Slider already at desired value, no action needed")
            return
        if value_to_set == max_value: 
            logging.info(f"Setting slider to max value {max_value}")
            self.driver.click(slider_name, timeout=20)
            slider.send_keys(Keys.END)
            time.sleep(2)
            self.driver.click(slider_name, timeout=20)
            return
        if value_to_set == min_value:
            logging.info(f"Setting slider to min value {min_value}")
            self.driver.click(slider_name, timeout=20)
            slider.send_keys(Keys.HOME)
            time.sleep(2)
            self.driver.click(slider_name, timeout=20)
            return
        key = Keys.LEFT if delta > 0 else Keys.RIGHT
        logging.info(f"Sending {key} key {delta} times")
        for _ in range(delta):
            slider.send_keys(key)
            time.sleep(0.05)

    def click_apply_text_size_slider(self):
        self.driver.click("text_size_slider_apply_change_button", timeout=10)
        time.sleep(5)

    def extract_value_from_percentage(self, v, slider_name):
        s = str(v).strip()
        if s.endswith('%'):
            s = s[:-1].strip()
        try:
            return int(s)
        except ValueError:
            raise ValueError(f"Unexpected slider value '{v}' for {slider_name}")

    def close_settings_window(self):
        self.driver.click("close_settings_window", timeout= 20)

    def update_text_size_in_system_settings(self, value):
        self.click_search_bar_on_windows()
        self.search_bar_on_windows("Text Size")
        self.set_slider_value_by_keys("text_size_slider", value , 100, 225)
        self.click_apply_text_size_slider()
        self.close_settings_window()
        time.sleep(5)

    def zoom_in(self):
        self.driver.send_keys("root_web_area", Keys.META + "=")

    def zoom_in_max(self):
        for _ in range(16):
            self.zoom_in()

    def zoom_out(self):
        self.driver.send_keys("root_web_area", Keys.META + "-")

    def reset_zoom(self):
        for _ in range(16):
            self.zoom_out()

    def close_magnifier(self):
        self.driver.send_keys("root_web_area", Keys.META + Keys.ESCAPE)

    def select_system_color_mode(self, mode):
        self.driver.ssh.send_command('start ms-settings:colors')    
        time.sleep(5)    
        logging.info(f"Selecting system color mode: {mode}")
        self.driver.click("system_settings_color_mode_combo_box", timeout=10)
        time.sleep(2)
        self.driver.click(mode, timeout=10)
        time.sleep(2)
        self.close_settings_window()
        time.sleep(2)

    def revert_system_color_mode(self):
        self.driver.ssh.send_command('start ms-settings:colors')    
        time.sleep(5)    
        self.driver.click("system_settings_color_mode_combo_box", timeout=10)
        time.sleep(2)
        self.driver.click("custom_mode", timeout=10)
        time.sleep(2)
        self.driver.click("system_settings_windows_mode_combo_box", timeout=10)
        time.sleep(2)
        self.driver.click("dark_mode", timeout=10)
        time.sleep(2)
        self.driver.click("system_settings_app_mode_combo_box", timeout=10)
        time.sleep(2)
        self.driver.click("light_mode", timeout=10)
        time.sleep(2)
        self.close_settings_window()
        time.sleep(2)

    def set_color_filter_toggle(self, state):
        current_state = self.driver.get_attribute("color_filter_toggle_switch", "Toggle.ToggleState")
        target_state = "1" if state == "on" else "0"
        if current_state != target_state:
            self.driver.click("color_filter_toggle_switch", timeout=10)

    def click_color_filter_button(self, element_name):
        self.driver.click(element_name, timeout=10)
        
    def change_system_color_filter(self, filter_name):
        self.driver.ssh.send_command('Start-Process "ms-settings:easeofaccess-colorfilter"', timeout = 10)
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        self.set_color_filter_toggle("on")
        self.scroll_to_element(filter_name)
        self.click_color_filter_radio_btn(filter_name)
        self.driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')

    def revert_system_color_filter(self):
        self.driver.ssh.send_command('Start-Process "ms-settings:easeofaccess-colorfilter"', timeout = 10)
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        self.set_color_filter_toggle("off")
        time.sleep(3)
        self.driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')
        
    def set_scale_from_settings(self, scale):
        self.driver.ssh.send_command('Start-Process ms-settings:display')
        time.sleep(2)
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        time.sleep(2)
        if not self.driver.wait_for_object("system_setting_brightness_slider", raise_e=False, timeout=10):
           self.click_setting_on_taskbar()
        logging.info(f"Setting scale to: {scale}")
        self.scroll_to_element("scale_combobox")
        time.sleep(2)
        self.driver.click("scale_combobox", timeout=10)
        self.driver.click(scale, timeout=10)
        time.sleep(2)
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', raise_e=False, timeout=40)

     #create image verification method for this testing
    def verify_scale_image(self,image_compare_result, image_name, scale):
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} image did not match the baseline for scale {scale}."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    def click_windows_explorer_on_taskbar(self):
        self.driver.click("windows_explorer_on_taskbar", timeout=10)
    
    def click_windows_ms_store_on_taskbar(self):
        self.driver.click("windows_msstore_on_taskbar", timeout=10)
    

    def set_scale_from_settings_for_task_group_module(self, scale):
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', raise_e=False, timeout=40)
        time.sleep(2)
        self.driver.ssh.send_command('Start-Process ms-settings:display')
        time.sleep(2)
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        time.sleep(2)
        logging.info(f"Setting scale to: {scale}")
        self.scroll_to_element("scale_combobox")
        time.sleep(2)
        self.driver.click("scale_combobox", timeout=10)
        self.driver.click(scale, timeout=10)
        time.sleep(2)
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', raise_e=False, timeout=40)

    def click_hp_app_window_title(self):
        self.driver.click("hp_app_window_title")

    def verify_hp_app_window_title(self):
        return self.driver.wait_for_object("hp_app_window_title")

    def scroll_dropdown_by_key(self, desired_mode_id):
        self.driver.send_keys("root_web_area",Keys.HOME)
        if self.driver.wait_for_object(desired_mode_id, raise_e=False, timeout=10) is False:
            self.driver.send_keys("root_web_area",Keys.END)
    
    def set_external_monitor_as_extended(self):
        self.driver.ssh.send_command('Start-Process ms-settings:display') 
        time.sleep(5)
        if "Maximize Settings" == self.verify_settings_window_maximize():
            self.maximize_settings_window()
        self.driver.click("external_monitor_setting_option", timeout=10)
        time.sleep(2)
        #set option as extended in dropdown
        self.driver.click("Extend_these_displays_option_in_external_monitor_setting", timeout=10)
        time.sleep(2)
        #select keep changes on popup if appears
        if self.driver.wait_for_object("keep_changes_on_popup", raise_e=False, timeout=10):
            self.driver.click("keep_changes_on_popup", timeout=10)
            time.sleep(2)
        self.close_settings_window()
        time.sleep(2)
    
    def minimize_windows_explorer_on_taskbar(self):
        self.driver.click("windows_explorer_minimize_button", timeout=10)

    def capture_screenshot(self, screenshot_path=None, page_name=None):
        """
        Capture a screenshot of the current application state.
        
        Args:
            screenshot_path (str, optional): Custom path to save the screenshot. Defaults to test result folder.
            page_name (str, optional): Name to use for the screenshot file. Defaults to test name.
        """
        current_test = os.environ.get("PYTEST_CURRENT_TEST")
        if current_test:
            test_name = current_test.split(" ")[0].split("::")[-1]
        if screenshot_path is None:
            base_dir = getattr(pytest, "test_result_folder", None)
            if base_dir:
                screenshot_dir = os.path.join(base_dir, test_name)
            else:
                screenshot_dir = os.getcwd()
            if not os.path.isdir(screenshot_dir):
                os.makedirs(screenshot_dir)
            file_name = f"{test_name}_{page_name}.png" if page_name else f"{test_name}.png"
            screenshot_path = os.path.join(screenshot_dir, file_name)
        else:
            if not os.path.isdir(screenshot_path):
                os.makedirs(screenshot_path)
            file_name = f"{test_name}_{page_name}.png" if page_name else f"{test_name}.png"
            screenshot_path = os.path.join(screenshot_path, file_name)
        time.sleep(3)  # allow time to click actions to happen
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot captured successfully: {screenshot_path}")
