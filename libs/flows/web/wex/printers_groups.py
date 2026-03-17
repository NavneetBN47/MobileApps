from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
import logging
from time import sleep

class PrintersTableEmpty(Exception):
    pass

class GroupRulesTableEmpty(Exception):
    pass

class GroupAssignedPrintersTableEmpty(Exception):
    pass

class PrinterGroups(WEXFlow):
    """
        Groups flow for WEX.
    """
    flow_name = "printers_groups"

############################ Main Menu verifys ############################

    def click_groups_printers_tab_title(self):
        return self.driver.click("groups_printers_tab_title",timeout=30)

    def verify_groups_page_breadcrumb(self):
        return self.driver.verify_object_string("groups_page_breadcrumb", timeout=30)

    def verify_groups_printers_tab_title(self):
        return self.driver.wait_for_object("groups_printers_tab_title")

    def verify_groups_printers_page_loaded(self):
        return self.driver.wait_for_object("groups_printers_page_loaded",timeout=30)

    def verify_groups_printers_add_group_button(self):
        return self.driver.wait_for_object("groups_printers_add_group_button",timeout=30)
    
    def verify_groups_printers_table_column_option_gear_button(self):
        return self.driver.wait_for_object("groups_printers_table_column_option_gear_button")

    def verify_groups_printers_table_loaded(self):
        if self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, raise_e=False):
            return True
        else:
            self.verify_groups_printers_table_is_empty_msg()
            raise PrintersTableEmpty("Printers table is empty") 

    def verify_groups_printers_table_is_empty_msg(self):
        return self.driver.wait_for_object("groups_printers_table_no_item_found_msg")

    def get_groups_printers_table_headers(self):
        printers_table_headers = []
        headers = self.driver.find_object("groups_printers_table_headers", multiple=True)

        for header in headers:
            # Strip out the button label and other unwanted text within the header
            header_text = header.text.strip()
            
            # Check if there's an unwanted extra part like "descending sorted" and remove it
            if 'descending sorted' in header_text:
                header_text = header_text.replace('descending sorted', '').strip()
            
            # Append the cleaned text to the list
            printers_table_headers.append(header_text)

        # Return the cleaned headers without the last item(which seems to be empty)
        headers = printers_table_headers[:-1]
        return headers

    ################################## Column Options Popup ##################################################

    def click_groups_printers_table_column_option_gear_button(self):
        return self.driver.click("groups_printers_table_column_option_gear_button", timeout=30)

    def verify_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title", timeout=20)

    def verify_column_options_popup_reset_to_default_button(self):
        return self.driver.verify_object_string("column_options_popup_reset_to_default_btn")

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def get_column_options_popup_options(self):
        actual_options = []
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options

    def click_column_option(self, column_option_name):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_object("column_option_popup_options_label", format_specifier=[column_option_name]))
        return self.driver.click("column_option_popup_options_label", format_specifier=[column_option_name])

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def verify_groups_printers_table_column(self, column_name, displayed=True):
        if column_name == "Automated Rules":
            return self.driver.wait_for_object("groups_printers_automated_rules_table_header", invisible=not displayed, timeout=60)

    def click_column_options_popup_reset_to_default_button(self):
        return self.driver.click("column_options_popup_reset_to_default_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    ################################## Add Group Page ##################################################

    def click_groups_printers_add_group_button(self):
        sleep(5)
        return self.driver.click("groups_printers_add_group_button",timeout=30)

    def verify_add_group_create_printer_group_page(self):
        return self.driver.wait_for_object("add_group_create_printer_group_page_title", timeout=30)
    
    def enter_group_name(self, group_name):
        return self.driver.send_keys("add_group_name_field", group_name)

    def enter_group_description(self, description):
        return self.driver.send_keys("add_group_description_field", description)

    def verify_add_group_rules_checkbox_selected(self):
        obj = self.driver.find_object("add_group_rules_checkbox")
        return obj.is_selected()

    def click_add_group_rules_checkbox(self):
        return self.driver.click("add_group_rules_checkbox")

    def click_add_groups_next_button(self):
        return self.driver.click("add_groups_next_button")

    def verify_add_groups_toast_message(self):
        self.driver.wait_for_object("add_groups_toast_message", timeout=20)
        return self.driver.get_text("add_groups_toast_message")

    def verify_group_name(self, group_name, displayed=True):
        return self.driver.wait_for_object("printers_groups_group_name", format_specifier=[group_name], timeout=30, invisible=not displayed)

    def create_group_without_rules(self, group_name):
        sleep(5)
        self.click_groups_printers_tab_title()
        self.click_groups_printers_add_group_button()
        self.enter_group_name(group_name)
        self.enter_group_description("Test group without rules")
        self.click_add_group_rules_checkbox()
        self.click_add_groups_next_button()
        # self.verify_group_name_in_all_pages(group_name)

    def remove_group_from_groups_page(self, group_name):
        sleep(5)
        self.click_groups_printers_tab_title()
        self.verify_groups_printers_table_loaded()
        self.select_group_by_name(group_name)
        self.click_group_details_delete_group_button()
        self.verify_delete_group_popup()
        security_code_text = self.get_delete_group_popup_security_code_text()
        self.enter_delete_group_popup_security_code_text(security_code_text)
        self.click_delete_group_popup_delete_button()
        # self.verify_group_name_in_all_pages(group_name, displayed=False)

    def verify_group_name_in_all_pages(self, group_name, root_obj=None):
        """
        Navigate through all table pages and check whether the given group name exists.
        Uses ONLY existing functions: select_page, get_max_page, wait_for_object, etc.
        Throws exception if not found by last page.
        """
        # Get total pages
        max_page = self.get_max_page(root_obj=root_obj)

        for page in range(1, max_page + 1):
            # Navigate to page
            self.select_page(page, root_obj=root_obj)

            try:
                # Try verifying on the current page
                self.verify_group_name(group_name, displayed=True)

                return True

            except Exception:
                # Not on this page → continue to next
                logging.info(f"Group '{group_name}' NOT found on page {page}, checking next page...")
                continue

        # If loop completes → not found on any page
        raise Exception(f"Group name '{group_name}' not found in any table page.")

    def select_group_by_name(self,group_name):
        sleep(5)
        return self.driver.click("group_list_group_name",format_specifier=[group_name],timeout=30)

    def click_group_details_delete_group_button(self):
        return self.driver.click("group_details_delete_group_button",timeout=30)
        
    def verify_delete_group_popup(self):
        return self.driver.wait_for_object("delete_group_popup", timeout=30)

    def verify_delete_group_popup_security_code(self):
        return self.driver.wait_for_object("delete_group_popup_security_code_text", timeout=30)

    def get_delete_group_popup_security_code_text(self):
        return self.driver.get_text("delete_group_popup_security_code_text")

    def enter_delete_group_popup_security_code_text(self, security_code):
        return self.driver.send_keys("delete_group_popup_security_code_text_box", security_code)
        
    def click_delete_group_popup_delete_button(self):
        return self.driver.click("delete_group_popup_delete_button", timeout=30)

    def verify_delete_groups_toast_message(self):
        self.driver.wait_for_object("delete_groups_toast_message", timeout=20)
        return self.driver.get_text("delete_groups_toast_message")

    def verify_create_printer_group_rule_page(self):
        return self.driver.wait_for_object("create_printer_group_rule_page_title", timeout=30)

    def click_create_printer_group_rule_page_property_dropdown(self):
        return self.driver.click("create_printer_group_rule_page_property_dropdown", timeout=30)

    def select_create_printer_group_rule_page_property(self,property_name):
        return self.driver.click("create_printer_group_rule_page_property_option", format_specifier=[property_name], timeout=30)

    def click_create_printer_group_rule_page_opertor_dropdown(self):
        return self.driver.click("create_printer_group_rule_page_operator_dropdown", timeout=30)

    def select_create_printer_group_rule_page_operator(self,operator_name):
        if operator_name == "Contains":
            operator_name = operator_name.lower()
        elif operator_name == "Equals":
            operator_name  = "eq"
        elif operator_name == "Starts with":
            operator_name = "sw"
        elif operator_name == "Isn't equal to":
            operator_name = "ne"
        return self.driver.click("create_printer_group_rule_page_operator_option", format_specifier=[operator_name], timeout=30)

    def click_create_printer_group_rule_page_value_dropdown(self):
        return self.driver.click("create_printer_group_rule_page_value_dropdown", timeout=30)

    def enter_create_printer_group_rule_page_value(self, value):
        return self.driver.send_keys("create_printer_group_rule_page_value_input_box", value, press_enter=True)

    def click_create_printer_group_rule_page_value_option(self, value):
        return self.driver.click("create_printer_group_rule_page_value_option", format_specifier=[value], timeout=30)

    def click_create_printer_group_rule_page_next_button(self):
        return self.driver.click("create_printer_group_rule_page_next_button", timeout=30)

    def verify_create_printer_group_review_page(self):
        return self.driver.wait_for_object("create_printer_group_review_page_title", timeout=30)

    def click_create_printer_group_review_page_create_button(self):
        return self.driver.click("create_printer_group_review_page_create_button", timeout=30)

    ##################################### Printer Groups Details Page #####################################

    def verify_printers_groups_details_page(self):
        return self.driver.wait_for_object("printers_groups_details_page_title", timeout=30)

    def verify_printer_groups_details_page_group_title(self, group_name):
        return self.driver.wait_for_object("printer_groups_details_page_group_title", format_specifier=[group_name], timeout=30)

    def verify_printer_groups_details_page_overview_tab(self):
        return self.driver.verify_object_string("printer_groups_details_page_overview_tab", timeout=30)

    def get_printer_groups_details_page_group_name(self):
        return self.driver.get_text("printer_groups_details_page_group_name")

    def get_printer_groups_details_page_group_rules(self):
        rules_count = self.driver.get_text("printer_groups_details_page_group_rules_count")
        return int(rules_count)

    def get_printer_groups_details_page_assigned_printers_count(self):
        assigned_printers_count = self.driver.get_text("printer_groups_details_page_assigned_printers_count")
        return int(assigned_printers_count) 

    def get_printer_groups_details_page_group_description(self):
        return self.driver.get_text("printer_groups_details_page_group_description")

    def click_printer_groups_details_page_rules_and_printers_tab(self):
        return self.driver.click("printer_groups_details_page_rules_and_printers_tab", timeout=30)

    def verify_printer_groups_details_page_rules_and_printers_tab(self):
        return self.driver.verify_object_string("printer_groups_details_page_rules_and_printers_tab", timeout=30)

    def verify_group_rules_table_loaded(self):
        if self.driver.wait_for_object("group_rules_table_entries", timeout=30, raise_e=False):
            return True
        else:
            self.verify_printers_groups_details_group_rules_table_is_empty()
            raise GroupRulesTableEmpty("Printers-Group Details - Group Rules table is empty")
        
    def verify_printers_groups_details_group_rules_table_is_empty(self):
        return self.driver.verify_object_string("printers_groups_details_group_rules_table_no_item_found_msg", timeout=30)

    def get_group_rules_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        table_entry_data = self.driver.find_object("group_rules_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]

    def get_property_name_in_group_rules_table(self):
        return self.get_group_rules_column_data("property_name")

    def get_operator_in_group_rules_table(self):
        return self.get_group_rules_column_data("operator_name")

    def get_value_in_group_rules_table(self):
        return self.get_group_rules_column_data("value_name")

    def verify_groups_assigned_printers_table_loaded(self):
        if self.driver.wait_for_object("assigned_printers_table_entries", timeout=30, raise_e=False):
            return True
        else:
            self.verify_printers_groups_details_assigned_printers_table_is_empty()
            raise GroupAssignedPrintersTableEmpty("Printers-Group Details - Assigned Printers table is empty")

    def verify_printers_groups_details_assigned_printers_table_is_empty(self):
        return self.driver.verify_object_string("printers_groups_details_assigned_printers_table_no_item_found_msg", timeout=30)

    def click_printer_groups_details_page_refresh_button(self):
        return self.driver.click("printer_groups_details_page_refresh_button", timeout=30)

    def get_groups_printers_details_total_table_entries(self,total_len=True, root_obj=None):
        entries = self.driver.find_object("assigned_printers_table_entries_column", multiple=True, root_obj=root_obj)
        if total_len:
            return len(entries)
        else:
            return entries 

    def get_groups_page_printers_detail_info(self):
        """Get all printers' detail info from the group details page assigned printers table."""
        printers_detail_list = []
        entries = self.get_groups_printers_details_total_table_entries(total_len=False)
    
        for entry in entries:
            printers_detail = {}
            all_fields = self.driver.find_object("assigned_printer_table_entry_all_cols", multiple=True, root_obj=entry)
            printers_detail["serial_number"] = all_fields[1].text.lower()
            printers_detail["model_name"] = all_fields[2].text.lower()
            printers_detail["policies"] = all_fields[3].text.lower()
            printers_detail["device_name"] = all_fields[4].text.lower()
            printers_detail["asset_number"] = all_fields[5].text.lower()
            printers_detail["location"] = all_fields[6].text.lower()
            printers_detail_list.append(printers_detail)
    
        return printers_detail_list