from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow

class WEBPOPUP(GothamFlow):
    flow_name="web_popup"

    def click_always_allow_checkbox(self):
        self.driver.click("always_allow_checkbox", timeout=10)

    def click_web_hpid_open_btn(self):
        self.driver.click("web_hpid_open_button")

    def click_save_password_never_button(self):
        self.driver.click("save_password_never_button")
        
    def verify_web_hpid_page(self):
        return self.driver.wait_for_object("web_hpid_page", raise_e=False)

    def verify_save_password_popup(self):
        return self.driver.wait_for_object("save_password_never_button", raise_e=False)
