from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class TouchpadHPOne(HPXFlow):
    flow_name = "TouchpadHPOne"

    def verify_touchpad_icon_show(self):
        return self.driver.wait_for_object("touchpad_icon")
    
    def click_touchpad_iocn(self):
        self.driver.click("touchpad_icon")

    def verify_enable_gesture_control_text_show(self):
        return self.driver.wait_for_object("enable_gesture_control_text")
    
    def verify_enable_gesture_control_tipsicon_show(self): 
        return self.driver.wait_for_object("enable_gesture_control_tipsicon")

    def verify_enable_gesture_control_toggle_show(self): 
        return self.driver.wait_for_object("enable_gesture_control_toggle") 

    def get_default_enable_gesture_control_toggle_state(self):
       return self.driver.get_attribute("enable_gesture_control_toggle","Toggle.ToggleState")
        
    def verify_brightness_text_show(self):
        return self.driver.wait_for_object("brightness_text")
    
    def verify_volume_text_show(self):
        return self.driver.wait_for_object("volume_text")
    
    def verify_SVG_image_show(self):
        return self.driver.wait_for_object("SVG_image")
    
    def verify_adjust_feedback_intensity_link_button_show(self):
        return self.driver.wait_for_object("adjust_feedback_intensity_link_button")
    
    def click_enable_gesture_control_toggle(self):
        self.driver.click("enable_gesture_control_toggle")
    
    def get_default_enable_gesture_control_toggle_state(self):
        return self.driver.get_attribute("enable_gesture_control_toggle","Toggle.ToggleState")  
    
    def click_adjust_feedback_intensity_link_button(self):
        self.driver.click("adjust_feedback_intensity_link_button")

    def verify_os_touchpad_setting_page_show_and_touchpad_toggle_is_on(self):
        return self.driver.wait_for_object("os_touchpad_setting_page_show_and_touchpad_toggle_is_on")
    
    def verify_os_setting_page_touchpad_feedback_toggle_is_on(self):
        return self.driver.wait_for_object("os_touchpad_setting_page_show_and_touchpad_feedback_toggle_is_on")
    
    def close_OS_touchpad_setting_page(self):
        self.driver.click("os_touchpad_setting_page")