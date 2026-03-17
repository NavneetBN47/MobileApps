from datetime import datetime
import logging
import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys
from SAF.decorator.saf_decorator import screenshot_compare


class DisplayControl(HPXRebrandingFlow):
    flow_name = "display_control"

    def verify_display_control_text_ltwo_page(self):
        return self.driver.get_attribute("display_control_text_ltwo_page", "Name",  timeout = 20)
    
    def verify_display_control_all_application_button_ltwo_page(self):
        return self.driver.wait_for_object("display_control_all_application_button_ltwo_page",raise_e=False, timeout = 15) is not False
    
    def verify_display_control_add_application_button_ltwo_page(self):
        return self.driver.wait_for_object("display_control_add_application_button_ltwo_page",raise_e=False, timeout = 10) is not False
    
    def click_display_control_all_application_button_ltwo_page(self):
        self.driver.click("display_control_all_application_button_ltwo_page", timeout = 10)
        
    def verify_display_control_brightness_text_ltwo_page(self):
        return self.driver.get_attribute("display_control_brightness_text_ltwo_page", "Name",  timeout = 20)
    
    def verify_display_control_brightness_slider_ltwo_page(self):
        return self.driver.wait_for_object("display_control_brightness_slider_button_ltwo_page",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_display_modes_select_box_ltwo_page(self):
        return self.driver.wait_for_object("display_control_display_modes_select_box_ltwo_page",raise_e=False, timeout = 10) is not False

    def click_display_control_display_modes_select_box_ltwo_page(self):
        self.driver.click("display_control_display_modes_select_box_ltwo_page",timeout = 30)

    def get_display_modes_dropdown_value(self,element_name):
        return self.driver.get_attribute(element_name,"Name", timeout=40)

    def select_display_modes_dropdown_value(self,element_name):
        self.driver.click(element_name, timeout=20)
        self.driver.click("display_control_title_bar",timeout = 10)

    
    def is_item_onscreen(self, element_name):
        item = self.driver.wait_for_object(element_name)
        if (item.get_attribute("IsOffscreen") == "false"):
            return True
    
    def verify_display_control_advanced_settings_card_ltwo_page(self):
        return self.driver.get_attribute("display_control_advanced_settings_card_ltwo_page", "Name",  timeout = 10)
    
    def click_display_control_advanced_settings_card_ltwo_page(self):
        self.driver.click("display_control_advanced_settings_card_ltwo_page",  timeout = 10)
    
    def verify_display_control_advanced_settings_restore_defaults_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_advanced_settings_restore_defaults_button_ltwo_page", "Name",  timeout = 10)

    def click_display_control_advanced_settings_restore_defaults_button_ltwo_page(self):
        self.driver.swipe(direction="down", distance=6)
        self.driver.click("display_control_advanced_settings_restore_defaults_button_ltwo_page", timeout = 10)
        for _ in range(3):
            if bool(self.driver.wait_for_object("display_control_restore_defaults_continue_onpopup_window_ltwo_page",raise_e=False,timeout = 10)) is True:
                break
            else:
                self.driver.swipe(direction="down", distance=6)
                self.driver.click("display_control_advanced_settings_restore_defaults_button_ltwo_page", timeout = 10)
        #after clicking restore system take some time to restore values( so we dont have to add hard sleep after each method)
        time.sleep(5)
        
    def verify_display_control_restore_defaults_description_onpopup_window_page(self):
        return self.driver.get_attribute("display_control_restore_defaults_description_onpopup_window_page", "Name",  timeout = 10)
    
    def verify_display_control_restore_defaults_do_not_show_again_checkbox(self):
        return self.driver.get_attribute("display_control_restore_defaults_do_not_show_again_checkbox", "Toggle.ToggleState",  timeout = 10)

    def verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page(self):
        return self.driver.get_attribute("display_control_restore_defaults_cancel_onpopup_window_ltwo_page", "Name",  timeout = 10)
    
    def verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page(self):
        return self.driver.get_attribute("display_control_restore_defaults_continue_onpopup_window_ltwo_page", "Name",  timeout = 10)
        
    def scroll_down_display_modes_list_window(self,distance=1):
        scroll_modes = self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 15)
        self.driver.click("display_control_title_bar",timeout = 10)#Traversing list can lock up application. This is a workaround.
        for _ in range(distance):
            scroll_modes.send_keys(Keys.DOWN)
            self.click_title_bar()
        time.sleep(3)

    def get_brightness_slider_value(self):
        time.sleep(8)#take some time to get value after chnaging modes.
        return self.driver.get_attribute("display_control_brightness_slider_button_ltwo_page", "Value.Value",  timeout = 20)
    
    def scroll_up_display_modes_list_window(self,distance=1):
        scroll_modes = self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 15)
        self.driver.click("display_control_title_bar",timeout = 10)#Traversing list can lock up application. This is a workaround.
        for _ in range(distance):
            scroll_modes.send_keys(Keys.UP)
            self.click_title_bar()
        time.sleep(3)

    def verify_display_modes_dropdown_value(self,element_name):
        return self.driver.get_attribute(element_name,"Name", timeout=10, raise_e=False)

    def click_display_control_low_blue_light_toggle_lthree_page(self):
        self.driver.click("display_control_low_blue_light_toggle_lthree_page", timeout = 15)
    
    def get_display_control_low_blue_light_toggle_lthree_page(self):
        return self.driver.get_attribute("display_control_low_blue_light_toggle_lthree_page", "Toggle.ToggleState",  timeout = 10)
    
    def click_display_control_advanced_settings_arrow_ltwo_page(self):
        for _ in range(5):
            if bool(self.driver.wait_for_object("display_control_advanced_display_settings_title_lthree_page",raise_e=False,timeout = 10)) is True:
                break
            else:
                self.driver.click("display_control_advanced_settings_arrow_ltwo_page", timeout = 10)
        
    def verify_display_control_advanced_settings_text_ltwo_page(self):
        return self.driver.get_attribute("display_control_advanced_settings_text_ltwo_page", "Name",  timeout = 20)

    def get_display_control_hdr_toggle_switch_ltwo_page(self):
        return self.driver.get_attribute("display_control_hdr_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 15)

    def verify_display_control_use_hdr_in_system_settings(self):
        return self.driver.get_attribute("display_control_use_hdr_in_system_settings", "Name",  timeout = 10)

    def verify_turn_off_hdr_chk_box_in_system_settings(self):
        return self.driver.wait_for_object("turn_off_hdr_chk_box_in_system_settings",raise_e=False, timeout = 10) is not False
    
    def click_use_hdr_show_more_option_in_system_settings(self):
        self.driver.click("display_control_use_hdr_in_system_settings", timeout = 10)
    
    def get_state_hdr_chk_box_in_system_settings(self):
        return self.driver.get_attribute("turn_off_hdr_chk_box_in_system_settings", "Toggle.ToggleState",  timeout = 10)

    def display_control_use_hdr_in_system_settings_is_enabled(self):
        return self.driver.get_attribute("display_control_use_hdr_in_system_settings", "IsEnabled",  timeout = 10)

    def display_control_hdr_toggle_switch_ltwo_page_is_enabled(self):
        return self.driver.get_attribute("display_control_hdr_toggle_switch_ltwo_page", "IsEnabled",  timeout = 10)

    def click_turn_off_hdr_chk_box_in_system_settings(self):
        self.driver.click("turn_off_hdr_chk_box_in_system_settings", timeout = 10)
   
    def click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page(self):
        self.driver.click("display_control_restore_defaults_cancel_onpopup_window_ltwo_page", timeout = 10)
        
    def verify_display_modes_list_window_default_time_ten_pm_lthree_page(self):
        return self.driver.wait_for_object("display_modes_list_window_default_time_ten_pm_lthree_page",raise_e=False, timeout = 10) is not False
    
    def verify_display_modes_list_window_default_turn_off_time_seven_am_lthree_page(self):
        return self.driver.wait_for_object("display_modes_list_window_default_turn_off_time_seven_am_lthree_page",raise_e=False, timeout = 10) is not False
    
    def set_display_control_brightness_slider_value_decrease_ltwo_pages(self,value):
        slider = self.driver.wait_for_object("display_control_brightness_slider_button_ltwo_page", timeout = 10)
        self.driver.click("display_control_brightness_slider_button_ltwo_page", timeout = 10)
        br_value = int(self.get_brightness_slider_value())
        for _ in range(br_value-value):
            time.sleep(5)
            slider.send_keys(Keys.LEFT)
    
    def get_contrast_slider_value(self):
        time.sleep(5)#take some time to get value after changing.
        return self.driver.get_attribute("display_control_contrast_slider_lthree_page","Value.Value",  timeout = 15)
            
    def click_display_control_restore_defaults_button_lthree_page(self):
        self.driver.click("display_control_restore_defaults_button_lthree_page", timeout = 10)
        for _ in range(3):
            if bool(self.driver.wait_for_object("display_control_restore_defaults_continue_onpopup_window_page_lthree_page",raise_e=False,timeout = 10)) is True:
                break
            else:
                self.driver.swipe(direction="down", distance=6)
                self.driver.click("display_control_restore_defaults_button_lthree_page", timeout = 10)
        #after clicking restore system take some time to restore values( so we dont have to add hard sleep after each method)
        time.sleep(5)
    
    def click_display_control_restore_defaults_continue_onpopup_window_ltwo_page(self):
        self.driver.click("display_control_restore_defaults_continue_onpopup_window_ltwo_page", timeout = 10)
        time.sleep(20)#system takes some time to restore values.
    
    def get_display_control_low_blue_light_turnon_dropdown_lthree_page(self):
        return self.driver.get_attribute("display_control_low_blue_light_turnon_dropdown_lthree_page", "Name", timeout = 10)
    
    def get_display_control_low_blue_light_turnoff_dropdown_lthree_page(self):
        return self.driver.get_attribute("display_control_low_blue_light_turnoff_dropdown_lthree_page", "Name", timeout = 10)

    def is_12_hour_format(self, time_str):
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return True
        except ValueError:
            return False
    
    def is_24_hour_format(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def click_display_control_switch_btn_lfour_page(self):
        self.driver.click("display_control_switch_btn_lfour_page", timeout = 10)

    def verify_display_control_back_to_pc_desktop_text_hdmi_popup_page(self):
        return self.driver.get_attribute("display_control_back_to_pc_desktop_text_hdmi_popup_page", "Name",  timeout = 10)
    
    def verify_display_control_back_to_pc_desktop_description_hdmi_popup_page(self):
        return self.driver.get_attribute("display_control_back_to_pc_desktop_description_hdmi_popup_page", "Name",  timeout = 10)
    
    def click_display_control_hdmi_popup_page_do_not_show_again_text(self):
        self.driver.click("display_control_hdmi_popup_page_do_not_show_again_checkbox", timeout = 10)
    
    def get_toggle_display_control_hdmi_popup_page_do_not_show_again_text(self):
        return self.driver.get_attribute("display_control_hdmi_popup_page_do_not_show_again_checkbox", "Toggle.ToggleState",  timeout = 10)
    
    def click_display_control_hdmi_popup_page_cancel_button(self):
        self.driver.click("display_control_hdmi_popup_page_cancel_button", timeout = 10)
    
    def verify_display_control_use_hdmi_input_txt_lthree_page(self):
        return self.driver.get_attribute("display_control_use_hdmi_input_txt_lthree_page", "Name",  timeout = 10)
    
    def get_display_control_display_modes_select_box_ltwo_page(self):
        return self.driver.get_attribute("display_control_display_modes_select_box_ltwo_page", "Name",  timeout = 20)
            
    def verify_display_control_disney_plus_app_ltwo_page(self):
        return self.driver.get_attribute("display_control_disney_plus_app_ltwo_page", "Name",  timeout = 15)
    
    def verify_display_control_tencent_app_ltwo_page(self):
        return self.driver.get_attribute("display_control_tencent_app_ltwo_page", "Name",  timeout = 15)

    def verify_display_control_iqiyi_app_ltwo_page(self):
        return self.driver.get_attribute("display_control_iqiyi_app_ltwo_page", "Name",  timeout = 15)

    def click_display_control_tencent_app_ltwo_page(self):
        self.driver.click("display_control_tencent_app_ltwo_page", timeout = 10)
    
    def click_display_control_iqiyi_app_ltwo_page(self):
        self.driver.click("display_control_iqiyi_app_ltwo_page", timeout = 10)
    
    def click_display_control_add_application_button_ltwo_page(self):
        self.driver.click("display_control_add_application_button_ltwo_page", timeout = 10)

    def verify_display_control_cancel_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_cancel_button_ltwo_page", "Name",  timeout = 10)
    
    def click_display_control_cancel_button_ltwo_page(self):
        self.driver.click("display_control_cancel_button_ltwo_page", timeout = 10)
    
    def verify_display_control_add_app_search_bar_ltwo_page(self):
        return self.driver.wait_for_object("display_control_add_app_search_bar_ltwo_page",raise_e=False, timeout = 10) is not False

    def verify_display_control_continue_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_add_app_continue_button_ltwo_page", "Name",  timeout = 10)
    
    def verify_display_control_application_list_ltwo_page(self):
        return self.driver.wait_for_object("display_control_application_list_ltwo_page",raise_e=False,  timeout = 10) is not False
    
    def verify_display_control_app_settings_header(self):
        return self.driver.wait_for_object("display_control_app_settings_header",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_support_popup(self):
        return self.driver.wait_for_object("display_control_support_popup",raise_e=False, timeout = 10) is not False
    
    def click_display_control_ok_support_popup_button(self):
        self.driver.click("display_control_ok_support_popup_button", timeout = 10)
   
    def verify_display_control_delete_profile_button(self):
        return self.driver.wait_for_object("display_control_delete_profile_button",raise_e=False, timeout = 10) is not False
    
    def click_display_control_delete_profile_button(self):
        self.driver.click("display_control_delete_profile_button", timeout = 15)
    
    def verify_display_control_delete_profile_checkbox_ltwo_page(self):
        return self.driver.get_attribute("display_control_delete_profile_checkbox_ltwo_page", "Toggle.ToggleState",  timeout = 10)
        
    def verify_display_control_app_settings_app_name(self):
        return self.driver.get_attribute("display_control_app_settings_app_name", "Name",  timeout = 10)
    
    def click_display_control_low_blue_light_turnon_dropdown_lthree_page(self):
        self.driver.click("display_control_low_blue_light_turnon_dropdown_lthree_page", timeout = 10)
    
    def select_display_control_low_blue_light_turnon_dropdown_hrs_ten_thirty_pm_lthree_page(self):
        self.driver.click("display_control_low_blue_light_turnon_dropdown_hrs_ten_thirty_pm_lthree_page", timeout = 10)
    
    def click_display_control_low_blue_light_turnoff_dropdown_lthree_page(self):
        self.driver.click("display_control_low_blue_light_turnoff_dropdown_lthree_page", timeout = 10)

    def click_display_control_low_blue_light_turnoff_dropdown_hrs_eight_am_lthree_page(self):
        self.driver.click("display_control_low_blue_light_turnoff_dropdown_hrs_eight_am_lthree_page", timeout = 10)
        
    def get_display_control_low_blue_light_turnon_error_msg_lthree_page(self):
        return self.driver.get_attribute("display_control_low_blue_light_turnon_error_msg_lthree_page", "Name",  timeout = 15)
    
    def get_display_control_low_blue_light_turnoff_error_msg_lthree_page(self):
        return self.driver.get_attribute("display_control_low_blue_light_turnoff_error_msg_lthree_page", "Name",  timeout = 15)
        
    def get_setting_display_slider_value(self):
        time.sleep(6)#take some time to get value after changing.
        return self.driver.get_attribute("setting_display_slider", "Value.Value",  timeout = 20)
    
    def get_display_control_low_blue_light_red_slider_lthree_page(self):
        value = self.driver.get_attribute("display_control_low_blue_light_red_slider_lthree_page", "Value.Value", timeout = 10)
        # workaround for slider getting changed to 98 when get_attribute is called
        if value == "98":
            self.set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 100, 0, 100)
            return "100"
        return value
        
    def get_display_control_low_blue_light_green_slider_lthree_page(self):
        value = self.driver.get_attribute("display_control_low_blue_light_green_slider_lthree_page","Value.Value",  timeout = 10)
        # workaround for slider getting changed to 98 when get_attribute is called
        if value == "98":
            self.set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 100, 0, 100)
            return "100"
        return value
        
    def get_display_control_low_blue_light_blue_slider_lthree_page(self):
        value = self.driver.get_attribute("display_control_low_blue_light_blue_slider_lthree_page", "Value.Value", timeout = 10)
        # workaround for slider getting changed to 98 when get_attribute is called
        if value == "98":
            self.set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 100, 0, 100)
            return "100"
        return value
        
    def click_display_control_hdr_toggle_btn_ltwo_page(self, desired_state="1"):
        self.driver.click("display_control_hdr_toggle_switch_ltwo_page", timeout = 15)
        time.sleep(10)
        #added for loop coz toggle sometimes not getting enabled in first click
        for _ in range(5):
            # Check for desired state 1 for on and 0 for off, with on being the default value
            if self.get_display_control_hdr_toggle_switch_ltwo_page() == desired_state:
                break
            else:
                self.driver.click("display_control_hdr_toggle_switch_ltwo_page", timeout = 15)
                time.sleep(10)
        time.sleep(2)
    
    def set_display_brightness_slider_value_for_analytics(self,max_changes=1):
        slider = self.driver.wait_for_object("display_control_brightness_slider_button_ltwo_page", timeout = 15)
        max_changes = 5
        changes_made = 0
        while changes_made < max_changes:
            slider_value = int(self.get_brightness_slider_value())
            print("slider_value",slider_value)
            time.sleep(2)
            if slider_value == 0:
                slider.send_keys(Keys.RIGHT)
            elif slider_value == 100:
                slider.send_keys(Keys.LEFT)
            else:
                if changes_made <=3:
                    slider.send_keys(Keys.RIGHT)
                else:
                    slider.send_keys(Keys.LEFT)
            changes_made += 1

    def set_display_contrast_slider_value_for_analytics(self,max_changes=1):
        slider = self.driver.wait_for_object("display_control_contrast_slider_lthree_page", timeout = 15)
        max_changes = 5
        changes_made = 0
        while changes_made < max_changes:
            slider_value = int(self.get_contrast_slider_value())
            print("slider_value",slider_value)
            time.sleep(2)
            if slider_value == 0:
                slider.send_keys(Keys.RIGHT)
            elif slider_value == 100:
                slider.send_keys(Keys.LEFT)
            else:
                if changes_made <=3:
                    slider.send_keys(Keys.RIGHT)
                else:
                    slider.send_keys(Keys.LEFT)
            changes_made += 1
        
    def verify_display_control_input_switch_text_lthree_page_keelung32(self):
        return self.driver.get_attribute("display_control_input_switch_text_lthree_page_keelung32", "Name",  timeout = 10)
    
    def verify_display_control_input_switch_tooltip_lthree_page_keelung32(self):
        return self.driver.wait_for_object("display_control_input_switch_tooltip_lthree_page_keelung32",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_color_adjustment_text_lthree_page(self):
        return self.driver.get_attribute("display_control_color_adjustment_text_lthree_page", "Name",  timeout = 10)

    def verify_display_control_low_blue_light_red_slider_lthree_page(self):
        return self.driver.wait_for_object("display_control_low_blue_light_red_slider_lthree_page",raise_e=False, timeout = 10) is not False

    def verify_display_control_low_blue_light_green_slider_lthree_page(self):
        return self.driver.wait_for_object("display_control_low_blue_light_green_slider_lthree_page",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_low_blue_light_blue_slider_lthree_page(self):
        return self.driver.wait_for_object("display_control_low_blue_light_blue_slider_lthree_page",raise_e=False,  timeout = 10)
    
    def select_display_modes_select_box_option_sRGB_web_ltwo_page(self):
        self.driver.click("display_modes_select_box_option_sRGB_web_ltwo_page", timeout = 10)
        time.sleep(5)
    
    def click_display_control_low_blue_light_turnon_dropdown_hrs_eleven_pm_lthree_page(self):
        self.driver.click("display_control_low_blue_light_turnon_dropdown_hrs_eleven_pm_lthree_page", timeout = 10)

    def click_display_control_hdmi_popup_continue_text(self):
        self.driver.click("display_control_hdmi_popup_page_continue_button", timeout = 20)

    def set_display_red_slider_value_for_analytics(self,max_changes=1):
        slider = self.driver.wait_for_object("display_control_low_blue_light_red_slider_lthree_page", timeout = 15)
        max_changes = 5
        changes_made = 0
        while changes_made < max_changes:
            slider_value = int(self.get_display_control_low_blue_light_red_slider_lthree_page())
            print("slider_value",slider_value)
            time.sleep(2)
            if slider_value == 0:
                slider.send_keys(Keys.RIGHT)
            elif slider_value == 100:
                slider.send_keys(Keys.LEFT)
            else:
                if changes_made <=3:
                    slider.send_keys(Keys.RIGHT)
                else:
                    slider.send_keys(Keys.LEFT)
            changes_made += 1

    def set_display_green_slider_value_for_analytics(self,max_changes=1):
        slider = self.driver.wait_for_object("display_control_low_blue_light_green_slider_lthree_page", timeout = 15)
        max_changes = 5
        changes_made = 0
        while changes_made < max_changes:
            slider_value = int(self.get_display_control_low_blue_light_green_slider_lthree_page())
            print("slider_value",slider_value)
            time.sleep(2)
            if slider_value == 0:
                slider.send_keys(Keys.RIGHT)
            elif slider_value == 100:
                slider.send_keys(Keys.LEFT)
            else:
                if changes_made <=3:
                    slider.send_keys(Keys.RIGHT)
                else:
                    slider.send_keys(Keys.LEFT)
            changes_made += 1

    def set_display_blue_slider_value_for_analytics(self,max_changes=1):
        slider = self.driver.wait_for_object("display_control_low_blue_light_blue_slider_lthree_page", timeout = 15)
        max_changes = 5
        changes_made = 0
        while changes_made < max_changes:
            slider_value = int(self.get_display_control_low_blue_light_blue_slider_lthree_page())
            print("slider_value",slider_value)
            time.sleep(2)
            if slider_value == 0:
                slider.send_keys(Keys.RIGHT)
            elif slider_value == 100:
                slider.send_keys(Keys.LEFT)
            else:
                if changes_made <=3:
                    slider.send_keys(Keys.RIGHT)
                else:
                    slider.send_keys(Keys.LEFT)
            changes_made += 1

    def click_display_control_advanced_settings_restore_defaults_do_not_show_again_checkbox_lthree_page(self):
        self.driver.click("display_control_advanced_settings_restore_defaults_do_not_show_again_checkbox_lthree_page", timeout = 10)
    
    def get_brightness_slider_value_from_system_tray(self):
        self.driver.click("system_tray_icon", timeout = 10)
        return self.driver.get_attribute("system_tray_brightness_slider_value", "RangeValue.Value",  timeout = 10)
    
    def click_display_control_out_of_synch_see_more_link_ltwo_page(self):
        self.driver.click("display_control_out_of_synch_see_more_link_ltwo_page", timeout = 10) 

    def click_display_control_out_of_synch_cancel_button_ltwo_page(self):
        self.driver.click("display_control_out_of_synch_cancel_button_ltwo_page", timeout = 10)

    def click_display_control_out_of_synch_discard_changes_button_ltwo_page(self):
        self.driver.click("display_control_out_of_synch_discard_changes_button_ltwo_page", timeout = 10)

    def click_display_control_out_of_synch_keep_new_changes_button_ltwo_page(self):
        self.driver.click("display_control_out_of_synch_keep_changes_button_ltwo_page", timeout = 10)
    
    def click_display_control_restore_defaults_do_not_show_again_checkbox(self):
        self.driver.click("display_control_restore_defaults_do_not_show_again_checkbox", timeout = 10)
    
    def is_display_control_restore_defaults_description_onpopup_window_page_visible(self):
        return self.driver.wait_for_object("display_control_restore_defaults_description_onpopup_window_page",raise_e=False, timeout = 10)

    def get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled(self):
        return self.driver.get_attribute("display_control_display_modes_select_box_ltwo_page", "IsEnabled",  timeout = 20)
    
    def enter_app_name_in_display_control_add_app_search_bar_ltwo_page(self,app_name):
        self.driver.click("display_control_add_app_search_bar_ltwo_page", timeout = 10)
        self.driver.send_keys("display_control_add_app_search_bar_ltwo_page", app_name)
    
    def click_display_control_add_app_continue_button_ltwo_page(self):
        self.driver.click("display_control_add_app_continue_button_ltwo_page", timeout = 10)

    def select_display_control_access_app_on_add_application_popup_lthree_page(self):
        self.driver.click("display_control_access_app_on_add_application_popup_lthree_page", timeout = 10)

    def get_display_control_restore_defaults_do_not_show_again_checkbox_state(self):
        return self.driver.get_attribute("display_control_restore_defaults_do_not_show_again_checkbox", "Toggle.ToggleState",  timeout = 10)
            
    def verify_display_control_out_of_synch_see_more_link_ltwo_page(self):
        return self.driver.wait_for_object("display_control_out_of_synch_see_more_link_ltwo_page",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_out_of_synch_keep_changes_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_out_of_synch_keep_changes_button_ltwo_page", "Name",  timeout = 10)

    def verify_display_control_out_of_synch_discard_changes_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_out_of_synch_discard_changes_button_ltwo_page", "Name",  timeout = 10)
    
    def verify_display_control_out_of_synch_cancel_button_ltwo_page(self):
        return self.driver.get_attribute("display_control_out_of_synch_cancel_button_ltwo_page", "Name",  timeout = 10)
        
    def verify_display_control_advancedsettings_keep_new_changes_button_lthree_page(self):
        return self.driver.get_attribute("display_control_advancedsettings_keep_new_changes_button_lthree_page", "Name",  timeout = 10)
    
    def verify_display_control_advancedsettings_discard_changes_button_lthree_page(self):
        return self.driver.get_attribute("display_control_advancedsettings_discard_changes_button_lthree_page", "Name",  timeout = 10)

    def verify_display_control_advancedsettings_cancel_button_lthree_page(self):
        return self.driver.get_attribute("display_control_advancedsettings_cancel_button_lthree_page", "Name",  timeout = 10)
    
    def click_display_control_advancedsettings_keep_new_changes_button_lthree_page(self):
        self.driver.click("display_control_advancedsettings_keep_new_changes_button_lthree_page", timeout = 10)

    def click_display_control_advancedsettings_discard_changes_button_lthree_page(self):
        self.driver.click("display_control_advancedsettings_discard_changes_button_lthree_page", timeout = 10)
        
    def verify_display_control_display_modes_text_ltwo_page(self):
        return self.driver.get_attribute("display_control_display_modes_text_ltwo_page", "Name",  timeout = 10)

    def verify_display_control_switch_btn_lfour_page(self):
        return self.driver.get_attribute("display_control_switch_btn_lfour_page", "Name",  timeout = 10)
                
    def click_display_control_disney_plus_app(self):
        self.driver.click("display_control_disney_plus_app_ltwo_page", timeout = 10)
        time.sleep(2)#needs time to chnage brightness and mode
            
    def verify_display_control_access_app_ltwo_page(self):
        return self.driver.get_attribute("display_control_access_app_ltwo_page", "Name",  timeout = 10)

    def is_display_control_access_app_ltwo_page_visible(self):
        return self.driver.wait_for_object("display_control_access_app_ltwo_page",raise_e=False, timeout = 10)
    
    def validate_display_control_disney_plus_app_ltwo_page(self):
        return self.driver.wait_for_object("display_control_disney_plus_app_ltwo_page",raise_e=False, timeout = 10) is not False
    
    def validate_display_control_tencent_app_ltwo_page(self):
        return self.driver.wait_for_object("display_control_tencent_app_ltwo_page",raise_e=False, timeout = 10) is not False

    def validate_display_control_iqiyi_app_ltwo_page(self):
        return self.driver.wait_for_object("display_control_iqiyi_app_ltwo_page",raise_e=False, timeout = 10) is not False
    
    def verify_display_control_iqiyi_app_ltwo_page_selected(self):
        return self.driver.get_attribute("display_control_iqiyi_app_ltwo_page", "SelectionItem.IsSelected",  timeout = 10)
    
    def verify_display_control_disney_plus_app_ltwo_page_selected(self):
        return self.driver.get_attribute("display_control_disney_plus_app_ltwo_page", "SelectionItem.IsSelected",  timeout = 10)

    def verify_display_control_tencent_app_ltwo_page_seleted(self):
        return self.driver.get_attribute("display_control_tencent_app_ltwo_page", "SelectionItem.IsSelected",  timeout = 10)

    def verify_display_control_all_application_button_ltwo_page_selected(self):
        return self.driver.get_attribute("display_control_all_application_button_ltwo_page", "SelectionItem.IsSelected",  timeout = 10)
    
    def verify_is_display_control_access_app_selected(self):
        time.sleep(2)
        return self.driver.get_attribute("display_control_access_app_ltwo_page", "SelectionItem.IsSelected", timeout = 10)
    
    def click_display_control_access_app_ltwo_page(self):
        self.driver.click("display_control_access_app_ltwo_page", timeout = 10)
        
    def verify_display_control_calculator_app_ltwo_page(self):
        return self.driver.get_attribute("display_control_calculator_app_ltwo_page", "Name",  timeout = 10)
    
    def click_display_control_calculator_app_ltwo_page(self):
        self.driver.click("display_control_calculator_app_ltwo_page", timeout = 10)

    def verify_display_control_restore_defaults_button_lthree_page(self):
        return self.driver.get_attribute("display_control_restore_defaults_button_lthree_page", "Name",  timeout = 10)
    
    def select_display_control_calculator_app_on_add_application_popup_lthree_page(self):
        self.driver.hover("display_control_calculator_app_on_add_application_popup_lthree_page")
        self.driver.click("display_control_calculator_app_on_add_application_popup_lthree_page", timeout = 10)

    def verify_display_control_calculator_app_on_add_application_popup_lthree_page(self):
        return self.driver.get_attribute("display_control_calculator_app_on_add_application_popup_lthree_page", "Name",  timeout = 10)
    
    def element_has_keyboard_focus(self,element):
        return self.driver.get_attribute(element, "HasKeyboardFocus",  timeout = 10)
    
    def set_slider_value(self, slider, desired_value):
        slider_element = self.driver.wait_for_object(slider, timeout=30)
        self.driver.click(slider, timeout=20)
        
        current_slider_value = int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20))
        slider_difference = current_slider_value - desired_value
        timeout = 0

        if slider_difference > 0:
            while ((current_slider_value - desired_value) > 0):
                if current_slider_value == desired_value:
                    time.sleep(5)
                    if int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20)) == desired_value:
                        break
                if timeout >= 200:
                    break
                slider_element.send_keys(Keys.LEFT)
                current_slider_value = int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20))
                timeout += 1
                
        else:
            while ((current_slider_value - desired_value) < 0):
                if current_slider_value == desired_value:
                    time.sleep(5)
                    if int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20)) == desired_value:
                        break
                if timeout >= 200:
                    break
                slider_element.send_keys(Keys.RIGHT)
                current_slider_value = int(self.driver.get_attribute(slider, "Value.Value",  timeout = 20))
                timeout += 1

    def click_back_arrow_to_navigate_to_previous_page(self):
        self.driver.click("back_arrow_to_navigate_to_previous_page", timeout = 10)
    
    def click_title_bar(self):
        self.driver.click("display_control_title_bar",timeout = 10)
    
    def verify_display_control_delete_profile_continue_btn(self):
        return self.driver.get_attribute("display_control_delete_profile_continue_btn", "Name",  timeout = 10)
    
    def click_display_control_hdmi_link(self, element):
        time.sleep(5)
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        self.driver.click(element,timeout=10)
        el.send_keys(Keys.TAB)
        time.sleep(3)
        el.send_keys(Keys.ENTER)

    def click_hdmi_link_skip_btn_lfour_page(self):
        self.driver.click("display_control_advancedsettings_hdmi_link_skip_button", timeout = 10)
    
    def get_display_control_advancedsettings_hdmi_link_skip_button(self):
        return self.driver.get_attribute("display_control_advancedsettings_hdmi_link_skip_button", "Name",  timeout = 10)

    def get_display_control_hdmi_link_title_text(self):
        return self.driver.get_attribute("display_control_hdmi_link_title_text", "Name",  timeout = 10)
    
    def get_display_control_hdmi_link_text_lthree_page(self):
        return self.driver.get_attribute("display_control_hdmi_link_text_lthree_page", "Name",  timeout = 10)

    def get_display_control_hdmi_popup_description_1_text(self):
        return self.driver.get_attribute("display_control_hdmi_popup_description_1_text", "Name",  timeout = 10)
    
    def click_display_control_next_btn_hdmi_popup_window(self):
        self.driver.click("display_control_next_btn_hdmi_popup_window", timeout = 10)
        
    def get_display_control_next_btn_hdmi_popup_window(self):
        return self.driver.get_attribute("display_control_next_btn_hdmi_popup_window", "Name",  timeout = 10)
    
    def get_display_control_back_to_pc_desktop_description_2_hdmi_popup_page(self):
        return self.driver.get_attribute("display_control_back_to_pc_desktop_description_2_hdmi_popup_page", "Name",  timeout = 10)
    
    def get_display_control_hdmi_popup_page_do_not_show_again_text(self):
        return self.driver.get_attribute("display_control_hdmi_popup_page_do_not_show_again_text", "Name",  timeout = 10)
    
    def get_display_control_hdmi_popup_page_cancel_button(self):
        return self.driver.get_attribute("display_control_hdmi_popup_page_cancel_button", "Name",  timeout = 10)

    def get_display_control_hdmi_popup_page_continue_button(self):
        return self.driver.get_attribute("display_control_hdmi_popup_page_continue_button", "Name",  timeout = 10)
    
    def get_display_control_hdmi_popup_description_2_text(self):
        return self.driver.get_attribute("display_control_hdmi_popup_description_2_text", "Name", timeout = 10)
    
    def get_display_control_hdmi_popup_description_3_text(self):
        return self.driver.get_attribute("display_control_hdmi_popup_description_3_text", "Name",  timeout = 10)
    
    def get_display_control_close_btn_hdmi_popup_window(self):
        return self.driver.get_attribute("display_control_close_btn_hdmi_popup_window","Name", timeout = 10)
    
    def scroll_modes(self, direction, desired_mode_name, desired_mode_id):
        if self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 15) is False:
            self.driver.click("display_control_display_modes_select_box_ltwo_page", timeout = 10)
            time.sleep(2)
        scroll_mode = self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 10)
        found_mode = False
        for _ in range(30):
            key = Keys.UP if direction == "up" else Keys.DOWN
            scroll_mode.send_keys(key)
            scroll_mode.send_keys(key)
            self.click_title_bar()
            if self.verify_display_modes_dropdown_value(desired_mode_id) == desired_mode_name:
                time.sleep(2)
                found_mode = True
                break
        if not found_mode: #This is to ensure that we scroll through the list if the first attempt fails
            for _ in range(30):
                key = Keys.DOWN if direction == "up" else Keys.UP # this is to ensure that we scroll in the opposite direction if the first attempt fails
                scroll_mode.send_keys(key)
                scroll_mode.send_keys(key)
                self.click_title_bar()
                if self.verify_display_modes_dropdown_value(desired_mode_id) == desired_mode_name:
                    time.sleep(2)
                    break
        self.click_title_bar() # Traversing list can lock up application. This is a workaround.
    
    def click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page(self):
        self.driver.click("display_control_restore_defaults_continue_onpopup_window_page_lthree_page", timeout = 10)
        time.sleep(20)#system takes some time to restore values.

    def click_display_control_low_blue_light_red_slider_lthree_page(self):
        self.driver.click("display_control_low_blue_light_red_slider_lthree_page",  timeout = 10)

    def click_display_control_low_blue_light_blue_slider_lthree_page(self):
        self.driver.click("display_control_low_blue_light_blue_slider_lthree_page",  timeout = 10)

    def click_display_control_low_blue_light_green_slider_lthree_page(self):
        self.driver.click("display_control_low_blue_light_green_slider_lthree_page",  timeout = 10)
    
    def verify_display_control_restore_defaults_continue_onpopup_window_page_lthree_page(self):
        return self.driver.wait_for_object("display_control_restore_defaults_continue_onpopup_window_page_lthree_page",raise_e=False, timeout = 10)
    
    def get_display_control_for_all_applications_text(self):
        return self.driver.get_attribute("display_control_for_all_applications_text", "Name",  timeout = 10)

    def verify_display_control_add_application_text_show_in_app_list(self):
        return self.driver.wait_for_object("display_control_for_add_applications_text_in_app_list",raise_e=False, timeout = 10)
    
    def search_apps_on_search_frame(self, app_name):
        self.driver.click("display_control_add_app_search_bar_ltwo_page")
        self.driver.send_keys("display_control_add_app_search_bar_ltwo_page", app_name)

    def click_searched_app_on_search_frame(self):
        self.driver.click("display_control_access_app_on_add_application_popup_lthree_page")

    def verify_serached_app_is_be_selected(self):
        return self.driver.wait_for_object("display_control_access_app_on_add_application_popup_lthree_page", raise_e=False, timeout=10)
    
    def verify_access_app_show_on_application_list(self):
        return self.driver.wait_for_object("access_on_application_list", raise_e=False, timeout=10)

    def click_cancel_button_on_dialog(self):
        self.driver.click("cancel_button_on_dialog")

    def verify_calculator_app_show_on_application_list(self):
        return self.driver.wait_for_object("calculator_on_application_list", raise_e=False, timeout=10)
    
    def verify_arrow_next_on_application_list(self):
        return self.driver.wait_for_object("arrow_next_on_application_list", raise_e=False, timeout=10)

    def verify_all_app_show_on_application_list(self, app_elemetns):
        return self.driver.wait_for_object(app_elemetns, raise_e=False, timeout=10)

    def verify_display_control_add_app_continue_button_ltwo_page(self):
        return self.driver.wait_for_object("display_control_add_app_continue_button_ltwo_page", raise_e=False, timeout=10)

    def verify_disney_plus_app_ltwo_page(self):
        return self.driver.wait_for_object("disney", raise_e=False, timeout=10)
    
    def verify_tencent_app_ltwo_page(self):
        return self.driver.wait_for_object("tencent", raise_e=False, timeout=10)
    
    def verify_iqiyi_app_ltwo_page(self):
        return self.driver.wait_for_object("iqiyi", raise_e=False, timeout=10)

    def click_disney_plus_app_ltwo_page(self):
        self.driver.click("disney", timeout=10)

    def click_tencent_app_ltwo_page(self):
        self.driver.click("tencent", timeout=10)

    def click_iqiyi_app_ltwo_page(self):
        self.driver.click("iqiyi", timeout=10)

    def click_display_control_delete_profile_button(self):
        self.driver.click("display_control_delete_profile_button", timeout=10)

    def verify_delete_profil_dialog_delete_profile_text_show(self):
        return self.driver.wait_for_object("delete_profile_dialog_delete_profile_text", raise_e=False, timeout=10)
    
    def verify_delete_profile_dialog_description_text(self):
        return self.driver.get_attribute("delete_profile_dialog_description_text", "Name", timeout=10)
    
    def verify_delete_profile_dialog_cancel_button_show(self):
        return self.driver.get_attribute("delete_profile_dialog_cancel_button", "Name", timeout=10)
    
    def click_delete_profile_dialog_cancel_button(self):
        self.driver.click("delete_profile_dialog_cancel_button", timeout=10)

    def verify_delete_profile_dialog_continue_button_show(self):
        return self.driver.get_attribute("delete_profile_dialog_continue_button", "Name", timeout=10)
    
    def click_delete_profile_dialog_continue_button(self):
        self.driver.click("delete_profile_dialog_continue_button", timeout=10)

    def verify_delete_profile_dialog_do_not_show_again_checkbox_show(self):
        return self.driver.wait_for_object("display_control_delete_profile_checkbox_ltwo_page", timeout=10)

    def click_delete_profile_dialog_do_not_show_again_checkbox(self):
        self.driver.click("display_control_delete_profile_checkbox_ltwo_page", timeout=10)

    def get_delete_profile_dialog_do_not_show_again_checkbox_checked(self):
        return self.driver.get_attribute("display_control_delete_profile_checkbox_ltwo_page", "Toggle.ToggleState", timeout=10)
    
    def verify_camera_app_ltwo_page(self):
        return self.driver.wait_for_object("camera", raise_e=False, timeout=10)
    
    def click_camera_app_ltwo_page(self):
        self.driver.click("camera", timeout=10)
    
    def verify_command_prompt_app_ltwo_page(self):
        return self.driver.wait_for_object("command_prompt", raise_e=False, timeout=10)
    
    def click_command_prompt_app_ltwo_page(self):
        self.driver.click("command_prompt", timeout=10)

    def verify_media_player_app_ltwo_page(self):
        return self.driver.wait_for_object("media_player", raise_e=False, timeout=10)
    
    def click_media_player_app_ltwo_page(self):
        self.driver.click("media_player", timeout=10)
    
    def verify_magnify_app_ltwo_page(self):
        return self.driver.wait_for_object("magnify", raise_e=False, timeout=10)
    
    def click_magnify_app_ltwo_page(self):
        self.driver.click("magnify", timeout=10)

    def verify_paint_app_ltwo_page(self):
        return self.driver.wait_for_object("paint", raise_e=False, timeout=10)
    
    def click_paint_app_ltwo_page(self):
        self.driver.click("paint", timeout=10)

    def verify_news_app_ltwo_page(self):
        return self.driver.wait_for_object("news", raise_e=False, timeout=10)
    
    def click_news_app_ltwo_page(self):
        self.driver.click("news", timeout=10)
    
    def send_alt_f4_to_active_element(self):
        """
        Send Alt+F4 to the currently focused/active element
        Uses any available element as a reference point
        """
        try:
            # Try to get any available element to send the key combination
            element = self.driver.wait_for_object("_system_close_btn", timeout=5)
            element.send_keys(Keys.ALT, Keys.F4)
            time.sleep(2)
            return True
        except Exception as e:
            logging.info(f"Failed to send Alt+F4 to active element: {e}")
            return False
    
    def click_display_control_previous_btn_hdmi_popup_window(self):
        self.driver.click("display_control_previous_btn_hdmi_popup_window")

    def get_display_control_advanced_display_settings_title_lthree_page(self):
        return self.driver.get_attribute("display_control_advanced_display_settings_title_lthree_page", "Name", timeout=10)
   
    def click_display_mode_select_mode_ltwo_page(self,element):
        el=self.driver.wait_for_object(element, raise_e=False, timeout=10)
        if not el:
            logging.info(f"{element} mode not displayed")
            time.sleep(2)
        else:
            self.driver.hover(element)
            el.send_keys(Keys.ENTER)
    
    def click_display_control_contrast_toggle_to_on(self):
        for _ in range(3):
            if self.driver.get_attribute("display_control_contrast_toggle", "Toggle.ToggleState", timeout=10) == "0":
                self.driver.hover("display_control_contrast_toggle")
                self.driver.click("display_control_contrast_toggle")
                time.sleep(20)
                
    def verify_display_control_contrast_toggle(self):
        return self.driver.wait_for_object("display_control_contrast_toggle", raise_e=False, timeout=10) is not False
    
    def verify_display_control_advanced_display_settings_title_lthree_page(self):
        return self.driver.wait_for_object("display_control_advanced_display_settings_title_lthree_page", raise_e=False, timeout=10) is not False

    @screenshot_compare(root_obj="display_control_card_module_image",include_param=["machine_type"],pass_ratio=0.08)
    def verify_display_control_card_lone_image(self,machine_type, raise_e=True):
        return self.driver.wait_for_object("display_control_advanced_settings_restore_defaults_button_ltwo_page", raise_e=raise_e, timeout=10)

    @screenshot_compare(root_obj="display_control_card_module_image",include_param=["machine_type"],pass_ratio=0.02)
    def verify_display_control_card_ltwo_page(self,machine_type,raise_e=True):
        return self.driver.wait_for_object("display_control_restore_defaults_button_lthree_page", raise_e=raise_e, timeout=10)

    def hover_on_element(self,element):
        self.driver.hover(element)
    
    def click_camera_app_on_install_modal(self):
        self.driver.click("camera_app_on_install_modal", timeout=10)

    def verify_focus_on_element(self, element):
        return self.driver.get_attribute(element, "IsKeyboardFocusable",  timeout=10)

    def verify_app_carousel_isSelected(self, element):
        return self.driver.get_attribute(element, "SelectionItem.IsSelected", timeout=10)

    def verify_app_name_on_carousel(self,element):
        return self.driver.get_attribute(element,"Name", timeout=10)
    
    def click_use_hdmi_input_tooltip(self):
        self.driver.click("use_hdmi_input_tooltip", timeout=10)

    def get_use_hdmi_input_tooltip(self):
        return self.driver.get_attribute("use_hdmi_input_tooltip", "Name", timeout=10)
    
    def scroll_modes_native(self, direction, desired_mode_name, desired_mode_id):
        if self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 15) is False:
            self.driver.click("display_control_display_modes_select_box_ltwo_page", timeout = 10)
            time.sleep(2)
        scroll_mode = self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 10)
        for _ in range(30):
            key = Keys.UP if direction == "up" else Keys.DOWN
            scroll_mode.send_keys(key)
            scroll_mode.send_keys(key)
            scroll_mode.send_keys(key)
            self.click_title_bar()
            if self.verify_display_modes_dropdown_value(desired_mode_id) == desired_mode_name:
                time.sleep(2)
                break
        self.click_title_bar() # Traversing list can lock up application. This is a workaround.

    @screenshot_compare(root_obj="display_control_card_module_image",include_param=["machine_name", "page_number", "scale"], pass_ratio=0.01)
    def verify_display_lone_page(self, machine_name, page_number, element, scale, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    @screenshot_compare(root_obj="display_control_card_module_image",include_param=["machine_name", "page_number", "scale"], pass_ratio=0.01)
    def verify_display_ltwo_page(self, machine_name, page_number, element, scale, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

    @screenshot_compare(pass_ratio=0.02)
    def verify_color_filter(self):
        return self.driver.wait_for_object("display_control_text_ltwo_page", raise_e=False, timeout=10)

    def verify_display_control_out_of_sync_see_more_link(self):
        return self.driver.wait_for_object("display_control_out_of_sync_see_more_link_ltwo_page", raise_e=False, timeout=10) is not False

    def click_display_control_out_of_sync_see_more_link(self):
        self.driver.click("display_control_out_of_sync_see_more_link_ltwo_page", timeout = 10)

    def verify_display_control_advanced_settings_out_of_sync_see_more_link(self):
        return self.driver.wait_for_object("display_control_out_of_sync_see_more_link_lthree_page", raise_e=False, timeout=10) is not False

    def click_display_control_advanced_settings_out_of_sync_see_more_link(self):
        self.driver.click("display_control_out_of_sync_see_more_link_lthree_page", timeout = 10)

    def click_display_control_advancedsettings_cancel_button_lthree_page(self):
        self.driver.click("display_control_advancedsettings_cancel_button_lthree_page", timeout = 10)
    
    def click_display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page(self):
        self.driver.click("display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page", timeout = 10)
    
    def click_display_control_input_switch_tooltip_lthree_page_keelung32(self):
        self.driver.click("display_control_input_switch_tooltip_lthree_page_keelung32", timeout = 10)
    
    def click_display_control_adjust_contrast_tooltip_ltwo_page(self):
        self.driver.click("display_control_adjust_contrast_tooltip_ltwo_page", timeout = 10)
    
    def click_display_control_close_btn_hdmi_popup_window(self):
        self.driver.click("display_control_close_btn_hdmi_popup_window", timeout = 10)
    
    def click_display_control_hdr_toggle_off_btn_ltwo_page(self):
        #added to click hdr togle till it's off
        self.driver.click("display_control_hdr_toggle_switch_ltwo_page", timeout = 15)
        #added for loop coz toggle sometimes not getting enabled in first click
        for _ in range(5):
            if self.get_display_control_hdr_toggle_switch_ltwo_page() == "0":
                break
            else:
                self.driver.click("display_control_hdr_toggle_switch_ltwo_page", timeout = 15)

    def select_last_display_mode(self):
        scroll_mode = self.driver.wait_for_object("display_modes_list_window_ltwo_page", timeout = 10)
        scroll_mode.send_keys(Keys.END)
    
    def scroll_up_down(self, distance=1,direction="down"):
        el=self.driver.wait_for_object("display_control_card_module_image", timeout=10)
        for _ in range(distance):
            if direction == "down":
                el.send_keys(Keys.PAGE_DOWN)
            elif direction == "up":
                el.send_keys(Keys.PAGE_UP)