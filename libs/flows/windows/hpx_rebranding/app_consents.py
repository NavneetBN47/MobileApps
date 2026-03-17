from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
import logging

class AppConsents(HPXRebrandingFlow):
    flow_name = "app_consents"

# *********************************************************************************
#                                VERIFICATION FLOWS                               *
# *********************************************************************************
    def verify_start_window_show_up(self):
        return self.driver.wait_for_object("start_window", timeout=20)

    def verify_privacy_here_link(self):
        return self.driver.wait_for_object("privacy_here_link", timeout=20)

    def verify_we_value_your_privacy_title(self):
        return self.driver.wait_for_object("we_value_your_privacy_title", timeout=20)

    def verify_terms_of_use_link(self):
        return self.driver.wait_for_object("terms_of_use_link", timeout=20)

    def verify_end_user_license_agreement_link(self):
        return self.driver.wait_for_object("end_user_license_agreement_link", timeout=20)

    def verify_hp_privacy_statement_link(self):
        return self.driver.wait_for_object("hp_privacy_statement_link", timeout=20)

    def verify_manage_choices_btn(self):
        self.driver.wait_for_object("manage_choices_btn")
        return True

    def verify_manage_choices_text(self):
        return self.driver.wait_for_object("manage_choices_text")

    def verify_accept_all_button_show_up(self):
        if self.driver.wait_for_object("accept_all_button",raise_e=False) is True:
            self.driver.swipe()
            self.driver.wait_for_object("accept_all_button")
        return True

    def verify_decline_optional_data(self):
        return self.driver.wait_for_object("decline_optional_data_btn", timeout=15)

    def verify_continue_as_guest_button_show_up(self):
        self.driver.wait_for_object("continue_as_guest_button", timeout=20)
        return True

    def verify_privacy_page_heading_show(self):
        return self.driver.wait_for_object("privacy_page_heading", timeout=20)

    def verify_accept_cookies_button_show(self):
        return self.driver.wait_for_object("accept_cookies_button", timeout=15)

    def verify_product_improvement_btn(self):
        return self.driver.wait_for_object("product_improvement_btn")

    def verify_adverstising_btn(self):
        return self.driver.wait_for_object("advertising_btn")

    def verify_advertising_here_link(self):
        return self.driver.wait_for_object("advertising_here_link", timeout=15)

    def verify_manage_privacy_back_btn(self):
        return self.driver.wait_for_object("manage_privacy_back_btn")

    def verify_manage_privacy_continue_btn(self):
        return self.driver.wait_for_object("manage_privacy_continue_btn")

    def verify_manage_choices_title_for_china(self):
        return self.driver.wait_for_object("manage_choices_title_china")

    def verify_your_data_and_privacy_title_china(self):
        return self.driver.wait_for_object("your_data_and_privacy_title_china", timeout=15)

    def verify_data_transfer_consent_for_china(self):
        self.driver.wait_for_object("data_transfer_consent_btn")
        return True

    def verify_product_improvement_btn_for_china(self):
        return self.driver.wait_for_object("product_improvement_china")

    def verify_advertising_btn_for_china(self):
        return self.driver.wait_for_object("advertising_china")

    def verify_product_improvement_china_is_enabled(self):
        self.driver.wait_for_object("product_improvement_china")
        if self.driver.get_attribute("product_improvement_china", "IsEnabled", raise_e=False, timeout=10).lower() == "true":
            return True
        else:
            return False

    def verify_advertising_china_is_enabled(self):
        self.driver.wait_for_object("advertising_china").is_enabled()
        if self.driver.get_attribute("advertising_china", "IsEnabled", raise_e=False, timeout=10).lower() == "true":
            return True
        else:
            return False

    def verify_advertising_india_is_enabled(self):
        return self.driver.wait_for_object("advertising_btn").is_enabled() 

    def verify_product_improvement_india_is_enabled(self):
        return self.driver.wait_for_object("product_improvement_btn").is_enabled()

    def verify_product_improvement_toggle_is_clicked(self):
        if self.verify_toggle_is_clicked("product_improvement_toggle_on") == "1":
            return True
        else:
            return False

    def verify_advertising_toggle_is_clicked(self):
        if self.verify_toggle_is_clicked("advertising_toggle_on") == "1":
            return True
        else:
            return False

    def verify_toggle_is_clicked(self,btn_name):
        element = self.driver.wait_for_object(btn_name)
        if element.get_attribute("Toggle.ToggleState") == "1":
            return True
        else:
            return False

    def verify_your_data_and_privacy_title(self):
        return self.driver.wait_for_object("your_data_and_privacy_title")

    def verify_close_app_privacy_btn(self):
        return self.driver.wait_for_object("close_app_privacy_btn")

    def get_necessary_text_from_apponly_consent_screen(self):
       return self.driver.get_attribute("necessary_text_from_apponly_consent_screen","Name") 

    def get_necessary_text_from_manage_choice_consent_screen(self):
        return self.driver.get_attribute("necessary_text_from_manage_choice_consent_screen","Name")

    def verify_manage_privacy_description_text(self):
        return self.driver.wait_for_object("manage_privacy_description_text")

    def verify_product_improvement_icon(self):
        return self.driver.wait_for_object("product_improvement_icon")

    def verify_advertising_icon(self):
        return self.driver.wait_for_object("advertising_icon") 

    def verify_manage_choice_continue_btn(self):
        return self.driver.wait_for_object("manage_choice_continue_btn")

    def verify_manage_choice_back_btn(self):
        return self.driver.wait_for_object("manage_choices_back_btn")

    def verify_close_app_privacy_btn(self):
        return self.driver.wait_for_object("close_app_privacy_btn")

    def verify_your_data_and_privacy_text(self):
        return self.driver.wait_for_object("your_data_and_privacy_text")

    def verify_manage_choices_back_btn(self):
        return self.driver.wait_for_object("manage_choices_back_btn")

    def verify_manage_choices_title(self):
        return self.driver.wait_for_object("manage_choices_title")

    def verify_product_improvement_toggle_off(self):
        return self.driver.wait_for_object("product_improvement_toggle_off")

    def verify_advertising_toggle_off(self):
        return self.driver.wait_for_object("advertising_toggle_off")
    
    def verify_app_only_consents_screen(self, raise_e=False):
        elements = [
            "your_data_and_privacy_title",
            "we_value_your_privacy_title",
            "terms_of_use_link",
            "ai_terms_of_use_link",
            "end_user_license_agreement_link",
            "hp_privacy_statement_link",
            "manage_choices_btn",
            "decline_optional_data_btn",
            "accept_all_button"
        ]
        return all(self.driver.wait_for_object(el, raise_e=raise_e) for el in elements)
        

    def verify_manage_choices_screen(self):
        self.driver.wait_for_object("manage_choices_title")
        self.driver.wait_for_object("product_improvement_btn")
        self.driver.wait_for_object("product_improvement_toggle_off")
        self.driver.wait_for_object("advertising_btn")
        self.driver.wait_for_object("advertising_toggle_off")
        self.driver.wait_for_object("your_data_and_privacy_title")
        try:
            self.driver.wait_for_object("customer_support_icon")
        except:
            logging.warning("Customer support icon not present")
        self.driver.wait_for_object("your_data_and_privacy_title")

    def verify_app_and_device_common_consents_screen(self):
        self.driver.wait_for_object("we_value_your_privacy_title")
        self.driver.wait_for_object("your_data_and_privacy_title")

    def verify_necessary_text_from_app_and_device_consents_screen(self):
        return self.driver.wait_for_object("necessary_text_from_app_device_consent_screen")

    def verify_ai_terms_of_use_link(self):
        return self.driver.wait_for_object("ai_terms_of_use_link")

    def verify_ai_terms_of_use_clicked_title(self,expected):
        logging.info("Verifying AI Terms of Use clicked title...")
        return expected in self.driver.wait_for_object("ai_terms_of_use_clicked_title").get_attribute("Name")

    def verify_hp_logo(self, raise_e=False):
        return self.driver.wait_for_object("hp_logo", raise_e=raise_e, timeout=10)

    def get_paragraph_1_basic_data_collection_text(self):
        return self.get_paragraph_text("paragraph_1_basic_data_collection_consent")

    def get_paragraph_2_optional_data_collection_text(self):
        return self.get_paragraph_text("paragraph_2_optional_data_collection_consent")

    def get_paragraph_3_accept_all_text(self):
        return self.get_combined_paragraph_text([
            "paragraph_3_data_collection_consent",
            "paragraph_3_data_collection_consent_highlight",
            "paragraph_3_data_collection_consent_suffix",
        ])

    def get_paragraph_4_manage_choices_text(self):
        return self.get_combined_paragraph_text([
            "paragraph_4_data_collection_consent",
            "paragraph_4_manage_choices_text",
        ])

    def get_paragraph_5_privacy_update_text(self):
        return self.get_paragraph_text("paragraph_5_data_collection_consent")

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************
    def click_close_app_privacy_btn(self):
        self.driver.click("close_app_privacy_btn", timeout=10)

    def click_manage_choices_btn(self):
        self.driver.swipe( direction="down",distance=3)
        if self.driver.wait_for_object("manage_choices_btn",timeout=15):
            self.driver.click("manage_choices_btn",timeout=10)

    def click_privacy_here_link(self):
        self.driver.click("privacy_here_link", timeout=20)

    def click_terms_of_use_link(self):
        self.driver.wait_for_object("terms_of_use_link", timeout=20)
        self.driver.click("terms_of_use_link", timeout=20)

    def click_end_user_license_agreement_link(self):
        self.driver.click("end_user_license_agreement_link", timeout=20)

    def click_privacy_page_heading(self):
        self.driver.click("privacy_page_heading")

    def click_decline_optional_data_button(self):
        self.driver.swipe(direction="down", distance=3)
        if self.driver.wait_for_object("decline_optional_data_btn", timeout=20) is not False:
            self.driver.click("decline_optional_data_btn", timeout=20)

    def click_accept_all_button(self):
        self.driver.swipe(direction="down", distance=3)
        if self.driver.wait_for_object("accept_all_button", timeout=20) is not False:
            self.driver.click("accept_all_button")

    def click_product_improvement_btn(self):
        self.driver.click("product_improvement_btn", timeout=10)

    def click_advertising_btn(self):
        self.driver.click("advertising_btn", timeout=10)

    def click_advertising_here_link(self):
        self.driver.click("advertising_here_link", timeout=15)

    def click_manage_privacy_back_btn(self):
        self.driver.swipe(direction="down", distance=3)
        if self.driver.wait_for_object("manage_privacy_back_btn", timeout=10) is not False:
            self.driver.click("manage_privacy_back_btn")

    def click_manage_privacy_continue_btn(self):
        self.driver.click("manage_privacy_continue_btn", timeout=10)

    def click_continue_as_guest_button(self):
        self.driver.click("continue_as_guest_button")

    def click_app_settings_tab(self):
        self.driver.click("my_hp_system_app_settings", timeout=15)
        time.sleep(5)

    def click_app_reset_button(self):
        self.driver.swipe("app_reset_button",direction="down", distance=7)
        self.driver.click("app_reset_button" , timeout =10)
        time.sleep(15)    
        self.driver.click("app_reset_confirm_button")

    def close_windows_settings_panel(self):
        self.driver.ssh.send_command('powershell Stop-Process -Name "SystemSettings"', timeout=15)

    def click_data_transfer_consent_for_china(self):
        self.driver.click("data_transfer_consent_btn")

    def click_product_improvement_btn_for_china(self):
        self.driver.click("product_improvement_china")

    def click_advertising_btn_for_china(self):
        self.driver.click("advertising_china")

    def verify_necessary_text(self):
        necessary_text = self.get_necessary_text_from_apponly_consent_screen()
        logging.info(f"App_only consent Text: '{necessary_text}'")
        sentence = necessary_text.split(".")
        sentence = sentence[0].split(",")
        result = sentence[1]
        logging.info(f"Necessary Text to be verify: '{result}'")

        if result not in necessary_text:
            logging.error(f"Necessary text does not contain '{result}'")
            return False
        else:
            logging.info(f"Necessary text contains '{result}'")
            return True

    def verify_manage_choice_body_text(self):
        necessary_text=self.get_necessary_text_from_manage_choice_consent_screen()
        logging.info(f"Manage_choice consent Text: '{necessary_text}'")
        sentence = necessary_text.split(".")
        result=sentence[0]
        logging.info(f"Necessary Text to be verify: '{result}'")
        if result  not in necessary_text:
            logging.error(f"Necessary text does not contain '{result}'")
        else:
            logging.info(f"Necessary text contains '{result}'")

    def click_manage_choices_back_btn(self):
        self.driver.click("manage_choices_back_btn", timeout = 10)

    def click_hp_privacy_statement_link(self):
        self.driver.click("hp_privacy_statement_link", timeout = 10)

    def click_manage_choice_continue_btn(self):
        self.driver.click("manage_choice_continue_btn", timeout = 10)

    def verify_app_privacy_title(self):
        self.driver.wait_for_object("app_privacy_title")

    def click_ai_terms_of_use_link(self):
        self.driver.click("ai_terms_of_use_link",timeout=15)
