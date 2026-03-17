from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from datetime import datetime
from time import sleep
from selenium.common.exceptions import *
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
import logging

class PendingPrintersTableEmpty(Exception):
    pass

class DeviceSearchException(Exception):
    pass

class PrinterSearchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class FilterValueException(Exception):
    pass

class WrongToastException(Exception):
    pass

class PendingPrinters(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "devices_pendingprinters"
   
    #######################3############## Main Menu verifys ########################################

    def verify_devices_pending_printers_button(self):
        return self.driver.wait_for_object("devices_pending_printers_button")

    def click_devices_pending_printers_button(self):
        return self.driver.click("devices_pending_printers_button")

    def verify_devices_pending_printers_table_loaded(self):
        # It verifies pending printers table is loaded and has lists of printers entry.
        if self.driver.wait_for_object("pending_printers_table_data", timeout=30, raise_e=False):
            return True
        else:
            raise PendingPrintersTableEmpty("Pending Printers table is empty")

    def verify_pending_printers_search_textbox(self):
        return self.driver.wait_for_object("pending_printers_search_textbox")
   
    def verify_pending_printers_add_printers_button(self):
        return self.driver.wait_for_object("pending_printers_add_printers_button")

    def verify_pending_printers_delete_button(self, displayed=True):
        return self.driver.wait_for_object("pending_printers_delete_button", invisible=not displayed, timeout=30)
    
    def verify_pending_printers_no_of_items_selected_label(self, displayed=True):
        return self.driver.wait_for_object("pending_printers_no_of_items_selected_label", invisible=not displayed, timeout=30)

    def verify_pending_printers_select_all_button(self, displayed=True):
        return self.driver.wait_for_object("pending_printers_select_all_button", invisible=not displayed, timeout=30)
    
    def verify_pending_printers_refresh_button(self):
        return self.driver.wait_for_object("pending_printers_refresh_button")
    
    def verify_pending_printers_gear_button(self):
        return self.driver.wait_for_object("pending_printers_gear_button")
    
    def verify_pending_printers_filter_button(self):
        return self.driver.wait_for_object("pending_printers_filter_button")
    
    def verify_pending_printers_status_overview_card(self):
        return self.driver.wait_for_object("pending_printers_status_overview_card")
    
    def verify_devices_pending_printers_table_headers(self):
        printers_table_headers = []
        headers = self.driver.find_object("devices_pending_printers_table_headers", multiple=True)

        for header in headers:
            # Strip out the button label and other unwanted text within the header
            header_text = header.text.strip()
            
            # Check if there's an unwanted extra part like "descending sorted" and remove it
            if 'descending sorted' in header_text:
                header_text = header_text.replace('descending sorted', '').strip()
            
            # Append the cleaned text to the list
            printers_table_headers.append(header_text)

        return printers_table_headers

    def verify_pending_printers_status_overview_card_expanded(self):
        is_expanded = self.driver.get_attribute("pending_printers_status_overview_card_expand_button", "aria-expanded")
        assert is_expanded == 'true'

    def click_pending_printers_status_overview_card_expand_button(self):
        return self.driver.click("pending_printers_status_overview_card_expand_button")
    
    def verify_pending_printers_status_overview_card_title(self):
        return self.driver.verify_object_string("pending_printers_status_overview_card_title")
    
    def verify_pending_printers_status_overview_card_description(self):
        return self.driver.verify_object_string("pending_printers_status_overview_card_description")
    
    def verify_pending_printers_status_overview_action_needed_card(self):
        return self.driver.wait_for_object("pending_printers_status_overview_action_needed_card")
    
    def verify_pending_printers_status_overview_error_card(self):
        return self.driver.wait_for_object("pending_printers_status_overview_error_card")
    
    def verify_pending_printers_status_overview_connected_card(self):
        return self.driver.wait_for_object("pending_printers_status_overview_connected_card")

    def verify_pending_printers_action_needed_card_label(self):
        return self.driver.verify_object_string("pending_printers_action_needed_card_label")
    
    def verify_pending_printers_action_needed_card_label_icon(self):
        return self.driver.wait_for_object("pending_printers_action_needed_card_label_icon")
    
    def verify_pending_printers_action_needed_card_title(self):
        return self.driver.verify_object_string("pending_printers_action_needed_card_title")
    
    def verify_pending_printers_action_needed_card_description(self):
        return self.driver.verify_object_string("pending_printers_action_needed_card_description")
    
    def verify_pending_printers_action_needed_card_printers_count(self):
        return self.driver.wait_for_object("pending_printers_action_needed_card_printers_count")

    def verify_pending_printers_error_card_label(self):
        return self.driver.verify_object_string("pending_printers_error_card_label")
    
    def verify_pending_printers_error_card_label_icon(self):
        return self.driver.wait_for_object("pending_printers_error_card_label_icon")
    
    def verify_pending_printers_error_card_title(self):
        return self.driver.verify_object_string("pending_printers_error_card_title")
    
    def verify_pending_printers_error_card_description(self):
        return self.driver.verify_object_string("pending_printers_error_card_description")
    
    def verify_pending_printers_error_card_printers_count(self):
        return self.driver.wait_for_object("pending_printers_error_card_printers_count")

    def verify_pending_printers_connected_card_label(self):
        return self.driver.verify_object_string("pending_printers_connected_card_label")
    
    def verify_pending_printers_connected_card_label_icon(self):
        return self.driver.wait_for_object("pending_printers_connected_card_label_icon")
    
    def verify_pending_printers_connected_card_title(self):
        return self.driver.verify_object_string("pending_printers_connected_card_title")
    
    def verify_pending_printers_connected_card_description(self):
        return self.driver.verify_object_string("pending_printers_connected_card_description")

    def verify_pending_printers_connected_card_printers_count(self):
        return self.driver.wait_for_object("pending_printers_connected_card_printers_count")

    def get_pending_printers_connected_card_printers_count(self):
        total_count = self.driver.get_text("pending_printers_connected_card_printers_count")
        # Split the text to get the connected printer count from total count of printers
        count = int(total_count.split()[0])
        return count

    def get_pending_printers_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        sleep(5)
        table_entry_data = self.driver.find_object("printers_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]
   
    def get_all_pending_printers_date_added(self):
        return self.get_pending_printers_column_data("pending_printers_date_added")
    
    def get_all_pending_printers_serial_number(self):
        return self.get_pending_printers_column_data("pending_printers_serial_number")
    
    def get_all_pending_printers_product_number(self):
        return self.get_pending_printers_column_data("pending_printers_product_number")
    
    def get_all_pending_printers_status(self):
        return self.get_pending_printers_column_data("pending_printers_status")

    def get_pending_printer_status_by_serial_number(self, serial_number):
        """
        Returns the status (as a string) for the printer with the given serial number.
        """
        device_serial_number = self.get_pending_printers_column_data("pending_printers_serial_number")
        connectivity_status = self.get_pending_printers_column_data("pending_printers_status")
        for s, status in zip(device_serial_number, connectivity_status):
            if s == serial_number.lower():
                return status
        return None  # or raise an exception if not found

    def verify_pending_printers_connectivity_column_status(self, serial_number):
        for _ in range(7):
            status = self.get_pending_printer_status_by_serial_number(serial_number)
            if status == "connected":
                return
            self.click_pending_printers_refresh_button()
            self.verify_devices_pending_printers_table_loaded()
        assert False, "Printer is not in connected state"

    def check_toast_successful_message(self):
        message = self.driver.wait_for_object("bottom_toast_msg", timeout=30).text
        expected_message = "1 printers deleted. It can take a few minutes for the operation to complete."
        if message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + message + " expected message is: " + expected_message)

    def verify_pending_printers_empty_widget_no_results_msg_displayed(self):
        obj = self.driver.wait_for_object('pending_printers_empty_widget_no_results_msg', raise_e=False)
        if obj:
            return obj.text.strip() == "No pending printers found"
        return False
    
    def verify_pending_printers_removed(self):
        for _ in range(7):
            if self.verify_pending_printers_empty_widget_no_results_msg_displayed():
                return
            sleep(3) # Wait for the device to be removed from the table
            self.click_pending_printers_refresh_button()
        assert False, "Onboarded device is still present in Pending Printers"

    def parse_date(self, date_str):
        now = datetime.now()
        if "Just Now" in date_str:
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
            # Normalize the input string to capitalize the first letter of the month
            # date_str = date_str.capitalize()
            try:
                return datetime.strptime(date_str, "%d %b, %Y").replace(microsecond=0)
            except ValueError:
                try:
                    return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)
                except ValueError:
                    return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)
            
    def verify_printers_date_added_is_sorted(self, date_list, order="ascending"):
        """
        Check if the list is sorted in the specified order.
        
        :param date_list: List of date strings to check.
        :param order: The order to check for. Can be "ascending" or "descending".
        :return: True if sorted in the specified order, False otherwise.
        """
        self.select_page_size(500)  # Ensure the page size is set to 500 for the printers table
        # Convert the date strings to datetime objects
        date_objects = [self.parse_date(date) for date in date_list]
        
        if order == "ascending":
            return all(date_objects[i] <= date_objects[i + 1] for i in range(len(date_objects) - 1))
        elif order == "descending":
            return all(date_objects[i] >= date_objects[i + 1] for i in range(len(date_objects) - 1))
        else:
            raise ValueError("Invalid order specified. Use 'ascending' or 'descending'.")

    def search_pending_printers(self, search_text):
        #Currently only pressing enter triggers the search it's probably a bug
        #As there is also a search button that doesn't work
        self.driver.wait_for_object("pending_printers_search_textbox")
        self.verify_devices_pending_printers_table_loaded()
        sleep(3)
        for _ in range(3):
            try:
                return self.driver.send_keys("pending_printers_search_textbox", search_text, press_enter=True)
            except (StaleElementReferenceException,ElementNotInteractableException):
                logging.info("Search Printers Send_keys is not working")
                sleep(3)
        raise PrinterSearchException("After 3 tries still Search printers Send_keys is not working")

    def clear_pending_printers_search_results_box(self):
        self.driver.wait_for_object("pending_printers_search_textbox", timeout=20)
        return self.driver.clear_text("pending_printers_search_textbox")

    def verify_pending_printers_search_results(self, search_text, column_name):
        """
        Verify that all entries in the specified column contain the search text.
        
        :param search_text: The text to search for within the column entries.
        :param column_name: The name of the column to search within.
        :raises DeviceSearchException: If any entry does not contain the search text.
        :return: True if all entries contain the search text.
        """
        column_index = self.get_header_index(column_name)
        all_devices = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[column_index], multiple=True)
        for device_entry in all_devices:
            if search_text.lower() in device_entry.text.lower():
                continue
            else:
                raise DeviceSearchException(f"Device entry: {device_entry.text} does not contain the search string: {search_text}")
        return True

    def verify_search_results_by_serial_number(self, search_text):
        return self.verify_pending_printers_search_results(search_text, "pending_printers_serial_number")
    
    def verify_search_results_by_product_number(self, search_text):
        return self.verify_pending_printers_search_results(search_text, "pending_printers_product_number")

    def verify_search_results_by_status(self, search_text):
        return self.verify_pending_printers_search_results(search_text, "pending_printers_status")

    def verify_search_results_by_date_added(self, search_text):
        return self.verify_pending_printers_search_results(search_text, "pending_printers_date_added")

    def verify_no_items_found(self, raise_e=True):
        return self.driver.verify_object_string('pending_printers_table_no_items_found_msg', raise_e=raise_e)
    
    def verify_pending_printers_delete_button_status(self, status):
        if status == "enabled":
            if self.driver.wait_for_object("pending_printers_delete_button", raise_e=False):
                return True
        elif status == "disabled":
            if not self.driver.wait_for_object("pending_printers_delete_button", raise_e=False):
                return True
        else:
            raise UnexpectedItemPresentException("Pending Printers delete button is enabled")
        return False
        
    def click_pending_printers_checkbox(self):
        return self.driver.click("pending_printers_table_checkbox", timeout=30)
    
    def click_pending_printers_delete_button(self):
        return self.driver.click("pending_printers_delete_button", timeout=30)

    def verify_delete_confirmation_popup(self, displayed=True):
        return self.driver.wait_for_object("pending_printers_delete_confirmation_popup", invisible=not displayed, timeout=30)
    
    def click_delete_confirmation_popup_cancel_button(self):
        return self.driver.click("pending_printers_delete_confirmation_popup_cancel_button", timeout=30)
    
    def verify_delete_confirmation_popup_title(self):
        return self.driver.verify_object_string("pending_printers_delete_confirmation_popup_title")
    
    def verify_delete_confirmation_popup_message(self):
        return self.driver.verify_object_string("pending_printers_delete_confirmation_popup_message")
    
    def verify_delete_confirmation_popup_cancel_button(self):
        return self.driver.wait_for_object("pending_printers_delete_confirmation_popup_cancel_button")
    
    def verify_delete_confirmation_popup_delete_button(self):
        return self.driver.wait_for_object("pending_printers_delete_confirmation_popup_delete_button")
    
    def verify_delete_confirmation_popup_close_button(self):
        return self.driver.wait_for_object("pending_printers_delete_confirmation_popup_close_button")
    
    def click_delete_confirmation_popup_close_button(self):
        return self.driver.click("pending_printers_delete_confirmation_popup_close_button", timeout=30)

    def click_delete_confirmation_popup_delete_button(self):
        return self.driver.click("pending_printers_delete_confirmation_popup_delete_button", timeout=30)
    
    def get_pending_printers_no_of_items_selected_label_count(self):
        sleep(5)
        label_text = self.driver.get_text("pending_printers_no_of_items_selected_label")
        count = int(label_text.split()[0])
        return count

    def click_pending_printers_select_all_button(self):
        return self.driver.click("pending_printers_select_all_button", timeout=20)
    
    def get_total_printers_items_count(self):
        try:
            # Attempt to find all checkboxes in the table
            items = self.driver.find_object("pending_printers_table_checkbox", multiple=True)
            return len(items)
        except NoSuchElementException:
            # If checkboxes are not found, verify the "no items found" message
            if self.driver.wait_for_object("pending_printers_table_no_items_found_msg", raise_e=False):
                logging.info("No items found in the Pending Printers table.")
                return 0
    
    def click_pending_printers_unselect_all_button(self):
        return self.driver.click("pending_printers_unselect_all_button")
    
    def click_pending_printers_refresh_button(self):
        return self.driver.click("pending_printers_refresh_button",timeout=30)
    
    def click_pending_printers_gear_button(self):
        return self.driver.click("pending_printers_gear_button")

################################################### Column Options Popup ##################################################

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
        if option == "Product number":
            options[1].click()
        elif option == "Status":
            options[2].click()
        elif option == "Date Added":
            options[3].click()

    def verify_printers_table_column(self,column_name,displayed=True):
        if column_name == "Product number":
                return self.driver.wait_for_object("pending_printers_product_number_table_header", invisible=not displayed, timeout=60)
        elif column_name == "Status":
                return self.driver.wait_for_object("pending_printers_status_table_header", invisible=not displayed, timeout=60)

    #############################################Filter Sidebar Popup################################################

    def click_pending_printers_filter_button(self):
        return self.driver.click("pending_printers_filter_button",timeout=30)
    
    def click_pending_printers_filter_side_bar_clear_all_button(self):
        return self.driver.click("pending_printers_filter_side_bar_clear_all_button",timeout=30)

    def verify_pending_printers_filter_side_bar_done_button(self):
        return self.driver.verify_object_string("pending_printers_filter_side_bar_done_button")
    
    def click_pending_printers_filter_side_bar_done_button(self):
        return self.driver.click("pending_printers_filter_side_bar_done_button",timeout=30)
    
    def verify_pending_printers_filter_side_bar_title(self,displayed=True):
        return self.driver.wait_for_object("pending_printers_filter_side_bar_title", invisible=not displayed, timeout=30)

    def verify_pending_printers_filter_side_bar_status_label(self):
        return self.driver.verify_object_string("pending_printers_filter_side_bar_status_label")

    def verify_pending_printers_filter_side_bar_clear_all_button_status(self, status):
        if status == "enabled":
            if not self.driver.wait_for_object("pending_printers_filter_side_bar_clear_all_button_disabled", raise_e=False):
                return True
            else:
                raise UnexpectedItemPresentException("Pending Printers filter side bar clear all button is disabled")
        elif status == "disabled":
            if self.driver.wait_for_object("pending_printers_filter_side_bar_clear_all_button_disabled", raise_e=False):
                return True
            else:
                raise UnexpectedItemPresentException("Pending Printers filter side bar clear all button is enabled")
        return False

    def verify_pending_printers_filter_side_bar_title(self,displayed=True):
        return self.driver.wait_for_object("pending_printers_filter_side_bar_title", invisible=not displayed, timeout=30)

    def select_pending_printers_filter(self, filter_name):
        if filter_name == "Action needed":
            self.driver.click("pending_printers_filter_side_bar_action_needed_checkbox")
        elif filter_name == "Error":
            self.driver.click("pending_printers_filter_side_bar_error_checkbox")
        elif filter_name == "Connected":
            self.driver.click("pending_printers_filter_side_bar_connected_checkbox")
    
    def verify_filter_in_pending_printers_table(self, filter_name):
        if filter_name == "Action needed" or filter_name == "Error" or filter_name == "Connected":
            header_index = self.get_header_index("pending_printers_status")

        if self.driver.wait_for_object("pending_printers_table_no_items_found_msg", raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("printers_table_data", format_specifier=[header_index], multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text + " does not contains the filter value: " + filter_name)
        return True
    
    def get_pending_printers_filter_count_in_filter_sidebar(self, filter_name):
        if filter_name == "Action needed":
            text = self.driver.get_text("pending_printers_filter_side_bar_action_needed_count")
        elif filter_name == "Error":
            text = self.driver.get_text("pending_printers_filter_side_bar_error_count")
        elif filter_name == "Connected":
            text = self.driver.get_text("pending_printers_filter_side_bar_connected_count")

        # Split the text to get the count
        count = int(text.strip('()'))
        return count

    def get_pending_printers_action_needed_card_printers_count(self):
        text = self.driver.get_text("pending_printers_action_needed_card_printers_count")
        # Split the text to get the count
        count = int(text.split()[0])
        return count
    
    def get_pending_printers_error_card_printers_count(self):
        text = self.driver.get_text("pending_printers_error_card_printers_count")
        # Split the text to get the count
        count = int(text.split()[0])
        return count

    def get_pending_printers_connected_card_printers_count(self):
        text = self.driver.get_text("pending_printers_connected_card_printers_count")
        # Split the text to get the count
        count = int(text.split()[0])
        return count
    
    def get_pending_printers_table_status_count(self, status):
        status_column = self.get_header_index("pending_printers_status")
        status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[status_column], multiple=True)
        status_count = 0
        for element in status_list:
            if status.lower() in element.text.lower():
                status_count += 1
        return status_count

    #################################################Add Printer Popup####################################################

    def click_pending_printers_add_printers_button(self):
        return self.driver.click("pending_printers_add_printers_button", timeout=30)
    
    def verify_add_printers_popup_title(self):
        return self.driver.verify_object_string("add_printers_popup_title", timeout=30)
    
    def verify_add_printers_popup_description(self):
        return self.driver.verify_object_string("add_printers_popup_description", timeout=30)
    
    def verify_add_printers_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_popup_close_button")
    
    def verify_add_printers_popup_cancel_button(self):
        return self.driver.wait_for_object("add_printers_popup_cancel_button")
    
    def verify_add_printers_popup_enter_manually_button(self):
        return self.driver.wait_for_object("add_printers_popup_enter_manually_button")

    def verify_add_printers_popup_enter_manually_button_name(self):
        return self.driver.verify_object_string("add_printers_popup_enter_manually_button_name")
    
    def verify_add_printers_popup_enter_manually_button_description(self):
        return self.driver.verify_object_string("add_printers_popup_enter_manually_button_description")
    
    def verify_add_printers_popup_enter_manually_button_icon(self):
        return self.driver.wait_for_object("add_printers_popup_enter_manually_button_icon")

    def click_add_printers_popup_close_button(self):
        return self.driver.click("add_printers_popup_close_button", timeout=30)

    def click_add_printers_popup_enter_manually_button(self):
        return self.driver.click("add_printers_popup_enter_manually_button", timeout=30)

    def verify_add_printers_enter_manually_popup_title(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_title",timeout=30)
    
    def verify_add_printers_enter_manually_popup_description(self):
        return self.driver.verify_object_string("add_printers_enter_manually_popup_description",timeout=30)
    
    def verify_add_printers_enter_manually_popup_back_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_back_button")
    
    def verify_add_printers_enter_manually_popup_close_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_close_button")
    
    def verify_add_printers_enter_manually_popup_cancel_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_cancel_button")
    
    def click_add_printers_enter_manually_popup_cancel_button(self):
        return self.driver.click("add_printers_enter_manually_popup_cancel_button", timeout=30)
    
    def verify_add_printers_enter_manually_popup_submit_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_submit_button")

    def verify_add_printers_printer1_field(self):
        return self.driver.wait_for_object("add_printers_printer1_field",timeout=30)
    
    def verify_add_printers_printer1_field_title(self):
        return self.driver.verify_object_string("add_printers_printer1_field_title")
    
    def verify_add_printers_printer1_field_delete_button(self, displayed=True):
        return self.driver.wait_for_object("add_printers_printer1_field_delete_button", invisible=not displayed, timeout=30)
    
    def verify_add_printers_printer1_field_serial_number_label(self):
        return self.driver.verify_object_string("add_printers_printer1_field_serial_number_label")
    
    def verify_add_printers_printer1_field_product_number_label(self):
        return self.driver.verify_object_string("add_printers_printer1_field_product_number_label")
    
    def verify_add_printers_printer1_field_serial_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer1_field_serial_number_textbox")
    
    def verify_add_printers_printer1_field_product_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer1_field_product_number_textbox")
    
    def verify_add_printers_printer1_field_serial_number_label_icon(self):
        return self.driver.wait_for_object("add_printers_printer1_field_serial_number_label_icon",timeout=20)
    
    def verify_add_printers_printer1_field_product_number_label_icon(self):
        return self.driver.wait_for_object("add_printers_printer1_field_product_number_label_icon")
    
    def verify_add_printers_enter_manually_popup_add_another_printer_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_add_another_printer_button")

    def verify_add_printers_printer1_field_serial_number_label_tooltip_message(self):
        # Verify the tooltip message for the serial number label
        ac = ActionChains(self.wdvr)
        obj = self.driver.find_object("add_printers_printer1_field_serial_number_label_icon")
        ac.move_to_element(obj).perform()
        tooltip_message = self.driver.wait_for_object("add_printers_printer1_field_serial_number_label_tooltip").text
        expected_message = "The serial number has 10 characters. You can find it on a sticker on your printer, or in the printer’s embedded web server (EWS)."
        assert tooltip_message == expected_message, f"Expected tooltip message: {expected_message}, but got: {tooltip_message}"

    def verify_add_printers_printer1_field_product_number_label_tooltip_message(self):
        # Verify the tooltip message for the product number label
        ac = ActionChains(self.wdvr)
        obj = self.driver.find_object("add_printers_printer1_field_product_number_label_icon")
        ac.move_to_element(obj).perform()
        # Wait for the tooltip to appear and get its text
        tooltip_message = self.driver.wait_for_object("add_printers_printer1_field_product_number_label_tooltip").text
        expected_message = "The product number typically has 6 to 8 characters. You can find it on a sticker on your printer, or in the printer’s embedded web server (EWS)."
        assert tooltip_message == expected_message, f"Expected tooltip message: {expected_message}, but got: {tooltip_message}"

    def click_add_printers_enter_manually_popup_back_button(self):
        return self.driver.click("add_printers_enter_manually_popup_back_button", timeout=30)
    
    def click_add_printers_enter_manually_popup_close_button(self):
        return self.driver.click("add_printers_enter_manually_popup_close_button", timeout=30)

    def enter_add_printers_printer1_field_serial_number(self, serial_number):
        return self.driver.send_keys("add_printers_printer1_field_serial_number_textbox", serial_number)

    def enter_add_printers_printer1_field_product_number(self, product_number):
        return self.driver.send_keys("add_printers_printer1_field_product_number_textbox", product_number)
    
    def get_add_printers_printer1_field_serial_number(self):
        serial_number = self.driver.get_attribute("add_printers_printer1_field_serial_number_textbox", "value")
        return serial_number

    def get_add_printers_printer1_field_product_number(self):
        product_number = self.driver.get_attribute("add_printers_printer1_field_product_number_textbox", "value")
        return product_number
    
    def click_add_printers_enter_manually_popup_submit_button(self):
        return self.driver.click("add_printers_enter_manually_popup_submit_button", timeout=30)
    
    def verify_add_printers_printer1_field_serial_number_field_warning_message(self):
        # Verify the tooltip message for the serial number field
        tooltip_message = self.driver.wait_for_object("add_printers_printer1_field_serial_number_textbox_warning_msg",timeout=20).text
        expected_message = "Enter a valid serial number."
        assert tooltip_message == expected_message, f"Expected tooltip message: {expected_message}, but got: {tooltip_message}"
    
    def verify_add_printers_printer1_field_product_number_field_warning_message(self):
        # Verify the tooltip message for the product number field
        tooltip_message = self.driver.wait_for_object("add_printers_printer1_field_product_number_textbox__warning_msg").text
        expected_message = "Enter a valid product number."
        assert tooltip_message == expected_message, f"Expected tooltip message: {expected_message}, but got: {tooltip_message}"

    def verify_add_printers_printer1_field_product_number_blacklisted_warning_message(self):
        # Verify the error message for the product number field when blacklisted
        self.driver.wait_for_object("add_printers_printer1_field_product_number_blacklisted_warning_message", timeout=30)
        error_message = self.driver.get_text("add_printers_printer1_field_product_number_blacklisted_warning_message")
        expected_message = "This product is not supported by the platform. Remove the printer from this list to continue"
        assert error_message == expected_message, f"Expected error message: {expected_message}, but got: {error_message}"

    def verify_add_printers_printer1_field_already_claimed_warning_message(self):
        # Verify the error message for the product number field when already claimed
        return self.driver.wait_for_object("add_printers_printer1_field_already_claimed_warning_message", timeout=30)
        # error_message = self.driver.get_text("add_printers_printer1_field_already_claimed_warning_message")
        # expected_message = "This printer already has a connection pending. To finish connecting, go to the Pending Printers tab."
        # assert error_message == expected_message, f"Expected error message: {expected_message}, but got: {error_message}"
    
    def click_add_printers_enter_manually_popup_add_another_printer_button(self):
        return self.driver.click("add_printers_enter_manually_popup_add_another_printer_button", timeout=30)

    def verify_discard_changes_popup(self):
        return self.driver.wait_for_object("discard_changes_popup", timeout=30)
    
    def verify_discard_changes_popup_title(self):
        return self.driver.verify_object_string("discard_changes_popup_title")
    
    def verify_discard_changes_popup_message(self):
        return self.driver.verify_object_string("discard_changes_popup_message")
    
    def verify_discard_changes_popup_go_back_button(self):
        return self.driver.wait_for_object("discard_changes_popup_go_back_button")
    
    def verify_discard_changes_popup_discard_button(self):
        return self.driver.wait_for_object("discard_changes_popup_discard_button")
    
    def click_discard_changes_popup_go_back_button(self):
        return self.driver.click("discard_changes_popup_go_back_button", timeout=30)

    def verify_add_printers_printer2_field(self,displayed=True):
        return self.driver.wait_for_object("add_printers_printer2_field", invisible=not displayed, timeout=30)
    
    def verify_add_printers_printer2_field_title(self):
        return self.driver.verify_object_string("add_printers_printer2_field_title")
    
    def verify_add_printers_printer2_field_delete_button(self,displayed=True):
        return self.driver.wait_for_object("add_printers_printer2_field_delete_button", invisible=not displayed, timeout=30)
    
    def verify_add_printers_printer2_field_serial_number_label(self):
        return self.driver.verify_object_string("add_printers_printer2_field_serial_number_label")
    
    def verify_add_printers_printer2_field_product_number_label(self):
        return self.driver.verify_object_string("add_printers_printer2_field_product_number_label")
    
    def verify_add_printers_printer2_field_serial_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer2_field_serial_number_textbox")
    
    def verify_add_printers_printer2_field_product_number_textbox(self):
        return self.driver.wait_for_object("add_printers_printer2_field_product_number_textbox")
    
    def verify_add_printers_enter_manually_popup_add_another_printer_button(self):
        return self.driver.wait_for_object("add_printers_enter_manually_popup_add_another_printer_button")

    def click_add_printers_printer2_field_delete_button(self):
        return self.driver.click("add_printers_printer2_field_delete_button", timeout=30)