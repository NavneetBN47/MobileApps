from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class VisionAI(HPXFlow):
    flow_name = "vision_ai"

    def verify_let_myhp_access_your_camear_dialog_show(self):
        return self.driver.wait_for_object("let_myHP_access_your_camera", raise_e=False, timeout=7) is not False

    def click_yes_button_on_let_myhp_access_dialog(self):
        self.driver.click("yes_button_in_let_access_dialog")

    def verify_camera_and_presence_detection_action_item_show(self):
        return self.driver.wait_for_object("camera_and_presence_detection_action_item", raise_e=False, timeout=10) is not False
    
    def verify_on_looker_detection_show(self):
        return self.driver.wait_for_object("onlooker_detection_text", raise_e=False, timeout=10) is not False
    
    def verify_on_looker_detection_button_state(self):
        return self.driver.get_attribute("onlooker_detection_button", "Toggle.ToggleState")
    
    def verify_enable_sureview_button_state(self):
        return self.driver.get_attribute("enable_sureview_button", "Toggle.ToggleState")

    def verify_auto_hdr_text_show(self):
        return self.driver.wait_for_object("auto_hdr_text", raise_e=False, timeout=10) is not False
    
    def get_auto_hdr_text(self):
        return self.driver.get_attribute("auto_hdr_text", "Name")
    
    def verify_auto_hdr_toggle_show(self):
        return self.driver.wait_for_object("auto_hdr_toggle", raise_e=False, timeout=10) is not False
    
    def get_auto_hdr_toggle_default_status(self):
        return self.driver.get_attribute("auto_hdr_toggle", "Toggle.ToggleState")
    
    def verify_auto_hdr_description_text_show(self):
        return self.driver.wait_for_object("auto_hdr_description_text", raise_e=False, timeout=10) is not False
    
    def get_auto_hdr_description_text(self):
        return self.driver.get_attribute("auto_hdr_description_text", "Name")
    
    def verify_auto_hdr_image_show(self):
        return self.driver.wait_for_object("auto_hdr_image", raise_e=False, timeout=10) is not False
    
    def get_on_looker_detection_text(self):
        return self.driver.get_attribute("onlooker_detection_text", "Name")

    def verify_on_looker_detection_button_show(self):
        return self.driver.wait_for_object("onlooker_detection_button", raise_e=False, timeout=10) is not False
    
    def get_on_looker_detection_button_state(self):
        return self.driver.get_attribute("onlooker_detection_button", "Toggle.ToggleState")

    def verify_on_looker_detection_description_text_show(self):
        return self.driver.wait_for_object("onlooker_detection_description_text", raise_e=False, timeout=10) is not False
    
    def get_on_looker_detection_description_text(self):
        return self.driver.get_attribute("onlooker_detection_description_text", "Name")
    
    def verify_enable_sureview_text_show(self):
        return self.driver.wait_for_object("enable_sureview_text", raise_e=False, timeout=10) is not False

    def verify_enable_sureview_tips_icon_show(self):
        return self.driver.wait_for_object("enable_sureview_tips_icon", raise_e=False, timeout=10) is not False
    
    def verify_enable_sureview_button_show(self):
        return self.driver.wait_for_object("enable_sureview_button", raise_e=False, timeout=10) is not False

    def get_enable_sureview_button_state(self):
        return self.driver.get_attribute("enable_sureview_button", "Toggle.ToggleState")
    
    def click_camera_and_presence_detection_action_item(self):
        self.driver.click("camera_and_presence_detection_action_item")

    def verify_restore_default_button_show(self):
        return self.driver.wait_for_object("restore_default_button", raise_e=False, timeout=10) is not False
    
    def click_restore_default_button(self):
        self.driver.click("restore_default_button")

    def verify_intelligent_dynamic_contrast_text_show(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_text", raise_e=False, timeout=10) is not False

    def get_intelligent_dynamic_contrast_text(self):
        return self.driver.get_attribute("intelligent_dynamic_contrast_text", "Name")
    
    def verify_intelligent_dynamic_contrast_toggle_show(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_toggle", raise_e=False, timeout=10) is not False
    
    def get_intelligent_dynamic_contrast_toggle_default_status(self):
        return self.driver.get_attribute("intelligent_dynamic_contrast_toggle", "Toggle.ToggleState")
    
    def verify_intelligent_dynamic_contrast_description_text_show(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_description_text", raise_e=False, timeout=10) is not False
    
    def get_intelligent_dynamic_contrast_description_text(self):
        return self.driver.get_attribute("intelligent_dynamic_contrast_description_text", "Name")
    
    def verify_intelligent_dynamic_contrast_image_show(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_image", raise_e=False, timeout=10) is not False
    
    def verify_attention_focus_text_show(self):
        return self.driver.wait_for_object("attention_focus_text", raise_e=False, timeout=10) is not False
    
    def get_attention_focus_text(self):
        return self.driver.get_attribute("attention_focus_text", "Name")

    def verify_attention_focus_toggle_show(self):
        return self.driver.wait_for_object("attention_focus_toggle", raise_e=False, timeout=10) is not False
    
    def get_attention_focus_toggle_default_status(self):
        return self.driver.get_attribute("attention_focus_toggle", "Toggle.ToggleState")
    
    def verify_attention_focus_description_text_show(self):
        return self.driver.wait_for_object("attention_focus_description_text", raise_e=False, timeout=10) is not False
    
    def get_attention_focus_description_text(self):
        return self.driver.get_attribute("attention_focus_description_text", "Name")
    
    def verify_attention_focus_image_show(self):
        return self.driver.wait_for_object("attention_focus_image", raise_e=False, timeout=10) is not False

    def verify_on_looker_detection_image_show(self):
        return self.driver.wait_for_object("onlooker_detection_image", raise_e=False, timeout=10) is not False

    def verify_enable_screen_blur_text_show(self):
        return self.driver.wait_for_object("enable_screen_blur_text", raise_e=False, timeout=10) is not False
    
    def verify_enable_screen_blur_tips_icon_show(self):
        return self.driver.wait_for_object("enable_screen_blur_tips_icon", raise_e=False, timeout=10) is not False
    
    def verify_enable_screen_blur_button_show(self):
        return self.driver.wait_for_object("enable_screen_blur_button", raise_e=False, timeout=10) is not False
    
    def get_enable_screen_blur_button_state(self):
        return self.driver.get_attribute("enable_screen_blur_button", "Toggle.ToggleState")
    
    def click_enable_sureview_button(self):
        self.driver.click("enable_sureview_button")

    def click_enable_screen_blur_button(self):
        self.driver.click("enable_screen_blur_button")

    def verify_presence_detection_title(self):
        return self.driver.get_attribute("presence_detection_title", "Name", timeout = 10)

    def click_auto_hdr_toggle_button(self):
        self.driver.click("auto_hdr_toggle")

    def get_toggle_windows_hdr_state(self):
        return self.driver.get_attribute("windows_hdr_toggle","Toggle.ToggleState")

    def click_onlooker_detection_button(self):
        self.driver.click("onlooker_detection_button")

    def verify_on_looker_detection_button_state(self):
        return self.driver.get_attribute("onlooker_detection_button", "Toggle.ToggleState")
    
    def get_top_title_text(self):
        return self.driver.get_attribute("top_title", "Name", timeout = 10)

    def get_enable_screen_blur_text(self):
        return self.driver.get_attribute("enable_screen_blur_text", "Name")
    
    def get_enable_screen_blur_tooltips(self):
        return self.driver.get_attribute("enable_screen_blur_tips_icon", "Name")

    def get_restore_default_button_text(self):
        return self.driver.get_attribute("restore_default_button", "Name")

    def click_attention_focus_toggle_button(self):
        self.driver.click("attention_focus_toggle")    
    
    def verify_yes_button_show(self):
        return self.driver.wait_for_object("yes_button_in_let_access_dialog", raise_e=False, timeout=7) is not False