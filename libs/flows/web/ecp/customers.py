import logging
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class CustomerTableEmpty(Exception):
    pass

class CustomerSearchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class Customers(ECPFlow):
    """
        Contains all of the elements and flows associated in Customers section for ECP
    """
    flow_name = "customers"

    ########################### Customers Page ###########################

    def verify_customers_page(self):
        return self.driver.wait_for_object("_shared_page_header_title", timeout=30)

    def verify_customers_page_title(self):
        return self.driver.verify_object_string("customers_title_lbl")
       
    def verify_customers_page_desc(self):
        return self.driver.verify_object_string("customers_description_lbl")

    def verify_customers_filter_button(self):
        return self.driver.wait_for_object("customers_filter_button")
    
    def verify_customers_refresh_button(self):
        return self.driver.wait_for_object("customers_refresh_button")

    def verify_customers_search_box(self):
        return self.driver.wait_for_object("customers_search_box")

    def click_customers_filter_button(self):
        return self.driver.click("customers_filter_button")

    def verify_customers_column_option_gear_button(self):
        return self.driver.wait_for_object("customers_settings_button")

    def click_customers_column_option_settings_gear_button(self):
        return self.driver.click("customers_settings_button")

    def verify_customers_table_data_load(self):
        # It verifies customers table is loaded and has lists of customers entry.
        if self.driver.wait_for_object("customers_table_checkbox", timeout=30, raise_e=False) is not False:
            return True
        else:
            raise CustomerTableEmpty("Customer table is empty")

    def click_customer_name(self):
        return self.driver.click("customers_table_customer_name")

    def click_customer_checkbox(self):
        return self.driver.click("customers_table_checkbox")

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("customers_contextual_footer")

    def verify_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("customers_contextual_footer",invisible=True)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("customers_contextual_footer_calcel_button")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.verify_object_string("customers_contextual_footer_selected_item_lbl")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("customers_contextual_footer_select_action_dropdown")

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("customers_contextual_footer_continue_button")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("customers_contextual_footer_calcel_button")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("customers_contextual_footer_continue_button")

    def get_last_updated_datetime(self):
        return self.driver.find_object("customers_last_updated_datetime_lbl").text

    def click_refresh_button(self):
        return self.driver.click("customers_refresh_button")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("customers_contextual_footer_select_action_dropdown")

    def select_contextual_footer_set_idp_option(self):
        return self.driver.click("customers_select_action_dropdown_set_idp_option")

    def get_contextual_footer_select_action_dropdown_options(self):
        return self.driver.wait_for_object("customers_select_action_dropdown_options").text

    def search_customers(self, cust_info, raise_e=True, timeout=10):
        """
            Search customer in customer table by using customer name
            Should display list of customers based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("customers_search_box",timeout=timeout, raise_e=raise_e)
        # self.driver.send_keys("search_user_inputbox", usr_info)
        # Press enter parameter is added , due to search enhancement.
        self.driver.send_keys("customers_search_box", cust_info, slow_type=True,press_enter=True)
        
        if self.driver.wait_for_object("customers_table_no_item_found_lbl",raise_e=False) is not False:
            table_entry_users=self.driver.wait_for_object("customers_table_no_item_found_lbl")
            logging.info(table_entry_users.text)
            return False
        else:
            table_entry_users = self.driver.find_object("customers_table_customer_name_lbl",multiple=True)

            for i in range(len(table_entry_users)):
                if cust_info in table_entry_users[i].text:
                    logging.info("Customer Name: " + table_entry_users[i].text+ " contains the searched string: " + cust_info)
                    break
                else:
                    raise CustomerSearchException("Customer Name: " + table_entry_users[i].text+ " does not contain the searched string: " + cust_info)
        return True

    def click_search_clear_button(self):
        return self.driver.click("customers_clear_search_button")

    def verify_settings_toast_message(self):
        return self.driver.verify_object_string("success_alert",timeout=10)

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

    ########################### Customer Details Screen ###########################

    def get_customer_details(self):
        customer_details = {}
        customer_details["customer_name"] = self.driver.wait_for_object("customer_details_cust_name").text
        customer_details["country"] = self.driver.get_text("customer_details_country")
        # customer_details["domain"] = self.driver.get_text("customer_details_idp")
        return customer_details

    def verify_customer_details_settings_button(self):
        return self.driver.wait_for_object("customer_details_settings_btn")

    def click_customer_details_settings_button(self):
        return self.driver.click("customer_details_settings_btn")

    def get_customer_table_entry_details(self):
        customer_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        customer_info["customer_name"] = all_fields[1].text
        customer_info["country"] = all_fields[2].text
        # customer_info["domain"] = all_fields[3].text
        return customer_info

    def verify_customer_details_domain_edit_button(self):
        return self.driver.verify_object_string("customer_details_domain_edit_btn")

    def click_customer_details_domain_edit_button(self):
        return self.driver.click("customer_details_domain_edit_btn")

    ########################### IDP Setting Screen ###########################

    def click_settings_button(self):
        return self.driver.click("settings_btn")
        
    def verify_settings_title(self):
        return self.driver.verify_object_string("settings_page_title")

    def verify_settings_description(self):
        return self.driver.verify_object_string("settings_page_desc")
            
    def verify_settings_identity_providers_dropdown(self):
        return self.driver.wait_for_object("settings_idp_dropdown")

    def verify_settings_domain_field(self):
        return self.driver.wait_for_object("settings_domain_field")
    
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
    
    def click_user_settings_all_users_tab(self):
        return self.driver.click("settings_all_users_breadcrumb")

    ################################## Column Options Popup ##################################################

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
        if option == "COUNTRY/REGION":
            options[1].click()
        elif option == "Domain":
            options[2].click()

    def verify_customers_tabel_column(self,column_name,displayed=True):
        if column_name == "COUNTRY/REGION":
                return self.driver.wait_for_object("customers_table_country_column", invisible=not displayed)
        elif column_name == "Domain":
                return self.driver.wait_for_object("customers_table_domain_column", invisible=not displayed)
