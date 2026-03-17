from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time
from selenium.webdriver.common.keys import Keys

class Mouse(HPXFlow):
    flow_name = "external_mouse"

    def get_title_text(self):
        return self.driver.wait_for_object("mouse_title").get_attribute("Name")
    
    def click_title(self):
        self.driver.click("mouse_title")
    
    def get_title_tooltips_text(self):
        return self.driver.wait_for_object("mouse_title_tootlips").get_attribute("Name")
    
    def get_middle_click_text(self):
        return self.driver.wait_for_object("mouse_title").get_attribute("Name")
    
    def get_scroll_left_text(self):
        return self.driver.wait_for_object("scroll_left").get_attribute("Name")
    
    def get_right_click_text(self):
        return self.driver.wait_for_object("right_click").get_attribute("Name")
    
    def get_scroll_right_text(self):
        return self.driver.wait_for_object("scroll_right").get_attribute("Name")
    
    def get_forward_text(self):
        return self.driver.wait_for_object("forward").get_attribute("Name")
    
    def get_task_view_text(self):
        return self.driver.wait_for_object("task_view").get_attribute("Name")

    def get_back_text(self):
        return self.driver.wait_for_object("back").get_attribute("Name")
    
    def get_mouse_sensitivity_text(self):
        return self.driver.wait_for_object("mouse_sensitivity").get_attribute("Name")
    
    def get_restore_button_text(self):
        return self.driver.wait_for_object("restore_button").get_attribute("Name")
    
    def click_restore_button(self):
        self.driver.click("restore_button")
    
    def verify_mouse_module_show(self):
        return self.driver.wait_for_object("mouse_title", raise_e=False, timeout=10) is not False
    
    def click_eidt_name_btn(self):
        self.driver.click("edit_name_button")
    
    def click_device_info_icon(self):
        self.driver.click("mosue_info_icon")
    
    def enter_device_name(self, text):
        self.driver.wait_for_object("device_name_input", timeout=10)
        self.driver.send_keys("device_name_input", text)
        el = self.driver.wait_for_object("device_name_input", displayed=False, timeout=3)
        time.sleep(3)
        el.send_keys(Keys.ENTER)
    
    def get_product_numer_title(self):
        return self.driver.wait_for_object("product_number_text").get_attribute("Name")
    
    def get_serial_number_title(self):
        return self.driver.wait_for_object("serial_number_text").get_attribute("Name")
    
    def get_firmware_version_title(self):
        return self.driver.wait_for_object("firmware_version_text").get_attribute("Name")
    
    def verify_connect_status_icon_show(self):
        return self.driver.wait_for_object("mosue_connect_status", raise_e=False, timeout=10) is not False
    
    def click_sensitivity_button(self):
        self.driver.click("mouse_sensitivity_button")
    
    def get_sensitivity_slider_value(self):
        return self.driver.wait_for_object("mouse_sensitivity_slider").get_attribute("LegacyIAccessible.Name")
    
    def set_sensitivity_slider_value_increase(self,value, slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.UP)
    
    def set_sensitivity_slider_value_decrease(self,value, slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.DOWN)
