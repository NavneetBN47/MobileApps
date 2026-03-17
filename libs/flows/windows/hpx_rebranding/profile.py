from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time

class Profile(HPXRebrandingFlow):
    flow_name = "profile"

    def verify_avatar_close_btn(self):
        return self.driver.wait_for_object("close_avatar_btn", timeout=10)

    def verify_support_device_btn(self):
        return self.driver.wait_for_object("support_device_btn", timeout=10)

    def verify_profile_settings_btn(self):
        return self.driver.wait_for_object("profile_settings_btn", timeout=10)

    def verify_devicepage_avatar_btn(self):
        return self.driver.wait_for_object("avatar_device_page", timeout=20)

    def verify_feedback_btn(self):
        self.driver.wait_for_object("feedback_btn", timeout=10)
        return self.driver.get_attribute("feedback_btn", "Name")

    def verify_sign_in_create_account_btn(self, timeout=30, raise_e=False):
        if self.driver.wait_for_object("sideflyout_sign_in_link", timeout=timeout, raise_e=raise_e):
            return True
        return False

    def verify_top_profile_icon_signed_in(self):
        '''
        This locator can be used only when the user is signed in.
        '''
        return self.driver.wait_for_object("profile_icon_signed_in", raise_e=False, timeout=20)

    def verify_account_link(self):
        """
        Click on Account link from Profile screen
        """
        if self.driver.wait_for_object("profile_account_link", timeout=5, raise_e=False):
            return True
        else:
            return False

    def verify_account_focused_text(self):
        return self.driver.wait_for_object("account_focused_text", timeout=5)

    def verify_profile_side_panel(self):
        if self.driver.wait_for_object("profile_side_panel", timeout=20):
            self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)
            self.driver.wait_for_object("support_device_btn")
            self.driver.wait_for_object("profile_settings_btn")
            self.driver.wait_for_object("feedback_btn")
            self.driver.wait_for_object("close_avatar_btn")
            return True
        else:
            return False

    def verify_global_sidebar_signed_in(self):
        if self.driver.wait_for_object("profile_side_panel"):
            self.driver.wait_for_object("support_device_btn")
            self.driver.wait_for_object("profile_settings_btn")
            self.driver.wait_for_object("profile_account_link")
            return True
        else:
            return False

    def verify_create_account_btn(self):
        return self.driver.wait_for_object("create_account_btn")

    def verify_profile_icon_show_up(self):
        return self.driver.wait_for_object("top_profile_icon") 

    def verify_sign_in_from_avatar_sideflyout(self):
        return self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)

    def verify_navbar_sign_in_button(self):
        return self.driver.wait_for_object("navbar_sign_in_button", timeout = 20)

    def get_user_initials_after_signin(self):
        self.driver.wait_for_object("profile_icon_signed_in", timeout=25)
        return self.driver.get_attribute("profile_icon_signed_in", "Name")

    def check_signin_btn_present(self):
        return self.driver.wait_for_object("navbar_sign_in_button", raise_e=False, timeout = 15)
    
    def verify_subscriptions_link(self):
        return self.driver.wait_for_object("subscriptions_link", timeout=10)

    def verify_close_settings_btn(self):
        return self.driver.wait_for_object("close_settings_btn", timeout=5)

    def verify_myhp_logo(self,raise_e=False,timeout=15):
        return self.driver.wait_for_object("hp_logo",raise_e=raise_e,timeout=timeout)

    def verify_add_device_button(self):
        return self.driver.wait_for_object("add_device_button",timeout=15)

    def verify_org_selector_button(self):
        return self.driver.wait_for_object("org_selector_button", raise_e=False)

    def verify_l1_screen_global_sidebar(self):
        if self.driver.wait_for_object("profile_side_panel"):
            self.driver.wait_for_object("org_selector_button")
            self.driver.wait_for_object("profile_account_link")
            self.driver.wait_for_object("support_device_btn")
            self.driver.wait_for_object("profile_settings_btn")
            self.driver.wait_for_object("feedback_btn")
            return True
        else:
            return False

    def verify_personal_tenant_is_default(self):
        return self.driver.wait_for_object("default_personal")

    def verify_l2_screen_of_org_selector(self): 
        if self.driver.wait_for_object("profile_title"):
            self.driver.wait_for_object("profile_and_organizations_title")
            self.driver.wait_for_object("org_selector_menu_back_button")
            self.driver.wait_for_object("personal_tenant")
            return True
        else:
            return False

    def verify_org_name_tenant_is_default(self):
        return self.driver.wait_for_object("default_org_name")

    def verify_org_name_tenant(self):
        return self.driver.wait_for_object("org_name_tenant")

    def verify_smb_tenant(self):
        return self.driver.wait_for_object("smb_tenant")

    def verify_smb_tenant_is_default(self):
        return self.driver.wait_for_object("default_smb_tenant")

    def verify_hulk_tenant(self):
        return self.driver.wait_for_object("hulk_tenant")

    def verify_hulk_tenant_is_default(self):
        return self.driver.wait_for_object("default_hulk_tenant")

    def verify_profile_setting_page_content(self):
        self.verify_sign_in_from_avatar_sideflyout()
        self.verify_subscriptions_link()
        self.verify_support_device_btn()
        self.verify_profile_settings_btn()
        return True

    def verify_feedback_is_disabled(self, btn):
        element = self.driver.wait_for_object(btn)
        if element.is_enabled() == True:
            return False
        else:
            return True
############################################# Action flows #############################################

    def click_close_avatar_btn(self):
        self.driver.wait_for_object("close_avatar_btn", timeout=15)
        self.driver.click("close_avatar_btn", timeout=10)

    def click_support_device_btn(self):
        self.driver.wait_for_object("support_device_btn", timeout=10)
        self.driver.click("support_device_btn")

    def click_profile_settings_btn(self):
        time.sleep(3)
        self.driver.click("profile_settings_btn")

    def click_devicepage_avatar_btn(self):
        self.driver.wait_for_object("avatar_device_page", timeout=10)
        self.driver.click("avatar_device_page", timeout=20)

    def click_feedback_btn(self):
        self.driver.wait_for_object("feedback_btn", timeout=10)
        self.driver.click("feedback_btn", timeout=10)

    def minimize_hp(self):
        self.driver.click("minimize_hp", timeout=5)

    def maximize_hp(self):
        self.driver.click("maximize_hp")

    def minimize_chrome(self):
        self.driver.wait_for_object("minimize_chrome", raise_e=False, timeout = 15)
        self.driver.click("minimize_chrome", raise_e=False)

    def maximize_chrome(self):
        self.driver.wait_for_object("maximize_chrome", raise_e=False, timeout = 20)
        self.driver.click("maximize_chrome", raise_e=False)

    def click_account_link(self):
        self.driver.click("profile_account_link", timeout = 10)

    def click_top_profile_icon_signed_in(self):
        self.driver.click("profile_icon_signed_in", timeout = 10)

    def click_support_link(self):
        self.driver.click("support_link", displayed=False, timeout = 10)

    def click_sign_in_create_account_btn(self, raise_e=False, timeout=20):
        self.driver.wait_for_object("sideflyout_sign_in_link", timeout=timeout, raise_e=raise_e)
        self.driver.click("sideflyout_sign_in_link", timeout = timeout, raise_e=True)

    def click_profile_icon_signed_in(self):
        self.driver.wait_for_object("profile_icon_signed_in", timeout = 20)
        self.driver.click("profile_icon_signed_in", timeout = 10)

    def click_navbar_sign_in_button(self):
        self.driver.click("navbar_sign_in_button", timeout = 10)

    def title_bar_close_myhp(self):
        self.driver.click("title_bar_close_myhp")

    def verify_and_click_on_try_again_text(self):
        self.driver.wait_for_object("try_again_text", timeout=10)
        self.driver.click("try_again_text")

    def click_sign_in_from_avatar_sideflyout(self):
        self.driver.wait_for_object("sideflyout_sign_in_link", timeout=20)
        self.driver.click("sideflyout_sign_in_link")

    def click_signed_in_profile_icon(self):
        self.driver.wait_for_object("profile_icon_signed_in", timeout=30)
        self.driver.click("profile_icon_signed_in")

    def click_view_privacy_resources_btn(self):
        self.driver.click("privacy_resources_btn", timeout = 10)

    def click_close_hpx_btn(self):
        self.driver.click("close_hpx_btn")

    def click_subscriptions_link(self):
        self.driver.click("subscriptions_link", timeout = 10)

    def click_profile_icon_show_up(self):
        self.driver.click("avatar_device_page")

    def hover_bell_icon(self):
        self.driver.hover("bell_icon")
        self.driver.click("bell_icon", timeout = 10)

    def navigate_to_settings_from_home(self):
        '''
        this is only for signed out flow
        '''
        self.click_devicepage_avatar_btn()
        self.click_profile_settings_btn()

    def click_add_device_button(self):
        self.driver.click("add_device_button")

    def click_org_selector_button(self):
        self.driver.click("org_selector_button")

    def click_org_name_tenant(self):
        self.driver.click("org_name_tenant")

    def click_org_selector_menu_back_button(self):
        self.driver.click("org_selector_menu_back_button")

    def click_smb_tenant(self):
        self.driver.click("smb_tenant")

    def click_hulk_tenant(self):
        self.driver.click("hulk_tenant")

    def click_smart_app_link(self):
        self.driver.click("smart_app_link", timeout=10)

    def verify_delete_your_account_link(self, raise_e=False):
        return self.driver.wait_for_object("hpx_profile_delete_account_btn", raise_e=raise_e, timeout=5)