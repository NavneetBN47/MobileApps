from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class CSS(HPXRebrandingFlow):
    flow_name = "css"

    def verify_settings_button_on_profile_page(self):
        return self.driver.wait_for_object("settings_title", timeout=15, raise_e=False)
    
    def click_settings_button_on_profile_page(self):
        self.driver.click("settings_title")

    def verify_settings_title_show_up(self):
        return self.driver.wait_for_object("settings_title", timeout=15, raise_e=False)
    
    def verify_manage_privacy_settings_button_on_settings_show_up(self):
        return self.driver.wait_for_object("manage_privacy_settings_button", timeout=15, raise_e=False)
    
    def verify_about_card_on_settings_show_up(self):
        return self.driver.wait_for_object("about_card_on_settings", timeout=15, raise_e=False)
    
    def verify_feedback_button_on_profile_page(self):
        return self.driver.wait_for_object("feedback_button", timeout=15, raise_e=False)
    
    def click_feedback_button_on_profile_page(self):
        self.driver.click("feedback_button")

    def verify_feedback_title_show_up(self):
        return self.driver.wait_for_object("feedback_title", timeout=15, raise_e=False)

    def verify_star_on_feedback_show_up(self):
        return self.driver.wait_for_object("star_on_feedback", timeout=15, raise_e=False)

    def verify_send_feedback_button_show_up(self):
        return self.driver.wait_for_object("send_feedback_button", timeout=15, raise_e=False)

    def verify_account_button_on_profile_page(self):
        return self.driver.wait_for_object("account_button", timeout=15, raise_e=False)

    def verify_close_button_show_up(self):
        return self.driver.wait_for_object("close_button", timeout=15, raise_e=False)

    def click_close_button(self):
        self.driver.click("close_button", timeout=10)

    def verify_back_to_menu_button_show_up(self):
        return self.driver.wait_for_object("back_to_menu_button", timeout=15, raise_e=False)
    
    def click_back_to_menu_button(self):
        self.driver.click("back_to_menu_button")

    def verify_sign_in_button_show_up(self):
        return self.driver.wait_for_object("sign_in_button", timeout=15, raise_e=False)
    
    def click_sign_in_button(self):
        self.driver.click("sign_in_button", timeout=10)

    def verify_app_version_txt_show_up(self):
        return self.driver.wait_for_object("app_version_txt", timeout=15, raise_e=False)
    
    def get_app_version_txt(self):
        return self.driver.get_attribute("app_version_txt", "Name", timeout=15)

    def verify_bell_icon_show_up(self):
        return self.driver.wait_for_object("bell_icon", timeout=20, raise_e=False)
    
    def click_bell_icon(self):
        self.driver.click("bell_icon")

    def verify_notification_title_show_up(self):
        return self.driver.wait_for_object("notification_title", timeout=15, raise_e=False)

    def verify_profile_txt_show_up(self):
        return self.driver.wait_for_object("profile_txt", timeout=15, raise_e=False)
    
    def verify_profile_icon_show_up(self):
        return self.driver.wait_for_object("profile_icon", timeout=15, raise_e=False)

    def verify_support_option_show_on_profile_page(self):
        return self.driver.wait_for_object("support_option", timeout=15, raise_e=False)

    def click_support_option_on_profile_page(self):
        self.driver.click("support_option")

    def verify_support_title_show_up(self):
        return self.driver.wait_for_object("support_title", raise_e=False, timeout = 10)

    def get_support_link_txt(self):
        return self.driver.get_attribute("support_link", "Name", timeout=20)

    def verify_myhp_title_bar(self):
        return self.driver.wait_for_object("myhp_title_bar", timeout=25)

    def verify_sign_in_btn_welcome_page(self):
        return self.driver.wait_for_object("sign_in_btn_welcome_page", timeout=15)

    def click_sign_in_btn_welcome_page(self):
        self.driver.click("sign_in_btn_welcome_page")

    def verify_open_myhp_alert(self):
        return self.driver.wait_for_object("open_myhp_alert", raise_e=False)

    def click_open_myhp_alert_btn(self):
        self.driver.click("open_myhp_alert_btn", timeout=5, raise_e=False)

    def verify_hp_maximize(self):
        # myHP is rebranded to HP
        self.driver.wait_for_object("maximize_hp", timeout=15)
        return self.driver.get_attribute("maximize_hp","Name")

    def maximize_hp(self):
        if "Maximize HP" == self.verify_hp_maximize():
            self.driver.click("maximize_hp")
