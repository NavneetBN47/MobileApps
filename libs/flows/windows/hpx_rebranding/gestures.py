import logging
import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare

class Gestures(HPXRebrandingFlow):
    flow_name = "gestures"

    def verify_gesture_card_title_show(self):
        return self.driver.wait_for_object("gesture_card_title",raise_e=False, timeout = 10)
    
    def verify_gesture_body_container_show(self):
        return self.driver.wait_for_object("gesture_body_container",raise_e=False, timeout = 10)
    
    def verify_pause_resume_img_show(self):
        return self.driver.wait_for_object("pause_resume_img",raise_e=False, timeout = 10)

    def verify_pause_resume_description_container_show(self):
        return self.driver.wait_for_object("pause_resume_description_container",raise_e=False, timeout = 10)
    
    def verify_pause_resume_try_out_button_show(self):
        return self.driver.wait_for_object("pause_resume_try_out_button",raise_e=False, timeout = 10)
    
    def click_pause_resume_try_out_button(self):
        self.driver.click("pause_resume_try_out_button", timeout = 20)

    def verify_pause_resume_toggle_show(self):
        return self.driver.wait_for_object("pause_resume_toggle",raise_e=False, timeout = 10)
    
    def get_pause_resume_toggle_status(self):
        return self.driver.get_attribute("pause_resume_toggle", "Toggle.ToggleState", timeout = 20)
    
    def verify_volume_adjust_img_show(self):
        return self.driver.wait_for_object("volume_adjust_img",raise_e=False, timeout = 10)

    def verify_volume_adjust_description_container_show(self):
        return self.driver.wait_for_object("volume_adjust_description_container",raise_e=False, timeout = 10)
    
    def verify_volume_adjust_try_out_button_show(self):
        return self.driver.wait_for_object("volume_adjust_try_out_button",raise_e=False, timeout = 10)
    
    def click_volume_adjust_try_out_button(self):
        self.driver.click("volume_adjust_try_out_button", timeout = 20)

    def verify_volume_adjust_toggle_show(self):
        return self.driver.wait_for_object("volume_adjust_toggle",raise_e=False, timeout = 10)
    
    def get_volume_adjust_toggle_status(self):
        return self.driver.get_attribute("volume_adjust_toggle", "Toggle.ToggleState")

    def verify_page_scroll_img_show(self):
        return self.driver.wait_for_object("page_scroll_img",raise_e=False, timeout = 10)

    def verify_page_scroll_description_container_show(self):
        return self.driver.wait_for_object("page_scroll_description_container",raise_e=False, timeout = 10)
    
    def verify_page_scroll_try_out_button_show(self):
        return self.driver.wait_for_object("page_scroll_try_out_button",raise_e=False, timeout = 10)
    
    def click_page_scroll_try_out_button(self):
        self.driver.click("page_scroll_try_out_button", timeout = 20)

    def verify_page_scroll_toggle_show(self):
        return self.driver.wait_for_object("page_scroll_toggle",raise_e=False, timeout = 10)
    
    def get_page_scroll_toggle_status(self):
        return self.driver.get_attribute("page_scroll_toggle", "Toggle.ToggleState")
        
    def verify_photo_scroll_img_show(self):
        return self.driver.wait_for_object("photo_scroll_img",raise_e=False, timeout = 10)

    def verify_photo_scroll_description_container_show(self):
        return self.driver.wait_for_object("photo_scroll_description_container",raise_e=False, timeout = 10)
                                           
    def verify_photo_scroll_try_out_button_show(self):
        return self.driver.wait_for_object("photo_scroll_try_out_button",raise_e=False, timeout = 10)

    def click_photo_scroll_try_out_button(self):
        self.driver.click("photo_scroll_try_out_button", timeout = 20)

    def verify_photo_scroll_toggle_show(self):
        return self.driver.wait_for_object("photo_scroll_toggle",raise_e=False, timeout = 10)
    
    def get_photo_scroll_toggle_status(self):
        return self.driver.get_attribute("photo_scroll_toggle", "Toggle.ToggleState")
    
    def verify_feedback_message_show(self):
        return self.driver.wait_for_object("feedback_message",raise_e=False, timeout = 10)
    
    def verify_feedback_message_tips_icon_show(self):
        return self.driver.wait_for_object("feedback_message_tips_icon",raise_e=False, timeout = 10)

    def verify_feedback_message_toggle_show(self):
        return self.driver.wait_for_object("feedback_message_toggle",raise_e=False, timeout = 10)
    
    def get_feedback_message_toggle_status(self):
        return self.driver.get_attribute("feedback_message_toggle", "Toggle.ToggleState")

    def verify_feedback_message_description_show(self):
        return self.driver.wait_for_object("feedback_message_description",raise_e=False, timeout = 10)
    
    def verify_gesture_restore_default_button_show(self):
        return self.driver.wait_for_object("gesture_restore_default_button",raise_e=False, timeout = 10)
    
    def verify_image_overlay_wrapper_show(self):
        return self.driver.wait_for_object("image_overlay_wrapper",raise_e=False, timeout = 10)
    
    def verify_play_pause_text_show(self):
        return self.driver.wait_for_object("play_pause_text",raise_e=False, timeout = 10)
    
    def verify_gesture_modal_description_show(self):
        return self.driver.wait_for_object("gesture_modal_description",raise_e=False, timeout = 10)
    
    def verify_play_pause_first_cancel_button_show(self):
        return self.driver.wait_for_object("play_pause_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_play_pause_first_start_button_show(self):
        return self.driver.wait_for_object("play_pause_first_start_button",raise_e=False, timeout = 10)
    
    def click_play_pause_first_start_button(self):
        self.driver.click("play_pause_first_start_button", timeout = 10)

    def verify_play_pause_second_cancel_button_show(self):
        return self.driver.wait_for_object("play_pause_second_cancel_button",raise_e=False, timeout = 10)

    def verify_play_pause_second_done_button_show(self):
        return self.driver.wait_for_object("play_pause_second_done_button",raise_e=False, timeout = 10)
    
    def click_play_pause_second_done_button(self):
        self.driver.click("play_pause_second_done_button", timeout = 10)

    def verify_volume_adjust_up_first_cancel_button_show(self):
        return self.driver.wait_for_object("volume_adjust_up_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_volume_adjust_up_first_start_button_show(self):
        return self.driver.wait_for_object("volume_adjust_up_first_start_button",raise_e=False, timeout = 10)
    
    def click_volume_adjust_up_first_start_button(self):
        self.driver.click("volume_adjust_up_first_start_button", timeout = 10)

    def verify_volume_adjust_up_second_cancel_button_show(self):
        return self.driver.wait_for_object("volume_adjust_up_second_cancel_button",raise_e=False, timeout = 10)
    
    def verify_volume_adjust_up_second_next_button_show(self):
        return self.driver.wait_for_object("volume_adjust_up_second_next_button",raise_e=False, timeout = 10)

    def click_volume_adjust_up_second_next_button(self):
        self.driver.click("volume_adjust_up_second_next_button", timeout = 10)   

    def verify_volume_adjust_down_first_cancel_button_show(self):
        return self.driver.wait_for_object("volume_adjust_down_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_volume_adjust_down_first_start_button_show(self):
        return self.driver.wait_for_object("volume_adjust_down_first_start_button",raise_e=False, timeout = 10)
    
    def click_volume_adjust_down_first_start_button(self):
        self.driver.click("volume_adjust_down_first_start_button", timeout = 10)

    def verify_volume_adjust_down_second_cancel_button_show(self):
        return self.driver.wait_for_object("volume_adjust_down_second_cancel_button",raise_e=False, timeout = 10)
    
    def verify_volume_adjust_down_second_done_button_show(self):
        return self.driver.wait_for_object("volume_adjust_down_second_done_button",raise_e=False, timeout = 10)
    
    def click_volume_adjust_down_second_done_button(self):
        self.driver.click("volume_adjust_down_second_done_button", timeout = 10)

    def verify_page_scroll_up_first_cancel_button_show(self):
        return self.driver.wait_for_object("page_scroll_up_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_page_scroll_up_first_start_button_show(self):
        return self.driver.wait_for_object("page_scroll_up_first_start_button",raise_e=False, timeout = 10)
    
    def click_page_scroll_up_first_start_button(self):
        self.driver.click("page_scroll_up_first_start_button", timeout = 10)

    def verify_page_scroll_up_second_cancel_button_show(self):
        return self.driver.wait_for_object("page_scroll_up_second_cancel_button",raise_e=False, timeout = 10)

    def verify_page_scroll_up_second_next_button_show(self):
        return self.driver.wait_for_object("page_scroll_up_second_next_button",raise_e=False, timeout = 10)

    def click_page_scroll_up_second_next_button(self):
        self.driver.click("page_scroll_up_second_next_button", timeout = 10)

    def verify_page_scroll_down_first_cancel_button_show(self):
        return self.driver.wait_for_object("page_scroll_down_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_page_scroll_down_first_start_button_show(self):
        return self.driver.wait_for_object("page_scroll_down_first_start_button",raise_e=False, timeout = 10)
    
    def click_page_scroll_down_first_start_button(self):
        self.driver.click("page_scroll_down_first_start_button", timeout = 10)

    def verify_page_scroll_down_second_cancel_button_show(self):
        return self.driver.wait_for_object("page_scroll_down_second_cancel_button",raise_e=False, timeout = 10)
    
    def verify_page_scroll_down_second_done_button_show(self):
        return self.driver.wait_for_object("page_scroll_down_second_done_button",raise_e=False, timeout = 10)
    
    def click_page_scroll_down_second_done_button(self):
        self.driver.click("page_scroll_down_second_done_button", timeout = 10)

    def verify_photo_scroll_previous_first_cancel_button_show(self):
        return self.driver.wait_for_object("photo_scroll_previous_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_photo_scroll_previous_first_start_button_show(self):
        return self.driver.wait_for_object("photo_scroll_previous_first_start_button",raise_e=False, timeout = 10)
    
    def click_photo_scroll_previous_first_start_button(self):
        self.driver.click("photo_scroll_previous_first_start_button", timeout = 10)

    def verify_photo_scroll_previous_second_cancel_button_show(self):
        return self.driver.wait_for_object("photo_scroll_previous_second_cancel_button",raise_e=False, timeout = 10)

    def verify_photo_scroll_previous_second_next_button_show(self):
        return self.driver.wait_for_object("photo_scroll_previous_second_next_button",raise_e=False, timeout = 10)
    
    def click_photo_scroll_previous_second_next_button(self):
        self.driver.click("photo_scroll_previous_second_next_button", timeout = 10)

    def verify_photo_scroll_next_first_cancel_button_show(self):
        return self.driver.wait_for_object("photo_scroll_next_first_cancel_button",raise_e=False, timeout = 10)
    
    def verify_photo_scroll_next_first_start_button_show(self):
        return self.driver.wait_for_object("photo_scroll_next_first_start_button",raise_e=False, timeout = 10)
    
    def click_photo_scroll_next_first_start_button(self):
        self.driver.click("photo_scroll_next_first_start_button", timeout = 10)

    def verify_photo_scroll_next_second_cancel_button_show(self):
        return self.driver.wait_for_object("photo_scroll_next_second_cancel_button",raise_e=False, timeout = 10)
    
    def verify_photo_scroll_next_second_done_button_show(self):
        return self.driver.wait_for_object("photo_scroll_next_second_done_button",raise_e=False, timeout = 10)
    
    def click_photo_scroll_next_second_done_button(self):
        self.driver.click("photo_scroll_next_second_done_button", timeout = 10)

    def click_image_overlay_wrapper(self):
        self.driver.click("image_overlay_wrapper", timeout = 10)

    def click_gesture_modal_description(self):
        self.driver.click("gesture_modal_description", timeout = 10)
    
    def click_pause_resume_toggle(self):
        self.driver.click("pause_resume_toggle", timeout = 10)
    
    def click_volume_adjust_toggle(self):
        self.driver.click("volume_adjust_toggle", timeout = 10)
    
    def click_page_scroll_toggle(self):
        self.driver.click("page_scroll_toggle", timeout = 10)
    
    def click_photo_scroll_toggle(self):
        self.driver.click("photo_scroll_toggle", timeout = 10)
        
    def click_gesture_restore_default_button(self):
        self.driver.click("gesture_restore_default_button", timeout = 10)
    
    def verify_gestures_unavailable_notification_show(self):
        return self.driver.wait_for_object("gestures_unavailable_notification", raise_e=False, timeout = 10)

    def click_play_pause_first_cancel_button(self):
        self.driver.click("play_pause_first_cancel_button", timeout = 5)
    
    def click_volume_adjust_first_cancel_button(self):
        self.driver.click("volume_adjust_up_first_cancel_button", timeout = 5)
    
    def click_page_scroll_first_cancel_button(self):
        self.driver.click("page_scroll_up_first_cancel_button", timeout = 5)
    
    def click_photo_scroll_first_cancel_button(self):
        self.driver.click("photo_scroll_previous_first_cancel_button", timeout = 5)
    
    def click_feedback_message_toggle(self):
        self.driver.click("feedback_message_toggle", timeout = 5)
    
    def get_pause_resume_text(self):
        return self.driver.get_attribute("pause_resume_text","Name", timeout = 10)
    
    def get_volume_adjust_text(self):
        return self.driver.get_attribute("volume_adjust_text","Name", timeout = 10)
    
    def get_page_scroll_text(self):
        return self.driver.get_attribute("page_scroll_text","Name", timeout = 10)
    
    def get_photo_scroll_text(self):
        return self.driver.get_attribute("photo_scroll_text","Name", timeout = 10)

    def click_feedback_message_tips_icon(self):
        self.driver.click("feedback_message_tips_icon", timeout = 5)
        
    def get_feedback_message_tips_text(self):
        return self.driver.get_attribute("feedback_message_tips_icon","Name", timeout = 10)

    def click_pause_resume_img(self):
        self.driver.click("pause_resume_img", timeout = 5)
            
    def click_volume_adjust_img(self):
        self.driver.click("volume_adjust_img", timeout = 5)

    def click_page_scroll_img(self):
        self.driver.click("page_scroll_img", timeout = 5)

    def click_photo_scroll_img(self):
        self.driver.click("photo_scroll_img", timeout = 5)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_gesture_card_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("gesture_card_title",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_pause_resume_description_container_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("pause_resume_description_container",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_volume_adjust_description_container_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("volume_adjust_description_container",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_page_scroll_description_container_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("page_scroll_description_container",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_photo_scroll_description_container_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("photo_scroll_description_container",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_feedback_message_description_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("feedback_message_description",raise_e=False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "color"], pass_ratio=0.02)
    def verify_gesture_card_title_show_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)