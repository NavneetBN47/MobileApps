from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from MobileApps.resources.const.web.const import WEX_URLS
import logging
import time
from datetime import datetime
from datetime import datetime, timedelta
from time import sleep

class PoliciesTableEmpty(Exception):
    pass

class CannotFindPolicySettingsTypeException(Exception):
    pass

class CannotFindPolicyException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class PolicySearchException(Exception):
    pass

class WrongToastException(Exception):
    pass

class SettingNotFoundException(Exception):
    pass

class Policies(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "fleet_management_policies"

    ############################# Main Menu verifys #############################

    def verify_fleet_management_breadcrumb(self):
        self.driver.verify_object_string("fleet_management_breadcrumb",timeout=30)

    def click_fleet_management_breadcrumb(self):
        return self.driver.click("fleet_management_breadcrumb",timeout=30)

    def click_remediations_policies_printers_tab(self):
        return self.driver.click("remediations_policies_printers_tab", timeout=30)

    def verify_remediations_printer_policies_tab(self):
        return self.driver.verify_object_string("remediations_printer_policies_button",timeout=30)
    
    def verify_remediations_printer_assignments_tab(self):
        return self.driver.verify_object_string("remediations_printer_assignments_button",timeout=30)
    
    def click_remediations_printer_policies_button(self):
        return self.driver.click("remediations_printer_policies_button",timeout=30)
    
    def click_remediations_printer_assignments_button(self):
        return self.driver.click("remediations_printer_assignments_button",timeout=30)

    def verify_fleet_management_policies_printers_button(self):
        return self.driver.wait_for_object("fleet_management_policies_printers_button")

    def click_fleet_management_policies_printers_button(self):
        return self.driver.click("fleet_management_policies_printers_button", timeout=20)

    def verify_fleet_management_policies_breadcrumb(self):
        return self.driver.verify_object_string("fleet_management_policies_breadcrumb")
    
    def verify_printers_policies_policies_tab(self):
        return self.driver.verify_object_string("printers_policies_policies_tab")
    
    def verify_printers_policies_assignments_tab(self):
        return self.driver.verify_object_string("printers_policies_assignments_tab")

    def verify_printers_policies_devices_tab(self):
        return self.driver.verify_object_string("printers_policies_devices_tab")

    def click_fleet_management_policies_breadcrumb(self):
        return self.driver.click("fleet_management_policies_breadcrumb")
    
    def verify_fleet_management_policy_details_policies_breadcrumb(self):
        return self.driver.verify_object_string("fleet_management_policy_details_policies_breadcrumb")

    def click_fleet_management_policy_details_policies_breadcrumb(self):
        return self.driver.click("fleet_management_policy_details_policies_breadcrumb")

    def click_fleet_management_policy_policy_details_breadcrumb(self):
        return self.driver.click("fleet_management_policy_policy_details_breadcrumb")

    def verify_fleet_management_policy_policy_details_breadcrumb(self):
        return self.driver.verify_object_string("fleet_management_policy_policy_details_breadcrumb",timeout=30)

    def verify_policies_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/remediations/printer-policies"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    ########################## Policies page UI ###############################

    def verify_policies_tab_table_data_load(self):
        # It verifies policies table is loaded and has lists of policies.
        if self.driver.wait_for_object("policies_tab_table_checkbox", timeout=30, raise_e=False):
            return True
        else:
            self.verify_policies_table_is_empty_msg()
            raise PoliciesTableEmpty("Policies table is empty")
        
    def verify_policies_table_is_empty_msg(self):
        return self.driver.wait_for_object("policies_table_no_item_found")    

    def verify_policies_tab_search_textbox(self):
        return self.driver.wait_for_object("policies_tab_search_textbox")

    def verify_policies_tab_import_button(self):
        return self.driver.wait_for_object("policies_tab_import_button")
    
    def verify_policies_tab_create_button(self):
        return self.driver.wait_for_object("policies_tab_create_button")

    def verify_policies_tab_column_option_gear_btn(self):
        return self.driver.wait_for_object("policies_tab_column_option_gear_btn")

    def verify_policies_table_headers(self):
        policies_table_headers = []
        headers = self.driver.find_object("policies_table_headers", multiple = True)
        for header in headers:
            table_headers = header.text.split("\n")[0]
            policies_table_headers.append(table_headers)
        # headers = policies_table_headers[1:]
        return policies_table_headers

    ######################### Column Option Popup UI ############################

    def click_policies_tab_column_option_gear_btn(self):
        return self.driver.click("policies_tab_column_option_gear_btn", timeout=30)

    def verify_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title", timeout=20)

    def get_column_options_popup_options(self):
        actual_options = []
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options

    def verify_column_options_popup_reset_to_default_button(self):
        return self.driver.verify_object_string("column_options_popup_reset_to_default_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def click_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "Policy Name":
            options[0].click()
        elif option == "Status":
            options[1].click()
        elif option == "Assigned to":
            options[2].click()
        elif option == "Category":
            options[3].click()
        elif option == "Modified by":
            options[4].click()
        elif option == "Last modified":
            options[5].click()

    def verify_policies_table_column(self,column_name,displayed=True):
        if column_name == "Category":
                return self.driver.wait_for_object("policies_table_catagory_column", invisible=not displayed, timeout=30)
        elif column_name == "Modified by":
                return self.driver.wait_for_object("policies_table_modifiedby_column", invisible=not displayed, timeout=30)
        elif column_name == "Last modified":
                return self.driver.wait_for_object("policies_table_last_modified_column", invisible=not displayed, timeout=30)

    ######################## Contextual Footer Ui ##################################

    def click_policy_checkbox(self):
        return self.driver.click("policies_table_checkbox",timeout=20)

    def verify_contextual_footer(self,displayed=True):
        return self.driver.wait_for_object("policies_contextual_footer", invisible=not displayed)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("policies_contextual_footer_cancel_button")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.wait_for_object("policies_item_selected_label")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("policies_contextual_footer_select_action_dropdown",timeout=30)

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("policies_contextual_footer_continue_button")

    def click_contextual_footer_select_action_dropdown(self):
        self.verify_contextual_footer_select_action_dropdown()
        return self.driver.click("policies_contextual_footer_select_action_dropdown", timeout=30)

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("policies_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("policies_contextual_footer_cancel_button")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("policies_contextual_footer_continue_button")

    ######################## Verifying toast message ##################################

    def check_toast_successful_message(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message",timeout=30).text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)

    ######################## Creating Policy ######################################

    def verify_create_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("create_policy_title", invisible=not displayed, timeout=30)
    
    def verify_create_policy_popup_title(self):
        return self.driver.verify_object_string("create_policy_title", timeout=30)

    def verify_basic_info_screen_step_title(self):
        return self.driver.verify_object_string("create_policy_basic_info_step_title")
    
    def verify_basic_info_screen_step_description(self):
        return self.driver.verify_object_string("create_policy_basic_info_step_description")

    def verify_basic_info_screen_policy_name_field(self):
        return self.driver.wait_for_object("create_policy_policy_name_txt")

    def verify_basic_info_screen_policy_settings_type_dropdown(self):
        return self.driver.wait_for_object("create_policy_policy_setting_type_dropdown",timeout=20)
    
    def verify_basic_info_screen_policy_name_field_error_msg(self):
        self.click_create_policy_next_button()
        return self.driver.verify_object_string("create_policy_basic_info_policy_error_msg")

    def verify_basic_info_screen_policy_settings_type_error_msg(self):
        return self.driver.verify_object_string("create_policy_basic_info_policy_settings_type_error_msg")

    def verify_basic_info_screen_note_field(self):
        return self.driver.wait_for_object("create_policy_basic_info_note_field") 

    def verify_create_policy_next_button_status(self,status):
        save_button=self.driver.wait_for_object("create_policy_next_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True 
    
    def verify_create_policy_cancel_button(self):
        return self.driver.verify_object_string("create_policy_cancel_btn")

    def click_create_policy_cancel_button(self):
        return self.driver.click("create_policy_cancel_btn")

    def verify_create_policy_step2_title(self):
        return self.driver.verify_object_string("create_policy_step2_title")

    def verify_create_policy_step2_description(self):
        return self.driver.verify_object_string("create_policy_step2_desc")

    def verify_create_policy_step2_related_items(self):
        return self.driver.wait_for_object("add_policy_related_item")

    def verify_create_policy_step3_title(self):
        return self.driver.verify_object_string("create_policy_step3_title")
    
    def verify_create_policy_step3_description(self):
        return self.driver.verify_object_string("create_policy_step3_desc")

    def verify_create_policy_back_button(self):
        return self.driver.verify_object_string("create_policy_back_button")

    def verify_create_policy_create_button(self):
        return self.driver.verify_object_string("create_policy_create_button")

    def click_create_policy_button(self):
        return self.driver.click("policies_create_btn",timeout=20)
    
    def enter_policy_name(self,policy_name):
        self.driver.wait_for_object("create_policy_policy_name_txt", timeout=30)
        return self.driver.send_keys("create_policy_policy_name_txt",policy_name)

    def select_policy_settings_type(self,setting_type):
        self.driver.wait_for_object("create_policy_policy_setting_type_dropdown", timeout=20)
        self.driver.click("create_policy_policy_setting_type_dropdown")
        sleep(5)  # Wait for the dropdown options to load
 
        # Loop to ensure dropdown options are visible
        for _ in range(3):  # Retry up to 3 times
            all_options = self.driver.find_object("create_policy_policy_setting_type_dropdown_options", multiple=True, raise_e=False)
            if all_options:
                break
            sleep(5)  # Wait for 3 seconds before retrying
            self.driver.click("create_policy_policy_setting_type_dropdown")  # Click dropdown again to retry
       
        for option in all_options:
            if setting_type == option.text:
                return option.click()
        raise CannotFindPolicySettingsTypeException("Cannot find policy settings type: " + setting_type)  

    def click_create_policy_next_button(self):
        sleep(5)  # Wait for 5 seconds to ensure the button is clickable
        return self.driver.click("create_policy_next_btn",timeout=30)
    
    def search_create_policy_settings(self,setting_name):
        self.driver.wait_for_object("create_policy_search_txt", timeout=30)
        return self.driver.send_keys("create_policy_search_txt",setting_name)

    def click_select_policy_settings_checkbox(self):
        return self.driver.click("create_policy_settings_checkbox",timeout=30)
    
    def click_create_policy_create_button(self):
        return self.driver.click("create_policy_create_button")

    def get_policy_accordion_settings(self):
        settings = []
        all_settings = self.driver.find_object("policy_accordion_settings",multiple=True)
        for setting in all_settings:
            settings.append(setting.text)
        return settings

    def click_create_policy_confirm_button(self):
        #For some settings confirm button is coming before done button, so to handle this below click is used.
        return self.driver.click("change_not_recommended_popup_confirm_button", timeout=10, raise_e=False)

    def create_policy(self,policy_name,policy_settings=None):
        self.click_create_policy_button()
        sleep(5) # To wait for the policy settings to load
        # self.click_create_policy_next_button()
        self.enter_policy_name(policy_name)
        self.select_policy_settings_type(setting_type="Skip Template")
        self.click_create_policy_next_button()
        sleep(5)
        if policy_settings != None:
            self.search_create_policy_settings(policy_settings)
        sleep(5)  # Wait for the search results to load
        self.click_select_policy_settings_checkbox()
        self.click_create_policy_next_button()
        self.click_create_policy_create_button()
        self.click_create_policy_confirm_button()
        self.click_create_policy_done_button()
    
    ######################## Policy Created Successfully Popup ####################

    def verify_policy_created_successfully_popup_title(self):
        return self.driver.verify_object_string("policy_created_successfully_popup_title", timeout=30)

    def verify_policy_created_successfully_popup_description(self):
        return self.driver.verify_object_string("policy_created_successfully_popup_desc")

    def verify_policy_created_successfully_popup_policy_name(self,policy_name):
        self.driver.verify_object_string("policy_created_successfully_popup_policy_name_label",timeout=30)
        assert policy_name == self.driver.wait_for_object("policy_created_successfully_popup_policy_name").text

    def verify_policy_created_successfully_popup_done_button(self):
        return self.driver.verify_object_string("create_policy_done_button",timeout=30)

    def click_create_policy_done_button(self):
        return self.driver.click("create_policy_done_button",timeout=40)

    ########################## Operation Failed Popup ##############################

    def verify_operation_failed_popup(self,displayed=True):
        return self.driver.wait_for_object("operation_failed_popup_title", invisible=not displayed, timeout=30)

    def verify_operation_failed_popup_title(self):
        return self.driver.verify_object_string("operation_failed_popup_title", timeout=30)

    def verify_operation_failed_popup_description(self):
        return self.driver.verify_object_string("operation_failed_popup_desc")

    def verify_operation_failed_popup_ok_button(self):
        return self.driver.wait_for_object("operation_failed_popup_ok_button")

    def click_operation_failed_popup_ok_button(self):
        return self.driver.click("operation_failed_popup_ok_button")

    ######################## Policy Details Page - General Details ####################

    def verify_policy_details_page_policy_detail_breadcrumb(self):
        self.driver.verify_object_string("policy_details_page_policy_detail_breadcrumb")

    def verify_policies_details_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/remediations/printer-policies/" + self.get_policy_id()
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def get_policy_id(self):
        full_url = self.driver.get_current_url()
        policy_id = full_url.split("printer-policies/")[1]
        return policy_id

    def get_edit_policy_id(self):
        full_url = self.driver.get_current_url()
        policy_id = full_url.split("edit/")[1]
        return policy_id

    def verify_policy_details_card(self,expanded=True):
        self.driver.wait_for_object("policy_details_card")
        is_expanded = self.driver.get_attribute("policy_details_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_policy_details_card(self):
        return self.driver.click("policy_details_card")

    def verify_policy_details_card_policy_name(self,policy_name):
        assert policy_name == self.driver.wait_for_object("policy_details_card_policy_name").text

    def verify_policy_details_card_edit_button(self):
        return self.driver.verify_object_string("policy_details_card_edit_btn")

    def click_policy_details_card_more_button(self):
        return self.driver.click("policy_details_card_more_btn",timeout=10)

    def verify_policy_details_card_remove_option(self):
        return self.driver.wait_for_object("policy_details_card_remove_option")

    def click_policy_details_card_remove_option(self):
        return self.driver.click("policy_details_card_remove_option")
    
    #################### Verify Policy in Policies Table ############################

    def search_policy(self, search_text):
        self.driver.wait_for_object("policy_search_field", timeout=30)
        self.driver.clear_text("policy_search_field")
        return self.driver.send_keys("policy_search_field", search_text)

    def verify_table_policy(self, search_text, search_column, policy_search=False, policy_status=None):
        self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        if policy_search:
            self.search_policy(search_text)
    
        search_column_index = self.get_header_index(search_column)
        print(search_column_index)
        search_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[search_column_index], multiple=True)
    
        if policy_status is not None:
            policy_status_column = self.get_header_index("policy_status")
            policy_status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_status_column], multiple=True)
    
        for index in range(len(search_list)):
            if search_text.lower() in search_list[index].text.lower():  # Changed to partial match
                if policy_status is not None and policy_status.lower() != policy_status_list[index].text.lower():
                    return False
                else:
                    return True
        raise CannotFindPolicyException(f"Cannot find policy_search: {search_text}")

    def verify_table_policy_by_name(self, policy_name, policy_search=False, policy_status=None):
        return self.verify_table_policy(policy_name, "policy_name", policy_search, policy_status)

    def verify_table_policy_by_status(self, status, status_search=False, policy_status=None):
        return self.verify_table_policy(status, "status", status_search, policy_status)

    def verify_table_policy_by_category(self, category, category_search=False, policy_status=None):
        return self.verify_table_policy(category, "category", category_search, policy_status)
    
    def verify_table_policy_by_modified_by(self, modified_by, modified_by_search=False, policy_status=None):
        return self.verify_table_policy(modified_by, "modified_by", modified_by_search, policy_status)
    
    def click_policy_save_button(self):
        return self.driver.click("edit_policy_save_button")

    def click_confirm_policy_save_button(self):
        return self.driver.click("confirm_policy_save_button")

    def update_policy_name(self,policy_name):
        self.driver.wait_for_object("edit_policy_policy_name_txt",timeout=30)
        self.driver.clear_text("edit_policy_policy_name_txt")
        return self.driver.send_keys("edit_policy_policy_name_txt", policy_name)

    def get_policy_status(self):
        return self.driver.wait_for_object("policies_status").text

    def get_policies_assigned_group_name(self):
        return self.driver.wait_for_object("policies_assigned_group_name").text

    def get_all_policy_names(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        policy_names.sort()
        return policy_names

    def get_all_policy_table_policy_names(self):
        return self.get_policies_column_data("policy_name")
    
    def get_all_status(self):
        return self.get_policies_column_data("policy_status")
    
    def get_all_modified_by(self):
        return self.get_policies_column_data("modified_by")
    
    def get_all_last_modified(self):
        return self.get_policies_column_data("last_modified")
    
    def get_policies_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        table_entry_data = self.driver.find_object("policies_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]
    
     ############################# Edit Policy Popup ################################

    def verify_edit_policies_page_breadcrumb(self):
        return self.driver.verify_object_string("edit_policies_page_breadcrumb")

    def verify_edit_policies_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/remediations/printer-policies/edit/" + self.get_edit_policy_id()
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def click_policy_details_card_edit_button(self):
        self.verify_policy_details_card_edit_button()
        sleep(3)
        return self.driver.click("policy_details_card_edit_btn", timeout=50)

    def verify_edit_policy_policy_name_text_field(self):
        return self.driver.wait_for_object("edit_policy_policy_name_txt")

    def verify_edit_policy_note_text_field(self):
        return self.driver.wait_for_object("edit_policy_note_txt")

    def verify_edit_policy_search_box(self):
        return self.driver.wait_for_object("policy_details_search_txt")

    def verify_edit_policy_add_button(self):
        return self.driver.verify_object_string("edit_policy_add_button")

    def verify_are_you_sure_to_save_this_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("policy_save_confirm_popup", invisible=not displayed)

    def verify_are_you_sure_to_save_this_policy_popup_description(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_desc")

    def verify_are_you_sure_to_save_this_policy_popup_policy_name(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_policy_name", timeout=30)

    def verify_are_you_sure_to_save_this_policy_popup_policy_name_value(self,policy_name):
        assert policy_name == self.driver.wait_for_object("policy_save_confirm_popup_policy_name_value").text

    def verify_are_you_sure_to_save_this_policy_popup_cancel_button(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_cancel_button")

    def verify_are_you_sure_to_save_this_policy_popup_save_button(self):
        return self.driver.verify_object_string("confirm_policy_save_button")

    def click_are_you_sure_to_save_this_policy_popup_cancel_button(self):
        return self.driver.click("policy_save_confirm_popup_cancel_button")

    ########################### Settings Not Saved Pop-up ###########################

    def verify_settings_not_saved_popup(self,displayed=True):
        return self.driver.wait_for_object("settings_not_saved_title", invisible=not displayed, timeout=30)

    def verify_settings_not_saved_popup_title(self):
        return self.driver.verify_object_string("settings_not_saved_title")

    def verify_settings_not_saved_popup_desc(self):
        self.driver.verify_object_string("settings_not_saved_desc_one")
        return self.driver.verify_object_string("settings_not_saved_desc_two")

    def verify_settings_not_saved_popup_cancel_button(self):
        return self.driver.verify_object_string("settings_not_saved_cancel_btn")

    def click_settings_not_saved_popup_cancel_button(self):
        return self.driver.click("settings_not_saved_cancel_btn")

    def verify_settings_not_saved_popup_leave_button(self):
        return self.driver.verify_object_string("settings_not_saved_leave_btn")

    def click_settings_not_saved_popup_leave_button(self):
        return self.driver.click("settings_not_saved_leave_btn")
    
    def get_updated_policy_name(self):
        return self.driver.get_text("create_policy_policy_name_txt")

    def verify_contextual_footer_save_button(self):
        return self.driver.wait_for_object("edit_policy_save_button")

    ############################# Add Policy Popup ###################################

    def verify_add_policy_pop_up(self,displayed=True):
        return self.driver.wait_for_object("add_policy_pop_up_title", invisible=not displayed)

    def verify_add_policy_pop_up_title(self):
        return self.driver.verify_object_string("add_policy_pop_up_title")

    def verify_add_policy_related_items(self):
        return self.driver.wait_for_object("add_policy_related_item")
    
    def verify_add_policy_cancel_button(self):
        return self.driver.verify_object_string("add_policy_popup_cancel_button")

    def verify_add_policy_add_button(self):
        return self.driver.verify_object_string("add_policy_popup_add_button")

    def verify_add_policy_popup_search_funtionality(self,settings_name):
        self.driver.send_keys("add_policy_popup_search_txt", settings_name)
        sleep(5)
        search_result = self.driver.find_object("add_policy_search_policy_setting_names",multiple=True)
        for i in range(len(search_result)):
            if settings_name in search_result[i].text.replace("&nbsp;"," "):
                logging.info("Policy Settings: " + search_result[i].text.replace("&nbsp;"," ") + " contains the searched string: " + settings_name)
                break
            else:
                raise CannotFindPolicyException("Policy Settings: " + search_result[i].text.replace("&nbsp;","") + " does not contain the searched string: " + settings_name)
        return True
    
    def click_add_policy_popup_cancel_button(self):
        return self.driver.click("add_policies_popup_cancel_button")

    def click_edit_policy_add_button(self):
        return self.driver.click("edit_policy_add_button")

    def search_policy_settings_in_add_policy_popup(self,policy_setting):
        return self.driver.send_keys("add_policy_popup_search_txt", policy_setting)
        
    def click_add_policy_checkbox(self):
        return self.driver.click("add_policy_popup_policy_checkbox")

    def click_add_policy_popup_add_button(self):
        return self.driver.click("add_policy_popup_add_button")

    def get_policy_settings_count(self):
        self.driver.wait_for_object("policies_details_settings_names",timeout=10)
        all_settings = self.driver.find_object("policies_details_settings_names",multiple=True)
        return len(all_settings)

    def click_remove_policy_settings_trash_button(self):
        return self.driver.click("edit_policy_settings_trash_button")
    
    def click_edit_policy_screen_add_policy_popup_cancel_button(self):
        return self.driver.click("add_policy_popup_cancel_button")

    def remove_policy(self,policy_name):
        self.search_policy(policy_name)
        self.click_policy_checkbox()
        self.click_contextual_footer_select_action_dropdown()
        self.select_action_dropdown_option("remove")
        self.click_contextual_footer_continue_button()
        self.click_remove_policy_popup_remove_button()
    
    ############################# Change Not Recommended Popup UI ############################

    def verify_change_not_recommended_popup(self,displayed=True):
        return self.driver.wait_for_object("change_not_recommended_popup", invisible=not displayed)

    def verify_change_not_recommended_popup_warning_icon(self):
        return self.driver.wait_for_object("change_not_recommended_popup_warning_icon")

    def verify_change_not_recommended_popup_title(self):
        return self.driver.verify_object_string("change_not_recommended_popup_title")

    def verify_change_not_recommended_popup_desc(self):
        return self.driver.verify_object_string("change_not_recommended_popup_desc")
    
    def verify_change_not_recommended_popup_desc_end_part(self):
        return self.driver.verify_object_string("change_not_recommended_popup_desc_end_part")
    
    def verify_change_not_recommended_popup_cancel_button(self):
        return self.driver.verify_object_string("change_not_recommended_popup_cancel_button")
    
    def click_change_not_recommended_popup_cancel_button(self):
        return self.driver.click("change_not_recommended_popup_cancel_button")
    
    def verify_change_not_recommended_popup_confirm_button(self):
        return self.driver.verify_object_string("change_not_recommended_popup_confirm_button")

    def click_change_not_recommended_popup_confirm_button(self):
        return self.driver.click("change_not_recommended_popup_confirm_button")

    ############################## Policy Details Page - Settings Details ################################

    def get_policy_settings_names(self):
        settings_names = []
        self.click_first_entry_link()
        self.driver.wait_for_object("policies_details_settings_names",timeout=10)
        all_settings = self.driver.find_object("policies_details_settings_names",multiple=True)
        for setting in all_settings:
            settings_names.append(setting.text)
        return settings_names

    def verify_policy_details_policy_settings_search(self,settings_name):
        self.driver.wait_for_object("policy_details_search_txt", timeout=30)
        sleep(5)
        self.driver.send_keys("policy_details_search_txt", settings_name)
        search_result = self.driver.find_object("policies_details_settings_names",multiple=True)
        for i in range(len(search_result)):
            if settings_name in search_result[i].text.replace("&nbsp;"," "):
                logging.info("Policy Settings: " + search_result[i].text.replace("&nbsp;"," ") + " contains the searched string: " + settings_name)
                break
            else:
                raise CannotFindPolicyException("Policy Settings: " + search_result[i].text.replace("&nbsp;","") + " does not contain the searched string: " + settings_name)
        return True
    
    def verify_policy_details_policy_settings_search_txtbox_text(self, category_name):
        return self.driver.wait_for_object("policy_settings_search_box_default_text", format_specifier=[category_name], timeout=30)

    def get_policy_details_policy_settiings_category_options(self):
        options = self.driver.find_object("policy_settings_category_options", multiple=True)
        policy_settings_category_options = [option.text for option in options]
        logging.info(policy_settings_category_options)
        return [option.text for option in options]
      
    def select_policy_details_policy_settiings_category_option(self, option):
        options = self.driver.find_object("policy_settings_category_options", multiple=True)
        for category_option in options:
            if category_option.text == option:
                return category_option.click()
        raise SettingNotFoundException(f"Setting '{option}' not found in the Policy Details page.")        

    def verify_policy_settings_card(self,expanded=False):
        self.driver.wait_for_object("policy_settings_card")
        is_expanded = self.driver.get_attribute("policy_settings_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_policy_settings_card(self):
        return self.driver.click("policy_settings_card")

     ########################################## Assignments Tab ##########################################

    def verify_assignments_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/remediations/policies-assignments"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def verify_assignments_table_loaded(self, table_load=True):
        #Only works with table with a link in it, which is most tables
        #else it verifies no items present message from table 
        if table_load:
            return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        else:
            return self.driver.wait_for_object("no_policy_found_message", timeout=30)

    def verify_no_policy_is_assigned_to_all_groups(self):
        if self.driver.wait_for_object("assignments_table_no_item_found", raise_e=False):
            logging.info("No policy found")
            return True
        else:
            return False
 
    def remove_assigned_policies_from_all_groups(self):
        all_policies = self.driver.find_object("assignments_delete_policy_btn", multiple=True)
        for policy in all_policies:
            policy.click()
       
        self.click_assignments_action_button()
        self.check_toast_successful_message("Policy unassigned successfully.")

    def click_printers_policies_assignments_tab(self):
        return self.driver.click("printers_policies_assignments_tab",timeout=20)

    def verify_assignments_tab_table_headers(self):
        assignments_policy_table_headers = []
        self.driver.wait_for_object("assignments_policy_table_headers", timeout=30)
        headers = self.driver.find_object("assignments_policy_table_headers", multiple=True)
        for header in headers:
            assignments_policy_table_headers.append(header.text)
        return assignments_policy_table_headers
    
    def click_assess_and_remediate_dropdown_option(self,option):
        self.driver.click("assignments_dropdown")
        options = self.driver.find_object("assignments_dropdown_options", multiple = True)
        if option == "Assess and Remediate":
            options[0].click()
        elif option == "Assess Only":
            options[1].click()
    
    def click_assignments_action_button(self):
        return self.driver.click("assignments_action_btn",timeout=5)
    
    def click_assignments_delete_policy_button(self):
        return self.driver.click("assignments_delete_policy_btn",timeout=30)

    def verify_assignments_contextual_footer(self):
        return self.driver.wait_for_object("assignment_contextual_footer",timeout=60)

    def verify_assignments_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("assignment_contextual_footer_cancel_button")

    def verify_assignments_contextual_footer_action_button(self):
        return self.driver.wait_for_object("assignments_action_btn")
    
    def verify_assignments_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("assignment_contextual_footer_cancel_button",invisible=True)
    
    def click_assignments_contextual_footer_cancel_button(self):
        return self.driver.click("assignment_contextual_footer_cancel_button")
    
    def select_assignments_policy_name(self):
        return self.driver.click("assignments_table_policy_name")

    def select_action_dropdown_option(self,option):
        sleep(5)
        return self.driver.click("policies_select_action_dropdown_option",format_specifier=[option])

    def click_remove_policy_popup_remove_button(self):
        return self.driver.click("remove_policy_popup_remove_button",timeout=30)
    
    ############################################## Groups Side Bar ############################################

    def verify_groups_side_bar_expand_btn(self):
        return self.driver.wait_for_object("group_side_bar_expand_btn",timeout=30)

    def click_groups_side_bar_expand_btn(self):
        return self.driver.click("group_side_bar_expand_btn",timeout=30)

    def verify_groups_side_bar_collapse_button_is_displayed(self):
        return self.driver.wait_for_object("group_side_bar_collapse_btn",raise_e=False)
    
    def verify_groups_side_bar_collapse_btn(self):
        return self.driver.wait_for_object("group_side_bar_collapse_btn")  

    def click_groups_side_bar_collapse_btn(self):
        return self.driver.click("group_side_bar_collapse_btn")
    
    def verify_groups_title(self,displayed=True):
        return self.driver.wait_for_object("groups_side_bar_title",invisible=not displayed)
    
    def verify_groups_all_group_title(self):
        return self.driver.verify_object_string("groups_all_group_title")
    
    def verify_groups_all_group_count(self):
        return self.driver.wait_for_object("groups_all_group_count")
    
    def verify_groups_all_group_expand_btn(self):
        return self.driver.wait_for_object("groups_all_group_expand_btn")

    def select_group(self,group_name):
        return self.driver.click("assignments_group_name",format_specifier=[group_name],timeout=30)    

    ##################################### Add Policy Popup ############################################

    def verify_assignments_add_policy_button(self):
        return self.driver.wait_for_object("assignments_add_policy_btn",timeout=30)

    def click_assignments_add_policy_button(self):
        sleep(5)
        return self.driver.click("assignments_add_policy_btn",timeout=30)
    
    def verify_add_policy_popup_title(self):
        return self.driver.verify_object_string("add_policies_popup_title", timeout=20)

    def verify_add_policy_popup_description(self):
        return self.driver.verify_object_string("add_policies_popup_desc")

    def verify_add_policy_popup_search_box(self):
        return self.driver.wait_for_object("policy_search_txt")

    def verify_add_policy_popup_cancel_button(self):
        return self.driver.verify_object_string("add_policies_popup_cancel_button")

    def verify_add_policy_popup_add_button(self):
        return self.driver.verify_object_string("assignments_add_policy_add_btn")

    def verify_add_policy_popup_close_button(self):
        return self.driver.wait_for_object("add_policies_popup_close_button")

    def click_add_policy_popup_close_button(self):
        return self.driver.click("add_policies_popup_close_button")

    def verify_add_policy_popup_add_button_status(self,status):
        save_button=self.driver.wait_for_object("assignments_add_policy_add_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True

    def click_add_policy_popup_cancel_button(self):
        return self.driver.click("add_policies_popup_cancel_button")
    
    def verify_add_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("add_policies_popup_title", invisible=not displayed, timeout=30)
    
    def click_add_policies_checkbox(self):
        return self.driver.click("assignments_add_policy_table_checkbox",timeout=10)
    
    def click_add_policy_button(self):
        return self.driver.click("assignments_add_policy_add_btn",timeout=5)
    
    def search_add_policy(self,policy_name):
        self.driver.wait_for_object("policy_search_txt", timeout=40)
        self.driver.send_keys("policy_search_txt", policy_name)
        sleep(5)
        if self.driver.wait_for_object("policies_table_no_item_found",raise_e=False):
            return False
        else:
            table_entry_policies = self.driver.find_object("add_policies_table_policy_name",multiple=True)
            logging.info("Total policies found: " + str(len(table_entry_policies)))
            for i in range(len(table_entry_policies)):
                logging.info("Policy Name: " + table_entry_policies[i].text)
                if policy_name in table_entry_policies[i].text:
                    logging.info("Policy Name: " + table_entry_policies[i].text + " contains the searched string: " + policy_name)
                    break
                else:
                    raise PolicySearchException("Policy Name: " + table_entry_policies[i].text + " does not contain the searched string: " + policy_name)
            return True

    def get_all_policy_names_from_add_policy_popup(self):
        policy_names = []
        self.driver.wait_for_object("add_policies_popup_policy_name",timeout=30)
        all_policies = self.driver.find_object("add_policies_popup_policy_name",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        policy_names.sort()
        return policy_names

    def get_assignments_policy_preview_name(self):
        return self.driver.wait_for_object("assignments_policy_preview_title",timeout=10).text
    
    def verify_assignments_policy_settings_title(self):
        return self.driver.verify_object_string("assignments_policy_preview_settings_title")

    def verify_assignments_policy_settings_card(self,expanded=False):
        self.driver.wait_for_object("policy_settings_card")
        is_expanded = self.driver.get_attribute("policy_settings_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_assignments_policy_setting_card(self):
        return self.driver.click("policy_settings_card")
    
    def click_assignments_policy_preview_close_button(self):
        return self.driver.click("assignments_policy_preview_close_btn")
    
    ########################################## Chnage Policy Priority Popup ##########################################
    
    def click_change_policy_priority_button(self):
        return self.driver.click("change_policy_priority_button",timeout=20)

    def verify_change_policy_priority_popup_title(self):
        return self.driver.verify_object_string("change_policy_priority_popup_title", timeout=30)

    def verify_change_policy_priority_popup_description(self):
        return self.driver.verify_object_string("change_policy_priority_popup_desc")

    def verify_change_policy_priority_popup_reset_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_reset_btn")

    def verify_change_policy_priority_popup_cancel_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_cancel_btn")

    def verify_change_policy_priority_popup_save_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_save_btn")

    def verify_change_policy_priority_popup_close_button(self):
        return self.driver.wait_for_object("change_policy_priority_popup_close_btn")

    def get_policy_priority(self):
        policy_names = []
        self.driver.wait_for_object("assignment_tab_polices_names",timeout=20)
        all_policies = self.driver.find_object("assignment_tab_polices_names",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        return policy_names

    def click_change_policy_priority_checkbox(self,option=0):
        policy_checkbox = self.driver.find_object("change_policy_priority_checkbox",multiple=True)
        return policy_checkbox[option].click()

    def get_low_priority_policy_name(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        low_priority_policy = policy_names[-1]
        return low_priority_policy
   
    def get_high_priority_policy_name(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        high_priority_policy = policy_names[0]
        return high_priority_policy

    def verify_change_policy_priority_popup_up_arrow_button(self):
        return self.driver.wait_for_object("change_policy_priority_up_arrow")

    def verify_change_policy_priority_popup_down_arrow_button(self):
        return self.driver.wait_for_object("change_policy_priority_down_arrow")

    def click_change_policy_priority_down_arrow(self):
        return self.driver.click("change_policy_priority_down_arrow")

    def click_change_policy_priority_up_arrow(self):
        return self.driver.click("change_policy_priority_up_arrow")

    def click_change_policy_priority_save_button(self):
        return self.driver.click("change_policy_priority_popup_save_btn")

    def click_change_policy_priority_cancel_button(self):
        return self.driver.click("change_policy_priority_popup_cancel_btn")

    def verify_change_policy_priority_popup(self,displayed=True):
        return self.driver.wait_for_object("change_policy_priority_popup_title", invisible=not displayed,timeout=30)

    def click_change_policy_priority_popup_close_button(self):
        return self.driver.click("change_policy_priority_popup_close_btn")

    def verify_policies_last_modified_column_is_sorted(self, date_list, order="ascending"):
        """
        Check if the list is sorted in the specified order.
        
        :param date_list: List of date strings to check.
        :param order: The order to check for. Can be "ascending" or "descending".
        :return: True if sorted in the specified order, False otherwise.
        """

        logging.info(f"Verifying if the list is sorted in {order} order: {date_list}")
        # Convert the date strings to datetime objects
        date_objects = [self.parse_date(date) for date in date_list]
        
        if order == "ascending":
            return all(date_objects[i] <= date_objects[i + 1] for i in range(len(date_objects) - 1))
        elif order == "descending":
            return all(date_objects[i] >= date_objects[i + 1] for i in range(len(date_objects) - 1))
        else:
            raise ValueError("Invalid order specified. Use 'ascending' or 'descending'.")

    def parse_date(self, date_str):
        now = datetime.now()
        original_date_str = date_str  # Keep original for error message
        date_str = date_str.lower().strip()
        
        if "just now" in date_str:
            return now.replace(microsecond=0)
        elif "minute" in date_str:
            minutes = int(date_str.split()[0])
            return (now - timedelta(minutes=minutes)).replace(microsecond=0)
        elif "hour" in date_str:
            hours = int(date_str.split()[0])
            return (now - timedelta(hours=hours)).replace(microsecond=0)
        
        elif "week" in date_str:
            weeks = int(date_str.split()[0])
            return (now - timedelta(weeks=weeks)).replace(microsecond=0)

        elif "yesterday" in date_str:
            return (now - timedelta(days=1)).replace(microsecond=0)
        elif "day" in date_str and "yesterday" not in date_str:
            days = int(date_str.split()[0])
            return (now - timedelta(days=days)).replace(microsecond=0)
        elif "month" in date_str:
            months = int(date_str.split()[0])
            return (now - timedelta(days=months*30)).replace(microsecond=0)

        else:
            # Normalize the input string to capitalize the first letter of the month
            date_str = date_str.capitalize()
            try:
                return datetime.strptime(date_str, "%b %d, %Y").replace(microsecond=0)
            except ValueError:
                try:
                    return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)
                except ValueError:
                    raise ValueError(f"Unable to parse date string: '{original_date_str}'. This might be a table header or invalid date format.")   