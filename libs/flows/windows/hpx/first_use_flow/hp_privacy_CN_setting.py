from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class HPPrivacySettingCN(HPXFlow):
    flow_name = "hp_privacysetting_cn"

    def click_accept_all_button(self):
        self.driver.click("accept_all_btn")

    def click_decline_all_button(self):
        self.driver.click("decline_all_btn")
    
    def click_manage_options_button(self):
        self.driver.click("manage_options_btn")

    def verify_hp_privacy_subtitle_show(self):
        return self.driver.wait_for_object("privacy_subtitle_1", raise_e=False)

    def verify_hp_privacy_show(self):
        return self.driver.wait_for_object("privacy_title", raise_e=False)
    
    def check_privacy_title(self):
        return self.driver.get_attribute("privacy_title", "Name")
    
    def check_privacy_subtitle_1(self):
        return self.driver.get_attribute("privacy_subtitle_1", "Name")
    
    def check_privacy_subtitle_2(self):
        return self.driver.get_attribute("privacy_subtitle_2", "Name")
    
    def check_privacy_subtitle_3(self):
        return self.driver.get_attribute("privacy_subtitle_3", "Name")
    
    def verify_accept_button_show(self):
        return self.driver.wait_for_object("accept_all_btn")
    
    def verify_decline_button_show(self):
        return self.driver.wait_for_object("decline_all_btn")
    
    def verify_manage_options_show(self):
        return self.driver.wait_for_object("manage_options_btn")
    
    def click_done_button(self):
        el = self.driver.find_object("done_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)
    
    
    def click_yes_to_all(self):
        el = self.driver.find_object("privacy_consent_yes_to_all")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def vreify_yes_to_all_btn(self):
        return self.driver.wait_for_object("privacy_consent_yes_to_all")
    
    def click_hp_system_link(self):
        self.driver.click("hp_system_link")
