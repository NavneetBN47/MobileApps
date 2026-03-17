from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction


class Mcafee(HPXFlow):
    flow_name = "mcafee"

    def verify_mcafee_header_show(self):
        return self.driver.wait_for_object("mcafee_sub_title", raise_e=False, timeout=20) is not False

    def enter_email(self, text):
        self.driver.wait_for_object("sign_in_email", timeout=30)
        self.driver.send_keys("sign_in_email", text)
    
    def get_invalid_data_message(self):
        return self.driver.get_attribute("email_errorMessage", "Name")

    def verify_skip_button_show(self):
        return self.driver.wait_for_object("skip_button", raise_e=False, timeout=10)

    def click_skip_button(self):
        return self.driver.click("skip_button")
    
    def complete_register(self, email):
        self.driver.wait_for_object("sign_in_email", timeout=10)
        self.driver.send_keys("sign_in_email", email)
        self.driver.click("next_button")
    
    def verify_register_success(self):
        return self.driver.wait_for_object("success_message", raise_e=False, timeout=10) is not False 

    def verify_next_btn_is_disabled(self):
        assert self.driver.get_attribute("next_button", attribute="IsEnabled").lower() == "false"

    def verify_next_btn_is_enabled(self):
        assert self.driver.get_attribute("next_button", attribute="IsEnabled").lower() == "true"
        