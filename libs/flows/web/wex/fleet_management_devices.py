import logging
import random
from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from MobileApps.resources.const.web.const import WEX_URLS
from time import sleep
from datetime import datetime
from selenium.common.exceptions import *
from datetime import datetime, timedelta

class DeviceSearchException(Exception):
    pass

class WrongToastException(Exception):
    pass

class PrinterSearchException(Exception):
    pass

class PrintersGroupNotFoundException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class PolicyNoncompliantException(Exception):
    pass

class SettingValueMismatchException(Exception):
    pass

class PrintersTableEmpty(Exception):
    pass

class SettingNotFoundException(Exception):
    pass

class CannotFindPolicyException(Exception):
    pass

class FilterValueException(Exception):
    pass

class Devices(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "fleet_management_devices"

    ############################ Main Menu verifys ############################

    def verify_devices_printers_table_loaded(self):
        # It verifies printers table is loaded and has lists of printers entry.
        if self.driver.wait_for_object("_shared_table_entries_with_link", timeout=40, raise_e=False):
            return True
        else:
            self.verify_printers_table_is_empty_msg()
            raise PrintersTableEmpty("Printers table is empty")

    def verify_printers_table_is_empty_msg(self):
        return self.driver.wait_for_object("printers_table_no_item_found_msg")

    def verify_fleet_management_devices_printers_button(self):
        return self.driver.wait_for_object("fleet_management_devices_printers_button")

    def verify_devices_printers_page_devices_breadcrumb(self):
        return self.driver.verify_object_string("devices_printers_page_devices_breadcrumb")
    
    def verify_devices_printers_page_refresh_button(self):
        return self.driver.wait_for_object("printers_refresh_button",timeout=30)
    
    def click_devices_printers_page_refresh_button(self):
        return self.driver.click("printers_refresh_button",timeout=30)
    
    def verify_printers_search_txtbox(self):
        return self.driver.wait_for_object("_shared_search_box")
    
    def verify_printers_export_all_btn(self):
        if self.driver.wait_for_object("printers_export_all_btn", raise_e=False):
            return True
        else:
            self.click_printers_floating_menu()
            return self.driver.wait_for_object("printers_export_all_btn")
    
    def verify_printers_add_btn(self):
        if self.driver.wait_for_object("printers_add_btn", raise_e=False):
            return True
        else:
            self.click_printers_floating_menu()
            return self.driver.wait_for_object("printers_add_btn")
    
    def verify_column_option_settings_gear_button(self):
        return self.driver.wait_for_object("printers_column_option_settings_gear_btn")
    
    def verify_page_size_btn(self, root_obj=None):
        return self.driver.wait_for_object("_shared_page_size_btn", root_obj=root_obj)

    def verify_page_nav(self, root_obj=None):
        return self.driver.wait_for_object("_shared_all_pages_btn", root_obj=root_obj)

    def verify_no_items_found(self, raise_e=True):
        return self.driver.wait_for_object('_shared_no_items_found_img', raise_e=raise_e, timeout=30)    
    
    def search_printers(self, search_text):
        #Currently only pressing enter triggers the search it's probably a bug
        #As there is also a search button that doesn't work
        self.driver.wait_for_object("_shared_search_box", timeout=30)
        self.verify_devices_printers_table_loaded()
        sleep(3)
        for _ in range(3):
            try:
                return self.driver.send_keys("_shared_search_box", search_text, press_enter=True)
            except (StaleElementReferenceException,ElementNotInteractableException):
                logging.debug("Search Printers Send_keys is not working")
                sleep(3)
        raise PrinterSearchException("After 3 tries still Search printers Send_keys is not working")

    def click_search_clear_button(self):
        return self.driver.click("printers_search_box_clear_button",timeout=30)

    def verify_printers_search_results(self, search_text, column_name):
        column_index = self.get_header_index(column_name)
        column_entries = self.driver.find_object("_shared_table_all_col_by_index", 
                                                format_specifier=[column_index], multiple=True)
        all_rows = self.driver.find_object("_shared_table_entries", multiple=True)
        
        for index, column_entry in enumerate(column_entries):
            # First check the target column
            if search_text.lower() in column_entry.text.lower():
                continue  # Found in target column
            
            # Not in target column, check entire row
            if index < len(all_rows):
                row_text = all_rows[index].text.lower()
                if search_text.lower() in row_text:
                    continue  # Found elsewhere in row (global search working)
            
            # Not found anywhere - this is a real failure
            raise DeviceSearchException(
                f"Search term '{search_text}' not found in '{column_name}' column or any other column of the row"
            )
        
        return True

    def verify_search_results_with_serial_number(self, search_text):
        return self.verify_printers_search_results(search_text, "serial_number")

    def verify_search_results_contain_serial(self, expected_serial):
        """Verify search results contain the expected serial number"""
        serial_column_index = self.get_header_index("printers_serial_number")
        serial_elements = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[serial_column_index], multiple=True)
        search_results = [elem.text.strip() for elem in serial_elements]
        
        assert any(expected_serial in serial for serial in search_results), \
            f"Expected serial '{expected_serial}' not found in search results: {search_results}"
    
    def verify_search_results_with_model_name(self, search_text):
        return self.verify_printers_search_results(search_text, "model_name")

    def verify_search_results_with_assessment_status(self, search_text):
        return self.verify_printers_search_results(search_text, "printer_assessment_status")

    def verify_search_results_with_assigned_policies(self, search_text):
        return self.verify_printers_search_results(search_text, "policies")

    def verify_search_results_with_policy_compliance(self, search_text):
        return self.verify_printers_search_results(search_text, "Policy_Compliance")

    def verify_search_results_with_connectivity(self, search_text):
        return self.verify_printers_search_results(search_text, "printer_connectivity")

    def verify_search_results_with_device_name(self, search_text):
        return self.verify_printers_search_results(search_text, "device_name")
    
    def verify_search_results_with_group(self, search_text):
        return self.verify_printers_search_results(search_text, "printers_group")
    
    def verify_search_results_with_wiredipv4_address(self, search_text):
        return self.verify_printers_search_results(search_text, "printers_wiredipv4")
    
    def verify_export_popup(self):
        return self.driver.wait_for_object("export_popup_modal")

    def verify_printers_table_headers(self):
        printers_table_headers = []
        headers = self.driver.find_object("printers_table_headers", multiple=True)

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

    def verify_printers_table_filtered_by_printer_assessment_status(self, status, expected_count=None):
        """
        Verify that the printers table is filtered by the specified printer assessment status.
        
        :param status: The printer assessment status to verify.
        :param expected_count: The expected number of printers with the specified status (optional).
        :raises DeviceSearchException: If the table is not correctly filtered or the count does not match.
        :return: True if the table is correctly filtered and the count matches (if provided).
        """
        assessment_column = self.get_header_index("printer_assessment_status")
        assessment_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[assessment_column], multiple=True)
        
        all_status = all(element.text.lower() == status.lower() for element in assessment_list)
        actual_count = len(assessment_list)
        
        if not all_status:
            raise DeviceSearchException(f"Printers table not filtered correctly. Not all printers have the assessment status '{status}'.")
        
        if expected_count is not None and actual_count != expected_count:
            raise DeviceSearchException(f"Expected {expected_count} printers with assessment status '{status}', but found {actual_count}.")
        
        return True
    
    def get_printers_table_count(self):
        return len(self.driver.find_object("_shared_table_entries_with_link", multiple=True))
    
    ########################Devices Page -PCs, Virtual Machines, Physical Assets############################
    
    def click_first_checkbox(self):
        return self.driver.click("printers_table_checkbox",timeout=30)

    def verify_devices_view_pcs_page(self):
        return self.driver.wait_for_object("devices_view_pcs_page", raise_e=False)

    def get_devices_view_pcs_page(self):
        return self.driver.wait_for_object("devices_view_pcs_page", raise_e=False).text

    def click_status_clear_button(self):
        sleep(5)  # Wait for the page to load
        return self.driver.click("pcs_status_clear_button", timeout=30)
    
    def verify_add_pcs_button(self):
        return self.driver.wait_for_object("add_pcs_button",raise_e=False)
    
    def verify_delete_pcs_button(self):
        return self.driver.wait_for_object("delete_pcs_button",raise_e=False)
    
    def verify_export_pcs_button(self):
        return self.driver.wait_for_object("export_pcs_button", raise_e=False)
    
    def verify_devices_view_virtual_machines_page(self):
        return self.driver.wait_for_object("devices_view_virtual_machines_page", raise_e=False)

    def get_devices_view_virtual_machines_page(self):
        return self.driver.wait_for_object("devices_view_virtual_machines_page", raise_e=False).text

    def verify_add_virtual_machines_button(self):
        return self.driver.wait_for_object("add_virtual_machines_button", raise_e=False)
    
    def verify_delete_virtual_machines_button(self):
        return self.driver.wait_for_object("delete_virtual_machines_button", raise_e=False)
    
    def verify_export_virtual_machines_button(self):
        return self.driver.wait_for_object("export_virtual_machines_button", raise_e=False)

    def verify_devices_view_physical_assets_page(self):
        return self.driver.wait_for_object("devices_view_physical_assets_page", raise_e=False)
    
    def get_devices_view_physical_assets_page(self):
        return self.driver.wait_for_object("devices_view_physical_assets_page", raise_e=False).text
    
    def verify_add_physical_assets_button(self):
        return self.driver.wait_for_object("add_physical_assets_button", raise_e=False)
    
    def verify_delete_physical_assets_button(self):
        return self.driver.wait_for_object("delete_physical_assets_button", raise_e=False)
        
    def verify_export_physical_assets_button(self):
        return self.driver.wait_for_object("export_physical_assets_button", raise_e=False)

    ############################ Main Menu Clicks ############################
   
    def click_devices_printers_button(self):
        return self.driver.click("fleet_management_devices_printers_button")

    def export_devices(self, file_type="CSV"):
        #Ignoring file type for now since it only supports CSV
        self.click_printers_export_all_btn()
        self.verify_export_popup()
        self.click_device_export_popup_export_btn()
        self.check_toast_successful_message()

    def click_printers_export_all_btn(self):
        self.verify_printers_export_all_btn()
        return self.driver.click("printers_export_all_btn")

    def click_device_export_popup_export_btn(self):
        return self.driver.click("export_popup_export_btn")

    def check_toast_successful_message(self):
        message = self.driver.wait_for_object("bottom_toast_msg").text
        expected_message = "File has been downloaded successfully!"
        if message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + message + " expected message is: " + expected_message)
    
    def select_option_from_printers_dropdown(self, option):
        #Option is a number that matches the drop down in order (starting from 1)
        self.driver.wait_for_object("devices_printers_menu_drop_down_option", format_specifier=[option])
        return self.driver.click("devices_printers_menu_drop_down_option", format_specifier=[option])

    def get_printers_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        table_entry_data = self.driver.find_object("printers_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]
   
    def get_all_printers_date_added(self):
        return self.get_printers_column_data("printers_date_added")
    
    def get_all_printers_serial_number(self):
        return self.get_printers_column_data("printers_serial_number")
    
    def get_all_printers_model_name(self):
        return self.get_printers_column_data("printers_model_name")
    
    def get_all_printers_assessment(self):
        return self.get_printers_column_data("printer_assessment_status")
    
    def get_all_printers_policies(self):
        return self.get_printers_column_data("printers_policies")    

    def get_all_printers_policy_compliance(self):
        return self.get_printers_column_data("printers_policy_compliance")
    
    def get_all_printers_policy_date_run(self):
        return self.get_printers_column_data("printers_policy_date_run")
    
    def get_all_printers_connectivity_status(self):
        return self.get_printers_column_data("printer_connectivity")
    
    def get_all_printers_device_name(self):
        return self.get_printers_column_data("printers_device_name")
    
    def get_all_printers_group(self):
        return self.get_printers_column_data("printers_group")
    
    def get_all_printers_wired_ipv4_address(self):
        return self.get_printers_column_data("printers_wiredipv4")
    
    def get_all_printers_model_name_from_the_group(self):
        return self.get_printers_column_data("printers_model_name")

    def get_all_printers_company_name(self):
        return self.get_printers_column_data("printers_company_name")
    
    def get_all_printers_contact_person(self):
        return self.get_printers_column_data("printers_contact_person")

    def get_all_printers_control_panel_language(self):
        return self.get_printers_column_data("printers_control_panel_language")
    
    def get_all_printers_manufacturer(self):
        return self.get_printers_column_data("printers_manufacturer")

    def parse_date(self, date_str):
        now = datetime.now()
        date_str = date_str.lower()
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
        elif "--"  in date_str:
            return datetime.max.replace(microsecond=0)

        else:
            # Normalize the input string to capitalize the first letter of the month
            date_str = date_str.capitalize()
            try:
                return datetime.strptime(date_str, "%b %d, %Y").replace(microsecond=0)
            except ValueError:
                try:
                    return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)
                except ValueError:
                    return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)

    def assessment_sort_key(self, status):
        """
        Define assessment priority order for sorting.
        Ascending: Passed < Low Risk < Not Assessed < Medium Risk < High Risk
        Descending: High Risk > Medium Risk > Not Assessed > Low Risk > Passed
        
        :param status: Assessment status string
        :return: Priority number (lower = appears first in ascending sort)
        """
        priority = {"Passed": 0, "Low Risk": 1, "Not Assessed": 2, "Medium Risk": 3, "High Risk": 4}
        return priority.get(status, 999)

    def verify_printers_date_added_is_sorted(self, date_list, order="ascending"):
        """
        Check if the list is sorted in the specified order.
        
        :param date_list: List of date strings to check.
        :param order: The order to check for. Can be "ascending" or "descending".
        :return: True if sorted in the specified order, False otherwise.
        """
        # Convert the date strings to datetime objects
        date_objects = [self.parse_date(date) for date in date_list]
        
        if order == "ascending":
            return all(date_objects[i] <= date_objects[i + 1] for i in range(len(date_objects) - 1))
        elif order == "descending":
            return all(date_objects[i] >= date_objects[i + 1] for i in range(len(date_objects) - 1))
        else:
            raise ValueError("Invalid order specified. Use 'ascending' or 'descending'.")
    
    def verify_printers_policy_date_run_is_sorted(self, date_list, order="ascending"):
        """
        Check if policy date run list is sorted in the specified order.
        Uses parse_date to handle relative time strings like "45 minutes ago".
        
        :param date_list: List of date/time strings to check (e.g., "45 minutes ago", "2 hours ago")
        :param order: The order to check for. Can be "ascending" or "descending".
        :return: True if sorted in the specified order, False otherwise.
        """
        return self.verify_printers_date_added_is_sorted(date_list, order)
    
    def verify_devices_printers_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"
    
    def verify_printers_table_no_devices_found_msg(self):
        return self.driver.verify_object_string("printers_table_no_item_found_msg")

    def get_selected_printers_count(self):
        entries = self.get_total_table_entries(total_len=False)
        selected_count = 0
        for entry in entries:
            if self.driver.find_object("printers_table_checkbox_selected", root_obj=entry, raise_e=False):
                selected_count += 1
        return selected_count

    ######################################## Filter Side bar #####################################################

    def verify_printers_filter_button(self):
        return self.driver.wait_for_object("printers_filter_button",timeout=20)
    
    def click_printers_filter_button(self):
        return self.driver.click("printers_filter_button",timeout=30)
            
    def verify_printers_filter_side_bar_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("printers_filter_side_bar_title", invisible=not displayed, timeout=30)
        return self.driver.verify_object_string("printers_filter_side_bar_title")
    
    def verify_printers_filter_side_bar_description(self):
        return self.driver.verify_object_string("printers_filter_side_bar_description")
    
    def verify_printers_filter_side_bar_search_box(self):
        return self.driver.wait_for_object("printers_filter_side_bar_search_box")

    def verify_printers_filter_side_bar_connectivity_label(self):
        return self.driver.verify_object_string("printers_filter_side_bar_connectivity_label")

    def click_printers_filter_side_bar_close_button(self):
        return self.driver.click("printers_filter_side_bar_close_btn")
    
    def select_printers_filter(self,filter_name):
        sleep(3) 
        filter_options = self.driver.find_object("printers_built_in_filter_options", multiple = True)
        for i in range(len(filter_options)):
            if filter_options[i].text == filter_name:
                filter_options[i].click()
                return True
            
    def verify_filter_in_printers_table(self,filter_name):
        if filter_name == "Online" or filter_name == "Offline":
            header_index = self.get_header_index("printer_connectivity")
        if self.driver.wait_for_object("printers_table_no_item_found_msg",raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("printers_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True
    
    def verify_filter_in_printers_table_for_security_assessment_column(self,filter_name):
        if filter_name == "Passed" or filter_name == "High Risk" or filter_name == "Medium Risk" or filter_name == "Low Risk" or filter_name == "Not Assessed":
            header_index = self.get_header_index("printer_assessment_status")
        if self.driver.wait_for_object("printers_table_no_item_found_msg",raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("printers_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True

    def verify_filter_in_printers_table_for_device_status_column(self,filter_name):
        if filter_name == "Error" or filter_name == "Warning" or filter_name == "Ready" or filter_name == "Unknown":
            header_index = self.get_header_index("status")
        if self.driver.wait_for_object("printers_table_no_item_found_msg",raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("printers_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True
    
    def verify_filter_in_printers_table_for_policy_compliance_column(self,filter_name):
        if filter_name == "Compliant" or filter_name == "Noncompliant" or filter_name == "Not Assessed":
            header_index = self.get_header_index("Policy_Compliance")
        if self.driver.wait_for_object("printers_table_no_item_found_msg",raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("printers_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True
    
    def verify_printers_table_filtered_by_printer_connectivity_status(self, filter_name, expected_count):
        sleep(5)
        self.select_page_size("500")
        header_index = self.get_header_index("printer_connectivity")
        connectivity_list = self.driver.find_object("printers_table_data", format_specifier=[header_index], multiple=True)
        all_status = all(element.text.lower() == filter_name.lower() for element in connectivity_list)
        actual_count = len(connectivity_list)
        logging.info(f"Actual count of printers with connectivity status '{filter_name}': {actual_count}")
        if not all_status:
            raise DeviceSearchException(f"Printers table not filtered correctly. Not all printers have the connectivity status '{filter_name}'.")
        if expected_count is not None and actual_count != expected_count:
            raise DeviceSearchException(f"Expected {expected_count} printers with connectivity status '{filter_name}', but found {actual_count}.")
        return True
    
    def verify_printers_table_filtered_by_printer_compliance_status(self, filter_name, expected_count):
        sleep(5)
        self.select_page_size("500")
        header_index = self.get_header_index("Policy_Compliance")
        compliance_list = self.driver.find_object("printers_table_data", format_specifier=[header_index], multiple=True)
        
        all_status = all(filter_name.lower() in element.text.lower() for element in compliance_list)
        actual_count = len(compliance_list)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_object("Policy_Compliance_table_header"))

        if not all_status:
            raise DeviceSearchException(f"Printers table not filtered correctly. Not all printers have the compliance status '{filter_name}'.")
        if expected_count is not None and actual_count != expected_count:
            raise DeviceSearchException(f"Expected {expected_count} printers with compliance status '{filter_name}', but found {actual_count}.")
        return True

    def select_printers_compliance_filter_option(self,filter_name):
        sleep(3) 
        filter_options = self.driver.find_object("printers_compliance_filter_options", multiple = True)
        for i in range(len(filter_options)):
            if filter_options[i].text == filter_name:
                filter_options[i].click()
                return True

    def verify_printers_filter_side_bar_connectivity_status_tags(self,filter_name):
            return self.driver.wait_for_object("printers_filter_side_bar_connectivity_status_tags", format_specifier=[filter_name], timeout=10)
    
    def click_printers_filter_side_bar_connectivity_status_tag_close_tag(self):
        return self.driver.click("printers_filter_side_bar_connectivity_status_tag_close_btn")
    
    def verify_printers_filter_side_bar_security_assessment_status_tags(self,filter_name):
            return self.driver.wait_for_object("printers_filter_side_bar_security_assessment_status_tags", format_specifier=[filter_name], timeout=10)

    def click_printers_filter_side_bar_security_assessment_status_tag_close_tag(self):
        return self.driver.click("printers_filter_side_bar_security_assessment_status_tag_close_btn")

    def verify_printers_filter_side_bar_device_status_column_status_tags(self,filter_name):
            return self.driver.wait_for_object("printers_filter_side_bar_device_status_column_status_tags", format_specifier=[filter_name], timeout=10)

    def click_printers_filter_side_bar_device_status_column_status_tag_close_tag(self):
        return self.driver.click("printers_filter_side_bar_device_status_column_status_tag_close_btn")

    def verify_printers_filter_side_bar_policy_compliance_status_tags(self,filter_name):
        return self.driver.wait_for_object("printers_filter_side_bar_policy_compliance_status_tags", format_specifier=[filter_name], timeout=30)
    
    def click_printers_filter_side_bar_policy_compliance_status_tag_close_tag(self):
        return self.driver.click("printers_filter_side_bar_policy_compliance_status_tag_close_btn", timeout=30)

    def verify_printers_filter_side_bar_connectivity_status_clear_all_tag(self):
        return self.driver.verify_object_string("printers_filter_side_bar_connectivity_status_clear_all_tag")
    
    def click_printers_filter_side_bar_connectivity_status_clear_all_tag(self):
        return self.driver.click("printers_filter_side_bar_connectivity_status_clear_all_tag")
    
    def verify_printers_filter_side_bar_connectivity_online_tag_is_not_displayed(self):
        return self.driver.wait_for_object("printers_filter_side_bar_connectivity_online_tag", invisible=True)
    
    def verify_printers_filter_side_bar_connectivity_offline_tag_is_not_displayed(self):
        return self.driver.wait_for_object("printers_filter_side_bar_connectivity_offline_tag", invisible=True)

    ################################### Export Devices Pop Up ####################################################

    def verify_export_devices_popup_title(self):
        return self.driver.verify_object_string("export_devices_popup_title")

    def verify_export_devices_popup_description(self):
        # Not using verify_object_string, as the actual string are in multiple lines("\n" New lines)
        expected_text = "Select the file format you would like to use for your exported device list. Once completed, your file will appear in the “Downloads” menu."
        actual_text=self.driver.get_text("export_devices_popup_desc").replace("\n", " ")
        self.compare_strings(expected_text, actual_text)
    
    def verify_export_devices_popup_cancel_button(self):
        return self.driver.verify_object_string("export_devices_popup_cancel_btn")

    def verify_export_devices_popup_export_button(self):
        return self.driver.verify_object_string("export_popup_export_btn")

    def verify_export_devices_popup_select_file_type_dropdown(self):
        return self.driver.wait_for_object("export_devices_popup_select_file_dropdown")

    def click_export_devices_popup_select_file_type_dropdown(self):
        return self.driver.click("export_devices_popup_select_file_dropdown")

    def click_export_devices_popup_cancel_button(self):
        return self.driver.click("export_devices_popup_cancel_btn")

    def get_select_file_type_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("export_devices_popup_select_file_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    #################################### Floating menu ######################################

    def verify_printers_floating_menu(self):
        return self.driver.wait_for_object("printers_floating_menu")

    def click_printers_floating_menu(self):
        return self.driver.click("printers_floating_menu")

    def get_printers_floating_menu_options(self):
        actual_options = []
        all_options = self.driver.find_object("printers_floating_menu_options", multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def click_printers_checkbox(self):
        return self.driver.click("printers_table_checkbox",timeout=30)
    
    def click_all_printers_checkbox(self):
        return self.driver.click("printers_table_select_all_checkbox",timeout=30)

    def verify_and_click_online_printer(self):
        status = "online"
        connectivity_column = self.get_header_index("printer_connectivity")
        checkbox_column = self.get_header_index("checkbox_column")
        connectivity_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[connectivity_column],multiple=True)
        checkbox_column_list = self.driver.find_object("_shared_table_checkbox_col_by_index", format_specifier=[checkbox_column],multiple=True)
        for index in range(len(connectivity_list)):
            if status == connectivity_list[index].text.lower():
                return checkbox_column_list[index].click()
            else:
                continue
        raise DeviceSearchException("Cannot find any connected printer")

    def verify_and_click_one_sim_printer(self):
        one_sim = "SIM"
        serial_number_column = self.get_header_index("printers_serial_number")
        serial_number_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[serial_number_column], multiple=True)
        for index in range(len(serial_number_list)):
            if one_sim in serial_number_list[index].text:
                return serial_number_list[index].click()
        raise DeviceSearchException("Cannot find any SIM printer")

    ################################## Column Options Popup ##################################################

    def click_printers_column_option_settings_gear_button(self):
        return self.driver.click("printers_column_option_settings_gear_btn",timeout=30)

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
    
    def click_column_options_popup_reset_to_default_button(self):
        return self.driver.click("column_options_popup_reset_to_default_btn",timeout=20)

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def click_column_option(self, column_option_name):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_object("column_option_popup_options_label", format_specifier=[column_option_name]))
        return self.driver.js_click("column_option_popup_options_label", format_specifier=[column_option_name])

    def verify_printers_table_column(self,column_name,displayed=True):
        if column_name == "Model Name":
                return self.driver.wait_for_object("printers_name_table_header", invisible=not displayed, timeout=60)
        elif column_name == "Connectivity":
                return self.driver.wait_for_object("printers_connection_table_header", invisible=not displayed, timeout=60)

    ################################### Group Side Bar ####################################################

    def verify_groups_side_bar_expand_btn(self):
        return self.driver.wait_for_object("group_side_bar_expand_btn")

    def click_groups_side_bar_expand_btn(self):
        return self.driver.click("group_side_bar_expand_btn")
    
    def verify_groups_side_bar_collapse_btn(self):
        return self.driver.wait_for_object("group_side_bar_collapse_btn")  

    def click_groups_side_bar_collapse_btn(self):
        return self.driver.click("group_side_bar_collapse_btn")
    
    def verify_groups_side_bar_collapse_button_is_displayed(self):
        return self.driver.wait_for_object("group_side_bar_collapse_btn",raise_e=False)
    
    def verify_groups_title(self,displayed=True):
        return self.driver.wait_for_object("groups_side_bar_title",invisible=not displayed,timeout=20)
    
    def verify_groups_create_group_button(self):
        return self.driver.wait_for_object("printers_groups_create_group_btn")

    def verify_groups_edit_groups_button(self):
        return self.driver.wait_for_object("printers_groups_edit_groups_btn")

    def verify_printers_manage_group_button(self):
        return self.driver.wait_for_object("printers_manage_group_button", raise_e=False)
    
    def click_printers_manage_group_button(self):
        return self.driver.click("printers_manage_group_button", timeout=30)
    
    def verify_groups_all_group_title(self):
        return self.driver.verify_object_string("groups_all_group_title",timeout=30)
    
    def verify_groups_all_group_count(self):
        return self.driver.wait_for_object("groups_all_group_count")

    def get_groups_all_group_count(self):
        return int(self.driver.wait_for_object("groups_all_group_count").text)
    
    def verify_groups_all_group_expand_btn(self):
        return self.driver.wait_for_object("groups_all_group_expand_btn")

    def get_printer_count(self,group_name):
        return int(self.driver.wait_for_object("printers_groups_group_count",format_specifier=[group_name],timeout=30).text)

    def click_printers_group(self,group_name):
        for _ in range(4):
            try:
                return self.driver.click("printers_groups_group_name",format_specifier=[group_name],timeout=30)
            except (NoSuchElementException,ElementClickInterceptedException):
                logging.debug("Printers groups hasn't loaded yet")
                sleep(3)
        raise PrintersGroupNotFoundException("After 4 tries still Printers groups hasn't loaded yet")
    
    def get_all_printer_group_names(self):
        group_names = []
        all_groups = self.driver.find_object("printers_group_group_names_list",multiple=True)
        for group in all_groups:
            group_names.append(group.text)
        return group_names
        
    def verify_printers_search_txtbox_text(self, group_name):
        return self.driver.find_object("printers_search_box_default_text", format_specifier=[group_name])

    def get_all_printer_groups_with_counts(self):
        group_name_elements = self.driver.find_object("printers_groups_name", multiple=True)
        group_count_elements = self.driver.find_object("printers_groups_device_count", multiple=True)
 
        group_names = [elem.text.strip() for elem in group_name_elements]
        device_counts = []
        for elem in group_count_elements:
            try:
                device_counts.append(int(elem.text.strip()))
            except Exception:
                device_counts.append(0)
        return group_names, device_counts
 
    def verify_selected_group_printers(self, group_names):
        for group_name in group_names:
            self.click_printers_group(group_name)
            # Check if printers table is empty
            if self.driver.wait_for_object("printers_table_no_item_found_msg", raise_e=False):
                # Table is empty, verify empty message
                self.verify_printers_table_is_empty_msg()
                continue
            self.verify_devices_printers_table_loaded()
               
            # For each printer in the table, verify the group matches the selected group name
            printer_groups = self.get_all_printers_group()
            for group in printer_groups:
                     assert group.lower() == group_name.lower(), (
                        f"Printer group '{group}' does not match selected group '{group_name}'"
                    )

    ################################### Move to Group Pop Up ####################################################

    def verify_move_to_group_button(self):
        if self.driver.wait_for_object("printers_move_to_group_button", raise_e=False):
            return True
        else:
            self.click_printers_floating_menu()
            return self.driver.wait_for_object("printers_move_to_group_button")

    def click_move_to_group_button(self):
        self.verify_move_to_group_button()
        return self.driver.click("printers_move_to_group_button")

    def verify_move_to_group_popup_title(self):
        return self.driver.verify_object_string("printers_move_to_group_popup_title")

    def verify_move_to_group_popup_description(self):
        return self.driver.verify_object_string("printers_move_to_group_popup_desc")

    def verify_move_to_group_popup_groups_to_move_field(self):
        return self.driver.wait_for_object("printers_move_to_group_popup_groups_to_move")
    
    def verify_move_to_group_popup_cancel_button(self):
        return self.driver.verify_object_string("printers_move_to_group_popup_cancel_btn")

    def verify_move_to_group_popup_move_button(self):
        return self.driver.verify_object_string("printers_move_to_group_popup_move_btn")

    def click_move_to_group_popup_cancel_button(self):
        return self.driver.click("printers_move_to_group_popup_cancel_btn")

    def click_move_to_group_popup_move_button(self):
        return self.driver.click("printers_move_to_group_popup_move_btn")

    ################################### Remove from group Pop Up ####################################################

    def verify_remove_from_group_popup_title(self):
        return self.driver.verify_object_string("printers_remove_from_group_popup_title")

    def verify_remove_from_group_popup_description(self):
        return self.driver.verify_object_string("printers_remove_from_group_popup_desc")
    
    def verify_remove_from_group_popup_cancel_button(self):
        return self.driver.verify_object_string("printers_remove_from_group_popup_cancel_btn")

    def verify_remove_from_group_popup_remove_button(self):
        return self.driver.verify_object_string("printers_remove_from_group_popup_remove_btn")

    def click_remove_from_group_popup_cancel_button(self):
        return self.driver.click("printers_remove_from_group_popup_cancel_btn")

    def click_remove_from_group_popup_remove_button(self):
        return self.driver.click("printers_remove_from_group_popup_remove_btn")
    
    ################################### Configure Device Pop-Up ####################################################

    def verify_configure_printers_button(self):
        if self.driver.wait_for_object("printers_configure_device_button", raise_e=False):
            return True
        else:
            self.click_printers_floating_menu()
            return self.driver.wait_for_object("printers_configure_device_button")

    def click_configure_printers_button(self):
        self.verify_configure_printers_button()
        return self.driver.click("printers_configure_device_button")

    def verify_configure_device_popup_title(self):
        return self.driver.verify_object_string("configure_device_popup_title", timeout=30)
    
    def verify_configure_device_popup_description(self):
        return self.driver.verify_object_string("configure_device_popup_desc")
    
    def verify_configure_device_popup_cancel_button(self):
        return self.driver.verify_object_string("configure_device_popup_cancel_btn")

    def verify_configure_device_popup_configure_button(self, disabled=False):
        button = self.driver.find_object("configure_device_popup_configure_btn")
        is_disabled = button.get_attribute("aria-disabled") == "true"
        if is_disabled != disabled:
            raise AssertionError(f"Expected 'Configure' button to be {'disabled' if disabled else 'enabled'}, but it is {'disabled' if is_disabled else 'enabled'}.")
        return True
    
    def click_configure_device_popup_cancel_button(self):
        return self.driver.click("configure_device_popup_cancel_btn")

    def verify_configure_device_popup_category_section_title(self):
        return self.driver.verify_object_string("configure_device_popup_category_section_title")
    
    def verify_configure_device_popup_all_category_option(self):
        return self.driver.verify_object_string("configure_device_popup_all_category_option")

    def verify_configure_device_popup_all_category_expand_button(self):
        return self.driver.wait_for_object("configure_device_popup_all_category_expand_btn")

    def verify_configure_device_popup_all_category_expanded(self):
        return self.driver.wait_for_object("configure_device_popup_all_category_expanded")
    
    def click_configure_device_popup_all_category_expand_button(self):
        return self.driver.click("configure_device_popup_all_category_expand_btn")
    
    def verify_configure_device_popup_all_category_collapsed(self):
        return self.driver.wait_for_object("configure_device_popup_all_category_expanded",invisible=True)

    def get_configure_device_popup_category_options(self):
        options = self.driver.find_object("configure_device_popup_category_options", multiple=True)
        return [option.text for option in options]

    def select_configure_device_popup_category_option(self, option):
        options = self.driver.find_object("configure_device_popup_category_options", multiple=True)
        for category_option in options:
            if category_option.text == option:
                return category_option.click()
        raise SettingNotFoundException(f"Setting '{option}' not found in the Configure Device popup.")
    
    def verify_configure_device_popup_category_option_displayed(self, option, displayed=True):
        try:
            # Convert the option to lowercase
            option = option.lower()

            # Handle special case for "web services"
            if option == "web services":
                option = "webServices"
        
            return self.driver.wait_for_object("configure_device_popup_edit_category_name", format_specifier=[option], invisible=not displayed, timeout=20)
        except NoSuchElementException:
            raise SettingNotFoundException(f"Setting '{option}' not found in the Configure Device popup.")

    def verify_configure_device_popup_search_txtbox_text(self, option):
        return self.driver.find_object("configure_device_popup_search_box_default_text", format_specifier=[option])
    
    def verify_configure_device_popup_show_selected_items_only_toggle_button(self):
        return self.driver.verify_object_string("configure_device_popup_show_selected_items_only_toggle_btn_name")
    
    def click_configure_device_popup_show_selected_items_only_toggle_button(self):
        return self.driver.click("configure_device_popup_show_selected_items_only_toggle_btn")
    
    def verify_configure_device_popup_show_selected_items_only_toggle_button_status(self, status):    
        if status == "enabled":
            if self.driver.get_attribute("configure_device_popup_show_selected_items_only_toggle_btn_value","value") == "true":
                return True
            else:
                raise UnexpectedItemPresentException("'Show Selected Items Only' toggle button is disabled")
        elif status == "disabled":
            if self.driver.get_attribute("configure_device_popup_show_selected_items_only_toggle_btn_value","value") == "false":
                return True
            else:
                raise UnexpectedItemPresentException("'Show Selected Items Only' toggle button is enabled")
        return False
    
    def verify_configure_device_popup_no_settings_selected_msg(self):
        return self.driver.verify_object_string("configure_device_popup_no_settings_selected_msg")
    
    def search_configure_device_popup_category_setting(self, setting_name):
        return self.driver.send_keys("configure_device_popup_search_box", setting_name, press_enter=True)
    
    def select_configure_device_popup_device_category_outgoing_servers_setting(self):
        return self.driver.click("configure_device_popup_outgoing_servers_setting",timeout=20)
    
    def click_configure_device_popup_search_txtbox_clear_button(self):
        return self.driver.click("configure_device_popup_search_box_clear_button")

    def verify_configure_device_popup_search_txtbox(self):
        return self.driver.wait_for_object("configure_device_popup_search_box")
    
    def search_configure_device_popup_device_settings(self, setting_name):
        return self.driver.send_keys("configure_device_popup_search_box", setting_name, press_enter=True)
    
    def verify_configure_device_popup_search_results(self, setting_name):
        setting_name = setting_name.lower()
        self.driver.wait_for_object("configure_device_popup_search_results", timeout=30) # Wait for Configure Device popup search results to load
        options = self.driver.find_object("configure_device_popup_search_results", multiple=True)
        for option in options:
            if setting_name in option.text.lower():
                return True
        raise SettingNotFoundException(f"Setting '{setting_name}' not found in the Configure Device popup.")

    def verify_configure_device_popup_no_settings_found_message(self, category_name):
        return self.driver.wait_for_object("configure_device_popup_no_settings_found_msg", format_specifier=[category_name])
    
    def click_configure_device_popup_search_in_all_button(self):
        return self.driver.click("configure_device_popup_search_in_all_btn")   

    def verify_download_app_configuration_button(self):
        if self.driver.wait_for_object("printers_download_app_configuration_btn", raise_e=False):
            return True
        else:
            self.click_printers_floating_menu()
            return self.driver.wait_for_object("printers_download_app_configuration_btn")

    ################################### Create Group Pop-Up ####################################################

    def click_printers_create_group_button(self):
        return self.driver.click("printers_groups_create_group_btn")

    def verify_create_group_popup_title(self):
        return self.driver.verify_object_string("create_group_popup_title")

    def verify_create_group_popup_description(self):
        return self.driver.verify_object_string("create_group_popup_desc")

    def verify_create_group_popup_group_name_field(self):
        return self.driver.wait_for_object("create_group_popup_group_name_txt")

    def enter_group_name(self,group_name):
        return self.driver.send_keys("create_group_popup_group_name_txt",group_name)

    def verify_create_group_popup_parent_group_field(self):
        return self.driver.wait_for_object("printers_move_to_group_popup_groups_to_move")

    def select_parent_group(self):
        return self.driver.click("printers_move_to_group_popup_groups_to_move")
    
    def verify_create_group_popup_cancel_button(self):
        return self.driver.verify_object_string("create_group_popup_cancel_btn")

    def click_create_group_popup_cancel_button(self):
        return self.driver.click("create_group_popup_cancel_btn")

    def verify_create_group_popup_create_button(self):
        return self.driver.verify_object_string("create_group_popup_create_btn")

    def click_create_group_popup_create_button(self):
        return self.driver.click("create_group_popup_create_btn")

    def verify_group_name(self,group_name,displayed=True):
        for _ in range(4):
            try:
                return self.driver.wait_for_object("printers_groups_group_name",invisible=not displayed,format_specifier=[group_name],timeout=30)
            except (NoSuchElementException):
                logging.debug("Printers groups hasn't loaded yet")
                sleep(3)
        raise PrintersGroupNotFoundException("After 4 tries still Printers groups hasn't loaded yet")

    ################################## Edit Group Popup ##################################################

    def click_printers_edit_groups_button(self):
        return self.driver.click("printers_groups_edit_groups_btn")

    def verify_edit_groups_popup_title(self):
        return self.driver.verify_object_string("edit_groups_popup_title",timeout=30)

    def verify_edit_groups_popup_description(self):
        return self.driver.verify_object_string("edit_groups_popup_desc")

    def verify_edit_groups_popup_delete_button(self):
        return self.driver.verify_object_string("edit_groups_popup_delete_btn",timeout=10)

    def click_edit_groups_popup_delete_button(self):
        return self.driver.click("edit_groups_popup_delete_btn")

    def verify_edit_groups_popup_create_tab(self):
        return self.driver.verify_object_string("edit_groups_popup_create_tab")

    def verify_edit_groups_popup_rename_tab(self):
        return self.driver.verify_object_string("edit_groups_popup_rename_tab")

    def verify_edit_groups_popup_close_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("edit_groups_popup_close_btn", timeout=30))
        return self.driver.verify_object_string("edit_groups_popup_close_btn")

    def click_edit_groups_popup_close_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("edit_groups_popup_close_btn", timeout=30))
        return self.driver.click("edit_groups_popup_close_btn", timeout=20)

    def select_group(self,group_name):
        return self.driver.click("group_list_group_name",format_specifier=[group_name],timeout=30)
        
    def click_edit_groups_popup_group_name(self,group_name):
        self.verify_edit_groups_popup_title()
        self.driver.wait_for_object("edit_groups_popup_group_name", format_specifier=[group_name], timeout=30)
        sleep(5)
        return self.driver.click("edit_groups_popup_group_name",format_specifier=[group_name],timeout=30)

    ################################## Edit Group Popup Create Tab ##################################################

    def verify_edit_groups_popup_create_tab_description(self):
        return self.driver.verify_object_string("create_tab_desc")

    def verify_edit_groups_popup_create_tab_group_name_label(self):
        return self.driver.verify_object_string("create_tab_group_name_lbl")

    def verify_edit_groups_popup_create_tab_group_name_field(self):
        return self.driver.wait_for_object("create_tab_group_name_txt",timeout=30)

    def enter_edit_groups_popup_create_tab_group_name(self,group_name):
        return self.driver.send_keys("create_tab_group_name_txt",group_name)

    def verify_edit_groups_popup_create_tab_parent_group_label(self):
        return self.driver.verify_object_string("create_tab_parent_group_lbl")

    def verify_edit_groups_popup_create_tab_parent_group_dropdown(self):
        return self.driver.wait_for_object("create_tab_parent_group_dropdown")

    def verify_edit_groups_popup_create_tab_create_button(self):
        return self.driver.verify_object_string("create_tab_create_btn")

    def click_edit_groups_popup_create_tab_create_button(self):
        return self.driver.click("create_tab_create_btn",timeout=20)

    ################################## Edit Group Popup Rename Tab ##################################################

    def click_edit_groups_popup_rename_tab(self):
        return self.driver.click("edit_groups_popup_rename_tab")

    def verify_edit_groups_popup_rename_tab_description(self):
        return self.driver.verify_object_string("rename_tab_desc")

    def verify_edit_groups_popup_rename_tab_group_name_label(self):
        return self.driver.verify_object_string("rename_tab_group_name_lbl")

    def edit_groups_popup_enter_group_name(self,group_name):
        return self.driver.send_keys("rename_tab_group_name_txt",group_name)

    def verify_edit_groups_popup_rename_tab_group_name_field(self):
        return self.driver.wait_for_object("rename_tab_group_name_txt")

    def verify_edit_groups_popup_rename_tab_rename_button(self):
        return self.driver.verify_object_string("rename_tab_rename_btn")

    def click_edit_groups_popup_rename_tab_rename_button(self):
        return self.driver.click("rename_tab_rename_btn")

    def verify_select_group_warning_message(self,displayed=True):
        if displayed:
            return self.driver.verify_object_string("rename_tab_select_group_warning_message")
        else:
            return self.driver.wait_for_object("rename_tab_select_group_warning_message", invisible=not displayed)
    
    def get_existing_group_warning_message(self):
        return self.driver.wait_for_object("rename_tab_existing_group_warning_message").text

    def verify_edit_groups_popup_rename_tab_group_name_textbox_status(self,status):
        if status == "disabled":
            if self.driver.wait_for_object("rename_tab_group_name_txt").is_enabled():
                raise UnexpectedItemPresentException(" Group Name textbox is enabled")
            return True
        else:
            if self.driver.wait_for_object("rename_tab_group_name_txt").is_enabled() is False:
                raise UnexpectedItemPresentException(" Group Name textbox is disabled")
            return True

    def verify_edit_groups_popup_rename_tab_rename_button_is_disabled(self):
        if self.driver.wait_for_object("rename_tab_rename_btn").is_enabled():
            raise UnexpectedItemPresentException("Rename button is enabled")
        return True

    ################################## Delete group Popup ##################################################

    def verify_delete_group_popup_title(self):
        return self.driver.verify_object_string("delete_group_popup_title")

    def verify_delete_group_popup_description(self):
        self.driver.verify_object_string("delete_group_popup_desc")
        return self.driver.verify_object_string("delete_group_popup_description")

    def verify_delete_group_popup_cancel_button(self):
        return self.driver.verify_object_string("delete_group_popup_cancel_btn")

    def click_delete_group_popup_cancel_button(self):
        return self.driver.click("delete_group_popup_cancel_btn")

    def verify_delete_group_popup_delete_button(self):
        return self.driver.verify_object_string("delete_group_popup_delete_btn")

    def click_delete_group_popup_delete_button(self):
        return self.driver.click("delete_group_popup_delete_btn")

    ####################################Add Device Pop-Up####################################################
    
    def click_printers_add_btn(self):
        self.verify_printers_add_btn()
        return self.driver.click("printers_add_btn", timeout=20)
    
    def verify_add_printers_popup_title(self):
        return self.driver.verify_object_string("add_printers_popup_title",timeout=30)
    
    def verify_add_printers_popup_description(self):
        return self.driver.verify_object_string("add_printers_popup_desc", timeout=30)

    def verify_add_printers_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_popup_close_btn", timeout=30)
    
    def verify_add_printers_popup_cancel_button(self):
        return self.driver.verify_object_string("add_printers_popup_cancel_btn", timeout=30)
    
    def verify_add_printers_popup_cloud_connect_button(self):
        return self.driver.wait_for_object("add_printers_popup_cloud_connect_btn", timeout=30)

    def click_add_printers_popup_cloud_connect_button(self):
        return self.driver.click("add_printers_popup_cloud_connect_btn", timeout=30)
    
    def verify_add_printers_popup_print_fleet_proxy_connect_button(self):
        return self.driver.wait_for_object("add_printers_popup_print_fleet_proxy_connect_btn", timeout=30)

    def click_add_printers_popup_print_fleet_proxy_connect_button(self):
        return self.driver.click("add_printers_popup_print_fleet_proxy_connect_btn", timeout=30)

    def verify_add_printers_popup_cloud_connect_button_name(self):
        return self.driver.verify_object_string("add_printers_popup_cloud_connect_btn_name", timeout=30)
    
    def verify_add_printers_popup_cloud_connect_button_description(self):
        return self.driver.verify_object_string("add_printers_popup_cloud_connect_btn_description", timeout=30)

    def verify_add_printers_popup_print_fleet_proxy_connect_button_name(self):
        return self.driver.verify_object_string("add_printers_popup_print_fleet_proxy_connect_btn_name", timeout=30)
    
    def verify_add_printers_popup_print_fleet_proxy_connect_button_description(self):
        return self.driver.verify_object_string("add_printers_popup_print_fleet_proxy_connect_btn_description", timeout=30)

    def click_add_printers_popup_close_button(self):
        return self.driver.click("add_printers_popup_close_btn", timeout=20)

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    ############################ Add Printers - Enter Manually Popup ######################################

    def verify_add_printers_enter_manually_popup_title(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_title", timeout=30)
    
    def verify_add_printers_enter_manually_popup_description(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_desc")

    def verify_add_printers_cloud_connect_enter_manually_btn_title(self):
        return self.driver.verify_object_string("add_printers_cloud_connect_enter_manually_btn_title")

    def verify_add_printers_cloud_connect_enter_manually_btn_desc(self):
        return self.driver.verify_object_string("add_printers_cloud_connect_enter_manually_btn_desc")

    def verify_add_printers_cloud_connect_enter_manually_btn(self):
        return self.driver.wait_for_object("add_printers_cloud_connect_enter_manually_btn")
    
    def click_add_printers_cloud_connect_enter_manually_btn(self):
        return self.driver.click("add_printers_cloud_connect_enter_manually_btn")

    def verify_add_printers_enter_manually_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_close_btn")

    def click_add_printers_enter_manually_popup_close_button(self):
        return self.driver.click("add_printers_enter_manually_popup_close_btn")

    def verify_add_printers_enter_manually_popup_cancel_button(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_cancel_btn")
    
    def click_add_printers_enter_manually_popup_cancel_button(self):
        return self.driver.click("add_printers_enter_manually_popup_cancel_btn")

    ############################### Add Printers- Clould Connect Printers Details Popup ###################

    def verify_add_printers_enter_manually_popup_printer_details_desc(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_printer_details_desc")

    def verify_add_printers_printer1_field_name_title(self):
        return self.driver.verify_object_string("add_printers_printer1_field_name_title")

    def verify_add_printers_printer1_field_serial_number_label(self):
        return self.driver.verify_object_string("add_printers_printer1_field_serial_number_label")

    def verify_add_printers_printer1_field_serial_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer1_field_serial_number_textbox")
    
    def verify_add_printers_printer1_field_product_number_label(self):
        return self.driver.verify_object_string("add_printers_printer1_field_product_number_label")
    
    def verify_add_printers_printer1_field_product_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer1_field_product_number_textbox")
    
    def verify_add_printers_printer1_field_delete_btn(self, displayed=True):
        return self.driver.wait_for_object("add_printers_printer1_field_delete_btn", invisible=not displayed, timeout=30)

    def enter_add_printers_printer1_field_serial_number(self,serial_number):
        return self.driver.send_keys("add_printers_printer1_field_serial_number_textbox",serial_number)

    def enter_add_printers_printer1_field_product_number(self,product_number):
        return self.driver.send_keys("add_printers_printer1_field_product_number_textbox",product_number)

    def get_add_printers_printer1_field_serial_number(self):
        serial_number = self.driver.get_attribute("add_printers_printer1_field_serial_number_textbox", "value")
        return serial_number

    def get_add_printers_printer1_field_product_number(self):
        product_number = self.driver.get_attribute("add_printers_printer1_field_product_number_textbox", "value")
        return product_number

    def verify_add_another_printer_link(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_add_another_printer_link")

    def click_add_another_printer_link(self):
        return self.driver.click("add_printers_enter_manually_popup_add_another_printer_link")

    def verify_add_printers_printer2_field(self,displayed=True):
        return self.driver.wait_for_object("add_printers_printer2_field", invisible=not displayed, timeout=30)

    def verify_add_printers_printer2_field_name_title(self):
        return self.driver.verify_object_string("add_printers_printer2_field_name_title")
    
    def verify_add_printers_printer2_field_serial_number_label(self):
        return self.driver.verify_object_string("add_printers_printer2_field_serial_number_label")

    def verify_add_printers_printer2_field_serial_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer2_field_serial_number_textbox")

    def verify_add_printers_printer2_field_product_number_label(self):
        return self.driver.verify_object_string("add_printers_printer2_field_product_number_label")
    
    def verify_add_printers_printer2_field_product_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer2_field_product_number_textbox")

    def verify_add_printers_printer2_field_delete_btn(self, displayed=True):
        return self.driver.wait_for_object("add_printers_printer2_field_delete_btn" , invisible=not displayed, timeout=30)

    def click_add_printers_printer2_field_delete_btn(self):
        return self.driver.click("add_printers_printer2_field_delete_btn")

    def verify_add_printers_enter_manually_details_popup_back_button(self):
        return self.driver.verify_object_string("add_printers_enter_manually_details_popup_back_btn")

    def click_add_printers_enter_manually_details_popup_back_button(self):
        return self.driver.click("add_printers_enter_manually_details_popup_back_btn")

    def verify_add_printers_enter_manually_details_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_details_popup_close_button", timeout=30)
    
    def click_add_printers_enter_manually_details_popup_close_button(self):
        return self.driver.click("add_printers_enter_manually_details_popup_close_button")

    def verify_add_printers_enter_manually_details_popup_submit_button(self):
        return self.driver.verify_object_string("add_printers_enter_manually_details_popup_submit_button")

    def verify_add_printers_enter_manually_details_popup_cancel_button(self):
        return self.driver.verify_object_string("add_printers_enter_manually_details_popup_cancel_button")

    def click_add_printers_enter_manually_details_popup_cancel_button(self):
        return self.driver.click("add_printers_enter_manually_details_popup_cancel_button")

    ################################# Add Printers - Discard Changes Popup ###############################

    def verify_add_printers_discard_changes_popup_title(self):
        return self.driver.verify_object_string("add_printers_discard_changes_popup_title")

    def verify_add_printers_discard_changes_popup_description(self):
        return self.driver.verify_object_string("add_printers_discard_changes_popup_desc")

    def verify_add_printers_discard_changes_popup_go_back_button(self):
        return self.driver.verify_object_string("add_printers_discard_changes_popup_go_back_button")

    def click_add_printers_discard_changes_popup_go_back_button(self):
        return self.driver.click("add_printers_discard_changes_popup_go_back_button")

    def verify_add_printers_discard_changes_popup_discard_button(self):
        return self.driver.verify_object_string("add_printers_discard_changes_popup_discard_button")
    
    def click_add_printers_discard_changes_popup_discard_button(self):
        return self.driver.click("add_printers_discard_changes_popup_discard_button")

    def verify_add_printers_discard_changes_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_discard_changes_popup_close_button")

    ################################## Add Printers - Print Fleet Proxy Popup ############################

    def verify_add_printers_print_fleet_proxy_popup_title(self):
        return self.driver.verify_object_string("add_printers_print_fleet_proxy_popup_title", timeout=30)

    def verify_add_printers_print_fleet_proxy_popup_description(self):
        return self.driver.verify_object_string("add_printers_print_fleet_proxy_popup_desc")

    def verify_add_printers_print_fleet_proxy_label(self):
        return self.driver.verify_object_string("add_printers_print_fleet_proxy_label")

    def verify_add_printers_print_fleet_proxy_version(self):
        return self.driver.wait_for_object("add_printers_print_fleet_proxy_version")

    def verify_add_printers_print_fleet_proxy_download_link(self):
        return self.driver.wait_for_object("add_printers_print_fleet_proxy_download_link")

    def click_add_printers_print_fleet_proxy_popup_back_button(self):
        return self.driver.click("add_printers_print_fleet_proxy_popup_back_btn")

    def verify_add_printers_print_fleet_proxy_done_button(self):
        return self.driver.verify_object_string("add_printers_print_fleet_proxy_done_btn")

    def click_add_printers_print_fleet_proxy_done_button(self):
        return self.driver.click("add_printers_print_fleet_proxy_done_btn")

    ########################################Printer details page###########################################

    def verify_printer_details_page(self):
        return self.driver.wait_for_object("printer_details_info_section")

    def verify_devices_printers_details_page_devices_breadcrumb(self):
        return self.driver.verify_object_string("devices_printers_details_devices_breadcrumb", timeout=30)
    
    def verify_devices_printers_details_page_details_breadcrumb(self):
        return self.driver.wait_for_object("devices_printers_details_page_details_breadcrumb", timeout=30)

    def verify_devices_printers_details_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers/" + self.get_device_cloud_id()
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"
    
    def click_devices_printers_details_page_devices_breadcrumb(self):
        return self.driver.click("devices_printers_details_devices_breadcrumb")

    def get_printers_serial_number(self):
        # It only takes first printer serial number from printer table
        printer_details=self.get_printers_detail_info()
        return printer_details["serial_number"]
    
    def get_printers_serial_number(self):
        # It only takes first printer serial number from printer table
        printer_details=self.get_printers_detail_info()
        return printer_details["serial_number"]
    
    def get_printers_ip_hostname_info(self):
        # It only takes first printer ip hostname from printer table
        printer_details=self.get_printers_detail_info()
        return printer_details["printers_wiredip_hostname"]
    
    def get_printers_ipv4_address_info(self):
        # It only takes first printer ipv4 address from printer table
        printer_details=self.get_printers_detail_info()
        return printer_details["printers_wiredipv4"]
    
    def get_printers_detail_info(self):
        printers_detail_list = []
        entries = self.get_total_table_entries(total_len=False)
        
        for entry in entries:
            printer_info = {}
            all_fields = self.driver.find_object("_shared_table_entry_all_cols", multiple=True, root_obj=entry)
            printer_info["serial_number"] = all_fields[1].text.lower()
            printer_info["model_name"] = all_fields[2].text.lower()
            printer_info["connectivity"] = all_fields[3].text.lower()
            printer_info["connectivity_type"] = all_fields[4].text.lower()
            printer_info["status"] = all_fields[5].text.lower()
            printer_info["status_updated"] = all_fields[6].text.lower()
            printer_info["group"] = all_fields[7].text.lower()
            printer_info["policies"] = all_fields[8].text.lower()
            # printer_info["policy_date_run"] = all_fields[9].text.lower()
            printer_info["security_assessment"] = all_fields[10].text.lower()
            printer_info["policy_compliance"] = all_fields[11].text.lower()
            printer_info["firmware_version"] = all_fields[12].text.lower()
            printer_info["location"] = all_fields[13].text.lower()
            printer_info["wired_hostname"] = all_fields[14].text.lower()
            printer_info["date_added"] = all_fields[15].text.lower()
            printer_info["wired_ipv4_address"] = all_fields[16].text.lower()
            printer_info["device_name"] = all_fields[17].text.lower()
            printer_info["asset_number"] = all_fields[18].text.lower()
            printer_info["manufacturer"] = all_fields[19].text.lower()
            printer_info["contact_person"] = all_fields[20].text.lower()
            printer_info["company_name"] = all_fields[21].text.lower()
            printer_info["control_panel_language"] = all_fields[22].text.lower()
            printer_info["printers_wiredipv6"] = all_fields[23].text.lower()
            # printer_info["printers_wiredmac"] = all_fields[24].text.lower()
            printer_info["wireless_ipv4_address"] = all_fields[25].text.lower()
            printer_info["wireless_ipv6_address"] = all_fields[26].text.lower()
            printer_info["wireless_mac_address"] = all_fields[27].text.lower()
            printer_info["wireless_hostname"] = all_fields[28].text.lower()
            printer_info["wifi_direct_ipv4_address"] = all_fields[29].text.lower()
            printer_info["wifi_direct_ipv6_address"] = all_fields[30].text.lower()
            printer_info["wifi_direct_mac_address"] = all_fields[31].text.lower()
            printer_info["wifi_direct_hostname"] = all_fields[32].text.lower()
            # printer_info["device_status_message"] = all_fields[33].text.lower()
            printer_info["apps"] = all_fields[34].text.lower()
            printer_info["last_synced"] = all_fields[35].text.lower()           
            printers_detail_list.append(printer_info)
        return printers_detail_list
    
    def enable_printers_table_column(self):
        self.click_printers_column_option_settings_gear_button()
        self.click_column_option("Asset Number")
        self.click_column_option("Manufacturer")
        self.click_column_option("Wired (Hostname)")
        self.click_column_option("Wired (IPv4 Address)")
        self.click_column_option("Wired (IPv6 Address)")
        self.click_column_option("Wired (MAC Address)")
        self.click_column_option("Status")
        self.click_column_option("Status Updated")
        self.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.verify_devices_printers_table_loaded()
        self.verify_printers_table_column("Wired_Hostname")

    def disable_printers_table_column(self):
        self.click_printers_column_option_settings_gear_button()
        self.click_column_option("Wired (Hostname)")
        self.click_column_option("Wired (IPv4 Address)")
        self.click_column_option("Asset Number")
        self.click_column_option("Manufacturer")
        self.click_column_option("Wired (IPv6 Address)")
        self.click_column_option("Wired (MAC Address)")
        self.click_column_option("Status")
        self.click_column_option("Status Updated")

        self.click_column_options_popup_save_button()
        self.verify_printers_table_column("Wired_Hostname",displayed=False)
        self.verify_printers_table_column("Wired_IPv4_Address",displayed=False)
        self.verify_printers_table_column("Wired_IPv6_Address",displayed=False)
        self.verify_printers_table_column("Wired_MAC_Address",displayed=False)
        self.verify_printers_table_column("Status",displayed=False)
        self.verify_printers_table_column("Status_Updated",displayed=False)

    def verify_printers_details_info(self):
        details_info = {}
        details_info["serial_number"] = self.driver.wait_for_object("printers_details_serial_number", timeout=30).text.lower()
        details_info["model_name"] = self.driver.wait_for_object("printers_details_info_section_printer_friendly_name",timeout=20).text.lower()
        # details_info["device_status_message"] = self.driver.wait_for_object("printers_device_status_message").text.lower()
        details_info["connectivity"] = self.driver.wait_for_object("printers_details_connectivity_status").text.lower()
        # details_info["printers_wiredipv4"] = self.driver.wait_for_object("printers_details_wiredipv4").text
        # details_info["printers_wiredip_hostname"] = self.driver.wait_for_object("printers_details_wiredip_hostname").text
        details_info["firmware_version"] = self.driver.wait_for_object("general_information_section_firmware_version").text
        details_info["location"] = self.driver.wait_for_object("printers_details_info_section_printer_location").text.lower()
        details_info["device_name"] = self.driver.wait_for_object("printers_details_info_section_printer_title").text.lower() 
        details_info["connectivity_type"] = self.driver.wait_for_object("printers_details_info_section_printer_type_label").text.lower()
        details_info["asset_number"] = self.driver.wait_for_object("general_information_section_asset_number").text
        details_info["manufacturer"] = self.driver.wait_for_object("general_information_section_manufacturer_name").text.lower()
        # details_info["printers_wiredipv6"] = self.driver.wait_for_object("general_information_section_wiredipv6_value").text
        # details_info["printers_wiredmac"] = self.driver.wait_for_object("general_information_section_wiredmac_value").text.lower()
        details_info["status"] = self.driver.wait_for_object("printers_details_status").text.lower()
        return details_info

    def verify_printers_details_page_printer_details_info_section(self):
        return self.driver.wait_for_object("printer_details_info_section")

    def verify_printers_details_info_section_supplies_chart(self):
        try:
            return self.driver.wait_for_object("printers_details_supplies_chart")
        except (NoSuchElementException, TimeoutException):
            print("Supplies chart not present")

    def verify_printers_details_page_overview_tab(self):
        return self.driver.verify_object_string("printers_details_overview_tab",timeout=30)

    def click_printers_details_overview_tab(self):
        return self.driver.click("printers_details_overview_tab",timeout=30)

    def verify_printers_details_page_properties_tab(self):
        return self.driver.verify_object_string("printers_details_properties_tab", timeout=30)

    def verify_printers_details_page_hp_secure_fleet_manager_tab(self):
        return self.driver.verify_object_string("printers_details_hp_secure_fleet_manager_tab", timeout=30)

    def verify_printers_details_page_hp_sds_event_log_tab(self):
        return self.driver.verify_object_string("printers_details_hp_sds_event_log_tab", timeout=30)
    
    def click_printers_details_page_hp_sds_event_log_tab(self):
        return self.driver.click("printers_details_hp_sds_event_log_tab",timeout=30)
    
    def verify_devices_printers_details_page_hp_sds_event_log_tab_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers/" + self.get_device_cloud_id() + "/sds-event-log"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def verify_printer_details_tab_highlighted(self, anchor):
        obj = self.driver.find_object("printers_details_tab_name_highlighted", format_specifier=[anchor])
        assert "true" == obj.get_attribute("aria-selected")

    def verify_printers_details_page_anchor_list(self):
        return self.driver.wait_for_object("printers_details_anchor_list")
    
    def verify_printers_details_info_section_printer_title(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_title",timeout=30)
    
    def verify_printer_details_info_section_expand_button(self):
        return self.driver.wait_for_object("printer_details_info_section_expand_btn")
    
    def verify_printers_details_page_printer_type_label(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_type_label",raise_e=False)
    
    def verify_printers_details_info_section_printer_image(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_image", timeout=30, raise_e=False)
    
    def verify_printers_details_info_section_printer_friendly_name(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_friendly_name")

    def verify_printers_details_info_section_printer_location(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_location")
    
    def verify_printers_details_info_section_printer_status_title(self):
        return self.driver.verify_object_string("printers_details_info_section_printer_status_title")
    
    def verify_printers_details_info_section_printer_status(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_status")
    
    def verify_printers_details_info_section_printer_status_updated_title(self):
        return self.driver.verify_object_string("printers_details_info_section_printer_status_updated_title")
    
    def verify_printers_details_info_section_printer_status_updated_date_and_time(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_status_updated_date_and_time")
    
    def verify_printers_details_info_section_printer_connectivity_title(self):
        return self.driver.verify_object_string("printers_details_info_section_printer_connectivity_title")
    
    def verify_printers_details_info_section_printer_connectivity_status(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_connectivity_status")
    
    def verify_printers_details_info_section_printer_status_message_title(self):
        return self.driver.verify_object_string("printers_details_info_section_printer_status_message_title")
    
    def verify_printers_details_info_section_printer_status_message(self):
        return self.driver.wait_for_object("printers_details_info_section_printer_status_message")
    
    def verify_printers_details_supplies_chart_start_scroll_button(self):
        return self.driver.wait_for_object("printers_details_supplies_chart_start_scroll_btn")
    
    def verify_printers_details_supply_chart_ink_cartridges_tab(self):
        return self.driver.verify_object_string("printers_details_supply_chart_ink_cartridges_tab")
    
    def verify_printers_details_supply_chart_printhead_tab(self):
        return self.driver.verify_object_string("printers_details_supply_chart_printhead_tab")
    
    def verify_printers_details_supply_chart_media_tab(self):
        return self.driver.verify_object_string("printers_details_supply_chart_media_tab")
    
    def verify_printers_details_supply_chart_other_supplies_tab(self):
        return self.driver.verify_object_string("printers_details_supply_chart_other_supplies_tab")
    
    def verify_printers_details_supplies_chart_end_scroll_button(self):
        return self.driver.wait_for_object("printers_details_supplies_chart_end_scroll_btn")
    
    def verify_printers_details_supplies_chart_estimated_supplies_label(self):
        return self.driver.verify_object_string("printers_details_supplies_chart_estimated_supplies_label")
    
    def verify_printers_details_supplies_chart_ink_cartridges_chart(self):
        return self.driver.wait_for_object("printers_details_supplies_chart_ink_cartridges_chart")
    
    ###################################Properties Tab####################################################

    def click_printers_details_page_properties_tab(self):
        return self.driver.click("printers_details_properties_tab",timeout=30)
    
    def verify_devices_printers_details_page_properties_tab_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers/" + self.get_device_cloud_id() + "/configuration"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def verify_copier_accordion(self):
        return self.driver.verify_object_string("printers_details_properties_tab_copier_card",timeout=30)

    def verify_device_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_device_card",timeout=30)

    def verify_ews_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_ews_card")

    def verify_network_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_network_card")

    def verify_security_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_securiry_card")

    def verify_supplies_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_supplies_card")

    def verify_solutions_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_solutions_card")

    def verify_digital_sending_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_digital_sending_card")

    def verify_web_services_accordion(self):
        return self.driver.verify_object_string("printer_details_properties_tab_web_services_card")

    def verify_wireless_accordian(self):
        return self.driver.verify_object_string("printer_details_properties_tab_wireless_card")

    def click_copier_accordion(self):
        return self.driver.click("printers_details_properties_tab_copier_card",timeout=30)
    
    def verify_copier_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printers_details_properties_tab_copier_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_copier_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the copier Category
        list_items = self.driver.find_object("property_tab_copier_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_device_accordion(self):
        return self.driver.click("printer_details_properties_tab_device_card",timeout=30)

    def verify_device_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_device_card","aria-expanded")
        assert is_expanded == 'true'

    def click_printer_device_details_device_property_card(self,setting_card):
        return self.driver.click("printer_device_details_device_property_card",format_specifier=[setting_card],timeout=15)

    def get_printer_device_details_device_property_value(self,setting_card):
        return self.driver.wait_for_object("printer_device_details_device_property_value",format_specifier=[setting_card],timeout=15).text

    def get_property_tab_device_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the device Category
        list_items = self.driver.find_object("property_tab_device_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers
    
    def click_ews_accordion(self):
        return self.driver.click("printer_details_properties_tab_ews_card", timeout=30)

    def verify_ews_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_ews_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_ews_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the ews Category
        list_items = self.driver.find_object("property_tab_ews_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_network_accordion(self):
        return self.driver.click("printer_details_properties_tab_network_card", timeout=30)
    
    def verify_network_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_network_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_network_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the network Category
        list_items = self.driver.find_object("property_tab_network_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_security_accordion(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_details_properties_tab_securiry_card"))
        return self.driver.click("printer_details_properties_tab_securiry_card")
    
    def verify_security_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_securiry_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_security_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the security Category
        list_items = self.driver.find_object("property_tab_security_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_supplies_accordion(self):
        return self.driver.click("printer_details_properties_tab_supplies_card", timeout=30)
    
    def verify_supplies_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_supplies_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_supplies_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the supplies Category
        list_items = self.driver.find_object("property_tab_supplies_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_solutions_accordion(self):
        return self.driver.click("printer_details_properties_tab_solutions_card", timeout=30)

    def verify_solutions_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_solutions_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_solutions_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the solutions Category
        list_items = self.driver.find_object("property_tab_solutions_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_digital_sending_accordion(self):
        return self.driver.click("printer_details_properties_tab_digital_sending_card", timeout=30)

    def verify_digital_sending_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_digital_sending_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_digital_sending_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the digital sending Category
        list_items = self.driver.find_object("property_tab_digital_sending_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_web_services_accordion(self):
        return self.driver.click("printer_details_properties_tab_web_services_card",timeout=30)
    
    def verify_web_services_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_web_services_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_web_services_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the web services Category
        list_items = self.driver.find_object("property_tab_web_services_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_wireless_accordion(self):
        return self.driver.click("printer_details_properties_tab_wireless_card", timeout=30)

    def verify_wireless_accordion_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_properties_tab_wireless_card","aria-expanded")
        assert is_expanded == 'true'

    def get_property_tab_wireless_category_setting_list_items(self):
        widget_headers = []
        # Locate all the list items under the wireless Category
        list_items = self.driver.find_object("property_tab_wireless_category_setting_list_items", multiple=True)
        for item in list_items:
            header = item.text.split('\n')[0]
            widget_headers.append(header)
        return widget_headers

    def click_show_editable_items_only_radio_button(self):
        return self.driver.click("show_editable_items_only_radio_btn",timeout=30)

    def verify_printers_details_properties_tab_anchor_list(self):
        return self.driver.wait_for_object("printers_details_properties_tab_anchor_list")

    def get_printers_details_properties_tab_anchor_list_items(self):
        anchor_list = []
        anchors = self.driver.find_object("printers_details_properties_tab_anchor_list",multiple=True)
        for anchor in anchors:
            item = anchor.text
            anchor_list.append(item)
        return anchor_list
    
    def click_printer_details_properties_tab_anchor_list_item(self,anchor):
        return self.driver.click("printers_details_property_anchor_list_item", format_specifier=[anchor], timeout=20)

    def verify_printer_details_properties_tab_anchor_list_item_highlighted(self, anchor):
        obj = self.driver.find_object("printers_details_property_anchor_list_item_highlighted", format_specifier=[anchor])
        title = obj.get_attribute("title")
        assert "Current anchor" == title, f"Expected 'Current anchor' but got '{title}'"

    def verify_edit_button_from_settings_list_in_properties_tab(self,setting_card):
        return self.driver.verify_object_string("printer_device_details_device_property_edit_button",format_specifier=[setting_card])
    
    def click_printer_device_details_device_property_edit_button(self,setting_card):
        return self.driver.click("printer_device_details_device_property_edit_button",format_specifier=[setting_card],timeout=20)

    ################################## HP Secure Fleet Manager Tab ###################################

    def click_printers_details_page_hp_secure_fleet_manager_tab(self):
        return self.driver.click("printers_details_hp_secure_fleet_manager_tab")
    
    def verify_devices_printers_details_page_hp_secure_fleet_manager_tab_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers/" + self.get_device_cloud_id() + "/fleet-manager"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"
    
    def verify_hp_secure_fleet_manager_widget_reports_dropdown(self):
        return self.driver.wait_for_object("reports_dropdown")

    def select_hp_secure_fleet_manager_reports_dropdown(self):
        return self.driver.click("reports_dropdown", timeout=30)

    def verify_hp_secure_fleet_manager_tab_export_as_pdf_button(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_tab_export_as_pdf_button")
    
    def click_hp_secure_fleet_manager_tab_export_as_pdf_button(self):
        return self.driver.click("hp_secure_fleet_manager_tab_export_as_pdf_button")
    
    def verify_hp_secure_fleet_manager_tab_no_reports_selected_icon(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_tab_no_reports_selected_icon")
    
    def verify_hp_secure_fleet_manager_tab_no_reports_selected_message(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_tab_no_reports_selected_message")
    
    def verify_hp_secure_fleet_manager_tab_note_message(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_tab_note_message")
    
    def verify_details_report_loaded(self):
        return self.driver.wait_for_object("report_date",timeout=15,raise_e=False)

    def get_report_result(self):
        return self.driver.wait_for_object("hp_secure_device_details_latest_report_result",timeout=10).text

    ##################################### Overview Tab ################################################

    def verify_printer_details_general_information_section(self):
        return self.driver.wait_for_object("printer_details_general_information_section",timeout=30)
    
    def verify_printer_details_connectivity_type_section(self):
        return self.driver.wait_for_object("printer_details_connectivity_type_section",timeout=30)
    
    def verify_printer_details_general_information_section_title(self):
        return self.driver.verify_object_string("printer_details_general_information_section_title")
    
    def verify_printer_details_connectivity_type_section_title(self):
        return self.driver.verify_object_string("printer_details_connectivity_type_section_title")
    
    def verify_printer_details_general_information_section_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_general_information_section","aria-expanded")
        assert is_expanded == 'true'

    def verify_printer_details_connectivity_type_section_expanded(self):
        is_expanded = self.driver.get_attribute("printer_details_connectivity_type_section","aria-expanded")
        assert is_expanded == 'true'

    def click_printer_details_connectivity_type_section(self):
        return self.driver.click("printer_details_connectivity_type_section")
 
    def verify_connectivity_type_section_printer_connectivity_name(self):
        return self.driver.wait_for_object("connectivity_type_section_printer_connectivity_type",timeout=30)
   
    def verify_connectivity_type_section_printer_connectivity_description(self):
        return self.driver.wait_for_object("connectivity_type_section_printer_connectivity_description")
   
    def verify_connectivity_type_section_printer_connectivity_status(self):
        return self.driver.wait_for_object("connectivity_type_section_printer_connectivity_status",timeout=30)
       
    def get_connectivity_type_section_printer_connectivity_type(self):
        return self.driver.get_text("connectivity_type_section_printer_connectivity_type")
   
    def click_connectivity_type_section_proxy_view_details_link(self):
        return self.driver.click("connectivity_type_section_proxy_view_details_link")
    
    def verify_general_information_section_asset_number_title(self):
        return self.driver.verify_object_string("general_information_section_asset_number_title")
    
    def verify_general_information_section_asset_number(self):
        return self.driver.wait_for_object("general_information_section_asset_number")

    def get_general_information_section_overview_tab_asset_number(self):
        return self.driver.wait_for_object("general_information_section_asset_number",timeout=40).text
    
    def get_general_information_section_overview_tab_hostname(self):
        return self.driver.wait_for_object("general_information_section_hostname",timeout=30).text   

    def get_general_information_section_overview_tab_ipv4_address(self):
        return self.driver.wait_for_object("general_information_section_ipv4_address",timeout=30).text
    
    def verify_general_information_section_device_group_title(self):
        return self.driver.verify_object_string("general_information_section_device_group_title")
    
    def verify_general_information_section_device_group(self):
        return self.driver.wait_for_object("general_information_section_device_group")
    
    def verify_general_information_section_date_added_title(self):
        return self.driver.verify_object_string("general_information_section_date_added_title")
    
    def verify_general_information_section_date_added(self):
        return self.driver.wait_for_object("general_information_section_date_added")
    
    def verify_general_information_section_firmware_version_title(self):
        return self.driver.verify_object_string("general_information_section_firmware_version_title")
    
    def verify_general_information_section_firmware_version(self):
        return self.driver.wait_for_object("general_information_section_firmware_version")
    
    def verify_general_information_section_serial_number_title(self):
        return self.driver.verify_object_string("general_information_section_serial_number_title")
    
    def verify_general_information_section_serial_number(self):
        return self.driver.wait_for_object("general_information_section_serial_number")

    def get_anchor_list_items(self):
        anchor_list = []
        anchors = self.driver.find_object("printers_details_anchor_list_items",multiple=True)
        for anchor in anchors:
            anchor_list.append(anchor.text)
        return anchor_list
 
    def click_anchor_list_item(self,anchor):
        if anchor == "General Information":
            return self.driver.click("printers_details_anchor_list_item", format_specifier=[1], timeout=20)
        elif anchor == "Connectivity Type":
            return self.driver.click("printers_details_anchor_list_item", format_specifier=[2], timeout=20)
   
    def verify_anchor_list_item_highlighted(self,anchor):
        if anchor == "General Information":
            obj = self.driver.wait_for_object("printers_details_anchor_list_item_highlighted", format_specifier=[1])
            assert "location" == obj.get_attribute("aria-current")
        elif anchor == "Connectivity Type":
            obj = self.driver.wait_for_object("printers_details_anchor_list_item_highlighted", format_specifier=[2])
            assert "location" == obj.get_attribute("aria-current")

    ################################## Reports ########################################

    def select_report(self, option):
        self.driver.wait_for_object("reports_dropdown_area",timeout=30)
        self.select_hp_secure_fleet_manager_reports_dropdown()
        return self.driver.click("select_device_" + option + "_option",timeout=20)
    
    def verify_device_report_type(self,report_type):
        if report_type == "assessment":
            return self.driver.verify_object_string("device_assessment_report_type",timeout=15)
        else:
            return self.driver.verify_object_string("device_remediation_report_type",timeout=15)

    def verify_device_report_description(self):
        return self.driver.verify_object_string("device_report_desc")

    def verify_report_content_expanded(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("report_content", timeout=30))
        is_expanded = self.driver.get_attribute("report_content","aria-expanded")
        assert is_expanded == 'true'

    def verify_report_content_collapsed(self):
        is_expanded = self.driver.get_attribute("report_content","aria-expanded")
        assert is_expanded == 'false'

    def click_report_content(self):
        return self.driver.click("report_content")
    
    def select_reports_dropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("reports_dropdown"))
        return self.driver.click("reports_dropdown")

    def verify_reports_dropdown_options(self):
        return self.driver.wait_for_object("reports_dropdown_options",timeout=15)

    ############################# Prnter Details - Policies Tab #############################

    def verify_printers_details_page_policies_tab(self):
        return self.driver.verify_object_string("printers_details_policies_tab",timeout=30)

    def click_printers_details_page_policies_tab(self):
        return self.driver.click("printers_details_policies_tab",timeout=30)
    
    def verify_devices_printers_details_page_policies_tab_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/printers/" + self.get_device_cloud_id() + "/policy"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"

    def verify_printers_details_policies_tab_anchor_list(self):
        return self.driver.wait_for_object("printers_details_policies_tab_anchor_list",timeout=30)
    
    def get_printers_details_policies_tab_anchor_list_items(self):
        anchor_list = []
        anchors = self.driver.find_object("printers_details_policies_tab_anchor_list",multiple=True)
        for anchor in anchors:
            item = anchor.text
            anchor_list.append(item)
        return anchor_list
    
    def click_printer_details_policies_tab_anchor_list_item(self,anchor):
        return self.driver.click("printers_details_policy_anchor_list_item", format_specifier=[anchor], timeout=20)
    
    def verify_printer_details_policies_tab_anchor_list_item_highlighted(self, anchor):
        obj = self.driver.find_object("printers_details_policy_anchor_list_item_highlighted", format_specifier=[anchor])
        assert "location" == obj.get_attribute("aria-current")        

        ################ Compliance Status Widget ###############

    def verify_printers_details_policies_tab_compliance_status_widget(self):
        return self.driver.wait_for_object("printers_details_policies_tab_compliance_status_widget")

    def verify_printers_details_policies_tab_compliance_status_widget_title(self):
        return self.driver.verify_object_string("printers_details_policies_tab_compliance_status_widget_title")

    def verify_compliance_status_widget_run_now_button(self):
        return self.driver.wait_for_object("compliance_status_widget_run_now_button")

    def verify_compliance_status_widget_run_now_button_is_enabled(self):
        if self.driver.find_object("compliance_status_widget_run_now_button_disabled", raise_e=False):
            logging.info("Run Now button is disabled")
            return False
        return True
    
    def verify_compliance_status_widget_no_items_found_message(self):
        return self.driver.verify_object_string("compliance_status_widget_no_items_found_message",timeout=20)
    
    def click_compliance_status_widget_run_now_button(self):
        return self.driver.click("compliance_status_widget_run_now_button",timeout=20)
    
    def check_policy_started_to_check_compliance_bottom_toast(self):
        expected_toast_message = "Policy compliance assessment in progress..."
        expected_toast_message_end_part = "The printer's updated compliance status will display when the process is finished."
        actual_message_part1 = self.driver.wait_for_object("policy_started_to_check_compliance_bottom_toast",timeout=20).text
        actual_message_part2 = self.driver.wait_for_object("policy_started_to_check_compliance_bottom_toast_end_part").text

        if actual_message_part1 != expected_toast_message or actual_message_part2 != expected_toast_message_end_part:
            raise WrongToastException(f"The toast message is: '{actual_message_part1} {actual_message_part2}' expected message is: '{expected_toast_message} {expected_toast_message_end_part}'")
        return True

    def verify_compliance_status_widget_expanded(self):
        is_expanded = self.driver.get_attribute("compliance_status_widget_expand_button","aria-expanded")
        assert is_expanded == 'true'

    def verify_compliance_status_widget_collapsed(self):
        is_expanded = self.driver.get_attribute("compliance_status_widget_expand_button","aria-expanded")
        assert is_expanded == 'false'

    def click_compliance_status_widget(self):
        return self.driver.click("compliance_status_widget_expand_button",timeout=30)

        ################ Device - Specific Policy Widget ################

    def verify_printers_details_policies_tab_policy_widget(self):
        return self.driver.wait_for_object("printers_details_policies_tab_policy_widget")

    def verify_printers_details_policies_tab_edit_button(self):
        return self.driver.wait_for_object("printers_details_policies_tab_edit_button")
    
    def click_printers_details_policies_tab_edit_button(self):
        return self.driver.click("printers_details_policies_tab_edit_button",timeout=30)

    def verify_printers_details_policies_tab_policy_widget_expand_button(self):
        self.driver.wait_for_object("printers_details_policies_tab_policy_widget_expand_button", timeout=30)
        is_expanded = self.driver.get_attribute("printers_details_policies_tab_policy_widget_expand_button","aria-expanded")
        assert is_expanded == 'true'

    def verify_printers_details_policies_tab_policy_widget_collapsed(self):
        is_expanded = self.driver.get_attribute("printers_details_policies_tab_policy_widget_expand_button","aria-expanded")
        assert is_expanded == 'false'

    def click_policy_widget(self):
        return self.driver.click("printers_details_policies_tab_policy_widget_expand_button",timeout=30)

    def verify_device_specific_policy_card_empty(self):
        if self.driver.wait_for_object("printers_details_policy_tab_no_policy_warning_message", raise_e=False):
            return True
        else:
            return False
        
    def search_policy_settings(self,setting_name):
        self.driver.click("edit_select_policy_settings_tab_all_dropdown", timeout=30)
        self.driver.wait_for_object("policy_settigs_search_txt", timeout=40)
        self.driver.send_keys("policy_settigs_search_txt",setting_name)
        # Check if the setting name is found
        if not self.driver.wait_for_object("policy_setting_result", timeout=30, raise_e=False):
            raise SettingNotFoundException(f"Setting '{setting_name}' not found.")
        return True

    def click_device_specific_policy_checkbox(self):
        return self.driver.click("edit_specific_policy_table_checkbox",timeout=20)

    def click_device_specific_policy_next_button(self):
        return self.driver.click("edit_specific_policy_next_btn")

    def click_device_specific_policy_settings_card(self,setting_card):
        return self.driver.click("device_specific_policy_settings_card",format_specifier=[setting_card], timeout=20)

    def click_ignore_unsupported_item_toggle(self):
        return self.driver.click("ignore_unsupported_item_toggle")
    
    def enter_device_property_value(self,settings_value,setting_card):
        return self.driver.send_keys("device_specific_policy_device_property_value_txt",settings_value,clear_text=False,format_specifier=[setting_card])

    def click_device_specific_policy_create_button(self):
        return self.driver.click("edit_specific_policy_remove_btn")
    
    def click_device_specific_policy_remove_button(self):
        return self.driver.click("edit_specific_policy_remove_btn")

    def verify_edit_device_policy_settings_title(self):
        return self.driver.verify_object_string("edit_device_policy_settings_title",timeout=30)

    def check_toast_successful_msg(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)

    def check_policy_removed_toast_successful_msg(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_msg",timeout=20).text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)

    def click_change_not_recommended_popup_confirm_button(self):
        #For some settings confirm button is coming before done button, so to handle this below click is used.
        return self.driver.click("change_not_recommended_popup_confirm_button", timeout=5, raise_e=False)

    def get_printer_device_page_connectivity_status(self):
        connectivity_status = self.driver.wait_for_object("printers_device_table_connectivity_status", raise_e=False)
        if not connectivity_status:
            return False
        connectivity_status = self.driver.get_text("printers_device_table_connectivity_status")
        return connectivity_status

    def get_printer_device_page_policy_list(self):
        policy_name = self.get_header_index("printers_policies")
        policy_name_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_name],multiple=True)
        for _ in range(len(policy_name_list)):
            actual_policy_name = self.driver.get_text("printers_device_table_policies_status")
        return actual_policy_name
   
    def get_printer_device_page_policy_compliance_list(self):
        policy_compliance = self.get_header_index("printers_policy_compliance")
        policy_compliance_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_compliance], multiple=True)
        
        if not policy_compliance_list:
            return None
        
        # Get the first entry's compliance status
        actual_status = self.driver.get_text("printers_device_table_policy_compliance_status")        
        # Extract the compliance status (first word before space or parenthesis)
        if "(" in actual_status:
            actual_compliance_status = actual_status.split("(")[0].strip()
        else:
            actual_compliance_status = actual_status.strip()
        return actual_compliance_status
 
    def verify_policies_device_list_compliance_status_when_no_policy_assigned(self,compliance_status):
        if compliance_status == "Not Assessed" or compliance_status == "Unknown":
            return True
        else:
            raise UnexpectedItemPresentException("Compliance status has not changed to Not Assessed or Unknown")
 
    def verify_policies_device_list_compliance_status(self,compliance_status):
        if compliance_status == "Compliant":
            return True
        elif compliance_status == "Noncompliant":
            return True
        elif compliance_status == "Unknown":
            raise UnexpectedItemPresentException("Compliance status is Unknown")
 
    def get_device_detail_policy_tab_policy_name(self):
        self.driver.wait_for_object("device_detail_policy_tab_policy_text",timeout=20)
        return self.driver.get_text("device_detail_policy_tab_policy_text")
 
    def get_device_detail_policy_tab_compliance_status(self):
        return self.driver.get_text("device_detail_policy_tab_compliance_status")
 
    def verify_device_specific_policy_setting_added(self,policy_setting_name):
        return self.driver.wait_for_object("device_specific_name_policy",format_specifier=[policy_setting_name],timeout=20)
 
    def verify_printers_device_details_policies_tab_policy_name(self,expected_name):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("device_detail_policy_tab_policy_text", timeout=30))
        actual_name = self.driver.get_text("device_detail_policy_tab_policy_text")
        assert actual_name == expected_name
 
    def verify_printers_device_details_policies_tab_compliance_policy_status(self,expected_status):
        sleep(5)
        actual_status = self.driver.wait_for_object("device_detail_policy_tab_compliance_status").text
        assert actual_status == expected_status
 
    def verify_printers_device_details_policy_compliance_total_policy_settings(self,expected_count,timeout=30):
        actual_count = self.driver.get_text("policy_device_details_total_policy_count")
        actual_policy_count = (actual_count.split(" ")[0]).strip()
        assert actual_policy_count == expected_count
   
    def verify_printers_device_details_policies_tab_assigned_policy_setting_name(self,setting_name):
        self.driver.wait_for_object("device_details_policies_tab_settings_name", format_specifier=[setting_name],timeout=30)
        if self.driver.wait_for_object("device_details_policies_tab_settings_name", format_specifier=[setting_name], raise_e=False):
            return True
        else:
            raise CannotFindPolicyException("Assigned Policy Setting not found in the Policy name")
 
    def click_printers_details_policies_tab_high_priority_settings_button(self):
        self.driver.click("printers_details_policies_tab_high_priority_settings_button",timeout=20)
 
    def verify_printers_details_policies_tab_high_priority_policy_warning_icon(self,compliance_status,policy_setting):
        if compliance_status ==  "Compliant":
            return self.driver.wait_for_object("device_details_high_priority_policy_checkmark_icon",format_specifier=[policy_setting])
        elif compliance_status == "Noncompliant":
            return self.driver.wait_for_object("device_details_high_priority_policy_warning_icon",format_specifier=[policy_setting])
 
    def verify_printers_details_policies_tab_high_priority_policy_warning_message(self,warning_message,compliance_status):
        if compliance_status ==  "Compliant":
            return True
        elif compliance_status == "Noncompliant":
            actual_warning_message = self.driver.get_text("device_details_high_priority_policy_warning_message")
            assert warning_message == actual_warning_message
       
    def verify_printers_device_details_assigned_policy_name_2(self,policy_name):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printers_device_details_priority_policy_name_2"))
        priority_policy = self.driver.get_text("printers_device_details_priority_policy_name_2")
        parts = priority_policy.split(" ")
        priority_policy_name = " ".join(parts[2:]).strip()
        assert priority_policy_name == policy_name
 
    def verify_printers_device_details_priority_2_compliance_status(self,compliance_status):
        actual_compliance_status = self.driver.get_text("printers_device_details_priority_2_compliance_status")
        assert actual_compliance_status == compliance_status
 
    def click_printers_device_details_assigned_policy_priority_2_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printers_device_details_priority_2_policy_button"))
        return self.driver.click("printers_device_details_priority_2_policy_button")
   
    def click_printers_details_policies_tab_priority_2_settings_button(self):
        self.driver.click("printers_details_policies_tab_priority_2_settings_button",timeout=20)
 
    def verify_printers_device_details_assigned_policy_priority_2_expanded(self,expanded=True):
        self.driver.wait_for_object("printers_device_details_priority_2_policy_button")
        is_expanded = self.driver.get_attribute("printers_device_details_priority_2_policy_button","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
 
    def verify_printers_device_details_low_priority_policy_name(self,low_priority_policy):
        self.driver.wait_for_object("device_details_low_priority_policy_name", format_specifier=[low_priority_policy],timeout=20)
        if self.driver.wait_for_object("device_details_low_priority_policy_name", format_specifier=[low_priority_policy], raise_e=False):
            return True
        else:
            raise CannotFindPolicyException("Assigned Low priority Policy not found")
 
    def verify_printers_device_details_low_priority_policy_overridden_status(self,low_priority_policy_status):
        self.driver.wait_for_object("device_details_low_priority_policy_status", format_specifier=[low_priority_policy_status],timeout=20)
        if self.driver.wait_for_object("device_details_low_priority_policy_status", format_specifier=[low_priority_policy_status], raise_e=False):
            return True
        else:
            raise CannotFindPolicyException("Assigned Low priority Policy status not found")
   
    def click_printers_device_details_low_priority_policy_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("device_details_low_priority_policy_button"))
        return self.driver.click("device_details_low_priority_policy_button")
   
    def click_printers_device_details_low_priority_policy_settings_button(self):
        return self.driver.click("device_details_low_priority_policy_settings_button", timeout=30)
   
    def verify_printers_device_details_low_priority_policy_warning_icon(self):
        return self.driver.wait_for_object("device_details_low_priority_policy_warning_icon",timeout=30)
   
    def verify_printers_device_details_low_priority_policy_warning_message(self,warning_message):
        actual_warning_message = self.driver.get_text("device_details_low_priority_policy_warning_message")
        assert warning_message == actual_warning_message

    ############################ Add or Remove Settings in Device Specific Policy Tab ############################

    def click_set_options_settings_checkbox(self, setting_card=None):
        return self.driver.click("set_options_settings_checkbox", format_specifier=[setting_card])

    def click_remediation_toggle(self):
        return self.driver.click("remediation_item_toggle")
    
    def add_settings_in_device_specific_policy_tab(self,setting_name, setting_card=None, settings_value=None, category_type=None, max_tls_radio=None, min_tls_radio=None, cipher_checkboxes=None):
        self.click_compliance_status_widget()
        self.click_policy_widget()
        if self.verify_device_specific_policy_card_empty() is False:
            self.remove_existing_device_specific_policy()
        self.click_printers_details_policies_tab_edit_button()
        self.search_policy_settings(setting_name)
        sleep(4) # Added sleep to wait for the search results to load
        self.click_device_specific_policy_checkbox()
        sleep(3)
        self.click_device_specific_policy_next_button()
 
        # Special handling for web encryption settings
        if setting_card == "web-encryption":
            self.click_device_specific_policy_settings_card(setting_card)
            self.click_ignore_unsupported_item_toggle()
            self.driver.click("web_encryption_change_ciphers_button")
            self.update_web_encryption_tls_settings(max_tls_radio, min_tls_radio, cipher_checkboxes)
        else:
            if category_type == "Devices":
                self.modify_devices_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Network":
                self.modify_network_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Supplies":
                self.modify_supplies_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Security":
                self.modify_security_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Firmware":
                self.modify_firmware_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "File System":
                self.modify_file_system_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Digital Sending":
                self.modify_digital_sending_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Embedded Web Server":
                self.modify_ews_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Web Services":
                self.modify_web_services_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Copier":
                self.modify_copier_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Fax":
                self.modify_fax_settings_in_device_specific_policy_settings(setting_card, settings_value)
            if category_type == "Certificate":
                self.modify_certificate_settings_in_device_specific_policy_settings(setting_card, settings_value)
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
        self.dismiss_toast()

    def update_web_encryption_tls_settings(self, max_tls_radio, min_tls_radio, cipher_checkboxes):
            self.driver.click(max_tls_radio)
            self.driver.click(min_tls_radio)
            self.driver.click("web_encryption_model_table_checkbox")
            self.driver.click("web_encryption_model_table_checkbox")  # to uncheck all the models
            for cipher in cipher_checkboxes:
                self.driver.click(cipher)
            self.driver.click("web_encryption_popup_save_button")

    def remove_existing_device_specific_policy(self):
        self.click_printers_details_policies_tab_edit_button()
        self.verify_edit_device_policy_settings_title()
        sleep(5)
        self.click_device_specific_policy_checkbox()
        # to uncheck all the policies
        self.click_device_specific_policy_checkbox()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_create_button()
        self.verify_device_specific_policy_card_empty() is True
        self.dismiss_toast()

    def get_device_cloud_id(self):
        full_url = self.driver.get_current_url()
        cloud_id = full_url.split("devices/printers/")[1].split("/")[0]
        return cloud_id
    
    def click_tcp_ip_printing_remediation_checkbox(self):
        return self.driver.click("remediation_checkbox")

    def select_control_panel_language(self,language):
        lang_dict = {"English": "en", "Russian": "ru", "Spanish": "es"}
        self.driver.click("control_panel_language_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("control_panel_language_option",format_specifier=[lang_dict[language]]))
        return self.driver.click("control_panel_language_option",format_specifier=[lang_dict[language]])

    def select_embedded_web_server_language(self,language):
        lang_dict = {"English": "en", "Russian": "ru", "Spanish": "es"}
        self.driver.click("embedded_web_server_language_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("embedded_web_server_language_option",format_specifier=[lang_dict[language]]))
        return self.driver.click("embedded_web_server_language_option",format_specifier=[lang_dict[language]])

    def update_temporary_and_standard_retain_jobs_setting_attributes(self, settings_value):
        stored_jobs_enabled_status = settings_value[0]
        temporary_stored_job_status = settings_value[1]
        # standard_stored_job_status = settings_value[2]

        if stored_jobs_enabled_status == "true":
            self.driver.click("retain_print_stored_jobs_checkbox")
        else:
            self.set_temporary_stored_job(temporary_stored_job_status)
            # self.set_standard_stored_job(standard_stored_job_status)
    
    def set_temporary_stored_job(self, temporary_stored_job_status):
        self.driver.click("temporary_stored_job_dropdown")
        if temporary_stored_job_status == 30:
            self.driver.click("temporary_stored_job_1_hour_option")
        elif temporary_stored_job_status == 1440:
            self.driver.click("temporary_stored_job_never_option")
        else:
            self.driver.click("temporary_stored_job_30_minutes_option")

    def set_standard_stored_job(self, standard_stored_job_status):
        self.driver.click("standard_job_retention_dropdown")
        if standard_stored_job_status == 30:
            self.driver.click("standard_job_retention_1_hour_option")
        elif standard_stored_job_status == 1440:
            self.driver.click("standard_job_retention_never_option")
        else:
            self.driver.click("standard_job_retention_30_minutes_option")

    def click_proxy_device_date_month_year_checkbox(self):
        return self.driver.click("proxy_device_date_month_year_checkbox")
    
    def click_proxy_device_year_month_date_checkbox(self):
        return self.driver.click("proxy_device_year_month_date_checkbox")

    def click_proxy_device_month_date_year_checkbox(self):
        return self.driver.click("proxy_device_month_date_year_checkbox")
    
    def click_proxy_device_24_hour_format(self):
        return self.driver.click("proxy_device_24_hour_format")

    def click_proxy_device_12_hour_format(self):
        return self.driver.click("proxy_device_12_hour_format")
    
    def set_devices_date_and_time_format(self,settings_value):
        device_date_format = settings_value[0]
        device_time_format = settings_value[1]
        if device_date_format == "mmmddyyyy":
            self.click_proxy_device_date_month_year_checkbox()
        elif device_date_format == "ddmmmyyyy":
            self.click_proxy_device_year_month_date_checkbox()
        elif device_date_format == "yyyymmmdd":
            self.click_proxy_device_month_date_year_checkbox()
        if device_time_format == "hr12":
            self.click_proxy_device_24_hour_format()
        else:
            self.click_proxy_device_12_hour_format()
    
    def update_sleep_settings(self,sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values):
        self.driver.send_keys("sleep_settings_sleep_mode_textbox",sleep_mode_values)
        if auto_on_events_status == "powerButtonPress":
            self.driver.click("sleep_settings_wake_all_events_radio_button")
        elif auto_on_events_status == "all":
            self.driver.click("sleep_settings_wake_network_port_radio_button")
        else:
            self.driver.click("sleep_settings_wake_all_events_radio_button") # Clicking on power button, device is going to DC state so changing to wake all events
        self.driver.send_keys("sleep_settings_auto_off_textbox",auto_off_after_sleep_values)

    def set_sleep_settings(self,settings_value):
        sleep_auto_off_timer_status=settings_value[0]
        sleep_mode_values=settings_value[1]
        auto_on_events_status=settings_value[2]
        auto_off_after_sleep_values=settings_value[3]
        if  sleep_auto_off_timer_status == "false":
            self.click_set_options_settings_checkbox("sleep-settings")
            self.update_sleep_settings(sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values)
        # else:
        #     self.click_set_options_settings_checkbox("sleep-settings")

    def set_restrict_color_status(self,settings_value):
        color_settings = settings_value[0]
        restrict_by_user_permissions = settings_value[1]
        restrict_by_application = settings_value[2]
        default_permission = settings_value[3]
        application_name = settings_value[4]
        if color_settings == "enableColor":
            self.driver.click("restrict_color_settings_grayscale_radio_button")
        elif color_settings == "disableColor":
            self.driver.click("restrict_color_settings_customize_color_radio_button")
            if restrict_by_user_permissions == "true":
                self.driver.click("restrict_by_user_permissions_checkbox")
            if restrict_by_application == "true":
                self.driver.click("restrict_by_application_checkbox")
            else:
                if default_permission == "bestColor":
                    self.driver.click("default_permissions_grayscale_radio_button")
                self.driver.click("non_default_applications_add_button")
                self.driver.send_keys("add_popup_application_name_textbox",application_name)
                self.driver.click("add_popup_add_button")

    def verify_service_access_code_textbox(self):
        if self.driver.wait_for_object("service_access_code_textbox_disabled").is_enabled():
            raise UnexpectedItemPresentException("TextBox is enabled")
        return True 

    def update_cors_origin_settings_values(self, settings_value, setting_card):
        cors_setting_checkbox = settings_value[0]
        site_name = settings_value[1]
        if cors_setting_checkbox == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.click("cors_setting_add_button")
            self.driver.send_keys("cors_setting_site_name_textbox", site_name)
            self.driver.click("cors_setting_add_popup_add_button")

    def enter_control_panel_timeout_value(self,timeout_value):
        return self.driver.send_keys("enter_control_panel_timeout",timeout_value)

    def update_host_usb_plug_and_play_setting_attributes(self, settings_status):
        plug_and_play_status = settings_status[0]
        print_from_usb_status = settings_status[1]
        scan_to_usb_status = settings_status[2]
        if plug_and_play_status == "false":
            self.click_host_usb_plug_and_play_option()
            if print_from_usb_status == "false":
                self.click_proxy_device_settings_checkbox("host-usb-pnp.retrieve")
            if scan_to_usb_status == "false":
                self.click_proxy_device_settings_checkbox("host-usb-pnp.save")

    def click_proxy_device_settings_checkbox(self, setting_name):
        return self.driver.click("proxy_device_settings_checkbox", format_specifier=[setting_name])

    def click_host_usb_plug_and_play_option(self):
        return self.driver.click("host_usb_plug_and_play_checkbox")

    def update_information_tab_setting_attributes(self, settings_status):
        information_tab_status = settings_status[0]
        display_job_log_status = settings_status[1]
        display_print_job_log_status = settings_status[2]
        if information_tab_status == "false":
            self.driver.click("require_admin_password_for_access_option")
        if display_job_log_status == "false":
            self.driver.click("display_print_page_option")
        if display_print_job_log_status == "false":
            self.driver.click("display_job_log_option")

    def verify_secure_boot_presence_option_is_disabled(self):
        if self.driver.find_object("secure_boot_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True

    def verify_whitelisting_presence_option_is_disabled(self):
        if self.driver.find_object("whitelisting_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True

    def set_languages_in_ews_language_setting(self,settings_value):
        selected_language = settings_value[0]
        language_source_status = settings_value[1]
        if language_source_status == "ews":
            self.driver.click("browser_language_settings_checkbox")
        elif language_source_status == "devcie":
            self.driver.click("printer_language_settings_checkbox")
        elif language_source_status == "browser":
            if selected_language == "en":
                self.select_embedded_web_server_language("Russian")
            else:
                self.select_embedded_web_server_language("English")

    def click_time_services_do_not_sync_network_time_server(self):
        return self.driver.click("time_services_do_not_sync_network_time_server")
    
    def click_time_services_automatic_sync_custom_network_time_server(self):
        return self.driver.click("time_services_automatic_sync_custom_network_time_server")

    def set_port_value_and_server_ip_address_for_time_services_settings(self,settings_value):
        time_services_system_time_sync = settings_value[0]
        time_services_ip_address = settings_value[1]
        local_port = settings_value[2]
        synchronize_time = settings_value[3]
        if time_services_system_time_sync == "ntp":
            self.click_time_services_do_not_sync_network_time_server()
        else:
            self.click_time_services_automatic_sync_custom_network_time_server()
            self.driver.send_keys("time_services_server_address_ip", time_services_ip_address )
            self.driver.send_keys("time_services_port_value", local_port)
            self.driver.send_keys("time_services_hours_value",synchronize_time )

    def set_email_notifications(self,notification_condition_status,notification_mode_status,email_addresses):
        if notification_condition_status == "never":
            self.driver.click("email_notification_settings_notify_job_fails_radio_button")
            if notification_mode_status == "email":
                self.driver.click("email_notification_settings_deliver_notification_print_radio_button")
            else:
                self.driver.click("email_notification_settings_deliver_notification_email_radio_button")
                self.driver.send_keys("email_notification_settings_deliver_notification_email_textbox",email_addresses)

    def set_email_notification_settings(self,settings_value):
        notification_condition_status=settings_value[0]
        notification_mode_status=settings_value[1]
        email_addresses=settings_value[2]
        self.set_email_notifications(notification_condition_status,notification_mode_status,email_addresses)

    def set_server_address_and_port_value_for_proxy_server_settings(self,setting_card,settings_value):
        proxy_server_status = settings_value[0]
        server_address = settings_value[1]
        server_port = settings_value[2]
        if proxy_server_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.send_keys("proxy_server_address_txt",server_address)
            self.driver.send_keys("proxy_server_port_txt",server_port)

    def set_cartridge_very_low_action_black(self,settings_value):
        cartridge_very_low_action_black_status=settings_value
        if cartridge_very_low_action_black_status == "stop":
            self.driver.js_click("cartridge_very_low_action_black_prompt_to_continue_radio_button")
        elif cartridge_very_low_action_black_status == "prompt":
            self.driver.js_click("cartridge_very_low_action_black_continue_radio_button")
        else:
            self.driver.js_click("cartridge_very_low_action_black_stop_radio_button")
       
    def set_cartridge_very_low_action_color(self,settings_value):
        cartridge_very_low_action_color_status=settings_value
        if cartridge_very_low_action_color_status == "stop":
            self.driver.js_click("cartridge_very_low_action_color_prompt_to_continue_radio_button")
        elif cartridge_very_low_action_color_status == "prompt":
            self.driver.js_click("cartridge_very_low_action_color_continue_radio_button")
        else:
            self.driver.js_click("cartridge_very_low_action_color_stop_radio_button")

    def verify_intrusion_detection_presence_option_is_disabled(self):
        if self.driver.find_object("intrusion_detection_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True

    def set_ip_values_and_auth_status_for_device_announcement_setting(self,setting_card,settings_value):
        announcement_status = settings_value[0]
        configuration_server_ip = settings_value[1]
        server_auth_status = settings_value[2]
        if announcement_status == False:
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.send_keys("device_announcement_agent_server_ip",configuration_server_ip)
            if server_auth_status == False:
                self.driver.click("configure_ip_label")
                self.driver.click("device_announcement_agent_auth_certificate_checkbox")

    def update_ipv6_information_setting_attributes(self,setting_card,settings_value):
        ipv6_status = settings_value[0]
        dhcpv6_policy_status = settings_value[1]
        domain_name = settings_value[2]
        primary_dns_ipv6_server_address = settings_value[3]
        secondary_dns_ipv6_server_address = settings_value[4]
        if ipv6_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.send_keys("ipv6_domain_name_textbox",domain_name)
            self.driver.send_keys("primary_ipv6_dns_textbox",primary_dns_ipv6_server_address)
            self.driver.send_keys("secondary_ipv6_dns_textbox",secondary_dns_ipv6_server_address)
            if dhcpv6_policy_status == "always":
                self.driver.click("dhcpv6_policy_stateless_config_radio_button")
            else:
                self.driver.click("dhcpv6_policy_only_requested_by_router_radio_button")

    def update_online_solutions_setting_attributes(self, settings_value):
        show_event_qr_code_status = settings_value[0]
        show_support_links_status = settings_value[1]
        show_links_in_event_log_status = settings_value[2]
        if show_event_qr_code_status == "true":
            self.driver.click("show_qr_code_control_panel_event_details_checkbox")
        if show_support_links_status == "true":
            self.driver.click("show_links_in_ews_event_log_checkbox")
        if show_links_in_event_log_status == "admin":
            self.driver.click("restrict_online_solutions_to_administrator_checkbox")

    def update_tcpip_configuration_method_setting_value(self, settings_value):
        if settings_value == "bootp":
            self.driver.click("tcpip_dhcp_server_radio_button")
        elif settings_value == "dhcpv4":
            self.driver.click("tcpip_auto_ip_radio_button")
        else:
            self.driver.click("tcpip_bootp_server_radio_button")

    def update_digital_sending_service_setting_attributes(self,settings_value):
        allow_use_of_digital_send = settings_value[0]
        allow_transfer_to_digital_send = settings_value[1]
        if allow_use_of_digital_send == "true":
            self.driver.click("allow_use_of_digital_send_checkbox")
        else:
            if allow_transfer_to_digital_send == "true":
                self.driver.click("allow_transfer_to_new_digital_send_checkbox")

    def enter_dns_server_setting_attributes_value(self,settings_value):
        clear_primary_dns_status = settings_value[0]
        primary_dns_server_ip = settings_value[1]
        clear_secondary_dns_status = settings_value[2]
        secondary_dns_server_ip = settings_value[3]
        domain_name = settings_value[4]
        if clear_primary_dns_status == "manual":
            self.driver.click("clear_primary_dns_server_checkbox")
        else:
            self.driver.send_keys("primary_dns_server_ip_textbox",primary_dns_server_ip)
        if clear_secondary_dns_status == "manual":
            self.driver.click("clear_secondary_dns_server_checkbox")
        else:
            self.driver.send_keys("secondary_dns_server_ip_textbox",secondary_dns_server_ip)
        self.driver.send_keys("dns_server_domain_name_textbox",domain_name)
        
    def click_copy_background_cleanup_policy_contextual_footer_select_action_dropdown(self):
        return self.driver.click("copy_background_cleanup_policy_contextual_footer_select_action_dropdown")
 
    def select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(self,option):
        options = self.driver.find_object("copy_background_cleanup_policy_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == 1:
            options[0].click()
        elif option == 2:
            options[1].click()
        elif option == 3:
            options[2].click()
        elif option == 4:
            options[3].click()
        elif option == 5:
            options[4].click()
        elif option == 6:
            options[5].click()
        elif option == 7:
            options[6].click()
        elif option == 8:
            options[7].click()
        elif option == 9:
            options[8].click()
   
    def click_copy_contrast_policy_contextual_footer_select_action_dropdown(self):
        return self.driver.click("copy_contrast_policy_contextual_footer_select_action_dropdown")
   
    def select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(self,option):
        options = self.driver.find_object("copy_contrast_policy_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == 1:
            options[0].click()
        elif option == 2:
            options[1].click()
        elif option == 3:
            options[2].click()
        elif option == 4:
            options[3].click()
        elif option == 5:
            options[4].click()
        elif option == 6:
            options[5].click()
        elif option == 7:
            options[6].click()
        elif option == 8:
            options[7].click()
        elif option == 9:
            options[8].click()
   
    def click_copy_darkness_option_selection_dropdown(self):
        return self.driver.click("copy_darkness_option_dropdown")
 
    def select_copy_darkness_select_action_dropdown_option(self,option):
        options = self.driver.find_object("copy_darkness_select_action_dropdown_option", multiple = True)
        if option == 1:
            options[0].click()
        elif option == 2:
            options[1].click()
        elif option == 3:
            options[2].click()
        elif option == 4:
            options[3].click()
        elif option == 5:
            options[4].click()
        elif option == 6:
            options[5].click()
        elif option == 7:
            options[6].click()
        elif option == 8:
            options[7].click()
        elif option == 9:
            options[8].click()
   
    def click_copy_optimize_printed_picture_radio_button(self):
        return self.driver.click("copy_optimize_printed_picture_radio_button")
   
    def click_copy_optimize_photograph_radio_button(self):
        return self.driver.click("copy_optimize_photograph_radio_button")
 
    def click_copy_optimize_text_radio_button(self):
        return self.driver.click("copy_optimize_text_radio_button")
   
    def click_copy_optimize_mixed_radio_button(self):
        return self.driver.click("copy_optimize_mixed_radio_button")
 
    def click_copy_tray_paper_option_selection_dropdown(self):
        return self.driver.click("copy_tray_paper_options_dropdown")
 
    def select_copy_tray_paper_select_action_dropdown_option(self,option):
        options = self.driver.find_object("copy_tray_paper_select_action_dropdown_option", multiple = True)
        if option == "auto":
            options[0].click()
        elif option == "manual":
            options[1].click()
        elif option == "tray-1":
            options[2].click()
        elif option == "tray-2":
            options[3].click()
        elif option == "tray-3":
            options[4].click()
        elif option == "tray-4":
            options[5].click()
        elif option == "tray-5":
            options[6].click()
   
    def click_copy_sharpness_option_selection_dropdown(self):
        return self.driver.click("copy_sharpness_option_dropdown")
 
    def select_copy_sharpness_select_action_dropdown_option(self,option):
        options = self.driver.find_object("copy_sharpness_select_action_dropdown_option", multiple = True)
        if option == 1:
            options[0].click()
        elif option == 2:
            options[1].click()
        elif option == 3:
            options[2].click()
        elif option == 4:
            options[3].click()
        elif option == 5:
            options[4].click()

    def click_disk_encryption_inactive_status(self):
        return self.driver.click("disk_encryption_inactive_status")

    def select_fax_header_location(self,location):
        loca_dict = {"Canada": "ca", "India": "in", "Russia": "ru", "Brazil": "br", "Finland": "fi", "Germany": "de", "Japan": "jp", "Austria": "au"}
        self.driver.js_click("fax_header_location_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("fax_header_location_option",format_specifier=[loca_dict[location]]))
        return self.driver.click("fax_header_location_option",format_specifier=[loca_dict[location]])

    def set_fax_header_Settings_attributes(self,settings_value):
        test_phone_number = settings_value[0]
        company_name = settings_value[1]
        fax_header_country_status = settings_value[2]
        self.driver.send_keys("fax_header_test_phone_number_textbox",test_phone_number)
        self.driver.send_keys("fax_header_company_name_textbox",company_name)
        if fax_header_country_status == "au":
            self.select_fax_header_location("Brazil")
        if fax_header_country_status == "br":
            self.select_fax_header_location("Canada")
        if fax_header_country_status == "ca":
            self.select_fax_header_location("Finland")
        if fax_header_country_status == "fi":
            self.select_fax_header_location("Germany")
        if fax_header_country_status == "de":
            self.select_fax_header_location("India")
        if fax_header_country_status == "in":
            self.select_fax_header_location("Japan")
        else:
            self.select_fax_header_location("Austria")

    def set_scan_settings_background_cleanup(self,background_method):
        self.click_copy_background_cleanup_policy_contextual_footer_select_action_dropdown()
        if background_method == 1:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(2)
        elif background_method == 2:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(3)
        elif background_method == 3:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(4)
        elif background_method == 4:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(5)
        elif background_method == 5:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(6)
        elif background_method == 6:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(7)
        elif background_method == 7:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(8)
        elif background_method == 8:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(9)
        elif background_method == 9:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(1)
        else:
            self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(3)

    def set_scan_settings_darkness(self,exposure):
        self.click_copy_darkness_option_selection_dropdown()
        if exposure == 1:
            self.select_copy_darkness_select_action_dropdown_option(2)
        elif exposure == 2:
            self.select_copy_darkness_select_action_dropdown_option(3)
        elif exposure == 3:
            self.select_copy_darkness_select_action_dropdown_option(4)
        elif exposure == 4:
            self.select_copy_darkness_select_action_dropdown_option(5)
        elif exposure == 5:
            self.select_copy_darkness_select_action_dropdown_option(6)
        elif exposure == 6:
            self.select_copy_darkness_select_action_dropdown_option(7)
        elif exposure == 7:
            self.select_copy_darkness_select_action_dropdown_option(8)
        elif exposure == 8:
            self.select_copy_darkness_select_action_dropdown_option(9)
        elif exposure == 9:
            self.select_copy_darkness_select_action_dropdown_option(1)
        else:
            self.select_copy_darkness_select_action_dropdown_option(5)
    
    def set_scan_settings_contrast(self,contrast):
        self.click_copy_contrast_policy_contextual_footer_select_action_dropdown()
        if contrast == 1:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(2)
        elif contrast == 2:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(3)
        elif contrast == 3:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(4)
        elif contrast == 4:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(5)
        elif contrast == 5:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(6)
        elif contrast == 6:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(7)
        elif contrast == 7:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(8)
        elif contrast == 8:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(9)
        elif contrast == 9:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(1)
        else:
            self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(5)

    def set_scan_settings_sharpness(self,sharpness):
        self.click_copy_sharpness_option_selection_dropdown()
        if sharpness == 1:
            self.select_copy_sharpness_select_action_dropdown_option(2)
        elif sharpness == 2:
            self.select_copy_sharpness_select_action_dropdown_option(3)
        elif sharpness == 3:
            self.select_copy_sharpness_select_action_dropdown_option(4)
        elif sharpness == 4:
            self.select_copy_sharpness_select_action_dropdown_option(5)
        elif sharpness == 5:
            self.select_copy_sharpness_select_action_dropdown_option(1)
        else:
            self.select_copy_sharpness_select_action_dropdown_option(3)

    def set_condition_on_which_to_notify_email_address(self,notification_mode,email_address):
        if notification_mode == "email":
            self.driver.click("method_used_to_deliver_notification_dropdown")
            self.driver.click("fax_send_and_receive_set_common_job_print_option")
        else:
            self.driver.click("method_used_to_deliver_notification_dropdown")
            self.driver.click("fax_send_and_receive_set_common_job_email_option")
            self.driver.send_keys("condition_on_which_to_notify_email_address_textfield",email_address)
        self.driver.click("set_common_job_popup_save_button")

    def set_notification_settings_condition_and_method(self,notification_condition,notification_mode,email_address):
        if notification_condition == "never":
            self.driver.click("fax_send_conditions_to_notify_dropdown")
            self.driver.click("fax_send_notify_if_job_fails_option")
            self.set_condition_on_which_to_notify_email_address(notification_mode,email_address)
        elif notification_condition == "onJobFailed":
            self.driver.click("fax_send_conditions_to_notify_dropdown")
            self.driver.click("fax_send_notify_when_job_completes_option")
            self.set_condition_on_which_to_notify_email_address(notification_mode,email_address)
        else:
            self.driver.click("fax_send_do_not_notify_option")
            self.driver.click("set_common_job_popup_save_button")

    def set_internet_fax_service(self,domain_name,account_email_address):
        self.driver.click("fax_send_internet_fax_service_radio_button")
        self.driver.click("fax_send_set_internet_fax_service_button")
        self.driver.send_keys("fax_send_set_internet_fax_service_domain_textfield",domain_name)
        self.driver.send_keys("fax_send_set_internet_fax_service_email_address_textfield",account_email_address)
        self.driver.click("fax_send_set_internt_fax_service_save_button")

    def set_intern_modem_settings(self,error_correction_mode_status,jbig_compression_status):
        self.driver.click("fax_send_internal_modem_radio_button")
        self.driver.click("fax_send_and_receive_set_internal_modem_option")
        if error_correction_mode_status == "true":
            self.driver.click("fax_send_error_correction")
        if jbig_compression_status == "true":
            self.driver.click("fax_send_jbig_compression")
        self.driver.click("set_internal_modem_popup_save_button")

    def set_fax_send_method_for_fax_send_setting(self,setting_card,settings_value):
        fax_send_status = settings_value[0]
        fax_send_method = settings_value[1]
        domain_name = settings_value[2]
        account_email_address = settings_value[3]
        background_method = settings_value[4]
        exposure = settings_value[5]
        contrast = settings_value[6]
        sharpness = settings_value[7]
        notification_condition = settings_value[8]
        notification_mode = settings_value[9]
        email_address = settings_value[10]
        error_correction_mode_status = settings_value[11]
        jbig_compression_status = settings_value[12]
        if fax_send_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.click("fax_send_and_receive_set_common_job_option")
            self.set_scan_settings_background_cleanup(background_method)
            self.set_scan_settings_darkness(exposure)
            self.set_scan_settings_contrast(contrast)
            self.set_scan_settings_sharpness(sharpness)
            self.set_notification_settings_condition_and_method(notification_condition,notification_mode,email_address)
            if fax_send_method == "internalModem":
                self.set_internet_fax_service(domain_name,account_email_address)
            elif fax_send_method == "internetFaxService":
                self.driver.click("fax_send_ip_fax_radio_button")
            else:
                self.set_intern_modem_settings(error_correction_mode_status,jbig_compression_status)

    def set_default_paper_selection(self,paper_selection_status):
        self.driver.click("fax_receive_paper_selection_dropdown")
        if paper_selection_status == "auto":
            self.driver.click("fax_receive_paper_selection_tray1")
        elif paper_selection_status == "tray1":
            self.driver.click("fax_receive_paper_selection_tray2")
        else:
            self.driver.click("fax_receive_paper_selection_auto")

    def set_fax_receive_internal_modem_attributes(self,ringer_volume_status,rings_to_answer_status):
        self.driver.click("fax_receive_internal_modem_method_option")
        self.driver.click("fax_send_and_receive_set_internal_modem_option")
        if ringer_volume_status == "off":
            self.driver.click("internal_modem_ringer_volume_high_option")
        if ringer_volume_status == "high":
            self.driver.click("internal_modem_ringer_volume_low_option")
        else:
            self.driver.click("internal_modem_ringer_volume_off_option")
        self.driver.send_keys("internal_modem_rings_to_answer_textbox",rings_to_answer_status)
        self.driver.click("set_internal_modem_popup_save_button")

    def set_fax_receive_method_for_fax_receive_setting(self,setting_card,settings_value):
        fax_receive_status = settings_value[0]
        paper_selection_status = settings_value[1]
        notification_condition_status = settings_value[2]
        notification_mode_status = settings_value[3]
        email_address = settings_value[4]
        fax_receive_method_status = settings_value[5]
        ringer_volume_status = settings_value[6]
        rings_to_answer_status = settings_value[7]
        if fax_receive_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.click("fax_send_and_receive_set_common_job_option")
            self.set_default_paper_selection(paper_selection_status)
            self.set_notification_settings_condition_and_method(notification_condition_status,notification_mode_status,email_address)
            if fax_receive_method_status == "internalModem":
               self.driver.click("fax_receive_ip_fax_method_option")
            else:
                self.set_fax_receive_internal_modem_attributes(ringer_volume_status,rings_to_answer_status)

    def set_email_scan_settings(self, settings_value):
        if settings_value == "photo":
            self.driver.click("email_scan_settings_photograph_radio_button")
        elif settings_value == "glossy":
            self.driver.click("email_scan_settings_text_radio_button")
        elif settings_value == "text":
            self.driver.click("email_scan_settings_mixed_radio_button")
        elif settings_value == "mixed":
            self.driver.click("email_scan_settings_printed_picture_radio_button")

    def update_network_folder_notification_settings(self,notification_condition_status,notification_mode_status,email_addresses):
        if notification_condition_status == "never":
            self.driver.click("network_folder_notification_settings_notify_job_fails_radio_button")
            if notification_mode_status == "email":
                self.driver.click("network_folder_notification_settings_deliver_notification_print_radio_button")
            else:
                self.driver.click("network_folder_notification_settings_deliver_notification_email_radio_button")
                self.driver.send_keys("network_folder_notification_settings_deliver_notification_email_textbox",email_addresses)
           
        elif notification_condition_status == "onJobFailed":
            self.driver.click("network_folder_notification_settings_notify_job_completes_radio_button")
            if notification_mode_status == "email":
                self.driver.click("network_folder_notification_settings_deliver_notification_print_radio_button")
            else:
                self.driver.click("network_folder_notification_settings_deliver_notification_email_radio_button")
                self.driver.send_keys("network_folder_notification_settings_deliver_notification_email_textbox",email_addresses)
 
        elif notification_condition_status == "onJobCompleted":
            self.driver.click("network_folder_notification_settings_do_not_disturb_radio_button")

    def set_network_folder_notification_settings(self,settings_value):
        notification_condition_status=settings_value[0]
        notification_mode_status=settings_value[1]
        email_addresses=settings_value[2]
        self.update_network_folder_notification_settings(notification_condition_status,notification_mode_status,email_addresses)

    def set_default_from_values(self,default_from_value,default_from_email,default_display_name,default_from_user_editable):
        if default_from_value == "false":
            self.driver.click("email_default_from_dropdown")
            self.driver.click("email_default_from_user_address_option")
        else:
            self.driver.send_keys("default_from_email_address_text_box",default_from_email)
            self.driver.send_keys("default_from_display_name_text_box",default_display_name)
        if default_from_user_editable == "true":
            self.driver.js_click("email_address_from_user_editable_checkbox",default_from_user_editable)

    def set_sign_in_required_and_user_editable_value_for_to_address(self,to_sign_in_required,user_editable_to):
        if to_sign_in_required == "false":
            self.driver.click("to_sign_in_required_dropdown")
            self.driver.js_click("to_user_address_sign_in_required_option",to_sign_in_required)
        if user_editable_to == "true":
            self.driver.js_click("email_address_to_user_editable_checkbox",user_editable_to)

    def set_sign_in_required_and_user_editable_value_for_cc_address(self,cc_sign_in_required,user_ediatable_cc):
        if cc_sign_in_required == "false":
            self.driver.click("cc_sign_in_required_dropdown")
            self.driver.js_click("cc_user_address_sign_in_required_option",cc_sign_in_required)
        if user_ediatable_cc == "true":
            self.driver.js_click("email_address_cc_user_editable_checkbox",user_ediatable_cc)

    def set_sign_in_required_and_user_editable_value_for_bcc_address(self,bcc_sign_in_required,user_editable_bcc):
        if bcc_sign_in_required == "false":
            self.driver.click("bcc_sign_in_required_dropdown")
            self.driver.js_click("bcc_user_address_sign_in_required_option",bcc_sign_in_required)
        if user_editable_bcc == "true":
            self.driver.js_click("email_address_bcc_user_editable_checkbox",user_editable_bcc)

    def enter_email_body_message(self,email_body_message):
        self.driver.js_click("email_address_message_text_box")
        self.driver.send_keys("email_address_message_text_box",email_body_message)

    def set_email_message_and_encrypt_email_values(self,email_message_user_editable,encrypt_email_user_editable):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("digitally_email_message_user_editable_checkbox"))
        if email_message_user_editable == "true":
            self.driver.js_click("digitally_email_message_user_editable_checkbox",email_message_user_editable)
        if encrypt_email_user_editable == "true":
            self.driver.js_click("encrypt_email_message_user_editable_checkbox",encrypt_email_user_editable)

    def set_email_address_message_in_email_setting_attributes(self,settings_value):
        address_filed_restrictions =  settings_value[0]
        default_from_value = settings_value[1]
        default_from_email =  settings_value[2]
        default_display_name = settings_value[3]
        default_from_user_editable = settings_value[4]
        to_sign_in_required = settings_value[5]
        user_editable_to = settings_value[6]
        cc_sign_in_required = settings_value[7]
        user_ediatable_cc = settings_value[8]
        bcc_sign_in_required = settings_value[9]
        user_editable_bcc = settings_value[10]
        email_subject_name = settings_value[11]
        user_editable_subject = settings_value[12]
        email_body_message = settings_value[13]
        user_editable_body = settings_value[14]
        allow_invaild_email_address = settings_value[15]
        email_message_user_editable = settings_value[16]
        encrypt_email_user_editable = settings_value[17]
        if address_filed_restrictions == "true":
            self.driver.click("address_field_from_address_book_radio_btn")
        self.driver.click("set_email_address_message_button")
        self.set_default_from_values(default_from_value,default_from_email,default_display_name,default_from_user_editable)
        self.set_sign_in_required_and_user_editable_value_for_to_address(to_sign_in_required,user_editable_to)
        self.set_sign_in_required_and_user_editable_value_for_cc_address(cc_sign_in_required,user_ediatable_cc)
        self.set_sign_in_required_and_user_editable_value_for_bcc_address(bcc_sign_in_required,user_editable_bcc)
        self.driver.send_keys("email_address_subject_text_box",email_subject_name)
        if user_editable_subject == "true":
            self.driver.click("email_address_subject_user_editable_checkbox")
        self.enter_email_body_message(email_body_message)
        if user_editable_body == "true":
            self.driver.click("email_address_message_user_editable_checkbox")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("email_address_message_popup_save_button"))
        self.driver.click("email_address_message_popup_save_button")
        if allow_invaild_email_address == "true":
            self.driver.click("allow_invalid_email_address_checkbox")
        self.set_email_message_and_encrypt_email_values(email_message_user_editable,encrypt_email_user_editable)
    
    def update_configuration_precedence_method_setting_value(self, settings_value):
        configuration_precedence_order_value = settings_value[0]
        configuration_precedence_order_method = settings_value[1]
        
        button_mapping = {
            "manual": "configuration_precedence_manual_button",
            "tftp": "configuration_precedence_tftp_button",
            "dhcpv4": "configuration_precedence_dhcpv4_button",
            "dhcpv6": "configuration_precedence_dhcpv6_button",
        }

        if configuration_precedence_order_method in button_mapping:
            self.driver.click(button_mapping[configuration_precedence_order_method])
            if self.driver.get_attribute("configuration_precedence_priority_high_button", "aria-disabled") == "true":
                self.driver.click("configuration_precedence_priority_low_button")
            else:
                self.driver.click("configuration_precedence_priority_high_button")

    def verify_security_802_1x_authentication_setting_title(self):
        if self.driver.verify_object_string("security_802_1x_authentication_setting_title") is True:
            return True
        else:
            raise UnexpectedItemPresentException("Title is not present")
 
    def verify_security_802_1x_authentication_wired_setting_attribute_value(self,settings_value):
        username = settings_value[0]
        server_name = settings_value[1]
        require_exact_match = settings_value[2]
        eap_tls_configure = settings_value[3]
        block_network = settings_value[4]
        self.driver.send_keys("security_802_username_textbox",username)
        self.driver.send_keys("security_802_password_textbox","1")
        self.driver.send_keys("security_802_confirm_password_textbox","1")
        self.driver.send_keys("security_802_server_id_textbox", server_name)
        if require_exact_match == "true":
            self.driver.click("security_802_require_exact_match_checkbox")
        if eap_tls_configure == "false":
            self.driver.click("security_802_eap_tls_configure_certificate")
        self.driver.click("security_802_peap_configure_certificate")
        if block_network == "true" or block_network == "false":
            self.driver.click("security_802_connect_anyway_radio_button")

    def verify_security_802_1x_authentication_wireless_setting_attribute_value(self,settings_value):
        username = settings_value[0]
        server_name = settings_value[1]
        eap_tls_configure = settings_value[2]
        peap_enabled = settings_value[3]
        self.driver.click("security_802_authentication_wireless_enterprise_wifi_access_radio_button")
        self.driver.send_keys("security_802_authentication_wireless_username_textbox",username)
        self.driver.send_keys("security_802_authentication_wireless_password_textbox","1")
        self.driver.send_keys("security_802_authentication_wireless_confirm_password_textbox","1")
        self.driver.send_keys("security_802_authentication_wireless_server_id_textbox", server_name)
        self.driver.click("security_802_require_exact_match_checkbox")
        if eap_tls_configure == "false":
            self.driver.click("security_802_eap_tls_configure_certificate")
        if peap_enabled == "true" or peap_enabled == "false":
            self.driver.click("security_802_peap_configure_certificate")
        self.driver.click("security_802_leap_configure_certificate")
 
    def update_802_1x_authentication_wireless_wpa_personal_settings(self,setting_card):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("802-1x-auth-wifi")
        self.driver.click("security_802_authentication_wireless_personal_wifi_access_radio_button")
        self.driver.click("security_802_authentication_wireless_wpa2_wpa_version_radio_button")
        self.driver.click("security_802_authentication_wireless_aes_wpa_encryption_radio_button")
        self.driver.send_keys("security_802_authentication_wireless_security_key_textbox", "1234567"+str(random.randint(1,9)))
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()

    def set_network_folder_file_settings_attributes_values(self,settings_value):
        self.driver.click("network_folder_file_setting_set_file_name_button")
        network_folder_file_name_prefix = settings_value[0]
        default_file_name = settings_value[1]
        user_ediatable = settings_value[2]
        network_folder_file_name_suffix = settings_value[3]
        default_colour_preference = settings_value[4]
        default_output_quality = settings_value[5]
        default_file_type = settings_value[6]
        default_resolution = settings_value[7]
        grey_scale_tiff_compression_method = settings_value[8]
        pdf_encryption = settings_value[9]
        blank_page_suppression= settings_value[10]
        self.update_network_folder_file_settings_prefix_value(network_folder_file_name_prefix)
        self.driver.send_keys("email_and_network_folder_default_file_name_text_box",default_file_name)
        self.driver.click("email_and_network_folder_file_name_popup_save_button")
        self.driver.click("network_folder_file_setting_set_file_name_button")
        if user_ediatable == "false":
            self.driver.click("email_and_network_folder_file_name_user_editable_checkbox")
            self.driver.click("email_and_network_folder_file_name_popup_save_button")
        self.update_network_folder_file_setting_suffix_value(network_folder_file_name_suffix)
        self.update_network_folder_file_original_size()
        self.update_network_folder_file_default_colour_preference(default_colour_preference)
        self.update_network_folder_file_default_output_quality(default_output_quality)
        self.update_network_folder_file_default_resolution(default_resolution)
        self.update_network_folder_file_settings_only_default_output(grey_scale_tiff_compression_method)
        self.update_network_folder_file_default_file_type_and_compression(default_file_type,pdf_encryption)
        self.update_blank_network_folder_file_page_suppression(blank_page_suppression)

    def update_network_folder_file_settings_prefix_value(self,network_folder_file_name_prefix):
        self.driver.click("email_and_network_folder_default_file_name_text_box")
        self.driver.click("email_and_network_folder_file_settings_file_name_prefix_dropdown")
        if network_folder_file_name_prefix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("network_folder_file_name_prefix_month_date_year_option")
        elif network_folder_file_name_prefix == "%DEVICE_DATE_MMDDYYYY%":
            self.driver.click("network_folder_file_name_prefix_year_month_date_option")
        elif network_folder_file_name_prefix == "%DEVICE_DATE_YYMMDD%":
            self.driver.click("network_folder_file_name_prefix_year_year_month_date_option")
        elif network_folder_file_name_prefix == "%DEVICE_DATE_YYYYMMDD%":
            self.driver.click("network_folder_file_name_prefix_time_option")
        elif network_folder_file_name_prefix == "%DEVICE_TIME_HHMMSS%":
            self.driver.click("network_folder_file_name_prefix_username_option")
        elif network_folder_file_name_prefix == "%SECURITY_USERNAME%":
            self.driver.click("network_folder_file_name_prefix_hostname_option")
        elif network_folder_file_name_prefix == "%DEVICE_HOSTNAME%":
            self.driver.click("network_folder_file_prefix_device_hostname_pqdn_option")
        else:
            self.driver.click("network_folder_file_name_prefix_date_month_year_option")
        if self.driver.get_attribute("network_folder_file_name_icon_plus_btn", "aria-disabled", raise_e=False) == "false":
            self.driver.click("network_folder_file_name_icon_plus_btn")
        # self.driver.click("email_and_network_folder_file_name_popup_save_button")
        # self.driver.click("network_folder_file_setting_set_file_name_button")
       
    def update_network_folder_file_setting_suffix_value(self,network_folder_file_name_suffix):
        self.driver.click("email_and_network_folder_file_file_name_suffix_dropdown")
        if network_folder_file_name_suffix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("network_folder_file_name_suffix_month_date_year_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_DATE_MMDDYYYY%")
        elif network_folder_file_name_suffix == "%DEVICE_DATE_MMDDYYYY%":
            self.driver.click("network_folder_file_name_suffix_year_month_date_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_DATE_YYMMDD%")
        elif network_folder_file_name_suffix == "%DEVICE_DATE_YYMMDD%":
            self.driver.click("network_folder_file_name_suffix_year_year_month_date_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_DATE_YYYYMMDD%")
        elif network_folder_file_name_suffix == "%DEVICE_DATE_YYYYMMDD%":
            self.driver.click("network_folder_file_name_suffix_time_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_TIME_HHMMSS%")
        elif network_folder_file_name_suffix == "%DEVICE_TIME_HHMMSS%":
            self.driver.click("network_folder_file_name_suffix_username_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%SECURITY_USERNAME%")
        elif network_folder_file_name_suffix == "%SECURITY_USERNAME%":
            self.driver.click("network_folder_file_name_suffix_hostname_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_HOSTNAME%")
        elif network_folder_file_name_suffix == "%DEVICE_HOSTNAME%":
            self.driver.click("network_folder_file_suffix_device_hostname_pqdn_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_HOSTNAME_PQDN%")
        else:
            self.driver.click("network_folder_file_name_suffix_date_month_year_option")
            self.driver.send_keys("network_folder_file_name_suffix_text_box","%DEVICE_DATE_DDMMYYYY%")

        self.driver.click("email_and_network_folder_file_name_popup_save_button")
   
    def update_network_folder_file_original_size(self):
        self.driver.click("network_folder_file_original_size_dropdown")
        self.driver.click("network_folder_file_original_size_a4_option")
   
    def update_network_folder_file_default_colour_preference(self,default_colour_preference):
        self.driver.click("network_folder_file_default_colour_preference_dropdown")
        if default_colour_preference == "autoDetect":
            self.driver.click("network_folder_file_black_option")
        elif default_colour_preference == "monochrome":
            self.driver.click("network_folder_file_black_or_grey_option")
        elif default_colour_preference == "grayscale":
            self.driver.click("network_folder_file_colour_option")
        else:
            self.driver.click("network_folder_file_automatically_detect_color_or_black_option")
   
    def update_network_folder_file_default_output_quality(self,default_output_quality):
        self.driver.click("network_folder_file_default_output_quality_dropdown")
        if default_output_quality == "high":
            self.driver.click("network_folder_file_default_output_quality_low_option")
        elif default_output_quality == "low":
            self.driver.click("network_folder_file_default_output_quality_medium_option")
        else:
            self.driver.click("network_folder_file_default_output_quality_high_option")
       
    def update_network_folder_file_default_resolution(self,default_resolution):
        self.driver.click("network_folder_file_default_resolution_dropdown")
        if default_resolution == "e75Dpi":
            self.driver.click("network_folder_file_default_resolution_150_dpi_option")
        # elif default_resolution == "e150Dpi":
        #     self.driver.click("network_folder_file_default_resolution_240_dpi_option")
        elif default_resolution == "e240Dpi":
            self.driver.click("network_folder_file_default_resolution_400_dpi_option")
        elif default_resolution == "e400Dpi":
            self.driver.click("network_folder_file_default_resolution_600_dpi_option")
        else:
            self.driver.click("network_folder_file_default_resolution_75_dpi_option")
   
    def update_network_folder_file_settings_only_default_output(self,grey_scale_tiff_compression_method):
        if grey_scale_tiff_compression_method != "lzw":
            self.driver.click("network_folder_file_default_file_type_dropdown")
            self.driver.click("network_folder_file_type_mtiff_option")
            self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("network_folder_file_grey_scale_tiff_compression_method_dropdown",timeout=10))
            if self.driver.get_attribute("network_folder_file_grey_scale_tiff_compression_method_dropdown","aria-disabled") == "false":
                self.driver.click("network_folder_file_grey_scale_tiff_compression_method_dropdown")
                self.driver.click("network_folder_file_grey_scale_tiff_compression_method_lzw_option")
       
    def update_network_folder_file_default_file_type_and_compression(self,default_file_type,pdf_encryption):
        self.driver.click("network_folder_file_default_file_type_dropdown")
        if default_file_type == "pdf":
            self.driver.click("network_folder_file_file_type_pdfa_option")
        elif default_file_type == "pdfa":
            self.driver.click("network_folder_file_type_mtiff_option")
        else:
            self.driver.click("network_folder_file_file_type_pdf_option")
        if self.driver.get_attribute("email_and_network_folder_file_pdf_encryption_checkbox","aria-disabled") == "false":
            if pdf_encryption == "false":
                self.driver.click("email_and_network_folder_file_pdf_encryption_checkbox")
           
    def update_blank_network_folder_file_page_suppression(self,blank_page_suppression):
        if self.driver.get_attribute("email_and_network_folder_file_blank_page_suppression_checkbox", "aria-hidden") == "false":
            if blank_page_suppression == "false":
                self.driver.click("email_and_network_folder_file_blank_page_suppression_checkbox")
            else:
                self.driver.click("email_and_network_folder_file_blank_page_suppression_checkbox")

    def set_email_file_settings_attributes_values(self,settings_value):
        self.driver.click("email_file_setting_set_file_name_button")
        email_file_name_prefix = settings_value[0]
        default_file_name = settings_value[1]
        user_ediatable = settings_value[2]
        email_file_name_suffix = settings_value[3]
        default_output_quality = settings_value[4]
        default_resolution = settings_value[5]
        grey_scale_tiff_compression_method = settings_value[6]
        pdf_encryption = settings_value[7]
        blank_page_suppression = settings_value[8]
        self.update_email_file_setting_prefix_value(email_file_name_prefix)
        self.driver.send_keys("email_and_network_folder_default_file_name_text_box",default_file_name)
        if user_ediatable == "false":
            self.driver.click("email_file_name_user_editable_checkbox")
        self.update_email_file_setting_suffix_value(email_file_name_suffix)
        self.update_email_file_settings_original_size()
        self.update_email_file_settings_color_grey_scale_tiff_compression_method(grey_scale_tiff_compression_method)
        self.update_email_file_default_output_quality_resolution_file_type_compression_pdf_encryption(default_output_quality,default_resolution)
        self.update_email_file_setting_pdf_encyrption_and_blank_page_suppression(pdf_encryption,blank_page_suppression)

    def update_email_file_setting_prefix_value(self,email_file_name_prefix):
        self.driver.click("email_and_network_folder_file_settings_file_name_prefix_dropdown")
        if email_file_name_prefix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("email_file_name_prefix_month_date_year_option")
        elif email_file_name_prefix == "%DEVICE_DATE_MMDDYYYY%":
            self.driver.click("email_file_name_prefix_device_hostname_pqdn_option")
        else:
            self.driver.click("email_file_name_prefix_date_month_year_option")
       
    def update_email_file_setting_suffix_value(self,email_file_name_suffix):
        self.driver.click("email_and_network_folder_file_file_name_suffix_dropdown")
        if email_file_name_suffix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("email_file_name_suffix_month_date_year_option")
        elif email_file_name_suffix == "%DEVICE_DATE_MMDDYYYY%":
            self.driver.click("email_file_name_suffix_device_hostname_pqdn_option")
        else:
            self.driver.click("email_file_name_suffix_date_month_year_option")
        self.driver.click("email_and_network_folder_file_name_popup_save_button")
   
    def update_email_file_settings_original_size(self):
        self.driver.click("email_file_original_size_dropdown")
        sleep(5)
        self.driver.js_click("email_file_original_size_a4_option")
   
    def update_email_file_settings_color_grey_scale_tiff_compression_method(self,grey_scale_tiff_compression_method):
        if grey_scale_tiff_compression_method != "lzw":
            self.driver.click("email_file_default_file_type_dropdown")
            self.driver.click("email_file_file_type_mtiff_option")
            self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("email_file_grey_scale_tiff_compression_method_dropdown",timeout=10))
            self.driver.click("email_file_grey_scale_tiff_compression_method_dropdown")
            self.driver.click("email_file_grey_scale_tiff_compression_method_lzw_option")
       
    def update_email_file_default_output_quality_resolution_file_type_compression_pdf_encryption(self,default_output_quality,default_resolution):
        self.toggle = random.choice([True, False])
        if default_output_quality == "medium":
            self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("email_file_default_output_quality_dropdown",timeout=10))
            self.driver.click("email_file_default_output_quality_dropdown")
            self.driver.click("email_file_default_output_quality_high_option")
            self.driver.click("email_file_default_resolution_dropdown")
            self.driver.click("email_file_default_resolution_300_dpi_option")
            self.driver.click("email_file_default_file_type_dropdown")
            self.driver.click("email_file_file_type_pdf_option")
            if self.driver.get_attribute("email_file_compression_dropdown","aria-disabled") == "false":
                self.driver.click("email_file_compression_dropdown")
                self.driver.click("email_file_compression_normal_option")
        elif default_output_quality == "high":
            self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("email_file_default_output_quality_dropdown",timeout=10))
            self.driver.click("email_file_default_output_quality_dropdown")
            self.driver.click("email_file_default_output_quality_low_option")
            if default_resolution == "e300Dpi" or default_resolution != "e75Dpi" or default_resolution != "e400Dpi":
                if self.toggle:
                    self.driver.click("email_file_default_resolution_dropdown")
                    self.driver.click("email_file_default_resolution_75_dpi_option")
                    self.driver.click("email_file_default_file_type_dropdown")
                    self.driver.click("email_file_file_type_pdf_option")
                    self.toggle = False
                else:
                    self.driver.click("email_file_default_resolution_dropdown")
                    self.driver.click("email_file_default_resolution_400_dpi_option")
                    self.driver.click("email_file_default_file_type_dropdown")
                    self.driver.click("email_file_file_type_pdf_option")
                    self.toggle = True
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("email_file_default_output_quality_dropdown",timeout=10))
            self.driver.click("email_file_default_output_quality_dropdown")
            self.driver.click("email_file_default_output_quality_medium_option")
            if default_resolution != "e100Dpi" or default_resolution != "e300Dpi":
                if self.toggle:
                    self.driver.click("email_file_default_resolution_dropdown")
                    self.driver.click("email_file_default_resolution_150_dpi_option")
                    self.driver.click("email_file_default_file_type_dropdown")
                    self.driver.click("email_file_file_type_pdf_option")
                    self.toggle = False
                else:
                    self.driver.click("email_file_default_resolution_dropdown")
                    self.driver.click("email_file_default_resolution_300_dpi_option")
                    self.driver.click("email_file_default_file_type_dropdown")
                    self.driver.click("email_file_file_type_pdf_option")
                    if self.driver.get_attribute("email_file_compression_dropdown","aria-disabled") == "false":
                        self.driver.click("email_file_compression_dropdown")
                        self.driver.click("email_file_compression_normal_option")
                    self.toggle = True
       
    def update_email_file_setting_pdf_encyrption_and_blank_page_suppression(self,pdf_encryption,blank_page_suppression):
        if self.driver.get_attribute("email_and_network_folder_file_pdf_encryption_checkbox", "aria-hidden") == "false":
            if pdf_encryption == "false":
                    self.driver.click("email_and_network_folder_file_pdf_encryption_checkbox")
            else:
                self.driver.click("email_and_network_folder_file_pdf_encryption_checkbox")
        if self.driver.get_attribute("email_and_network_folder_file_blank_page_suppression_checkbox", "aria-hidden") == "false":
            if blank_page_suppression == "false":
                self.driver.click("email_and_network_folder_file_blank_page_suppression_checkbox")
            else:
                self.driver.click("email_and_network_folder_file_blank_page_suppression_checkbox")

    def enter_bootloader_current_password(self,random_password):
        self.driver.send_keys("bootloader_current_password_textbox",random_password)
 
    def enter_bootloader_new_password(self,random_password):
        self.driver.send_keys("bootloader_new_password_textbox",random_password)
 
    def enter_bootloader_confirm_password(self, random_password):
        self.driver.send_keys("bootloader_confirm_password_textbox", random_password)
 
    def click_edit_setting_popup_save_button(self):
        self.driver.click("edit_setting_popup_save_button")
 
    def enter_properties_tab_pjl_password_textbox_value(self,password):
        return self.driver.send_keys("properties_tab_pjl_password_textbox",password)
 
    def enter_properties_tab_pjl_confirm_password_textbox_value(self,password):
        return self.driver.send_keys("properties_tab_pjl_confirm_password_textbox",password)
 
    def verify_security_snmp_v1_v2_properties_tab_setting_title(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("security_snmp_v1v2_properties_tab_setting_title"))
        if self.driver.verify_object_string("security_snmp_v1v2_properties_tab_setting_title") is True:
            return True
        else:
            raise UnexpectedItemPresentException("Title is not present")
 
    def enter_snmp_v1v2_read_community_name_password_textbox(self,password):
        return self.driver.send_keys("snmp_v1v2_read_community_name_password_textbox",password)
 
    def enter_snmp_v1v2_read_community_name_confirm_password_textbox(self,password):
        return self.driver.send_keys("snmp_v1v2_read_community_name_confirm_password_textbox",password)
 
    def enter_snmp_v1v2_read_write_community_name_password_textbox(self,password):
        return self.driver.send_keys("snmp_v1v2_read_write_community_name_password_textbox",password)
   
    def enter_snmp_v1v2_read_write_community_name_confirm_password_textbox(self,password):
        return self.driver.send_keys("snmp_v1v2_read_write_community_name_confirm_password_textbox",password)
 
    def verify_security_snmp_v3_properties_tab_setting_title(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("security_snmp_v3_properties_tab_setting_title"))
        if self.driver.verify_object_string("security_snmp_v3_properties_tab_setting_title") is True:
            return True
        else:
            raise UnexpectedItemPresentException("Title is not present")
 
    def enter_snmp_v3_username_textbox(self,username):
        return self.driver.send_keys("snmp_v3_user_name_textbox",username)
 
    def update_snmp_v3_authentication_passphase(self,passphase):
        self.driver.send_keys("snmp_v3_authentication_password_textbox",passphase)
        return self.driver.send_keys("snmp_v3_authentication_confirm_password_textbox",passphase)

    def update_snmp_v3_privacy_passphase(self,passphase):
        self.driver.send_keys("snmp_v3_privacy_password_textbox",passphase)
        return self.driver.send_keys("snmp_v3_privacy_confirm_password_textbox",passphase)
        
    def click_snmp_v1v2_disable_option(self):
        return self.driver.click("snmp_v1v2_disable_radio_btn")
 
    def click_snmp_v1v2_read_only_radio_btn(self):
        return self.driver.click("snmp_v1v2_read_only_radio_btn")
 
    def click_snmp_v1v2_read_write_radio_btn(self):
        return self.driver.click("snmp_v1v2_read_write_radio_btn")
 
    def click_snmp_v3_option(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("snmp_v3_checkbox"))
        return self.driver.click("snmp_v3_checkbox")
    
    def update_snmpv1v2_as_read_only_and_snmpv3_attribute_as_enable(self,settings_value):
        username = settings_value[0]
        min_password_length = settings_value[1]
        snmpv3_max_attempts = settings_value[2]
        snmpv3_reset_attempts_after_sec = settings_value[3]
        lockout_duration_min = settings_value[4]
        self.click_snmp_v3_option()
        self.enter_snmp_v3_username_textbox(username)
        self.driver.send_keys("snmp_v3_minimum_password_length_textbox",min_password_length)
        self.update_snmp_v3_authentication_passphase("Test123$")
        sleep(2)
        self.update_snmp_v3_privacy_passphase("Test12345$")
        self.driver.click("snmp_v3_account_lockout_checkbox")
        self.driver.send_keys("snmp_v3_maximum_attempts_textbox",snmpv3_max_attempts)
        self.driver.send_keys("snmp_v3_reset_attempts_after_textbox",snmpv3_reset_attempts_after_sec)
        self.driver.send_keys("snmp_v3_lockout_duration_textbox",lockout_duration_min)
 
    def update_snmpv1v2_and_v3_setting_attributes_as_disable(self,setting_card):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card(setting_card)
        self.driver.click("snmpv1v2_enable_checkbox")
        self.click_snmp_v3_option()
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
 
    def update_snmpv1v2_and_v3_setting_attributes_as_read_write_and_disable(self, setting_card):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card(setting_card)
        self.driver.click("snmpv1v2_enable_checkbox")
        self.click_snmp_v1v2_read_write_radio_btn()
        self.enter_snmp_v1v2_read_community_name_password_textbox("1")
        self.enter_snmp_v1v2_read_community_name_confirm_password_textbox("1")
        self.enter_snmp_v1v2_read_write_community_name_password_textbox("1")
        self.enter_snmp_v1v2_read_write_community_name_confirm_password_textbox("1")
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
        sleep(5)

    def update_stored_data_pin_protection_attribute_values(self, settings_value):
        four_digit_pin = settings_value[0]
        pin_required_to_store_a_scan = settings_value[1]
        pin_requireded_driver_stored_jobs = settings_value[2]
        cancel_pin_jobs = settings_value[3]
        if four_digit_pin == "false":
            self.driver.click("stored_data_pin_protection_four_digit_pin_checkbox")
        if pin_required_to_store_a_scan == "false":
            self.driver.click("stored_data_pin_protection_pin_required_to_store_a_scan_checkbox")
        if pin_requireded_driver_stored_jobs == "false":
            self.driver.click("stored_data_pin_protection_pin_required_for_driver_stored_jobs_checkbox")
        if cancel_pin_jobs == "false":
            self.driver.click("stored_data_pin_protection_cancel_pin_jobs_checkbox")

    def update_home_screen_customization_future_smart_setting_attributes(self):
        self.driver.click("home_screen_customization_import_reference_button")
        self.driver.send_keys("home_screen_import_device_data_popup_search_textbox", "VNBE400101")
        self.driver.click("home_screen_import_device_data_popup_device_model_name")
        self.driver.click("home_screen_import_device_data_popup_select_button")
        self.driver.click("home_screen_application_dropdown")
        self.driver.click("home_screen_application_tescopy_option")

    def update_home_screen_customization_future_smart_to_default_hp_or_samsung(self, setting_card):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card(setting_card)
        self.driver.click("home_screen_application_dropdown")
        self.driver.click("home_screen_application_default_hp_option")
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
        self.dismiss_toast()

    ################################### Modify Device Specific Policy Settings ####################################

    def navigating_to_device_page_from_printers_details_tab(self,serial_number):
        self.click_devices_printers_button()
        self.search_printers(serial_number)
        self.click_first_entry_link()
        self.verify_printers_details_page_policies_tab()
        self.click_printers_details_page_policies_tab()

    def get_policies_device_list_compliance_status(self):
        return self.driver.get_text("policies_compliance_status_widget_compliance_status")
    
    def get_policies_compliance_status_widget_compliance_status_reason(self):
        return self.driver.get_text("policies_compliance_status_widget_compliance_status_reason")

    def verify_policies_compliance_status(self,serial_number):
        count = 0
        while count < 5:
            if self.get_policies_device_list_compliance_status() == "Compliant":
                return True
            else:
                sleep(5)
                self.navigating_to_device_page_from_printers_details_tab(serial_number)
                count+=1
        raise PolicyNoncompliantException("Assigned Policy is Non Compliant")

    def verify_pjl_password_configuration_update_in_properties_tab(self, serial_number):
        for _ in range(5):
            if self.get_printer_device_details_device_property_value("pjl-password") == "Configured":
                return True
            else:
                sleep(5)
                self.navigating_to_device_page_from_printers_details_tab(serial_number)
                self.click_printers_details_page_properties_tab()
                self.click_security_accordion()
                self.click_printer_device_details_device_property_card("pjl-password")
        raise AssertionError("PJL Password Configuration is not updated in properties tab")
 
    def updating_security_accordion_snmpv1v2_widget(self, serial_number):
        self.navigating_to_device_page_from_printers_details_tab(serial_number)
        self.click_printers_details_page_properties_tab()
        self.click_security_accordion()
        self.click_printer_device_details_device_property_card("snmp-v1-v2")
 
    def verify_snmp_v1v2_read_only_update_status_in_properties_tab(self, serial_number):
        for _ in range(5):
            if self.get_printer_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read Only Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv1v2_widget(serial_number)
        raise AssertionError("SNMP V1/V2 Read Only Access is not updated in properties tab")
 
    def verify_snmp_v1v2_read_and_write_update_status_in_properties_tab(self, serial_number):
        for _ in range(5):
            if self.get_printer_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read and Write Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv1v2_widget(serial_number)
        raise AssertionError("SNMP V1/V2 Read Write Access is not updated in properties tab")
 
    def updating_security_accordion_snmpv3_widget(self, serial_number):
        self.navigating_to_device_page_from_printers_details_tab(serial_number)
        self.click_printers_details_page_properties_tab()
        self.click_security_accordion()
        self.click_printer_device_details_device_property_card("snmp-v3")
 
    def verify_snmp_v3_enabled_status_in_properties_tab(self, serial_number):
        for _ in range(5):
            if self.get_printer_device_details_device_property_value("snmp-v3-enabled") == "Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv3_widget(serial_number)
        raise AssertionError("SNMP V3 Enabled status is not updated in properties tab")
 
    def verify_snmp_v3_disabled_status_in_properties_tab(self,serial_number):
        for _ in range(5):
            if self.get_printer_device_details_device_property_value("snmp-v3-enabled") == "Disabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv3_widget(serial_number)
        raise AssertionError("SNMP V3 Disabled status is not updated in properties tab")

    def get_printer_device_details_authentication_property_value(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_device_details_authentication_property_value", timeout=15))
        return self.driver.wait_for_object("printer_device_details_authentication_property_value", timeout=15).text
 
    def verify_802x_authentication_configuration_update_in_properties_tab(self, server_id, serial_number):
        for _ in range(5):
            if self.get_printer_device_details_authentication_property_value() == server_id:
                return True
            else:
                sleep(5)
                self.navigating_to_device_page_from_printers_details_tab(serial_number)
                self.click_printers_details_page_properties_tab()
                self.click_security_accordion()
                self.click_printer_device_details_device_property_card("dot1x-authentication")
        raise AssertionError("802.1x Authentication Configuration is not updated in properties tab")

    def enter_ews_admin_password_textbox_value(self, password):
        return self.driver.send_keys("ews_admin_password_textbox", password)
 
    def enter_ews_admin_confirm_password_textbox_value(self, password):
        return self.driver.send_keys("ews_admin_confirm_password_textbox", password)
    
    def update_outgoing_server_setting_attributes_value(self, settings_value):
        server_name = settings_value[0]
        port_number = settings_value[1]
        user_name = settings_value[2]
        password = settings_value[3]
       
        # Add first outgoing server
        self.driver.click("outgoing_server_list_add_button")
        self.driver.send_keys("outgoing_server_server_name_textbox", server_name)
        self.driver.send_keys("outgoing_server_port_textbox", port_number)
        self.driver.js_click("outgoing_server_use_authentication_checkbox")
        self.driver.click("outgoing_server_use_credential_control_panel_radio_button")
        self.driver.click("outgoing_server_server_usage_send_to_email_checkbox")
        self.driver.click("outgoing_server_server_usage_internet_fax_checkbox")
        self.driver.click("outgoing_server_add_popup_add_button")
       
        # Add second outgoing server with different usage credential and server usage
        self.driver.click("outgoing_server_list_add_button")
        self.driver.clear_text("outgoing_server_server_name_textbox")
        self.driver.send_keys("outgoing_server_server_name_textbox", "newsmtp.com")
        self.driver.clear_text("outgoing_server_port_textbox")
        self.driver.send_keys("outgoing_server_port_textbox", port_number)
        self.driver.js_click("outgoing_server_use_authentication_checkbox")
        self.driver.click("outgoing_server_enable_smtp_ssl_tls_protocol_checkbox")
        self.driver.click("outgoing_server_smtp_validate_certificates_for_outgoing_server")
        self.driver.click("outgoing_server_use_credential_defined_below_radio_button")
        self.driver.send_keys("outgoing_server_username_textbox", user_name)
        self.driver.send_keys("outgoing_server_password_textbox", password)
        self.driver.click("outgoing_server_server_usage_autosend_checkbox")
        self.driver.click("outgoing_server_add_popup_add_button")

    def update_smb_cifs_shared_folder_setting_attributes(self, settings_value):
        smb_v1 = settings_value[0]
        smb_v2 = settings_value[1]
        smb_v3 = settings_value[2]
        # Scenario 1: V1=true, V2=true, V3=true (all enabled in backend)
        # This would leave all UI disabled, so enable v3 to ensure at least one is selected
        if smb_v1 == "true" and smb_v2 == "true" and smb_v3 == "true":
            self.driver.click("smb_cifs_v3_radio_button")
            return
       
        # Scenario 2: V1=false, V2=true, V3=false  
        # Click v1 and v3, but that combination is not allowed, so only click v1
        elif smb_v1 == "false" and smb_v2 == "true" and smb_v3 == "false":
            self.driver.click("smb_cifs_v1_radio_button")
            return
       
        # Click to enable when backend value is "false"
        if smb_v1 == "false":
            self.driver.click("smb_cifs_v1_radio_button")
        if smb_v2 == "false":
            self.driver.click("smb_cifs_v2_radio_button")
        if smb_v3 == "false":
            self.driver.click("smb_cifs_v3_radio_button")

    def select_random_country_in_identity_certificate(self):
        self.driver.js_click("identity_certificate_country_dropdown")
        # here we have some contry dropdown, from the dropdown each time have to select random country
        country_codes = ['au', 'br', 'ca', 'cn', 'fr', 'de', 'in', 'ie', 'it', 'jp', 'mx', 'ru', 'sg', 'za', 'es', 'se', 'ch', 'tw', 'th', 'gb', 'us', 'vn']
        selected_country_code = random.choice(country_codes)
        self.driver.click("identity_certificate_country_option", format_specifier=[selected_country_code])
 
    def select_random_key_size_in_identity_certificate(self):
        self.driver.click("identity_certificate_key_size_dropdown")
        # here we have key size dropdown, from the dropdown each time have to select random key size
        key_sizes = ['2048', '3072', '4096']
        selected_key_size = random.choice(key_sizes)
        self.driver.click("identity_certificate_key_size_option", format_specifier=[selected_key_size])
 
    def select_random_encryption_key_in_identity_certificate(self):
        self.driver.click("identity_certificate_key_size_dropdown")
        key_length_options = ['p256', 'p384', 'p521']
        selected_key_length = random.choice(key_length_options)
        self.driver.click("identity_certificate_encryption_key_option", format_specifier=[selected_key_length])
 
    def select_random_algorithm_in_identity_certificate(self):
        # here we have algorithm radio buttons, need to select random algorithm each time
        algorithms = ['sha256', 'sha384', 'sha512']
        selected_algorithm = random.choice(algorithms)
        self.driver.click("identity_certificate_algorithm_{}_radio_button".format(selected_algorithm))
 
    def set_fqdn_as_source_of_common_name_in_identity_certiifcate(self, settings_value):
        organization_name = settings_value[0]
        organization_unit = settings_value[1]
        city_name = settings_value[2]
        state_name = settings_value[3]
        upn_username = settings_value[4]
        upn_domain = settings_value[5]
        est_connector_url = settings_value[6]
        est_connector_port = settings_value[7]
        est_server_username = settings_value[8]
        est_server_password = settings_value[9]
        arbitrary_label = settings_value[10]
        certificate_renewal_threshold = settings_value[11]
        self.driver.click("identity_certificate_fqdn_as_common_name_radio_button")
        self.driver.send_keys("identity_certificate_organization_name_text_box", organization_name)
        self.driver.send_keys("identity_certificate_organization_unit_text_box", organization_unit)
        self.driver.send_keys("identity_certificate_city_name_text_box", city_name)
        self.driver.send_keys("identity_certificate_state_name_text_box", state_name)
        self.select_random_country_in_identity_certificate()
        # Click IP Address and UPN checkbox from SAN options
        self.driver.click("identity_certificate_ip_address_checkbox")
        self.driver.click("identity_certificate_upn_checkbox")
        self.driver.send_keys("identity_certificate_upn_username_text_box", upn_username)
        self.driver.send_keys("identity_certificate_upn_domain_text_box", upn_domain)
        self.driver.click("uncheck_check_san_in_policy_assessment_checkbox")
        self.driver.click("rsa_encryption_key_radio_button")
        self.select_random_key_size_in_identity_certificate()
        self.select_random_algorithm_in_identity_certificate()
        self.driver.send_keys("identity_certificate_est_connector_url_text_box", est_connector_url)
        self.driver.send_keys("identity_certificate_est_connector_port_text_box", est_connector_port)
        self.driver.send_keys("identity_certificate_est_server_username_text_box", est_server_username)
        self.driver.send_keys("identity_certificate_est_server_password_text_box", est_server_password)
        self.driver.send_keys("identity_certificate_arbitrary_label_text_box", arbitrary_label)
        self.driver.send_keys("identity_certificate_renewal_threshold_text_box", certificate_renewal_threshold)
 
    def update_ip_address_as_common_name_in_identity_certificate_setting(self, setting_card):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("identity-certificate")
        self.driver.click("identity_certificate_ip_address_as_common_name_radio_button")
        self.driver.click("identity_certificate_fqdn_checkbox")
        self.driver.click("identity_certificate_hostname_checkbox")
        self.driver.click("uncheck_check_san_in_policy_assessment_checkbox")
        self.driver.click("ecdsa_encryption_key_radio_button")
        self.select_random_encryption_key_in_identity_certificate()
        self.driver.click("uncheck_authenticate_with_est_user_credentials_checkbox")
        self.driver.send_keys("est_certificate_serial_number_text_box", "hp-est-3")
        self.driver.send_keys("est_certificate_password_text_box", "eeZq_uiJkwJU@X@46Ls")
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
        self.dismiss_toast()

    def modify_devices_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Devices Category Settings: Asset Number, Company Name, Contact Person, Device Location, Device Name, Control Panel Language, Retain Print Job, Use Requested Tray, Date/Time Format, Sleep Settings,
        # Manual Feed Prompt, Override A4/Letter, Size / Type Prompt, Tray 1 Mode / Manual Feed, Online Solutions, Show Date and Time, Duplex Binding, Home Screen Customization - FutureSmart, Retain Temporary Print Jobs after Reboot
        # Temporary Job Storage Limit 
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "ctrl-panel-language":
            if settings_value == "es":
                self.select_control_panel_language("Russian")
            else:
                self.select_control_panel_language("Spanish")
        elif setting_card == "retain-jobs":
            # self.click_ignore_unsupported_item_toggle()
            self.update_temporary_and_standard_retain_jobs_setting_attributes(settings_value)
        elif setting_card == "use-requested-tray":
            if settings_value == "exclusively":
                self.driver.click("user_requested_tray_first_radio_button")
            else:
                self.driver.click("user_requested_tray_exclusively_radio_button")
        elif setting_card == "date-time-format":
            self.set_devices_date_and_time_format(settings_value)
        elif setting_card == "sleep-settings":
            self.set_sleep_settings(settings_value)
        elif setting_card == "manual-feed-prompt":
            if settings_value == "always":
                self.driver.click("manual_feed_prompt_unless_loaded")
            else:
                self.driver.click("manual_feed_prompt_always")
        elif setting_card == "override-letter-a4":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "size-type-prompt":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "manual-feed":
            if settings_value == "false":
                self.driver.click("manual_feed_first_radio_button")
            else:
                self.driver.click("manual_feed_cassette_radio_button")
        elif setting_card == "energy-setting":
            inactivityTimeout = settings_value[0]
            shutdownTimeout = settings_value[1]
            self.set_energy_settings_inactivity(inactivityTimeout)
            self.set_energy_settings_shutdown(shutdownTimeout)
        elif setting_card == "auto-send":
            self.update_auto_send_setting_attributes(settings_value)
        elif setting_card == "time-zone":
            self.set_time_zone_setting(settings_value)
        elif setting_card == "online-solutions":
            self.update_online_solutions_setting_attributes(settings_value)
        elif setting_card == "show-date-time":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "duplex-binding":
            if settings_value == "oneSided":
                self.driver.click("duplex_binding_long_edge_radio_button")
            elif settings_value == "long_edge":
                self.driver.click("duplex_binding_short_edge_radio_button")
            else:
                self.driver.click("duplex_binding_none_one_sided_radio_button")
        elif setting_card == "outgoing-servers":
            self.update_outgoing_server_setting_attributes_value(settings_value)
        elif setting_card == "home-screen-custom":
            self.update_home_screen_customization_future_smart_setting_attributes()
        elif setting_card == "retain-jobs-after-reboot":
            if settings_value == "all":
                self.driver.click("retain_jobs_after_reboot_do_not_retain_radio_button")
            elif settings_value == "off":
                self.driver.click("retain_jobs_after_reboot_personal_job_radio_button")
            elif settings_value == "personal":
                self.driver.click("retain_jobs_after_reboot_retain_radio_button") 
            elif setting_card == "job-storage-limit-temporary":
                temporary_job_storage_limit = settings_value
                self.driver.clear_text("temporary_job_storage_limit_textbox")
                self.driver.send_keys("temporary_job_storage_limit_textbox", temporary_job_storage_limit)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_network_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Network Category Settings: Support Contact, System Location, System Contact, Wins Port, Wins Registration, Web Services (WS) Discovery, WS-Print, Internet Print Protocol, Secure Internet Print Protocol, TFTP Configuration File, 
        # Telnet, Line Printer Daemon, LLMNR, SLP, Standard TCP/IP Printing (P9100), DHCPv4 FQDN compliance with RFC 4702, FTP Print, AirPrint, AirPrint Fax, Web Scan, Bonjour, IPv4 Multicast, IPv6 Information,
        # TCP/IP Configuration Method, DNS Server, FIPS 140 Compliance Library
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "wins-port":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "wins-registration":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ws-discovery":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ws-print":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ipp":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ipps":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "tftp-cfg":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "telnet":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "lpd-lpr":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "llmnr":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "slp":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "tcpip-print":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_tcp_ip_printing_remediation_checkbox()
        elif setting_card == "dhcp-v4-compliance":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ftp-print":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "airprint":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "airprint-fax":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "web-scan":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "bonjour":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ipv4-multicast":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ipv6-info":
            self.update_ipv6_information_setting_attributes(setting_card,settings_value )
        elif setting_card == "tcpip-config":
            self.update_tcpip_configuration_method_setting_value(settings_value)
        elif setting_card == "dns-server":
            self.enter_dns_server_setting_attributes_value(settings_value)
        elif setting_card == "configuration-precedence":
            self.update_configuration_precedence_method_setting_value(settings_value)
        elif setting_card == "fips-140-compliance":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_supplies_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Supplies Category Settings: Cartridge Threshold - Black, Cartridge Threshold - Cyan, Cartridge Very Low Action - Black, Cartridge Very Low Action - Color, Cartridge Very Low Action - Black, Cartridge Very Low Action - Color
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "cartridge-threshold-black":
            self.driver.send_keys("cartridge_threshold_black_text_box",settings_value)
        elif setting_card == "cartridge-threshold-cyan":
            self.driver.send_keys("cartridge_threshold_cyan_text_box",settings_value)
        elif setting_card == "cartridge-threshold-magenta":
            self.driver.send_keys("cartridge_threshold_magenta_text_box",settings_value)
        elif setting_card == "cartridge-threshold-yellow":
            self.driver.send_keys("cartridge_threshold_yellow_text_box",settings_value)
        elif setting_card == "very-low-action-black":
            self.set_cartridge_very_low_action_black(settings_value[0])
        elif setting_card == "very-low-action-color":
            self.set_cartridge_very_low_action_color(settings_value[1])
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_security_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Security Category Settings: HP Jetdirect XML Services, Remote Firmware Update (RFU), Require HTTPS Redirect, Printer Job Language (PJL) Password, Printer Job Language (PJL) Access Commands, Restrict Color, Service Access Code,
        # Cross-Origin Resource Sharing (CORS), Control Panel Timeout, CSRF, Direct Connect Ports, Host USB Plug and Play, Information Tab, PostScript Security, SNMPv1/v2, SNMPv3, Secure Boot Presence, Whitelisting Presence, Verify Certificate for IPP/IPPS Pull Printing, Intrusion Detection Presence, Device Announcement Agent,
        # Check for Latest Firmware, Digital Sending Service, Display Color Usage Job Log Page on Information Tab, Embedded Web Server Access, Disk Encryption Status, Stored Data PIN Protection, Bootloader Password, LDAP Setup, 802 .1x Authentication (Wired), 802.1x Authentication (Wireless),
        # SMB/CIFS (Shared Folder), EWS Admin Password
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "jd-xml-svc":
            if settings_value == True:
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "remote-fw-update":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "https-redirect":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "pjl-password":
            self.click_remediation_toggle()
        elif setting_card == "pjl-command":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "restrict-color":
            self.set_restrict_color_status(settings_value)
        elif setting_card == "svc-access-code":
            self.driver.send_keys("service_access_code_text_box",settings_value)
            self.driver.send_keys("service_access_code_confirm_text_box",settings_value)
        elif setting_card == "cors":
            self.update_cors_origin_settings_values(settings_value,setting_card)
        elif setting_card == "ctrl-panel-timeout":
                self.enter_control_panel_timeout_value(settings_value)
        elif setting_card == "csrf-prevention":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "dc-ports":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "host-usb-pnp":
            self.update_host_usb_plug_and_play_setting_attributes(settings_value)
        elif setting_card == "info-tab":
            self.update_information_tab_setting_attributes(settings_value)
        elif setting_card == "ps-security":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "snmp-v1-v2":
            if settings_value == "true":
                self.driver.click("snmp_v1v2_disable_radio_btn")
        elif setting_card == "snmp-v3":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "snmp":
            # self.driver.click("snmpv1v2_enable_checkbox")
            self.update_snmpv1v2_as_read_only_and_snmpv3_attribute_as_enable(settings_value)
        elif setting_card == "secure-boot-presence":
            self.verify_secure_boot_presence_option_is_disabled()
        elif setting_card == "whitelist-presence":
            self.verify_whitelisting_presence_option_is_disabled()
        elif setting_card == "whitelist-presence":
            self.verify_whitelisting_presence_option_is_disabled()
        elif setting_card == "remote-fw-update":
            self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "verify-certificate":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "intrusion-detect-presence":
            self.verify_intrusion_detection_presence_option_is_disabled()
        elif setting_card == "device-announcement":
            self.set_ip_values_and_auth_status_for_device_announcement_setting(setting_card,settings_value)
        elif setting_card == "check-latest":
            pass
        elif setting_card == "digital-sending":
            self.update_digital_sending_service_setting_attributes(settings_value)
        elif setting_card == "color-usage-log":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "ews-access":
            pass
        elif setting_card == "disk-encryption":
            pass
        elif setting_card == "legacy-fw-update":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "pin-protection":
            self.update_stored_data_pin_protection_attribute_values(settings_value)
        elif setting_card == "bootloader-password":
            self.enter_bootloader_new_password(settings_value)
            self.enter_bootloader_confirm_password(settings_value)
        elif setting_card == "ldap-setup":
            self.update_ldap_setup_setting_attributes(settings_value)
        elif setting_card == "802-1x-auth":
            self.verify_security_802_1x_authentication_wired_setting_attribute_value(settings_value)
        elif setting_card == "802-1x-auth-wifi":
            self.verify_security_802_1x_authentication_wireless_setting_attribute_value(settings_value)
        elif setting_card == "smb-cifs":
            self.update_smb_cifs_shared_folder_setting_attributes(settings_value)
        elif setting_card == "ews-password":
            self.enter_ews_admin_password_textbox_value("Test@123")
            self.enter_ews_admin_confirm_password_textbox_value("Test@123")
            self.driver.click("ews_password_password_complexity_checkbox")
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_firmware_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Firmware Category Settings: Auto Firmware Update
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "auto-fw-update":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_file_system_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # File System Category Settings: File System Access Protocols, File Erase Mode
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "fs-access-protocol":
            ps_file_system_access_enabled_status = settings_value[0]
            pjl_file_system_access_enabled_status = settings_value[1]
            if ps_file_system_access_enabled_status == "false":
                self.driver.click("ps_access_option")
            if pjl_file_system_access_enabled_status == "false":
                self.driver.click("pjl_access_option")
        elif setting_card == "file-erase":
            if settings_value == "secureFastErase":
                self.driver.click("file_erase_non_secure_radio_button")
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_digital_sending_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Digital Sending Category Settings: Save To Network Folder, Save to SharePoint, Send to Email, Email Notification Settings, Email Scan Settings, Network Folder Notification Settings,
        # Email Address / Message Settings, Email File Settings, Network Folder File Settings, Allow access to LDAP address book
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "save-to-network-folder":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "save-to-share-point":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "save-to-email":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        elif setting_card == "email-notification":
            self.set_email_notification_settings(settings_value)
        elif setting_card == "email-scan":
            self.set_email_scan_settings(settings_value)
        elif setting_card == "network-folder-notification":
            self.set_network_folder_notification_settings(settings_value)
        elif setting_card == "email-message":
            self.set_email_address_message_in_email_setting_attributes(settings_value)
        elif setting_card == "network-folder-file":
            self.set_network_folder_file_settings_attributes_values(settings_value)
        elif setting_card == "email-file":
            self.set_email_file_settings_attributes_values(settings_value)
        elif setting_card == "ldap-ab-access":
            self.update_ldap_address_book_access_setting_attributes(settings_value)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_ews_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # EWS Category Settings: EWS Language, Time Services
        sleep(7)
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "ews-language":
            self.set_languages_in_ews_language_setting(settings_value)
        elif setting_card == "time-services":
            self.set_port_value_and_server_ip_address_for_time_services_settings(settings_value)

    def modify_web_services_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Web Services Category Settings: HP JetAdvantage (More Apps), Proxy Server, Smart Cloud Print
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "hp-jet-adv":
            hp_jetadvantage = settings_value[0]
            hp_jetadvantage_accountcreation = settings_value[1]
            if hp_jetadvantage == "true":
                self.click_proxy_device_settings_checkbox("hp-jet-adv.check")
            else:
                if hp_jetadvantage_accountcreation == "true":
                    self.click_proxy_device_settings_checkbox("hp-jet-adv.create-account")
        elif setting_card == "proxy-server":
            self.set_server_address_and_port_value_for_proxy_server_settings(setting_card,settings_value)
        elif setting_card == "smart-cloud-print":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_copier_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Copier Category Settings: Copy Paper Tray Selection, Copy Darkness, Copy Sharpness, Copy Optimize Text or Picture, Copy Background Cleanup, Copy Contrast
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "copy-tray":        
            self.click_copy_tray_paper_option_selection_dropdown()
            if settings_value == "auto":
                self.select_copy_tray_paper_select_action_dropdown_option("manual")
            elif settings_value == "manual":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-1")
            elif settings_value == "tray-1":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-2")
            elif settings_value == "tray-2":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-3")
            elif settings_value == "tray-3":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-4")
            elif settings_value == "tray-4":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-5")
            elif settings_value == "tray-5":
                self.select_copy_tray_paper_select_action_dropdown_option("auto")
            else:
                self.select_copy_tray_paper_select_action_dropdown_option("auto")
        elif setting_card == "copy-darkness":
            self.click_copy_darkness_option_selection_dropdown()
            if settings_value == 1:
                self.select_copy_darkness_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_darkness_select_action_dropdown_option(3)
            elif settings_value == 3:
                self.select_copy_darkness_select_action_dropdown_option(4)
            elif settings_value == 4:
                self.select_copy_darkness_select_action_dropdown_option(5)
            elif settings_value == 5:
                self.select_copy_darkness_select_action_dropdown_option(6)
            elif settings_value == 6:
                self.select_copy_darkness_select_action_dropdown_option(7)
            elif settings_value == 7:
                self.select_copy_darkness_select_action_dropdown_option(8)
            elif settings_value == 8:
                self.select_copy_darkness_select_action_dropdown_option(9)
            elif settings_value == 9:
                self.select_copy_darkness_select_action_dropdown_option(1)
            else:
                self.select_copy_darkness_select_action_dropdown_option(5)
        elif setting_card == "copy-sharpness":
            self.click_copy_sharpness_option_selection_dropdown()
            if settings_value == 1:
                self.select_copy_sharpness_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_sharpness_select_action_dropdown_option(3)
            elif settings_value == 3:
                self.select_copy_sharpness_select_action_dropdown_option(4)
            elif settings_value == 4:
                self.select_copy_sharpness_select_action_dropdown_option(5)
            elif settings_value == 5:
                self.select_copy_sharpness_select_action_dropdown_option(1)
            else:
                self.select_copy_sharpness_select_action_dropdown_option(3)
        elif setting_card == "copy-optimize":
            if settings_value == "photo":
                self.click_copy_optimize_photograph_radio_button()
            elif settings_value == "glossy":
                self.click_copy_optimize_text_radio_button()
            elif settings_value == "text":
                self.click_copy_optimize_mixed_radio_button()
            elif settings_value == "mixed":
                self.click_copy_optimize_printed_picture_radio_button()
        elif setting_card == "copy-bg-cleanup":
            self.click_copy_background_cleanup_policy_contextual_footer_select_action_dropdown()
            if settings_value == 1:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(3)
            elif settings_value == 3:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(4)
            elif settings_value == 4:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(5)
            elif settings_value == 5:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(6)
            elif settings_value == 6:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(7)
            elif settings_value == 7:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(8)
            elif settings_value == 8:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(9)
            elif settings_value == 9:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(1)
            else:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(3)
        elif setting_card == "copy-contrast":
            self.click_copy_contrast_policy_contextual_footer_select_action_dropdown()
            if settings_value == 1:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(2)
            elif settings_value == 2:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(3)
            elif settings_value == 3:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(4)
            elif settings_value == 4:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(5)
            elif settings_value == 5:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(6)
            elif settings_value == 6:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(7)
            elif settings_value == 7:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(8)
            elif settings_value == 8:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(9)
            elif settings_value == 9:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(1)
            else:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(5)
        else:
            self.enter_device_property_value(settings_value,setting_card)

    def modify_fax_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Fax Category Settings: Fax Header Settings,Fax Receive Settings, Fax Send Settings, IP Fax Settings, PC Fax Send Settings
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "fax-header":
            self.set_fax_header_Settings_attributes(settings_value)
        elif setting_card == "fax-receive":
            self.set_fax_receive_method_for_fax_receive_setting(setting_card,settings_value)
        elif setting_card == "fax-send":
            self.set_fax_send_method_for_fax_send_setting(setting_card,settings_value)
        elif setting_card == "ip-fax":
            fax_ip = settings_value[0]
            company_name = settings_value[1]
            self.driver.send_keys("ip_fax_settings_company_name_text_box",fax_ip)
            self.driver.send_keys("ip_fax_settings_fax_id_text_box",company_name)
        elif setting_card == "pc-fax-send":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)

    def modify_certificate_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Identity Certificate
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "identity-certificate":
            self.set_fqdn_as_source_of_common_name_in_identity_certiifcate(settings_value)
        
    def remove_settings_in_device_specific_policy_tab(self, setting_name):
        self.click_printers_details_page_policies_tab()
        self.click_printers_details_policies_tab_edit_button()
        self.search_policy_settings(setting_name)
        sleep(5)  # Wait for the search results to load
        self.click_device_specific_policy_checkbox()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_remove_button()
        self.check_policy_removed_toast_successful_msg("Device-Specific Policy has been removed.")

    def navigating_to_device_page_from_printers_details_hp_secure_fleet_tab(self,serial_number):
        self.click_devices_printers_button()
        self.search_printers(serial_number)
        self.click_first_entry_link()
        self.click_printers_details_page_hp_secure_fleet_manager_tab()
        self.select_report("assessment")
        self.verify_details_report_loaded()
    
    def verify_assessment_status_report(self,serial_number):
        self.select_report("assessment")
        self.verify_details_report_loaded()
        for _ in range(2):  # Attempt up to 2 times
            if self.get_report_result() == "Passed":
                return True
            else:
                sleep(3)
                self.navigating_to_device_page_from_printers_details_hp_secure_fleet_tab(serial_number)
        raise SettingValueMismatchException("Assigned Setting Value is Mismatch")

    def click_printer_firmware_update_checkbox(self):
        return self.driver.click("printer_firmware_update_checkbox")
    
    def set_energy_settings_inactivity(self, inactivityTimeout):
        self.driver.click("energy_settings_inactivity_dropdown")
        if inactivityTimeout == 1:
            self.driver.click("energy_settings_off_inactivity_five_minutes_option")
        elif inactivityTimeout == 5:
            self.driver.click("energy_settings_off_inactivity_fifteen_minutes_option")
        elif inactivityTimeout == 15:
            self.driver.click("energy_settings_off_inactivity_thirty_minutes_option")
        elif inactivityTimeout == 30:
            self.driver.click("energy_settings_off_inactivity_one_hour_option")
        else:
            self.driver.click("energy_settings_off_inactivity_one_minute_option")

    def set_energy_settings_shutdown(self, shutdownTimeout):
        self.driver.click("energy_settings_shutdown_inactivity_dropdown")
        if shutdownTimeout == 120:
            self.driver.click("energy_settings_shutdown_inactivity_four_hour_option")
        elif shutdownTimeout == 240:
            self.driver.click("energy_settings_shutdown_inactivity_eight_hour_option")
        else:
            self.driver.click("energy_settings_shutdown_inactivity_two_hour_option")
        
    def set_auto_send_every_days_and_weeks_values(self,auto_send_frequency_unit_status,days,weeks,months,pages):
        if auto_send_frequency_unit_status == "days":
            self.driver.click("auto_send_every_weeks_radio_button")
            self.driver.send_keys("auto_send_every_days_and_month_textbox", weeks)
        elif auto_send_frequency_unit_status == "weeks":
            self.driver.click("auto_send_every_months_radio_button")
            self.driver.send_keys("auto_send_every_days_and_month_textbox", months)
        elif auto_send_frequency_unit_status == "months":
            self.driver.click("auto_send_every_pages_radio_button")
            self.driver.send_keys("auto_send_every_days_and_month_textbox", pages)
        else:
            self.driver.click("auto_send_every_days_radio_button")
            self.driver.send_keys("auto_send_every_days_and_month_textbox", days)

    def set_values_for_send_to_hp_and_send_to_url(self,send_to_url_list_status,https_url):
        self.driver.click("auto_send_to_hp_using_https_checkbox")
        if send_to_url_list_status == "false":
            self.driver.click("auto_send_to_url_checkbox")
            self.driver.js_click("auto_send_to_url_add_button") 
            self.driver.send_keys("auto_send_to_url_web_address_textbox",https_url)
            self.driver.click("auto_send_add_popup_add_button")

    def set_values_for_send_to_email_address(self,send_to_email_address,email_address):
        if send_to_email_address == "false":
            self.driver.click("auto_send_to_email_checkbox")
            self.driver.js_click("auto_send_to_email_add_button")
            self.driver.send_keys("auto_send_to_email_email_address_textbox",email_address)
            self.driver.click("auto_send_add_popup_add_button")

    def update_auto_send_setting_attributes(self, settings_value):
        auto_send_enabled_status = settings_value[0]
        auto_send_frequency_unit_status = settings_value[1]
        days = settings_value[2]
        weeks = settings_value[3]
        months = settings_value[4]
        pages = settings_value[5]
        send_to_url_list_status = settings_value[6]
        https_url = settings_value[7]
        send_to_email_address = settings_value[8]
        email_address = settings_value[9]
        if auto_send_enabled_status == "true":
            self.click_set_options_settings_checkbox("auto-send")
        else:
            self.set_auto_send_every_days_and_weeks_values(auto_send_frequency_unit_status,days,weeks,months,pages)
            self.set_values_for_send_to_hp_and_send_to_url(send_to_url_list_status,https_url)
            self.set_values_for_send_to_email_address(send_to_email_address,email_address)
        
    def click_select_an_option_dropdown(self):
        return self.driver.click("time_zone_select_an_option_dropdown")
    
    def click_africa_Casablanca_option(self):
        return self.driver.click("time_zone_africa_casablanca_option")
    
    def click_africa_harare_option(self):
        return self.driver.click("time_zone_africa_harare_option")
        
    def click_africa_nairobi_option(self):
        return self.driver.click("time_zone_africa_nairobi_option")
    
    def click_africa_tripoli_option(self):
        return self.driver.click("time_zone_africa_tripoli_option")
    
    def click_asia_bangkok_option(self):
        return self.driver.click("time_zone_asia_bangkok_option")
    
    def click_asia_beirut_option(self):
        return self.driver.click("time_zone_asia_beirut_option")
    
    def click_africa_algiers_option(self):
        return self.driver.click("time_zone_west_center_africa_option")
    
    def click_dst_option(self):
        return self.driver.click("time_zone_dst_checkbox")
    
    def set_time_zone_setting(self,settings_value):
        time_zone_day_light_saving_status=settings_value[0]
        self.click_select_an_option_dropdown()
        if time_zone_day_light_saving_status == "Africa/Algiers":
            self.click_africa_Casablanca_option()
            self.click_dst_option()
        elif time_zone_day_light_saving_status == "Africa/Casablanca":
            self.click_africa_harare_option()
        elif time_zone_day_light_saving_status == "Africa/Harare":
            self.click_africa_nairobi_option()
        elif time_zone_day_light_saving_status == "Africa/Nairobi":
            self.click_africa_tripoli_option()
        elif time_zone_day_light_saving_status == "Africa/Tripoli":
            self.click_asia_bangkok_option()
        elif time_zone_day_light_saving_status == "Asia/Bangkok":
            self.click_asia_beirut_option()
            self.click_dst_option()
        else:
            self.click_africa_algiers_option()

    ############################### Printer details - HP SDS Event Log tab ####################################

    def verify_hp_sds_event_log_tab_event_log_title(self):
        return self.driver.verify_object_string("hp_sds_event_log_tab_event_log_title",timeout=30)
    
    def verify_hp_sds_event_log_tab_event_log_description(self):
        return self.driver.verify_object_string("hp_sds_event_log_tab_event_log_description",timeout=20)

    def verify_sds_event_log_tab_event_log_table_loaded(self):
        # It verifies printers sds table is loaded and has lists of events
        if self.driver.wait_for_object("sds_table_entries_with_type", timeout=30, raise_e=False):
            return True
        else:
            self.verify_sds_event_log_tab_event_log_table_is_empty_msg()
            raise PrintersTableEmpty("SDS Event log table is empty")
    
    def verify_sds_event_log_tab_event_log_table_is_empty_msg(self):
        self.driver.wait_for_object("sds_event_log_tab_event_log_table_empty_msg_img",timeout=20)
        return self.driver.wait_for_object("sds_event_log_tab_event_log_table_empty_msg")

    def verify_sds_event_log_tab_filters_button(self):
        return self.driver.verify_object_string("sds_event_log_tab_filters_button")
    
    def verify_sds_event_log_tab_column_options_button(self):
        return self.driver.wait_for_object("sds_event_log_tab_column_options_button")

    def verify_sds_event_log_tab_event_log_table_headers(self):
        sds_event_log_table_headers = []
        headers = self.driver.find_object("sds_event_log_table_headers", multiple=True)

        for header in headers:
            # Strip out the button label and other unwanted text within the header
            header_text = header.text.strip()
            
            # Check if there's an unwanted extra part like "descending sorted" and remove it
            if 'descending sorted' in header_text:
                header_text = header_text.replace('descending sorted', '').strip()
            
            # Append the cleaned text to the list
            sds_event_log_table_headers.append(header_text)

        # Return the cleaned headers without the last item (which seems to be empty)
        headers = sds_event_log_table_headers[:-1]
        return headers

    def click_sds_event_log_tab_filters_button(self):
        return self.driver.click("sds_event_log_tab_filters_button")

    ################################## LDAP Sign-In Settings ####################################

    def update_ldap_setup_setting_attributes(self, settings_value):
        # ldap_server_address, port_number, bind_prefix, root_name, match_attribute, email_attribute, display_name_attribute, group_attribute
        ldap_server_address = settings_value[0]
        port_number = settings_value[1]
        bind_prefix = settings_value[2]
        root_name = settings_value[3]
        match_attribute = settings_value[4]
        email_attribute = settings_value[5]
        display_name_attribute = settings_value[6]
        group_attribute = settings_value[7]
        self.driver.click("ldap_sign_in_enable_checkbox")
        self.driver.send_keys("ldap_server_address_textbox", ldap_server_address)
        self.driver.send_keys("ldap_port_number_textbox", port_number)
        self.click_ldap_use_ssl_checkbox()
        mfp_radio_btn = self.driver.wait_for_object("ldap_mfp_user_credentials_radio_button")
        if mfp_radio_btn.is_selected() is False:
            self.driver.click("ldap_mfp_user_credentials_radio_button")
        self.driver.send_keys("ldap_bind_prefix_textbox", bind_prefix)
        self.driver.js_click("ldap_bind_and_search_add_button")
        self.driver.send_keys("ldap_root_name_textbox", root_name)
        self.driver.click("ldap_add_root_popup_add_button")
        self.driver.send_keys("ldap_match_attribute_textbox", match_attribute)
        self.driver.send_keys("ldap_email_attribute_textbox", email_attribute)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.driver.find_object("ldap_display_name_attribute_textbox"))
        self.driver.send_keys("ldap_display_name_attribute_textbox", display_name_attribute)
        self.driver.send_keys("ldap_group_attribute_textbox", group_attribute)
        self.click_ldap_exact_match_checkbox()

    def click_ldap_use_ssl_checkbox(self):
        return self.driver.js_click("ldap_use_ssl_checkbox")

    def click_ldap_exact_match_checkbox(self):
        return self.driver.js_click("ldap_exact_match_checkbox")

    def click_ldap_enable_checkbox(self):
        return self.driver.click("ldap_sign_in_enable_checkbox")

    def update_ldap_admin_credentials_settings(self,setting_name, setting_card=None, settings_value=None):
        ldap_server_address = settings_value[0]
        port_number = settings_value[1]
        domain_name = settings_value[2]
        root_name = settings_value[3]
        match_attribute = settings_value[4]
        email_attribute = settings_value[5]
        display_name_attribute = settings_value[6]
        group_attribute = settings_value[7]

        self.click_compliance_status_widget()
        self.click_policy_widget()
        if self.verify_device_specific_policy_card_empty() is False:
            self.remove_existing_device_specific_policy()
        self.click_printers_details_policies_tab_edit_button()
        self.search_policy_settings(setting_name)
        sleep(4) # Added sleep to wait for the search results to load
        self.click_device_specific_policy_checkbox()
        sleep(3)
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("ldap-setup")
        self.click_ignore_unsupported_item_toggle()
        self.click_ldap_enable_checkbox()
        self.driver.send_keys("ldap_server_address_textbox", ldap_server_address)
        self.driver.send_keys("ldap_port_number_textbox", port_number)
        self.click_ldap_use_ssl_checkbox()
        self.driver.click("ldap_admin_credentials_radio_button")
        self.driver.send_keys("ldap_admin_username_textbox", domain_name)
        self.driver.send_keys("ldap_admin_password_textbox", "1")
        self.driver.js_click("ldap_bind_and_search_add_button")
        self.driver.send_keys("ldap_root_name_textbox", root_name)
        self.driver.click("ldap_add_root_popup_add_button")
        self.driver.send_keys("ldap_match_attribute_textbox", match_attribute)
        self.driver.send_keys("ldap_email_attribute_textbox", email_attribute)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.driver.find_object("ldap_display_name_attribute_textbox"))
        self.driver.send_keys("ldap_display_name_attribute_textbox", display_name_attribute)
        self.driver.send_keys("ldap_group_attribute_textbox", group_attribute)
        self.click_ldap_exact_match_checkbox()        
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()

    def update_ldap_use_ssl_and_exact_match_settings(self, setting_card=None):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("ldap-setup")
        self.click_ldap_use_ssl_checkbox()
        self.click_ldap_exact_match_checkbox()
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()

    ############################# LDAP Address Book Access Settings ###############################
 
    def click_ldap_address_book_enable_checkbox(self):
        return self.driver.click("ldap_address_book_enable_checkbox")
 
    def update_ldap_address_book_access_setting_attributes(self, settings_value):
        ldap_server_address = settings_value[0]
        port_number = settings_value[1]
        starting_point_directory = settings_value[2]
        ldap_search_filter = settings_value[3]
        self.click_ldap_address_book_enable_checkbox()
        self.driver.send_keys("ldap_address_book_server_address_textbox", ldap_server_address)
        self.driver.send_keys("ldap_address_book_port_number_textbox", port_number)
        self.click_ldap_use_ssl_checkbox()
        self.driver.click("ldap_address_book_no_authentication_radio_button")
        self.driver.send_keys("ldap_address_book_starting_point_directory_textbox", starting_point_directory)
        # Updating Source for Attribute Name
        self.driver.click("ldap_address_book_active_directory_default_radio_button")
        self.driver.send_keys("ldap_address_book_search_filter_textbox", ldap_search_filter)
 
    # Disable SSL and change Windows Domain Authentication
    def update_ldap_ssl_and_change_windows_domain_authentication_settings(self, setting_card=None):
        self.click_printers_details_policies_tab_edit_button()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("ldap-ab-access")
        self.click_ldap_use_ssl_checkbox()
        self.driver.click("ldap_address_book_windows_domain_authentication_radio_button")
        self.driver.send_keys("ldap_address_book_windows_domain_textbox", "testdomain" + str(random.randint(1, 9)) + ".com")
        self.driver.send_keys("ldap_address_book_username_textbox", "ldapuser" + str(random.randint(1, 9)))
        self.driver.send_keys("ldap_address_book_password_textbox", "Test@123")
        # Updating Source for Attribute Name
        self.driver.js_click("ldap_address_book_exchange_55_default_radio_button")
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
 
    def update_allow_access_to_ldap_address_book_with_custom_attributes(self,setting_name, setting_card=None, settings_value=None):
        ldap_server_address = settings_value[0]
        port_number = settings_value[1]    
        starting_point_directory = settings_value[2]
        match_attribute = settings_value[3]
        email_attribute = settings_value[4]
        fax_number_attribute = settings_value[5]
        ldap_search_filter = settings_value[6]
 
        self.click_compliance_status_widget()
        self.click_policy_widget()
        if self.verify_device_specific_policy_card_empty() is False:
            self.remove_existing_device_specific_policy()
        self.click_printers_details_policies_tab_edit_button()
        self.search_policy_settings(setting_name)
        sleep(4) # Added sleep to wait for the search results to load
        self.click_device_specific_policy_checkbox()
        sleep(3)
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_settings_card("ldap-ab-access")
        self.click_ignore_unsupported_item_toggle()
        self.click_ldap_address_book_enable_checkbox()
        self.driver.send_keys("ldap_address_book_server_address_textbox", ldap_server_address)
        self.driver.send_keys("ldap_address_book_port_number_textbox", port_number)
        self.driver.js_click("ldap_use_ssl_checkbox")
        self.driver.click("ldap_use_simple_authentication_radio_button")
        self.driver.send_keys("ldap_address_book_username_textbox", "ldapuser" + str(random.randint(1, 9)))
        self.driver.send_keys("ldap_address_book_password_textbox", "Test@123")
        self.driver.send_keys("ldap_address_book_starting_point_directory_textbox", starting_point_directory)
        # Updating Source for Attribute Name
        self.driver.js_click("ldap_address_book_custom_attributes_radio_button")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.driver.find_object("ldap_address_book_match_attribute_textbox"))
        self.driver.send_keys("ldap_address_book_match_attribute_textbox", match_attribute)
        self.driver.send_keys("ldap_address_book_email_attribute_textbox", email_attribute)
        self.driver.send_keys("ldap_address_book_fax_number_attribute_textbox", fax_number_attribute)
        self.driver.send_keys("ldap_address_book_search_filter_textbox", ldap_search_filter)
        self.click_device_specific_policy_create_button()
        self.click_change_not_recommended_popup_confirm_button()
 
    ############################################# SDS Event Log Tab ###########################################

    def click_sds_event_log_tab_column_options_button(self):
        return self.driver.click("sds_event_log_tab_column_options_button")
    
    def verify_sds_event_log_tab_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title")

    def verify_sds_event_log_tab_column_options_popup_reset_to_default_button(self):
        return self.driver.wait_for_object("column_options_popup_reset_to_default_btn")

    def verify_sds_event_log_tab_column_options_popup_cancel_button(self):
        return self.driver.wait_for_object("column_options_popup_cancel_btn")

    def verify_sds_event_log_tab_column_options_popup_save_button(self):
        return self.driver.wait_for_object("column_options_popup_save_btn")

    def get_sds_event_log_tab_column_options_popup_options(self):
        options = []
        column_options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in column_options:
            options.append(option.text)
        return options

    def click_sds_event_log_table_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "Code":
            options[0].click()
        elif option == "Description":
            options[1].click()
        elif option == "Recommended action":
            options[2].click()

    def click_sds_event_log_tab_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def verify_sds_event_log_table_column(self,column_name,displayed=True):
        if column_name == "Code":
                return self.driver.wait_for_object("event_log_table_code_column_header", invisible=not displayed, timeout=60)
        elif column_name == "Description":
                return self.driver.wait_for_object("event_log_table_description_column_header", invisible=not displayed, timeout=60)
        elif column_name == "Recommended action":
                return self.driver.wait_for_object("event_log_table_recommended_action_column_header", invisible=not displayed, timeout=60)

    def click_sds_event_log_tab_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def get_sds_event_log_table_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        table_entry_data = self.driver.find_object("sds_event_log_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]
   
    def get_all_event_logs_code(self):
        return self.get_all_event_logs("event_log_code")
    
    def get_all_event_logs_description(self):
        return self.get_all_event_logs("event_log_description")
    
    def get_all_event_logs_type(self):
        return self.get_all_event_logs("event_log_type")
    
    def get_all_event_logs_cycle(self):
        return self.get_all_event_logs("event_log_cycle")

    def get_all_event_logs_firmware_version(self):
        return self.get_all_event_logs("event_log_firmware_version")

    def get_all_event_logs_date(self):
        return self.get_all_event_logs("event_log_date")

    def get_all_event_logs(self, column_name):
        logs = self.get_sds_event_log_table_column_data(column_name, to_lower=True)
        count = self.get_total_entries()

        if count > 100:
            if self.driver.get_attribute("_shared_page_prev_nav_btn", "aria-disabled", raise_e=False) == "false":
                self.driver.click("_shared_page_prev_nav_btn")
            else:
                self.driver.click("_shared_page_next_nav_btn")
            logs.extend(self.get_sds_event_log_table_column_data(column_name, to_lower=True))
        return logs

    def parse_event_log_date(self, date_str):
        now = datetime.now()
        if "just now" in date_str:
            return now.replace(microsecond=0)
        elif "minute" in date_str:
            minutes = int(date_str.split()[0])
            return (now - timedelta(minutes=minutes)).replace(microsecond=0)
        elif "hour" in date_str:
            hours = int(date_str.split()[0])
            return (now - timedelta(hours=hours)).replace(microsecond=0)
        elif "yesterday" in date_str:
            return (now - timedelta(days=1)).replace(microsecond=0)
        elif "day" in date_str and "yesterday" not in date_str:
            days = int(date_str.split()[0])
            return (now - timedelta(days=days)).replace(microsecond=0)

        else:
            try:
                return datetime.strptime(date_str, "%b %d, %Y %I:%M %p").replace(microsecond=0)
            except ValueError:
                return datetime.strptime(date_str, "%b %d, %Y").replace(microsecond=0)

    def verify_event_log_date_is_sorted(self, date_list, order="ascending"):
        """
        Check if the list is sorted in the specified order.
        
        :param date_list: List of date strings to check.
        :param order: The order to check for. Can be "ascending" or "descending".
        :return: True if sorted in the specified order, False otherwise.
        """
        logging.info(f"Date string: {date_list}")
        # Convert the date strings to datetime objects
        date_objects = [self.parse_event_log_date(date) for date in date_list]
        logging.info(f"Date objects: {date_objects}")
        
        if order == "ascending":
            return all(date_objects[i] <= date_objects[i + 1] for i in range(len(date_objects) - 1))
        elif order == "descending":
            return all(date_objects[i] >= date_objects[i + 1] for i in range(len(date_objects) - 1))
        else:
            raise ValueError("Invalid order specified. Use 'ascending' or 'descending'.")

    def verify_event_log_filter_side_bar_title(self,displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("event_log_filter_side_bar_title", invisible=not displayed, timeout=20,raise_e=False)
        return self.driver.verify_object_string("event_log_filter_side_bar_title")

    def verify_event_log_filter_side_bar_clear_all_button(self):
        return self.driver.verify_object_string("event_log_filter_side_bar_clear_all_button")
    
    def click_event_log_filter_side_bar_clear_all_button(self):
        return self.driver.click("event_log_filter_side_bar_clear_all_button")
    
    def verify_event_log_filter_side_bar_event_type_dropdown_label(self):
        return self.driver.verify_object_string("event_log_filter_side_bar_event_type_dropdown_label")
    
    def verify_event_log_filter_side_bar_event_type_dropdown(self):
        return self.driver.wait_for_object("event_log_filter_side_bar_event_type_dropdown")
    
    def click_event_log_filter_side_bar_event_type_dropdown(self):
        return self.driver.click("event_log_filter_side_bar_event_type_dropdown")
    
    def verify_event_log_filter_side_bar_timeframe_dropdown_label(self):
        return self.driver.verify_object_string("event_log_filter_side_bar_timeframe_dropdown_label")
    
    def verify_event_log_filter_side_bar_timeframe_dropdown(self):
        return self.driver.wait_for_object("event_log_filter_side_bar_timeframe_dropdown")

    def click_event_log_filter_side_bar_timeframe_dropdown(self):
        return self.driver.click("event_log_filter_side_bar_timeframe_dropdown")
    
    def click_event_log_filter_side_bar_done_button(self):
        return self.driver.click("event_log_filter_side_bar_done_button")

    def get_event_log_filter_side_bar_event_type_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("event_log_filter_side_bar_event_type_dropdown_options", multiple=True)
        for option in all_options:
            # Split the text by newline characters to get individual options
            actual_options.extend(option.text.split('\n'))
        return actual_options
    
    def get_event_log_filter_side_bar_timeframe_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("event_log_filter_side_bar_timeframe_dropdown_options",multiple=True)
        for option in all_options:
            # Split the text by newline characters to get individual options
            actual_options.extend(option.text.split('\n'))
        return actual_options
    
    def select_event_log_filter_timeframe_dropdown_options(self,option):
        options = self.driver.find_object("event_log_filter_side_bar_timeframe_dropdown_options", multiple = True)    
        if option == "Last 7 days":
            options[0].click()
        elif option == "Last 30 days":
            options[1].click()
        elif option == "Last 60 days":
            options[2].click()
        elif option == "Last 90 days":
            options[3].click()
        elif option == "Custom":
            options[4].click()
    
    def select_event_log_filter_event_type_dropdown_options(self,option):
        options = self.driver.find_object("event_log_filter_side_bar_event_type_dropdown_options", multiple = True)
        if option == "All":
            options[0].click()
        elif option == "Error":
            options[1].click()
        elif option == "Warning":
            options[2].click()
        elif option == "Info":
            options[3].click()

    def get_event_log_filter_side_bar_event_type_dropdown_selected_option(self):
        return self.driver.get_text("event_log_filter_side_bar_event_type_dropdown")
    
    def get_event_log_filter_side_bar_timeframe_dropdown_selected_option(self):
        return self.driver.get_text("event_log_filter_side_bar_timeframe_dropdown")
    
    def get_sds_event_log_table_all_event_logs_type(self):
        return self.get_sds_event_log_table_column_data("event_log_type", to_lower=True)
    
    def click_sds_event_log_table_first_guide_me_link(self):
        # Check if the link is present
        if self.driver.wait_for_object("event_log_table_first_guide_me_link",raise_e=False):
            return self.driver.click("event_log_table_first_guide_me_link")
        else:
            # Click on the code column
            self.click_table_header_by_name("event_log_code")
            # Attempt to click the link again
            return self.driver.click("event_log_table_first_guide_me_link")
    
    def get_sds_event_log_table_first_link_description(self):
        return self.driver.get_text("event_log_table_first_link_description")
    
    def verify_guide_me_link_page_loaded(self):
        new_window_name = "guide_me_link_window"
        self.driver.add_window_and_switch(new_window_name)
        if "entitlement" in self.driver.current_url:
            logging.info("Guide Me link page loaded successfully.")
            return True
        else:
            raise UnexpectedItemPresentException("Guide Me link page did not load as expected.")
    
    def verify_guide_me_link_page_description(self):
        return self.driver.get_text("guide_me_link_page_description")

    def get_sds_event_log_table_all_event_logs_date(self):
        return self.get_sds_event_log_table_column_data("event_log_date", to_lower=True)
   
    def verify_is_date_within_last_days(self, date_str, days):
        date = self.parse_event_log_date(date_str)
        return date >= datetime.now() - timedelta(days=days)
    
    def set_custom_timeframe(self, start_date, end_date):
        self.driver.send_keys("event_log_filter_side_bar_start_date", start_date)
        self.driver.send_keys("event_log_filter_side_bar_end_date", end_date)
    
    def verify_date_is_within_range(self, date_str, start_date, end_date):
        date = self.parse_event_log_date(date_str)
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return start <= date <= end