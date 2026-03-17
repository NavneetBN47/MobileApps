from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class Settings(HPXFlow):
    flow_name = "settings"

    def click_privacy_url(self):
        self.driver.click("click_privacy_btn")

    def verify_settings_header(self):
        return self.driver.wait_for_object("settings_header").get_attribute("Name")
    
    def verify_settings_module_show_on_global_navigation_panel(self):
        return self.driver.wait_for_object("settings_module", raise_e=False, timeout=10)
      
    def click_done_button(self):
        el = self.driver.find_object("done_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def click_learn_more(self):
        self.driver.click("learn_more_link")

    def click_yes_to_all(self):
        el = self.driver.find_object("privacy_consent_yes_to_all")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)
    
    def click_warranty_yes_button(self):
        el = self.driver.find_object("warranty_consent_yes_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def click_warranty_no_button(self):
        self.driver.click("warranty_consent_no_button")

    def click_sysinfo_yes_button(self):
        el = self.driver.find_object("sysinfo_consent_yes_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width, height)
        
    
    def click_sysinfo_no_button(self):
        el = self.driver.find_object("sysinfo_consent_no_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width, height)

    def click_marketing_yes_button(self):
        el = self.driver.find_object("marketing_consent_yes_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width, height)
        
    def verify_marketing_consent_show(self):
        return self.driver.wait_for_object("marketing_consent") is not False
    
    def click_marketing_no_button(self):

        self.driver.click("marketing_consent_no_button")
    
    def click_about_tab(self):
        self.driver.click("about_module")

    def click_about_tab_id(self):
        self.driver.click("about_tab")

    def verify_about_privacyPolicy_link(self):
        return self.driver.wait_for_object("about_privacyPolicy").get_attribute("Name")
    
    def verify_about_userLicenceAgreement_link(self):
        return self.driver.wait_for_object("about_userLicenceAgreement").get_attribute("Name")

   
    def verify_about_myHPtext(self):
        return self.driver.wait_for_object("about_myHPtext").get_attribute("Name")

    def click_privacyink(self):
        self.driver.click("about_privacyPolicy")

    def click_useragreement(self):
         self.driver.click("about_userLicenceAgreement")
         
    
    def verify_privacy_title(self):
        return self.driver.wait_for_object("privacy_consent_title").get_attribute("Name")

    def click_privacy_title(self):
        self.driver.click("privacy_consent_title")
    
    def click_notification_module(self):
        self.driver.click("notification_module")

    def click_device_and_account(self):
        self.driver.click("device_and_account_btn")

    def click_tips_and_tutorials(self):
        self.driver.click("tips_and_tutorials_btn")

    def click_news_and_offers(self):
        self.driver.click("news_and_offers_btn")

    def click_share_your_feedback(self):
        self.driver.click("share_your_feedback_btn")
    
    def verify_device_and_account_state(self):
        return self.driver.wait_for_object("device_and_account_btn").get_attribute("Toggle.ToggleState")
    
    def verify_tips_and_tutorials(self):
        return self.driver.wait_for_object("tips_and_tutorials_btn").get_attribute("Toggle.ToggleState")

    def verify_news_and_offers(self):
        return self.driver.wait_for_object("news_and_offers_btn").get_attribute("Toggle.ToggleState")

    def verify_share_your_feedback(self):
        return self.driver.wait_for_object("share_your_feedback_btn").get_attribute("Toggle.ToggleState")

    def click_hp_privacy_settings(self):
        self.driver.wait_for_object("hp_privacy_settings", clickable=True).click()
          
    def verify_hp_system_link(self):
        return self.driver.wait_for_object("click_hp_system_information_data_collection_link").get_attribute("Name")
               
    def click_hp_system_info_sys_data_collection_url(self):
        self.driver.click("click_hp_system_information_data_collection_link")
    
    def verify_privacy_tab(self):
        return self.driver.wait_for_object("privacy_tab") is not False
    
    def click_privacy_tab(self):
        self.driver.click("privacy_tab")
    
    def verify_notfications_tab(self):
        return self.driver.wait_for_object("notification_tab") is not False
    
    def verify_about_tab(self):
        return self.driver.wait_for_object("about_tab") is not False
    
    def verify_click_here_link_show(self):
        return self.driver.wait_for_object("hp_privacy_settings") is not False

    def verify_system_info_link_show(self):
        return self.driver.wait_for_object("click_hp_system_information_data_collection_link") is not False
    
    def get_about_text(self):
        return self.driver.wait_for_object("about_tab").get_attribute("Name")
    
    def get_privacyPolicy_text(self):
        return self.driver.wait_for_object("about_privacyPolicy").get_attribute("Name")
    
    def get_user_agreement_text(self):
        return self.driver.wait_for_object("about_userLicenceAgreement").get_attribute("Name")

    def get_notification_text(self):
        return self.driver.wait_for_object("notification_tab").text
    
    def get_privacy_text(self):
        return self.driver.wait_for_object("privacy_tab").get_attribute("Name")
    
    def get_privacyReviewPolicy_text(self):
        return self.driver.wait_for_object("privacy_review_policy").get_attribute("Name")
    
    def get_theFeature_text(self):
        return self.driver.wait_for_object("privacy_long_text").get_attribute("Name")
    
    def get_hpSystemLink_text(self):
        return self.driver.wait_for_object("hp_system_link").get_attribute("Name")
    
    def get_hpPrivacySetting_text(self):
        return self.driver.wait_for_object("hp_privacy_settings").get_attribute("Name")
    
    def click_no_to_all(self):
        el = self.driver.find_object("privacy_consent_no_to_all")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def verify_no_to_all_btn(self):
        return self.driver.wait_for_object("privacy_consent_no_to_all") is not False

    def verify_yes_to_all_btn(self):
        return self.driver.wait_for_object("privacy_consent_yes_to_all") is not False

    def click_error_ok_button(self):
        self.driver.click("error_ok_button")

    def verify_privacy_tab_visible(self):
        return self.driver.wait_for_object("privacy_tab", raise_e=False, timeout=5)

    def get_detail_text(self):
        return self.driver.wait_for_object("privacy_detail_text").get_attribute("Name")
    
    def get_copr_right_txt_about(self):
        return self.driver.get_attribute("copr_right_txt_about","Name")
    
    def get_version_about(self):
        return self.driver.get_attribute("version_about","Name")
    
    def get_manage_notifications(self):
        return self.driver.get_attribute("manage_notifications","Name")
    
    def get_privacy_setting(self):
        return self.driver.get_attribute("privacy_setting","Name")
    
    def verify_version_about_show(self):
        return self.driver.wait_for_object("version_about", raise_e=False, timeout=5)

    def get_hpPrivacyStatementLink_text(self):
        return self.driver.get_attribute("hp_privacy_statement_text","Name")

    def get_learn_more_go_text(self):
        return self.driver.get_attribute("to_learn_text","Name")
    
    def get_modify_notification(self):
        return self.driver.get_attribute("modify_notification","Name")

    def get_desktop_notification(self):
        return self.driver.get_attribute("desktop_notification","Name")
    
    def get_device_account_title(self):
        return self.driver.get_attribute("device_account_title","Name")

    def get_device_account_description(self):
        return self.driver.get_attribute("update_support","Name")

    def get_tips_tutorial_title(self):
        return self.driver.get_attribute("tips_tutorial","Name")

    def get_tips_tutorial_description(self):
        return self.driver.get_attribute("tips_tutorial_description","Name")

    def get_news_offers_title(self):
        return self.driver.get_attribute("news_and_offers_title","Name")

    def get_news_offers_description(self):
        return self.driver.get_attribute("news_and_offers_description","Name")

    def get_share_feedback_title(self):
        return self.driver.get_attribute("share_your_feedback_title","Name")

    def get_share_feedback_description(self):
        return self.driver.get_attribute("share_your_feedback_description","Name")
    
    def click_privacy_clicked_btn(self):
        self.driver.click("privacy_clicked_btn")

    def verify_warranty_consent_yes(self):
        return self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
    
    def verify_sysinfo_consent_yes(self):
        return self.driver.wait_for_object("sysinfo_consent_yes_button").get_attribute("SelectionItem.IsSelected")
    
    def verify_marketing_consent_yes(self):
        return self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")

    def click_feedback_tab(self):
        self.driver.click("feedback_tab")
    
    def get_feedback_tab(self):
        return self.driver.get_attribute("feedback_tab","Name")
    
    def get_feedback_title(self):
        return self.driver.get_attribute("feedback_title","Name")
    
    def get_feedback_description(self):
        return self.driver.get_attribute("feedback_description","Name")
    
    def get_rating_experience(self):
        return self.driver.get_attribute("rating_experience","Name")
    
    def click_rating_star_1(self):
        self.driver.click("rating_star_1")

    def click_rating_star_2(self):
        self.driver.click("rating_star_2")

    def click_rating_star_3(self):
        self.driver.click("rating_star_3")

    def click_rating_star_4(self):
        self.driver.click("rating_star_4")

    def click_rating_star_5(self):
        self.driver.click("rating_star_5")
    
    def get_rating_disclaimer(self):
        return self.driver.get_attribute("rating_disclaimer","Name")
    
    def get_additional_feedback(self):
        return self.driver.get_attribute("additional_feedback","Name")
    
    def get_feedback_disclaimer(self):
        return self.driver.get_attribute("feedback_disclaimer","Name")
    
    def get_submit_feedback(self):
        return self.driver.get_attribute("submit_feedback","Name")
    
    def click_submit_feedback(self):
        self.driver.click("submit_feedback")
    
    def get_required_field_error(self):
        return self.driver.get_attribute("required_field_error","Name")
    
    def get_character_limit_error(self):
        return self.driver.get_attribute("character_limit_error","Name")
    
    def get_feedback_thankyou(self):
        return self.driver.get_attribute("feedback_thankyou","Name")
    
    def get_feedback_thankyou_disclaimer(self):
        return self.driver.get_attribute("feedback_thankyou_disclaimer","Name")
    
    def click_feedback_thankyou_close(self):
        self.driver.click("feedback_thankyou_close")
    
    def click_click_here_link(self):
        self.driver.click("click_here_link")

    def verify_menu_back_btn_from_settings(self):
        self.driver.wait_for_object("menu_back_btn_from_settings")

    def verify_settings_title(self):
        self.driver.wait_for_object("settings_title")

    def verify_manage_privacy_preferences(self):
        self.driver.wait_for_object("manage_privacy_preferences")

    def verify_privacy_statement_link(self):
        self.driver.wait_for_object("privacy_statement_link")

    def verify_about_title(self):
        self.driver.wait_for_object("about_title")

    def verify_version(self):
        self.driver.wait_for_object("version")

    def verify_about_userLicenceAgreement(self):
        self.driver.wait_for_object("about_userLicenceAgreement")

    def verify_terms_of_use(self):
        self.driver.wait_for_object('terms_of_use_link')

    def verify_privacy_statement_link_tab_name(self):
        return self.driver.get_attribute("privacy_statement_link_tab_name", "Name")

    def verify_terms_of_use_link_tab_name(self):
        return self.driver.get_attribute("terms_of_use_link_tab_name", "Name")

##################################### click actions #####################################

    def click_menu_back_btn_from_settings(self):
        self.driver.click("menu_back_btn_from_settings")

    def click_manage_privacy_preferences(self):
        self.driver.click("manage_privacy_preferences")

    def click_privacy_statement_link(self):
        self.driver.click("privacy_statement_link")

    def click_about_userLicenceAgreement(self):
        self.driver.click("about_userLicenceAgreement")

    def click_terms_of_use(self):
        self.driver.click("terms_of_use_link")

    def verify_settings_page_side_panel(self):
        self.driver.wait_for_object("settings_page")
        self.driver.wait_for_object("privacy_statement")
        self.driver.wait_for_object("manage_privacy_preferences")
        self.verify_version_about_show()
        self.driver.wait_for_object("about_userLicenceAgreement")

    def click_settings_option_from_home(self):
        self.driver.wait_for_object("settings_btn_home").click()