from MobileApps.libs.flows.windows.hpx.system_preferences import SystemPreferences
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
import pytest
from time import sleep
import os

class SystemFlow(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver
        self.sp = SystemPreferences(driver)

    def click_system_notification(self):
        self.sp.click_on_notification()

    def turn_off_toggle_notification(self):
        self.sp.toggle_notification()

    def get_toggle_notification_state(self):
        return self.sp.toggle_notification_state()

    def verify_device_and_account(self):
        return self.sp.verify_device_and_account_state()

    def verify_tips_and_tutorials(self):
        return self.sp.verify_tips_and_tutorials_state()

    def verify_news_and_offers(self):
        return self.sp.verify_news_and_offers_state()

    def verify_share_your_feedback(self):
        return self.sp.verify_share_your_feedback_state()

    def click_news_and_offers(self):
        self.sp.click_news_and_offers()

    def click_share_your_feedback(self):
        self.sp.click_share_your_feedback()

    def click_external_link(self):
        self.sp.click_external_link_to_navigate_sytem_notification()

    def click_on_system_notification_close(self):
        self.sp.click_system_notification_close()

    def click_confirmation_pop_up(self):
        self.sp.click_confirmation_pop_up()

    def close_myhp_app(self):
        self.sp.click_close_button()

    def click_start_btn(self):
        self.sp.click_start_btn()

    def verify_open_btn_on_HP_app(self):
        return self.sp.verify_open_btn_on_HP()

    def input_text_in_search_box(self,app_name):
        self.sp.input_text_in_search_box(app_name)

    def input_text_in_aplicationsearch(self,app_name):
        self.sp.input_text_in_aplicationsearch(app_name)

    def input_url_in_website_box(self,url):
        self.sp.input_url_in_website_box(url)

    def click_close_btn_setting(self):
        self.sp.click_close_On_Setting()

    def click_myHP_app_On_Start_To_Open(self):
        self.sp.click_myHP_app_On_Start()
    
    def click_app_setting_on_myHP(self):
        self.sp.click_app_setting_on_myHP()
    
    def get_app_name_in_app_setting(self):
        return self.sp.get_app_name_in_app_setting()
    
    def get_app_version_in_app_setting(self):
        return self.sp.get_app_version_in_app_setting()
    
    def get_app_size_in_app_setting(self):
        return self.sp.get_app_size_in_app_setting()
    
    def verify_app_version_in_app_setting(self):
        return self.sp.verify_app_version_in_app_setting()
    
    def maximize_settings_app(self):
        return self.sp.maximize_settings_window()
    
    def verify_app_size(self):
        return self.sp.verify_app_size()
    
    def verify_reset_button(self):
        return self.sp.verify_reset_button()
    
    def verify_uninstall_btn_on_app_setting(self):
        return self.sp.verify_uninstall_btn_on_app_setting()
    
    def click_myHP_app_using_msix_bundle(self):
        self.sp.click_hpx_folder_under_misx_bundle()
        self.sp.click_hpx_msix_bundle()
        
    def click_open_btn_on_HP(self):
        self.sp.click_open_btn_on_HP()
    
    def get_app_name_on_installer_window(self):
        return self.sp.get_app_name_on_installer_window()
    
    def get_app_version(self):
        return self.sp.get_app_version()
    
    def click_more_btn(self):
        self.sp.click_more_btn()
    
    def verify_app_capabilities(self):
        return self.sp.verify_app_capabilities()
    
    def click_launch_btn(self):
        self.sp.click_launch_btn()

    def click_search_box(self):
        self.sp.click_on_search_box()

    def enter_text_search_box(self):
        self.sp.enter_text_on_search_box()

    def click_on_open_tab_from_start_menu(self):
        self.sp.click_on_open_tab_from_start_menu()
    
    def click_start_btn_taskbar(self):
        self.sp.click_start_btn_taskbar()
    
    def verify_accessibility_tool_on_taskbar(self):
        return self.sp.verify_accessibility_tool_on_taskbar()
    
    def click_inspect_on_accessibility_tool(self):
        self.sp.click_inspect_on_accessibility_tool()
    
    def click_what_to_select_dd(self):
        self.sp.click_what_to_select_dd()
    
    def click_entire_app_opt_in_dd(self):
        self.sp.click_entire_app_opt_in_dd()
    
    def press_ctrl_i_on_accessibility_tool(self):
        self.sp.press_ctrl_i_on_accessibility_tool()
    
    def press_alt_tab_on_accessibility_tool(self):
        self.sp.press_alt_tab_on_accessibility_tool()
        
    def verify_congratulations_msg_on_accessibility_tool_visible(self):
        return self.sp.verify_congratulations_msg_on_accessibility_tool_visible()
    
    def press_shift_f8_on_accessibility_tool(self):
        self.sp.press_shift_f8_on_accessibility_tool()
    
    def click_get_started_btn_on_accessibility_tool(self):
        self.sp.click_get_started_btn_on_accessibility_tool()

    def click_get_started_btn_on_tool(self):
        self.sp.click_get_started_btn_on_tool()

    def enter_search_box(self,text):
        self.sp.enter_search_box(text)

    def click_start_menu_search_box(self):
        self.sp.click_start_menu_search_box()
    
    def click_get_started_btn_on_accessibility_tool(self):
        self.sp.click_get_started_btn_on_accessibility_tool()

    def click_get_started_btn_on_tool(self):
        self.sp.click_get_started_btn_on_tool()

    def right_click_win_hp_app_item(self):
        self.sp.right_click_win_hp_app_item()

    def verify_win_hp_right_opt_display(self):
        self.sp.verify_win_hp_right_opt_display()

    def click_win_app_uninstall_btn(self):
        self.sp.click_win_app_uninstall_btn()

    def verify_win_app_uninstall_info_dialog(self):
        return self.sp.verify_win_app_uninstall_info_dialog()
    
    def click_win_app_uninstall_info_btn(self):
        self.sp.click_win_app_uninstall_info_btn()
    
    def get_windows_brightness_value(self):
        return self.sp.get_windows_brightness_value()

    def click_windows_battery_icon(self):
        self.sp.click_windows_battery_icon()
    
    def verify_windows_use_hdr_button_show(self):
        return self.sp.verify_windows_use_hdr_button_show()

    def minimize_windows_settings(self):
        self.sp.minimize_windows_settings()
    
    def windows_brightness_decrease(self, value):
        self.sp.windows_brightness_decrease(value)
    
    def windows_brightness_increase(self, value):
        self.sp.windows_brightness_increase(value)
    
    def click_windows_hdr_button(self):
        self.sp.click_windows_hdr_button()

    def get_windows_hdr_button_status(self):
        return self.sp.get_windows_hdr_button_status()
    
    def click_close_accessibility_tool(self):
        self.sp.click_close_accessibility_tool()
