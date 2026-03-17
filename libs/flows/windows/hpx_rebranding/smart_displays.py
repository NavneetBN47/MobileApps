import logging
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time

class SmartDisplays(HPXRebrandingFlow):
    flow_name = "smart_displays"

    def verify_screen_shift_button_status(self):
        return self.driver.get_attribute("screen_shift_button", "Toggle.ToggleState", raise_e=False, timeout=10)

    def click_screen_shift_button(self):
        self.driver.click("screen_shift_button")
    
    def click_screen_shift_restore_button(self):
        self.driver.click("screen_shift_restore_button")

    def verify_feature_notice_show(self):
        return self.driver.wait_for_object("feature_notice", raise_e=False, timeout = 10)
    
    def verify_banner_image_show(self):
        return self.driver.wait_for_object("banner_image", raise_e=False, timeout = 10)
    
    def get_screen_shift_description_text(self):
        return self.driver.get_attribute("screen_shift_desc", "Name")

    def verify_restore_default_button_show(self):
        return self.driver.wait_for_object("screen_shift_restore_button", raise_e=False, timeout=10)
    
    def verify_feature_notice_commercial_show(self):
        return self.driver.wait_for_object("feature_notice_commercial", raise_e=False, timeout = 10)
    
    def verify_look_to_move_toggle_show(self):
        if self.driver.wait_for_object("look_to_move_toggle_on", raise_e=False, timeout = 10):
            return True
        elif self.driver.wait_for_object("look_to_move_toggle_off", raise_e=False, timeout = 10):
            return True
        else:
            return False
    
    def verify_look_to_control_toggle_show(self):
        if self.driver.wait_for_object("look_to_control_toggle_on", raise_e=False, timeout = 10):
            return True
        elif self.driver.wait_for_object("look_to_control_toggle_off", raise_e=False, timeout = 10):
            return True
        else:
            return False
        
    def verfy_restore_default_button_commercial_show(self):
        return self.driver.wait_for_object("restore_default_button_commercial", raise_e=False, timeout=10)
    
    def verify_look_to_move_button_status(self):
        if self.driver.wait_for_object("look_to_move_toggle_off", raise_e=False, timeout = 5):
            return self.driver.get_attribute("look_to_move_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)
        else:
            return self.driver.get_attribute("look_to_move_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_look_to_control_button_status(self):
        if self.driver.wait_for_object("look_to_control_toggle_off", raise_e=False, timeout = 5):
            return self.driver.get_attribute("look_to_control_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)
        else:
            return self.driver.get_attribute("look_to_control_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def turn_on_look_to_move_toggle(self):
        if self.verify_look_to_move_button_status() == "0":
            self.driver.click("look_to_move_toggle_off")
        else:
            self.driver.click("look_to_move_toggle_on")
            time.sleep(2)
            self.driver.click("look_to_move_toggle_off")
            
    def turn_off_look_to_move_toggle(self):
        if self.verify_look_to_move_button_status() == "0":
            self.driver.click("look_to_move_toggle_off")
            time.sleep(2)
            self.driver.click("look_to_move_toggle_on")
        else:
            self.driver.click("look_to_move_toggle_off")
    
    def turn_on_look_to_control_toggle(self):
        if self.verify_look_to_control_button_status() == "0":
            self.driver.click("look_to_control_toggle_off")
        else:
            self.driver.click("look_to_control_toggle_on")
            time.sleep(2)
            self.driver.click("look_to_control_toggle_off")
    
    def turn_off_look_to_control_toggle(self):
        if self.verify_look_to_control_button_status() == "0":
            self.driver.click("look_to_control_toggle_off")
            time.sleep(2)
            self.driver.click("look_to_control_toggle_on")
        else:
            self.driver.click("look_to_control_toggle_off")
    
    def click_restore_default_button_commercial(self):
        self.driver.click("restore_default_button_commercial")
    
    def get_error_handling_message(self):
        return self.driver.get_attribute("feature_notice_description", "Name", raise_e=False, timeout=10)
