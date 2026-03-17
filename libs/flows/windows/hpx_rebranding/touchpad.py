import logging
import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys
from SAF.decorator.saf_decorator import screenshot_compare


class Touchpad(HPXRebrandingFlow):
    flow_name = "touchpad"

    def verify_touchpad_title_show(self):
        return self.driver.wait_for_object("touchpad_title", raise_e=False, timeout=20)
    
    def verify_enable_gesture_control_button_state(self):
        return self.driver.get_attribute("enable_gesture_button", "Toggle.ToggleState")
    
    def click_enable_gesture_control_button(self):
        self.driver.click("enable_gesture_button", timeout=10)

    def verify_enable_gesture_control_text_show(self):
        return self.driver.wait_for_object("enable_gesture_text", raise_e=False, timeout=10)

    def verify_adjust_feedback_intensity_link_show(self):
        return self.driver.wait_for_object("adjust_feedback_intensity_link", raise_e=False, timeout=10)
    
    def verify_restore_default_button_show(self):
        return self.driver.wait_for_object("restore_default_button", raise_e=False, timeout=10)
    
    def click_restore_default_button(self):
        self.driver.click("restore_default_button", timeout=10)
    
    def click_adjust_feedback_intensity_link(self):
        self.driver.click("adjust_feedback_intensity_link", timeout=10)
    
    def click_windows_setting_feedback(self):
        self.driver.click("windows_setting_feedback", timeout=10)
    
    def get_windows_intensity_slider_value(self):
        return self.driver.get_attribute("windows_intensity_slider", "Value.Value",  timeout = 10)
    
    def set_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name, raise_e=False, timeout=10)
        for _ in range(value):
            time.sleep(2)
            slider.send_keys(Keys.RIGHT)

    def set_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name, raise_e=False, timeout=10)
        for _ in range(value):
            time.sleep(2)  
            slider.send_keys(Keys.LEFT)
    
    def click_windows_touchpad_togggle(self):
        self.driver.click("windows_touchpad_toggle", timeout=10)
    
    def verify_enable_touchpad_message_show(self):
        return self.driver.wait_for_object("enable_touchpad_message", raise_e=False, timeout=10)

    def click_return_button_on_top_left_corner(self):
        self.driver.click("return_button", timeout=10)

    def get_contextual_config_touchpad_card_text(self):
        return self.driver.get_attribute("contextual_config_touchpad_card", "Name", timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_touchpad_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("touchpad_title", raise_e=False, timeout=20)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_enable_gesture_control_text_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("enable_gesture_text", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_adjust_feedback_intensity_link_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("adjust_feedback_intensity_link", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["mode"], pass_ratio=0.02)
    def verify_touchpad_title_show_mode(self, mode):
        return self.driver.wait_for_object("touchpad_title", raise_e = False, timeout = 10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "color"], pass_ratio=0.02)
    def verify_touchpad_title_show_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)