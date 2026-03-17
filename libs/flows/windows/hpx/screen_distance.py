from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class ScreenDistance(HPXFlow):
    flow_name = "screen_distance"
    
    def verify_screen_distance_title_show(self):
        return self.driver.wait_for_object("screen_distance_title").get_attribute("Name")
    
    def verify_screen_distance_subtitle_show(self):
        return self.driver.wait_for_object("screen_distance_subtitle").get_attribute("Name")

    def verify_alert_option_title_show(self):
        return self.driver.wait_for_object("alert_option_title").get_attribute("Name")

    def verify_nudge_option_show(self):
        return self.driver.wait_for_object("nudge_option", raise_e=False, timeout=5)

    def verify_alert_option_show(self):
        return self.driver.wait_for_object("alert_option", raise_e=False, timeout=5)

    def verify_blur_option_show(self):
        return self.driver.wait_for_object("blur_option", raise_e=False, timeout=5)
    
    def verify_set_preferred_title_show(self):
        return self.driver.wait_for_object("set_preferred_title").get_attribute("Name")
    
    def verify_set_preferred_subtitle_show(self):
        return self.driver.wait_for_object("set_preferred_subtitle").get_attribute("Name")
    
    def verify_change_button_show(self):
        return self.driver.wait_for_object("change_button").get_attribute("Name")
    
    def verify_restore_button_show(self):
        return self.driver.wait_for_object("restore_button").get_attribute("Name")
    
    def verify_screen_distance_button_show(self):
        return self.driver.wait_for_object("screen_distance_button", raise_e=False, timeout=20)
    
    def click_screen_distance_button(self):
        self.driver.click("screen_distance_button", raise_e=False, timeout=20)
    
    def click_screen_distance_tootlips(self):
        self.driver.click("screen_distance_tooltips", raise_e=False, timeout=20)
    
    def verify_screen_distance_tootlips(self):
        return self.driver.wait_for_object("screen_distance_tooltips").get_attribute("Name")
    
    def verify_screen_distance_button_status(self):
        return self.driver.get_attribute("screen_distance_button", "Toggle.ToggleState", timeout=15)
    
    def click_restore_button(self):
        self.driver.click("restore_button", raise_e=False, timeout=20)

    def get_screen_distance_nav_title(self):
        return self.driver.get_attribute("screen_distance_nav_title", "Name")
    
    def get_toggle_text(self):
        return self.driver.get_attribute("toggle_text", "Name")
    
    def click_change_button(self):
        self.driver.click("change_button", raise_e=False, timeout=20)
    
    def get_cancel_text(self):
        return self.driver.get_attribute("cancel_text", "Name")
    
    def get_save_text(self):
        return self.driver.get_attribute("save_text", "Name")
    
    def get_nudge_text_on_card(self):
        return self.driver.get_attribute("nudge_text_on_card", "Name")
    
    def get_nudge_card_subtitle_text(self):
        return self.driver.get_attribute("nudge_card_subtitle_text", "Name")
    
    def get_alert_text_on_card(self):
        return self.driver.get_attribute("alert_text_on_card", "Name")
    
    def get_alert_card_subtitle_text(self):
        return self.driver.get_attribute("alert_card_subtitle_text", "Name")
    
    def get_blur_text_on_card(self):
        return self.driver.get_attribute("blur_text_on_card", "Name")
    
    def get_blur_card_subtitle_text(self):
        return self.driver.get_attribute("blur_card_subtitle_text", "Name")
    
    def get_current_set_distance(self):
        return self.driver.get_attribute("current_set_distance", "Name")
    
    def verify_nudge_button_show(self):
        return self.driver.wait_for_object("nudge_button", raise_e=False, timeout=5)
    
    def verify_alert_button_show(self):
        return self.driver.wait_for_object("alert_button", raise_e=False, timeout=5)

    def verify_blur_button_show(self):
        return self.driver.wait_for_object("blur_button", raise_e=False, timeout=5)
