from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time
 
class Gesture(HPXFlow):
    flow_name = "gesture"
 
    def click_gesture_card(self):
        self.driver.click("gesture_card")
 
    def verify_gesture_panel_banner_show(self):
        return self.driver.wait_for_object("gesture_panel_banner", raise_e=False, timeout=10)
   
    def verify_gesture_panel_banner_description(self):
        return self.driver.wait_for_object("previewing_pause_resume_strings_under_gesture_panel", raise_e=False, timeout=10)
   
    def verify_try_this_gesture_button_show(self):
        return self.driver.wait_for_object("try_this_gesture_button", raise_e=False, timeout=10)
    
    def click_try_this_gesture_button(self):
        self.driver.click("try_this_gesture_button")
   
    def click_pause_resume_card(self):
        self.driver.click("pause_resume_card")

    def is_pause_resume_card_selected(self):
        return self.driver.get_attribute("pause_resume_card_enable", "Toggle.ToggleState")
    
    def is_pause_resume_card_not_selected(self):
        return self.driver.get_attribute("pause_resume_card_disable", "Toggle.ToggleState")
    
    def verify_pause_resume_card_title_show(self):
        return self.driver.wait_for_object("pause_resume_card_title", raise_e=False, timeout=10)
   
    def verify_pause_resume_toggle_show(self):
        return self.driver.wait_for_object("pause_resume_toggle", raise_e=False, timeout=10)
   
    def click_pause_resume_toggle(self):
        self.driver.click("pause_resume_toggle")

    def verify_pause_resume_card_description_show(self):
        return self.driver.wait_for_object("pause_resume_card_description", raise_e=False, timeout=10)
 
    def is_pause_resume_toggle_enabled(self):
        return self.driver.get_attribute("pause_resume_toggle", "Toggle.ToggleState")
   
    def verify_volume_adjust_card_title_show(self):
        return self.driver.wait_for_object("volume_adjust_card_title", raise_e=False, timeout=10)
   
    def verify_volume_adjust_toggle_show(self):
        return self.driver.wait_for_object("volume_adjust_toggle", raise_e=False, timeout=10)
    
    def click_volume_adjust_toggle(self):
        self.driver.click("volume_adjust_toggle")

    def is_volume_adjust_card_not_selected(self):
        return self.driver.get_attribute("volume_adjust_card_disable", "Toggle.ToggleState")
    
    def is_volume_adjust_card_selected(self):
        return self.driver.get_attribute("volume_adjust_card_enable", "Toggle.ToggleState")
    
    def click_volume_adjust_card(self):
        self.driver.click("volume_adjust_card")
   
    def verify_volume_adjust_card_description_show(self):
        return self.driver.wait_for_object("volume_adjust_card_description", raise_e=False, timeout=10)
   
    def is_volume_adjust_toggle_enabled(self):
        return self.driver.get_attribute("volume_adjust_toggle", "Toggle.ToggleState")
   
    def verify_page_scroll_card_title_show(self):
        return self.driver.wait_for_object("page_scroll_card_title", raise_e=False, timeout=10)
   
    def verify_page_scroll_toggle_show(self):
        return self.driver.wait_for_object("page_scroll_toggle", raise_e=False, timeout=10)
    
    def click_page_scroll_toggle(self):
        self.driver.click("page_scroll_toggle")
   
    def verify_page_scroll_card_description_show(self):
        return self.driver.wait_for_object("page_scroll_card_description", raise_e=False, timeout=10)
   
    def is_page_scroll_toggle_enabled(self):
        return self.driver.get_attribute("page_scroll_toggle", "Toggle.ToggleState")
    
    def verify_restore_defaults_button_show(self):
        return self.driver.wait_for_object("restore_defaults_button", raise_e=False, timeout=10)
       
    def verify_settings_button_on_gesture_page_show(self):
        return self.driver.wait_for_object("settings_button_on_gesture_page", raise_e=False, timeout=10)
   
    def click_settings_button_on_gesture_page(self):
        self.driver.click("settings_button_on_gesture_page")
 
    def verify_advanced_settings_page_close_button_show(self):
        return self.driver.wait_for_object("advanced_settings_page_close_button", raise_e=False, timeout=10)
 
    def verify_advanced_settings_page_title_show(self):
        return self.driver.wait_for_object("advanced_settings_page_title", raise_e=False, timeout=10)
   
    def verify_advanced_settings_page_second_title_show(self):
        return self.driver.wait_for_object("advanced_settings_page_second_title", raise_e=False, timeout=10)
 
    def verify_feedback_message_toggle_show(self):
        return self.driver.wait_for_object("feedback_message_toggle", raise_e=False, timeout=10)
   
    def is_feedback_message_toggle_enabled(self):
        return self.driver.get_attribute("feedback_message_toggle", "Toggle.ToggleState")
    
    def click_feedback_message_toggle(self):
        self.driver.click("feedback_message_toggle")
   
    def verify_feedback_message_description_show(self):
        return self.driver.wait_for_object("feedback_message_description", raise_e=False, timeout=10)
   
    def verify_picture_on_advanced_settings_page_show(self):
        return self.driver.wait_for_object("picture_on_advanced_settings_page", raise_e=False, timeout=10)
   
    def click_close_button_on_advanced_settings_page(self):
        self.driver.click("advanced_settings_page_close_button")

    def verify_play_pause_title_show(self):
        return self.driver.wait_for_object("play_pause_title", raise_e=False, timeout=10)
    
    def verify_play_pause_description_show(self):
        return self.driver.wait_for_object("play_pause_description", raise_e=False, timeout=10)
    
    def verify_play_pause_close_button_show(self):
        return self.driver.wait_for_object("play_pause_close_button", raise_e=False, timeout=10)
    
    def verify_play_pause_start_button_show(self):
        return self.driver.wait_for_object("play_pause_start_button", raise_e=False, timeout=10)
    
    def click_play_pause_start_button(self):
        self.driver.click("play_pause_start_button")

    def click_play_pause_close_button(self):
        self.driver.click("play_pause_close_button")

    def verify_photo_scroll_card_title_show(self):
        return self.driver.wait_for_object("photo_scroll_card_title", raise_e=False, timeout=10)
    
    def verify_photo_scroll_toggle_show(self):
        return self.driver.wait_for_object("photo_scroll_toggle", raise_e=False, timeout=10)
    
    def click_photo_scroll_toggle(self):
        self.driver.click("photo_scroll_toggle")
    
    def verify_photo_scroll_card_description_show(self):
        return self.driver.wait_for_object("photo_scroll_description", raise_e=False, timeout=10)
    
    def is_photo_scroll_toggle_enabled(self):
        return self.driver.get_attribute("photo_scroll_toggle", "Toggle.ToggleState")
    
    def click_restore_defaults_button(self):
        self.driver.click("restore_defaults_button")
    
    def click_restore_button(self):
        self.driver.click("restore_button")
    
    def click_restore_defaults_button(self):
        self.driver.click("restore_defaults_button")
    
    def click_pop_window_restore_defaults_button(self):
        self.driver.click("pop_window_restore_button")
