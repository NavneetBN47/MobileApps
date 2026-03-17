from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys

class ScreenTime(HPXFlow):
    flow_name = "screen_time"
    
    def verify_screen_time_title_show(self):
        return self.driver.wait_for_object("screen_time_title").get_attribute("Name")
    
    def verify_screen_time_subtitle_show(self):
        return self.driver.wait_for_object("screen_time_subtitle").get_attribute("Name")
    
    def verify_screen_time_tooltips_show(self):
        return self.driver.wait_for_object("screen_time_tooltips").get_attribute("Name")
    
    def verify_active_screen_title_show(self):
        return self.driver.wait_for_object("active_screen_title").get_attribute("Name")
    
    def verify_send_reminder_title_show(self):
        return self.driver.wait_for_object("send_reminder_title").get_attribute("Name")
    
    def verify_send_reminder_tooltips_show(self):
        return self.driver.wait_for_object("send_reminder_tooltips").get_attribute("Name")
    
    def verify_send_reminder_subtitle_show(self):
        return self.driver.wait_for_object("send_reminder_subtitle").get_attribute("Name")
    
    def verify_screen_time_button_show(self):
        return self.driver.wait_for_object("screen_time_button", raise_e=False, timeout=20)
    
    def is_screen_time_toggle_selected(self):
        return self.driver.find_object("screen_time_button").get_attribute("Toggle.ToggleState")
    
    def verify_send_reminder_button_show(self):
        return self.driver.wait_for_object("send_reminder_button", raise_e=False, timeout=20)
    
    def is_send_reminder_toggle_selected(self):
        return self.driver.find_object("send_reminder_button").get_attribute("Toggle.ToggleState")
    
    def verify_reminder_interva_title_show(self):
        return self.driver.wait_for_object("reminder_interval_title").get_attribute("Name")
    
    def click_screen_time_button(self):
        self.driver.click("screen_time_button", raise_e=False, timeout=20)
    
    def click_send_reminder_button(self):
        self.driver.click("send_reminder_button", raise_e=False, timeout=20)
    
    def click_screen_time_tootlips(self):
        self.driver.click("screen_time_tooltips", raise_e=False, timeout=20)
    
    def click_send_reminder_tootlips(self):
        self.driver.click("send_reminder_tooltips", raise_e=False, timeout=20)

    def click_reminder_interval_combobox(self):
        self.driver.click("reminder_interval_combobox", raise_e=False, timeout=20)

    def get_all_time_from_time_list(self):
        return self.driver.wait_for_object("reminder_interval_combobox").get_attribute("Name")

    def open_dropdown_list(self):
        el = self.driver.wait_for_object("reminder_interval_combobox")
        el.send_keys(Keys.ENTER)

    
    def click_4_hours(self):
        el = self.driver.wait_for_object("4_hours")
        self.driver.click("4_hours", raise_e=False, timeout=20)
        el.send_keys(Keys.ENTER)


    def verify_4_hours_selected(self):
        return self.driver.wait_for_object("4_hours").get_attribute("Name")