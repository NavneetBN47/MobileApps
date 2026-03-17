from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class SanityCheck(HPXFlow):
    flow_name = "sanity_check"

    def verify_support_module_show(self):
        return self.driver.wait_for_object("support_module_title", raise_e=False, timeout=20)
    
    def verify_programmable_key_module_show(self):
        return self.driver.wait_for_object("programmable_title", raise_e=False, timeout=20)

    def verify_old_programmable_key_module_show(self):
        return self.driver.wait_for_object("programmable_save_button", raise_e=False, timeout=20)
    
    def verify_smartCamV3_module_show(self):
        return self.driver.wait_for_object("smartCamV3_camera", raise_e=False, timeout=30)
    
    def verify_home_module_show(self):
        return self.driver.wait_for_object("home_section_title", raise_e=False, timeout=20)
    
    def verify_display_control_show(self):
        return self.driver.wait_for_object("display_control_module", raise_e=False, timeout=20)

    def close_smartcamV3_module(self):
        self.driver.click("smartCamV3_camera")
        time.sleep(2)
        self.driver.click("smartcamV3_close_btn")

    def check_top_build_version(self):
        return self.driver.wait_for_object("top_build_version", raise_e=False, timeout=20)

    
    def verify_privacy_alert_module_show(self):
        return self.driver.wait_for_object("snooze_duration_text", raise_e=False, timeout=20)

    def verify_auto_dimming_module_show(self):
        return self.driver.wait_for_object("dimming_restore_button", raise_e=False, timeout=20)


    def verify_5G_module_show(self):
        return self.driver.wait_for_object("fiveG_connectivity", raise_e=False, timeout=20)
    
    def verify_rgb_keyboard_module_show(self):
        return self.driver.wait_for_object("enable_rgb_lighting", raise_e=False, timeout=20)

    def verify_pen_control_module_show(self):
        return self.driver.wait_for_object("pen_top_button", raise_e=False, timeout=20)
    
    def verify_pc_device_section_action(self):
        return self.driver.wait_for_object("pc_device_section", raise_e=False, timeout=20)
    
    def click_support_card(self):
        self.driver.wait_for_object("support_card", raise_e=False, timeout=20)
        self.driver.click("support_card")

    def verify_support_guide_title_show(self):
        return self.driver.wait_for_object("support_guide_title", raise_e=False, timeout=20)
    
    def click_bell_icon(self):
        self.driver.wait_for_object("bell_icon", raise_e=False, timeout=20)
        self.driver.click("bell_icon")
    
    def verify_notfication_tips_show(self):
        return self.driver.wait_for_object("notifications_tips", raise_e=False, timeout=20)
    
    def verify_bell_flyout_notification_show(self):
        return self.driver.wait_for_object("bell_flyout_notification", raise_e=False, timeout=20)
    
    def get_notfications_tips_text(self):
        return self.driver.get_attribute("notifications_tips", "Name")
    
    def get_new_message_text(self):
        return self.driver.get_attribute("new_message", "Name")
    
    def verify_system_control_subtitle_show_consumer(self):
        return self.driver.wait_for_object("system_control_subtitle_consumer", raise_e=False, timeout=20)
    
    def verify_system_control_subtitle_show_commercial(self):
        return self.driver.wait_for_object("system_control_subtitle_commercial", raise_e=False, timeout=20)
    
    def verify_screen_time_subtitle(self):
        return self.driver.wait_for_object("screen_time_subtitle", raise_e=False, timeout=20)
    
    def verify_screen_distance_subtitle_show(self):
        return self.driver.wait_for_object("screen_distance_subtitle", raise_e=False, timeout=20)
    
    def verify_touchpad_show(self):
        return self.driver.wait_for_object("touchpad_title", raise_e=False, timeout=20)
    
    def get_gesture_control_text(self):
        return self.driver.get_attribute("touchpad_gesture_control", "Name")
    
    def verify_pen_right_click_show(self):
        return self.driver.wait_for_object("right_itg", raise_e=False, timeout=20)
    
    def verify_home_next_step_title_show(self):
        return self.driver.wait_for_object("home_next_step", raise_e=False, timeout=20)
    
    def verify_audio_module_show(self):
        return self.driver.wait_for_object("audio_module_itg", raise_e=False, timeout=20)
    
    def verify_home_audio_card_show(self):
        return self.driver.wait_for_object("audio_card_home", raise_e=False, timeout=20)

    def verify_battery_information_show(self):
        return self.driver.wait_for_object("battery_information", raise_e=False, timeout=20)

    def verify_charging_options_show(self):
        return self.driver.wait_for_object("charging_options", raise_e=False, timeout=20)
    
    def verify_attention_focus_show(self):
        return self.driver.wait_for_object("attention_focus", raise_e=False, timeout=20)
    
    def verify_onlooker_detection_show(self):
        return self.driver.wait_for_object("onlooker_detection", raise_e=False, timeout=20)
    
    def verify_enable_screen_blur_show(self):
        return self.driver.wait_for_object("enable_screen_blur", raise_e=False, timeout=20)