import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys
from SAF.decorator.saf_decorator import screenshot_compare

class PenControl(HPXRebrandingFlow):
    flow_name = "pen_control"

    def get_customize_buttons_restore_default_button_text(self):
        return self.driver.get_attribute("restore_default_customize_button_ltwo_page","Name", timeout=15)
     
    def get_pen_title(self):
        return self.driver.get_attribute("pen_title","Name", timeout=20)

    def get_erase_text_commercial(self):
        return self.driver.get_attribute("customize_lower_barrel_button_erase","Name", timeout = 15)

    def get_apps(self):
        return self.driver.get_attribute("apps","Name", timeout = 15)

    def get_media_control(self):
        return self.driver.get_attribute("media_control","Name", timeout = 15)

    def click_media_control_dropdown(self):
        self.driver.click("media_control_dropdown", timeout = 15)

    def get_productivity(self):
        return self.driver.get_attribute("productivity","Name", timeout = 15)

    def click_more_link_on_app_consumer(self):
        self.driver.click("more_link_on_app_consumer", timeout = 15)
    
    def click_upper_barrel_button_commercial(self):
        self.driver.click("customize_upper_barrel_button", timeout =15)
        
    def click_lower_barrel_button_commercial(self):
        self.driver.click("customize_lower_barrel_button", timeout =15)
    
    def click_single_press_button_commercial(self):
        self.driver.click("customize_top_button_single_press", timeout =15)
        
    def click_double_press_button_commercial(self):
        self.driver.click("customize_top_button_double_press", timeout =15)

    def click_long_press_button_commercial(self):
        self.driver.click("customize_top_button_long_press", timeout =15)

    def verify_single_press_button_show(self):
        return self.driver.wait_for_object("single_press_title", raise_e=False, timeout=20)

    def verify_double_press_button_show(self):
        return self.driver.wait_for_object("double_press_button", raise_e=False, timeout=20)

    def verify_long_press_button_show(self):
        return self.driver.wait_for_object("long_press_button", raise_e=False, timeout=20)

    def verify_single_press_side_menu_title_commercial(self):
        return self.driver.get_attribute("single_press_title","Name", timeout = 15)    

    def scroll_touch_on_off_element_commercial(self):
        self.driver.send_keys("touch_on_off_text_commercial", Keys.PAGE_UP)

    def get_page_up_text_commercial(self):
        return self.driver.get_attribute("page_up_text_commercial","Name", timeout = 15)

    def get_page_down_text_commercial(self):
        return self.driver.get_attribute("page_down_text_commercial","Name", timeout = 15)

    def get_touch_on_off_text_commercial(self):
        return self.driver.get_attribute("touch_on_off_text_commercial","Name", timeout = 15)
    
    def click_customize_button_touch_on_off_text(self):
        self.driver.hover("touch_on_off_text_commercial")
        self.driver.click("touch_on_off_text_commercial", timeout = 10)

    def get_pen_menu_text_commercial(self):
        return self.driver.get_attribute("pen_menu_text_commercial","Name", timeout = 15)
    
    def click_customize_button_pen_menu_text(self):
        self.driver.hover("pen_menu_text_commercial")
        self.driver.click("pen_menu_text_commercial", timeout = 10)

    def get_disabled_text_commercial(self):
        return self.driver.get_attribute("disabled_text_commercial","Name", timeout = 15)
    
    def click_customize_button_disabled_text(self):
        self.driver.click("disabled_text_commercial", timeout = 10)

    def get_screen_snipping_text_commercial_selecion(self):
        return self.driver.get_attribute("screen_snipping_text_commercial_selection","Name", timeout = 15)

    def get_screen_snipping_text_commercial(self):
        return self.driver.get_attribute("screen_snipping_text_commercial","Name", timeout = 15)
    
    def click_customize_button_screen_snipping_text(self):
        self.driver.hover("screen_snipping_text_commercial")
        self.driver.click("screen_snipping_text_commercial", timeout = 10)

    def get_windows_search_text_commercial(self):
        return self.driver.get_attribute("windows_search_text_commercial","Name", timeout = 15)
    
    def click_customize_button_windows_search_text(self):
        self.driver.click("windows_search_text_commercial", timeout = 15)

    def get_web_browser_text_commercial(self):
        return self.driver.get_attribute("web_browser_text_commercial","Name", timeout = 15)
    
    def click_customize_button_web_browser_text(self):
        self.driver.hover("web_browser_text_commercial")
        self.driver.click("web_browser_text_commercial", timeout = 10)

    def get_ms_whiteboard_text_commercial(self):
        return self.driver.get_attribute("customize_top_button_single_press_ms_whiteboard","Name", timeout = 15)
    
    def click_customize_button_ms_whiteboard_text(self):
        self.driver.hover("customize_top_button_single_press_ms_whiteboard")
        self.driver.click("customize_top_button_single_press_ms_whiteboard", timeout = 10)

    def get_switch_application_text_commercial(self):
        return self.driver.get_attribute("customize_top_button_single_press_switch_application","Name", timeout = 15)  
    
    def click_customize_button_switch_application_text(self):
        self.driver.hover("customize_top_button_single_press_switch_application")
        self.driver.click("customize_top_button_single_press_switch_application", timeout = 10)

    def get_play_pause_text_commercial(self):
        return self.driver.get_attribute("play_pause_text_commercial","Name", timeout = 15)
    
    def get_email_text_commercial(self):
        return self.driver.get_attribute("email_text_commercial","Name", timeout = 15)
    
    def click_customize_button_email_text(self):
        self.driver.hover("email_text_commercial")
        self.driver.click("email_text_commercial", timeout = 10)
    
    def click_email_text_commercial(self):
        self.driver.click("pen_control_customize_btn_upper_barrel_btn_email_radio_btn_lthree_page", timeout = 15)
        if self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_email_radio_btn_lthree_page","SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_upper_barrel_btn_email_radio_btn_lthree_page", timeout = 15)

    def get_open_app_text_commercial(self):
        return self.driver.get_attribute("open_app_text_commercial","Name", timeout = 15)
    
    def click_customize_button_open_app_text(self):
        self.driver.hover("open_app_text_commercial")
        time.sleep(3)
        self.driver.click("open_app_text_commercial", timeout = 10)

    def get_onenote_text_commercial(self):
        return self.driver.get_attribute("onenote_text_commercial","Name", timeout = 15)
    
    def click_customize_button_onenote_text(self):
        self.driver.hover("onenote_text_commercial")
        self.driver.click("onenote_text_commercial", timeout = 10)    

    def get_next_track_text_commercial(self):
        return self.driver.get_attribute("next_track_text_commercial","Name", timeout = 15)

    def get_previous_track_text_commercial(self):
        return self.driver.get_attribute("previous_track_text_commercial","Name", timeout = 15)

    def get_volume_up_text_commercial(self):
        return self.driver.get_attribute("volume_up_text_commercial","Name", timeout = 15)

    def get_volume_down_text_commercial(self):
        return self.driver.get_attribute("volume_down_text_commercial","Name", timeout = 15)

    def get_mute_audio_text_commercial(self):
        return self.driver.get_attribute("mute_audio_text_commercial","Name", timeout = 15)

    def click_mute_audio_text_commercial(self):
        self.driver.click("pen_control_customize_btn_upper_barrel_btn_media_control_mute_audio_radio_btn_lthree_page", timeout = 15)
        if self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_media_control_mute_audio_radio_btn_lthree_page","SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_upper_barrel_btn_media_control_mute_audio_radio_btn_lthree_page", timeout = 15)

    def click_customize_buttons(self):
        self.driver.click("customize_buttons", timeout =20)

    def get_customize_buttons_text(self):
        return self.driver.get_attribute("customize_buttons","Name", timeout = 15)
    
    def click_customize_buttons_pen_image(self):
        self.driver.click("customize_buttons_pen_image", timeout =15)

    def click_my_pen_button(self):
        self.driver.click("my_pen_button", timeout =15)
    
    def get_single_press_text(self):
        return self.driver.get_attribute("single_press_title", "Name", timeout = 15)

    def click_customize_upper_barrel_button(self):
        self.driver.click("customize_upper_barrel_button", timeout =15)

    def click_customize_lower_barrel_button(self):
        self.driver.click("customize_lower_barrel_button", timeout = 15)

    def get_upper_barrel_button_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button", "Name", timeout = 15)
    
    def get_lower_barrel_button_text(self):
        return self.driver.get_attribute("customize_lower_barrel_button", "Name", timeout = 15)
    
    def get_top_button_single_press_text(self):
        return self.driver.get_attribute("customize_top_button_single_press", "Name", timeout = 15)
    
    def get_top_button_double_press_text(self):
        return self.driver.get_attribute("customize_top_button_double_press", "Name", timeout = 15)
    
    def get_top_button_long_press_text(self):
        return self.driver.get_attribute("customize_top_button_long_press", "Name", timeout = 15)
    
    def get_upper_barrel_button_right_click_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_right_click", "Name", timeout = 15)

    def click_customize_button_right_click_text(self):
        self.driver.hover("customize_upper_barrel_button_right_click")
        self.driver.click("customize_upper_barrel_button_right_click", timeout = 10)
    
    def get_upper_barrel_button_left_click_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_left_click", "Name", timeout = 15)

    def click_customize_button_left_click_text(self):
        self.driver.hover("customize_upper_barrel_button_left_click")
        self.driver.click("customize_upper_barrel_button_left_click", timeout = 10)
    
    def get_upper_barrel_button_middle_click_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_middle_click", "Name", timeout = 15)

    def click_customize_button_middle_click_text(self):
        self.driver.hover("customize_upper_barrel_button_middle_click")
        self.driver.click("customize_upper_barrel_button_middle_click", timeout = 10)
    
    def get_upper_barrel_button_fourth_click_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_fourth_click", "Name", timeout = 15)

    def click_customize_button_fourth_click_text(self):
        self.driver.hover("customize_upper_barrel_button_fourth_click")
        self.driver.click("customize_upper_barrel_button_fourth_click", timeout = 10)
    
    def click_upper_barrel_button_fourth_click_text(self):
        self.driver.click("pen_control_customize_btn_upper_barrel_btn_fourth_click_radio_btn_lthree_page", timeout = 15)
        time.sleep(2)
        if self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_fourth_click_radio_btn_lthree_page","SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_upper_barrel_btn_fourth_click_radio_btn_lthree_page", timeout = 15)
    
    def get_upper_barrel_button_fifth_click_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_fifth_click", "Name", timeout = 15)

    def click_customize_button_fifth_click_text(self):
        self.driver.hover("customize_upper_barrel_button_fifth_click")
        self.driver.click("customize_upper_barrel_button_fifth_click", timeout = 10)

    def get_upper_barrel_button_ltwo_page_title(self):
        return self.driver.get_attribute("customize_buttons_upper_barrel_button_title", "Name", timeout = 15)
    
    def click_customize_button_universal_select_text(self):
        self.driver.hover("customize_buttons_upper_barrel_button_universal_select", timeout = 10)
        self.driver.click("customize_buttons_upper_barrel_button_universal_select", timeout = 10)

    def get_upper_barrel_button_copy_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_copy", "Name", timeout = 15)
    
    def click_customize_button_copy_text(self):
        self.driver.hover("customize_upper_barrel_button_copy")
        self.driver.click("customize_upper_barrel_button_copy", timeout = 10)

    def get_upper_barrel_button_paste_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_paste", "Name", timeout = 15)
    
    def click_customize_button_paste_text(self):
        self.driver.hover("customize_upper_barrel_button_paste")
        self.driver.click("customize_upper_barrel_button_paste", timeout = 10)

    def get_upper_barrel_button_undo_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_undo", "Name", timeout = 15)
    
    def click_customize_button_undo_text(self):
        self.driver.hover("customize_upper_barrel_button_undo")
        self.driver.click("customize_upper_barrel_button_undo", timeout = 10)

    def click_upper_barrel_button_undo_text(self):
        self.driver.click("customize_upper_barrel_button_undo", timeout = 15)

    def get_upper_barrel_button_radial_menu_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_radial_menu", "Name", timeout = 15)
    
    def click_customize_button_radial_menu_text(self):
        self.driver.hover("customize_upper_barrel_button_radial_menu")
        self.driver.click("customize_upper_barrel_button_radial_menu", timeout = 10)

    def get_upper_barrel_button_redo_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_redo", "Name", timeout = 15)
    
    def click_customize_button_redo_text(self):
        self.driver.hover("customize_upper_barrel_button_redo")
        self.driver.click("customize_upper_barrel_button_redo", timeout = 10)

    def get_upper_barrel_button_page_up_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_page_up", "Name", timeout = 15)
    
    def click_customize_button_page_up_text(self):
        self.driver.click("customize_upper_barrel_button_page_up", timeout = 10)
 
    def get_upper_barrel_button_page_down_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_page_down", "Name", timeout = 15)
    
    def click_customize_button_page_down_text(self):
        self.driver.click("customize_upper_barrel_button_page_down", timeout = 10)

    def get_upper_barrel_button_go_back_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_go_back", "Name", timeout = 15)
    
    def click_customize_button_go_back_text(self):
        self.driver.hover("customize_upper_barrel_button_go_back")
        self.driver.click("customize_upper_barrel_button_go_back", timeout = 10)

    def get_upper_barrel_button_go_forward_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_go_forward", "Name", timeout = 15)
   
    def click_customize_button_go_forward_text(self):
        self.driver.hover("customize_upper_barrel_button_go_forward")
        self.driver.click("customize_upper_barrel_button_go_forward", timeout = 10)
    
    def get_upper_barrel_button_erase_text(self):
        return self.driver.get_attribute("customize_upper_barrel_button_erase", "Name", timeout = 15)

    def click_customize_button_erase_text(self):
        self.driver.hover("customize_upper_barrel_button_erase")
        self.driver.click("customize_upper_barrel_button_erase", timeout = 10)
    
    def get_lower_barrel_button_erase_text(self):
        return self.driver.get_attribute("customize_lower_barrel_button_erase", "Name", timeout = 15)

    def get_top_button_single_press_ms_whiteboard_text(self):
        return self.driver.get_attribute("customize_top_button_single_press_ms_whiteboard", "Name", timeout = 15)
       
    def get_top_button_double_press_screen_snipping_text(self):
        return self.driver.get_attribute("customize_top_button_double_press_screen_snipping", "Name", timeout = 15)
       
    def get_top_button_long_press_sticky_notes_text(self):
        return self.driver.get_attribute("customize_top_button_long_press_sticky_notes", "Name", timeout = 15)
    
    def get_upper_barrel_button_right_arrow(self):
        return self.driver.get_attribute("upper_barrel_button_right_arrow_icon", "Name", timeout = 15)

    def get_lower_barrel_button_right_arrow(self):
        return self.driver.get_attribute("lower_barrel_button_right_arrow_icon", "Name", timeout = 15)

    def get_top_button_single_press_right_arrow(self):
        return self.driver.get_attribute("top_button_single_press_right_arrow_icon", "Name", timeout = 15)
    
    def get_top_button_double_press_right_arrow(self):
        return self.driver.get_attribute("top_button_double_press_right_arrow_icon", "Name", timeout = 15)   

    def get_top_button_long_press_right_arrow(self):
        return self.driver.get_attribute("top_button_long_press_right_arrow_icon", "Name", timeout = 15)   

    def get_current_assignment(self):
        return self.driver.get_attribute("current_assignment_text", "Name", timeout = 15, raise_e=False)   
    
    def get_upper_barrel_button_productivity_title(self):
        return self.driver.get_attribute("upper_barrel_button_productivity_title", "Name", timeout = 15)

    def get_lower_barrel_button_productivity_title(self):
        return self.driver.get_attribute("lower_barrel_button_productivity_title", "Name", timeout = 15)
    
    def get_top_button_single_press_productivity_title(self):
        return self.driver.get_attribute("top_button_single_press_productivity_title", "Name", timeout = 15)
            
    def get_top_button_double_press_productivity_title(self):
        return self.driver.get_attribute("top_button_double_press_productivity_title", "Name", timeout = 15)
            
    def get_top_button_long_press_productivity_title(self):
        return self.driver.get_attribute("top_button_long_press_productivity_title", "Name", timeout = 15)
        
    def get_upper_barrel_button_pen_title(self):
        return self.driver.get_attribute("upper_barrel_button_pen_title", "Name", timeout = 15)

    def get_lower_barrel_button_pen_title(self):
        return self.driver.get_attribute("lower_barrel_button_pen_title", "Name", timeout = 15)
    
    def get_top_button_single_press_pen_title(self):
        return self.driver.get_attribute("top_button_single_press_pen_title", "Name", timeout = 15)
            
    def get_top_button_double_press_pen_title(self):
        return self.driver.get_attribute("top_button_double_press_pen_title", "Name", timeout = 15)
            
    def get_top_button_long_press_pen_title(self):
        return self.driver.get_attribute("top_button_long_press_pen_title", "Name", timeout = 15)
        
    def get_upper_barrel_button_apps_title(self):
        return self.driver.get_attribute("upper_barrel_button_apps_title", "Name", timeout = 15)

    def get_lower_barrel_button_apps_title(self):
        return self.driver.get_attribute("lower_barrel_button_apps_title", "Name", timeout = 15)
    
    def get_top_button_single_press_apps_title(self):
        return self.driver.get_attribute("top_button_single_press_apps_title", "Name", timeout = 15)
            
    def get_top_button_double_press_apps_title(self):
        return self.driver.get_attribute("top_button_double_press_apps_title", "Name", timeout = 15)
            
    def get_top_button_long_press_apps_title(self):
        return self.driver.get_attribute("top_button_long_press_apps_title", "Name", timeout = 15)
        
    def get_upper_barrel_button_media_control_title(self):
        return self.driver.get_attribute("upper_barrel_button_media_control_title", "Name", timeout = 15)

    def get_lower_barrel_button_media_control_title(self):
        return self.driver.get_attribute("lower_barrel_button_media_control_title", "Name", timeout = 15)
    
    def get_top_button_single_press_media_control_title(self):
        return self.driver.get_attribute("top_button_single_press_media_control_title", "Name", timeout = 15)
            
    def get_top_button_double_press_media_control_title(self):
        return self.driver.get_attribute("top_button_double_press_media_control_title", "Name", timeout = 15)
            
    def get_top_button_long_press_media_control_title(self):
        return self.driver.get_attribute("top_button_long_press_media_control_title", "Name", timeout = 15)    
  
    def get_productivity_arrow_icon(self):
        return self.driver.get_attribute("productivity_arrow_icon", "Name", timeout = 15)
    
    def click_productivity_arrow_icon(self):
        self.driver.click("productivity_arrow_icon", timeout =15)

    def get_pen_arrow_icon(self):
        return self.driver.get_attribute("pen_arrow_icon", "Name", timeout = 15)
    
    def click_pen_arrow_icon(self):
        self.driver.click("pen_arrow_icon", timeout =15)

    def get_apps_arrow_icon(self):
        return self.driver.get_attribute("apps_arrow_icon", "Name", timeout = 15)
    
    def click_apps_arrow_icon(self):
        self.driver.click("apps_arrow_icon", timeout =15)
      
    def get_media_control_arrow_icon(self):
        return self.driver.get_attribute("media_control_arrow_icon", "Name", timeout = 15)
    
    def click_media_arrow_icon(self):
        self.driver.click("media_control_arrow_icon", timeout =15)

    def click_button_copy_text(self):
        self.driver.click("customize_upper_barrel_button_copy", timeout =15)
    
    def click_radial_menu_button(self):
        self.driver.click("radial_menu_commercial", timeout = 10)

    def click_radial_slice1_button(self):
        self.driver.click("radial_menu_commercial_slice1", timeout = 10)

    def click_radial_slice1_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice1_productivity_show_more_button", timeout = 10)

    def click_radial_slice1_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice1_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice1_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice1_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice1_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice1_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice1_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice1_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice1_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice1_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice2_button(self):
        self.driver.click("radial_menu_commercial_slice2", timeout = 10)

    def click_radial_slice2_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice2_productivity_show_more_button", timeout = 10)

    def click_radial_slice2_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice2_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice2_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice2_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice2_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice2_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice2_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice2_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice2_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice2_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice3_button(self):
        self.driver.click("radial_menu_commercial_slice3", timeout = 10)

    def click_radial_slice3_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice3_productivity_show_more_button", timeout = 10)

    def click_radial_slice3_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice3_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice3_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice3_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice3_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice3_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice3_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice3_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice3_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice3_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice4_button(self):
        self.driver.click("radial_menu_commercial_slice4", timeout = 10)

    def click_radial_slice4_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice4_productivity_show_more_button", timeout = 10)

    def click_radial_slice4_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice4_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice4_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice4_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice4_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice4_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice4_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice4_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice4_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice4_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice5_button(self):
        self.driver.click("radial_menu_commercial_slice5", timeout = 10)

    def click_radial_slice5_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice5_productivity_show_more_button", timeout = 10)

    def click_radial_slice5_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice5_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice5_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice5_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice5_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice5_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice5_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice5_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice5_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice5_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice6_button(self):
        self.driver.click("radial_menu_commercial_slice6", timeout = 10)

    def click_radial_slice6_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice6_productivity_show_more_button", timeout = 10)

    def click_radial_slice6_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice6_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice6_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice6_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice6_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice6_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice6_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice6_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice6_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice6_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice7_button(self):
        self.driver.click("radial_menu_commercial_slice7", timeout = 10)

    def click_radial_slice7_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice7_productivity_show_more_button", timeout = 10)

    def click_radial_slice7_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice7_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice7_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice7_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice7_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice7_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice7_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice7_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice7_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice7_productivity_go_forward_radio_button", timeout = 10)
        
    def click_radial_slice8_button(self):
        self.driver.click("radial_menu_commercial_slice8", timeout = 10)

    def click_radial_slice8_productivity_show_more_button(self):
        self.driver.click("radial_menu_commercial_slice8_productivity_show_more_button", timeout = 10)

    def click_radial_slice8_productivity_universal_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_universal_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_universal_radio_button", timeout = 10)

    def click_radial_slice8_productivity_paste_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_paste_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_paste_radio_button", timeout = 10)
            
    def click_radial_slice8_productivity_undo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_undo_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_undo_radio_button", timeout = 10)

    def click_radial_slice8_productivity_copy_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_copy_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_copy_radio_button", timeout = 10)

    def click_radial_slice8_productivity_redo_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_redo_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_redo_radio_button", timeout = 10)

    def click_radial_slice8_productivity_page_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_page_up_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_page_up_radio_button", timeout = 10)

    def click_radial_slice8_productivity_page_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_page_down_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_page_down_radio_button", timeout = 10)

    def click_radial_slice8_productivity_go_back_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_go_back_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_go_back_radio_button", timeout = 10)

    def click_radial_slice8_productivity_go_forward_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_productivity_go_forward_radio_button")
        self.driver.click("radial_menu_commercial_slice8_productivity_go_forward_radio_button", timeout = 10)

    def click_customize_back_button(self):
        self.driver.click("customize_back_buttons", timeout =15)

    def click_more_link_on_productivity_button(self):
        self.driver.click("more_link_on_productivity", timeout =15)

    def click_more_link_on_productivity_button_lower_barrel(self):
        self.driver.click("more_link_on_productivity_lower_barrel", timeout =15)

    def click_more_link_on_pen_button(self):
        self.driver.click("more_link_on_pen", timeout =15)

    def click_more_link_on_apps_button(self):
        self.driver.click("more_link_on_apps", timeout =15)

    def click_more_link_on_media_control_button(self):
        self.driver.click("more_link_on_media_control", timeout =15)

    def click_radial_slice1_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice1_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_erase_radio_button", timeout = 10)

    def click_radial_slice1_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice1_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice1_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice1_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice1_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice1_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_menu_radio_button", timeout = 10)

    def click_radial_slice1_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice1_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice2_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice2_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_erase_radio_button", timeout = 10)

    def click_radial_slice2_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice2_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice2_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice2_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice2_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice2_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_menu_radio_button", timeout = 10)

    def click_radial_slice2_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice2_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice3_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice3_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_erase_radio_button", timeout = 10)

    def click_radial_slice3_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice3_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice3_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice3_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice3_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice3_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_menu_radio_button", timeout = 10)

    def click_radial_slice3_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice3_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice4_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice4_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_erase_radio_button", timeout = 10)

    def click_radial_slice4_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice4_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice4_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice4_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice4_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice4_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_menu_radio_button", timeout = 10)

    def click_radial_slice4_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice4_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice5_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice5_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_erase_radio_button", timeout = 10)

    def click_radial_slice5_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice5_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice5_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice5_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice5_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice5_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_menu_radio_button", timeout = 10)

    def click_radial_slice5_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice5_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice6_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice6_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_erase_radio_button", timeout = 10)

    def click_radial_slice6_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice6_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice6_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice6_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice6_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice6_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_menu_radio_button", timeout = 10)

    def click_radial_slice6_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice6_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice7_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice7_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_erase_radio_button", timeout = 10)

    def click_radial_slice7_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice7_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice7_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice7_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice7_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice7_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_menu_radio_button", timeout = 10)

    def click_radial_slice7_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice7_pen_disabled_radio_button", timeout = 10)

    def click_radial_slice8_pen_onoff_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_onoff_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_onoff_radio_button", timeout = 10)
    
    def click_radial_slice8_pen_erase_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_erase_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_erase_radio_button", timeout = 10)

    def click_radial_slice8_pen_left_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_left_click_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_left_click_radio_button", timeout = 10)

    def click_radial_slice8_pen_right_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_right_click_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_right_click_radio_button", timeout = 10)
    
    def click_radial_slice8_pen_middle_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_middle_click_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_middle_click_radio_button", timeout = 10)

    def click_radial_slice8_pen_fourth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_fourth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_fourth_click_radio_button", timeout = 10)

    def click_radial_slice8_pen_fifth_click_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_fifth_click_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_fifth_click_radio_button", timeout = 10)

    def click_radial_slice8_pen_menu_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_menu_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_menu_radio_button", timeout = 10)

    def click_radial_slice8_pen_disabled_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_pen_disabled_radio_button")
        self.driver.click("radial_menu_commercial_slice8_pen_disabled_radio_button", timeout = 10)

    def click_upper_barrel_hover_click_toggle_lthree_page(self):
        self.driver.click("upper_barrel_hover_click_toggle_lthree_page", timeout =15)

    def get_upper_barrel_hover_click_toggle_lthree_page_value(self):
        return self.driver.get_attribute("upper_barrel_hover_click_toggle_lthree_page", "Name", timeout = 15)
    
    def get_current_assignment_copy_value(self):
        return self.driver.get_attribute("customize_upper_barrel_button_copy", "Name", timeout = 15)  
    
    def get_current_assignment_undo_value(self):
        return self.driver.get_attribute("customize_upper_barrel_button_undo", "Name", timeout = 15)    

    def get_current_assignment_web_browser_value(self):
        return self.driver.get_attribute("web_browser_text_commercial", "Name", timeout = 15)

    def get_current_assignment_mute_audio_value(self):
        return self.driver.get_attribute("mute_audio_text_commercial", "Name", timeout = 15)

    def get_current_assignment_fourth_click_value(self):
        return self.driver.get_attribute("customize_upper_barrel_button_fourth_click", "Name", timeout = 15)

    def get_current_assignment_email_value(self):
        return self.driver.get_attribute("email_text_commercial", "Name", timeout = 15) 

    def click_radial_slice_add_application_cancel_button(self):
        self.driver.click("radial_menu_commercial_slice_add_application_cancel", timeout = 10)

    def click_radial_slice1_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice1_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice1_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice1_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice1_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice1_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_email_radio_button", timeout = 10)

    def click_radial_slice1_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice1_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice1_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice1_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice2_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice2_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice2_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice2_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice2_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice2_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_email_radio_button", timeout = 10)

    def click_radial_slice2_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice2_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice2_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice2_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice3_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice3_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice3_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice3_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice3_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice3_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_email_radio_button", timeout = 10)

    def click_radial_slice3_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice3_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice3_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice3_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice4_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice4_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice4_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice4_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice4_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice4_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_email_radio_button", timeout = 10)

    def click_radial_slice4_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice4_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice4_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice4_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice5_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice5_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice5_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice5_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice5_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice5_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_email_radio_button", timeout = 10)

    def click_radial_slice5_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice5_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice5_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice5_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice6_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice6_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice6_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice6_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice6_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice6_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_email_radio_button", timeout = 10)

    def click_radial_slice6_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice6_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice6_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice6_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice7_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice7_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice7_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice7_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice7_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice7_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_email_radio_button", timeout = 10)

    def click_radial_slice7_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice7_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice7_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice7_apps_onenote_radio_button", timeout = 10)

    def click_radial_slice8_apps_windows_search_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_windows_search_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_windows_search_radio_button", timeout = 10)

    def click_radial_slice8_apps_ms_whiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_ms_whiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_ms_whiteboard_radio_button", timeout = 10)

    def click_radial_slice8_apps_screen_snipping_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_screen_snipping_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_screen_snipping_radio_button", timeout = 10)

    def click_radial_slice8_apps_switch_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_switch_app_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_switch_app_radio_button", timeout = 10)

    def click_radial_slice8_apps_web_browser_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_web_browser_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_web_browser_radio_button", timeout = 10)

    def click_radial_slice8_apps_email_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_email_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_email_radio_button", timeout = 10)

    def click_radial_slice8_apps_open_app_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_open_app_radio_button")
        time.sleep(3)
        self.driver.click("radial_menu_commercial_slice8_apps_open_app_radio_button", timeout = 10)

    def click_radial_slice8_apps_onenote_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_apps_onenote_radio_button")
        self.driver.click("radial_menu_commercial_slice8_apps_onenote_radio_button", timeout = 10)                         

    def click_radial_slice1_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_playpause_radio_button", timeout = 10)

    def click_radial_slice1_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_next_track_radio_button", timeout = 10)

    def click_radial_slice1_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice1_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice1_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice1_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice1_media_mute_radio_button", timeout = 10)

    def click_radial_slice2_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_playpause_radio_button", timeout = 10)

    def click_radial_slice2_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_next_track_radio_button", timeout = 10)

    def click_radial_slice2_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice2_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice2_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice2_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice2_media_mute_radio_button", timeout = 10)

    def click_radial_slice3_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_playpause_radio_button", timeout = 10)

    def click_radial_slice3_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_next_track_radio_button", timeout = 10)

    def click_radial_slice3_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice3_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice3_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice3_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice3_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice3_media_mute_radio_button", timeout = 10)

    def click_radial_slice4_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_playpause_radio_button", timeout = 10)

    def click_radial_slice4_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_next_track_radio_button", timeout = 10)

    def click_radial_slice4_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice4_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice4_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice4_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice4_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice4_media_mute_radio_button", timeout = 10)

    def click_radial_slice5_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_playpause_radio_button", timeout = 10)

    def click_radial_slice5_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_next_track_radio_button", timeout = 10)

    def click_radial_slice5_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice5_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice5_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice5_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice5_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice5_media_mute_radio_button", timeout = 10)

    def click_radial_slice6_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_playpause_radio_button", timeout = 10)

    def click_radial_slice6_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_next_track_radio_button", timeout = 10)

    def click_radial_slice6_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice6_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice6_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice6_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice6_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice6_media_mute_radio_button", timeout = 10)

    def click_radial_slice7_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_playpause_radio_button", timeout = 10)

    def click_radial_slice7_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_next_track_radio_button", timeout = 10)

    def click_radial_slice7_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice7_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice7_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice7_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice7_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice7_media_mute_radio_button", timeout = 10)

    def click_radial_slice8_media_playpause_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_playpause_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_playpause_radio_button", timeout = 10)

    def click_radial_slice8_media_next_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_next_track_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_next_track_radio_button", timeout = 10)

    def click_radial_slice8_media_previous_track_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_previous_track_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_previous_track_radio_button", timeout = 10)

    def click_radial_slice8_media_volume_up_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_volume_up_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_volume_up_radio_button", timeout = 10)

    def click_radial_slice8_media_volume_down_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_volume_down_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_volume_down_radio_button", timeout = 10)

    def click_radial_slice8_media_mute_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice8_media_mute_radio_button")
        self.driver.click("radial_menu_commercial_slice8_media_mute_radio_button", timeout = 10)
        
    def click_pencontrol_upper_barrel_btn_prod_radial_goback(self):
        self.driver.click("pencontrol_upper_barrel_btn_prod_radial_goback", timeout = 15)
          
    def click_pencontrol_upper_barrel_btn_prod_radial_goforward(self):
        self.driver.click("pencontrol_upper_barrel_btn_prod_radial_goforward", timeout = 15) 

    def click_pencontrol_upper_barrel_btn_prod_radial_pageup(self):
        self.driver.click("pencontrol_upper_barrel_btn_prod_page_up", timeout = 15)
         
    def click_pencontrol_upper_barrel_btn_prod_radial_redo(self):
        self.driver.click("pencontrol_upper_barrel_btn_prod_radial_redo", timeout = 15) 
        
    def click_pencontrol_upper_barrel_btn_prod_radial_pagedown(self):
        self.driver.click("pencontrol_upper_barrel_btn_prod_radial_pagedown", timeout = 15) 

    def get_more_link_on_pen_button(self):
        return self.driver.get_attribute("more_link_on_app_consumer","Name", timeout=15)

    def get_pencontrol_name_prod_radial_goback(self):
        return self.driver.get_attribute("pencontrol_name_prod_radial_goback","Name", timeout=15)

    def get_pencontrol_name_prod_radial_goforward(self):
        return self.driver.get_attribute("pencontrol_name_prod_radial_goforward","Name", timeout=15)

    def get_pencontrol_name_prod_radial_pagedown(self):
        return self.driver.get_attribute("pencontrol_name_prod_radial_pagedown","Name", timeout=15)

    def get_pencontrol_name_prod_radial_redo(self):
        return self.driver.get_attribute("pencontrol_name_prod_radial_redo","Name", timeout=15)

    def get_pencontrol_name_prod_page_up(self):
        return self.driver.get_attribute("pencontrol_name_prod_page_up","Name", timeout=15)
    
    def get_current_assignment_selected_value(self):
        return self.driver.get_attribute("current_assignment_selected_value","Name", timeout=20)
    
    def click_pencontrol_upper_barrel_btn_prod_radial_menu(self):
        self.driver.hover("pencontrol_upper_barrel_btn_prod_radial_menu")
        self.driver.click("pencontrol_upper_barrel_btn_prod_radial_menu", timeout = 15)

    def click_pencontrol_lower_barrel_btn_prod_paste(self):
        self.driver.click("pencontrol_lower_barrel_btn_prod_paste", timeout = 15)

    def click_pencontrol_topbutton_singlepress_row(self):
        self.driver.click("pencontrol_topbutton_singlepress_row", timeout = 15)

    def click_pencontrol_topbutton_doublepress_row(self):
        self.driver.click("pencontrol_topbutton_doublepress_row", timeout = 15)

    def click_pencontrol_topbutton_longpress_row(self):
        self.driver.click("pencontrol_topbutton_longpress_row", timeout = 15)

    def click_radial_menu_buttons(self):
        self.driver.click("customize_upper_barrel_button_radial_menu", timeout =15)

    def get_play_pause_text_consumer(self):
        return self.driver.get_attribute("play_pause_text_consumer","Name", timeout = 15)

    def get_shift_key_text(self):
        return self.driver.get_attribute("shift_key_text", "Name", timeout = 15)

    def get_control_key_text(self):
        return self.driver.get_attribute("control_key_text", "Name", timeout = 15)
    
    def get_alt_key_text(self):
        return self.driver.get_attribute("alt_key_text", "Name", timeout = 15)
    
    def get_windows_key_text(self):
        return self.driver.get_attribute("windows_key_text", "Name", timeout = 15)
    
    def get_tab_key_text(self):
        return self.driver.get_attribute("tab_key_text", "Name", timeout = 15)
    
    def get_right_arrow_key_text(self):
        return self.driver.get_attribute("right_arrow_key_text", "Name", timeout = 15)
    
    def get_left_arrow_key_text(self):
        return self.driver.get_attribute("left_arrow_key_text", "Name", timeout = 15)

    def get_previous_page_text(self):
        return self.driver.get_attribute("previous_page_text", "Name", timeout = 15)
    
    def get_next_page_text(self):
        return self.driver.get_attribute("next_page_text", "Name", timeout = 15)

    def get_scroll_text(self):
        return self.driver.get_attribute("scroll_text", "Name", timeout = 15)
    
    def get_right_click_text_commercial(self):
        return self.driver.get_attribute("consumer_right_click_text", "Name", timeout = 15)

    def get_disable_pen_buttons_text(self):
        return self.driver.get_attribute("disable_pen_buttons_text", "Name", timeout = 15)

    def get_take_screenshot_text(self):
        return self.driver.get_attribute("take_screenshot_text", "Name", timeout = 15)

    def get_switch_between_apps_text(self):
        return self.driver.get_attribute("switch_between_apps_text", "Name", timeout = 15)

    def get_launch_task_manager_text(self):
        return self.driver.get_attribute("launch_task_manager_text", "Name", timeout = 15)

    def get_new_browser_tab_text(self):
        return self.driver.get_attribute("new_browser_tab_text", "Name", timeout = 15)

    def get_show_the_desktop_text(self):
        return self.driver.get_attribute("show_the_desktop_text", "Name", timeout = 15)

    def get_mute_unmute_text(self):
        return self.driver.get_attribute("mute_unmute_text", "Name", timeout = 15)
    
    def click_mute_unmute_text(self):
        self.driver.click("mute_unmute_text", timeout = 20)

    def click_consumer_customize_buttons(self):
        self.driver.click("consumer_customize_buttons", timeout =20)

    def click_customize_play_pause_text(self):
        self.driver.hover("play_pause_text_commercial")
        self.driver.click("play_pause_text_commercial", timeout = 10)

    def click_customize_next_track_text(self):
        self.driver.hover("next_track_text_commercial")
        self.driver.click("next_track_text_commercial", timeout = 10)

    def click_customize_previous_track_text(self):
        self.driver.hover("previous_track_text_commercial")
        self.driver.click("previous_track_text_commercial", timeout = 10)

    def click_customize_volume_up_text(self):
        self.driver.hover("volume_up_text_commercial")
        self.driver.click("volume_up_text_commercial", timeout = 10)

    def click_customize_volume_down_text(self):
        self.driver.hover("volume_down_text_commercial")
        self.driver.click("volume_down_text_commercial", timeout = 10)

    def click_customize_mute_audio_text(self):
        self.driver.hover("mute_audio_text_commercial")
        self.driver.click("mute_audio_text_commercial", timeout = 10)

    def get_hp_rechargeable_active_pen_g3pencontrol(self):
        return self.driver.get_attribute("hp_rechargeable_active_pen_g3pencontro", "Name", timeout = 15)

    def get_pressure_sensitivity_text(self):
        return self.driver.get_attribute("pressure_sensitivity_text", "Name", timeout = 15)

    def get_pressure_low_sensitivity_text(self):
        return self.driver.get_attribute("pressure_low_sensitivity_text", "Name", timeout = 15)

    def get_pressure_high_sensitivity_text(self):
        return self.driver.get_attribute("pressure_high_sensitivity_text", "Name", timeout = 15)

    def get_tilt_sensitivity_text(self):
        return self.driver.get_attribute("tilt_sensitivity_text", "Name", timeout = 15)

    def get_tilt_narrow_sensitivity_text(self):
        return self.driver.get_attribute("tilt_narrow_sensitivity_text", "Name", timeout = 15)

    def get_tilt_wide_sensitivity_text(self):
        return self.driver.get_attribute("tilt_wide_sensitivity_text", "Name", timeout = 15)

    def get_pen_sensitivity_restore_defaults_btn_text(self):
        return self.driver.get_attribute("restore_default_pen_sensitivity_menu_ltwo_page","Name", timeout=15)

    def select_administrative_tools(self):
        self.driver.click("administrative_tools", timeout =20)

    def click_add_button(self):
        self.driver.click("add_button", timeout =20)

    def click_cancel_button(self):
        self.driver.click("cancel_button", timeout =20)

    def verify_pen_sensitivity_pressure_slider(self):
        return self.driver.get_attribute("pen_sensitivity_pressure_slider", "Name", timeout = 15)
    
    def get_pen_sensitivity_pressure_slider_value(self):
        return self.driver.get_attribute("pen_sensitivity_pressure_slider", "Value.Value", timeout = 15)
    
    def verify_pen_sensitivity_pressure_low_indicator(self):
        return self.driver.get_attribute("pressure_low_sensitivity_text", "Name", timeout = 15)
    
    def verify_pen_sensitivity_pressure_high_indicator(self):
        return self.driver.get_attribute("pressure_high_sensitivity_text", "Name", timeout = 15)

    def verify_pen_sensitivity_card(self):
        return self.driver.get_attribute("pen_sensitivity_card", "Name", timeout = 15)
    
    def click_pen_sensitivity_card(self):
        self.driver.click("pen_sensitivity_card", timeout = 15)

    def verify_customize_buttons(self):
        return self.driver.get_attribute("customize_buttons", "Name", timeout = 15, raise_e=False)
    
    def click_customize_button_sticky_note_text(self):
        self.driver.hover("customize_top_button_long_press_sticky_notes")
        self.driver.click("customize_top_button_long_press_sticky_notes", timeout = 10)
    
    def click_customize_button_quick_note_text(self):
        self.driver.click("customize_top_button_quick_note", timeout = 15) 

    def click_more_link_top_button_single_press(self):
        self.driver.click("more_link_on_top_button_single_press", timeout = 10)  

    def click_more_link_top_button_double_press(self):
        self.driver.click("more_link_on_top_button_double_press", timeout = 10)        

    def click_more_link_top_button_long_press(self):
        self.driver.click("more_link_on_top_button_long_press", timeout = 10)              

    def verify_radial_menu_commercial(self):
        return self.driver.get_attribute("radial_menu_commercial", "Name", timeout = 15)
    
    def verify_external_display_card(self):
        return self.driver.get_attribute("external_display_card", "Name", timeout = 15)
    
    def click_external_display_card(self):
        self.driver.click("external_display_card", timeout = 15)
    
    def verify_external_display_card_context_aware(self):
        return self.driver.get_attribute("external_display_card_context_aware", "Name", timeout = 15)
    
    def get_external_display_card_context_aware_text(self):
        return self.driver.get_attribute("external_display_card_context_aware", "Name", timeout = 15)

    def verify_radial_menu_card_context_aware(self):
        return self.driver.get_attribute("radial_menu_card_context_aware", "Name", timeout = 15)
    
    def get_radial_menu_card_context_aware_text(self):
        return self.driver.get_attribute("radial_menu_card_context_aware", "Name", timeout = 15)

    def verify_context_aware_all_app_button(self):
        return self.driver.get_attribute("context_aware_all_app_button", "Name", timeout = 15)
    
    def click_context_aware_all_app_button(self):
        self.driver.click("context_aware_all_app_button", timeout = 15)

    def verify_add_button(self):
        return self.driver.get_attribute("add_button", "Name", timeout = 15)
    
    def verify_search_access_on_application_list(self):
        return self.driver.get_attribute("search_access_on_application_list", "Name", timeout = 15)

    def click_access_on_application_list_dialog(self):
        self.driver.click("search_access_on_application_list")

    def verify_application_list_on_dialog_show_up(self):
        return self.driver.wait_for_object("application_list_on_dialog", raise_e=False, timeout=10)

    def click_pen_continue_onpopup_window_page(self):
        self.driver.click("pen_continue_onpopup_window_page", timeout = 15)

    def click_pen_cancel_onpopup_window_page(self):
        self.driver.click("pen_cancel_onpopup_window_page", timeout = 15)

    def check_context_aware_carsoul_for_app(self, name):
        locator_base = "context_aware_carousel_item_"
        for i in range(0, 9):
            locator = locator_base+str(i)
            if not self.driver.get_attribute(locator, "Name", timeout=15):
                return False
            
            if self.driver.get_attribute(locator, "Name", timeout=15) == name:
                return True
            
            return False; 

    def verify_pen_image_lone_page(self):
        return self.driver.wait_for_object("pen_image_lone_page", raise_e=False, timeout=15)

    def get_notification_tab_text_lone_page(self):
        return self.driver.get_attribute("notification_tab_text_lone_page", "Name", timeout=15)

    def verify_notification_tab_toggle_switch_lone_page(self):
        return self.driver.wait_for_object("notification_tab_toggle_switch_lone_page", raise_e=False, timeout=15)

    def verify_product_information_card_lone_page(self):
        return self.driver.wait_for_object("product_information_card_lone_page", raise_e=False, timeout=15) is not False

    def get_restore_default_button_lone_page(self):
        return self.driver.get_attribute("restore_default_button_lone_page", "Name", timeout=15)
           
    def verify_desktop_icon_on_pen_external_display_lone_page(self):
        return self.driver.wait_for_object("desktop_icon_on_pen_external_display_lone_page", raise_e=False, timeout=15)

    def verify_pen_ltwo_page_title(self):
        return self.driver.wait_for_object("pen_ltwo_page_title", raise_e=False, timeout=15)
    
    def verify_display_selection_dd_ltwo_page(self):
        return self.driver.wait_for_object("display_selection_dd_ltwo_page", raise_e=False, timeout=15) is not False

    def get_state_enable_this_feature_toggle_switch_ltwo_page(self):
        return self.driver.get_attribute("enable_this_feature_toggle_switch_ltwo_page", "Name", timeout=15)

    def verify_device_orientation_ltwo_page(self):
        return self.driver.wait_for_object("device_orientation_ltwo_page", raise_e=False, timeout=15) is not False
    
    def get_landscape_ltwo_page(self):
        return self.driver.get_attribute("landscape_ltwo_page", "Name", timeout=15)
    
    def get_landscape_flipped_ltwo_page(self):
        return self.driver.get_attribute("landscape_flipped_ltwo_page", "Name", timeout=15)
    
    def get_portrait_ltwo_page(self):
        return self.driver.get_attribute("portrait_ltwo_page", "Name", timeout=15)
    
    def get_portrait_flipped_ltwo_page(self):
        return self.driver.get_attribute("portrait_flipped_ltwo_page", "Name", timeout=15)
    
    def verify_input_mode_ltwo_page(self):
        return self.driver.wait_for_object("input_mode_ltwo_page", raise_e=False, timeout=15)
    
    def get_pen_only_ltwo_page(self):
        return self.driver.get_attribute("pen_only_ltwo_page", "Name", timeout=15)
    
    def get_pen_and_touch_ltwo_page(self):
        return self.driver.get_attribute("pen_and_touch_ltwo_page", "Name", timeout=15)
    
    def verify_display_mapping_ltwo_page(self):
        return self.driver.wait_for_object("display_mapping_ltwo_page", raise_e=False, timeout=15)
    
    def get_scale_ltwo_page(self):
        return self.driver.get_attribute("scale_ltwo_page", "Name", timeout=15)
    
    def get_stretch_ltwo_page(self):
        return self.driver.get_attribute("stretch_ltwo_page", "Name", timeout=15)
    
    def get_external_display_restore_defaults_button_text(self):
        return self.driver.get_attribute("restore_default_external_display_ltwo_page", "Name", timeout=15)
    
    def verify_desktop_icon_on_pen_external_display_ltwo_page(self):
        return self.driver.wait_for_object("desktop_icon_on_pen_external_display_ltwo_page", raise_e=False, timeout=15)
    
    def verify_enable_this_feature_text_ltwo_page(self):
        return self.driver.wait_for_object("enable_this_feature_text_ltwo_page", raise_e=False, timeout=15) is not False

    def get_connected_text_lone_page(self):
        return self.driver.get_attribute("connected_text_lone_page", "Name", timeout=15)
    
    def get_trio_x_pen_name_lone_page(self):
        return self.driver.get_attribute("trio_x_pen", "Name", timeout=15)

    def verify_product_information_title_lone_page(self):
        return self.driver.wait_for_object("product_information_title_lone_page", raise_e=False, timeout=15)

    def verify_product_number_on_product_information_card_lone_page(self):
        return self.driver.wait_for_object("product_number_on_product_information_card_lone_page", raise_e=False, timeout=15)
    
    def verify_serial_number_on_product_information_card_lone_page(self):
        return self.driver.wait_for_object("serial_number_on_product_information_card_lone_page", raise_e=False, timeout=15)

    def verify_firmware_version_on_product_information_card_lone_page(self):
        return self.driver.wait_for_object("firmware_version_on_product_information_card_lone_page", raise_e=False, timeout=15)

    def get_button_need_reassignment_lone_page(self):
        return self.driver.get_attribute("button_need_reassignment_lone_page", "Name", timeout=15)

    def click_button_need_reassignment_lone_page(self):
        self.driver.click("button_need_reassignment_lone_page", timeout = 15)
    
    def click_customize_buttons_upper_barrel_mswhiteboard_lthree_page(self):
        self.driver.hover("customize_buttons_upper_barrel_mswhiteboard_lthree_page")
        time.sleep(2)
        self.driver.click("customize_buttons_upper_barrel_mswhiteboard_lthree_page", timeout = 15)
    
    def is_selected_customize_buttons_upper_barrel_mswhiteboard_lthree_page(self):
        return self.driver.get_attribute("customize_buttons_upper_barrel_mswhiteboard_lthree_page", "SelectionItem.IsSelected", timeout=15)

    def get_assign_app_not_available_lthree_page(self):
        return self.driver.get_attribute("assign_app_not_available_lthree_page", "Name", timeout=15)
    
    def click_radial_menu_commercial_slice1_mswhiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice1_mswhiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice1_mswhiteboard_radio_button", timeout = 15)
    
    def is_selected_radial_menu_commercial_slice1_mswhiteboard_radio_button(self):
        return self.driver.get_attribute("radial_menu_commercial_slice1_mswhiteboard_radio_button", "SelectionItem.IsSelected", timeout=15)

    def click_radial_menu_commercial_slice2_mswhiteboard_radio_button(self):
        self.driver.hover("radial_menu_commercial_slice2_mswhiteboard_radio_button")
        self.driver.click("radial_menu_commercial_slice2_mswhiteboard_radio_button", timeout = 15)
    
    def is_selected_radial_menu_commercial_slice2_mswhiteboard_radio_button(self):
        return self.driver.get_attribute("radial_menu_commercial_slice2_mswhiteboard_radio_button", "SelectionItem.IsSelected", timeout=15)
    
    def get_trio_pen_name_consumer(self):
        return self.driver.get_attribute("trio_pen_name_consumer", "Name", timeout=15)
    
    def click_customize_topbutton_singlepress(self):
        self.driver.click("customize_topbutton_singlepress", timeout = 15)

    def click_customize_topbutton_doublepress(self):
        self.driver.click("customize_topbutton_doublepress", timeout = 15)

    def click_customize_topbutton_longpress(self):
        self.driver.click("customize_topbutton_longpress", timeout = 15)
        
    def click_lowerbarrel_hover_click_toggle_button_lthree_page(self):
        self.driver.click("lowerbarrel_hover_click_toggle_lthree_page", timeout =15)
        
    def click_productivity_chevron_down_arrow(self):
        self.driver.click("productivity_chevron_down_arrow", timeout =15)

    def click_media_control_chevron_down_arrow(self):
        self.driver.click("media_control_chevron_down_arrow", timeout =15)
    
    def get_customize_button_add_application_text_on_add_application_popup(self):
        return self.driver.get_attribute("customize_button_add_application_text_on_add_application_popup", "Name", timeout=15)

    def verify_access_app_on_carousel(self):
        return self.driver.wait_for_object("access_app_on_carousel", raise_e=False, timeout=15)

    def is_access_app_on_carousel_selected(self):
        return self.driver.get_attribute("access_app_on_carousel", "SelectionItem.IsSelected", timeout=15)

    def verify_calculator_app_on_carousel(self):
        return self.driver.wait_for_object("calculator_app_on_carousel", raise_e=False, timeout=15)

    def click_calculator_app_on_carousel(self):
        self.driver.click("calculator_app_on_carousel", timeout=15)

    def click_delete_profile_btn_on_carousel(self):
        self.driver.click("delete_profile_btn_on_carousel", timeout=15)

    def click_access_app_on_carousel(self):
        self.driver.click("access_app_on_carousel", timeout=15)

    def click_notification_tab_toggle_switch_lone_page(self):
        self.driver.click("notification_tab_toggle_switch_lone_page", timeout=15)

    def click_top_button_single_press_apps_title(self):
        self.driver.click("top_button_single_press_apps_title", timeout = 15)

    def verify_upper_barrel_card_show_up(self):
        return self.driver.wait_for_object("customize_upper_barrel_button", raise_e=False, timeout=15)

    def verify_lower_barrel_card_show_up(self):
        return self.driver.wait_for_object("customize_lower_barrel_button", raise_e=False, timeout=15)
    
    def get_top_button_long_press_quick_note_text(self):
        return self.driver.get_attribute("customize_top_button_quick_note", "Name", timeout=15)

    def get_nested_pen_name_lone_page(self):
        return self.driver.get_attribute("roo_pen_lone_name","Name", timeout = 15)

    def click_mute_unmute_radio_btn_upper_barrel(self):
        self.driver.click("mute_unmute_radio_btn_upper_barrel", timeout = 15)
    
    def mute_unmute_radio_btn_upper_barrel_selected(self):
        return self.driver.get_attribute("mute_unmute_radio_btn_upper_barrel", "SelectionItem.IsSelected", timeout=15)
    
    def click_mute_unmute_radio_btn_lower_barrel(self):
        self.driver.click("mute_unmute_radio_btn_lower_barrel", timeout = 15)
    
    def mute_unmute_radio_btn_lower_barrel_selected(self):
        return self.driver.get_attribute("mute_unmute_radio_btn_lower_barrel", "SelectionItem.IsSelected", timeout=15)

    def click_undo_radio_btn_upper_barrel(self):
        self.driver.hover("undo_radio_btn_upper_barrel")
        self.driver.click("undo_radio_btn_upper_barrel", timeout = 15)

    def undo_radio_btn_upper_barrel_selected(self):
        return self.driver.get_attribute("undo_radio_btn_upper_barrel", "SelectionItem.IsSelected", timeout=15)

    def click_change_app_to_open_btn_slice1(self):
        self.driver.hover("change_app_to_open_btn_slice1")
        self.driver.click("change_app_to_open_btn_slice1", timeout = 15)

    def click_change_app_to_open_btn_slice2(self):
        self.driver.hover("change_app_to_open_btn_slice2")
        self.driver.click("change_app_to_open_btn_slice2", timeout = 15)

    def click_change_app_to_open_btn_slice3(self):
        self.driver.hover("change_app_to_open_btn_slice3")
        self.driver.click("change_app_to_open_btn_slice3", timeout = 15)

    def click_change_app_to_open_btn_slice4(self):
        self.driver.hover("change_app_to_open_btn_slice4")
        self.driver.click("change_app_to_open_btn_slice4", timeout = 15)

    def click_change_app_to_open_btn_slice5(self):
        self.driver.hover("change_app_to_open_btn_slice5")
        self.driver.click("change_app_to_open_btn_slice5", timeout = 15)

    def click_change_app_to_open_btn_slice6(self):
        self.driver.hover("change_app_to_open_btn_slice6")
        self.driver.click("change_app_to_open_btn_slice6", timeout = 15)

    def click_change_app_to_open_btn_slice7(self):
        self.driver.hover("change_app_to_open_btn_slice7")
        self.driver.click("change_app_to_open_btn_slice7", timeout = 15)

    def click_change_app_to_open_btn_slice8(self):
        self.driver.hover("change_app_to_open_btn_slice8")
        self.driver.click("change_app_to_open_btn_slice8", timeout = 15)
    
    def get_external_display_display_selection_for_input_txt(self):
        return self.driver.get_attribute("external_display_display_selection_for_input_txt", "Name", timeout=15)

    def get_toggle_state_enable_this_feature_toggle_switch_ltwo_page(self):
        return self.driver.get_attribute("enable_this_feature_toggle_switch_ltwo_page", "Toggle.ToggleState", timeout=15)
    
    def click_enable_this_feature_toggle_switch_ltwo_page(self):
        self.driver.click("enable_this_feature_toggle_switch_ltwo_page")
    
    def click_restore_default_button_lone_page(self):
        self.driver.click("restore_default_button_lone_page", timeout=15)
    
    def click_restore_default_continue_button_lone_page(self):
        self.driver.click("restore_default_continue_lone_page", timeout=15)

    def click_customize_buttons_restore_default_button(self):
        self.driver.click("restore_default_customize_button_ltwo_page", timeout=15)    

    def click_customize_buttons_restore_default_continue_button(self):
        self.driver.click("restore_default_customize_button_continue_ltwo_page", timeout=15)  

    def click_restore_default_radial_menu_ltwo_page(self):
        self.driver.click("restore_default_radial_menu_ltwo_page", timeout=15)    

    def click_restore_default_continue_radial_menu_ltwo_page(self):
        self.driver.click("restore_default_radial_menu_continue_ltwo_page", timeout=15) 

    def click_pen_sensitivity_restore_defaults_button(self):
        self.driver.click("restore_default_pen_sensitivity_menu_ltwo_page", timeout=15)    

    def click_restore_default_continue_pen_sensitivity_ltwo_page(self):
        self.driver.click("restore_default_pen_sensitivity_menu_continue_ltwo_page", timeout=15) 

    def click_restore_default_external_display_ltwo_page(self):
        self.driver.click("restore_default_external_display_ltwo_page", timeout=15)    

    def click_restore_default_continue_external_display_ltwo_page(self):
        self.driver.click("restore_default_external_display_continue_ltwo_page", timeout=15) 

    def verify_my_pen_button(self):
        self.driver.wait_for_object("my_pen_button", raise_e=False, timeout=15)



    def get_radial_menu_page_title(self):
        title = self.driver.wait_for_object( "radial_menu_title", raise_e=False, timeout=5)
        logging.info(title)
        if title:
            title = self.driver.get_attribute("radial_menu_title", "Name", timeout=5)
            logging.info(title)
            return title
        return False

    def get_sensitivity_menu_page_title(self):
        title = self.driver.wait_for_object( "sensitivity_menu_title", raise_e=False, timeout=5)
        logging.info(title)
        if title:
            title = self.driver.get_attribute("sensitivity_menu_title", "Name", timeout=5)
            logging.info(title)
            return title
        return False
    
    def click_pen_sensitivity_pressure_slider(self):
        self.driver.click("pen_sensitivity_pressure_slider", timeout = 15)

    def click_pen_sensitivity_tilt_slider(self):
        self.driver.click("pen_sensitivity_tilt_slider", timeout = 15)
    
    def get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_action_ltwo_page", "Name", timeout = 15)

    def get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_lower_barrel_btn_action_ltwo_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_top_btn_single_press_action_ltwo_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_single_press_action_ltwo_page", "Name", timeout = 15)

    def get_pen_control_customize_btn_screen_snipping_action_ltwo_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_screen_snipping_action_ltwo_page", "Name", timeout = 15)

    def get_pen_control_customize_btn_top_btn_long_press_action_ltwo_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_long_press_action_ltwo_page", "Name", timeout = 15)
    
    def get_upper_barrel_hover_click_toggle_lthree_page(self):
        return self.driver.get_attribute("upper_barrel_hover_click_toggle_lthree_page", "Toggle.ToggleState", timeout = 15)

    def get_pen_control_customize_btn_lower_barrel_btn_title_text_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_lower_barrel_btn_title_text_lthree_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_top_btn_single_press_title_text_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_single_press_title_text_lthree_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_top_btn_double_press_title_text_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_double_press_title_text_lthree_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_top_btn_long_press_title_text_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_long_press_title_text_lthree_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_upper_barrel_btn_universal_select_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_universal_select_lthree_page", "Name", timeout = 15)
    
    def get_lowerbarrel_hover_click_toggle_state_lthree_page(self):
        return self.driver.get_attribute("lowerbarrel_hover_click_toggle_lthree_page", "Toggle.ToggleState", timeout = 15)

    def click_pen_control_customize_btn_top_btn_single_press_mute_audio_radio_btn_lthree_page(self):
        self.driver.hover("pen_control_customize_btn_top_btn_single_press_mute_audio_radio_btn_lthree_page")
        self.driver.click("pen_control_customize_btn_top_btn_single_press_mute_audio_radio_btn_lthree_page", timeout = 15)
    
    def get_pen_control_customize_btn_top_btn_single_press_mute_audio_current_assignment_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_top_btn_single_press_mute_audio_current_assignment_lthree_page", "Name", timeout = 15)

    def get_pen_control_customize_btn_upper_barrel_btn_productivity_universal_select_text_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_upper_barrel_btn_productivity_universal_select_text_lthree_page", "Name", timeout = 15)

    def click_pen_control_customize_btn_upper_barrel_btn_pen_forth_click_text_lthree_page(self):
        self.driver.click("pen_control_customize_btn_upper_barrel_btn_pen_forth_click_text_lthree_page", timeout = 15)
    
    def click_pen_control_customize_btn_lower_barrel_btn_apps_email_action_lthree_page(self):
        self.driver.click("pen_control_customize_btn_lower_barrel_btn_apps_email_action_lthree_page", timeout = 15)
        if self.driver.get_attribute("pen_control_customize_btn_lower_barrel_btn_apps_email_radio_btn_lthree_page", "SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_lower_barrel_btn_apps_email_action_lthree_page", timeout = 15)
    
    def click_pen_control_customize_btn_lower_barrel_btn_media_control_mute_audio_action_lthree_page(self):
        self.driver.click("pen_control_customize_btn_lower_barrel_btn_media_control_mute_audio_radio_btn_lthree_page", timeout = 15)
        if self.driver.get_attribute("pen_control_customize_btn_lower_barrel_btn_media_control_mute_audio_radio_btn_lthree_page", "SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_lower_barrel_btn_media_control_mute_audio_radio_btn_lthree_page", timeout = 15)
    
    def get_pen_control_redial_menu_slice1_action_l_ltwo_page(self):
        return self.driver.get_attribute("pen_control_redial_menu_slice1_action_ltwo_page", "Name", timeout = 15)
    
    def verify_pen_control_top_btn_double_press_screen_snipping_action_lthree_page(self):
        return self.driver.wait_for_object("pen_control_top_btn_double_press_screen_snipping_action_lthree_page", raise_e=False, timeout=10)

    def click_pen_control_top_btn_double_press_media_control_mute_audio_action_lthree_page(self):
        self.driver.click("pen_control_top_btn_double_press_media_control_mute_audio_action_lthree_page",timeout = 15)

    def click_pen_control_top_btn_double_press_media_control_quick_note_action_lthree_page(self):
        self.driver.click("pen_control_top_btn_double_press_media_control_quick_note_action_lthree_page",timeout = 15)
    
    def click_pen_control_customize_btn_top_btn_long_press_media_control_mute_action_lthree_page(self):
        self.driver.hover("pen_control_customize_btn_top_btn_long_press_media_control_mute_action_lthree_page")
        self.driver.click("pen_control_customize_btn_top_btn_long_press_media_control_mute_action_lthree_page",timeout = 15)
            
    def get_pen_ltwo_page_title(self):
        title = self.driver.wait_for_object( "pen_ltwo_page_title", raise_e=False, timeout=5)
        logging.info(title)
        if title:
            title = self.driver.get_attribute("pen_ltwo_page_title", "Name", timeout=5)
            logging.info(title)
            return title
        return False
    
    def verify_radial_menu_card(self):
        return self.driver.wait_for_object("radial_menu_commercial", raise_e=False, timeout=5)
    
    def click_pen_control_customize_btn_top_btn_single_press_pen_menu_action_lthree_page(self):
        self.driver.click("pen_control_customize_btn_top_btn_single_press_pen_menu_action_lthree_page", timeout = 15)
        if self.driver.get_attribute("pen_control_customize_btn_top_btn_single_press_pen_menu_radio_btn_lthree_page", "SelectionItem.IsSelected") == "false":
            self.driver.click("pen_control_customize_btn_top_btn_single_press_pen_menu_action_lthree_page", timeout = 15)
    
    def get_radial_menu_commercial_slice1(self):
        return self.driver.get_attribute("radial_menu_ltwo_slice1_assigned_app_not_available", "Name", timeout=5)
    
    def get_radial_menu_commercial_slice2(self):
        return self.driver.get_attribute("radial_menu_ltwo_slice2_assigned_app_not_available", "Name", timeout=15)

    def get_one_step_inking_card(self):
        return self.driver.get_attribute("one_step_inking_card", "Name", timeout = 15)
    
    def verify_pen_control_one_step_ink_card_image_ltwo_page(self):
        return self.driver.wait_for_object("pen_control_one_step_ink_card_image_lone_page", raise_e=False, timeout=15) is not False
        
    def get_pen_control_one_step_ink_subheader_text_lone_page(self):
        return self.driver.get_attribute("pen_control_one_step_ink_subheader_text_lone_page", "Name", timeout = 15)

    def click_one_step_inking_screen_snipping_1(self):
        self.driver.click("one_step_inking_screen_snipping", timeout = 15)
        if self.driver.get_attribute("pen_control_one_step_ink_screen_snipping_radio_btn_ltwo_page", "SelectionItem.IsSelected") == "false":
            self.driver.click("one_step_inking_screen_snipping", timeout = 15)
    
    def verify_one_step_inking_pen_menu(self):
        return self.driver.wait_for_object("one_step_inking_pen_menu", raise_e=False, timeout=15) is not False

    def verify_one_step_inking_one_note(self):
        return self.driver.wait_for_object("one_step_inking_one_note", raise_e=False, timeout=15) is not False
    
    def verify_one_step_inking_ms_white_board(self):
        return self.driver.wait_for_object("one_step_inking_ms_white_board", raise_e=False, timeout=15) is not False
    
    def verify_one_step_inking_snipping_tool(self):
        return self.driver.wait_for_object("one_step_inking_snipping_tool", raise_e=False, timeout=15) is not False
    
    def verify_one_step_inking_open_app(self):
        return self.driver.wait_for_object("one_step_inking_open_app", raise_e=False, timeout=15) is not False

    def verify_one_step_inking_disabled(self):
        return self.driver.wait_for_object("one_step_inking_disabled", raise_e=False, timeout=15) is not False

    def click_one_step_inking_card(self):
        self.driver.click("one_step_inking_card", timeout=15)
    
    def get_pen_sensitivity_tilt_slider_value(self):
        return self.driver.get_attribute("pen_sensitivity_tilt_slider", "Value.Value", timeout=15)
    
    def set_slider_max(self,slider):
        slider_element = self.driver.wait_for_object(slider, timeout=30)
        for _ in range(4):
            slider_element.send_keys(Keys.RIGHT)
            if self.driver.get_attribute(slider, "Value.Value", timeout=15) == "2":
                break
            else:
                slider_element.send_keys(Keys.RIGHT)
            time.sleep(2)
      
    def click_display_selection_drop_down(self):
        self.driver.click("display_selection_picker",timeout =15)

    def click_first_display_from_drop_down(self):
        self.driver.click("display_selection_picker_first_display",timeout =15)

    def click_landscape_radio_button(self):
        self.driver.hover("landscape_ltwo_page")
        time.sleep(3)
        self.driver.click("landscape_ltwo_page", timeout=15)
        
    def click_landscape_flipped_radio_button(self):
        self.driver.hover("landscape_flipped_ltwo_page")
        self.driver.click("landscape_flipped_ltwo_page", timeout=15)
       
    def click_portrait_orientation(self):
        self.driver.click("portrait_ltwo_page", timeout=15)

    def click_portrait_flipped_orientation(self):
        self.driver.click("portrait_flipped_ltwo_page", timeout=15)

    def click_pen_only_mode(self):
        self.driver.click("pen_only_ltwo_page", timeout = 15)

    def click_pen_and_touch_mode(self):
        self.driver.click("pen_and_touch_ltwo_page", timeout = 15)
    
    def click_scale_display_mapping(self):
        self.driver.click("scale_ltwo_page", timeout=15)

    def click_stretch_display_mapping(self):
        self.driver.click("stretch_ltwo_page", timeout=15)

    def swipe_down_to_element(self, locator):
        #swipe to top first and then swipe down to the element
        logging.info("Scroll to top first")
        self.driver.swipe(direction="up", distance=15)
        self.driver.scroll_element(locator)
        #swipe one more in case the element is not fully displayed.
        logging.info("swipe one more in case the element is not fully displayed")
        self.driver.swipe(direction="down", distance=1)
        assert self.driver.wait_for_object(locator, raise_e=False, timeout = 5), "Couldn't locate {locator}"
        
    def swipe_down_to_external_display_card(self):
        self.swipe_down_to_element("external_display_card")

    def swipe_down_to_pen_sensitivity_card(self):
        self.swipe_down_to_element("pen_sensitivity_card")

    def swipe_down_to_restore_default_lone_button(self):
        self.swipe_down_to_element("restore_default_button_lone_page")
   
    def swipe_down_to_restore_default_external_display_ltwo_page(self):
        self.swipe_down_to_element("restore_default_external_display_ltwo_page")
    
    def swipe_down_to_scale_and_stretch_radio_butons(self):
        self.swipe_down_to_element("scale_ltwo_page")

    def click_one_step_inking_card(self):
        self.driver.click("one_step_inking_card", timeout=15)

    def swipe_down_to_one_step_inking_card(self):
        self.swipe_down_to_element("one_step_inking_card")

    def wait_hover_and_click_radio_button(self,element):
        self.driver.wait_for_object(element, raise_e=False, timeout = 5)
        self.driver.hover(element)
        time.sleep(1)
        self.driver.click(element, timeout=15)       

    def click_one_step_inking_pen_menu(self):
        self.wait_hover_and_click_radio_button("one_step_inking_pen_menu")

    def click_one_step_inking_one_note(self):
        self.wait_hover_and_click_radio_button("one_step_inking_one_note")
 
    def click_one_step_inking_ms_white_board(self):
        self.wait_hover_and_click_radio_button("one_step_inking_ms_white_board")

    def click_one_step_inking_snipping_tool(self):
        self.wait_hover_and_click_radio_button("one_step_inking_snipping_tool")

    def click_one_step_inking_screen_snipping(self):
        self.wait_hover_and_click_radio_button("one_step_inking_screen_snipping")

    def click_one_step_inking_open_app(self):
        self.wait_hover_and_click_radio_button("one_step_inking_open_app")

    def click_one_step_inking_open_app_cancel_button(self):
        is_button_present =  self.driver.wait_for_object("one_step_inking_open_app_cancel_button", raise_e=False, timeout = 5)
        if is_button_present:
            self.driver.click("one_step_inking_open_app_cancel_button", timeout=15)

    def click_one_step_inking_disabled(self):
        self.wait_hover_and_click_radio_button("one_step_inking_disabled")

    def click_notification_tab_toggle_off_switch_lone_page(self):
        self.driver.click("notification_tab_toggle_off_switch_lone_page",timeout=10)

    def get_toggle_state_of_alert(self,on_locator,off_locator):
        toggle_state= self.driver.get_attribute(on_locator,"Toggle.ToggleState",raise_e=False, timeout=10)
        if not toggle_state:
            toggle_state = self.driver.get_attribute(off_locator,"Toggle.ToggleState",raise_e=False, timeout=10)
        return toggle_state

    def get_toggle_state_pen_not_detected_alert(self):
        return self.get_toggle_state_of_alert("pen_not_detected_alert_toggle_on","pen_not_detected_alert_toggle_off")

    def get_toggle_state_pen_out_of_range_alert(self):
        return self.get_toggle_state_of_alert("notification_tab_toggle_switch_lone_page","notification_tab_toggle_off_switch_lone_page")

    def get_toggle_state_pen_power_saving_alert(self):
        return self.get_toggle_state_of_alert("power_saving_alert_toggle_on","power_saving_alert_toggle_off")

    def click_power_saving_alert_toggle_on(self):
        self.driver.click("power_saving_alert_toggle_on",timeout=10)

    def click_power_saving_alert_toggle_off(self):
        self.driver.click("power_saving_alert_toggle_off",timeout=10)

    def click_pen_not_detected_alert_toggle_on(self):
        self.driver.click("pen_not_detected_alert_toggle_on",timeout=10)

    def click_pen_not_detected_alert_toggle_off(self):
        self.driver.click("pen_not_detected_alert_toggle_off",timeout=10)

    def swipe_to_alert_when_pen_is_idle_text(self):
        self.swipe_down_to_element("alert_when_pen_is_idle_text")

    def click_touch_stylus_for_status(self):
        self.driver.click("touch_stylus_for_status_button",timeout=10)

    def swipe_down_to_radial_slice1_apps_ms_whiteboard_radio_button(self) :
        self.swipe_down_to_element("radial_menu_commercial_slice1_apps_ms_whiteboard_radio_button")

    def click_radial_menu_needs_reassignment_button(self) :
        self.driver.click("radial_menu_needs_reassignment_button",timeout=10)

    def click_one_step_inking_needs_reassignment_button(self):
        self.driver.click("one_step_inking_needs_reassignment_button",timeout=10)

    def click_button_needs_reassignment_button(self): 
        self.driver.click("button_needs_reassignment_button",timeout=10)

    def get_radial_menu_needs_reassignment_button(self):
        return self.driver.wait_for_object("radial_menu_needs_reassignment_button",raise_e=False, timeout=10)

    def get_one_step_inking_needs_reassignment_button(self):
        return self.driver.wait_for_object("one_step_inking_needs_reassignment_button", raise_e=False, timeout=10)

    def get_button_needs_reassignment_button(self): 
        return self.driver.wait_for_object("button_needs_reassignment_button", raise_e=False, timeout=10)

    def swipe_down_to_upper_barrel_button_ms_whiteboard(self):
        self.swipe_down_to_element("customize_buttons_upper_barrel_mswhiteboard_lthree_page")

    def hover_element(self, element):
        self.driver.hover(element)
    
    def click_pencontrol_lower_barrel_btn_prod_radial_menu(self):
        self.driver.hover("pencontrol_lower_barrel_btn_prod_radial_menu")
        self.driver.click("pencontrol_lower_barrel_btn_prod_radial_menu", timeout = 15)

    # Wait for Customize Buttons card and compare the screenshot against the golden image stored in ImageBank
    @screenshot_compare(root_obj="customize_buttons", pass_ratio=0.01)
    def wait_and_verify_customize_buttons(self, raise_e=True):
        return self.driver.wait_for_object("customize_buttons", raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["pen_type"], root_obj="pen_sensitivity_card", pass_ratio=0.01)
    def wait_and_verify_pen_sensitivity_card(self, pen_type, raise_e=True):
        return self.driver.wait_for_object("pen_sensitivity_card", raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["barrel_type"], root_obj="radial_menu_commercial", pass_ratio=0.01)
    def verify_radial_menu_commercial_barrel_buttons(self, barrel_type, raise_e=True):
        return self.driver.wait_for_object("radial_menu_commercial", raise_e=raise_e, timeout=10)

    
    @screenshot_compare(include_param=["slice_number"],root_obj="desktop_icon_on_pen_external_display_ltwo_page", pass_ratio=0.01, )
    def verify_slice_image(self, slice_number, raise_e=True ):
        self.driver.hover(f"radial_menu_commercial_slice{slice_number}")
        return self.driver.wait_for_object("desktop_icon_on_pen_external_display_ltwo_page", raise_e=raise_e, timeout=10)

    def verify_restore_default_radial_menu_ltwo_page(self):
        return self.driver.wait_for_object("restore_default_radial_menu_ltwo_page",raise_e=True, timeout=15)    
    
    def verify_slice(self, slice_number, raise_e=True):
        return self.driver.wait_for_object(f"radial_menu_commercial_slice{slice_number}", raise_e=raise_e, timeout=10)

    @screenshot_compare(root_obj="desktop_icon_on_pen_external_display_ltwo_page", pass_ratio=0.01)
    def verify_radial_menu_ltwo_default_image(self, raise_e=True):
         return self.driver.wait_for_object("desktop_icon_on_pen_external_display_ltwo_page", raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param = ["pen_type"], root_obj="pen_image_lone_page", pass_ratio=0.01)
    def verify_pen_lone_image(self, pen_type, raise_e=True):
        return self.driver.wait_for_object("pen_image_lone_page", raise_e=raise_e, timeout=5)

    @screenshot_compare(include_param = ["barrel_type", "pen_type"], root_obj="desktop_icon_on_pen_external_display_ltwo_page", pass_ratio=0.01)
    def verify_customize_buttons_pen_lwo_image(self, barrel_type, pen_type, raise_e=True):
        return self.driver.wait_for_object("desktop_icon_on_pen_external_display_ltwo_page", raise_e=raise_e, timeout=5)
    
    @screenshot_compare(include_param = [ "pen_type"], root_obj="desktop_icon_on_pen_external_display_ltwo_page", pass_ratio=0.01)
    def verify_pen_sensitivity_lwo_image(self,  pen_type, raise_e=True):
        return self.driver.wait_for_object("desktop_icon_on_pen_external_display_ltwo_page", raise_e=raise_e, timeout=5)

    def click_windows_settings_title_bar(self):
        self.driver.click("windows_settings_title_bar", timeout=15)

    def wait_for_customize_buttons_element(self):
        self.driver.wait_for_object("customize_buttons", timeout=30)

    @screenshot_compare(include_param = ["barrel_type"], root_obj="trio_pen_image_ltwo_page", pass_ratio=0.01)
    def verify_customize_buttons_pen_lwo_image_trio(self,barrel_type, raise_e=True):
        return self.driver.wait_for_object("trio_pen_image_ltwo_page", raise_e=raise_e, timeout=5)

    @screenshot_compare(root_obj="trio_pen_image_ltwo_page", pass_ratio=0.01)
    def verify_pen_sensitivity_lwo_image_trio(self, raise_e=True):
        return self.driver.wait_for_object("trio_pen_image_ltwo_page", raise_e=raise_e, timeout=5)

    def get_upper_barrel_button_current_assignment_value(self):
        return self.driver.get_attribute("upper_barrel_button_current_assignment", "Name", raise_e=False, timeout=5)

    def get_top_button_single_press_current_assignment_value(self):
        return self.driver.get_attribute("top_button_single_press_current_assignment", "Name", raise_e=False, timeout=5)

    def get_lower_barrel_button_current_assignment_value(self):
        return self.driver.get_attribute("lower_barrel_button_current_assignment", "Name", raise_e=False, timeout=5)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.01)
    def verify_pen_lone_page(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.01)
    def verify_pen_ltwo_page(self, machine_name, page_title, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    def click_customize_topbutton_single_press_screensnipping_radio_button(self):
        self.driver.click("customize_topbutton_single_press_screensnipping_radio_button", timeout = 15)

    def click_customize_topbutton_double_press_mswhiteboard_radio_button(self):
        self.driver.click("customize_topbutton_double_press_mswhiteboard_radio_button", timeout = 15)
    
    def click_customize_topbutton_long_press_screen_snipping_radio_button(self):
        self.driver.click("customize_topbutton_long_press_screen_snipping_radio_button", timeout = 15)

    def click_customize_upper_barrel_erase_radio_button(self):
        self.driver.click("customize_upper_barrel_erase_radio_button", timeout = 15)
    
    def click_customize_lower_barrel_right_click_radio_button(self):
        self.driver.click("customize_lower_barrel_right_click_radio_button", timeout = 15)
    
    def get_customize_btn_lower_barrel_right_click_action(self):
        return self.driver.get_attribute("customize_btn_lower_barrel_right_click_action", "Name", timeout = 15)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"], pass_ratio=0.01)
    def verify_pen_lone_page_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    def click_pen_control_customize_btn_lower_barrel_btn_undo_radio_btn_lthree_page(self):
        self.driver.click("pen_control_customize_btn_lower_barrel_btn_undo_radio_btn_lthree_page", timeout = 15)
    
    def get_pen_control_customize_btn_upper_barrel_undo_action_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_upper_barrel_undo_action_lthree_page", "Name", timeout = 15)
    
    def get_pen_control_customize_btn_lower_barrel_undo_action_lthree_page(self):
        return self.driver.get_attribute("pen_control_customize_btn_lower_barrel_undo_action_lthree_page", "Name", timeout = 15)
    
    def click_radial_menu_slice1_paste_radio_btn(self):
        self.driver.click("radial_menu_slice1_paste_radio_btn", timeout = 15)
    
    def click_radial_menu_slice2_paste_radio_btn(self):
        self.driver.click("radial_menu_slice2_paste_radio_btn", timeout = 15)

    @screenshot_compare(include_param=["pen_name", "page_number", "mode"], pass_ratio=0.01)
    def verify_pen_lone_page_mode(self, pen_name, page_number, element, mode, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    def get_pen_name_on_lone_page(self):
        return self.driver.get_attribute("pen_name_on_lone_page","Name", timeout = 15)

    def verify_external_display_title_text(self):
        return self.driver.wait_for_object("external_display_title_text", raise_e=False, timeout=10) is not False
    
    def verify_pen_control_customize_btn_top_btn_single_press_title_text_lthree_page(self):
        return self.driver.wait_for_object("pen_control_customize_btn_top_btn_single_press_title_text_lthree_page", raise_e=False, timeout=10) is not False
    
    def enter_app_name_in_add_app_search_bar_ltwo_page(self, app_name):
        self.driver.send_keys("search_box_on_add_application_popup", app_name)
        