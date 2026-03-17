import logging
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.keys import Keys
import time

class DisplayControl(HPXFlow):
    flow_name = "display_control"

    def verify_myhp_logo_is_present(self):
        return self.driver.wait_for_object("myHP_logo") is not False

    def verify_pcdevices_title(self):
        return self.driver.get_attribute("pc_devices_navigation_text","Name")

    def verify_pcdevices_display_title(self):
        return self.driver.get_attribute("display_title","Name")

    def verify_brightness_contrast_label(self):
        return self.driver.get_attribute("Brightness_contrast","Name")

    def verify_brightness_slider_is_present(self):
        return self.driver.wait_for_object("Brightness_slider", timeout = 30) is not False

    def verify_contrast_slider_is_present(self):
        return self.driver.wait_for_object("Contrast_slider", timeout = 30) is not False

    def verify_restore_default_button(self):
        return self.driver.get_attribute("Restore_default","Name", timeout = 30)

    def verify_display_modes_title(self):
        return self.driver.get_attribute("Display_modes_title","Name")

    def verify_standard_title(self):
        return self.driver.get_attribute("Standard_title","Name")

    def verify_default_tile(self):
        return self.driver.get_attribute("Default_tile","Name")

    def verify_work_tile(self):
        return self.driver.get_attribute("Work_tile","Name")

    def verify_low_light_tile(self):
        return self.driver.get_attribute("Low_Light_tile","Name")

    def verify_entertainment_tile(self):
        return self.driver.get_attribute("Entertainment_tile","Name")

    def verify_low_blue_light_tile(self):
        return self.driver.get_attribute("Low_blue_light_tile","Name")

    def verify_advanced_title(self):
        return self.driver.get_attribute("Advanced_Title","Name")

    def verify_sRGB_web_tile(self):
        return self.driver.get_attribute("sRGB_Web_tile","Name")

    def verify_adobe_RGB_tile(self):
        return self.driver.get_attribute("Adobe_RGB_tile","Name")

    def verify_display_p3__tile(self):
        return self.driver.get_attribute("Display_P3_tile","Name")

    def verify_native_tile(self):
        return self.driver.get_attribute("Native_tile","Name", timeout = 15)

    def verify_low_blue_light_scheduler_title(self):
        return self.driver.get_attribute("Low_Blue_Light_Scheduler_Title","Name")

    def click_low_blue_light_scheduler_title(self):
        return self.driver.click("Low_Blue_Light_Scheduler_Title")

    def verify_low_blue_light_scheduler_modal_title(self):
        return self.driver.get_attribute("Low_Blue_Light_Scheduler_Modal_Title","Name")

    def verify_low_blue_light_scheduler_modal_subtitle(self):
        return self.driver.get_attribute("Low_Blue_Light_Scheduler_Modal_SubTitle","Name")

    def verify_schedule_title(self):
        return self.driver.get_attribute("Schedule_Title","Name")

    def verify_schedule_toggle_is_present(self):
        return self.driver.wait_for_object("Schedule_Toggle") is not False

    def click_schedule_toggle_turn_on(self):
        self.driver.click("Schedule_Toggle")

    def click_schedule_toggle_turn_off(self):
        self.driver.click("Schedule_Toggle")

    def toggle_notification_state(self):
        return self.driver.get_attribute("Schedule_Toggle","Toggle.ToggleState")

    def verify_turn_on_text(self):
        return self.driver.get_attribute("Turn_On_Text","Name")

    def verify_turn_off_text(self):
        return self.driver.get_attribute("Turn_Off_Text","Name")

    def verify_save_button(self):
        return self.driver.get_attribute("Save_Button","Name")

    def click_save_button(self):
        return self.driver.click("Save_Button")

    def verify_cancel_button(self):
        return self.driver.get_attribute("Cancel_Button","Name")

    def click_cancel_button(self):
        return self.driver.click("Cancel_Button")

    def click_restore_default_button(self):
        self.driver.click("Restore_default", timeout = 20)
        time.sleep(5)
        if bool(self.driver.wait_for_object("restore_factory_settings_continue", raise_e=False, timeout = 10)) == True:
            self.driver.click("restore_factory_settings_continue")

    def verify_display_control_module(self):
        return self.driver.wait_for_object("pc_devices_navigation_text", raise_e=False, timeout=5)
        
    def verify_standard_mode(self):
        return self.driver.wait_for_object("Standard_title", raise_e=False, timeout=5)
           
    def verify_default_mode(self):
        return self.driver.wait_for_object("Default_tile", raise_e=False, timeout=5)
          
    def verify_work_mode(self):
        return self.driver.wait_for_object("Work_tile",raise_e=False, timeout=5)
 
    def verify_low_light_mode(self):
        return self.driver.wait_for_object("Low_Light_tile",raise_e=False, timeout=5)
               
    def verify_entertainment_mode(self):
        return self.driver.wait_for_object("Entertainment_tile", raise_e=False, timeout=5)
    
    def verify_low_blue_light_mode(self):
        return self.driver.wait_for_object("Low_blue_light_tile",raise_e=False, timeout=5)
          
    def verify_advanced_mode(self):
        return self.driver.wait_for_object("Advanced_Title",raise_e=False, timeout=5)
    
    def verify_sRGB_mode(self):
        return self.driver.wait_for_object("sRGB_Web_tile",raise_e=False, timeout=5)
    
    def verify_adobe_RGB_mode(self):
        return self.driver.wait_for_object("Adobe_RGB_tile",raise_e=False, timeout=5)
    
    def verify_display_p3_mode(self):
        return self.driver.wait_for_object("Display_P3_tile",raise_e=False, timeout=5)
    
    def verify_low_blue_light_scheduler(self):
        return self.driver.wait_for_object("Low_Blue_Light_Scheduler_Title",raise_e=False, timeout=5)
    
    def verify_restore_defaults_btn(self):
        return self.driver.wait_for_object("Restore_default",raise_e=False, timeout=5)
    
    def verify_native_mode_tile(self):
        return self.driver.wait_for_object("Native_tile",raise_e=False, timeout=5)
    
    def verify_low_blue_light_scheduler_modal(self):
        return self.driver.wait_for_object("Low_Blue_Light_Scheduler_Modal_Title",raise_e=False, timeout=5)
    
    def verify_hour_text(self):
        return self.driver.get_attribute("turn_on_hour_text","Name")
    
    def verify_turn_on_am_pm_text(self):
        return self.driver.get_attribute("turn_on_am_pm_text","Name")
    
    def verify_turn_off_hour_text(self):
        return self.driver.get_attribute("turn_off_hour_text","Name")
    
    def verify_turn_off_am_pm_text(self):
        return self.driver.get_attribute("turn_off_am_pm_text","Name")
    
    def get_adobe_rgb_text(self):
        return self.driver.get_attribute("adobe_rgb_text","Name")

    def get_display_title_text(self):
        return self.driver.get_attribute("display_title","Name")
    
    def set_schedule_toggle_on(self):
        if (self.driver.get_attribute("Schedule_Toggle","Toggle.ToggleState")=="off"):
            self.driver.click("Schedule_Toggle")
    
    def verify_advaced_setting_visible(self):
        return self.driver.get_attribute("advanced_setting","Name", timeout = 45)
    
    def click_advaced_setting(self):
        self.driver.click("advanced_setting", timeout = 40)
    
    def verify_advanced_settings_title(self):
        return self.driver.get_attribute("advanced_settings_title","Name", timeout = 40)
    
    def verify_low_blue_light_text(self):
        return self.driver.get_attribute("low_blue_light_txt","Name")
    
    def verify_low_blue_light_toggle_text(self):
        return self.driver.get_attribute("low_blue_light_toggle_text","Name")
    
    def get_toggle_of_low_blue_light(self):
        return self.driver.get_attribute("low_blue_light_toggle","Toggle.ToggleState", timeout = 30)
    
    def click_low_blue_light_toggle_on(self):
        self.driver.click("low_blue_light_toggle")
    
    def get_turn_on_advanced_settings(self):
        return self.driver.get_attribute("turn_on_advanced_settings","Name", timeout = 10)
    
    def click_turn_on_combo_advanced_settings(self):
        self.driver.click("turn_on_combo_advanced_settings")
    
    def verify_turn_on_am_text(self):
        return self.driver.get_attribute("turn_on_am","Name")
    
    def verify_turn_on_pm_text(self):
        return self.driver.get_attribute("turn_on_pm","Name")
    
    def get_turn_off_advanced_settings(self):
        return self.driver.get_attribute("turn_off_advanced_settings","Name", timeout = 10)
    
    def click_turn_off_combo_advanced_settings(self):
        self.driver.click("turn_off_combo_advanced_settings")
    
    def verify_turn_off_am_text(self):
        return self.driver.get_attribute("turn_off_am","Name")
    
    def verify_turn_off_pm_text(self):
        return self.driver.get_attribute("turn_off_pm","Name")

    def click_default_tile(self):
        return self.driver.click("Default_tile")

    def click_work_tile(self):
        return self.driver.click("Work_tile", raise_e = False)

    def click_low_light_tile(self):
        return self.driver.click("Low_Light_tile")

    def click_entertainment_tile(self):
        return self.driver.click("Entertainment_tile")

    def click_low_blue_light_tile(self):
        return self.driver.click("Low_blue_light_tile")

    def click_advanced_title(self):
        return self.driver.click("Advanced_Title")

    def click_sRGB_web_tile(self):
        return self.driver.click("sRGB_Web_tile")

    def click_adobe_RGB_tile(self):
        return self.driver.click("Adobe_RGB_tile")

    def click_display_p3_tile(self):
        return self.driver.click("Display_P3_tile")

    def click_native_tile(self):
        return self.driver.click("Native_tile", timeout = 10)

    def click_brightness_slider(self):
        return self.driver.click("Brightness_slider")

    def click_contrast_slider(self):
        return self.driver.click("Contrast_slider")
    
    def click_close_btn_advanced_settings(self):
        self.driver.click("close_btn_advanced_settings")
    
    def verify_add_application_text(self):
        return self.driver.get_attribute("add_application","Name", timeout = 30)
    
    def click_add_application_btn(self):
        self.driver.click("add_application", timeout = 10)
    
    def verify_applications_display(self):
        return self.driver.wait_for_object("applications",raise_e=False, timeout=5)
    
    def verify_applications_text(self):
        return self.driver.get_attribute("applications","Name")
    
    def verify_search_application_text(self):
        return self.driver.get_attribute("search_application","Name")
    
    def verify_cancel_text(self):
        return self.driver.get_attribute("cancel","Name")
    
    def click_app_in_app_list(self):
        self.driver.click("app_in_list")
    
    def verify_add_btn_text(self):
        return self.driver.get_attribute("add_btn","Name")
    
    def click_add_btn(self):
        self.driver.click("add_btn")
    
    def hover_added_app(self):
        self.driver.click("added_app", timeout = 10)
    
    def verify_delete_disney_plus_app_display(self):
        return self.driver.wait_for_object("delete_disney_plus_app",raise_e=False, timeout=5)
    
    def click_delete_disney_plus_app(self):
        self.driver.click("delete_disney_plus_app")
    
    def verify_delete_app_setting_window(self):
        return self.driver.wait_for_object("delete_app_setting",raise_e=False, timeout=5)
    
    def verify_delete_app_setting(self):
        return self.driver.get_attribute("delete_app_setting","Name")
    
    def verify_delete_app_setting_sub_title(self):
        return self.driver.get_attribute("delete_app_setting_sub_title","Name")
    
    def verify_do_not_show_again(self):
        return self.driver.get_attribute("do_not_show_again","Name")
    
    def verify_cancel_on_delete_app_setting(self):
        return self.driver.get_attribute("cancel_on_delete_app_setting","Name")
    
    def verify_continue_on_delete_app_setting(self):
        return self.driver.get_attribute("continue_on_delete_app_setting","Name")
    
    def click_cancel_on_delete_app_setting(self):
        self.driver.click("cancel_on_delete_app_setting")
    
    def click_low_blue_light_toggle(self):
        self.driver.click("low_blue_light_toggle_text")

    def verify_natural_mode_title(self):
        return self.driver.get_attribute("neutral_mode","Name", timeout = 10)

    def verify_game_mode_title(self):
        return self.driver.get_attribute("game_mode","Name", timeout = 10)

    def verify_reading_mode_title(self):
        return self.driver.get_attribute("reading_mode","Name")

    def verify_night_mode_title(self):
        return self.driver.get_attribute("night_mode","Name")

    def verify_movie_mode_title(self):
        return self.driver.get_attribute("movie_mode","Name")

    def verify_enhanceplus_mode_title(self):
        return self.driver.get_attribute("enhanceplus_mode","Name")

    def click_natural_mode(self):
        self.driver.click("neutral_mode", timeout = 10)

    def click_game_mode(self):
        self.driver.click("game_mode", timeout = 10)

    def click_reading_mode(self):
        self.driver.click("reading_mode", timeout = 10)

    def click_night_mode(self):
        self.driver.click("night_mode", timeout = 10)

    def click_movie_mode(self):
        self.driver.click("movie_mode", timeout = 10)

    def click_enhanceplus_mode(self):
        self.driver.click("enhanceplus_mode", timeout = 10)

    def get_brightness_slider_value(self,slider_name):
        time.sleep(10)
        return self.driver.get_attribute(slider_name,"RangeValue.Value", timeout = 40 )

    def set_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.RIGHT)

    def set_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)  
            slider.send_keys(Keys.LEFT)

    def get_system_brightness(self):
        time.sleep(5)
        return self.driver.get_attribute("system_brightness", "RangeValue.Value", timeout = 30)   

    def get_contrast_slider_value(self,slider_name):
        time.sleep(5)
        return self.driver.get_attribute(slider_name,"RangeValue.Value", timeout=30)
    
    def get_turn_on_am_pm_advanced_settings(self):
        return self.driver.get_attribute("turn_on_combo_advanced_settings","Name")
    
    def get_turn_off_am_pm_advanced_settings(self):
        return self.driver.get_attribute("turn_off_combo_advanced_settings","Name")

    def get_toggle_of_low_blue_light_status(self):
        return self.driver.wait_for_object("low_blue_light_toggle") is not False
    
    def click_turn_on_advanced_settings_dropdown(self):
        self.driver.click("turn_on_advanced_settings")
    
    def select_dropdown_on_item(self):
        self.driver.click("dropdown_on_item")

    def select_dropdown_on_am_pm_item(self):
        self.driver.click("dropdown_on_am_pm_item",timeout=10)

    def click_turn_off_advanced_settings_dropdow(self):
        self.driver.click("turn_off_advanced_settings")

    def get_advance_setting_error_message(self):
        return self.driver.get_attribute("advance_setting_error_message","Name", timeout = 10)
   
    def verify_red_slider(self):
        return self.driver.get_attribute("red_slider","Name", timeout = 20)

    def verify_blue_slider(self):
        return self.driver.get_attribute("blue_slider","Name", timeout = 20)

    def verify_green_slider(self):
        return self.driver.get_attribute("green_slider","Name", timeout = 20)

    def verify_color_adjestments_tooltip_text(self):
        return self.driver.get_attribute("color_adjestments_tool_tip","Name")

    def verify_low_blue_light_toggle_is_present(self):
        return self.driver.wait_for_object("low_blue_light_toggle") is not False

    def verify_trun_on_am_pm_combobox_is_present(self):
        return self.driver.wait_for_object("turn_on_combo_advanced_settings") is not False

    def verify_trun_off_am_pm_combobox_is_present(self):
        return self.driver.wait_for_object("turn_off_am_pm_combo_advanced_settings") is not False

    def verify_trun_on_hr_combobox_is_present(self):
        return self.driver.wait_for_object("turn_on_hr_combo_advanced_settings") is not False

    def verify_trun_off_hr_combobox_is_present(self):
        return self.driver.wait_for_object("turn_off_hr_combo_advanced_settings") is not False

    def get_color_adjestments(self):
        return self.driver.get_attribute("color_adjestments","Name", timeout = 10)
    
    def get_native_text(self):
        return self.driver.get_attribute("native_text","Name")

    def get_low_blue_light_tooltip(self):
        return self.driver.get_attribute("low_blue_light_toggle_text","Name")

    def click_low_blue_light_tooltip(self):
        self.driver.click("low_blue_light_toggle_text")

    def get_r_text(self):
        return self.driver.get_attribute("r_text","Name")

    def get_g_text(self):
        return self.driver.get_attribute("g_text","Name")

    def get_b_text(self):
        return self.driver.get_attribute("b_text","Name")

    def get_use_hdmi_input(self):
        return self.driver.get_attribute("use_hdmi_input","Name")

    def click_use_hdmi_input_tooltip(self):
        self.driver.click("use_hdmi_input_tooltip")

    def get_use_hdmi_input_tooltip(self):
        return self.driver.get_attribute("use_hdmi_input_tooltip","Name")

    def get_switch_text(self):
        return self.driver.get_attribute("switch_text","Name")

    def get_press_text(self):
        return self.driver.get_attribute("press_text","Name")
    
    def get_hdmi_input_osd_help_text(self):
        return self.driver.get_attribute("hdmi_input_osd_help_text","Name")
    
    def click_switch_btn(self):
        self.driver.click("switch_text")
    
    def get_back_to_pc_desktop_window_title(self):
        return self.driver.get_attribute("back_to_pc_desktop_window_title","Name")
    
    def get_back_to_pc_desktop_window_sub_title(self):
        return self.driver.get_attribute("back_to_pc_desktop_window_sub_title","Name")
    
    def get_keys_to_stop_using_pcdesktop_text(self):
        return self.driver.get_attribute("keys_to_stop_using_pcdesktop_text","Name")
    
    def get_do_not_show_text_on_back_to_pc_desktop_window(self):
        return self.driver.get_attribute("do_not_show_text_on_back_to_pc_desktop_window","Name")
    
    def get_cancel_btn_on_back_to_pc_desktop_window(self):
        return self.driver.get_attribute("cancel_btn_on_back_to_pc_desktop_window","Name")
    
    def get_continue_btn_on_back_to_pc_desktop_window(self):
        return self.driver.get_attribute("continue_btn_on_back_to_pc_desktop_window","Name")
    
    def click_continue_btn_on_back_to_pc_desktop_window(self):
        self.driver.click("continue_btn_on_back_to_pc_desktop_window")
    
    def click_hdmi_input_osd_help_text(self):
        self.driver.click("hdmi_input_osd_help_text")
    
    def get_hdmi_input_osd_help_title_text(self):
        return self.driver.get_attribute("hdmi_input_osd_help_title_text","Name")
    
    def get_hdmi_input_osd_help_sub_title_text(self):
        return self.driver.get_attribute("hdmi_input_osd_help_sub_title_text","Name")
    
    def get_up_down_arrows_text(self):
        return self.driver.get_attribute("up_down_arrows_text","Name")
    
    def get_enter_text(self):
        return self.driver.get_attribute("enter_text","Name")
    
    def get_navigate_osd_menu_text(self):
        return self.driver.get_attribute("navigate_osd_menu_text","Name")
    
    def get_enter_des_text(self):
        return self.driver.get_attribute("enter_des_text","Name")
    
    def get_close_btn_on_hdmi_input_osd_help_window(self):
        return self.driver.get_attribute("close_btn_on_hdmi_input_osd_help_window","Name")
    
    def click_close_btn_on_hdmi_input_osd_help_window(self):
        self.driver.click("close_btn_on_hdmi_input_osd_help_window")

    def verify_on_hour_time(self):
        return self.driver.get_attribute("turn_on_hr_combo_advanced_settings","Name", timeout = 10)

    def verify_off_hour_time(self):
        return self.driver.get_attribute("turn_off_hr_combo_advanced_settings","Name", timeout = 10)
    
    def verify_turn_on_default_pm_time(self):
        return self.driver.get_attribute("turn_on_combo_advanced_settings","Name")

    def verify_turn_off_default_am_time(self):
        return self.driver.get_attribute("turn_off_combo_advanced_settings","Name")

    def verify_red_slider_value(self):
        time.sleep(5)
        return self.driver.get_attribute("red_slider","RangeValue.Value", timeout = 20)

    def verify_blue_slider_value(self):
        time.sleep(5)
        return self.driver.get_attribute("blue_slider","RangeValue.Value", timeout = 20)

    def verify_green_slider_value(self):
        time.sleep(5)
        return self.driver.get_attribute("green_slider","RangeValue.Value", timeout = 20)

    def verify_brightness_slider_default_value(self):
        return self.driver.get_attribute("brightness_slider","RangeValue.Value")
    
    def click_hdmi_input_osd_help_link(self):
        self.driver.click("hdmi_input_osd_help_text")

    def hover_on_advanced_settings_lbl_tooltip_icon(self):
        self.driver.click("low_blue_light_toggle_text", timeout = 10)

    def verify_advanced_settings_lbl_tooltip_icon(self):
        return self.driver.get_attribute("low_blue_light_toggle_text","Name")
    
    def click_display_title(self):
        self.driver.click("display_title")

    def set_slider_value(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        width, height = slider.rect["width"], slider.rect["height"]
        self.driver.click_by_coordinates(slider, width * value * 0.01, height * 0.5)

    def verify_windows_do_not_show_visible(self):
        return self.driver.wait_for_object("back_to_pc_desktop_window_title", raise_e=False, timeout = 10) is not False

    def verify_hpmi_input_description(self):
        return self.driver.get_attribute("hpmi_input_description","Name")

    def click_display_title(self):
        self.driver.click("display_title")

    def select_dropdown_on_item_default(self):
        self.driver.click("dropdown_on_item_default", timeout = 10)

    def set_brightness_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.RIGHT)

    def set_contrast_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.LEFT)

    def get_game_mode(self):
        return self.driver.get_attribute("game_mode","Name")

    def get_brightness_slider_value_100(self):
        time.sleep(5)
        return self.driver.get_attribute("Brightness_slider","RangeValue.Value")

    def get_contrast_slider_value_100(self):
        time.sleep(5)
        return self.driver.get_attribute("Contrast_slider","RangeValue.Value")

    def get_toggle_of_low_blue_light_on(self):
        return self.driver.get_attribute("low_blue_light_toggle","Toggle.ToggleState")

    def click_restore_default_button_1(self):
        self.driver.click("Restore_default")
        self.driver.click("Restore_default")

    def click_continue_button_dialog(self):
        self.driver.click("restore_factory_settings_continue")
    
    def get_hdr_button_status(self):
        return self.driver.get_attribute("hdr_button","Toggle.ToggleState", timeout=20)

    def get_hdr_windows_settings_text(self):
        return self.driver.get_attribute("hdr_windows_settings","Name")

    def click_hdr_tooltips_icon(self):
        self.driver.click("hdr_tooltips", timeout = 10)

    def get_hdr_tooltips_text(self):
        return self.driver.get_attribute("hdr_tooltips","Name")

    def click_hdr_button(self):
        self.driver.click("hdr_button", raise_e=False)

    def verify_work_mode_status(self):
        return self.driver.get_attribute("Work_tile","IsKeyboardFoucusable")

    def verfiy_disable_button_show(self):
        return self.driver.wait_for_object("disable_button", raise_e=False, timeout = 10) is not False

    def get_hdr_disable_text(self):
        return self.driver.get_attribute("hdr_disable_text","Name")

    def verify_hdr_disable_text(self):
        return self.driver.wait_for_object("hdr_disable_text", raise_e=False, timeout = 10) is not False

    def click_disable_button(self):
        self.driver.click("disable_button", timeout = 10)

    def click_windows_display_settings(self):
        self.driver.click("hdr_windows_settings")

    def get_restore_pop_up_windows_title(self):
        return self.driver.get_attribute("hdr_restore_pop_up_windows_title","Name")
    
    def get_restore_pop_up_windows_subtitle(self):
        return self.driver.get_attribute("hdr_restore_pop_up_windows_subtitle","Name")

    def get_restore_pop_up_windows_do_not_show_text(self):
        return self.driver.get_attribute("hdr_restore_pop_up_windows_do_not_show","Name")

    def get_restore_pop_up_windows_cancel_text(self):
        return self.driver.get_attribute("hdr_restore_pop_up_windows_cancel_button","Name")

    def get_restore_pop_up_windows_continue_text(self):
        return self.driver.get_attribute("pop_up_continue","Name")

    def click_restore_pop_up_continue_button(self):
        if bool(self.driver.wait_for_object("pop_up_continue", raise_e=False, timeout = 10)) is False:
            self.driver.click("Restore_default")
        self.driver.click("pop_up_continue", timeout = 10)

    def click_restore_pop_up_do_not_show_checkbox(self):
        self.driver.click("hdr_restore_pop_up_windows_checkbox")
    
    def click_restore_defaults_button(self):
        self.driver.click("Restore_default", timeout = 40)
    
    def get_display_control_title_text(self):
        return self.driver.get_attribute("display_title","Name", timeout = 10)
    
    def search_application(self,app_name):
        self.driver.send_keys("search_application", app_name)

    def verify_tencent_video_app(self):
        return self.driver.get_attribute("tencent_video_app","Name", raise_e=False, timeout = 40)
    
    def click_tencent_video_app(self):
        self.driver.click("tencent_video_app", timeout = 40)
    
    def verify_iqiyi_app(self):
        return self.driver.get_attribute("iqiyi_app","Name", raise_e=False)
    
    def click_iqiyi_app(self):
        self.driver.click("iqiyi_app", timeout = 40)
    
    def verify_disney_plus_app(self):
        return self.driver.get_attribute("disney_plus_app","Name",raise_e=False)
    
    def click_disney_plus_app(self):
        self.driver.click("disney_plus_app", timeout = 40)
    
    def verify_advanced_title_exist(self):
        return self.driver.get_attribute("Advanced_Title","Name",raise_e=False)
    
    def click_global_app_icon(self):
        self.driver.click("default_global_app")

    def verify_calculator_app(self):
        return self.driver.get_attribute("calculator_app","Name", timeout =20)

    def click_to_select_calculator_app(self):
        self.driver.click("calculator_app", timeout = 5)

    def click_to_delete_calculator_app(self):
        self.driver.click("delete_calculator_app")
  
    def click_to_delete_disney_plus_app(self):
        self.driver.click("delete_disney_plus_app")

    def click_to_delete_tencent_video_app(self):
        self.driver.click("delete_tencent_video_app")

    def click_to_delete_iqiyi_video_app(self):
        self.driver.click("delete_iqiyi_app")
    
    def get_restore_pop_up_windows_do_not_show_again_checkbox(self):
        return self.driver.get_attribute("hdr_restore_pop_up_windows_checkbox","Name")
    
    def click_restore_pop_up_windows_cancel_button(self):
        self.driver.click("hdr_restore_pop_up_windows_cancel_button")

    def verify_restore_pop_up_windows_title(self):
        return self.driver.wait_for_object("hdr_restore_pop_up_windows_title", raise_e=False, timeout = 10) is not False
    
    def verify_turn_on_time_drop_down_list_show(self):
        return self.driver.get_attribute("turn_on_hr_combo_advanced_settings","Name")
    
    def click_turn_on_time_drop_down_list(self):
        self.driver.click("turn_on_hr_combo_advanced_settings")

    def select_turn_on_time_drop_down_list(self):
        self.driver.click("time_is_11:00")

    def get_turn_off_time_drop_down_list_show(self):
        return self.driver.get_attribute("turn_off_hr_combo_advanced_settings","Name")

    def click_turn_off_time_drop_down_list(self):
        self.driver.click("turn_off_hr_combo_advanced_settings")
    
    def select_turn_off_time_drop_down_list(self):
        self.driver.click("time_is_6:00")

    def select_turn_off_time_drop_down_list_as_eight(self):
        self.driver.click("time_is_8:00")

    def get_low_blue_light_toggle_status(self):
        return self.driver.get_attribute("low_blue_light_toggle","Toggle.ToggleState", timeout = 30)
    
    def get_turn_on_time_drop_down_list_show(self):
        return self.driver.get_attribute("turn_on_hr_combo_advanced_settings","Name")
    
    def set_red_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.LEFT)
            time.sleep(3)

    def set_green_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.LEFT)
            time.sleep(3)

    def set_blue_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.LEFT)
            time.sleep(3)

    def get_turn_on_time_state_show(self):
        return self.driver.get_attribute("turn_on_combo_advanced_settings","Name")
    
    def verify_turn_on_time_state_list_show(self):
        return self.driver.wait_for_object("turn_on_time_state_list_show", raise_e=False, timeout = 10) is not False
    
    def click_turn_on_time_state_list(self):
        self.driver.click("turn_on_time_state_list_show")

    def select_turn_on_time_state_am(self):
        self.driver.click("turn_on_time_state_list_show")
    
    def get_turn_off_time_state_show(self):
        return self.driver.get_attribute("turn_off_combo_advanced_settings","Name")
    
    def verify_turn_off_time_state_list_show(self):
        return self.driver.wait_for_object("turn_off_time_state_list_show", raise_e=False, timeout = 10) is not False
    
    def click_turn_off_time_state_list(self):
        self.driver.click("turn_off_time_state_list_show")

    def select_turn_off_time_state_pm(self):
        self.driver.click("turn_off_time_state_is_pm")

    def get_trun_on_time_drop_down_is_grey(self):
        return self.driver.get_attribute("turn_on_hr_combo_advanced_settings","IsEnabled")
    
    def get_trun_on_time_state_is_grey(self):
        return self.driver.get_attribute("turn_on_combo_advanced_settings","IsEnabled")
    
    def get_trun_off_time_drop_down_is_grey(self):
        return self.driver.get_attribute("turn_off_hr_combo_advanced_settings","IsEnabled")
    
    def get_trun_off_time_state_is_grey(self):
        return self.driver.get_attribute("turn_off_combo_advanced_settings","IsEnabled")
    
    def select_am_on_am_pm_turn_on_drop_down(self):
        self.driver.click("am_on_am_pm_turn_on_drop_down")
    
    def select_pm_on_am_pm_turn_on_drop_down(self):
        self.driver.click("pm_on_am_pm_turn_on_drop_down", timeout = 10)
    
    def click_access_app_delete_button(self):
        self.driver.click("access_app_delete_button")

    def click_continue_on_delete_app_setting(self):
        self.driver.click("continue_on_delete_app_setting")

    def click_low_blue_light_toggle_off(self):
        self.driver.click("low_blue_light_toggle")
    
    def get_app_name_from_app_add_list(self):
        return self.driver.get_attribute("added_app","Name")
    
    def verify_reading_mode_selected(self):
        return self.driver.get_attribute("reading_mode_container","SelectionItem.IsSelected", timeout = 10)
    
    def verify_neutral_mode_selected(self):
        return self.driver.get_attribute("neutral_mode_container","SelectionItem.IsSelected", timeout = 20)
    
    def verify_hdr_restore_pop_up_windows_checkbox(self):
        return self.driver.wait_for_object("hdr_restore_pop_up_windows_checkbox", raise_e=False, timeout = 10)
    
    def verify_hdr_restore_pop_up_windows_cancel_button(self):
        return self.driver.wait_for_object("hdr_restore_pop_up_windows_cancel_button", raise_e=False, timeout = 10)
    
    def verify_restore_factory_settings_continue(self):
        return self.driver.wait_for_object("restore_factory_settings_continue", raise_e=False, timeout = 10)
    
    def verify_close_btn_on_restore_popup(self):
        return self.driver.wait_for_object("close_btn_on_restore_popup", raise_e=False, timeout = 10)
    
    def verify_default_global_app(self):
        return self.driver.wait_for_object("default_global_app", raise_e=False, timeout = 10) is not False

    def is_night_mode_selected(self):
        time.sleep(10)
        return self.driver.get_attribute("night_mode_container","SelectionItem.IsSelected")
    
    def verify_app_out_of_sync_show(self):
        return self.driver.wait_for_object("out_off_sync_title", raise_e=False, timeout = 20) is not False
    
    def click_see_more_link(self):
        self.driver.click("see_more_link", timeout = 0.5)
    
    def verify_not_synchronized_title(self):
        return self.driver.wait_for_object("not_synchronized_title", raise_e=False, timeout = 20) is not False
    
    def click_discard_changes_button(self):
        self.driver.click("discard_changes_button")
    
    def click_keep_new_changes_button(self):
        self.driver.click("keep_new_changes_button")
    
    def verify_discard_changes_button_show(self):
        return self.driver.wait_for_object("discard_changes_button", raise_e=False, timeout = 20) is not False

    def verify_keep_new_changes_button_show(self):
        return self.driver.wait_for_object("keep_new_changes_button", raise_e=False, timeout = 20) is not False
    
    def is_reading_mode_selected(self):
        return self.driver.get_attribute("reading_mode_container","SelectionItem.IsSelected", timeout = 10)
    
    def is_red_slider_visible(self):
        return self.driver.wait_for_object("red_slider", raise_e=False, timeout = 10) is not False
    
    def is_green_slider_visible(self):
        return self.driver.wait_for_object("green_slider", raise_e=False, timeout = 10) is not False
    
    def is_blue_slider_visible(self):
        return self.driver.wait_for_object("blue_slider", raise_e=False, timeout = 10) is not False
    
    def verify_see_more_link_show(self):
        return self.driver.wait_for_object("see_more_link", raise_e=False, timeout = 20) is not False
    
    def click_turn_off_time_state_is_am(self):
        self.driver.click("turn_off_time_state_is_am", timeout = 30)
    
    def get_item_turn_on_time_drop_down_list_show(self):
        return self.driver.get_attribute("turn_on_time_drop_down_list_show","Name")
    
    def get_item_turn_off_time_drop_down_list_show(self):
        return self.driver.get_attribute("turn_off_time_drop_down_list_show","Name")
    
    def is_low_blue_light_tile_selected(self):
        return self.driver.get_attribute("Low_blue_light_tile","SelectionItem.IsSelected", timeout = 10)
    
    def click_neutral_mode_container(self):
        self.driver.click("neutral_mode_container")
    
    def click_close_btn_on_restore_popup(self):
        self.driver.click("close_btn_on_restore_popup")
    
    def click_calculator_in_app_window(self):
        self.driver.click("calculator_in_app_window")
    
    def select_calculator_in_app_list(self):
        self.driver.click("calculator_in_app_list")
    
    def is_Native_tile_selected(self):
        return self.driver.get_attribute("Native_tile","SelectionItem.IsSelected", timeout = 10)
    
    def verify_warm_mode_title(self):
        return self.driver.get_attribute("warm_mode","Name", timeout = 10)

    def click_warm_mode(self):
        self.driver.click("warm_mode", timeout = 10)
    
    def is_default_tile_selected(self):
        return self.driver.get_attribute("Default_tile","SelectionItem.IsSelected", timeout = 10)
    
    def turn_on_hr_combo_advanced_settings_is_enable(self):
        return self.driver.get_attribute("turn_on_hr_combo_advanced_settings","IsEnabled", timeout = 10)
    
    def turn_off_hr_combo_advanced_settings_is_enable(self):
        return self.driver.get_attribute("turn_off_hr_combo_advanced_settings","IsEnabled", timeout = 10)

    def click_check_box_on_backup_to_pc_desktop(self):
        self.driver.click("check_box_on_backup_to_pc_desktop")
    
    def verify_click_check_box_on_backup_to_pc_desktop_is_selected(self):
        return self.driver.get_attribute("check_box_on_backup_to_pc_desktop","Toggle.ToggleState", timeout = 10)
    
    def click_cancel_btn_on_back_to_pc_desktop_window(self):
        self.driver.click("cancel_btn_on_back_to_pc_desktop_window")

    def verify_cool_mode_title(self):
        return self.driver.get_attribute("cool_mode","Name", timeout = 30)
    
    def verify_bt709_mode_title(self):
        return self.driver.get_attribute("bt709_mode","Name")
    
    def verify_srgb_d65_mode_title(self):
        return self.driver.get_attribute("srgb_d65_mode","Name")
    
    def verify_p3_d65_mode_title(self):
        return self.driver.get_attribute("p3_d65_mode","Name")
    
    def click_cool_mode_title(self):
        return self.driver.click("cool_mode", timeout = 10)
    
    def click_bt709_mode_title(self):
        return self.driver.click("bt709_mode", timeout = 10)
    
    def click_srgb_d65_mode_title(self):
        return self.driver.click("srgb_d65_mode", timeout = 10)
    
    def click_p3_d65_mode_title(self):
        return self.driver.click("p3_d65_mode", timeout = 10)

    def get_toggle_color_filter_state(self):
        return self.driver.get_attribute("color_filter_toggle","Toggle.ToggleState")
    
    def turn_toggle_color_filter_on(self):
        if int(self.get_toggle_color_filter_state())== 0:
            self.driver.click("color_filter_toggle")
    
    def turn_toggle_color_filter_off(self):
        if int(self.get_toggle_color_filter_state())== 1:
            self.driver.click("color_filter_toggle")
    
    def press_alt_f4(self):
        el= self.driver.wait_for_object("Native_tile")
        el.send_keys(Keys.ALT + Keys.F4)