import logging
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class UserSearchException(Exception):
    pass

class FilterValueException(Exception):
    pass

class MyOrganizationTableEmpty(Exception):
    pass

class WrongToastException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class MyOrganization(ECPFlow):
    """
        Contains all of the elements and flows associated in My Organization for ECP
    """
    flow_name = "my_organization"

    ########################### My Organization Page ###########################

    def click_my_organization_link(self):
        return self.driver.click("avatar_my_organization_link",timeout=15)

    def verify_my_organization_page_title(self):
        return self.driver.wait_for_object("_shared_page_header_title",timeout=30)

    def verify_my_organization_page_description(self):
        return self.driver.verify_object_string("my_organization_description")

    def verify_my_organization_filter_button(self):
        return self.driver.verify_object_string("my_organization_filter_button")

    def verify_my_organization_settings_button(self):
        return self.driver.verify_object_string("my_organization_settings_button")

    def verify_my_organization_column_option_gear(self):
        return self.driver.wait_for_object("my_organization_column_option_gear")

    def search_user(self, user_info, raise_e=True, timeout=10):
        """
            Search user in My Organization table by using user email id
            Should display list of user based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("my_organization_search_txt",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("my_organization_search_txt", user_info,press_enter=True)

        if self.driver.wait_for_object("my_org_table_no_item_found_lbl",raise_e=False) is not False:
            table_entry_users=self.driver.wait_for_object("my_org_table_no_item_found_lbl")
            if raise_e:
                raise MyOrganizationTableEmpty("My Organization table is empty")
            else:
                logging.info(table_entry_users.text)
                return False
        else:
            table_entry_users = self.driver.find_object("my_org_table_user_email_lbl",multiple=True)

            for i in range(len(table_entry_users)):
                if user_info.lower() in table_entry_users[i].text.lower():
                    logging.info("Customer email: " + table_entry_users[i].text+ " contains the searched string: " + user_info)
                    return True
                else:
                    if raise_e:
                        raise UserSearchException("Customer email: " + table_entry_users[i].text+ " does not contain the searched string: " + user_info)
                    else:
                        return False

    ################################## Column Options Popup ##################################################

    def click_my_organization_column_option_gear(self):
        return self.driver.click("my_organization_column_option_gear")

    def verify_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title")

    def get_column_options_popup_options(self):
        actual_options = []
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options

    def verify_column_options_popup_reset_to_default_button(self):
        return self.driver.verify_object_string("column_options_popup_reset_to_default_btn")

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def click_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "User Name":
            options[0].click()
        elif option == "Email Address":
            options[1].click()
        elif option == "Status":
            options[2].click()
        elif option == "Role":
            options[3].click()

    def verify_my_organization_tabel_column(self,column_name,displayed=True):
        if column_name == "USER NAME":
                return self.driver.wait_for_object("my_org_table_username_column", invisible=not displayed)
        elif column_name == "EMAIL ADDRESS":
                return self.driver.wait_for_object("my_org_table_email_column", invisible=not displayed)
        elif column_name == "ROLE":
                return self.driver.wait_for_object("my_org_table_role_column", invisible=not displayed)
        elif column_name == "STATUS":
                return self.driver.wait_for_object("my_org_table_status_column", invisible=not displayed)
        elif column_name == "ASSIGNED TO":
                return self.driver.wait_for_object("my_org_table_assigned_to_column", invisible=not displayed)

    ################################## Filter Side Bar ##################################################

    def click_my_organization_filter_button(self):
        return self.driver.click("my_organization_filter_button")

    def verify_filter_side_bar_title(self):
        return self.driver.verify_object_string("filter_side_bar_title")

    def click_filter_side_bar_close_button(self):
        return self.driver.click("filter_side_bar_close_btn")

    def select_filter(self,filter_name):
        filter_options = self.driver.find_object("built_in_filter_options", multiple = True)
        for i in range(len(filter_options)):
            if filter_options[i].text == filter_name:
                filter_options[i].click()

    def verify_filter_in_my_organization_table(self,filter_name):

        if filter_name == "Active" or filter_name == "Pending" or filter_name == "Expired":
            header_index = self.get_header_index("status")
        else:
            header_index = self.get_header_index("role")

        if self.driver.wait_for_object("my_org_table_no_item_found_lbl",raise_e=False) is not False:
            return False
        else:
            table_entry_data = self.driver.find_object("my_org_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True

    ########################### IDP Setting Screen ###########################
    
    def click_my_organization_settings_button(self):
        return self.driver.click("my_organization_settings_button")

    def verify_settings_title(self):
        return self.driver.verify_object_string("settings_page_title",timeout=20)

    def verify_settings_description(self):
        return self.driver.verify_object_string("settings_page_desc")
            
    def verify_settings_identity_providers_dropdown(self):
        return self.driver.wait_for_object("settings_idp_dropdown")

    def verify_settings_domain_field(self):
        return self.driver.wait_for_object("settings_domain_field",timeout=20)
    
    def click_settings_identity_providers_dropdown(self):
        return self.driver.click("settings_idp_dropdown")

    def get_settings_idp_dropdown_default_option(self):
        return self.driver.wait_for_object("settings_idp_default_dropdown_option").text
    
    def get_settings_idp_dropdown_options(self):
        actual_options = []
        self.driver.click("settings_idp_dropdown",timeout=10)
        all_options = self.driver.find_object("settings_idp_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def select_settings_idp_dropdown_option(self,option_name):
        self.driver.click("settings_idp_dropdown",timeout=20)
        options = self.driver.find_object("settings_idp_dropdown_options",multiple=True)
        if option_name == "HP":
            options[0].click()
        elif option_name == "Google":
            options[1].click()
        elif option_name == "Azure":                                                        
            options[2].click()
    
    def verify_settings_contextual_footer(self):
        return self.driver.wait_for_object("settings_contextual_footer")
    
    def verify_settings_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("settings_contextual_footer_cancel_btn")
    
    def verify_settings_contextual_footer_save_button(self):
        return self.driver.verify_object_string("settings_contextual_footer_save_btn")

    def click_settings_contextual_footer_cancel_button(self):
        return self.driver.click("settings_contextual_footer_cancel_btn")
    
    def click_settings_contextual_footer_save_button(self):
        return self.driver.click("settings_contextual_footer_save_btn")

    def verify_settings_invalid_domain_error_message(self):
        return self.driver.verify_object_string("settings_domain_field_invalid_error_msg")
    
    def verify_settings_domain_field_error_message(self):
        return self.driver.verify_object_string("settings_domain_field_empty_error_msg")
    
    def verify_settings_contextual_footer_save_button_status(self,status):
        save_button=self.driver.wait_for_object("settings_contextual_footer_save_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True

    def clear_settings_domain_field(self):
        return self.driver.clear_text("settings_domain_field")
    
    def enter_domain_name(self, domain_name):
        return self.driver.send_keys("settings_domain_field", domain_name,clear_text=False)
    
    def get_settings_current_idp_value(self):
        return self.driver.wait_for_object("settings_idp_dropdown").text
    
    def get_settings_current_domain_value(self):
        return self.driver.get_attribute("settings_domain_field","value")
    
    def change_settings_idp_value(self,current_idp):
        if current_idp == "HP":
            self.select_settings_idp_dropdown_option("Google")
        elif current_idp == "Google":
            self.select_settings_idp_dropdown_option("HP")
        else:
            self.select_settings_idp_dropdown_option("HP")
    
    def verify_settings_toast_message(self):
        return self.driver.verify_object_string("success_alert",timeout=10)
    
    def check_toast_successful_message(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)
        
    def get_organization_table_entry_details(self):
        organization_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        organization_info["username"] = all_fields[0].text
        organization_info["email_address"] = all_fields[1].text
        organization_info["status"] = all_fields[2].text
        organization_info["role"] = all_fields[3].text
        return organization_info

    def get_organization_details(self):
        organization_details = {}
        organization_details["username"] = self.driver.wait_for_object("my_org_details_username").text
        organization_details["email_address"] = self.driver.get_text("my_org_details_email")
        organization_details["role"] = self.driver.get_text("my_org_details_role")
        organization_details["status"] = self.driver.get_text("my_org_details_status")
        return organization_details
    
    def verify_my_organization_details_personal_info_card(self):
        self.driver.wait_for_object("my_org_details_region")
        return self.driver.wait_for_object("my_org_details_phone")
    
    def verify_my_organization_details_organization_info_card(self):
        return self.driver.wait_for_object("my_org_details_accounts")
    
    def click_organization_name(self):
        return self.driver.click("my_org_table_org_name_lbl")

    ########################### Settings Not Saved Pop-up ###########################

    def verify_settings_not_saved_popup_title(self):
        return self.driver.verify_object_string("settings_not_saved_title")

    def verify_settings_not_saved_popup_desc(self):
        # Not using verify_object_string, as the actual string are in multiple lines("\n" New lines)
        expected_text = "Are you sure you want to leave this page? All unsaved changes will be lost."
        actual_text=self.driver.wait_for_object("settings_not_saved_desc").text.replace("\n", " ")
        self.compare_strings(expected_text, actual_text)

    def verify_settings_not_saved_popup_cancel_button(self):
        return self.driver.verify_object_string("settings_not_saved_cancel_btn")

    def click_settings_not_saved_popup_cancel_button(self):
        return self.driver.click("settings_not_saved_cancel_btn")

    def verify_settings_not_saved_popup_leave_button(self):
        return self.driver.verify_object_string("settings_not_saved_leave_btn")

    def click_settings_not_saved_popup_leave_button(self):
        return self.driver.click("settings_not_saved_leave_btn")


    