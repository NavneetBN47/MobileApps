from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow

class HpxFUF(HPXFlow):
    flow_name = "hpx_fuf"

# *********************************************************************************
#                                VERIFICATION FLOWS                               *
# *********************************************************************************

    def verify_accept_all_button_show_up(self):
        return self.driver.wait_for_object("accept_all_button", raise_e=False, timeout=20)
    
    def verify_continue_as_guest_button_show_up(self):
        return self.driver.wait_for_object("continue_as_guest_button", raise_e=False, timeout=10)
    
    def verify_camera_yes_button_show(self):
        return self.driver.wait_for_object("yes_button_in_let_access_dialog", raise_e=False, timeout=25)
    
    def verify_what_is_this_dialog_show(self):
        return self.driver.wait_for_object("what_is_new_skip_button", raise_e=False, timeout=15)
    
    def verify_privacy_page_heading_show(self):
        return self.driver.wait_for_object("privacy_page_heading", raise_e=False, timeout=20)
    
    def verify_accept_cookies_button_show(self):
        return self.driver.wait_for_object("accept_cookies_button", raise_e=False, timeout=15)

    def verify_continue_update_button_show(self):
        return self.driver.wait_for_object("continue_update_button", raise_e=False, timeout=30)

    def verify_cancel_update_button_show(self):
        return self.driver.wait_for_object("cancel_update_button", raise_e=False, timeout=30)

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************
    def click_privacy_page_heading(self):
        self.driver.click("privacy_page_heading")
    
    def click_accept_all_button(self):
        self.driver.click("accept_all_button")

    def click_continue_as_guest_button(self):
        self.driver.click("continue_as_guest_button")
    
    def click_camera_yes_button_on_let_myhp_access_dialog(self):
        self.driver.click("yes_button_in_let_access_dialog", timeout = 20)
    
    def click_what_is_new_skip_button(self):
        self.driver.click("what_is_new_skip_button")

    def click_accept_cookies_button(self):
        self.driver.click("accept_cookies_button")

    def click_continue_as_guest_btn(self):
        if self.verify_continue_as_guest_button_show_up():
            self.click_continue_as_guest_button()

    def click_continue_update_button(self):
        self.driver.click("continue_update_button")
    
    def click_cancel_update_button(self):
        self.driver.click("cancel_update_button")