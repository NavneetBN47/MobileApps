from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from SAF.decorator.saf_decorator import string_validation
import logging

class UnexpectedItemPresentException(Exception):
    pass

class Account(SMBFlow):

    flow_name = "account"

    ############################ Account Profile ############################

    def click_account_profile_tab(self):
        return self.driver.click("account_profile_tab",timeout=30)

    def verify_account_profile_tab(self):
        return self.driver.wait_for_object("account_profile_tab",timeout=20)

    def click_organization_tab(self):
        return self.driver.click("application_myAccount_profile_organization_tab",timeout=20)

    def click_personal_tab(self):
        return self.driver.click("application_myAccount_profile_personal",timeout=20)

    @string_validation("application_myAccount_profile_organization_tab")
    def verify_organization_tab(self):
        return self.driver.wait_for_object("application_myAccount_profile_organization_tab",timeout=20)

    @string_validation("application_myAccount_profile_personal")
    def verify_personal_tab(self):
        return self.driver.wait_for_object("application_myAccount_profile_personal",timeout=20)

    def verify_uid_is_disabled(self):
        if self.driver.find_object("organization_uid_txt").is_enabled():
            raise UnexpectedItemPresentException(" UID Text Box  is enabled")
        return True

    def verify_uid(self):
        return self.driver.wait_for_object("organization_uid_txt")

    @string_validation("application_myAccount_profile_organization_uid")
    def verify_uid_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_organization_uid")

    def verify_organizations_name(self):
        return self.driver.wait_for_object("organization_name_txt")

    def verify_organization_description(self):
        return self.driver.wait_for_object("organization_description_txt")

    @string_validation("application_myAccount_profile_organization_name")
    def verify_organization_name_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_organization_name")

    @string_validation("application_myAccount_profile_organization_description")
    def verify_organization_desc_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_organization_description")

    def enter_organization_name(self, org_name):
        return self.driver.send_keys("organization_name_txt", org_name)

    def enter_organization_desc(self, org_desc):
        return self.driver.send_keys("organization_description_txt", org_desc)
    
    def get_organization_name(self):
        return self.driver.get_text("organization_name_txt")

    def get_organization_desc(self):
        return self.driver.get_text("organization_description_txt")

    def verify_organization_name(self, org_name):
        self.compare_strings(org_name, self.get_organization_name())

    def verify_organization_desc(self, org_desc):
        self.compare_strings(org_desc, self.get_organization_desc())

    @string_validation("application_myAccount_modal_changeSuccess")
    def verify_toast_notification(self):
        return self.driver.wait_for_object("application_myAccount_modal_changeSuccess")

    def click_apply_button(self):
        return self.driver.click("application_myAccount_profile_button_applyChanges",timeout=20)

    def click_cancel_button(self):
        return self.driver.click("application_myAccount_profile_button_cancel")

    def clear_organization_name(self):
        return self.driver.clear_text("organization_name_txt")

    def verify_apply_button_status(self,status):
        if status == "disabled":
            if self.driver.find_object("application_myAccount_profile_button_applyChanges").is_enabled():
                raise UnexpectedItemPresentException(" Apply button  is enabled")
            return True
        else:
            if self.driver.find_object("application_myAccount_profile_button_applyChanges").is_enabled() is False:
                raise UnexpectedItemPresentException(" Apply button is disabled")
            return True

    def verify_organization_tab_is_not_selected(self):
        is_selected = self.driver.get_attribute("application_myAccount_profile_organization_tab","aria-selected")
        if is_selected == 'true':
            raise UnexpectedItemPresentException("Organization Tab is Seleceted")
        return True

    ##################### Unsaved Changes Pop-Up #######################

    @string_validation("application_myAccount_modal_confirmModalTitle")
    def verify_unsaved_changes_popup_title(self):
        return self.driver.wait_for_object("application_myAccount_modal_confirmModalTitle")

    @string_validation("application_myAccount_modal_toastLeavePage")
    def verify_unsaved_changes_popup_desc(self):
        return self.driver.wait_for_object("application_myAccount_modal_toastLeavePage")
       
    @string_validation("application_myAccount_unsavedChanges_cancel")
    def verify_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("application_myAccount_unsavedChanges_cancel",timeout=30)

    @string_validation("application_myAccount_unsavedChanges_leave")
    def verify_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("application_myAccount_unsavedChanges_leave",timeout=30)

    def click_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("application_myAccount_unsavedChanges_cancel",timeout=30)

    def click_unsaved_changes_popup_leave_button(self):
        return self.driver.click("application_myAccount_unsavedChanges_leave",timeout=30)
    
    ###################### Account Section #######################

    @string_validation("settings_header")
    def verify_account_screen_title(self):
        return self.driver.wait_for_object("settings_header",timeout=30)
    
    @string_validation("settings_body")
    def verify_account_screen_description(self):
        return self.driver.wait_for_object("settings_body")

    @string_validation("settings_accountProfile_header")
    def verify_account_profile_tab_title(self):
        return self.driver.wait_for_object("settings_accountProfile_header",timeout=20)

    @string_validation("settings_accountProfile_body")
    def verify_account_profile_tab_description(self):
        return self.driver.wait_for_object("settings_accountProfile_body")

    def verify_preferences_tab_title(self):
        return self.driver.get_text("preferences_tab_title")

    def verify_preferences_tab_description(self):
        return self.driver.get_text("preferences_tab_title_desc")

    @string_validation("settings_shipping_header")
    def verify_shipping_tab_title(self):
        return self.driver.get_text("settings_shipping_header")
    
    @string_validation("settings_shipping_body")
    def verify_shipping_tab_description(self):
        return self.driver.get_text("settings_shipping_body")
    
    @string_validation("settings_billing_header")
    def verify_billing_tab_title(self):
        return self.driver.get_text("settings_billing_header")
    
    @string_validation("settings_billings_body")
    def verify_billing_tab_description(self):
        return self.driver.get_text("settings_billings_body")

    ###################### Account Profile Personal tab Section #######################

    def enter_first_name(self, first_name):
        self.driver.wait_for_object("profile_first_name_txt_box", timeout=30)
        return self.driver.send_keys("profile_first_name_txt_box", first_name)
    
    def get_first_name(self):
        return self.driver.get_attribute("profile_first_name_txt_box","value")

    def enter_last_name(self, last_name):
        return self.driver.send_keys("profile_last_name_txt_box", last_name)

    def get_last_name(self):
        return self.driver.get_attribute("profile_last_name_txt_box","value")

    def enter_email(self, email):
        return self.driver.send_keys("profile_email_txt_box", email)

    def select_country(self, country):
        self.driver.click("profile_country_dropdown")
        self.driver.wait_for_object("profile_country_option", format_specifier=[country])
        return self.driver.click("profile_country_option", format_specifier=[country])
    
    def enter_phonenumber(self, phonenumber):
        return self.driver.send_keys("profile_phone_txt_box", phonenumber)
    
    def get_phonenumber(self):
        return self.driver.wait_for_object("profile_phone_txt_box").text

    def verify_personal_tab_is_not_selected(self):
        is_selected = self.driver.get_attribute("application_myAccount_profile_personal","aria-selected")
        if is_selected == 'true':
            raise UnexpectedItemPresentException("Personal Tab is Seleceted")
        return True

    ##################### Account Profile Verify all fields #######################

    @string_validation("application_myAccount_profile_mainHeader")
    def verify_account_profile_screen_title(self):
        return self.driver.wait_for_object("application_myAccount_profile_mainHeader",timeout=20)
    
    @string_validation("application_myAccount_profile_description2")
    def verify_account_profile_screen_description(self):
        return self.driver.wait_for_object("application_myAccount_profile_description2")

    def verify_firstname(self):
        return self.driver.wait_for_object("profile_first_name_txt_box", timeout=30)

    @string_validation("application_myAccount_profile_firstName")
    def verify_firstname_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_firstName")

    def verify_lastname(self):
        return self.driver.wait_for_object("profile_last_name_txt_box")

    @string_validation("application_myAccount_profile_familyName")
    def verify_lastname_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_familyName")

    def verify_email(self):
        #verify email is disable
        if self.driver.find_object("profile_email_txt_box").is_enabled():
            raise UnexpectedItemPresentException("Email text box is enabled")
        return True

    @string_validation("application_myAccount_profile_email")    
    def verify_email_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_email")

    def verify_organization_country(self):
        return self.driver.wait_for_object("organization_country_dropdown")

    def verify_organization_country_label(self):
        return self.driver.wait_for_object("organization_country_dropdown_label")

    @string_validation("application_myAccount_profile_phoneNumber")
    def verify_phonenumber_label(self):
        return self.driver.wait_for_object("application_myAccount_profile_phoneNumber")

    @string_validation("application_myAccount_profile_button_applyChanges")
    def verify_apply_changes_button(self):
        return self.driver.wait_for_object("application_myAccount_profile_button_applyChanges")

    def verify_first_name(self, first_name):
        self.compare_strings(first_name, self.get_first_name())

    def verify_last_name(self, last_name):
        self.compare_strings(last_name, self.get_last_name())
        
    def verify_emailID(self, email):
        self.compare_strings(email, self.get_email())

    def verify_phonenumber(self, phonenumber):
        self.compare_strings(phonenumber, self.get_phonenumber())
    
    @string_validation("application_myAccount_profile_constraints_invalidPhoneNumber")
    def verify_phonenumber_field_invalid_error_msg(self):
        return self.driver.wait_for_object("application_myAccount_profile_constraints_invalidPhoneNumber")

    def get_email(self):
        return self.driver.wait_for_object("profile_email_txt_box").text()

 ###################### Account Profile Change Password Functionality #######################
    def click_change_password_link(self):      
        return self.driver.click("application_myAccount_profile_link_changePassword")
    
    @string_validation("application_myAccount_profile_link_changePassword")
    def verify_change_password_link(self):
        return self.driver.wait_for_object("application_myAccount_profile_link_changePassword")

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    ###################### Account Profile Contextual Footer #######################

    def verify_cancel_button_is_not_displayed(self):
        return self.driver.wait_for_object("application_myAccount_profile_button_cancel", invisible=True)

    @string_validation("application_myAccount_profile_button_cancel")
    def verify_cancel_button_is_displayed(self):
        return self.driver.wait_for_object("application_myAccount_profile_button_cancel")
    
    @string_validation("application_myAccount_profile_button_applyChanges")
    def verify_apply_changes_button_is_displayed(self):
        return self.driver.wait_for_object("application_myAccount_profile_button_applyChanges")

    ###################### Account Profile Verify first and last field clear #######################

    def clear_firstname_text(self):
        return self.driver.clear_text("profile_first_name_txt_box")
    
    def clear_lastname_text(self):
        return self.driver.clear_text("profile_last_name_txt_box")

    ############################ Preferences ############################

    def click_preferences_tab(self):
        return self.driver.click("preferences_tab",timeout=30)

    def verify_account_preferences_tab(self):
        return self.driver.wait_for_object("preferences_tab",timeout=30)
    
    def click_preferences_privacy_tab(self):
        return self.driver.click("privacy_tab",timeout=30)
    
    def verify_preferences_privacy_tab(self):
        return self.driver.wait_for_object("privacy_tab",timeout=30)

    def verify_preferences_language_tab(self):
        return self.driver.wait_for_object("language_tab",timeout=30)
    
    def click_preferences_language_tab(self):
        return self.driver.click("language_tab",timeout=30)

    def verify_preferences_notification_tab(self):
        return self.driver.wait_for_object("notifications_tab",timeout=30)
    
    def verify_preferences_notification_tab_displayed(self):
        if self.driver.find_object("notifications_tab", raise_e=False) is not False:
            return True
        else:
            logging.info("Notifcations tab is not available")
            return False
        
    def click_preferences_notifications_tab(self):
        return self.driver.click("notifications_tab",timeout=30)

    ##################### Notification Tab #######################
    @string_validation("settings_preferences_header")
    def verify_preferences_screen_title(self):
        return self.driver.wait_for_object("settings_preferences_header", timeout=20)
    
    @string_validation("settings_preferences_body")
    def verify_preferences_screen_description(self):
        return self.driver.wait_for_object("settings_preferences_body")

    @string_validation("settings_preferences_notifications")
    def verify_notifications_tab_title(self):
        return self.driver.wait_for_object("settings_preferences_notifications")
    
    @string_validation("settings_preferences_privacy")
    def verify_privacy_tab_title(self):
        return self.driver.wait_for_object("settings_preferences_privacy")
        
    @string_validation("settings_preferences_language")
    def verify_language_tab_title(self):
        return self.driver.wait_for_object("settings_preferences_language")

    @string_validation("settings_preferences_notificationPreferences_body")
    def verify_notifications_tab_description(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_body")
    
    @string_validation("settings_preferences_notificationPreferences_printer_title")
    def verify_notification_type_printer_and_service_status(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_printer_title")
    
    @string_validation("settings_preferences_notificationPreferences_billing_title")
    def verify_notification_type_account_and_billing(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_billing_title")
    
    @string_validation("settings_preferences_notificationPreferences_promotions_title")
    def verify_notification_type_promotions(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_promotions_title")

    @string_validation("settings_preferences_notificationPreferences_feature_title")
    def verify_notification_type_feature_awareness(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_feature_title")

    @string_validation("settings_preferences_notificationPreferences_printer_description")
    def verify_notification_type_printer_and_service_status_description(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_printer_description")
    
    @string_validation("settings_preferences_notificationPreferences_billing_description")
    def verify_notification_type_account_and_billing_description(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_billing_description")

    @string_validation("settings_preferences_notificationPreferences_promotions_description")
    def verify_notification_type_promotions_type_description(self):
       return self.driver.wait_for_object("settings_preferences_notificationPreferences_promotions_description")

    @string_validation("settings_preferences_notificationPreferences_feature_description")
    def verify_notification_type_feature_awareness_type_description(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_feature_description")
    
    def click_notification_type_printer_and_service_status_toggle_button(self):
        return self.driver.click("printer_type_toggle",timeout=5)
    
    def click_notification_type_account_and_billing_toggle_button(self):
        return self.driver.click("billing_type_toggle",timeout=5)
    
    def click_notification_type_promotions_toggle_button(self):
        return self.driver.click("promotions_type_toggle",timeout=5)
    
    def click_notification_type_feature_awarenesss_toggle_button(self):
        return self.driver.click("feature_type_toggle",timeout=5)
        
    def get_notification_type_printer_and_service_toggle_button_status(self):
        return self.driver.get_text("printer_type_status")

    @string_validation("settings_preferences_notificationPreferences_toggle_on")
    def verify_notification_type_printer_and_service_toggle_button_on_status(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_toggle_on")

    @string_validation("settings_preferences_notificationPreferences_toggle_off")
    def verify_notification_type_printer_and_service_toggle_button_off_status(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_toggle_off")
    
    def get_notification_type_account_and_billing_toggle_button_status(self):
        return self.driver.get_text("billing_type_status")

    def get_notification_type_promotions_toggle_button_status(self):
        return self.driver.get_text("promotions_type_status")
    
    def get_notification_type_feature_awareness_toggle_button_status(self):
        return self.driver.get_text("feature_type_status")
    
    @string_validation("settings_preferences_notificationPreferences_toast_success")
    def verify_positive_toast_notification(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_toast_success")
    
    @string_validation("settings_preferences_notificationPreferences_toast_error")
    def verify_negative_toast_notification(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_toast_error")

    def get_notifications_table_headers(self):
        notifications_table_headers = []
        headers = self.driver.find_object("notification_table_headers", multiple = True)
        for header in headers:
            notifications_table_headers.append(header.text)
        return notifications_table_headers

    @string_validation("settings_preferences_notificationPreferences_notificationType")
    def verify_notifications_table_header_notification_type(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_notificationType")
            
    @string_validation("settings_preferences_notificationPreferences_email")
    def verify_notifications_table_header_email(self):
        return self.driver.wait_for_object("settings_preferences_notificationPreferences_email")
        
    def verify_learn_more_hyperlink_text(self):
        return self.driver.verify_object_string("privacy_tab_learnmore_hyperlink")

    def click_learn_more_hyperlink(self):
        return self.driver.click("privacy_tab_learnmore_hyperlink",timeout=20)

    def verify_required_label(self):
        return self.driver.wait_for_object("required_label")

    def verify_printer_analytics_label(self):
        return self.driver.wait_for_object("printer_analytics_label")

    def verify_advertising_label(self):
        return self.driver.wait_for_object("advertising_label")

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    def get_required_toggle_button_status(self):
        self.driver.get_attribute("required_toggle_button_status","aria-disabled",timeout=30)
        return self.driver.wait_for_object("required_toggle_button_status").is_enabled()

    def get_printer_analytics_toggle_button_status(self):
        return self.driver.get_attribute("printer_analytics_toggle_button_status","aria-checked",timeout=30)

    def click_printer_analytics_toggle_button(self):
        return self.driver.js_click("printer_analytics_toggle_button_status")

    def get_advertising_toggle_button_status(self):
        return self.driver.get_attribute("advertising_toggle_button_status","aria-checked")

    def click_advertising_toggle_button(self):
        return self.driver.js_click("advertising_toggle_button_status")

    def verify_required_description(self):
        return self.driver.verify_object_string("required_description", timeout=30)

    def verify_printer_analytics_description(self):
        self.driver.verify_object_string("printer_analytics_description_part_1")
        return self.driver.verify_object_string("printer_analytics_description_part_2")

    def verify_advertising_description(self):
        return self.driver.verify_object_string("advertising_description")

    ###########################Language Tab####################################

    @string_validation("settings_preferences_languageSelectDescription")
    def verify_language_tab_description(self):
        return self.driver.wait_for_object("settings_preferences_languageSelectDescription")

    def verify_language_tab_dropdown(self):
        return self.driver.wait_for_object("language_tab_dropdown")

    def click_language_tab_dropdown(self):
        return self.driver.click("language_tab_dropdown")

    def get_all_languages_in_dropdown(self):
        languages = []
        language_list = self.driver.find_object("language_tab_dropdown_option_list", multiple=True)
        for language in language_list:
            languages.append(language.text)
        return languages

    def enter_preferred_language_in_language_dropdown(self, language):
        return self.driver.send_keys("settings_preferences_searchLanguagePlaceholder", language)
    
    def clear_preferred_language_in_language_dropdown(self):
        return self.driver.clear_text("settings_preferences_searchLanguagePlaceholder")

    # @string_validation("settings_preferences_select_showingResult")
    def verify_preferred_language_result_in_language_dropdown(self):
        return self.driver.wait_for_object("settings_preferences_select_showingResult")

    # @string_validation("settings_preferences_select_showingResults")
    def verify_preferred_language_multiple_result_in_language_dropdown(self):
        return self.driver.wait_for_object("settings_preferences_select_showingResults")

    @string_validation("settings_preferences_select_noResults")
    def verify_language_dropdown_no_items_msg(self):
        return self.driver.wait_for_object("settings_preferences_select_noResults")

    def select_preferred_language_in_language_dropdown(self):
        return self.driver.click("language_tab_dropdown_option")

    def get_preferences_screen_title(self):
        self.driver.wait_for_object("settings_preferences_header",timeout=20)
        return self.driver.get_text("settings_preferences_header")

    def click_language_tab_apply_button(self):
        return self.driver.click("settings_preferences_apply",timeout=30)

    def click_language_tab_cancel_button(self):
        return self.driver.click("settings_preferences_cancel")

    @string_validation("settings_preferences_apply")
    def verify_language_tab_apply_button(self):
        return self.driver.wait_for_object("settings_preferences_apply",timeout=30)
    
    @string_validation("settings_preferences_cancel")
    def verify_language_tab_cancel_button(self):
        return self.driver.wait_for_object("settings_preferences_cancel")

    ##################### Preferences- Unsaved Changes Pop-Up #######################

    @string_validation("settings_preferences_unsavedChangesModal_title")
    def verify_preferences_unsaved_changes_popup_title(self):
        return self.driver.wait_for_object("settings_preferences_unsavedChangesModal_title",timeout=30)

    @string_validation("settings_preferences_unsavedChangesModal_body")
    def verify_preferences_unsaved_changes_popup_desc(self):
        return self.driver.wait_for_object("settings_preferences_unsavedChangesModal_body")
       
    def verify_preferences_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("preferences_unsaved_changes_popup_cancel_button",timeout=30)

    def verify_preferences_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("preferences_unsaved_changes_popup_leave_button",timeout=30)

    def click_preferences_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("preferences_unsaved_changes_popup_cancel_button",timeout=30)

    def click_preferences_unsaved_changes_popup_leave_button(self):
        return self.driver.click("preferences_unsaved_changes_popup_leave_button",timeout=30)