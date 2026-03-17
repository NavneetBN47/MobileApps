from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class HPLogin(HPXFlow):
    flow_name = "hp_login"

    def close_login_page(self):
        el = self.driver.find_object("close_btn")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def verfiy_login_page_show(self):
        return self.driver.wait_for_object("close_btn", raise_e=False, timeout=60) is not False
        

    def go_to_my_account(self):
        self.driver.wait_for_object("success_icon", raise_e=False, timeout=30)
        self.driver.click("success_icon")
        self.driver.wait_for_object("my_account_button", raise_e=False, timeout=30)
        self.driver.click("my_account_button")
        self.driver.wait_for_object("manage_account_link", raise_e=False, timeout=30)

    
    def click_sign_out_btn(self):
        self.driver.wait_for_object("profile_icon", raise_e=False, timeout=30)
        self.driver.click("profile_icon")
        self.driver.wait_for_object("sign_out_button", raise_e=False, timeout=30)
        time.sleep(3)
        self.driver.click("sign_out_button")

    def verify_manage_account_link_show(self):
        return self.driver.wait_for_object("manage_account_link", raise_e=False, timeout=30)

    def verify_success_icon_show(self):
        return self.driver.wait_for_object("success_icon", raise_e=False, timeout=30)
    
    def verify_profile_icon_show(self):
        return self.driver.wait_for_object("profile_icon", raise_e=False, timeout=30)

    def verify_sign_in_page_show(self):
        return self.driver.wait_for_object("username_form", raise_e=False, timeout=30)
    
    def verify_sign_up_page_show(self):
        return self.driver.wait_for_object("firstname", raise_e=False, timeout=30)
    
    def click_sign_up_link(self):
        self.driver.click("signup_link")
    
    def click_profile_icon(self):
        self.driver.click("profile_icon")
    
    def verify_sigin_create_account_show(self):
        return self.driver.wait_for_object("signin_create_account_btn",raise_e=False,)

    def verify_singout_btn(self):
        self.driver.wait_for_object("sign_out_button")

    def verify_user_signed_in(self):
        self.driver.wait_for_object("user_signed_in")


