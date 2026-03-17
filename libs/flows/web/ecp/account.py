import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class UnexpectedItemPresentException(Exception):
    pass

class Account(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "account"

    ###################### Account Profile Section #######################
    def enter_username(self, username):
        #Currently this box is grayed out, not sure if that'll change in the future
        return self.driver.send_keys("profile_username_txt_box", username)

    def enter_first_name(self, first_name):
        return self.driver.send_keys("profile_first_name_txt_box", first_name)
    
    def get_first_name(self):
        self.driver.wait_for_object("profile_first_name_txt_box")
        return self.driver.get_text("profile_first_name_txt_box")

    def enter_last_name(self, last_name):
        return self.driver.send_keys("profile_last_name_txt_box", last_name)

    def get_last_name(self):
        return self.driver.wait_for_object("profile_last_name_txt_box").text

    def get_last_name(self):
        return self.driver.wait_for_object("profile_last_name_txt_box").text

    def enter_email(self, email):
        return self.driver.send_keys("profile_email_txt_box", email)

    def select_country(self, country):
        self.driver.click("profile_country_dropdown")
        self.driver.wait_for_object("profile_country_option", format_specifier=[country])
        return self.driver.click("profile_country_option", format_specifier=[country])
    
    def select_language(self, language):
        self.driver.click("profile_language_dropdown")
        self.driver.wait_for_object("profile_language_option", format_specifier=[language])
        return self.driver.click("profile_language_option", format_specifier=[language])
    
    def click_apply_changes_button(self):
        return self.driver.click("apply_changes_button")

    ##################### Account Profile Verify all fields #######################
    def verify_account_profile_page(self):
        return self.driver.wait_for_object("profile_first_name_txt_box", timeout=30)

    def verify_account_profile_page_header(self):
        return self.driver.verify_object_string("profile_page_title")
    
    def verify_account_profile_page_header_description(self):
        return self.driver.verify_object_string("profile_title_desc")
            
    def verify_username_disable(self):
        #verify user name is disable
        if self.driver.find_object("profile_username_txt_box").is_enabled():
            raise UnexpectedItemPresentException("username text box is enabled")
        return True

    def verify_username_label(self):
        return self.driver.wait_for_object("profile_username_label")

    def verify_firstname(self):
        return self.driver.wait_for_object("profile_first_name_txt_box")

    def verify_firstname_label(self):
        return self.driver.verify_object_string("profile_firstname_label")

    def verify_lastname(self):
        return self.driver.wait_for_object("profile_last_name_txt_box")

    def verify_lastname_label(self):
        return self.driver.verify_object_string("profile_lastname_label")

    def verify_phone_number(self):
        return self.driver.wait_for_object("profile_phone_number")

    def verify_phone_number_label(self):
        return self.driver.verify_object_string("profile_phone_number_label")

    def verify_email(self):
        return self.driver.wait_for_object("profile_email_txt_box")

    def verify_email_label(self):
        expected_email_label = "Email" 
        if expected_email_label != self.driver.get_text("profile_email_label"):
            self.driver.verify_object_string("profile_email")

    def verify_country(self):
        return self.driver.wait_for_object("profile_country_dropdown")

    def verify_country_label(self):
        return self.driver.verify_object_string("profile_country_label")

    def verify_language(self):
        return self.driver.wait_for_object("profile_language_dropdown")

    def verify_language_label(self):
        expected_text="Select Language"
        actual_text=self.driver.get_text("profile_language_label")
        self.compare_strings(expected_text, actual_text)

    def verify_change_password_link(self):
        return self.driver.wait_for_object("change_password_link")

    def verify_apply_changes_button_disable(self):
        #verify Apply changes button is disable
        if self.driver.find_object("apply_changes_button").is_enabled():
            raise UnexpectedItemPresentException(" Apply changes button is enabled")
        return True

    def verify_apply_changes_button(self):
        return self.driver.wait_for_object("apply_changes_button")

    def verify_first_name(self, first_name):
        self.compare_strings(first_name, self.get_first_name())

    def verify_last_name(self, last_name):
        self.compare_strings(last_name, self.get_last_name())
        
    def verify_emailID(self, email):
        self.compare_strings(email, self.get_email())
    
    def get_email(self):
        return self.driver.get_text("profile_email_txt_box")
    
    def get_last_name(self):
        return self.driver.get_text("profile_last_name_txt_box")


    ###################### Account Profile Verify Cancel Button Functionality #######################

    def verify_cancel_button_is_not_displayed(self):
        return self.driver.wait_for_object("profile_cancel_button", invisible=True)

    def verify_account_profile_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("profile_cancel_button", invisible=True)

    def verify_cancel_button_is_displayed(self):
        return self.driver.wait_for_object("profile_cancel_button")

    def verify_account_profile_contextual_footer_is_displayed(self):
        return self.driver.wait_for_object("profile_cancel_button")

    def click_cancel_button(self):
        return self.driver.click("profile_cancel_button")

    ###################### Account Profile Verify email field error #######################

    def clear_email_text(self):
        self.driver.clear_text("profile_email_txt_box")

    def verify_empty_email_error_message(self):
        expected_empty_email_error_message="Updating your email will not change your username."
        actual_empty_email_error_message=self.driver.get_text("profile_email_error_label")
        self.compare_strings(expected_empty_email_error_message, actual_empty_email_error_message)

    def verify_invalid_email_error_message(self):
        expected_invalid_email_error_message="Invalid email. Enter a valid email address"
        actual_invalid_email_error_message=self.driver.get_text("profile_email_error_label")
        self.compare_strings(expected_invalid_email_error_message, actual_invalid_email_error_message)

    ###################### popup Updating email will not change Username   #######################

    def verify_popup_Updating_email_will_not_change_Username(self):
        return self.driver.wait_for_object("popup_Updating_email_will_not_change_Username")

    def verify_popup_Updating_email_will_not_change_Username_description(self):
        expected_text ="Updating your email will not change your username. Remember to use your Username to sign in to your account."
        actual_text=self.driver.get_text("popup_Updating_email_will_not_change_Username_desc")
        self.compare_strings(expected_text, actual_text)

    def verify_popup_continue_button(self):
        return self.driver.wait_for_object("popup_continue_button")

    def click_popup_continue_button(self):
        return self.driver.click("popup_continue_button")

    def verify_toast_notification(self,raise_e=True):
        return self.driver.verify_object_string("success_alert")
    
    ######################### Organization Information tab ###################################
    def verify_ecp_home_title_bar(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("shell_title_bar", timeout=timeout, raise_e=raise_e)
    
    def click_personal_tab(self):
        return self.driver.click("account_profile_personal_tab",timeout=20)

    def click_organization_tab(self):
        return self.driver.click("account_profile_organization_tab",timeout=20)
    
    def verify_uid_is_disabled(self):
        if self.driver.find_object("organization_uid_txt").is_enabled():
            raise UnexpectedItemPresentException(" UID Text Box  is enabled")
        return True

    def verify_uid(self):
        return self.driver.wait_for_object("organization_uid_lbl")

    def verify_organizations_name(self):
        return self.driver.wait_for_object("organization_name_txt")

    def verify_organization_description(self):
        return self.driver.wait_for_object("organization_description_txt")

    def verify_organization_name_label(self):
        return self.driver.wait_for_object("organization_name_lbl")

    def verify_organization_desc_label(self):
        return self.driver.verify_object_string("organization_description_lbl")

    def enter_organization_name(self, org_name):
        return self.driver.send_keys("organization_name_txt", org_name)
    
    def verify_apply_changes_button_is_displayed(self):
        return self.driver.wait_for_object("apply_changes_button")

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

    def verify_organization_tab_is_not_selected(self):
        is_selected = self.driver.get_attribute("account_profile_organization_tab","aria-selected")
        if is_selected == 'true':
            raise UnexpectedItemPresentException("Organization Tab is Seleceted")
        return True

    def verify_personal_tab_is_not_selected(self):
        is_selected = self.driver.get_attribute("account_profile_personal_tab","aria-selected")
        if is_selected == 'true':
            raise UnexpectedItemPresentException("Personal Tab is Seleceted")
        return True

    # ##################### Unsaved Changes Pop-Up #######################

    def verify_unsaved_changes_popup_title(self):
        return self.driver.verify_object_string("unsaved_changes_popup_title")

    def verify_unsaved_changes_popup_desc(self):
        return self.driver.verify_object_string("unsaved_changes_popup_desc")
       
    def verify_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("unsaved_changes_popup_cancel_button")

    def verify_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("unsaved_changes_popup_leave_button")

    def click_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("unsaved_changes_popup_cancel_button")

    def click_unsaved_changes_popup_leave_button(self):
        return self.driver.click("unsaved_changes_popup_leave_button")

    ##################### Account Screen ###################################

    def verify_account_profile_card(self):
        return self.driver.wait_for_object("account_profile_card",timeout=30)

    def verify_account_profile_card_title(self):
        return self.driver.verify_object_string("account_profile_card_title")
    
    def verify_account_profile_card_description(self):
        return self.driver.verify_object_string("account_profile_card_desc")

    def click_account_profile_card(self):
        return self.driver.click("account_profile_card_chevron")