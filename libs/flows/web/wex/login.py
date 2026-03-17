from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class Login(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "login"

    def verify_sign_in_btn(self):
        return self.driver.wait_for_object("signin_btn",timeout=60)
    
    def click_sign_in_btn(self):
        return self.driver.click("signin_btn",timeout=20)

    def verify_email_address(self):
        return self.driver.wait_for_object("email_txt_box",timeout=30)

    def enter_email_address(self, email):
        return self.driver.send_keys("email_txt_box", email)
    
    def click_continue_btn_btn(self):
        # self.driver.verify_object_string("continue_btn"
        return self.driver.click("continue_btn",timeout=30)
    
    def verify_password_txt(self):
        return self.driver.wait_for_object("password_txt_box",timeout=30)
    
    def enter_password(self, password):
        return self.driver.send_keys("password_txt_box", password)

    def verify_login_btn(self):
        return self.driver.wait_for_object("login_btn",timeout=20)
    
    def click_login_btn(self):
        return self.driver.click("login_btn")

    def click_use_password_button(self):
        return self.driver.click("use_password_button",timeout=30)

    def login_wex(self, email, password):
        self.verify_sign_in_btn()
        self.click_sign_in_btn()
        self.verify_email_address()
        self.enter_email_address(email)
        self.click_continue_btn_btn()
        self.click_use_password_button()
        self.verify_password_txt()
        self.enter_password(password)
        self.click_login_btn()