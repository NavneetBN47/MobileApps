from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.keys import Keys

class RGBKeyboard(HPXFlow):

    flow_name = "rgb_keyboard"
    
    def get_rgb_keyboard_text(self):
        return self.driver.wait_for_object("RGB_keyboard_header").get_attribute("Name")
    
    def get_enable_rgb_lighting_text(self):
        return self.driver.wait_for_object("enable_RGB_lighting").get_attribute("Name")
    
    def get_static_text(self):
        return self.driver.wait_for_object("static").get_attribute("Name")
    
    def get_wave_text(self):
        return self.driver.wait_for_object("wave").get_attribute("Name")
    
    def get_ripple_text(self):
        return self.driver.wait_for_object("ripple").get_attribute("Name")
    
    def get_breathing_text(self):
        return self.driver.wait_for_object("breathing").get_attribute("Name")
    
    def get_raindrops_text(self):
        return self.driver.wait_for_object("raindrops").get_attribute("Name")
    
    def get_colorcycle_text(self):
        return self.driver.wait_for_object("colorcycle").get_attribute("Name")

    def verify_rgb_keyboard(self):
        return self.driver.get_attribute("RGB_keyboard_id","Name")

    def click_rgb_keyboard(self):
        self.driver.click("RGB_keyboard_id")

    def click_static_button(self):
        self.driver.click("static")

    def click_wave_button(self):
        self.driver.click("wave")

    def click_ripple_button(self):
        self.driver.click("ripple")

    def click_breathing_button(self):
        self.driver.click("breathing")

    def click_raindrops_button(self):
        self.driver.click("raindrops")

    def click_color_cycle_button(self):
        self.driver.click("colorcycle")

    def click_restore_default_button(self):
        self.driver.click("restore_default_tab")

    def click_RGB_lighting_toggle_button(self):
        self.driver.click("enable_RGB_lighting_toggle")

    def get_RGB_lighting_toggle_button_state(self):
        return self.driver.get_attribute("enable_RGB_lighting_toggle","Toggle.ToggleState")

    def is_enable_restore_default_tab(self):
        return self.driver.is_enable("restore_default_tab")

    def get_slider_value(self):
        return self.driver.get_attribute("brightness_slider", "RangeValue.Value")
    
    def set_slider_value_increase(self,value):
        slider = self.driver.wait_for_object("brightness_slider")
        for _ in range(value):
            slider.send_keys(Keys.RIGHT)

    def set_slider_value_decrease(self,value):
        slider = self.driver.wait_for_object("brightness_slider")
        for _ in range(value):
            slider.send_keys(Keys.LEFT)
    
    def get_brightness_level(self):
        result = self.driver.ssh.send_command('powershell "Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness"')
        return result["stdout"]

    def click_restore_default_tab(self):
        self.driver.click("restore_default_tab")

    def get_restore_button_text(self):
        return self.driver.wait_for_object("restore_default_tab").get_attribute("Name")
    
    def verify_rgb_header(self):
        return self.driver.wait_for_object("RGB_keyboard_header",raise_e=False, timeout=2) 
    
    def click_red_button(self):
        self.driver.click("red_button")

    def click_yellow_button(self):
        self.driver.click("yellow_button")

    def click_green_button(self):
        self.driver.click("green_button")

    def click_cyan_button(self):
        self.driver.click("cyan_button")

    def click_blue_button(self):
        self.driver.click("blue_button")

    def click_purple_button(self):
        self.driver.click("purple_button")

    def click_white_button(self):
        self.driver.click("white_button")        