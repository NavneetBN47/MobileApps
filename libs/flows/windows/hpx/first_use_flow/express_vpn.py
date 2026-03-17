from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction


class ExpressVPN(HPXFlow):
    flow_name = "express_vpn"

    def verify_express_vpn_header_show(self):
        return self.driver.wait_for_object("express_vpn_header", raise_e=False, timeout=20) is not False

    def enter_email(self, text):
        self.driver.wait_for_object("express_vpn_email", timeout=30)
        self.driver.send_keys("express_vpn_email", text)
    
    def get_invalid_data_message(self):
        return self.driver.get_attribute("signup_error_message", "Name")

    def verify_skip_button_show(self):
        return self.driver.wait_for_object("vpn_skip_button", raise_e=False, timeout=10) is not False

    def click_skip_button(self):
        self.driver.click("vpn_skip_button")