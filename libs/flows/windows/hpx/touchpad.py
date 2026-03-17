from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class Touchpad(HPXFlow):
    flow_name = "touch_pad"
    
    def get_touchpad_header_text(self):
        return self.driver.wait_for_object("touchpad_header").get_attribute("Name")
    
    def verify_touchpad_card(self):
        return self.driver.wait_for_object("touchpad_card", raise_e=False, timeout=20)

    def verify_touchpad_card_title(self):
        return self.driver.wait_for_object("touchpad_card_title", raise_e=False, timeout=20)
    
    def get_touchpad_card_title_text(self):
        return self.driver.wait_for_object("touchpad_card_title").get_attribute("Name")

    def verify_touchpad_card_discription(self):
        return self.driver.wait_for_object("touchpad_card_discription", raise_e=False, timeout=20)
    
    def get_touchpad_card_discription_text(self):
        return self.driver.wait_for_object("touchpad_card_discription").get_attribute("Name")

    def get_touchpad_title_text(self):
        return self.driver.wait_for_object("touchpad_title").get_attribute("Name")
    
    def get_touchpad_tooltip_text(self):
        return self.driver.wait_for_object("touchpad_tooltip").get_attribute("Name")

    def hover_touchpad_tooltip(self):
        self.driver.hover("touchpad_tooltip", x_offset=24, y_offset=24)
    
    def get_touchpad_brightness_text(self):
        return self.driver.wait_for_object("touchpad_brightness_string").get_attribute("Name")

    def get_touchpad_volume_text(self):
        return self.driver.wait_for_object("touchpad_volume_string").get_attribute("Name")

    def get_touchpad_win_setting_text(self):
        return self.driver.wait_for_object("touchpad_win_setting").get_attribute("Name")

    def get_touchpad_enable_toggle_switch_status(self):
        return self.driver.wait_for_object("touchpad_enable_toggle_switch").get_attribute("Toggle.ToggleState")
    
    def click_touchpad_enable_toggle_switch(self):
        self.driver.click("touchpad_enable_toggle_switch")

    def verify_touchpad_PCDevice_header(self):
        return self.driver.wait_for_object("touchpad_device_page_header", raise_e=False, timeout=20)
    
    def verify_touchpad_PCDevice_header_text(self):
        return self.driver.wait_for_object("touchpad_device_page_header_text", raise_e=False, timeout=20)
    
    def get_touchpad_PCDevice_header_text(self):
        return self.driver.wait_for_object("touchpad_device_page_header_text").get_attribute("Name")    
    
    def click_touchpad_header(self):
        self.driver.click("touchpad_device_page_header")