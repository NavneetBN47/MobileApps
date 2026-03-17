from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from MobileApps.resources.const.web.const import WEX_URLS
import logging
from datetime import datetime, timedelta
from time import sleep

class ProxiesTableEmpty(Exception):
    pass

class ProxiesSearchException(Exception):
    pass

class FilterValueException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class PrintProxies(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "fleet_management_printproxies"
    view_instructions_newtab_url = "https://downloads.hpdaas.com/staging/fleet-proxy-software/user-guide/userGuide.pdf"

    ############################ Main Menu verifys ############################

    def verify_fleet_management_print_proxies_breadcrumb(self):
        return self.driver.verify_object_string("fleet_management_print_proxies_breadcrumb",timeout=30)

    def verify_print_proxies_download_button(self):
        return self.driver.wait_for_object("print_proxies_download_button")
 
    def verify_print_proxies_page_url(self, stack):
        stack_urls = {
            "pie": WEX_URLS.PIE,
            "stage": WEX_URLS.STAGE,
            "production": WEX_URLS.PRODUCTION,
            "test": WEX_URLS.TEST
        }
        expected_url = stack_urls[stack] + "/ui/view/devices/print-proxies"
        assert self.driver.wdvr.current_url == expected_url, f"Expected URL: {expected_url}, but got: {self.driver.wdvr.current_url}"
 
    def verify_proxies_table_headers(self):
        printers_table_headers = []
        headers = self.driver.find_object("proxies_table_headers", multiple = True)
        for header in headers:
            printers_table_headers.append(header.text)
        # headers = printers_table_headers[1:]
        return printers_table_headers
    
    def click_devices_proxies_button(self):
        return self.driver.click("fleet_management_devices_proxies_button")
    
    ########################## Print Proxies page UI ###############################

    def verify_print_proxies_search_textbox(self):
        return self.driver.wait_for_object("print_proxies_search_txtbox")
    
    def verify_print_proxies_filter_button(self):
        return self.driver.verify_object_string("print_proxies_filter_btn",timeout=20)
    
    def verify_print_proxies_add_button(self):
        return self.driver.verify_object_string("print_proxies_add_btn",timeout=30)
    
    def click_print_proxies_add_button(self):
        return self.driver.click("print_proxies_add_btn",timeout=30)

    def verify_print_proxies_column_option_gear_button(self):
        return self.driver.wait_for_object("print_proxies_column_option_gear_btn")

    def click_print_proxies_column_option_gear_button(self):
        return self.driver.click("print_proxies_column_option_gear_btn")

    def verify_print_proxies_proxies_table(self):
        return self.driver.wait_for_object("print_proxies_proxies_table")

    def verify_print_proxies_table_data_load(self):
        # It verifies print proxies table is loaded and has lists of proxies entry.
        if self.driver.wait_for_object("print_proxies_table_checkbox", timeout=30, raise_e=False):
            return True
        else:
            self.verify_print_proxies_table_is_empty_msg()
            raise ProxiesTableEmpty("Print Proxies table is empty")
        
    def verify_print_proxies_table_is_empty_msg(self):
        self.driver.verify_object_string("print_proxies_table_no_item_found_msg")
        return self.driver.verify_object_string("print_proxies_table_add_proxy_msg")

    def search_proxy(self, search_text, table_entry_locator="print_proxies_table_proxy_name", raise_e=True, timeout=10):
        """
        Search text in print proxies table.
        Should display list of proxies based on search string, if search string matches,
        else should display No items found message.
        """
        self.driver.wait_for_object("print_proxies_search_txtbox", timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("print_proxies_search_txtbox", search_text, press_enter=True)

        if self.driver.wait_for_object("print_proxies_table_no_item_found_lbl", raise_e=False):
            table_empty = self.driver.wait_for_object("print_proxies_table_no_item_found_lbl")
            logging.info(table_empty.text)
            return False
        else:
            table_entry_proxies = self.driver.find_object(table_entry_locator, multiple=True)

            for entry in table_entry_proxies:
                if search_text.lower() in entry.text.lower():
                    logging.info(f"{search_text} is present in proxies list: {entry.text}")
                    break
                else:
                    raise ProxiesSearchException(f"{search_text} is not present in proxies list: {entry.text}")
        return True

    def search_proxy_with_connectivity_type(self, connectivity_type, raise_e=True, timeout=10):
        return self.search_proxy(connectivity_type, "print_proxies_table_connectivity_name", raise_e, timeout)

    def search_proxy_with_number_of_devices(self, number_of_devices, raise_e=True, timeout=10):
        return self.search_proxy(str(number_of_devices), "print_proxies_table_number_of_devices", raise_e, timeout)

    def search_proxy_with_description(self, description, raise_e=True, timeout=10):
        return self.search_proxy(description, "print_proxies_table_description", raise_e, timeout)

    def search_proxy_with_host_name(self, host_name, raise_e=True, timeout=10):
        return self.search_proxy(host_name, "print_proxies_table_host_name", raise_e, timeout)

    def click_search_clear_button(self):
        return self.driver.click("print_proxies_clear_search_button")

    def get_search_string(self,stack):
        if stack == "pie":
            return "hp-"
        elif stack == "stage":
            return "boi"
        elif stack == "production":
            return "hp-"
        elif stack == "test":
            return "patrick"
        else:
            return "default"

    def get_column_data(self, column_name, to_lower=False):
        header_index = self.get_header_index(column_name)
        table_entry_data = self.driver.find_object("print_proxies_table_data", format_specifier=[header_index], multiple=True)
        if to_lower:
            return [entry.text.lower() for entry in table_entry_data]
        else:
            return [entry.text for entry in table_entry_data]

    def get_all_proxy_names(self):
        return self.get_column_data("proxy_name", to_lower=True)

    def get_all_proxy_devices_count(self):
        return self.get_column_data("proxy_devices_count")

    def get_all_connectivity_status(self):
        return self.get_column_data("connectivity_status")

    def get_all_last_updated_date_and_time(self):
        return self.get_column_data("last_updated")

    def get_all_host_names(self):
        return self.get_column_data("host_name", to_lower=True)

    def get_all_proxy_descriptions(self):
        return self.get_column_data("proxy_description", to_lower=True)
    
    def get_all_proxies_date_added(self):
        return self.get_column_data("proxy_date_added", to_lower=True)
    
    def parse_date(self, date_str):
        now = datetime.now()
        def get_number(word):
            # Handle 'a', 'an', or digit
            return 1 if word in ("a", "an") else int(word)
        if "Just Now" in date_str:
            return now.replace(microsecond=0)
        elif "minute" in date_str:
            minutes = get_number(date_str.split()[0])
            return (now - timedelta(minutes=minutes)).replace(microsecond=0)
        elif "hour" in date_str:
            hours = get_number(date_str.split()[0])
            return (now - timedelta(hours=hours)).replace(microsecond=0)
        elif "yesterday" in date_str:
            return (now - timedelta(days=1)).replace(microsecond=0)
        elif "day" in date_str and "Yesterday" not in date_str:
            days = get_number(date_str.split()[0])
            return (now - timedelta(days=days)).replace(microsecond=0)
        elif "week" in date_str:
            weeks = get_number(date_str.split()[0])
            return (now - timedelta(weeks=weeks)).replace(microsecond=0)
        elif "month" in date_str:
            months = get_number(date_str.split()[0])
            return (now - timedelta(days=months * 30)).replace(microsecond=0)
        elif "year" in date_str:
            years = get_number(date_str.split()[0])
            return (now - timedelta(days=years * 365)).replace(microsecond=0)
        else:
            return datetime.strptime(date_str, "%b %d, %Y, %I:%M %p").replace(microsecond=0)

    def verify_proxies_date_added_is_sorted(self, date_list, order="ascending"):
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
    
    def get_proxy_devices_count(self):
        return self.driver.get_text("print_proxies_table_number_of_devices")

    ##################### Filter Side Bar UI and functionality ######################

    def click_print_proxies_filter_button(self):
        return self.driver.click("print_proxies_filter_btn",timeout=30)

    def verify_filter_side_bar_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("filter_side_bar_title", invisible=not displayed, timeout=30)
        return self.driver.verify_object_string("filter_side_bar_title")

    def verify_filter_side_bar_description(self):
        return self.driver.verify_object_string("filter_side_bar_description")
    
    def verify_filter_side_bar_search_box(self):
        return self.driver.wait_for_object("filter_side_bar_search_box")

    def verify_filter_side_bar_connectivity_label(self):
        return self.driver.verify_object_string("filter_side_bar_connectivity_label")

    def click_filter_side_bar_close_button(self):
        return self.driver.click("filter_side_bar_close_btn")

    def select_filter(self,filter_name):
        filter_options = self.driver.find_object("built_in_filter_options", multiple = True)
        for i in range(len(filter_options)):
            if filter_options[i].text == filter_name:
                filter_options[i].click()

    def verify_filter_in_proxies_table(self,filter_name):
        if filter_name == "Online" or filter_name == "Offline":
            header_index = self.get_header_index("connectivity_status")

        if self.driver.wait_for_object("print_proxies_table_no_item_found_lbl",raise_e=False):
            return False
        else:
            table_entry_data = self.driver.find_object("print_proxies_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True
    
    def verify_filter_side_bar_connectivity_status_tags(self,filter_name):
            return self.driver.wait_for_object("filter_side_bar_connectivity_status_tags", format_specifier=[filter_name], timeout=10)
 
    def verify_filter_side_bar_connectivity_online_tag_is_not_displayed(self):
        return self.driver.wait_for_object("filter_side_bar_connectivity_online_tag", invisible=True)
 
    def verify_filter_side_bar_connectivity_offline_tag_is_not_displayed(self):
        return self.driver.wait_for_object("filter_side_bar_connectivity_offline_tag", invisible=True)
           
    def click_filter_side_bar_connectivity_status_tag_close_tag(self):
        return self.driver.click("filter_side_bar_connectivity_status_tag_close_tag")
 
    def verify_filter_side_bar_connectivity_status_clear_all_tag(self):
        return self.driver.verify_object_string("filter_side_bar_connectivity_status_clear_all_tag")
   
    def click_filter_side_bar_connectivity_status_clear_all_tag(self):
        return self.driver.click("filter_side_bar_connectivity_status_clear_all_tag")

    def verify_print_proxies_filter_items_selected_text_displayed(self, displayed=True):
        return self.driver.wait_for_object("filter_side_bar_items_selected_text", invisible=not displayed)

    def get_print_proxies_filter_items_selected_text(self):
        return self.driver.wait_for_object("filter_side_bar_items_selected_text").text
    
    def verify_print_proxies_filter_clear_all_button(self):
        return self.driver.wait_for_object("filter_side_bar_items_clear_all_btn")

    def click_print_proxies_filter_clear_all_button(self):
        return self.driver.click("filter_side_bar_items_clear_all_btn")
    
    ####################### Print Proxies Contextual Footer ############################

    def click_print_proxies_checkbox(self):
        return self.driver.click("print_proxies_table_checkbox")

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("print_proxies_contextual_footer")

    def verify_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("print_proxies_contextual_footer",invisible=True)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("print_proxies_contextual_footer_cancel_button")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.verify_object_string("print_proxies_contextual_footer_selected_item_lbl")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("print_proxies_contextual_footer_select_action_dropdown")

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("print_proxies_contextual_footer_continue_button")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("print_proxies_contextual_footer_cancel_button")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("print_proxies_contextual_footer_continue_button")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("print_proxies_contextual_footer_select_action_dropdown")

    def select_contextual_footer_select_action_dropdown_option(self,option):
        options = self.driver.find_object("print_proxies_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == "Edit":
            options[0].click()
        elif option == "Remove":
            options[1].click()

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("print_proxies_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    ################################## Column Options Popup ##################################################

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
        if option == "Connectivity":
            options[1].click()
        elif option == "Last Updated":
            options[2].click()
        elif option == "Date Added":
            options[3].click()
        elif option == "Devices":
            options[4].click()
        elif option == "Host name":
            options[5].click()
        elif option == "Description":
            options[6].click()
        elif option == "Fleet Proxy Version":
            options[7].click()

    def verify_print_proxies_table_column(self,column_name,displayed=True):
        if column_name == "Connectivity":
                return self.driver.wait_for_object("print_proxies_table_connectivity_column", invisible=not displayed)
        elif column_name == "Last Updated":
                return self.driver.wait_for_object("print_proxies_table_last_updated_column", invisible=not displayed)
        elif column_name == "Date Added":
                return self.driver.wait_for_object("print_proxies_table_date_added_column", invisible=not displayed)
        
    ################################# verify proxy Popup ######################################################
    
    def verify_verify_proxy_popup_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("verify_proxy_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("verify_proxy_popup_title")
    
    def verify_verify_proxy_popup_description(self):
        return self.driver.verify_object_string("verify_proxy_popup_description")
    
    def verify_verify_proxy_popup_code_label(self):
        return self.driver.verify_object_string("verify_proxy_popup_code_label")
    
    def verify_verify_proxy_popup_code_text_box(self):
        return self.driver.wait_for_object("verify_proxy_popup_code_txt")
    
    def verify_verify_proxy_popup_note(self):
        return self.driver.verify_object_string("verify_proxy_popup_proxy_note")

    def verify_verify_proxy_popup_cancel_button(self):
        return self.driver.verify_object_string("verify_proxy_popup_cancel_btn")

    def verify_verify_proxy_popup_verify_button(self):
        return self.driver.verify_object_string("verify_proxy_popup_verify_btn")
    
    def click_verify_proxy_popup_cancel_button(self):
        return self.driver.click("verify_proxy_popup_cancel_btn")

    def click_verify_proxy_popup_verify_button(self):
        return self.driver.click("verify_proxy_popup_verify_btn")
    
    def enter_code(self, code):
        return self.driver.send_keys("verify_proxy_popup_code_txt", code)
    
    def get_verify_proxy_popup_code_text_box_tooltip_msg(self):
        return self.driver.wait_for_object("verify_proxy_popup_code_required_tooltip_msg").text
    
    def verify_verify_proxy_invalid_code_error_msg(self):
        return self.driver.verify_object_string("verify_proxy_invalid_code_error_msg")

    ################################# proxy verified Popup ######################################################

    def verify_proxy_verified_popup_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("proxy_verified_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("proxy_verified_popup_title",timeout=30)
    
    def verify_proxy_verified_popup_description(self):
        return self.driver.verify_object_string("proxy_verified_popup_description")
    
    def verify_proxy_verified_popup_cancel_button(self):
        return self.driver.verify_object_string("proxy_verified_popup_cancel_btn")

    def verify_proxy_verified_popup_allow_button(self):
        return self.driver.verify_object_string("proxy_verified_popup_allow_btn")
    
    def click_proxy_verified_popup_cancel_button(self):
        return self.driver.click("proxy_verified_popup_cancel_btn")

    def click_proxy_verified_popup_allow_button(self):
        return self.driver.click("proxy_verified_popup_allow_btn")

    ################################# proxy connected Popup ######################################################

    def verify_proxy_connected_popup_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("proxy_connected_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("proxy_connected_popup_title",timeout=15)
    
    def verify_proxy_connected_popup_success_icon(self):
        return self.driver.wait_for_object("proxy_connected_popup_success_icon")
    
    def verify_proxy_connected_popup_description(self):
        return self.driver.verify_object_string("proxy_connected_popup_description")
    
    def verify_proxy_connected_popup_proxy_name_label(self):
        return self.driver.verify_object_string("proxy_connected_popup_proxy_name_label")

    def verify_proxy_connected_popup_done_button(self):
        return self.driver.verify_object_string("proxy_connected_popup_done_btn")

    def click_proxy_connected_popup_done_button(self):
        return self.driver.click("proxy_connected_popup_done_btn")
    
    def enter_proxy_name(self, proxy_name):
        sleep(3)
        self.driver.js_clear_text("proxy_connected_popup_proxy_name_txt")
        return self.driver.send_keys("proxy_connected_popup_proxy_name_txt", proxy_name)
    
    def enter_proxy_description(self, proxy_description):
        return self.driver.send_keys("proxy_connected_popup_proxy_desc_txt", proxy_description)

    def get_proxy_connected_popup_proxy_name_text_box_tooltip_msg(self):
        return self.driver.wait_for_object("proxy_connected_popup_proxy_name_tooltip_msg").text
    
    def verify_add_proxy_toast_message(self, proxy_name):
        return self.check_toast_successful_message(f"{proxy_name} successfully added.")

    def removing_the_existing_proxy(self):
        self.click_print_proxies_checkbox()
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_select_action_dropdown_option("Remove")
        self.click_contextual_footer_continue_button()
        self.click_remove_proxy_popup_remove_button()
        self.click_search_clear_button()
        self.verify_print_proxies_table_data_load()
        assert False == self.search_proxy("Automation-prod")

    ################################## Reconnect this Proxy Popup ########################################

    def verify_reconnect_this_proxy_popup_title(self, displayed=True):
        return self.driver.wait_for_object("reconnect_proxy_popup_title", invisible=not displayed)

    def verify_reconnect_this_proxy_popup_description_1(self):
        full_description = self.driver.get_text("reconnect_proxy_popup_description_text_1")
        "This Proxy" == full_description.split("\n")[0]
    
    def verify_reconnect_proxy_popup_description_hostname(self):
        return self.driver.wait_for_object("reconnect_proxy_popup_description_hostname")

    def verify_reconnect_proxy_popup_description_text_2(self):
        return self.driver.verify_object_string("reconnect_proxy_popup_description_text_2")

    def verify_reconnect_proxy_popup_proxy_name_label(self):
        proxy_name = self.driver.get_text("reconnect_proxy_popup_proxy_name_label")
        "Proxy Name:" == proxy_name.split(':')[0] + ":"
    
    def get_recconect_proxy_popup_proxy_name(self):
        return self.driver.get_text("reconnect_proxy_popup_proxy_name_txt")

    def verify_reconnect_proxy_popup_proxy_description_label(self):
        description = self.driver.get_text("reconnect_proxy_popup_proxy_description_label")
        "Description:" == description.split(":")[0] + ":"

    def get_recconect_proxy_popup_proxy_description(self):
        return self.driver.get_text("reconnect_proxy_popup_proxy_description_txt")
    
    def verify_reconnect_proxy_popup_note_message(self):
        return self.driver.verify_object_string("reconnect_proxy_popup_reconnect_note_message")

    def verify_reconnect_this_proxy_popup_cancel_button(self):
        return self.driver.verify_object_string("reconnect_proxy_popup_cancel_button")

    def verify_reconnect_this_proxy_popup_reconnect_button(self):
        return self.driver.verify_object_string("reconnect_proxy_popup_reconnect_button")

    def click_reconnect_this_proxy_popup_cancel_button(self):
        return self.driver.click("reconnect_proxy_popup_cancel_button")

    def click_reconnect_this_proxy_popup_reconnect_button(self):
        return self.driver.click("reconnect_proxy_popup_reconnect_button")

    ################################## Edit Proxy Popup ##################################################

    def verify_edit_proxy_popup_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("edit_proxy_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("edit_proxy_popup_title")

    def verify_edit_proxy_popup_description(self):
        return self.driver.verify_object_string("edit_proxy_popup_desc")

    def get_edit_proxy_popup_proxy_name(self):
        return self.driver.get_attribute("edit_proxy_popup_proxy_name_txt","value")

    def get_edit_proxy_popup_proxy_description(self):
        return self.driver.get_attribute("edit_proxy_popup_desc_txt","value")
    
    def verify_edit_proxy_popup_proxy_name_textbox(self):
        return self.driver.wait_for_object("edit_proxy_popup_proxy_name_txt")

    def verify_edit_proxy_popup_proxy_description(self):
        return self.driver.wait_for_object("edit_proxy_popup_desc_txt")

    def update_proxy_name(self,proxy_name):
        self.clear_edit_proxy_popup_proxy_name()
        sleep(3)  # Wait for the clear action to complete
        return self.driver.send_keys("edit_proxy_popup_proxy_name_txt", proxy_name)

    def update_proxy_description(self,proxy_name):
        return self.driver.send_keys("edit_proxy_popup_desc_txt", proxy_name)

    def verify_edit_proxy_popup_cancel_button(self):
        return self.driver.verify_object_string("edit_proxy_popup_cancel_btn")

    def verify_edit_proxy_popup_save_button(self):
        return self.driver.verify_object_string("edit_proxy_popup_save_btn") 
    
    def verify_edit_proxy_popup_save_button_status(self, status):
        save_button = self.driver.wait_for_object("edit_proxy_popup_save_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException("Save button is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException("Save button is disabled")
            return True

    def click_edit_proxy_popup_cancel_button(self):
        return self.driver.click("edit_proxy_popup_cancel_btn") 

    def verify_edit_proxy_popup_proxy_save_button_status(self,status):
        save_button  =self.driver.wait_for_object("edit_proxy_popup_save_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException("Save button is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException("Save button is disabled")
            return True

    def click_edit_proxy_popup_save_button(self):
        return self.driver.click("edit_proxy_popup_save_btn")
    
    def get_edit_proxy_popup_proxy_name_text_box_tooltip_msg(self):
        return self.driver.get_text("edit_proxy_popup_proxy_name_tooltip_msg")
    
    def clear_edit_proxy_popup_proxy_name(self):
        return self.driver.js_clear_text("edit_proxy_popup_proxy_name_txt")
    
    def click_edit_proxy_popup_proxy_name_text_box(self):
        return self.driver.click("edit_proxy_popup_proxy_name_txt")
    
    def verify_edit_proxy_toast_message(self,proxy_name):
        text = "{} successfully saved."
        expected_alert_message = text.format(proxy_name)
        return self.check_toast_successful_message(expected_alert_message)
    
    ################################## Remove Proxy ##################################################

    def verify_remove_proxy_popup_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("remove_proxy_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("remove_proxy_popup_title")

    def verify_remove_proxy_popup_description(self):
        self.driver.verify_object_string("remove_proxy_popup_desc")
        return self.driver.verify_object_string("remove_proxy_popup_desc_end_part")

    def verify_remove_proxy_popup_cancel_button(self):
        return self.driver.verify_object_string("remove_proxy_popup_cancel_btn")

    def verify_remove_proxy_popup_remove_button(self):
        return self.driver.verify_object_string("remove_proxy_popup_remove_btn")

    def click_remove_proxy_popup_cancel_button(self):
        return self.driver.click("remove_proxy_popup_cancel_btn")

    def click_remove_proxy_popup_remove_button(self):
        return self.driver.click("remove_proxy_popup_remove_btn")
    
    def verify_remove_proxy_toast_message(self,proxy_name):
        text = "{} removed."
        expected_alert_message = text.format(proxy_name)
        return self.check_toast_successful_message(expected_alert_message)
    
  #################################### Add Device Pop-Up ####################################################
   
    def click_print_proxies_download_button(self):
        return self.driver.click("print_proxies_download_button", timeout=20)
   
    def verify_add_printers_popup_title(self):
        return self.driver.verify_object_string("add_printers_popup_title",timeout=30)
 
    def verify_add_printers_popup_sub_title(self):
        return self.driver.verify_object_string("add_printers_popup_sub_title")
   
    def verify_add_printers_popup_description(self):
        return self.driver.verify_object_string("add_printers_popup_desc", timeout=30)
   
    def verify_add_printers_popup_view_system_requirements_link(self):
        return self.driver.verify_object_string("add_printers_popup_view_system_requirements_link")
    
    def verify_add_printers_popup_view_instructions_link(self):
        return self.driver.verify_object_string("add_printers_popup_view_instructions_link")
   
    def verify_add_printers_popup_done_button(self):
        return self.driver.verify_object_string("add_printers_popup_done_btn")
   
    def verify_add_printers_popup_list_android_application_option(self):
        return self.driver.verify_object_string("add_printers_popup_android_application_option")
   
    def verify_add_printers_popup_list_macOS_application_option(self):
        return self.driver.verify_object_string("add_printers_popup_macOS_application_option")
   
    def verify_add_printers_popup_list_linux_analytics_application_option(self):
        return self.driver.verify_object_string("add_printers_popup_linux_analytics_application_option")
   
    def verify_add_printers_popup_list_linux_core_application_option(self):
        return self.driver.verify_object_string("add_printers_popup_linux_core_application_option")
   
    def verify_add_printers_popup_list_windows_application_option(self):
        return self.driver.verify_object_string("add_printers_popup_windows_application_option")
   
    def verify_add_printers_popup_list_network_readiness_tool_option(self):
        return self.driver.verify_object_string("add_printers_popup_network_readiness_tool_option")
   
    def verify_add_printers_popup_list_hp_protect_and_trace_with_wolf_connect_option(self):
        return self.driver.verify_object_string("add_printers_popup_hp_protect_and_trace_with_wolf_connect_option")
   
    def verify_add_printers_popup_list_print_fleet_proxy_option(self):
        return self.driver.verify_object_string("add_printers_popup_print_fleet_proxy_option")
   
    def verify_add_printers_popup_list_incident_integration_option(self):
        return self.driver.verify_object_string("add_printers_popup_incident_integration_option")
   
    def click_add_printers_popup_done_button(self):
        return self.driver.click("add_printers_popup_done_btn")
   
    def click_add_printers_popup_view_system_requirements_link(self):
        return self.driver.click("add_printers_popup_view_system_requirements_link",timeout=30)

    def click_add_printers_popup_view_instructions_link(self):
        return self.driver.click("add_printers_popup_view_instructions_link", timeout=30)
   
    def verify_view_system_requirements_page_title(self):
        return self.driver.verify_object_string("view_system_requirements_page_title",timeout=30)
   
    def verify_view_system_requirements_page_description(self):
        return self.driver.verify_object_string("view_system_requirements_page_desc")
   
    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()
 
    def verify_add_printers_popup_hp_print_fleet_proxy_download_button(self):
        return self.driver.wait_for_object("add_printers_popup_hp_print_fleet_proxy_download_button", timeout=30)
    
    def verify_add_printers_popup_hp_print_fleet_proxy_download_button_title(self):
        return self.driver.verify_object_string("add_printers_popup_hp_print_fleet_proxy_download_button_title")
    
    def verify_add_printers_popup_hp_print_fleet_proxy_download_button_version(self):
        return self.driver.wait_for_object("add_printers_popup_hp_print_fleet_proxy_download_button_version")
    
    def verify_add_printers_popup_hp_print_fleet_proxy_download_button_icon(self):
        return self.driver.wait_for_object("add_printers_popup_hp_print_fleet_proxy_download_button_icon")

    def verify_view_instructions_newtab_url(self):
        return self.driver.wdvr.current_url == self.view_instructions_newtab_url