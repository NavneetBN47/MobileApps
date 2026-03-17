from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction


class Dropbox(HPXFlow):
    flow_name = "dropbox"

    def check_sub_title_text(self):
        return self.driver.get_attribute("dropbox_sub_title", "Name")
        

    def verify_dropbox_header_show(self):
        return self.driver.wait_for_object("dropbox_sub_title", raise_e=False, timeout=10) is not False

    def click_skip_button(self):
        self.driver.click("skip_button")
    
    def enter_sign_in_email(self, text):
        self.driver.wait_for_object("sign_in_email", timeout=30)
        self.driver.send_keys("sign_in_email", text)

    def enter_sign_in_passwd(self, text):
        self.driver.wait_for_object("sign_in_password", timeout=30)
        self.driver.send_keys("sign_in_password", text)

    def click_sign_in_button(self):
        self.driver.click("sign_in_button")
    
    def get_sign_in_email_error_message(self):
        return self.driver.get_attribute("signin_email_errorMessage", "Name")
    
    def navigate_to_sign_up_page(self):
        el = self.driver.find_object("create_one_link")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.96, height * 0.5)

    
    def verify_sign_up_header_show(self):
        return self.driver.wait_for_object("signup_header", raise_e=False, timeout=10) is not False

    
    def enter_sign_up_first_name(self, text):
        self.driver.wait_for_object("sign_up_firstname", timeout=30)
        self.driver.send_keys("sign_up_firstname", text)
    
    def enter_sign_up_last_name(self, text):
        self.driver.wait_for_object("sign_up_lastname")
        self.driver.send_keys("sign_up_lastname", text)

    def enter_sign_up_email_address(self, text):
        self.driver.wait_for_object("sign_up_email")
        self.driver.send_keys("sign_up_email", text)

    def enter_sign_up_email_passwd(self, text):
        self.driver.wait_for_object("sign_up_password")
        self.driver.send_keys("sign_up_password", text)
    
    def click_sign_up_checkbox(self):
        self.driver.click("sign_up_checkbox")
    
    def click_sign_up_button(self):
        self.driver.click("sign_up_button")

    def get_firstName_invalid_data_message(self):
        return self.driver.get_attribute("signup_firstName_errorMessage", "Name")
    
    def get_lastName_invalid_data_message(self):
        return self.driver.get_attribute("signup_lastName_errorMessage", "Name")

    def get_email_invalid_data_message(self):
        return self.driver.get_attribute("signup_email_errorMessage", "Name")
    
    def click_terms_link(self):
        self.driver.click("terms_link")
    
    def click_terms_link(self):
        self.driver.click("hp_offer_link")
    
    def get_sign_in_not_exist_user_message(self):
        return self.driver.get_attribute("signin_error_message", "Name")
    
    def get_sign_up_exist_user_message(self):
        return self.driver.get_attribute("signup_error_message", "Name")
    
    def verify_skip_button_show(self):
        return self.driver.wait_for_object("skip_button", raise_e=False, timeout=10) is not False