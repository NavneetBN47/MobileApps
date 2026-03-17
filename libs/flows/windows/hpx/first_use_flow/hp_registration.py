from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction


class HPRegistration(HPXFlow):
    flow_name = "hp_registration"

    def check_sub_title_text(self):
        return self.driver.get_attribute("register_subtitle", "Name")

    def verify_hp_registration_show(self):
        obj = self.driver.wait_for_object("register_subtitle", raise_e=False, timeout=10)
        if obj:
            return obj.is_displayed()
        else:
            return False
    
    def verify_skip_button_show(self):
        return self.driver.wait_for_object("skip_button", raise_e=False, timeout=30) is not False

    def click_skip_button(self):
        self.driver.wait_for_object("skip_button", clickable=True, raise_e=False, timeout=15)
        self.driver.click("skip_button", timeout=10)

    def verify_continue_button(self):
        return self.driver.wait_for_object("continue_btn", clickable=True, raise_e=False, timeout=15) is not False

    def click_continue_button(self):
        self.driver.click("continue_btn")

    def click_hpone_skip_button(self):
        self.driver.click("hpone_skip_button")
        
    def open_privacy_link(self):
        self.driver.click("privacy_link")
        
    def get_privacy_url_text(self):
        return self.driver.get_attribute("privacy_in_browser", "Value.Value")
    
    def enter_first_name(self, text):
        self.driver.wait_for_object("first_name", timeout=30)
        self.driver.send_keys("first_name", text)
    
    def enter_last_name(self, text):
        self.driver.wait_for_object("last_name")
        self.driver.send_keys("last_name", text)

    def enter_email_address(self, text):
        self.driver.wait_for_object("email_address")
        self.driver.send_keys("email_address", text) 
    
    def registtation_button_is_selected(self):
        return self.driver.get_attribute("register_button", "IsKeyboardFocusable")
    
    def get_firstName_invalid_data_message(self):  
        return self.driver.get_attribute("firstName_invalid_data", "Name")
    
    def get_lastName_invalid_data_message(self):
        return self.driver.get_attribute("lastName_invalid_data", "Name")

    def get_email_invalid_data_message(self):
        return self.driver.get_attribute("email_invalid_data", "Name")
    
    def verify_firstName_invalid_data_message_show(self):
        return self.driver.wait_for_object("firstName_invalid_data", raise_e=False, timeout=10)

    def verify_lastName_invalid_data_message_show(self):
        return self.driver.wait_for_object("lastName_invalid_data", raise_e=False, timeout=10)
    
    def verify_email_invalid_data_message_show(self):
        return self.driver.wait_for_object("email_invalid_data", raise_e=False, timeout=10)

    def complete_register(self,firstname, lastname, email):
        self.driver.wait_for_object("first_name", timeout=30)
        self.driver.send_keys("first_name", firstname)
        self.driver.wait_for_object("last_name")
        self.driver.send_keys("last_name", lastname)
        self.driver.wait_for_object("email_address")
        self.driver.send_keys("email_address", email)
        self.driver.click("register_button")
    
    def verify_register_success(self):
        return self.driver.wait_for_object("success_message", raise_e=False, timeout=10) is not False
    
    def verify_header_text(self):
        return self.driver.get_attribute("registration_header", "Name")

    def verify_register_buttontext(self):
        return self.driver.get_attribute("register_button_text", "Name")

    def verify_skip_buttontext(self):
        return self.driver.get_attribute("skip_button", "Name")

    def check_localization_sub_title(self):
        return self.driver.get_attribute("localization_register_subtitle", "Name")

    def verify_localization_register_button(self):
        return self.driver.get_attribute("localization_register_buttontitle", "Name")

    def verify_localization_skip_button(self):
        return self.driver.get_attribute("localization_skip_buttontitle", "Name")
    
    def click_country_dropdown_list(self):
        self.driver.click("country_dropdown_list")
    
    def veify_country_uganda_show(self):
        return self.driver.wait_for_object("country_uganda", raise_e=False, timeout=10)
    
    def veify_country_ukraine_show(self):
        return self.driver.wait_for_object("country_ukraine", raise_e=False, timeout=10)
    
    def veify_country_kingdom_show(self):
        return self.driver.wait_for_object("country_kingdom", raise_e=False, timeout=10)
    
    def click_skip_next_btn(self):
        if(self.driver.wait_for_object("localization_skip_buttontitle", raise_e=False, timeout=10)) is True:
            self.driver.click("localization_skip_buttontitle")

    def verify_registration_page_is_display(self):
        return self.driver.wait_for_object("registration_header", raise_e=False, timeout=10)

    def check_localization_firstname_text(self):
        return self.driver.get_attribute("first_name", "Name")
    
    def check_localization_lastname_text(self):
        return self.driver.get_attribute("last_name", "Name")
    
    def check_localization_email_text(self):
        return self.driver.get_attribute("email_address", "Name")
    
    def verify_localization_privacy_statement(self):
        return self.driver.get_attribute("privacy_link", "Name")
    
    def verify_hpone_page_show(self):
        return self.driver.wait_for_object("hpone_page_title", raise_e=False, timeout=10) is not False
    
    def click_hpone_page_skip_btn(self):
        self.driver.click("hpone_page_btn")

    def check_localization_country(self):
        return self.driver.get_attribute("country_dropdown_list", "Name")
    
    def enter_invalid_first_name(self):
        self.driver.wait_for_object("first_name", timeout=30)
        self.driver.send_keys("first_name", "#")
    
    def enter_invalid_last_name(self):
        self.driver.wait_for_object("last_name", timeout=30)
        self.driver.send_keys("last_name", "#")
    
    def enter_invalid_email(self):
        self.driver.wait_for_object("email_address", timeout=30)
        self.driver.send_keys("email_address", "#")

    def check_localization_invalid_first_name(self):
        return self.driver.get_attribute("firstName_invalid_data", "Name")

    def check_localization_invalid_last_name(self):
        return self.driver.get_attribute("lastName_invalid_data", "Name")
    
    def check_localization_invalid_email(self):
        return self.driver.get_attribute("email_invalid_data", "Name")
