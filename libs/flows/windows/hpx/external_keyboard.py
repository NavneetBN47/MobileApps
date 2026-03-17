from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time
from selenium.webdriver.common.keys import Keys

class Keyboard(HPXFlow):
    flow_name = "external_keyboard"

    def get_title_text(self):
        return self.driver.wait_for_object("keyboard_title").get_attribute("Name")
    
    def click_title(self):
        self.driver.click("keyboard_title")
    
    def click_battery_icon(self):
        self.driver.click("keyboard_des_text")
    
    def get_title_tooltips_text(self):
        return self.driver.wait_for_object("keyboard_title_tootlips").get_attribute("Name")
    
    def get_keyboard_des_text(self):
        return self.driver.wait_for_object("keyboard_des_text").get_attribute("Name")
    
    def verify_battery_icon_show(self):
        return self.driver.wait_for_object("battery_icon", raise_e=False, timeout=10) is not False
    
    def verify_info_icon_show(self):
        return self.driver.wait_for_object("keyboard_info_icon", raise_e=False, timeout=10) is not False
    
    def click_info_icon(self):
        return self.driver.click("keyboard_info_icon")
    
    def get_lighting_setup_text(self):
        return self.driver.wait_for_object("lighting_setup").get_attribute("Name")
    
    def get_proximity_sensor_text(self):
        return self.driver.wait_for_object("proximity_sensor").get_attribute("Name")
    
    def get_backlight_auto_adjust_text(self):
        return self.driver.wait_for_object("backlight_auto_adjust").get_attribute("Name")
    
    def get_restore_button_text(self):
        return self.driver.wait_for_object("restore_button").get_attribute("Name")
    
    def click_rename_icon(self):
        return self.driver.click("keyboard_rename_btn")
    
    def verify_keyboard_module_show(self):
        return self.driver.wait_for_object("keyboard_title", raise_e=False, timeout=10) is not False
    
    def verify_production_number_show(self):
        return self.driver.wait_for_object("production_number", raise_e=False, timeout=10) is not False
    
    def verify_serial_number_show(self):
        return self.driver.wait_for_object("serial_number", raise_e=False, timeout=10) is not False
    
    def verify_firmware_version_show(self):
        return self.driver.wait_for_object("firmware_version", raise_e=False, timeout=10) is not False
    
    def verify_production_number_text_show(self):
        return self.driver.wait_for_object("production_number_text", raise_e=False, timeout=10) is not False
    
    def verify_serial_number_text_show(self):
        return self.driver.wait_for_object("serial_number_text", raise_e=False, timeout=10) is not False
    
    def verify_firmware_version_text_show(self):
        return self.driver.wait_for_object("firmware_version_text", raise_e=False, timeout=10) is not False
    
    def enter_device_name(self, text):
        self.driver.wait_for_object("device_name_input", timeout=10)
        self.driver.send_keys("device_name_input", text)
        el = self.driver.wait_for_object("device_name_input", displayed=False, timeout=3)
        time.sleep(3)
        el.send_keys(Keys.ENTER)
    
    def click_proximity_sensor_btn(self):
        self.driver.click("proximity_sensor_btn")
    
    def click_backlight_adjust_btn(self):
        self.driver.click("backlight_adjust_btn")
    
    def verify_proximity_sensor_btn_status(self):
        return self.driver.wait_for_object("proximity_sensor_btn").get_attribute("Toggle.ToggleState")
    
    def verify_backlight_adjust_btn_status(self):
        return self.driver.wait_for_object("backlight_adjust_btn").get_attribute("Toggle.ToggleState")
    
    def click_proximity_sensor_tootips_btn(self):
        self.driver.click("proximity_sensor_tootips")
    
    def click_backlight_adjust_tooltips_btn(self):
        self.driver.click("backlight_adjust_tooltips")
    
    def verify_proximity_sensor_tootips_message1(self):
        return self.driver.wait_for_object("proximity_tooltip_message1").get_attribute("Name")
    
    def verify_proximity_sensor_tootips_message2(self):
        return self.driver.wait_for_object("proximity_tooltip_message2").get_attribute("Name")
    
    def verify_backlight_adjust_tooltips_message1(self):
        return self.driver.wait_for_object("backlight_tooltip_message1").get_attribute("Name")
    
    def verify_backlight_adjust_tooltips_message2(self):
        return self.driver.wait_for_object("backlight_tooltip_message2").get_attribute("Name")
    
    def close_proximity_sensor_tootips(self):
        self.driver.click("proximity_tooltip_close")
    
    def set_time_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.RIGHT)

    def set_time_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.LEFT)
    
    def set_brightness_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.RIGHT)

    def set_brightness_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.LEFT)
    
    def get_time_slider_value(self):
        return self.driver.wait_for_object("time_slider").get_attribute("RangeValue.Value")
    
    def get_brightness_slider_value(self):
        return self.driver.wait_for_object("brightness_slider").get_attribute("RangeValue.Value")
    
    def click_restore_button(self):
        self.driver.click("restore_button")

    def click_runas_admin(self):
        self.driver.click("runas_admin")

    def click_close_cmd_console(self):
        self.driver.click("close_cmd_window")

    def verify_update_firmware_toast_notification_pop_up(self):
        return self.driver.get_attribute("update_firmware_toast_window","Name")
    
    def verify_update_firmware_button(self):
        return self.driver.get_attribute("update_firmware_button","Name")
        
    def verify_open_myhp_firmware_button(self):
        return self.driver.get_attribute("open_myhp_firmware_button","Name")
    
    def click_open_myhp_firmware_button(self):
        self.driver.click("click_open_myhp_firmware_button")

    def get_toast_notification_title(self):
        return self.driver.get_attribute("toast_notification_title","Name")
      
    def get_dismiss_button_on_toast_notification(self):
        return self.driver.get_attribute("dismiss_button_on_toast_notification","Name")
    
    def click_dismiss_button_on_toast_notification(self):
        self.driver.click("dismiss_button_on_toast_notification")

    def click_update_now_button_in_the_app(self):
        self.driver.click("update_now_button_in_the_app")

    def get_update_now_button_in_the_app(self):
        return self.driver.get_attribute("update_now_button_in_the_app","Name")

    def click_ok_to_close_console_popup(self):
        self.driver.send_keys("pop_up_after_console_close", Keys.ENTER)  
    
    def get_firmware_version_text_show(self):
        return self.driver.get_attribute("firmware_version_text", "Name")
            
    def verify_update_now_button_in_the_app(self):
        return self.driver.wait_for_object("update_now_button_in_the_app",raise_e=False, timeout=10) is not False
    
    def verify_open_myhp_firmware_button_present(self):  
        return self.driver.wait_for_object("open_myhp_firmware_button", raise_e=False, timeout=10) is not False
    
    def hover_usb_connection_tooltip(self):
        self.driver.hover("usb_connection_tooltip", x_offset=24, y_offset=24)
    
    def get_usb_connection_tooltip(self):
        return self.driver.wait_for_object("usb_connection_tooltip").get_attribute("Name")
    
    def hover_mute_key(self):
        self.driver.hover("mute_key", x_offset=24, y_offset=24)
    
    def get_mute_key_text(self):
        return self.driver.wait_for_object("mute_key").get_attribute("Name")
    
    def hover_volume_down_key(self):
        self.driver.hover("volume_down_key", x_offset=24, y_offset=24)
    
    def get_volume_down_key_text(self):
        return self.driver.wait_for_object("volume_down_key").get_attribute("Name")
    
    def hover_volume_up_key(self):
        self.driver.hover("volume_up_key", x_offset=24, y_offset=24)
    
    def get_volume_up_key_text(self):
        return self.driver.wait_for_object("volume_up_key").get_attribute("Name")
    
    def hover_previous_track_key(self):
        self.driver.hover("previous_track_key", x_offset=24, y_offset=24)
    
    def get_previous_track_key_text(self):
        return self.driver.wait_for_object("previous_track_key").get_attribute("Name")
    
    def hover_play_pause_key(self):
        self.driver.hover("play_pause_key", x_offset=24, y_offset=24)
    
    def get_play_pause_key_text(self):
        return self.driver.wait_for_object("play_pause_key").get_attribute("Name")
    
    def hover_next_track_key(self):
        self.driver.hover("next_track_key", x_offset=24, y_offset=24)
    
    def get_next_track_key_text(self):
        return self.driver.wait_for_object("next_track_key").get_attribute("Name")
    
    def hover_screen_brightness_down_key(self):
        self.driver.hover("screen_brightness_down_key", x_offset=24, y_offset=24)
    
    def get_screen_brightness_down_key_text(self):
        return self.driver.wait_for_object("screen_brightness_down_key").get_attribute("Name")
    
    def hover_screen_brightness_up_key(self):
        self.driver.hover("screen_brightness_up_key", x_offset=24, y_offset=24)
    
    def get_screen_brightness_up_key_text(self):
        return self.driver.wait_for_object("screen_brightness_up_key").get_attribute("Name")
    
    def hover_new_window_key(self):
        self.driver.hover("new_window", x_offset=24, y_offset=24)
    
    def get_new_window_key_text(self):
        return self.driver.wait_for_object("new_window").get_attribute("Name")
    
    def hover_window_settings_key(self):
        self.driver.hover("window_settings_key", x_offset=24, y_offset=24)
    
    def get_window_settings_key_text(self):
        return self.driver.wait_for_object("window_settings_key").get_attribute("Name")
    
    def hover_switch_screen_key(self):
        self.driver.hover("switch_screen_key", x_offset=24, y_offset=24)
    
    def get_switch_screen_key_text(self):
        return self.driver.wait_for_object("switch_screen_key").get_attribute("Name")
    
    def hover_windows_search_key(self):
        self.driver.hover("windows_search_key", x_offset=24, y_offset=24)
    
    def get_windows_search_key_text(self):
        return self.driver.wait_for_object("windows_search_key").get_attribute("Name")
    
    def hover_mic_mute_key(self):
        self.driver.hover("mic_mute_key", x_offset=24, y_offset=24)
    
    def get_mic_mute_key_text(self):
        return self.driver.wait_for_object("mic_mute_key").get_attribute("Name")
    
    def hover_keyboard_backlight_key(self):
        self.driver.hover("keyboard_backlight_key", x_offset=24, y_offset=24)
    
    def get_keyboard_backlight_key_text(self):
        return self.driver.wait_for_object("keyboard_backlight_key").get_attribute("Name")
    
    def hover_desktop_show_hide_key(self):
        self.driver.hover("desktop_show_hide_key", x_offset=24, y_offset=24)
    
    def get_desktop_show_hide_key_text(self):
        return self.driver.wait_for_object("desktop_show_hide_key").get_attribute("Name")
    
    def hover_action_center_key(self):
        self.driver.hover("action_center_key", x_offset=24, y_offset=24)
    
    def get_action_center_key_text(self):
        return self.driver.wait_for_object("action_center_key").get_attribute("Name")
    
    def hover_lock_key(self):
        self.driver.hover("lock_key", x_offset=24, y_offset=24)
    
    def get_lock_key_text(self):
        return self.driver.wait_for_object("lock_key").get_attribute("Name")
    
    def hover_insert_key(self):
        self.driver.hover("insert_key", x_offset=24, y_offset=24)
    
    def get_insert_key(self):
        return self.driver.wait_for_object("insert_key").get_attribute("Name")
    
    def hover_home_key(self):
        self.driver.hover("home_key", x_offset=24, y_offset=24)
    
    def get_home_key(self):
        return self.driver.wait_for_object("home_key").get_attribute("Name")
    
    def hover_page_up_key(self):
        self.driver.hover("page_up_key", x_offset=24, y_offset=24)
    
    def get_page_up_key(self):
        return self.driver.wait_for_object("page_up_key").get_attribute("Name")
    
    def hover_delete_key(self):
        self.driver.hover("delete_key", x_offset=24, y_offset=24)
    
    def get_delete_key(self):
        return self.driver.wait_for_object("delete_key").get_attribute("Name")
    
    def hover_end_key(self):
        self.driver.hover("end_key", x_offset=24, y_offset=24)
    
    def get_end_key(self):
        return self.driver.wait_for_object("end_key").get_attribute("Name")
    
    def hover_page_down_key(self):
        self.driver.hover("page_down_key", x_offset=24, y_offset=24)
    
    def get_page_down_key(self):
        return self.driver.wait_for_object("page_down_key").get_attribute("Name")
    
    def click_fn_key(self):
        self.driver.click("fn_key")
    
    def get_fn_key_title_text(self):
        return self.driver.wait_for_object("fn_key_title").get_attribute("Name")
    
    def click_fn_key_tooltip_icon(self):
        self.driver.click("fn_key_tooltip_icon")
    
    def get_fn_key_tooltip_text(self):
        return self.driver.wait_for_object("fn_key_tooltip_icon").get_attribute("Name")
    
    def get_function_lock_on_start(self):
        return self.driver.wait_for_object("function_lock_on_start").get_attribute("Name")
    
    def click_function_lock_on_start_tooltip_icon(self):
        self.driver.click("function_lock_on_start_tooltip_icon")
    
    def get_function_lock_on_start_tooltip_icon(self):
        return self.driver.wait_for_object("function_lock_on_start_tooltip_icon").get_attribute("Name")
    
    def get_function_lock(self):
        return self.driver.wait_for_object("function_lock").get_attribute("Name")
    
    def click_function_lock_tooltip_icon(self):
        self.driver.click("function_lock_tooltip_icon")
    
    def get_function_lock_tooltip_icon(self):
        return self.driver.wait_for_object("function_lock_tooltip_icon").get_attribute("Name")
    
    def get_fn_key_text(self):
        return self.driver.wait_for_object("fn_key_title_text").get_attribute("Name")
    
    def get_function_key_lock_on_start_toggle_status(self):
        return self.driver.get_attribute("function_key_lock_on_start_toggle","Toggle.ToggleState")
    
    def get_function_key_lock_toggle_status(self):
        return self.driver.get_attribute("function_key_lock_toggle","Toggle.ToggleState")
    
    def click_fn_key_lock_on_start_toggle(self):
        self.driver.click("function_key_lock_on_start_toggle")

    def click_fn_key_lock_toggle(self):
        self.driver.click("function_key_lock_toggle")

    def click_mute_key_to_open_side_panel(self):
        self.driver.click("mute_key")        
    
    def get_fn_key_text_on_side_panel(self):
        self.driver.get_attribute("fn_key_text_on_side_panel","Name")

    def click_more_tab_on_side_panel(self):
        self.driver.click("more_text_on_side_panel")   

    def scroll_down_with_tab(self, element):
        el = self.driver.wait_for_object("side_panel_window_to_scroll", displayed=False, timeout=3)
        for _ in range(50):
            el.send_keys(Keys.ARROW_DOWN)
            if (self.driver.wait_for_object(element, raise_e=False, timeout=1)):
                break  

    def scroll_up_with_tab(self, element):
        el = self.driver.wait_for_object("side_panel_window_to_scroll", displayed=False, timeout=3)
        for _ in range(50):
            el.send_keys(Keys.ARROW_UP)
            if (self.driver.wait_for_object(element, raise_e=False, timeout=1)):
                break               
    
    def get_productivity_text_on_side_panel(self):
        return self.driver.get_attribute("productivity_text_on_side_panel","Name",timeout=20)

    def click_productivity_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("productivity_collapse_button_side_panel","Name", timeout= 10,raise_e=False) == "Collapse":
            self.driver.click("productivity_collapse_button_side_panel")

    def click_productivity_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("productivity_expand_button_side_panel","Name", timeout= 10,raise_e=False) == "Expand":
            self.driver.click("productivity_expand_button_side_panel")

    def get_copy_text_on_side_panel(self):
        return self.driver.get_attribute("copy_text_on_side_panel","Name")

    def get_cut_text_on_side_panel(self):
        return self.driver.get_attribute("cut_text_on_side_panel","Name")

    def get_paste_text_on_side_panel(self):
        return self.driver.get_attribute("paste_text_on_side_panel","Name")

    def get_undo_text_on_side_panel(self):
        return self.driver.get_attribute("undo_text_on_side_panel","Name")
    
    def get_redo_text_on_side_panel(self):
        return self.driver.get_attribute("redo_text_on_side_panel","Name")

    def get_more_text_on_side_panel(self):
        return self.driver.get_attribute("more_text_on_side_panel","Name")

    def get_select_all_text_on_side_panel(self):
        return self.driver.get_attribute("select_all_text_on_side_panel","Name")

    def get_print_text_on_side_panel(self):
        return self.driver.get_attribute("print_text_on_side_panel","Name")

    def get_zoom_in_text_on_side_panel(self):
        return self.driver.get_attribute("zoom_in_text_on_side_panel","Name")

    def get_zoom_out_text_on_side_panel(self):
        return self.driver.get_attribute("zoom_out_text_on_side_panel","Name")

    def get_page_up_text_on_side_panel(self):
        return self.driver.get_attribute("page_up_text_on_side_panel","Name")

    def get_page_down_text_on_side_panel(self):
        return self.driver.get_attribute("page_down_text_on_side_panel","Name")

    def get_find_text_on_side_panel(self):
        return self.driver.get_attribute("find_text_on_side_panel","Name")

    def get_back_text_on_side_panel(self):
        return self.driver.get_attribute("back_text_on_side_panel","Name")

    def get_forward_text_on_side_panel(self):
        return self.driver.get_attribute("forward_text_on_side_panel","Name")

    def get_refresh_reload_text_on_side_panel(self):
        return self.driver.get_attribute("refresh_reload_text_on_side_panel","Name")

    def get_print_screen_text_on_side_panel(self):
        return self.driver.get_attribute("print_screen_text_on_side_panel","Name")

    def get_action_center_text_on_side_panel(self):
        return self.driver.get_attribute("action_center_text_on_side_panel","Name")

    def get_media_control_text_on_side_panel(self):
        return self.driver.get_attribute("media_control_text_on_side_panel","Name")

    def click_media_control_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("media_control_collapsed_button_side_panel","Name", timeout= 10, raise_e=False) == "Collapse":
            self.driver.click("media_control_collapsed_button_side_panel")

    def click_media_control_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("media_control_expand_button_side_panel","Name", timeout= 10, raise_e=False) == "Expand":
           self.driver.click("media_control_expand_button_side_panel")

    def get_volume_up_text_on_side_panel(self):
        return self.driver.get_attribute("volume_up_text_on_side_panel","Name")

    def get_volume_down_text_on_side_panel(self):
        return self.driver.get_attribute("volume_down_text_on_side_panel","Name")

    def get_play_pause_text_on_side_panel(self):
        return self.driver.get_attribute("play_pause_text_on_side_panel","Name")

    def get_previous_track_text_on_side_panel(self):
        return self.driver.get_attribute("previous_track_text_on_side_panel","Name")

    def get_next_track_text_on_side_panel(self):
        return self.driver.get_attribute("next_track_text_on_side_panel","Name")

    def get_mute_text_on_side_panel(self):
        return self.driver.get_attribute("mute_text_on_side_panel","Name")

    def get_mic_mute_text_on_side_panel(self):
        return self.driver.get_attribute("mic_mute_text_on_side_panel","Name")

    def get_app_and_file_text_on_side_panel(self):
        return self.driver.get_attribute("app_and_file_text_on_side_panel","Name")

    def click_app_and_files_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("app_and_files_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("app_and_files_collapsed_button_side_panel")

    def click_app_and_files_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("app_and_files_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("app_and_files_expand_button_side_panel")

    def get_open_file_text_on_side_panel(self):
        return self.driver.get_attribute("open_file_text_on_side_panel","Name")

    def get_file_save_text_on_side_panel(self):
        return self.driver.get_attribute("file_save_text_on_side_panel","Name")

    def get_open_folder_text_on_side_panel(self):
        return self.driver.get_attribute("open_folder_text_on_side_panel","Name")

    def get_documents_text_on_side_panel(self):
        return self.driver.get_attribute("documents_text_on_side_panel","Name")

    def get_download_folder_text_on_side_panel(self):
        return self.driver.get_attribute("download_folder_text_on_side_panel","Name")

    def get_pictures_text_on_side_panel(self):
        return self.driver.get_attribute("pictures_text_on_side_panel","Name")

    def get_videos_text_on_side_panel(self):
        return self.driver.get_attribute("videos_text_on_side_panel","Name")

    def get_calculator_text_on_side_panel(self):
        return self.driver.get_attribute("calculator_text_on_side_panel","Name")

    def get_system_text_on_side_panel(self):
        return self.driver.get_attribute("system_text_on_side_panel","Name")

    def click_system_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("system_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("system_collapsed_button_side_panel")
       
    def click_system_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("system_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("system_expand_button_side_panel")

    def get_lock_text_on_side_panel(self):
        return self.driver.get_attribute("lock_text_on_side_panel","Name")

    def get_sleep_text_on_side_panel(self):
        return self.driver.get_attribute("sleep_text_on_side_panel","Name")

    def get_shutdown_text_on_side_panel(self):
        return self.driver.get_attribute("shutdown_text_on_side_panel","Name")

    def get_restart_text_on_side_panel(self):
        return self.driver.get_attribute("restart_text_on_side_panel","Name")

    def get_signout_text_on_side_panel(self):
        return self.driver.get_attribute("signout_text_on_side_panel","Name")

    def get_screen_brightness_plus_text_on_side_panel(self):
        return self.driver.get_attribute("screen_brightness_plus_text_on_side_panel","Name")

    def get_screen_brightness_minus_text_on_side_panel(self):
        return self.driver.get_attribute("screen_brightness_minus_text_on_side_panel","Name")

    def get_windows_search_text_on_side_panel(self):
        return self.driver.get_attribute("windows_search_text_on_side_panel","Name")

    def get_windows_settings_text_on_side_panel(self):
        return self.driver.get_attribute("windows_settings_text_on_side_panel","Name")

    def get_switch_language_text_on_side_panel(self):
        return self.driver.get_attribute("switch_language_text_on_side_panel","Name")

    def get_this_computer_text_on_side_panel(self):
        return self.driver.get_attribute("this_computer_text_on_side_panel","Name")
    
    def get_windows_management_text_on_side_panel(self):
        return self.driver.get_attribute("windows_management_text_on_side_panel","Name")

    def click_windows_management_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("windows_management_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("windows_management_collapsed_button_side_panel")

    def click_windows_management_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("windows_management_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("windows_management_expand_button_side_panel")

    def get_maximize_window_text_on_side_panel(self):
        return self.driver.get_attribute("maximum_window_text_on_side_panel","Name")

    def get_minimize_window_text_on_side_panel(self):
        return self.driver.get_attribute("minimum_window_text_on_side_panel","Name")

    def get_close_window_text_on_side_panel(self):
        return self.driver.get_attribute("close_window_text_on_side_panel","Name")

    def get_new_window_text_on_side_panel(self):
        return self.driver.get_attribute("new_window_text_on_side_panel","Name")

    def get_snap_left_text_on_side_panel(self):
        return self.driver.get_attribute("snap_left_text_on_side_panel","Name")

    def get_snap_right_text_on_side_panel(self):
        return self.driver.get_attribute("snap_right_text_on_side_panel","Name")

    def get_desktop_show_hide_text_on_side_panel(self):
        return self.driver.get_attribute("desktop_show_hide_text_on_side_panel","Name")

    def get_switch_apps_text_on_side_panel(self):
        return self.driver.get_attribute("switch_apps_text_on_side_panel","Name")

    def get_switch_screen_text_on_side_panel(self):
        return self.driver.get_attribute("switch_screen_text_on_side_panel","Name")

    def get_task_view_text_on_side_panel(self):
        return self.driver.get_attribute("task_view_text_on_side_panel","Name")

    def get_desktop_next_text_on_side_panel(self):
        return self.driver.get_attribute("desktop_next_text_on_side_panel","Name")

    def get_desktop_previous_text_on_side_panel(self):
        return self.driver.get_attribute("desktop_previous_text_on_side_panel","Name")

    def get_start_menu_text_on_side_panel(self):
        return self.driver.get_attribute("start_menu_text_on_side_panel","Name")

    def get_web_browsing_text_on_side_panel(self):
        return self.driver.get_attribute("web_browsing_text_on_side_panel","Name")

    def click_web_browsing_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("web_browsing_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("web_browsing_collapsed_button_side_panel")

    def click_web_browsing_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("web_browsing_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("web_browsing_expand_button_side_panel") 

    def get_web_browsing_home_text_on_side_panel(self):
        return self.driver.get_attribute("home_text_on_side_panel","Name") 

    def get_web_browsing_web_search_text_on_side_panel(self):
        return self.driver.get_attribute("web_search_text_on_side_panel","Name") 

    def get_web_browsing_open_new_tab_text_on_side_panel(self):
        return self.driver.get_attribute("open_new_tab_page_text_on_side_panel","Name")

    def get_web_browsing_close_tab_text_on_side_panel(self):
        return self.driver.get_attribute("close_tab_page_text_on_side_panel","Name") 

    def get_web_browsing_switch_between_open_tabs_text_on_side_panel(self):
        return self.driver.get_attribute("switch_between_open_tabs_text_on_side_panel","Name")                            

    def get_web_browsing_toggle_full_screen_tabs_text_on_side_panel(self):
        return self.driver.get_attribute("toggle_fullscreen_window_text_on_side_panel","Name") 

    def get_web_browsing_save_page_as_bookmark_text_on_side_panel(self):
        return self.driver.get_attribute("save_page_as_bookmark_text_on_side_panel","Name")

    def get_keyboard_text_on_side_panel(self):
        return self.driver.get_attribute("keyboard_text_on_side_panel","Name") 

    def click_keyboard_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("keyboard_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("keyboard_collapsed_button_side_panel")

    def click_keyboard_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("keyboard_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("keyboard_expand_button_side_panel")

    def get_key_f1_text_on_side_panel(self):
       return self.driver.get_attribute("key_f1_text_on_side_panel","Name")     

    def get_key_f2_text_on_side_panel(self):
        return self.driver.get_attribute("key_f2_text_on_side_panel","Name")    

    def get_key_f3_text_on_side_panel(self):
        return self.driver.get_attribute("key_f3_text_on_side_panel","Name")

    def get_key_f4_text_on_side_panel(self):
        return self.driver.get_attribute("key_f4_text_on_side_panel","Name") 

    def get_key_f5_text_on_side_panel(self):
        return self.driver.get_attribute("key_f5_text_on_side_panel","Name")

    def get_key_f6_text_on_side_panel(self):
        return self.driver.get_attribute("key_f6_text_on_side_panel","Name")    

    def get_key_f7_text_on_side_panel(self):
        return self.driver.get_attribute("key_f7_text_on_side_panel","Name")

    def get_key_f8_text_on_side_panel(self):
        return self.driver.get_attribute("key_f8_text_on_side_panel","Name")

    def get_key_f9_text_on_side_panel(self):
        return self.driver.get_attribute("key_f9_text_on_side_panel","Name")

    def get_key_f10_text_on_side_panel(self):
        return self.driver.get_attribute("key_f10_text_on_side_panel","Name") 

    def get_key_f11_text_on_side_panel(self):
        return self.driver.get_attribute("key_f11_text_on_side_panel","Name")     

    def get_key_f12_text_on_side_panel(self):
        return self.driver.get_attribute("key_f12_text_on_side_panel","Name")   

    def get_key_insert_text_on_side_panel(self):
        return self.driver.get_attribute("key_insert_text_on_side_panel","Name") 

    def get_key_home_text_on_side_panel(self):
        return self.driver.get_attribute("key_home_text_on_side_panel","Name")     

    def get_key_page_up_text_on_side_panel(self):
        return self.driver.get_attribute("key_page_up_text_on_side_panel","Name")    

    def get_key_delete_up_text_on_side_panel(self):
        return self.driver.get_attribute("key_delete_up_text_on_side_panel","Name")

    def get_key_end_up_text_on_side_panel(self):
        return self.driver.get_attribute("key_end_up_text_on_side_panel","Name") 
    
    def get_key_page_down_up_text_on_side_panel(self):
        return self.driver.get_attribute("key_page_down_text_on_side_panel","Name")
    
    def get_key_scrlk_text_on_side_panel(self):
        return self.driver.get_attribute("key_scrlk_text_on_side_panel","Name")
    
    def get_mouse_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_text_on_side_panel","Name") 

    def click_mouse_collapsed_button_to_expand_side_panel(self):
        if self.driver.get_attribute("mouse_collapsed_button_side_panel","Name", timeout= 20, raise_e=False) == "Collapse":
            self.driver.click("mouse_collapsed_button_side_panel")

    def click_mouse_expand_button_to_collapse_side_panel(self):
        if self.driver.get_attribute("mouse_expand_button_side_panel","Name", timeout= 20, raise_e=False) == "Expand":
            self.driver.click("mouse_expand_button_side_panel")

    def get_double_click_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_double_click_text_side_panel","Name")   

    def get_right_click_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_right_click_text_side_panel","Name")

    def get_middle_click_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_middle_click_text_side_panel","Name") 

    def get_scroll_left_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_scroll_left_text_side_panel","Name")

    def get_scroll_right_text_on_side_panel(self):
        return self.driver.get_attribute("mouse_scroll_right_text_side_panel","Name")
    
    def click_productnumber_copy_icon(self):
        self.driver.click("production_number_text", timeout = 10)

    def click_serialnumber_copy_icon(self):
        self.driver.click("serial_number_text", timeout = 10)

    def get_productnumber_copy_text(self):
        return self.driver.get_attribute("product_number_copied_tooltip","Name")

    def get_serialnumber_copy_text(self):
        return self.driver.get_attribute("serial_number_copied_tooltip","Name")
    
    def enter_text_in_search_box(self, text):
        self.driver.click("search_txt_box")
        if self.driver.get_attribute("search_txt_box","Value.Value") != "":
            self.driver.wait_for_object("search_txt_box").clear()
        self.driver.send_keys("search_txt_box", text)

    def verify_search_txt_box(self):
        return self.driver.wait_for_object("search_txt_box", raise_e=False, timeout=10) is not False
    
    def verify_fn_key_text_on_side_panel(self):
        return self.driver.wait_for_object("fn_key_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_productivity_text_on_side_panel(self):
        return self.driver.wait_for_object("productivity_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_copy_text_on_side_panel(self):
        return self.driver.wait_for_object("copy_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_cut_text_on_side_panel(self):
        return self.driver.wait_for_object("cut_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_paste_text_on_side_panel(self):
        return self.driver.wait_for_object("paste_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_undo_text_on_side_panel(self):
        return self.driver.wait_for_object("undo_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_redo_text_on_side_panel(self):
        return self.driver.wait_for_object("redo_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_more_text_on_side_panel(self):
        return self.driver.wait_for_object("more_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_media_control_text_on_side_panel(self):
        return self.driver.wait_for_object("media_control_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_app_and_file_text_on_side_panel(self):
        return self.driver.wait_for_object("app_and_file_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_open_file_text_on_side_panel(self):
        return self.driver.wait_for_object("open_file_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_file_save_text_on_side_panel(self):
        return self.driver.wait_for_object("file_save_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_open_folder_text_on_side_panel(self):
        return self.driver.wait_for_object("open_folder_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_documents_text_on_side_panel(self):
        return self.driver.wait_for_object("documents_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_keyboard_text_on_side_panel(self):
        return self.driver.wait_for_object("keyboard_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_key_f1_text_on_side_panel(self):
        return self.driver.wait_for_object("key_f1_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_key_f10_text_on_side_panel(self):
        return self.driver.wait_for_object("key_f10_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_key_f11_text_on_side_panel(self):
        return self.driver.wait_for_object("key_f11_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_key_f12_text_on_side_panel(self):
        return self.driver.wait_for_object("key_f12_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_download_folder_text_on_side_panel(self):
        return self.driver.wait_for_object("download_folder_text_on_side_panel", raise_e=False, timeout=10) is not False
    
    def verify_Cannot_find_the_action_txt(self):
        return self.driver.wait_for_object("Cannot_find_the_action_txt", raise_e=False, timeout=10) is not False
    
    def click_x_on_search_txt_box(self):
        self.driver.wait_for_object("search_txt_box").clear()
    
    def verify_keyboard_new_pop_message(self):
        return self.driver.wait_for_object("new_pop_widonws_title", raise_e=False, timeout=10) is not False
