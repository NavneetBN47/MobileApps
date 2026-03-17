import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class HPXSupport(HPXRebrandingFlow):
    flow_name = "hpx_support"

    def verify_support_home_navbar_btn(self):
        return self.driver.wait_for_object("support_home_navbar_btn")

    def verify_contact_us_navbar_btn(self):
        return self.driver.wait_for_object("contact_us_navbar_btn")

    def verify_business_support_navbar_btn(self):
        return self.driver.wait_for_object("business_support_navbar_btn")

    def verify_support_home_link(self):
        return self.driver.wait_for_object("support_home_link")

    def verify_printing_support_link(self):
        return self.driver.wait_for_object("printing_support_link")

    def verify_computing_support_link(self):
        return self.driver.wait_for_object("computing_support_link")

    def verify_support_side_panel_title(self):
        return self.driver.wait_for_object("support_side_panel_title")

    def verify_go_to_support_hp_com(self):
        return self.driver.wait_for_object("support_goto_support_hp_com")

    def verify_support_side_panel(self, support_panel=None):
        self.driver.wait_for_object("support_panel_device_card")
        if support_panel == "support_link":
            self.driver.wait_for_object("support_goto_support_hp_com") # for PROD 
        else:
            self.driver.wait_for_object("add_a_device_btn_support_page") # for ITG & STG

    def verify_browser_pane(self):
        time.sleep(5)  # Waiting for browser pane/tab_name to load
        return self.driver.wait_for_object("tab_name_browser", timeout=15)

    def get_browser_tab_name(self):
        time.sleep(5)  # Waiting for browser pane/tab_name to load
        return self.driver.get_attribute("tab_name_browser", "Name", timeout=15)

    def verify_create_account_btn(self):
        return self.driver.wait_for_object("create_account_btn")

    def verify_username_or_email_placeholder(self):
        return self.driver.wait_for_object("username_or_email_placeholder", timeout=20)

    def verify_sign_in_mobile_num(self):
        return self.driver.wait_for_object("sign_in_mobile_num")

    def verify_use_password_btn(self):
        return self.driver.wait_for_object("use_password_btn")

    def verify_browser_login_page(self, timeout=30, raise_e=False):
        username = self.driver.wait_for_object("username_or_email_placeholder", timeout=timeout, raise_e=raise_e)
        mobile = self.driver.wait_for_object("sign_in_mobile_num", timeout=timeout, raise_e=raise_e)
        password_btn = self.driver.wait_for_object("use_password_btn", timeout=timeout, raise_e=raise_e)
        return bool(username and mobile and password_btn)

    def verify_add_a_device_btn_support_page(self):
        return self.driver.wait_for_object("add_a_device_btn_support_page")

############################################# Action flows #############################################

    def click_support_link(self):
        self.driver.click("support_goto_support_hp_com")

    def click_add_a_device_btn_support_page(self):
        self.driver.click("add_a_device_btn_support_page")
