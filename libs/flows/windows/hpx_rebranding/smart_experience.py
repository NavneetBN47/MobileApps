from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare
class SmartExperience(HPXRebrandingFlow):
    flow_name = "smart_experience"

    def verify_camera_and_presence_detection_header_masadan_ltwo_page(self):
        return self.driver.wait_for_object("camera_and_presence_detection_key_header_masadan_ltwo_page", timeout = 20)
    
    def verify_camera_and_presence_detection_header_ultron_ltwo_page(self):
        return self.driver.wait_for_object("presence_detection_key_header_ultron_ltwo_page", timeout = 20)

    def get_camera_and_presence_detection_header_masadan_ltwo_page(self):
        return self.driver.get_attribute("camera_and_presence_detection_key_header_masadan_ltwo_page", "Name", timeout = 20)
    
    def get_camera_and_presence_detection_header_ultron_ltwo_page(self):
        return self.driver.get_attribute("presence_detection_key_header_ultron_ltwo_page","Name", timeout = 20)
    
    def verify_auto_hdr_text_ltwo_page(self):
        return self.driver.wait_for_object("auto_hdr_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_auto_hdr_description_ltwo_page(self):
        return self.driver.wait_for_object("auto_hdr_description_two_page", raise_e=False, timeout=15)
    
    def get_auto_hdr_toggle_button_state(self):
        return self.driver.get_attribute("auto_hdr_toggle_button_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_auto_hdr_toggle_button(self):
        self.driver.click("auto_hdr_toggle_button_ltwo_page", timeout = 10)
    
    def verify_intelligent_dynamic_contrast_text_ltwo_page(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_intelligent_dynamic_contrast_description_ltwo_page(self):
        return self.driver.wait_for_object("intelligent_dynamic_contrast_description_ltwo_page", raise_e=False, timeout=15)
    
    def get_intelligent_dynamic_contrast_toggle_button_state(self):
        return self.driver.get_attribute("intelligent_dynamic_contrast_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_intelligent_dynamic_contrast_toggle_button(self):
        self.driver.click("intelligent_dynamic_contrast_toggle_switch_ltwo_page", timeout = 10)

    def verify_attention_focus_text_ltwo_page(self):
        return self.driver.wait_for_object("attention_focus_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_attention_focus_description_ltwo_page(self):
        return self.driver.wait_for_object("attention_focus_description_ltwo_page", raise_e=False, timeout=15)
    
    def get_attention_focus_toggle_button_state(self):
        return self.driver.get_attribute("attention_focus_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_attention_focus_toggle_button_toggle_button_state(self):
        self.driver.click("attention_focus_toggle_switch_ltwo_page", timeout = 10)

    def verify_onlooker_detection_text_ltwo_page(self):
        return self.driver.wait_for_object("onlooker_detection_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_onlooker_detection_description_ltwo_page(self):
        return self.driver.wait_for_object("onlooker_detection_description_ltwo_page", raise_e=False, timeout=15)
    
    def get_onlooker_detection_toggle_button_state(self):
        return self.driver.get_attribute("onlooker_detection_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_onlooker_detection_toggle_button(self):
        self.driver.click("onlooker_detection_toggle_switch_ltwo_page", timeout = 10)

    def verify_enable_screen_blur_ltwo_page(self):
        return self.driver.wait_for_object("enable_screen_blur_card_ltwo_page", raise_e=False, timeout=15)    

    def click_enable_screen_blur_tooltip(self):
        self.driver.click("enable_screen_blur_info_tooltip_ltwo_page", timeout = 10)

    def get_enable_screen_blur_toggle_button_state(self):
        return self.driver.get_attribute("enable_screen_blur_info_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_enable_screen_blur_toggle_button(self):
        self.driver.click("enable_screen_blur_info_toggle_switch_ltwo_page", timeout = 10)    

    def verify_restore_default_button_ltwo_page(self):
        return self.driver.wait_for_object("restore_default_ltwo_page", raise_e=False, timeout=15)    

    def click_restore_default_button_ltwo_page(self):
        self.driver.click("restore_default_ltwo_page", timeout = 10)

    def verify_auto_screen_dimming_ultron_text_ltwo_page(self):
        return self.driver.wait_for_object("auto_screen_dimming_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_auto_screen_dimming_description_ultron_ltwo_page(self):
        return self.driver.wait_for_object("auto_screen_dimming_description_two_page", raise_e=False, timeout=15)
    
    def get_auto_screen_dimming_toggle_button_state_ultron(self):
        return self.driver.get_attribute("auto_screen_dimming_toggle_button_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_auto_screen_dimming_toggle_button_ultron(self):
        self.driver.click("auto_screen_dimming_toggle_button_ltwo_page", timeout = 10)

    def verify_pivacy_alert_text_ultron_ltwo_page(self):
        return self.driver.wait_for_object("privacy_alert_text_ltwo_page", raise_e=False, timeout=15)
    
    def verify_pivacy_alert_description_ultron_ltwo_page(self):
        return self.driver.wait_for_object("privacy_alert_description_two_page", raise_e=False, timeout=15)
    
    def get_pivacy_alert_toggle_button_state_ultron(self):
        return self.driver.get_attribute("privacy_alert_toggle_button_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_pivacy_alert_toggle_button_ultron(self):
        self.driver.click("privacy_alert_toggle_button_ltwo_page", timeout = 10)

    def verify_enable_sure_view_ltwo_page(self):
        return self.driver.wait_for_object("enable_sureview_card_ltwo_page", raise_e=False, timeout=15)    

    def click_enable_sure_view_tooltip(self):
        self.driver.click("enable_sure_view_tooltip_ltwo_page", timeout = 10)

    def get_enable_sure_view_toggle_button_state(self):
        return self.driver.get_attribute("enable_sureview_info_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def click_enable_sure_view_toggle_button(self):
        self.driver.click("enable_sureview_info_toggle_switch_ltwo_page", timeout = 10)   
    
    def verify_privacy_alert_toggle_button_ltwo_page(self):
        return self.driver.get_attribute("privacy_alert_toggle_button_ltwo_page", "Name", raise_e=False, timeout=10)

    def verify_auto_screen_dimming_toggle_button_ltwo_page(self):
        return self.driver.get_attribute("auto_screen_dimming_toggle_button_ltwo_page", "Name", raise_e=False, timeout=10)
    
    def get_auto_screen_dimming_description_two_page(self):
        return self.driver.get_attribute("auto_screen_dimming_description_two_page", "Name", raise_e=False, timeout=10)
    
    def get_privacy_alert_description_two_page(self):
        return self.driver.get_attribute("privacy_alert_description_two_page", "Name", raise_e=False, timeout=10)

    def get_auto_hdr_description_two_page(self):
        return self.driver.get_attribute("auto_hdr_description_two_page", "Name", raise_e=False, timeout=10)
    
    def get_sure_view_toggle_ltwo_page(self):
        return self.driver.get_attribute("enable_sureview_info_toggle_switch_ltwo_page", "Toggle.ToggleState",  timeout = 20)
    
    def get_presence_detection_contextual_text(self):
        return self.driver.get_attribute("contextual_text_presence_detection_lone_page", "Name", timeout = 20)
    
    def get_sure_view_tooltip_description_text(self):
        return self.driver.get_attribute("sure_view_tooltip_description_ltwo_page", "Name",  timeout = 20)
    
    def click_sure_view_tooltip(self):
        self.driver.click("sure_view_tooltip_description_ltwo_page", timeout = 10)

    @screenshot_compare(root_obj="presence_detection_module_image",include_param=["machine_type"],pass_ratio=0.01)
    def verify_presence_detection_image(self,machine_type,raise_e=True):
        return self.driver.wait_for_object("restore_default_ltwo_page", raise_e=raise_e, timeout=10)

    @screenshot_compare(root_obj="presence_detection_module_image", pass_ratio=0.01)
    def verify_color_filter(self):
        return self.driver.wait_for_object("camera_and_presence_detection_key_header_masadan_ltwo_page", raise_e=False, timeout=10)

    @screenshot_compare(root_obj="presence_detection_module_image",include_param=["machine_type","mode"], pass_ratio=0.01)
    def verify_dark_mode(self,machine_type,mode):
        return self.driver.wait_for_object("camera_and_presence_detection_key_header_masadan_ltwo_page", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_type", "percent"], pass_ratio=0.01)
    def verify_magnifier(self, machine_type, percent):
        return self.driver.wait_for_object("camera_and_presence_detection_key_header_masadan_ltwo_page", raise_e=False, timeout=10)
    
    def click_presence_detection_card(self):
        self.driver.click("presence_detection_card_lone_page", timeout = 10)
