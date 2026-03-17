from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys

class HPXSettings(HPXRebrandingFlow):
    flow_name = "hpx_settings"

    def verify_settings_header(self):
        self.driver.wait_for_object("settings_header", timeout=15)
        return self.driver.get_attribute("settings_header", "Name", timeout=10)

    def verify_privacy_tab_visible(self):
        return self.driver.wait_for_object("privacy_tab")

    def verify_version_about_show(self):
        return self.driver.wait_for_object("about_version")

    def get_app_version_copy_btn(self):
        self.driver.wait_for_object("copy_version_btn")
        return self.driver.get_attribute("copy_version_btn", "Name", timeout=10)

    def verify_privacy_statement_link(self):
        return self.driver.wait_for_object("privacy_statement_link")

    def verify_terms_of_use(self):
        for _ in range(10):
            if self.driver.wait_for_object("terms_of_use_link", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("terms_of_use_link")

    def verify_end_user_license_agreement(self):
        return self.driver.wait_for_object("about_user_license_agreement")

    def click_manage_privacy_settings_back_btn(self):
        return self.driver.click("manage_privacy_settings_back_btn")

    def click_hp_end_user_license_agreement(self):
        self.driver.click("about_user_license_agreement", timeout=5)

    def verify_manage_privacy_btn(self):
        return self.driver.wait_for_object("manage_privacy_settings_btn")

    def verify_application_privacy_text(self):
        return self.driver.wait_for_object("application_privacy_text")
    
    def verify_manage_privacy_title(self):
        return self.driver.wait_for_object("manage_privacy_settings_title")

    def verify_delete_your_account_text(self):
        if self.driver.wait_for_object("delete_your_account_text", raise_e=False):
            return True
        else:
            return False

    def verify_computer_privacy_title(self):
        return self.driver.wait_for_object("computer_privacy_title")

    def verify_system_admin_warning_msg(self):
        return self.driver.wait_for_object("system_manage_choices")

    def verify_application_privacy_consents(self):
        self.driver.wait_for_object("product_improvement_consent")
        self.driver.wait_for_object("advertising_text_consent")
        return True

    def verify_device_privacy_text(self):
        return self.driver.wait_for_object("device_privacy_text")

    def verify_about_user_license_agreement(self):
        for _ in range(15):
            if self.driver.wait_for_object("about_user_license_agreement", raise_e=False) is False:
                self.driver.swipe()
            else:
                break   
        return self.driver.wait_for_object("about_user_license_agreement")

    def verify_version_read_only(self):
        self.driver.wait_for_object("about_version")
        self.driver.click("about_version")

    def verify_settings_title(self):
        return self.driver.wait_for_object("settings_title")

    def verify_menu_back_btn_from_settings(self):
        return self.driver.wait_for_object("menu_back_btn_from_settings")

    def verify_sign_out_btn(self):
        self.driver.swipe("sign_out_btn_myhp", distance=5)
        return self.driver.wait_for_object("sign_out_btn_myhp")

    def verify_sign_out_after_clicking_sign_out_btn(self, raise_e=False):
        if self.driver.wait_for_object("sign_out_btn_myhp", raise_e=raise_e):
            return True
        else:
            return False

    def verify_view_privacy_resources_btn(self):
        return self.driver.wait_for_object("privacy_resources_btn", timeout = 10)

    def verify_settings_side_panel(self):
        self.verify_manage_privacy_btn()
        self.verify_privacy_statement_link()
        self.verify_about_section_title()
        self.verify_terms_of_use()
        self.verify_about_user_license_agreement()
        return True

    def verify_device_supply_status_description_text(self):
        return self.driver.wait_for_object("device_supply_status_description_text")

    def verify_device_supply_status_text(self):
        return self.driver.wait_for_object("device_supply_status_text", timeout=20)

    def verify_device_supply_status_toggle(self): 
        return self.driver.wait_for_object("device_supply_status_toggle")

    def verify_about_version_in_settings(self):
        return self.driver.wait_for_object("about_version", timeout=10)

    def verify_navbar_sign_in_button(self):
        return self.driver.wait_for_object("navbar_sign_in_button", timeout = 20)

    def verify_device_privacy_consents(self):
        self.driver.wait_for_object("manage_privacy_settings_back_btn")
        self.driver.wait_for_object("product_improvement_consent")
        self.driver.wait_for_object("advertising_text_consent")

    def return_toggle_status_device_supply(self):
        return self.driver.get_attribute("device_supply_status_toggle", "Toggle.ToggleState")

    def get_system_settings_notifications_toggle_state(self):
        return self.driver.get_attribute("system_notifications_toggle", "Toggle.ToggleState")

    def verify_product_improvement_china_toggle_is_avaibale(self):
        if self.verify_toggle_is_enabled("product_improvement_china_toggle"):
            return True
        else:
            return False

    def verify_advertising_china_is_avaibale(self):
        if self.verify_toggle_is_enabled("advertising_china_toggle"):
            return True
        else:
            return False

    def verify_toggle_is_enabled(self, toggle_name):
        element = self.driver.wait_for_object(toggle_name)
        if element.is_enabled() == True:
            return True
        else:
            return False

    def verify_product_improvement_toggle_is_clicked(self):
        if self.verify_toggle_is_clicked("product_improvement_toggle"):
            return True
        else:
            return False

    def verify_advertising_toggle_is_clicked(self):
        if self.verify_toggle_is_clicked("advertising_toggle"):
            return True
        else:
            return False

    def verify_data_transfer_china_consent_toggle_is_clicked(self):
        if self.verify_toggle_is_clicked("data_transfer_china_toggle"):
            return True
        else:
            return False

    def verify_toggle_is_clicked(self,btn_name):
        element = self.driver.wait_for_object(btn_name)
        if element.get_attribute("Toggle.ToggleState") == "1":
            return True
        else:
            return False

    def verify_manage_privacy_settings_page(self):
        self.verify_manage_privacy_title()
        self.verify_application_privacy_text()
        self.verify_device_privacy_text()
        return True

    def verify_about_section_title(self):
        return self.driver.wait_for_object("about_section_title")

    def verify_manage_privacy_settings_back_btn(self):
        return self.driver.wait_for_object("manage_privacy_settings_back_btn")

    def verify_settings_notifications_title(self):
        return self.driver.wait_for_object("settings_notifications_title")

    def verify_copyright_description_text(self):
        for _ in range(15):
            if self.driver.wait_for_object("copyrights_text", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("copyrights_text")

    def verify_manage_privacy_settings_arrow(self):
        return self.driver.wait_for_object("manage_privacy_settings_arrow")

    def verify_terms_of_use(self):
        return self.driver.wait_for_object("terms_of_use_link")

    def verify_here_link_in_advertising_toggle(self):
        return self.driver.wait_for_object("here_link_in_advertising_toggle")

    def verify_product_improvement_description_text(self):
        return self.driver.wait_for_object("product_improvement_description_text")

    def verify_advertising_description_text(self):
        return self.driver.wait_for_object("advertising_description_text")

    def verify_setting_page_content(self):
        self.verify_settings_notifications_title()
        self.verify_privacy_tab_visible()
        self.verify_about_section_title()
        self.verify_device_supply_status_text()
        self.verify_device_supply_status_toggle()
        self.verify_device_supply_status_description_text()
        self.verify_manage_privacy_btn()
        self.verify_privacy_statement_link()
        self.verify_terms_of_use()
        self.verify_about_user_license_agreement()
        return True
    
    def verify_app_instance_id(self):
        return self.driver.wait_for_object("app_instance_id")

    def get_manage_privacy_description_text(self):
        return self.driver.get_attribute("manage_privacy_description_text", "Name")

    def verify_customer_support_consent(self, raise_e=False):
        return self.driver.wait_for_object("customer_support_consent", raise_e=raise_e, timeout=10)

    def get_computer_privacy_customer_support_toggle_state(self):
        state = self.driver.get_attribute(
                    "manage_privacy_customer_support_toggle", "Toggle.ToggleState")
        return "ON" if str(state) == "1" else "OFF"

    def get_computer_privacy_product_improvement_toggle_state(self):
        state = self.driver.get_attribute(
                    "manage_privacy_product_improvement_toggle", "Toggle.ToggleState")
        return "ON" if str(state) == "1" else "OFF"

    def get_computer_privacy_advertising_toggle_state(self):
        state = self.driver.get_attribute(
                    "manage_privacy_advertising_toggle", "Toggle.ToggleState")
        return "ON" if str(state) == "1" else "OFF"

    def verify_delete_your_account_link(self, raise_e=True):
        """
        Verify if the "Delete your Account" link is present in the Privacy settings.
        """
        return self.driver.wait_for_object("delete_your_account_link", raise_e=raise_e)

    def verify_computer_privacy_customer_support_description_text(self, raise_e=True):
        return self.driver.wait_for_object("computer_privacy_customer_support_description_text", raise_e=raise_e, timeout=15)

    def verify_computer_privacy_product_improvement_text(self, raise_e=True):
        return self.driver.wait_for_object("computer_privacy_product_improvement_description_text", raise_e=raise_e, timeout=15)
    
    def verify_computer_privacy_advertising_description_text(self, raise_e=True):
        return self.driver.wait_for_object("computer_privacy_advertising_description_text", raise_e=raise_e, timeout=15)
    
    def get_manage_privacy_product_improvement_toggle_state(self):
        state = self.driver.get_attribute(
            "manage_privacy_product_improvement_toggle", "Toggle.ToggleState"
        )
        return "ON" if str(state) == "1" else "OFF"
 
    def get_manage_privacy_advertising_toggle_state(self):
        state = self.driver.get_attribute(
            "manage_privacy_advertising_toggle", "Toggle.ToggleState"
        )
        return "ON" if str(state) == "1" else "OFF"
    
    def verify_computer_privacy_warning_message(self, raise_e=False):
        return self.driver.wait_for_object("computer_privacy_warning_message", raise_e=raise_e , timeout=10)

    def get_system_admin_warning_msg(self):
        return self.driver.get_attribute("system_manage_choices", "Name")
  
  ##################################### verification actions #####################################

    def click_privacy_statement_link(self):
        self.driver.click("privacy_statement_link", timeout=5)

    def click_terms_of_use(self):
        self.driver.click("terms_of_use_link", timeout=5)

    def click_profile_settings_btn(self):
        self.driver.click("settings_btn_home", timeout=20)

    def click_myhp_on_task_bar(self):
        self.driver.click("myhp_on_task_bar", timeout=5)

    def sign_out_from_settings(self):
        self.driver.click("profile_icon_signed_in", timeout = 20)
        self.click_profile_settings_btn()
        self.verify_about_version_in_settings()
        self.click_sign_out_btn()
        self.verify_navbar_sign_in_button()

    def click_manage_privacy_btn(self):
        self.driver.click("manage_privacy_settings_btn")

    def click_device_privacy_btn(self):
        self.driver.swipe("device_privacy_btn", direction="down")
        self.driver.click("device_privacy_btn")

    def click_menu_back_btn_from_settings(self):
        self.driver.click("menu_back_btn_from_settings", timeout=5)

    def click_sign_out_btn(self):
        self.driver.swipe("sign_out_btn_myhp", distance=5)
        el = self.driver.wait_for_object("sign_out_btn_myhp")
        el.send_keys(Keys.ENTER)

    def scroll_to_up_menu_btn(self):
        self.driver.swipe("privacy_statement_link",direction="up")
        self.driver.wait_for_object("menu_back_btn_from_settings")

    def click_about_user_license_agreement(self):
        self.driver.click("about_user_license_agreement", timeout = 10)

    def click_view_privacy_resources_btn(self):
        self.driver.click("privacy_resources_btn", timeout = 10)

    def click_support_device_btn_right_arrow(self):
        self.driver.click("support_device_btn", timeout=10)

    def go_home_from_settings_and_support(self, page=None):
        if page == "support_page":
            self.driver.click("back_menu_btn_support_panel")
        else:
            self.driver.swipe("menu_back_btn_from_settings", direction="up")
            self.driver.click("minimize_hp")
            self.driver.click("myhp_on_task_bar", timeout=10)
            self.driver.click("menu_back_btn_from_settings")
        self.driver.wait_for_object("close_avatar_btn")
        self.driver.click("minimize_hp")
        self.driver.click("myhp_on_task_bar", timeout=10)
        self.driver.click("close_avatar_btn")

    def click_device_supply_status_toggle(self):
        self.driver.click("device_supply_status_toggle", timeout=5)

    def get_device_supply_status_description_text(self):
        return self.driver.get_attribute("device_supply_status_description_text", "Name")

    def click_system_notifications_toggle(self):
        self.driver.click("system_notifications_toggle")

    def minimize_and_click_hp_from_taskbar(self):
        self.driver.click("minimize_hp")
        self.driver.click("myhp_on_task_bar", timeout=10)

    def get_product_improvement_description_text(self):
        return self.driver.get_attribute("product_improvement_description_text", "Name")

    def get_advertising_description_text(self):
        return self.driver.get_attribute("advertising_description_text", "Name")

    def click_computer_privacy_customer_support_china_toggle(self):
        self.driver.click("computer_privacy_customer_support_china_toggle", timeout=5)  
        
    def click_computer_privacy_product_improvement_china_toggle(self):
        self.driver.click("computer_privacy_product_improvement_china_toggle", timeout=5)
        
    def click_computer_privacy_advertising_china_toggle(self):
        self.driver.click("computer_privacy_advertising_china_toggle", timeout=5)
        
    def click_device_privacy_back_btn(self):
        self.driver.click("device_privacy_back_btn", timeout=5)
    
    def click_computer_privacy_product_improvement_link(self):
        self.driver.click("computer_privacy_product_improvement_link", timeout=10)

    def click_device_privacy_arrow_button(self):
        self.driver.swipe("device_privacy_button_arrow", direction="down")
        self.driver.click("device_privacy_button_arrow", timeout=10)

    def click_here_link_in_advertising_toggle(self):
        self.driver.click("here_link_in_advertising_toggle", timeout=10)