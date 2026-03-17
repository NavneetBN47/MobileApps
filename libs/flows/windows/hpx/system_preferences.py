from typing import KeysView
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SystemPreferences(HPXFlow):
    flow_name = "system_preferences"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    # ----------------Windows Settings(Printers & Scanners)---------------- #

    def click_on_notification(self):
        self.driver.click("notification")

    def toggle_notification(self):
        self.driver.click("toggle_notification")

    def toggle_notification_state(self):
        return self.driver.get_attribute("toggle_notification", "Toggle.ToggleState")

    def verify_device_and_account_state(self):
        return self.driver.is_enable("device_and_account_btn")

    def verify_tips_and_tutorials_state(self):
        return self.driver.is_enable("tips_and_tutorials_btn")

    def verify_news_and_offers_state(self):
        return self.driver.is_enable("news_and_offers_btn")

    def verify_share_your_feedback_state(self):
        return self.driver.is_enable("share_your_feedback_btn")

    def click_news_and_offers(self):
        self.driver.click("news_and_offers_btn")

    def click_share_your_feedback(self):
        self.driver.click("share_your_feedback_btn")

    def click_external_link_to_navigate_sytem_notification(self):
        self.driver.click("external_link_to_navigate_back_to_system_notification_settings")

    def click_system_notification_close(self):
        self.driver.click("system_notification_close")

    def click_confirmation_pop_up(self):
        self.driver.click("title_bar_yes_button")

    def click_close_button(self):
        self.driver.click("close_app_button")

    def click_start_btn(self):
        self.driver.click("start_btn")

    def input_text_in_search_box(self, app_name):
        self.driver.wait_for_object("search_text_box", timeout=30)
        self.driver.send_keys("search_text_box", app_name)

    def input_text_in_aplicationsearch(self, app_name):
        self.driver.wait_for_object("aplicationsearch", timeout=30)
        self.driver.send_keys("aplicationsearch", app_name)

    def input_url_in_website_box(self, url):
        self.driver.wait_for_object("website_input", timeout=30)
        self.driver.send_keys("website_input", url)

    def verify_open_btn_on_HP(self):
        return self.driver.wait_for_object("open_btn_on_HP") is not False

    def click_close_On_Setting(self):
        self.driver.click("closeOnSetting")

    def click_myHP_app_On_Start(self):
        self.driver.click("myHP_app_On_Start")
    
    def click_app_setting_on_myHP(self):
        self.driver.click("app_setting_on_myHP")
    
    def get_app_name_in_app_setting(self):
        return self.driver.get_attribute("myHP_app_name_in_app_setting","Name")
    
    def get_app_version_in_app_setting(self):
        return self.driver.get_attribute("app_version_in_app_setting","Name")
    
    def get_app_size_in_app_setting(self):
        return self.driver.get_attribute("app_size_in_app_setting","Name")
    
    def verify_app_version_in_app_setting(self):
        return self.driver.wait_for_object("app_version_in_app_setting") is not False
    
    def verify_app_size(self):
        return self.driver.wait_for_object("app_size_in_app_setting") is not False
    
    def verify_reset_button(self):
        return self.driver.wait_for_object("reset_on_app_setting") is not False
    
    def verify_uninstall_btn_on_app_setting(self):
        return self.driver.wait_for_object("uninstall_btn_on_app_setting") is not False
    
    def click_hpx_folder_under_misx_bundle(self):
        self.driver.click("hpx_folder_under_misx_bundle")
        self.driver.send_keys("hpx_folder_under_misx_bundle",Keys.ENTER)
    
    def click_hpx_msix_bundle(self):
        self.driver.click("hpx_msix_bundle")
        self.driver.send_keys("hpx_msix_bundle",Keys.ENTER)
    
    def click_open_btn_on_HP(self):
        self.driver.click("open_btn_on_HP",timeout=15)
    
    def get_app_name_on_installer_window(self):
        return self.driver.get_attribute("app_name_on_installer_window","Name")
    
    def get_app_version(self):
        return self.driver.get_attribute("app_version","Name")
    
    def click_more_btn(self):
        self.driver.click("more_btn")
    
    def verify_app_capabilities(self):
        return self.driver.wait_for_object("app_capabilities") is not False
    
    def click_launch_btn(self):
        self.driver.click("launch_btn")
        self.driver.send_keys("launch_btn",Keys.ENTER)

    def click_on_search_box(self):
        self.driver.click("start_menu_search_box")

    def enter_text_on_search_box(self):
        self.driver.send_keys("start_menu_search_box","myHP")

    def click_on_open_tab_from_start_menu(self):
        self.driver.click("open_tab_from_Start_menu")
    
    def click_start_btn_taskbar(self):
        self.driver.click("start_btn")
        
    def verify_accessibility_tool_on_taskbar(self):
        return self.driver.wait_for_object("accessibility_tool_on_taskbar") is not False
    
    def click_inspect_on_accessibility_tool(self):
        self.driver.click("inspect_on_accessibility_tool")
    
    def click_what_to_select_dd(self):
        self.driver.click("what_to_select_dd")
    
    def click_entire_app_opt_in_dd(self):
        self.driver.click("entire_app_opt_in_dd")
    
    def press_ctrl_i_on_accessibility_tool(self):
        el=self.driver.wait_for_object("inspect_on_accessibility_tool")
        el.send_keys(Keys.CONTROL+"i")
    
    def press_alt_tab_on_accessibility_tool(self):
        el=self.driver.wait_for_object("inspect_on_accessibility_tool")
        el.send_keys(Keys.ALT, Keys.TAB)
    
    def press_shift_f8_on_accessibility_tool(self):
        el=self.driver.wait_for_object("inspect_on_accessibility_tool")
        el.send_keys(Keys.SHIFT, Keys.F8)
    
    def verify_congratulations_msg_on_accessibility_tool_visible(self):
        return self.driver.wait_for_object("congratulations_msg_on_accessibility_tool_visible", raise_e=False, timeout=5)
    
    def click_get_started_btn_on_accessibility_tool(self):
        self.driver.click("get_started_btn_on_accessibility_tool")

    def click_get_started_btn_on_tool(self):
        self.driver.click("get_started_on_tool")

    def enter_search_box(self,text):
        self.driver.send_keys("start_menu_search_box",text)

    def click_start_menu_search_box(self):
        self.driver.click("start_menu_search_box")
        self.driver.send_keys("start_menu_search_box",Keys.RETURN)
        
    def click_get_started_btn_on_accessibility_tool(self):
        self.driver.click("get_started_btn_on_accessibility_tool")

    def click_get_started_btn_on_tool(self):
        self.driver.click("get_started_on_tool")

    def verify_win_hp_right_opt_display(self):
        self.driver.wait_for_object("win_uninstall_btn")

    def verify_win_app_uninstall_info_dialog(self, raise_e=False, timeout=25):
        return self.driver.wait_for_object("win_uninstall_info_btn", raise_e=raise_e, timeout=timeout)
    
    def right_click_win_hp_app_item(self):
        el = self.driver.wait_for_object("win_my_hp_item")
        el.send_keys(Keys.SHIFT, Keys.F10)
    
    def click_win_app_uninstall_btn(self):
        self.driver.click("win_uninstall_btn", change_check={"wait_obj": "win_uninstall_info_btn"}, retry=6)

    def click_win_app_uninstall_info_btn(self):
        self.driver.click("win_uninstall_info_btn")

    def check_hp_app_exist(self, check_path):
        fh = self.driver.ssh.check_file(check_path)
        return fh

    def get_windows_brightness_value(self):
        return self.driver.get_attribute("windows_brightness","RangeValue.Value")
    
    def click_windows_battery_icon(self):
        self.driver.click("windows_battery_icon")
    
    def verify_windows_use_hdr_button_show(self):
        return self.driver.wait_for_object("windows_hdr_button", raise_e = False) is not False

    def minimize_windows_settings(self):
        self.driver.click("minimize_windows_settings")

    def windows_brightness_decrease(self, value):
        slider = self.driver.wait_for_object("windows_brightness", timeout = 10)
        for _ in range(value):
            slider.send_keys(Keys.LEFT)

    
    def windows_brightness_increase(self, value):
        slider = self.driver.wait_for_object("windows_brightness", timeout = 10)
        for _ in range(value):
            slider.send_keys(Keys.RIGHT)

    def click_windows_hdr_button(self):
        self.driver.click("windows_hdr_button")
    
    def get_windows_hdr_button_status(self):
        return self.driver.get_attribute("windows_hdr_button","Toggle.ToggleState")
    
    def click_close_accessibility_tool(self):
        self.driver.click("close_accessibility_tool")
