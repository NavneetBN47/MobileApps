from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time
from selenium.webdriver.common.keys import Keys

class VideoControl(HPXFlow):
    flow_name = "video_control"

    def verify_video_control_auto_frame(self):
        return self.driver.wait_for_object("auto_frame_btn", raise_e=False, timeout=30)

    def maximize_window(self):
        self.driver.click("maximize_window")

    def verify_enhance_your_video_experience_show(self):
        return self.driver.wait_for_object("Enhance_your_video")

    def verify_tutorial_next_button_show(self):
        return self.driver.wait_for_object("tutorial_next_button")

    def click_tutorial_next_button(self):
        self.driver.click("tutorial_next_button")

    def verify_lets_get_your_show(self):
        return self.driver.wait_for_object("let_get_your")

    def verify_gallery_view_toggle_status(self):
        return self.driver.get_attribute("gallery_view_btn", "Toggle.ToggleState")

    def click_gallery_view_btn(self):
        self.driver.click("gallery_view_btn", raise_e=False, timeout=30)

    def click_gallery_view_text(self):
        self.driver.click("gallery_views")

    def click_auto_frame_btn(self):
        self.driver.click("auto_frame_btn", raise_e=False, timeout=30)

    def verify_auto_frame_toggle_status(self):
        return self.driver.get_attribute("auto_frame_btn", "Toggle.ToggleState")

    def verify_video_control_Enhance(self):
        return self.driver.wait_for_object("enhance_btn", raise_e=False, timeout=30)

    def click_enhance_btn(self):
        self.driver.click("enhance_btn", raise_e=False, timeout=30)

    def verify_enhance_toggle_status(self):
        return self.driver.get_attribute("enhance_btn", "Toggle.ToggleState")

    def verify_video_control_gallery_view(self):
        return self.driver.wait_for_object("gallery_view", raise_e=False, timeout=30)

    def verify_enhance_toggle_status(self):
        return self.driver.get_attribute("enhance_btn", "Toggle.ToggleState")

    def verify_enhance_your_video_experience_show(self):
        return self.driver.wait_for_object("enhance_your_video")

    def verify_tutorial_next_button_show(self):
        return self.driver.wait_for_object("tutorial_next_button")

    def click_tutorial_next_button(self):
        self.driver.click("tutorial_next_button")

    def verify_lets_get_your_show(self):
        return self.driver.wait_for_object("let_get_your")

    def verify_video_control_gallery_view(self):
        return self.driver.wait_for_object("gallery_view_btn", raise_e=False, timeout=30)

    def verify_gallery_view_toggle_status(self):
        return self.driver.get_attribute("gallery_view_btn", "Toggle.ToggleState")

    def verify_video_control_background_off(self):
        return self.driver.wait_for_object("background_off")

    def verify_video_control_resolutioncombobox_auto(self):
        return self.driver.wait_for_object("resoultioncombobox_auto")

    def verify_mixer_tab_show(self):
        return self.driver.wait_for_object("mixer_tab", raise_e=False, timeout=30)

    def click_mixer_tab(self):
        self.driver.click("mixer_tab")

    def click_gallery_view_btn(self):
        self.driver.click("gallery_view_btn", raise_e=False, timeout=30)

    def click_gallery_view_text(self):
        self.driver.click("gallery_views")

    def verify_video_control_auto_frame(self):
        return self.driver.wait_for_object("auto_frame_btn", raise_e=False, timeout=30)

    def verify_video_control_Enhance(self):
        return self.driver.wait_for_object("enhance_btn", raise_e=False, timeout=30)

    def verify_video_control_background_off_status(self):
        return self.driver.get_attribute("background_off", "Name")

    def verify_video_control_resolutioncombobox_auto(self):
        return self.driver.wait_for_object("resoultioncombobox_auto")

    def verify_mixer_tab_show(self):
        return self.driver.wait_for_object("mixer_tab")

    def click_mixer_tab(self):
        self.driver.click("mixer_tab")

    def verify_picture_in_picture_show(self):
        return self.driver.wait_for_object("picture_in_picture")

    def move_down_for_restore(self,element):
        el = self.driver.wait_for_object("scroll_window", displayed=False, timeout=3)	
        for i in range(33):
            el.send_keys(Keys.TAB)
            find_element = self.driver.wait_for_object(element, raise_e=False, timeout=1)
                       
    def move_down_page(self, element):
        el = self.driver.wait_for_object("scroll_window", displayed=False, timeout=3)
        for i in range(40):
            el.send_keys(Keys.TAB)
            find_element = self.driver.wait_for_object(element, raise_e=False, timeout=1)

    def verify_tutorial_button_show(self):
        return self.driver.wait_for_object("tutorial_button_icon")

    def click_tutorial_button(self):
        self.driver.click("tutorial_button_icon")

    def verify_backlight_adjustment_text_show(self):
        return self.driver.wait_for_object("backlight_adjustment_text")

    def verify_backlight_adjustment_toggle_status(self):
        return self.driver.get_attribute("backlight_adjustment_btn", "Toggle.ToggleState")

    def click_backlight_adjustment_btn(self):
        self.driver.click("backlight_adjustment_btn")

    def verify_lowlight_adjustment_text_show(self):
        return self.driver.wait_for_object("lowlight_adjustment_text")

    def verify_lowlight_adjustment_toggle_status(self):
        return self.driver.get_attribute("lowlight_adjustment_btn", "Toggle.ToggleState")

    def click_lowlight_adjustment_btn(self):
        self.driver.click("lowlight_adjustment_btn")

    def verify_natural_tone_text_show(self):
        return self.driver.wait_for_object("natural_tone_text")

    def verify_natural_tone_toggle_status(self):
        return self.driver.get_attribute("natural_tone_btn", "Toggle.ToggleState")

    def click_natural_tone_btn(self):
        self.driver.click("natural_tone_btn")

    def verify_background_blur_text_show(self):
        return self.driver.wait_for_object("background_blur_text")

    def click_background_blur_btn(self):
        self.driver.click("background_blur_btn")

    def verify_background_blur_status(self):
        return self.driver.get_attribute("background_blur_btn", "Name")

    def verify_large_small_show(self):
        return self.driver.wait_for_object("large_small_btn")

    def click_large_small_btn(self):
        self.driver.click("large_small_btn")

    def verify_large_small_btn_status(self):
        return self.driver.get_attribute("large_small_btn", "Name")

    def move_down_page_1(self, element):
        el = self.driver.wait_for_object("scroll_window", displayed=False, timeout=3)
        for i in range(57):
            el.send_keys(Keys.TAB)
            find_element = self.driver.wait_for_object(element, raise_e=False, timeout=1)

    def move_down_page_2(self, element):
        el = self.driver.wait_for_object("scroll_window", displayed=False, timeout=3)
        for i in range(17):
            el.send_keys(Keys.TAB)
            find_element = self.driver.wait_for_object(element, raise_e=False, timeout=1)

    def verify_restore_button_show(self):
        return self.driver.wait_for_object("restore_default")

    def click_restore_button(self):
        self.driver.click("restore_default")

    def click_maximize_video_control_window(self):
        self.driver.click("maximize_video_control_page")

    def verify_video_control_window_maximize(self):
        if (self.driver.wait_for_object("maximize_video_control_page", invisible=False, raise_e=False)):
            return self.driver.wait_for_object("maximize_video_control_page").get_attribute("Name")
        return ""

    def get_enhance_video_control_text(self):
        return self.driver.get_attribute("tutorial_first_page_lable_text", "Name", timeout=20)

    def get_tutorial_first_page_tip_text(self):
        return self.driver.get_attribute("tutorial_first_page_tip_text", "Name", timeout=20)

    def get_start_hp_enhanced_camera_text(self):
        return self.driver.get_attribute("start_hp_enhanced_camera_text", "Name", timeout=20)

    def click_next_arrow(self):
        self.driver.click("next_page_arrow")

    def get_lets_get_you_ready_text(self):
        return self.driver.get_attribute("tutorial_second_page_lable_text", "Name", timeout=20)

    def get_tutorial_second_page_tip_text(self):
        return self.driver.get_attribute("tutorial_second_page_tip_text", "Name", timeout=20)

    def get_camera_input_text(self):
        return self.driver.get_attribute("camera_input_text", "Name", timeout=20)

    def get_hp_enhanced_camera_text(self):
        return self.driver.get_attribute("hp_enhanced_camera_text", "Name", timeout=20)

    def get_hp_wide_vision_5mp_camera_text(self):
        return self.driver.get_attribute("hp_wide_vision_5mp_camera_text", "Name", timeout=20)

    def mixer_help_button_to_navigate_back_to_tutorial_first_page(self):
        if self.driver.wait_for_object("mixer_help_button_to_navigate_back_to_tutorial_first_page", raise_e=False,timeout=10):
            self.driver.click("mixer_help_button_to_navigate_back_to_tutorial_first_page")

    def get_help_text(self):
        return self.driver.get_attribute("mixer_help_button_to_navigate_back_to_tutorial_first_page", "Name", timeout=20)

    def get_mixer_button_text(self):
        return self.driver.get_attribute("mixer_tab", "Name", timeout=20)

    def click_mixer_button(self):
        self.driver.click("mixer_tab")

    def get_layouts_text(self):
        return self.driver.get_attribute("layouts_text", "Name", timeout=20)

    def click_split_screen_button(self):
        self.driver.click("split_screen_text", timeout=20)

    def get_split_screen_text(self):
        return self.driver.get_attribute("split_screen_text", "Name", timeout=20)

    def click_picture_in_picture_button(self):
        self.driver.click("picture_in_picture_text", timeout=20)
    
    def verify_picture_in_picture_status(self): 
        return self.driver.get_attribute("picture_in_picture", "Name")
        
    def verify_my_tab_button_with_icon_1(self): 
        return self.driver.wait_for_object("my_tab_button_with_icon_1")
    
    def click_my_tab_button_with_icon_1(self):
        self.driver.click("my_tab_button_with_icon_1")
    
    def get_picture_in_picture_text(self):
        return self.driver.get_attribute("picture_in_picture_text", "Name", timeout=20)

    def click_large_small_button(self):
        self.driver.click("large_small_text", timeout=20)

    def get_large_small_text(self):
        return self.driver.get_attribute("large_small_text", "Name", timeout=20)

    def get_restore_default_settings_text(self):
        return self.driver.get_attribute("restore_default_settings_text", "Name", timeout=20)

    def get_default_auto_text(self):
        return self.driver.get_attribute("auto_text_for_combo_box", "Name", timeout=20)

    def click_default_auto_text(self):
        self.driver.click("auto_text_for_combo_box", timeout=20)

    def click_auto_dropbox_tooltip_text(self):
        self.driver.click("auto_dropbox_tooltip", timeout=20)

    def get_auto_dropbox_tooltip_text(self):
        return self.driver.get_attribute("auto_dropbox_tooltip", "Name", timeout=20)

    def click_auto_dropbox_caret(self):
        self.driver.click("combo_box_caret", timeout=30)

    def get_auto_dropbox_2160p_text(self):
        return self.driver.get_attribute("auto_dropbox_first_element_text", "Name", timeout=20)

    def get_auto_dropbox_1440p_text(self):
        return self.driver.get_attribute("auto_dropbox_second_element_text", "Name", timeout=20)

    def get_auto_dropbox_1080p_text(self):
        return self.driver.get_attribute("auto_dropbox_third_element_text", "Name", timeout=20)

    def get_auto_dropbox_720p_text(self):
        return self.driver.get_attribute("auto_dropbox_fourth_element_text", "Name", timeout=20)

    def get_auto_dropbox_360psd_text(self):
        return self.driver.get_attribute("auto_dropbox_fifth_element_text", "Name", timeout=20)

    def get_auto_text(self):
        return self.driver.get_attribute("auto_dropbox_sixth_element_text", "Name", timeout=20)

    def get_hp_wide_vision_5mp_camera1_text(self):
        return self.driver.get_attribute("shp_wide_vision_5mp_camera1_text", "Name", timeout=20)

    def click_camera_settings_to_go_back_main_screen(self):
        self.driver.click("camera_settings_text", timeout=20)

    def get_gallery_view_text(self):
        self.driver.click("gallery_view_text_button", timeout=20)
        return self.driver.get_attribute("gallery_view_text_button", "Name", timeout=20)

    def get_auto_frame_text(self):
        return self.driver.get_attribute("auto_frame_text", "Name", timeout=20)

    def get_gallery_view_tooltip_text(self):
        self.driver.click("gallary_view_tooltip", timeout=20)
        return self.driver.get_attribute("gallary_view_tooltip", "Name", timeout=20)

    def get_auto_frame_tooltip_text(self):
        self.driver.click("auto_frame_tooltip", timeout=20)
        return self.driver.get_attribute("auto_frame_tooltip", "Name", timeout=20)

    def click_auto_frame_toggle_switch(self):
        self.driver.click("auto_frame_toggle_switch", timeout=20)

    def click_auto_frame_wide_frame(self):
        self.driver.click("wide_pic_frame_button", timeout=20)

    def get_auto_frame_wide_frame_text(self):
        return self.driver.get_attribute("wide_pic_frame_button", "Name", timeout=20)

    def click_auto_frame_portrait_frame(self):
        self.driver.click("portrait_pic_frame_button", timeout=20)

    def get_auto_frame_portrait_frame_text(self):
        return self.driver.get_attribute("portrait_pic_frame_button", "Name", timeout=20)

    def click_auto_frame_tight_frame(self):
        self.driver.click("tight_pic_frame_button", timeout=20)

    def get_auto_frame_tight_frame_text(self):
        return self.driver.get_attribute("tight_pic_frame_button", "Name", timeout=20)

    def get_enhance_text(self):
        return self.driver.get_attribute("enhance_text", "Name", timeout=20)

    def get_enhance_tooltip_text(self):
        self.driver.click("enhance_tooltip", timeout=20)
        return self.driver.get_attribute("enhance_tooltip", "Name", timeout=20)

    def click_enhance_toggle_switch(self):
        self.driver.click("enhance_toggle_switch", timeout=20)

    def get_backlight_adjustment_text(self):
        return self.driver.get_attribute("backlight_adjustment_text", "Name", timeout=20)

    def get_low_light_adjustment_text(self):
        return self.driver.get_attribute("low_light_adjustment_text", "Name", timeout=20)

    def get_natural_tone_text(self):
        return self.driver.get_attribute("natural_tone_text", "Name", timeout=20)

    def get_natural_tone_tooltip_text(self):
        self.driver.click("natural_tone_tooltip", timeout=20)
        return self.driver.get_attribute("natural_tone_tooltip", "Name", timeout=20)

    def get_appearance_filter_text(self):
        return self.driver.get_attribute("appearance_filter_text", "Name", timeout=20)

    def get_eye_contact_text(self):
        return self.driver.get_attribute("eye_contact_text", "Name", timeout=20)

    def get_eye_contact_tooltip_text(self):
        self.driver.click("eye_contact_tooltip", timeout=20)
        return self.driver.get_attribute("eye_contact_tooltip", "Name", timeout=20)

    def get_background_text(self):
        return self.driver.get_attribute("background_text", "Name", timeout=20)

    def get_add_new_text(self):
        return self.driver.get_attribute("add_new_text", "Name", timeout=20)

    def get_off_text(self):
        return self.driver.get_attribute("off_text", "Name", timeout=20)

    def get_blur_text(self):
        return self.driver.get_attribute("blur_text", "Name", timeout=20)

    def get_officeone_text(self):
        return self.driver.get_attribute("office1_text", "Name", timeout=20)

    def get_officetwo_text(self):
        return self.driver.get_attribute("office2_text", "Name", timeout=20)

    def get_cafe_text(self):
        return self.driver.get_attribute("cafe_text", "Name", timeout=20)

    def get_living_room_text(self):
        return self.driver.get_attribute("living_room_text", "Name", timeout=20)

    def get_outdoor_text(self):
        return self.driver.get_attribute("outdoor_text", "Name", timeout=20)

    def get_restore_default_settings_text(self):
        return self.driver.get_attribute("restore_default_settings_text", "Name", timeout=20)

    def get_hp_presence_logo_text(self):
        return self.driver.get_attribute("hp_presence_logo_text", "Name", timeout=20)

    def get_anti_flicker_off_text(self):
        return self.driver.get_attribute("anti_flicker_off_text", "Name", timeout=20)

    def click_anti_flicker_off(self):
        self.driver.click("anti_flicker_off_text")

    def get_anti_flicker_off_combobox_first_element_text(self):
        return self.driver.get_attribute("anti_flicker_off_combobox_first_element", "Name", timeout=20)

    def get_anti_flicker_off_combobox_second_element_text(self):
        return self.driver.get_attribute("anti_flicker_off_combobox_second_element", "Name", timeout=20)

    def get_anti_flicker_off_combobox_third_element_text(self):
        return self.driver.get_attribute("anti_flicker_off_combobox_third_element", "Name", timeout=20)

    def get_anti_flicker_off_tooltip_text(self):
        self.driver.click("anti_flicker_off_tooltip", timeout=20)
        return self.driver.get_attribute("anti_flicker_off_tooltip", "Name", timeout=20)

    def click_auto(self):
        self.driver.click("enhance_toggle_switch", timeout=20)

    def get_allow_multiple_ppl_face_framing_text(self):
        return self.driver.get_attribute("allow_multiple_ppl_face_framing_text", "Name", timeout=20)

    def get_allow_multiple_ppl_face_framing_tooltip(self):
        self.driver.click("allow_multiple_ppl_face_framing_tooltip", timeout=20)
        return self.driver.get_attribute("allow_multiple_ppl_face_framing_tooltip", "Name", timeout=20)

    def get_low_battery_usage_text(self):
        return self.driver.get_attribute("low_battery_usage_text", "Name", timeout=20)

    def get_medium_battery_usage_text(self):
        return self.driver.get_attribute("medium_battery_usage_text", "Name", timeout=20)

    def get_high_battery_usage_text(self):
        return self.driver.get_attribute("high_battery_usage_text", "Name", timeout=20)

    def get_battery_usage_tooltip_text(self):
        self.driver.click("low_battery_usage_tooltip", timeout=20)
        return self.driver.get_attribute("low_battery_usage_tooltip", "Name", timeout=20)

    def get_share_as_window_text(self):
        #self.driver.click("sidebar_button_share_as_window_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_share_as_window_text", "Name", timeout=20)

    def get_hp_enhanced_camera_view_text(self):
        return self.driver.get_attribute("hp_enhanced_camera_view_title_bar_text", "Name", timeout=20)

    def get_save_a_pdf_text(self):
        self.driver.click("sidebar_button_save_a_pdf_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_save_a_pdf_text", "Name", timeout=20)

    def get_snap_phote_text(self):
        self.driver.click("sidebar_button_snap_photo_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_snap_photo_text", "Name", timeout=20)

    def get_start_recording_text(self):
        return self.driver.get_attribute("sidebar_button_start_recording_text", "Name", timeout=20)

    def click_start_recording_text(self):
        self.driver.click("sidebar_button_start_recording_text", timeout=20)

    def get_stop_and_save_recording_cancel_text(self):
        return self.driver.get_attribute("stop_and_save_recording_cancel_text", "Name", timeout=20)

    def get_stop_and_save_recording_save_as_text(self):
        return self.driver.get_attribute("stop_and_save_recording_save_as_text", "Name", timeout=20)

    def get_stop_and_save_recording_save_text(self):
        return self.driver.get_attribute("stop_and_save_recording_save_text", "Name", timeout=20)

    def get_cancel_recording_text(self):
        self.driver.click("sidebar_button_cancel_recording_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_cancel_recording_text", "Name", timeout=20)

    def get_cancel_recording_pop_up_text(self):
        return self.driver.get_attribute("pop_up_cancel_recording_text", "Name", timeout=20)

    def get_cancel_recording_pop_up_tip_text(self):
        return self.driver.get_attribute("pop_up_cancel_recording_tip_text", "Name", timeout=20)

    def get_go_back_text(self):
        return self.driver.get_attribute("pop_up_cancel_recording_go_back_text", "Name", timeout=20)

    def get_delete_from_pop_up_text(self):
        return self.driver.get_attribute("pop_up_cancel_recording_delete_text", "Name", timeout=20)

    def click_delete_from_pop_up_text(self):
        self.driver.click("pop_up_cancel_recording_delete_text")

    def get_start_livestream_text(self):
        self.driver.click("sidebar_button_start_livestream_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_start_livestream_text", "Name", timeout=20)

    def get_configure_livestream_text(self):
        return self.driver.get_attribute("configure_live_stream_text", "Name", timeout=20)

    def get_connect_a_rtmp_server_text(self):
        return self.driver.get_attribute("connect_a_rtmp_server_text", "Name", timeout=20)

    def get_stream_url_text(self):
        return self.driver.get_attribute("stream_url__text", "Name", timeout=20)

    def get_stream_url_tooltip_text(self):
        self.driver.click("stream_url_tooltip", timeout=20)
        return self.driver.get_attribute("stream_url_tooltip", "Name", timeout=20)

    def get_rtmp_text(self):
        return self.driver.get_attribute("rtmp_text_box", "Name", timeout=20)

    def get_stream_key_text(self):
        return self.driver.get_attribute("stream_key_text", "Name", timeout=20)

    def get_paste_stream_key_text(self):
        return self.driver.get_attribute("paste_stream_key_text_box", "Name", timeout=20)

    def get_start_liveStream_button_text(self):
        return self.driver.get_attribute("start_live_stream_button_text", "Name", timeout=20)

    def get_brb_text(self):
        return self.driver.get_attribute("sidebar_button_be_right_back_text", "Name", timeout=20)

    def click_brb_button(self):
        self.driver.click("sidebar_button_end_be_right_back_text", timeout=20)

    def get_end_brb_text(self):
        # self.driver.click("sidebar_button_be_right_back_text", timeout=20)
        return self.driver.get_attribute("sidebar_button_end_be_right_back_text", "Name", timeout=20)

    def click_end_brb_text(self):
        self.driver.click("sidebar_button_be_right_back_text", timeout=20)

    def get_automatic_keystone_text(self):
        return self.driver.get_attribute("icon_automatic_keystone_text", "Name", timeout=20)

    def click_automatic_keystone_button(self):
        self.driver.click("icon_automatic_keystone_text")

    def get_end_automatic_keystone_text(self):
        # self.driver.click("icon_end_automatic_keystone_text")
        return self.driver.get_attribute("icon_end_automatic_keystone_text", "Name", timeout=20)

    def click_end_automatic_keystone_text(self):
        self.driver.click("icon_end_automatic_keystone_text")

    def get_manual_keystone_text(self):
        return self.driver.get_attribute("icon_manual_keystone_text", "Name", timeout=20)

    def click_manual_keystone_button(self):
        self.driver.click("icon_manual_keystone_text")

    def get_end_manual_keystone_text(self):
        # self.driver.click("icon_end_manual_keystone_text")
        return self.driver.get_attribute("icon_end_manual_keystone_text", "Name", timeout=20)

    def get_accept_text(self):
        return self.driver.get_attribute("manual_keystone_accept_text", "Name", timeout=20)

    def get_cancel_text(self):
        return self.driver.get_attribute("manual_keystone_cancel_text", "Name", timeout=20)

    def click_cancel_text(self):
        self.driver.click("manual_keystone_cancel_text")

    def click_end_manual_keystone_text(self):
        self.driver.click("icon_end_manual_keystone_text")

    def get_rotate_text(self):
        self.driver.click("icon_rotate_text")
        return self.driver.get_attribute("icon_rotate_text", "Name", timeout=20)

    def close_share_as_window_open_window(self):
        self.driver.click("share_as_window_close_window", timeout=20)

    def close_save_as_window(self):
        self.driver.click("save_as_close_window", timeout=20)

    def scroll_down_with_tab(self, element):
        el = self.driver.wait_for_object("scroll_window", displayed=False, timeout=3)
        for i in range(40):
            el.send_keys(Keys.TAB)
            if (self.driver.wait_for_object(element, raise_e=False, timeout=1)):
                break

    def click_video_control(self):
        return self.driver.click("video_control_card")	

    def verify_hpone_page_show(self):
        return self.driver.wait_for_object("hpone_page_title", raise_e=False, timeout=10) is not False

    def click_hpone_page_skip_btn(self):
        self.driver.click("hpone_page_btn")

    def verify_help_icon_show(self):
        return self.driver.wait_for_object("help_icon", raise_e=False, timeout=10) is not False
    
    def click_help_icon(self):
        self.driver.click("help_icon")
    
    def verify_camera_settings_text_show(self):
        return self.driver.wait_for_object("camera_settings_text", raise_e=False, timeout=10) is not False  
    
    def click_camera_settings_text(self):
        self.driver.click("camera_settings_text")

    def verify_layout1_icon_show(self):
        return self.driver.wait_for_object("layout1_icon", raise_e=False, timeout=10) is not False
    
    def click_layout1_icon(self):
        self.driver.click("layout1_icon")
    
    def verify_layout1_icon_status(self): 
        return self.driver.get_attribute("layout1_icon", "Name")
    
    def verify_video_control_card(self):
        return self.driver.wait_for_object("video_control_card", raise_e=False, timeout=30)