import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class DeviceSearchException(Exception):
    pass

class WrongToastException(Exception):
    pass

class NoPrinterException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class DevicesGroupNotFoundException(Exception):
    pass

class PrintersGroupNotFoundException(Exception):
    pass

class Devices(ECPFlow):
    flow_name = "devices"

    def verify_device_page(self, table_load=True):
        #self.verify_all_devices_tab()
        #This object make sure the table is loaded
        #Doesn't work if no entries are found
        if table_load:
            return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        else:
            return self.driver.wait_for_object("_shared_page_header_title", timeout=30)
        
    def verify_device_page_content(self, timeout=20):
        self.driver.wait_for_object("device_page_content", timeout=timeout)
    
    def verify_and_click_online_printer(self):
        status = "online"
        connectivity_column = self.get_header_index("device_connectivity")
        checkbox_column = self.get_header_index("checkbox_column")
        connectivity_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[connectivity_column],multiple=True)
        checkbox_column_list = self.driver.find_object("_shared_table_checkbox_col_by_index", format_specifier=[checkbox_column],multiple=True)
        for index in range(len(connectivity_list)):
            if status == connectivity_list[index].text.lower():
                return checkbox_column_list[index].click()
            else:
                continue
        raise DeviceSearchException("Cannot find any connected printer")

    def verify_device_status_by_serial_number(self, device_name, serial_number, status="Online"):
        self.search_device(device_name)
        
        if not self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False, raise_e=False):
            raise DeviceSearchException(f"Cannot find device '{device_name}' with serial number: {serial_number}")

        serial_column = self.get_header_index("device_serial")
        status_column = self.get_header_index("device_status")
        serial_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[serial_column],multiple=True)
        status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[status_column],multiple=True)

        for index in range(len(serial_list)):
            if serial_number.lower() != serial_list[index].text.lower():
                continue
            if status.lower() == status_list[index].text.lower():
                return True
            else:
                return False
        
        raise DeviceSearchException(f"Cannot find device '{device_name}' with serial number: {serial_number}")

    def click_groups_side_bar_expand_btn(self):
        return self.driver.click("group_side_bar_expand_btn")
    
    def click_group_side_bar_collapse_btn(self):
        return self.driver.click("group_side_bar_collapse_btn")

    def verify_groups_side_bar_collapse_button_is_displayed(self):
        return self.driver.wait_for_object("group_side_bar_collapse_btn",raise_e=False)

    def verify_all_devices_tab(self):
        return self.driver.wait_for_object("all_devices_tab")

    def verify_search_device_name_txt(self):
        return self.driver.wait_for_object("search_device_name_txt")

    def verify_export_popup(self):
        return self.driver.wait_for_object("export_popup_div")

    def search_device(self, dev_name):
        #Currently only pressing enter triggers the search it's probably a bug
        #As there is also a search button that doesn't work
        self.driver.wait_for_object("search_device_name_txt")
        self.verify_device_page()
        sleep(3)
        for _ in range(3):
            try:
                return self.driver.send_keys("search_device_name_txt", dev_name, press_enter=True)
            except (StaleElementReferenceException,ElementNotInteractableException):
                logging.debug("Search devices Send_keys is not working")
                sleep(3)
        raise DeviceSearchException("After 3 tries still Search devices Send_keys is not working")

    def export_devices(self, file_type="CVS"):
        #Ignoring file type for now since it only supports CVS
        self.click_device_export_btn()
        self.verify_export_popup()
        self.click_device_export_popup_submit_btn()
        self.check_toast_successful_messages()

    def click_device_export_btn(self):
        return self.driver.click("export_all_btn")

    def click_device_export_popup_submit_btn(self):
        return self.driver.click("export_popup_submit")

    def check_toast_successful_messages(self):
        message = self.driver.wait_for_object("bottom_toast_msg").text
        expected_message = "File has been downloaded successfully!"
        if message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + message + " expected message is: " + expected_message)

    def click_devcies_tab_breadcrumb(self):
        self.driver.click("devcies_tab_breadcrumb")

    def get_devices_detail_info(self):
        device_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        device_info["serial_number"] = all_fields[1].text.lower()
        device_info["device_name"] = all_fields[14].text.lower()
        device_info["device_status"] = all_fields[12].text.lower()
        device_info["connectivity"] = all_fields[4].text.lower()
        return device_info

    def verify_devices_details(self):
        details_info = {}
        details_info["serial_number"] = self.driver.wait_for_object("devices_details_serial_number").text.lower()
        details_info["device_name"] = self.driver.wait_for_object("devices_details_name",timeout=20).text.lower().split('\n')[0].strip()
        details_info["device_status"] = self.driver.wait_for_object("devices_details_status").text.lower()
        details_info["connectivity"] = self.driver.wait_for_object("devices_details_connectivity_status").text.lower()
        return details_info

    def get_security_risk_detail(self):
        return self.driver.wait_for_object("devices_details_security",timeout=20).text.lower()

    def click_device_details_view_link(self):
        return self.driver.click("device_details_view_link",timeout=30)
    
    def verify_navigated_tab(self,tab_name):
        navigated_tab = self.driver.wait_for_object(tab_name,timeout=20).get_attribute("aria-selected")
        assert navigated_tab == 'true'
    
    def verify_devices_detail_loaded(self):
        return self.driver.wait_for_object("endpoint_security_devices_detail_name", timeout=30)
        
    def verify_devices_details_list_synced_with_device_screen(self):
        details_info = {}
        self.verify_devices_detail_loaded()
        details_info["device_name"] = self.driver.wait_for_object("endpoint_security_devices_detail_name").text.lower()
        # details_info["assessment_status"] = self.driver.wait_for_object("solution_devices_details_security").text.lower()
        self.driver.click("solution_hp_secure_fleet_manager_breadcrumd")
        sleep(5) # To wait for the page to load
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        details_info["device_status"] = all_fields[2].text.lower()
        self.click_first_entry_link()
        details_info["connectivity"] = self.driver.wait_for_object("solution_devices_details_status").text.lower()
        details_info["serial_number"] = self.driver.wait_for_object("solution_devices_details_serial_number",timeout=10).text.lower()
        return details_info
     
    def verify_device_page_title(self):
        return self.driver.verify_object_string("devices_title")
 
    def verify_device_page_desc(self):
        return self.driver.verify_object_string("devices_desc")
 
    def verify_all_devices_tab(self):
        return self.driver.wait_for_object("all_devices_tab")

    def verify_refresh_btn(self):
        return self.driver.wait_for_object("_shared_sync_button")

    def verify_search_device_name_txtbox(self):
        return self.driver.wait_for_object("search_device_name_txt")

    def verify_device_export_btn(self):
        return self.driver.wait_for_object("export_all_btn")
    
    def search_online_device(self, dev_name):
        self.search_device(dev_name)
        if self.driver.find_object('_shared_no_items_found_img', raise_e=False) is not False:
            raise DeviceSearchException("Devices table has no Online device. Turn the device Online to assign policy")
        else:
            return True

    ################################### Device Count ####################################################
    
    def get_devices(self):
        # This method returns the online, offline and total devices count 
        online_devices = 0
        offline_devices = 0
        self.driver.wait_for_object("_shared_table_entries",timeout=30)
        self.select_page_size_new("100")
        max_pages=self.get_max_page()
        for page in range(max_pages):
            self.select_page(page+1)
            rows = self.driver.find_object("_shared_table_entries",multiple=True)
            for row in rows:
                s = row.text
                if 'Online' in s:
                    online_devices+=1
                if 'Offline' in s:
                    offline_devices+=1
        devices_page_device_count = {"online" : online_devices, "offline" : offline_devices, "total_count" : online_devices+offline_devices}
        return devices_page_device_count

    ################################### Contextual Footer ####################################################

    def click_devices_checkbox(self):
        return self.driver.click("devices_table_checkbox",timeout=10)

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("devices_contextual_footer_cancel_btn")

    def verify_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("devices_contextual_footer_cancel_btn",invisible=True)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("devices_contextual_footer_cancel_btn")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.verify_object_string("devices_contextual_footer_selected_item_label")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("devices_contextual_footer_select_action_dropdown")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("devices_contextual_footer_select_action_dropdown")

    def select_contextual_footer_select_action_dropdown_option(self,option):
        options = self.driver.find_object("devices_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == "Move to group":
            options[0].click()
        elif option == "Remove from group":
            options[1].click()
        elif option == "Configure Device":
            options[2].click()

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("devices_contextual_footer_continue_btn")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("devices_contextual_footer_cancel_btn")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("devices_contextual_footer_continue_btn")

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("devices_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def verify_remove_from_group_option_status(self,status):
        if status == "enabled":
            if self.driver.get_attribute("select_action_dropdown_remove_from_group_option","aria-disabled") == "true":
                raise UnexpectedItemPresentException("Remove From Group option is disabled")
            return True
        else:
            if self.driver.get_attribute("select_action_dropdown_remove_from_group_option","aria-disabled") == "false":
                raise UnexpectedItemPresentException("Remove From Group option is enabled")
            return True

    ################################### Groups ####################################################

    def get_device_count(self,group_name):
        return int(self.driver.wait_for_object("devices_groups_group_count",format_specifier=[group_name],timeout=10).text)

    def click_devices_group(self,group_name):
        for _ in range(3):
            try:
                return self.driver.click("devices_groups_group_name",format_specifier=[group_name],timeout=10)
            except (NoSuchElementException,ElementClickInterceptedException):
                logging.debug("Devices groups hasn't loaded yet")
                sleep(3)
        raise DevicesGroupNotFoundException("After 3 tries still Devices groups hasn't loaded yet")
    
    def click_devices_group_all_option(self,group_name):
        for _ in range(3):
            try:
                return self.driver.click("devices_side_group_all_option",format_specifier=[group_name],timeout=10)
            except (NoSuchElementException,ElementClickInterceptedException):
                logging.debug("Devices groups hasn't loaded yet")
                sleep(3)
        raise DevicesGroupNotFoundException("After 3 tries still All Devices groups hasn't loaded yet")

    def get_device_serial_number(self):
        # It only takes first device serial number from device table
        device_details=self.get_devices_detail_info()
        return device_details["serial_number"]

    ################################### Move to Group Pop Up ####################################################

    def verify_move_to_group_popup_title(self):
        return self.driver.verify_object_string("devices_move_to_group_popup_title")

    def verify_move_to_group_popup_description(self):
        return self.driver.verify_object_string("devices_move_to_group_popup_desc")

    def verify_move_to_group_popup_groups_to_move_field(self):
        return self.driver.wait_for_object("devices_move_to_group_popup_groups_to_move")
    
    def verify_move_to_group_popup_cancel_button(self):
        return self.driver.verify_object_string("devices_move_to_group_popup_cancel_btn")

    def verify_move_to_group_popup_move_button(self):
        return self.driver.verify_object_string("devices_move_to_group_popup_move_btn")

    def click_move_to_group_popup_cancel_button(self):
        return self.driver.click("devices_move_to_group_popup_cancel_btn")

    def click_move_to_group_popup_move_button(self):
        return self.driver.click("devices_move_to_group_popup_move_btn")

    ################################### Remove from group Pop Up ####################################################

    def verify_remove_from_group_popup_title(self):
        return self.driver.verify_object_string("devices_remove_from_group_popup_title")

    def verify_remove_from_group_popup_description(self):
        return self.driver.verify_object_string("devices_remove_from_group_popup_desc")
    
    def verify_remove_from_group_popup_cancel_button(self):
        return self.driver.verify_object_string("devices_remove_from_group_popup_cancel_btn")

    def verify_remove_from_group_popup_remove_button(self):
        return self.driver.verify_object_string("devices_remove_from_group_popup_remove_btn")

    def click_remove_from_group_popup_cancel_button(self):
        return self.driver.click("devices_remove_from_group_popup_cancel_btn")

    def click_remove_from_group_popup_remove_button(self):
        return self.driver.click("devices_remove_from_group_popup_remove_btn")

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
        return self.driver.verify_object_string("export_popup_submit")

    def verify_export_devices_popup_select_file_type_dropdown(self):
        return self.driver.wait_for_object("export_devices_popup_select_file_dropdown")

    def click_export_devices_popup_select_file_type_dropdown(self):
        return self.driver.click("export_devices_popup_select_file_dropdown")

    def click_export_devices_popup_cancel_button(self):
        return self.driver.click("export_devices_popup_cancel_btn")

    def get_select_file_type_dropdown_options(self):
        file_type = self.driver.get_attribute("export_devices_popup_select_file_dropdown","value")
        return file_type

    ################################### Create Group Pop-Up ####################################################

    def click_devices_create_group_button(self):
        return self.driver.click("devices_create_group_btn")

    def verify_create_group_popup_title(self):
        return self.driver.verify_object_string("create_group_popup_title")

    def verify_create_group_popup_description(self):
        return self.driver.verify_object_string("create_group_popup_desc")

    def verify_create_group_popup_group_name_field(self):
        return self.driver.wait_for_object("create_group_popup_group_name_txt")

    def enter_group_name(self,group_name):
        return self.driver.send_keys("create_group_popup_group_name_txt",group_name)

    def verify_create_group_popup_parent_group_field(self):
        return self.driver.wait_for_object("devices_move_to_group_popup_groups_to_move")

    def select_parent_group(self):
        return self.driver.click("devices_move_to_group_popup_groups_to_move")
    
    def verify_create_group_popup_cancel_button(self):
        return self.driver.verify_object_string("create_group_popup_cancel_btn")

    def click_create_group_popup_cancel_button(self):
        return self.driver.click("create_group_popup_cancel_btn")

    def verify_create_group_popup_create_button(self):
        return self.driver.verify_object_string("create_group_popup_create_btn")

    def click_create_group_popup_create_button(self):
        return self.driver.click("create_group_popup_create_btn")

    def verify_group_name(self,group_name,displayed=True):
        for _ in range(3):
                try:
                    return self.driver.wait_for_object("devices_groups_group_name",invisible=not displayed,format_specifier=[group_name],timeout=30)
                except (NoSuchElementException):
                    logging.debug("Devices groups hasn't loaded yet")
                    sleep(3)
        raise PrintersGroupNotFoundException("After 3 tries still Devices groups hasn't loaded yet")

    ################################## Column Options Popup ##################################################

    def click_devices_column_option_settings_gear_button(self):
        return self.driver.click("devices_column_option_settings_gear_btn")

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

    # def click_column_option(self,option):
    #     options = self.driver.find_object("column_option_popup_options", multiple = True)
    #     if option == "MODEL NAME":
    #         options[1].click()
    #     elif option == "CONNECTIVITY":
    #         options[3].click()

    def click_column_option(self, column_option_name):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_object("column_option_popup_options_label", format_specifier=[column_option_name]))
        return self.driver.js_click("column_option_popup_options_label", format_specifier=[column_option_name])

    def verify_devices_tabel_column(self,column_name,displayed=True):
        if column_name == "MODEL NAME":
                return self.driver.wait_for_object("device_name_table_header", invisible=not displayed)
        elif column_name == "CONNECTIVITY":
                return self.driver.wait_for_object("device_status_table_header", invisible=not displayed)

    ################################## Edit Group Popup ##################################################

    def click_devices_edit_group_button(self):
        return self.driver.click("devices_edit_group_btn")

    def verify_edit_group_popup_title(self):
        return self.driver.verify_object_string("edit_group_popup_title")

    def verify_edit_group_popup_description(self):
        return self.driver.verify_object_string("edit_group_popup_desc")

    def verify_edit_group_popup_delete_button(self):
        return self.driver.verify_object_string("edit_group_popup_delete_btn",timeout=10)

    def click_edit_group_popup_delete_button(self):
        return self.driver.click("edit_group_popup_delete_btn")

    def verify_edit_group_popup_create_tab(self):
        return self.driver.verify_object_string("edit_group_popup_create_tab")

    def verify_edit_group_popup_rename_tab(self):
        return self.driver.verify_object_string("edit_group_popup_rename_tab")

    def verify_edit_group_popup_close_button(self):
        return self.driver.verify_object_string("edit_group_popup_close_btn")

    def click_edit_group_popup_close_button(self):
        return self.driver.click("edit_group_popup_close_btn")

    def select_group(self,group_name):
        return self.driver.click("group_list_group_name",format_specifier=[group_name],timeout=30) # Add timeout to handle the slow loading of the group list

    ################################## Edit Group Popup Create Tab ##################################################

    def verify_edit_group_popup_create_tab_description(self):
        return self.driver.verify_object_string("create_tab_desc")

    def verify_edit_group_popup_create_tab_group_name_label(self):
        return self.driver.verify_object_string("create_tab_group_name_lbl")

    def verify_edit_group_popup_create_tab_group_name_field(self):
        return self.driver.wait_for_object("create_tab_group_name_txt")

    def enter_edit_group_popup_create_tab_group_name(self,group_name):
        return self.driver.send_keys("create_tab_group_name_txt",group_name)

    def verify_edit_group_popup_create_tab_parebnt_group_label(self):
        return self.driver.verify_object_string("create_tab_parent_group_lbl")

    def verify_edit_group_popup_create_tab_parebnt_group_dropdown(self):
        return self.driver.wait_for_object("create_tab_parent_group_dropdown")

    def verify_edit_group_popup_create_tab_create_button(self):
        return self.driver.verify_object_string("create_tab_create_btn")

    def click_edit_group_popup_create_tab_create_button(self):
        return self.driver.click("create_tab_create_btn")

    ################################## Edit Group Popup Rename Tab ##################################################

    def click_edit_group_popup_rename_tab(self):
        return self.driver.click("edit_group_popup_rename_tab")

    def verify_edit_group_popup_rename_tab_description(self):
        return self.driver.verify_object_string("rename_tab_desc")

    def verify_edit_group_popup_rename_tab_group_name_label(self):
        return self.driver.verify_object_string("rename_tab_group_name_lbl")

    def edit_group_popup_enter_group_name(self,group_name):
        return self.driver.send_keys("rename_tab_group_name_txt",group_name)

    def verify_edit_group_popup_rename_tab_group_name_field(self):
        return self.driver.wait_for_object("rename_tab_group_name_txt")

    def verify_edit_group_popup_rename_tab_rename_button(self):
        return self.driver.verify_object_string("rename_tab_rename_btn")

    def click_edit_group_popup_rename_tab_rename_button(self):
        return self.driver.click("rename_tab_rename_btn")

    def verify_select_group_warning_message(self,displayed=True):
        if displayed:
            return self.driver.verify_object_string("rename_tab_select_group_warning_message")
        else:
            return self.driver.wait_for_object("rename_tab_select_group_warning_message", invisible=not displayed)

    def verify_edit_group_popup_rename_tab_group_name_textbox_status(self,status):
        if status == "disabled":
            if self.driver.find_object("rename_tab_group_name_txt").is_enabled():
                raise UnexpectedItemPresentException(" Group Name textbox is enabled")
            return True
        else:
            if self.driver.find_object("rename_tab_group_name_txt").is_enabled() is False:
                raise UnexpectedItemPresentException(" Group Name textbox is disabled")
            return True

    def verify_edit_group_popup_rename_tab_rename_button_is_disabled(self):
        if self.driver.find_object("rename_tab_rename_btn").is_enabled():
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

    ################################## Properties Tab ##################################################

    def click_device_details_properties_tab(self):
        return self.driver.click("device_details_properties_tab",timeout=30)
    
    def verify_ews_accordion(self):
        return self.driver.verify_object_string("device_details_properties_tab_ews_card",timeout=30)

    def verify_network_accordion(self):
        return self.driver.verify_object_string("device_details_properties_tab_network_card")

    def verify_security_accordion(self):
        return self.driver.verify_object_string("device_details_properties_tab_securiry_card")

    def verify_supplies_accordion(self):
        return self.driver.verify_object_string("device_details_properties_tab_supplies_card")

    def verify_device_accordion(self):
        return self.driver.verify_object_string("device_details_properties_tab_device_card")

    def verify_show_editable_items_only(self):
        return self.driver.verify_object_string("device_details_properties_tab_show_editable")

    def verify_show_editable_items_only_toggle_status(self):
        self.driver.wait_for_object("show_editable_items_only_radio_btn")
        # toggle_status = self.driver.get_attribute("device_details_properties_tab_show_editable_toggle","aria-checked")
        # if toggle_on:
        #     assert toggle_status == 'true'
        # else:
        #     assert toggle_status == 'false'

    def get_device_details_overview_asset_number(self):
        return self.driver.wait_for_object("devices_details_overview_asset_number",timeout=30).text
    
    def click_device_accordion(self):
        return self.driver.click("device_details_properties_tab_device_card",timeout=30)
    
    def click_device_details_device_property_card(self,setting_card):
        return self.driver.click("device_details_device_property_card",format_specifier=[setting_card],timeout=15)
    
    def get_device_details_device_property_value(self,setting_card):
        return self.driver.wait_for_object("device_details_device_property_value",format_specifier=[setting_card],timeout=15).text
    
    def click_edit_button_from_settings_list_in_properties_tab(self,setting_card):
        return self.driver.click("device_details_device_property_edit_button",format_specifier=[setting_card])

    def click_security_accordion(self):
        return self.driver.click("device_details_properties_tab_securiry_card",timeout=30)

    def verify_security_pjl_password_properties_tab_setting_title(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("security_pjl_password_properties_tab_setting_title"))
        if self.driver.verify_object_string("security_pjl_password_properties_tab_setting_title") is True:
            return True
        else:
            raise UnexpectedItemPresentException("Title is not present")
    
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
        self.driver.send_keys("snmp_v3_authentication_confirm_password_textbox",passphase)
        self.driver.send_keys("snmp_v3_privacy_password_textbox",passphase)
        self.driver.send_keys("snmp_v3_privacy_confirm_password_textbox",passphase)
        
    ################################## Device Details - Policy Tab ##################################################

    def click_device_details_policy_tab(self):
        return self.driver.click("device_details_policy_tab",timeout=30)

    def verify_device_details_policy_tab(self):
        return self.driver.verify_object_string("device_details_policy_tab",timeout=30)
    
    def verify_device_details_policies_tab_compliance_status_widget(self):
        return self.driver.wait_for_object("device_details_policies_tab_compliance_status_widget",timeout=30)
    
    def click_device_details_policies_tab_compliance_status_widget(self):
        return self.driver.click("device_details_compliance_status_widget_expand_button")
    
    def verify_device_details_device_specific_policy_card(self):
        return self.driver.wait_for_object("device_details_policy_card",timeout=30)
    
    def verify_device_details_policy_card_title(self):
        return self.driver.verify_object_string("device_details_policy_card_title",timeout=30)

    def click_device_details_policy_widget_expand_button(self):
        return self.driver.click("device_details_policy_widget_expand_button",timeout=30)
    
    def device_specific_policy_card_empty(self):
        if self.driver.wait_for_object("device_details_specific_policy_no_policy_warning_message", raise_e=False) is not False:
            return True
        else:
            return False

    def click_policy_device_specific_policy_compliance_accordian(self):
        return self.driver.click("policy_device_specific_policy_compliance_accordian")

    def check_toast_successful_message(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)

    def check_bottom_toast_policy_create_success_msg(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_policy_create_success_msg").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)


    def click_device_specific_policy_edit_button(self):
        return self.driver.click("device_details_specific_policy_edit_btn")

    def verify_device_specific_policy_edit_button(self):
        return self.driver.verify_object_string("device_details_specific_policy_edit_btn")
    
    def click_device_specific_policy_checkbox(self):
        return self.driver.click("edit_specific_policy_table_checkbox")

    def click_device_specific_policy_next_button(self):
        return self.driver.click("edit_specific_policy_next_btn")

    def click_device_specific_policy_remove_button(self):
        return self.driver.click("edit_specific_policy_remove_btn")

    def verify_device_specific_policy_card_no_policy_message(self):
        self.driver.verify_object_string("device_details_specific_policy_no_policy_warning_message")
        return self.driver.verify_object_string("device_details_specific_policy_no_policy_warning_message_end_part")

    def search_policy_settings(self,setting_name):
        self.driver.wait_for_object("policy_settigs_search_txt", timeout=30) 
        return self.driver.send_keys("policy_settigs_search_txt",setting_name)

    def click_device_specific_policy_create_button(self):
        return self.driver.click("edit_specific_policy_remove_btn")

    def verify_device_specific_policy_setting_added(self,policy_setting_name):
        return self.driver.wait_for_object("device_specific_name_policy",format_specifier=[policy_setting_name])
    
    def verify_edit_device_policy_settings_title(self):
        return self.driver.verify_object_string("edit_device_policy_settings_title",timeout=30)
    
    def click_device_specific_policy_settings_card(self,setting_card):
        return self.driver.click("device_specific_policy_settings_card",format_specifier=[setting_card])
    
    def click_ignore_unsupported_item_toggle(self):
        return self.driver.click("ignore_unsupported_item_toggle")
    
    def click_user_requested_tray_first_radio_button(self):
        return self.driver.click("user_requested_tray_first_radio_button")
    
    def click_user_requested_tray_exclusively_radio_button(self):
        return self.driver.click("user_requested_tray_exclusively_radio_button")
    
    def click_manual_feed_prompt_unless_loaded(self):
        return self.driver.click("manual_feed_prompt_unless_loaded")

    def click_manual_feed_prompt_always(self):
        return self.driver.click("manual_feed_prompt_always")

    def click_manual_feed_first_radio_button(self):
        return self.driver.click("manual_feed_first_radio_button")

    def click_manual_feed_cassette_radio_button(self):
        return self.driver.click("manual_feed_cassette_radio_button")
    
    def enter_device_property_value(self,settings_value,setting_card):
        return self.driver.send_keys("device_specific_policy_device_property_value_txt",settings_value,clear_text=False,format_specifier=[setting_card])
    
    def check_toast_successful_msg(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)
    
    ####################### Device Details - HP Secure Fleet Manager Tab #################
 
    def verify_device_details_hp_secure_fleet_manager_tab(self):
        return self.driver.verify_object_string("device_details_hp_secure_fleet_manager_tab",timeout=30)
 
    def click_device_details_hp_secure_fleet_manager_tab(self):
        return self.driver.click("device_details_hp_secure_fleet_manager_tab")
    
    ######################## Device Details Connectivity Type Widget #####################

    def verify_device_detail_connectivity_type_widget_title(self):
        return self.driver.verify_object_string("device_detail_connectivity_type_widget_header", timeout=10)
    
    def get_device_detail_connectivity_type_widget_device_type(self):
        return self.driver.get_text("connectivity_type_widget_device_type")
        
    def verify_device_details_connectivity_type_widget_proxy_status(self):
        return self.driver.wait_for_object("connectivity_type_widget_proxy_status")
    
    def cick_connectivity_type_widget_view_details_link(self):
        return self.driver.click("connectivity_type_widget_view_details_link")
    
    def remove_existing_device_specific_policy(self):
        self.click_device_specific_policy_edit_button()
        self.verify_edit_device_policy_settings_title()
        self.click_device_specific_policy_checkbox()
        # to uncheck all the policies
        self.click_device_specific_policy_checkbox()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_create_button()
        self.click_device_details_policy_widget_expand_button()
        self.dismiss_toast()

    def click_edit_group_popup_group_name(self,group_name):
        self.driver.click("edit_group_popup_group_name", format_specifier=[group_name], timeout=30)
        # Group name locator got fixed, so commenting this code
        # try:
        #     # Attempt to click on the first element
        #     self.driver.click("group_list_group_name", format_specifier=[group_name])
        # except Exception as e:
        #     print(f"Failed to click on group_list_group_name due to: {e}")
        #     # If the first click fails, attempt to click on the second element
        #     self.driver.click("edit_group_popup_group_name", format_specifier=[group_name], timeout=30)

    def create_group_with_one_device(self,group_name,serial_number):
        if self.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.click_groups_side_bar_expand_btn()
        self.click_devices_create_group_button()
        self.enter_group_name(group_name)
        self.click_create_group_popup_create_button()
        self.dismiss_toast()
        self.search_device(serial_number)
        self.click_devices_checkbox()
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_select_action_dropdown_option("Move to group")
        self.click_contextual_footer_continue_button()
        self.select_group(group_name)
        self.click_move_to_group_popup_move_button()
        self.dismiss_toast()

    def delete_group(self,group_name):
        self.verify_device_page()
        if self.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.click_groups_side_bar_expand_btn()
        self.click_devices_edit_group_button()
        self.click_edit_group_popup_group_name(group_name)
        self.click_edit_group_popup_delete_button()
        self.click_delete_group_popup_delete_button()
        self.dismiss_toast()
        self.click_edit_group_popup_close_button()
    
    def get_device_cloud_id(self):
        full_url = self.driver.get_current_url()
        cloud_id = full_url.split("devices/")[1]
        return cloud_id
    
    def click_change_not_recommended_popup_confirm_button(self):
        #For some settings confirm button is coming before done button, so to handle this below click is used.
        return self.driver.click("change_not_recommended_popup_confirm_button", timeout=5, raise_e=False)

    def click_set_options_settings_checkbox(self, setting_card=None):
        return self.driver.click("set_options_settings_checkbox", format_specifier=[setting_card])

    def click_tcp_ip_printing_remediation_checkbox(self):
        return self.driver.click("remediation_checkbox")
    
    def click_configure_ip_label(self):
        return self.driver.click("configure_ip_label")
    
    def click_device_announcement_agent_auth_certificate_checkbox(self):
        return self.driver.click("device_announcement_agent_auth_certificate_checkbox")
    
    def click_browser_language_settings_checkbox(self):
        return self.driver.click("browser_language_settings_checkbox")

    def click_printer_language_settings_checkbox(self):
        return self.driver.click("printer_language_settings_checkbox")

    def navigating_to_device_details_tab(self, temp_group_name):
        self.verify_device_page()
        if self.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.click_groups_side_bar_expand_btn()
        self.click_devices_group(temp_group_name)
        self.click_first_entry_link()
        self.click_device_details_policy_tab()

    def add_settings_in_device_specific_policy_tab(self, setting_name, setting_card=None, settings_value=None, category_type=None):
        self.click_device_details_policy_tab()
        self.click_device_details_policy_widget_expand_button()
        if self.device_specific_policy_card_empty() is False:
            self.remove_existing_device_specific_policy()
        self.click_device_specific_policy_edit_button()
        self.search_policy_settings(setting_name)
        self.click_device_specific_policy_checkbox()
        self.click_device_specific_policy_next_button()
        if category_type == "Copier": 
            self.modify_copier_settings_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Devices":
            self.modify_devices_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Digital Sending":
            self.modify_digital_sending_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Embedded Web Server":
            self.modify_ews_category_setting_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Fax":
            self.modify_fax_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "File System":
            self.modify_file_system_category_setting_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Network":
            self.modify_network_category_setting_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Security":
            self.modify_security_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
        elif category_type == "Supplies":
            self.modify_supplies_category_settings_in_device_specific_policy_settings(setting_card, settings_value)
        else:
            self.modify_web_services_category_settings_in_device_specific_policy_settings(setting_card, settings_value)

    def click_proxy_device_settings_checkbox(self, setting_name):
        return self.driver.click("proxy_device_settings_checkbox", format_specifier=[setting_name])

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
    
    def verify_service_access_code_textbox(self):
        if self.driver.find_object("service_access_code_textbox_disabled").is_enabled():
            raise UnexpectedItemPresentException("TextBox is enabled")
        return True

    def click_file_erase_non_secure_radio_button(self):
        return self.driver.click("file_erase_non_secure_radio_button")
    
    def click_file_erase_secure_fast_erase_radio_button(self):
        return self.driver.click("file_erase_secure_fast_erase_radio_button")
    
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
        elif option == 5:
            options[4].click()   

    def click_copy_optimize_printed_picture_radio_button(self):
        return self.driver.click("copy_optimize_printed_picture_radio_button")
    
    def click_copy_optimize_photograph_radio_button(self):
        return self.driver.click("copy_optimize_photograph_radio_button")

    def click_copy_optimize_text_radio_button(self):
        return self.driver.click("copy_optimize_text_radio_button")
    
    def click_copy_optimize_mixed_radio_button(self):
        return self.driver.click("copy_optimize_mixed_radio_button")
    
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
        elif option == 6:
            options[5].click()
        
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
        elif option == 6:
            options[5].click()
    
    def click_time_services_do_not_sync_network_time_server(self):
        return self.driver.click("time_services_do_not_sync_network_time_server")
    
    def click_time_services_automatic_sync_custom_network_time_server(self):
        return self.driver.click("time_services_automatic_sync_custom_network_time_server")
    
    def click_ps_access_option(self):
        return self.driver.click("ps_access_option")

    def click_pjl_access_option(self):
          return self.driver.click("pjl_access_option")
    
    def select_control_panel_language(self,language):
        lang_dict = {"English": "en", "Russian": "ru", "Spanish": "es"}
        self.driver.click("control_panel_language_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("control_panel_language_option",format_specifier=[lang_dict[language]]))
        return self.driver.click("control_panel_language_option",format_specifier=[lang_dict[language]])

    def select_fax_header_location(self,location):
        loca_dict = {"Canada": "ca", "India": "in", "Russia": "ru"}
        self.driver.click("fax_header_location_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("fax_header_location_option",format_specifier=[loca_dict[location]]))
        return self.driver.click("fax_header_location_option",format_specifier=[loca_dict[location]])

    def set_scan_settings_background_cleanup(self,background_method):
        self.driver.click("fax_send_background_cleanup_dropdown")
        if background_method == 3:
            self.driver.click("fax_send_less_specks_option")
        elif background_method == 9:
            self.driver.click("fax_send_more_specks_option")
        else:
            self.driver.click("fax_send_normal_option")
    
    def set_scan_settings_darkness(self,exposure):
        self.driver.click("fax_send_darkness_dropdown")
        if exposure == 5:
            self.driver.click("fax_send_darker_option")
        elif exposure == 9:
            self.driver.click("fax_send_lighter_option")
        else:
            self.driver.click("fax_send_darkness_normal_option")
    
    def set_scan_settings_contrast(self,contrast):
        self.driver.click("fax_send_contrast_dropdown")
        if contrast == 5:
            self.driver.click("fax_send_contrast_more_option")
        elif contrast == 9:
            self.driver.click("fax_send_contrast_less_option")
        else:
            self.driver.click("fax_send_contrast_normal_option")
    
    def set_scan_settings_sharpness(self,sharpness):
        self.driver.click("fax_send_sharpness_dropdown")
        if sharpness == 3:
            self.driver.click("fax_send_sharper_edges_option")
        elif sharpness == 5:
            self.driver.click("fax_send_softer_edges_option")
        else:
            self.driver.click("fax_send_sharpness_normal_option")

    def set_notification_settings_condition_and_method(self,notification_condition,notification_mode,email_address):
        if notification_condition == "never":
            self.driver.click("fax_send_conditions_to_notify_dropdown")
            self.driver.click("fax_send_notify_if_job_fails_option")
            if notification_mode == "email":
                self.driver.click("fax_send_used_to_deliver_notification_dropdown")
                self.driver.click("fax_send_and_receive_set_common_job_print_option")
            else:
                self.driver.send_keys("fax_send_email_address_textfield",email_address)
            self.driver.click("fax_send_set_common_job_save_button")
        else:
            self.driver.click("fax_send_set_common_job_save_button")
    
    def set_internet_fax_service(self,domain_name,account_email_address):
        self.driver.click("fax_send_internet_fax_service_radio_button")
        self.driver.click("fax_send_set_internet_fax_service_button")
        self.driver.send_keys("fax_send_set_internet_fax_service_domain_textfield",domain_name)
        self.driver.send_keys("fax_send_set_internet_fax_service_email_address_textfield",account_email_address)
        self.driver.click("fax_send_set_internt_fax_service_save_button")
    
    def click_fax_send_ip_fax_method(self):
        return self.driver.click("fax_send_ip_fax_method_option")
    
    def set_intern_modem_settings(self,error_correction_mode_status,jbig_compression_status):
        self.driver.click("fax_send_internal_modem_radio_button")
        self.driver.click("fax_send_and_receive_set_internal_modem_option")
        if error_correction_mode_status == "true":
            self.driver.click("fax_send_error_correction")
        if jbig_compression_status == "true":
            self.driver.click("fax_send_jbig_compression")
        self.driver.click("fax_send_set_internal_modem_popup_save_button")

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
    
    def set_country_value_for_fax_header_setting(self,settings_value):
        test_phone_number = settings_value[0]
        company_name = settings_value[1]
        fax_header_country_status = settings_value[2]
        self.driver.send_keys("fax_header_phone_number_text_box",test_phone_number)
        self.driver.send_keys("fax_header_company_name_text_box",company_name)
        if fax_header_country_status == "ca":
            self.select_fax_header_location("India")
        if fax_header_country_status == "in":
            self.select_fax_header_location("Russia")
        else:
            self.select_fax_header_location("Canada")

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
                self.click_fax_send_ip_fax_method()
            else:
                self.set_intern_modem_settings(error_correction_mode_status,jbig_compression_status)

    def set_plug_and_play_status(self,settings_value,setting_card):
        plug_and_play_status = settings_value[0]
        print_from_usb_status = settings_value[1]
        scan_to_usb_status = settings_value[2]
        if plug_and_play_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            if print_from_usb_status == "false":
                self.driver.click("host_plug_and_play_retrieve_from_usb_checkbox")
            if scan_to_usb_status == "false":
                self.driver.click("host_plug_and_play_save_to_usb_checkbox")

    def update_temporary_and_standard_retain_jobs_setting_attributes(self, settings_value):
        stored_jobs_enabled_status = settings_value[0]
        temporary_stored_job_status = settings_value[1]
        standard_stored_job_status = settings_value[2]

        if stored_jobs_enabled_status == "true":
            self.driver.click("retain_print_stored_jobs_checkbox")
        else:
            self.set_temporary_stored_job(temporary_stored_job_status)
            self.set_standard_stored_job(standard_stored_job_status)
    
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
        
    def set_default_paper_selection(self,paper_selection_status):
        self.driver.click("fax_receive_paper_selection_dropdown")
        if paper_selection_status == "auto":
            self.driver.click("fax_receive_paper_selection_tray1")
        elif paper_selection_status == "tray1":
            self.driver.click("fax_receive_paper_selection_tray2")
        else:
            self.driver.click("fax_receive_paper_selection_auto")
    
    def set_default_notification_settings(self,notification_condition_status,notification_mode_status,email_address):
        self.driver.click("fax_receive_do_not_notify_dropdown")
        if notification_condition_status == "never":
            self.driver.click("fax_receive_job_failed_option")
            if notification_mode_status == "email":
                self.driver.click("fax_receive_deliver_notification_dropdown")
                self.driver.click("fax_send_and_receive_set_common_job_print_option")
            else:
                self.driver.send_keys("fax_receive_set_common_job_email_textfield",email_address)
            self.driver.click("fax_receive_set_common_job_save_button")
    
    def set_fax_receive_ip_fax(self):
        return self.driver.click("fax_receive_ip_fax_method_option")

    def set_fax_receive_internal_modem_attributes(self,ringer_volume_status,rings_to_answer_status):
        self.driver.click("fax_receive_set_internal_modem_button")
        self.driver.click("fax_receive_internal_modem_ringer_volume_dropdown")
        if ringer_volume_status == "off":
            self.driver.click("internal_modem_ringer_volume_high_option")
        if ringer_volume_status == "high":
            self.driver.click("internal_modem_ringer_volume_low_option")
        else:
            self.driver.click("internal_modem_ringer_volume_off_option")
            self.driver.send_keys("internal_modem_rings_to_answer_textbox",rings_to_answer_status)
            self.driver.click("set_internal_modem_popup_save_button")

    def update_fax_receive_setting_attributes(self, settings_value):
        fax_receive_status = settings_value[0]
        paper_selection_status = settings_value[1]
        notification_condition_status = settings_value[2]
        notification_mode_status = settings_value[3]
        email_address = settings_value[4]
        fax_receive_method_status = settings_value[5]
        ringer_volume_status = settings_value[6]
        rings_to_answer_status = settings_value[7]
        if fax_receive_status == "false":
            self.driver.click("fax_receive_setting_checkbox")
            self.driver.click("fax_send_and_receive_set_common_job_option")
            self.set_default_paper_selection(paper_selection_status)
            self.set_default_notification_settings(notification_condition_status,notification_mode_status,email_address)
            if fax_receive_method_status == "internalModem":
               self.set_fax_receive_ip_fax()
            else:
                self.set_fax_receive_internal_modem_attributes(ringer_volume_status,rings_to_answer_status)

    def set_ip_values_and_auth_status_for_device_announcement_setting(self,setting_card,settings_value):
        announcement_status = settings_value[0]
        configuration_server_ip = settings_value[1]
        server_auth_status = settings_value[2]
        if announcement_status == False:
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.send_keys("device_announcement_agent_server_ip",configuration_server_ip)
            if server_auth_status == False:
                self.click_configure_ip_label()
                self.click_device_announcement_agent_auth_certificate_checkbox()

    def set_digital_sending_allow_use_and_allow_transfer_attribute(self,settings_value):
        digital_sending_allow_use = settings_value[0]
        digital_sending_allow_transfer = settings_value[1]
        if digital_sending_allow_use == "true":
            self.driver.click("digital_sending_allow_use_checkbox")
        else:
            if digital_sending_allow_transfer == "true":
                self.driver.click("digital_sending_allow_transfer_checkbox")

    def set_languages_in_ews_language_setting(self,settings_value):
        selected_language = settings_value[0]
        language_source_status = settings_value[1]
        if language_source_status == "ews":
            self.click_browser_language_settings_checkbox()
        elif language_source_status == "browser":
            self.click_printer_language_settings_checkbox()
        elif language_source_status == "device":
            if selected_language == "en":
                self.select_control_panel_language("Russian")
            else:
                self.select_control_panel_language("English")

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

    def set_server_address_and_port_value_for_proxy_server_settings(self,setting_card,settings_value):
        proxy_server_status = settings_value[0]
        server_address = settings_value[1]
        server_port = settings_value[2]
        if proxy_server_status == "false":
            self.click_set_options_settings_checkbox(setting_card)
            self.driver.send_keys("proxy_server_address_txt",server_address)
            self.driver.send_keys("proxy_server_port_txt",server_port)

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

    def set_energy_settings_inactivity(self, inactivityTimeout):
        self.driver.click("energy_settings_inactivity_dropdown")
        if inactivityTimeout == 1:
            self.driver.click("energy_settings_off_inactivity_five_minutes_option")
        elif inactivityTimeout == 5:
            self.driver.click("energy_settings_off_inactivity_fifteen_minutes_option")
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

    def set_email_scan_settings(self, settings_value):
        if settings_value == "photo":
            self.driver.click("email_scan_settings_photograph_radio_button")
        elif settings_value == "glossy":
            self.driver.click("email_scan_settings_text_radio_button")
        elif settings_value == "text":
            self.driver.click("email_scan_settings_mixed_radio_button")
        elif settings_value == "mixed":
            self.driver.click("email_scan_settings_printed_picture_radio_button")

    def set_email_notifications(self,notification_condition_status,notification_mode_status,email_addresses):
        if notification_condition_status == "never":
            self.driver.click("email_notification_settings_notify_job_fails_radio_button")
            if notification_mode_status == "email":
                self.driver.click("email_notification_settings_deliver_notification_print_radio_button")
            else:
                self.driver.send_keys("email_notification_settings_deliver_notification_email_textbox",email_addresses)
                
    def update_network_folder_notification_settings(self,notification_condition_status,notification_mode_status,email_addresses):
        if notification_condition_status == "never":
            self.driver.click("network_folder_notification_settings_notify_job_fails_radio_button")
            if notification_mode_status == "email":
                self.driver.click("network_folder_notification_settings_deliver_notification_print_radio_button") 
            else:
                self.driver.send_keys("network_folder_notification_settings_deliver_notification_email_textbox",email_addresses)
        
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

    def set_email_notification_settings(self,settings_value):
        notification_condition_status=settings_value[0]
        notification_mode_status=settings_value[1]
        email_addresses=settings_value[2]
        self.set_email_notifications(notification_condition_status,notification_mode_status,email_addresses)

    def set_network_folder_notification_settings(self,settings_value):
        notification_condition_status=settings_value[0]
        notification_mode_status=settings_value[1]
        email_addresses=settings_value[2]
        self.update_network_folder_notification_settings(notification_condition_status,notification_mode_status,email_addresses)

    def set_restrict_color_status(self,settings_value):
        restrict_color = settings_value[0]
        restrict_by_application = settings_value[1]
        default_permission = settings_value[2]
        name = settings_value[3]    
        non_default_permission = settings_value[4]
        if restrict_color == "enableColor":
            self.driver.click("enable_set_color_access_radio_button")
            if restrict_by_application == "true":
                self.driver.click("restrict_by_application_checkbox")
            else:
                self.set_default_and_non_default_permission_for_application(default_permission,name,non_default_permission)

    def set_default_and_non_default_permission_for_application(self,default_permission,name,non_default_permission):
        if default_permission == "bestColor":
            self.driver.click("default_permission_remove_color_radio_button")
        self.driver.click("restrict_color_add_button")
        self.driver.send_keys("restirct_color_add_popup_application_name_textbox", name)
        if non_default_permission == "bestColor":
            self.driver.click("restrict_color_add_popup_remove_color_radio_button")
        self.driver.click("restrict_color_add_popup_add_button")
    
    def update_sleep_settings(self,sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values):
        self.driver.send_keys("sleep_settings_sleep_mode_textbox",sleep_mode_values)
        if auto_on_events_status == "powerButtonPress":
            self.driver.click("sleep_settings_wake_all_events_radio_button")
        elif auto_on_events_status == "all":
            self.driver.click("sleep_settings_wake_network_port_radio_button")
        else:
            self.driver.click("sleep_settings_wake_power_button_only_radio_button")
        self.driver.send_keys("sleep_settings_auto_off_textbox",auto_off_after_sleep_values)
    
    def set_sleep_settings(self,settings_value):
        sleep_auto_off_timer_status=settings_value[0]
        sleep_mode_values=settings_value[1]
        auto_on_events_status=settings_value[2]
        auto_off_after_sleep_values=settings_value[3]
        if  sleep_auto_off_timer_status == "false":
            self.click_set_options_settings_checkbox("sleep-settings")
            self.update_sleep_settings(sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values)
        else:
            self.click_set_options_settings_checkbox("sleep-settings")

    def set_cartridge_very_low_action_black(self,settings_value):
        cartridge_very_low_action_black_status=settings_value
        if cartridge_very_low_action_black_status == "stop":
            self.driver.click("cartridge_very_low_action_black_prompt_to_continue_radio_button")
        elif cartridge_very_low_action_black_status == "prompt":
            self.driver.click("cartridge_very_low_action_black_continue_radio_button")
        else:
            self.driver.click("cartridge_very_low_action_black_stop_radio_button")
        
    def set_cartridge_very_low_action_color(self,settings_value):
        cartridge_very_low_action_color_status=settings_value
        if cartridge_very_low_action_color_status == "stop":
            self.driver.click("cartridge_very_low_action_color_prompt_to_continue_radio_button")
        elif cartridge_very_low_action_color_status == "prompt":
            self.driver.click("cartridge_very_low_action_color_continue_radio_button")
        else:
            self.driver.click("cartridge_very_low_action_color_stop_radio_button")

    def update_email_file_setting_prefix_value(self,email_file_name_prefix):
        self.driver.click("email_file_file_name_prefix_dropdown")
        if email_file_name_prefix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("email_file_name_prefix_time_option")
        elif email_file_name_prefix == "%DEVICE_TIME_HHMMSS%":
            self.driver.click("email_file_name_prefix_username_option")
        elif email_file_name_prefix == "%SECURITY_USERNAME%":
            self.driver.click("email_file_name_prefix_hostname_option")
        else:
            self.driver.click("email_file_name_prefix_date_option")

    def update_email_file_setting_suffix_value(self,email_file_name_suffix):
        self.driver.click("email_file_file_name_suffix_dropdown")
        if email_file_name_suffix == "%DEVICE_DATE_DDMMYYYY%":
            self.driver.click("email_file_name_suffix_time_option")
        elif email_file_name_suffix == "%DEVICE_TIME_HHMMSS%":
            self.driver.click("email_file_name_suffix_username_option")
        elif email_file_name_suffix == "%SECURITY_USERNAME%":
            self.driver.click("email_file_name_suffix_hostname_option")
        else:
            self.driver.click("email_file_name_suffix_date_option")
        self.driver.click("email_file_name_popup_save_button")

    def update_email_original_size_and_default_output_quality(self,default_output_quality):
        self.driver.click("email_file_original_size_dropdown")
        self.driver.click("email_file_original_size_a4_option")
        self.driver.click("email_file_default_output_quality_dropdown")
        if default_output_quality == "high":
            self.driver.click("email_file_default_output_quality_low_option")
        elif default_output_quality == "low":
            self.driver.click("email_file_default_output_quality_medium_option")
        else:
            self.driver.click("email_file_default_output_quality_high_option")

    def update_default_file_type(self,default_file_type):
        self.driver.click("email_file_default_file_type_dropdown")
        if default_file_type == "jpeg":
            self.driver.click("email_file_file_type_pdf_option")
        elif default_file_type == "pdf":
            self.driver.click("email_file_file_type_pdfa_option")
        elif default_file_type == "pdfa":
            self.driver.click("email_file_file_type_tiff_option")
        else:
            self.driver.click("email_file_file_type_jpeg_option")

    def update_default_resolution_and_compression(self,default_resolution):
        self.driver.click("email_file_default_resolution_dropdown")
        if default_resolution == "75":
            self.driver.click("email_file_default_resolution_150_dpi_option")
        elif default_resolution == "150":
            self.driver.click("email_file_default_resolution_300_dpi_option")
        elif default_resolution == "300":
            self.driver.click("email_file_default_resolution_600_dpi_option")
        else:
            self.driver.click("email_file_default_resolution_75_dpi_option")
        self.driver.click("email_file_compression_dropdown")
        self.driver.click("email_file_copression_normal_option")

    def update_pdf_encryption_and_blank_page_suppression(self,pdf_encryption,blank_page_suppression):
        if pdf_encryption == "false":
            self.driver.click("email_file_pdf_encryption_checkbox")
        if blank_page_suppression == "false":
            self.driver.click("email_file_blank_page_suppression_checkbox")

    def set_email_file_settings_attributs_values(self,setting_value):
        self.driver.click("email_file_setting_set_file_name_button")
        email_file_name_prefix = setting_value[0]
        default_file_name = setting_value[1]
        user_ediatable = setting_value[2]
        email_file_name_suffix = setting_value[3]
        default_output_quality = setting_value[4]
        default_file_type = setting_value[5]
        default_resolution = setting_value[6]
        pdf_encryption = setting_value[7]
        blank_page_suppression = setting_value[8]
        self.update_email_file_setting_prefix_value(email_file_name_prefix)
        self.driver.send_keys("email_defult_file_name_text_box",default_file_name)
        if user_ediatable == "true":
            self.driver.click("email_file_name_user_editable_checkbox")
        self.update_email_file_setting_suffix_value(email_file_name_suffix)
        self.update_email_original_size_and_default_output_quality(default_output_quality)
        self.update_default_file_type(default_file_type)
        self.update_default_resolution_and_compression(default_resolution)
        self.update_pdf_encryption_and_blank_page_suppression(pdf_encryption,blank_page_suppression)
    
    def update_set_file_name_setting(self,prefix_status,filename,user_editable_status,suffix_status):
        self.driver.click("network_folder_file_setting_file_name_button")
        self.driver.click("network_folder_file_name_prefix_dropdown")
        if prefix_status == "%DEVICE_TIME_DDMMYYYY%":
            self.driver.click("network_folder_file_name_prefix_time_hours_min_sec_option")
        elif prefix_status == "%DEVICE_TIME_HHMMSS":
            self.driver.click("network_folder_file_name_prefix_user_name_option")
        elif prefix_status == "%SECURITY_USERNAME%":
            self.driver.click("network_folder_file_name_prefix_host_name_option")
        else:
            self.driver.click("network_folder_file_name_prefix_date_month_year_option")
        
        self.driver.send_keys("network_folder_default_file_name_text_field",filename)

        if user_editable_status == "true":
            self.driver.click("network_folder_user_editable_checkbox")

        self.driver.click("network_folder_file_name_suffix_dropdown")
        if suffix_status == "%DEVICE_TIME_DDMMYYYY%":
            self.driver.click("network_folder_file_name_suffix_time_hours_min_sec_option")
        elif suffix_status == "%DEVICE_TIME_HHMMSS":
            self.driver.click("network_folder_file_name_suffix_user_name_option")
        elif suffix_status == "%SECURITY_USERNAME%":
            self.driver.click("network_folder_file_name_suffix_host_name_option")
        else:
            self.driver.click("network_folder_file_name_suffix_date_month_year_option")
        self.driver.click("network_folder_file_setting_save_button")

    def set_original_size(self):
        self.driver.click("network_folder_original_file_dropdown")
        self.driver.click("network_folder_original_file_a4_option")
    
    def set_default_output_quality(self,output_quality_status):
        self.driver.click("network_folder_output_quality_dropdown")
        if output_quality_status == "high":
            self.driver.click("network_folder_output_quality_low_option")
        elif output_quality_status == "low":
            self.driver.click("network_folder_output_quality_medium_option")
        else:
            self.driver.click("network_folder_output_quality_high_option")
    
    def set_default_file_type(self,file_type_status):
        self.driver.click("network_folder_file_type_dropdown")
        if file_type_status == "tiff":
            self.driver.click("network_folder_file_type_pdf_option")
        elif file_type_status == "pdf":
            self.driver.click("network_folder_file_type_pdfa_option")
        elif file_type_status == "pdfa":
            self.driver.click("network_folder_file_type_jpeg_option")
        else:
            self.driver.click("network_folder_file_type_tiff_option")

    def set_default_resolution(self,resoultion_status):
        self.driver.click("network_folder_resolution_dropdown")
        if resoultion_status == "e200Dpi":
            self.driver.click("network_folder_resolution_300dpi_option")
        elif resoultion_status == "e300Dpi":
            self.driver.click("network_folder_resolution_75dpi_option")
        elif resoultion_status == "e75Dpi":
            self.driver.click("network_folder_resolution_150dpi_option")
        else:
            self.driver.click("network_folder_resolution_200dpi_option")
    
    def set_compression(self):
        self.driver.click("network_folder_compression_dropdown")
        self.driver.click("network_folder_compression_normal_option")

    def set_pdf_and_blank_page_supression_status(self,pdf_encryption_status,blank_page_supression_status):
        if pdf_encryption_status == "false":
            self.driver.click("network_folder_pdf_compression_checkbox")
        if blank_page_supression_status == "false":
            self.driver.click("network_folder_blank_page_supression_checkbox")

    def set_network_folder_file_settings(self,settings_value):
        prefix_status=settings_value[0]
        filename=settings_value[1]
        user_editable_status=settings_value[2]
        suffix_status=settings_value[3]
        output_quality_status=settings_value[4]
        file_type_status=settings_value[5]
        resoultion_status=settings_value[6]
        pdf_encryption_status=settings_value[7]
        blank_page_supression_status=settings_value[8]
        self.update_set_file_name_setting(prefix_status,filename,user_editable_status,suffix_status)
        self.set_original_size()
        self.set_default_output_quality(output_quality_status)
        self.set_default_file_type(file_type_status)
        self.set_default_resolution(resoultion_status)
        self.set_compression()
        self.set_pdf_and_blank_page_supression_status(pdf_encryption_status,blank_page_supression_status)
    
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
        
    def click_hp_web_services_checkbox(self):
        return self.driver.click("hp_web_services_checkbox")
    
    def click_hp_eprint_checkbox(self):
        return self.driver.click("hp_eprint_checkbox")

    def click_print_apps_checkbox(self):
        return self.driver.click("print_apps_checkbox")
    
    def set_eprint_settings_option(self):
        self.click_ignore_unsupported_item_toggle()
        self.click_hp_web_services_checkbox()
        self.click_hp_eprint_checkbox()
        self.click_print_apps_checkbox()
        self.click_device_specific_policy_create_button()
    
    def set_eprint_setting(self):
        self.click_hp_web_services_checkbox()
    
    def set_ipv4_information_setting(self,settings_value):
            ip_address_value = settings_value[0]
            subnet_mask_value = settings_value[1]
            gateway_value = settings_value[2]
            self.driver.send_keys("ip_address_textbox",ip_address_value)
            self.driver.send_keys("subnet_mask_textbox",subnet_mask_value)
            self.driver.send_keys("default_gateway_textbox",gateway_value)
            
    def modify_devices_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Devices Category
        # Devices Category Settings: Use Requested Tray, Override A4/Letter, Tray1 Mode/Manual Feed, Size Type Prompt, Manual Feed Prompt, Date and Time Format, Control Panel Language, Retain Print Jobs, Asset Number, Contact Person,4
        # Device Name, Device Location, Company Name, Energy Settings, AutoSend, Sleep Settings,Show Date and Time, Time Zone/Daylight Saving, ePrint Settings
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "use-requested-tray":
            if settings_value == "exclusively":
                self.click_user_requested_tray_first_radio_button()
            else:
                self.click_user_requested_tray_exclusively_radio_button()
            self.click_device_specific_policy_create_button()
        elif setting_card == "override-letter-a4":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "manual-feed":
            if settings_value == "false":
                self.click_manual_feed_first_radio_button()
            else:
                self.click_manual_feed_cassette_radio_button()
            self.click_device_specific_policy_create_button()
        elif setting_card == "size-type-prompt":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "manual-feed-prompt":
            if settings_value == "always":
                self.click_manual_feed_prompt_unless_loaded()
            else:
                self.click_manual_feed_prompt_always()
            self.click_device_specific_policy_create_button()
        elif setting_card == "date-time-format":
            self.set_devices_date_and_time_format(settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "ctrl-panel-language":
            # current_language = settings_value[0]
            if settings_value == "es":
                self.select_control_panel_language("Russian")
            else:
                self.select_control_panel_language("Spanish")
            self.click_device_specific_policy_create_button()
        elif setting_card == "retain-jobs":
            self.update_temporary_and_standard_retain_jobs_setting_attributes(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "energy-settings":
            inactivityTimeout = settings_value[0]
            shutdownTimeout = settings_value[1]
            self.set_energy_settings_inactivity(inactivityTimeout)
            self.set_energy_settings_shutdown(shutdownTimeout)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "auto-send":
            self.update_auto_send_setting_attributes(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "sleep-settings":
            self.set_sleep_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "time-zone":
            self.set_time_zone_setting(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "hp-web-svc":
            self.set_eprint_setting()
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "show-date-time":
            self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def modify_digital_sending_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Digital Sending Category
        # Digital Sending Category Settings: Save to Network Folder, Save to SharePoint, Send to Email, Email Address or Email Settings,
        # Email Scan Settings, Email Notification Settings, Network Folder Notification Settings, Email File Settings, Network Folder File Settings, IPv4 Information
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "save-to-network-folder":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "save-to-share-point":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "save-to-email":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "email-message":
            self.click_ignore_unsupported_item_toggle()
            self.set_email_address_message_in_email_setting_attributes(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "email-scan":
            self.set_email_scan_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "email-notification":
            self.set_email_notification_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "network-folder-notification":
            self.set_network_folder_notification_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "email-file":
            self.set_email_file_settings_attributs_values(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "network-folder-file":
            self.set_network_folder_file_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def modify_ews_category_setting_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Embedded Web Server Category
        # EWS Category Settings: EWS Language, Time Services
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "ews-language":
            self.set_languages_in_ews_language_setting(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "time-services":
            self.set_port_value_and_server_ip_address_for_time_services_settings(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
    
    def modify_fax_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Fax Category
        # Fax Category Settings: PC Fax Send, Fax Header Setting, Fax Send Settings, IP Fax, Fax Receive Settings
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "pc-fax-send":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "fax-header":
            self.set_country_value_for_fax_header_setting(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "fax-send":
            self.set_fax_send_method_for_fax_send_setting(setting_card,settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ip-fax":
            fax_ip = settings_value[0]
            company_name = settings_value[1]
            self.driver.send_keys("ip_fax_settings_company_name_text_box",fax_ip)
            self.driver.send_keys("ip_fax_settings_fax_id_text_box",company_name)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "fax-receive":
            self.click_ignore_unsupported_item_toggle()
            self.update_fax_receive_setting_attributes(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def modify_file_system_category_setting_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # File System Category
        # File System Category Settings: File Erase Mode, File System Access Protocol
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "file-erase":
            if settings_value == "secureFastErase":
                self.click_file_erase_non_secure_radio_button()
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "fs-access-protocol":
            ps_file_system_access_enabled_status = settings_value[0]
            pjl_file_system_access_enabled_status = settings_value[1]
            if ps_file_system_access_enabled_status == "false":
                self.click_ps_access_option()
            if pjl_file_system_access_enabled_status == "false":
                self.click_pjl_access_option()
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()

    def modify_network_category_setting_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Network Category
        # Network Category Settings: Wins Registration, Wins Port, LLMNR, SLP, Bonjour, WS-Discovery, IPP, IPPS, TCP/IP Printing 9100, LPD/LPR, WS-Print,
        # FTP-Print, Telnet, TFTP Configuration, AirPrint Scan/Secure Scan, AirPrint, Support Contact, System Location, AirPrint-Fax, System Contact, IPv4 Multicast
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "wins-registration":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button() 
        elif setting_card == "wins-port":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "llmnr":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "slp":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "bonjour":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ws-discovery":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ipp":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ipps":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "tcpip-print":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_tcp_ip_printing_remediation_checkbox()
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "lpd-lpr":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ws-print":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "ftp-print":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "telnet":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
                self.click_device_specific_policy_create_button()
                self.click_change_not_recommended_popup_confirm_button()
            else:
                self.click_device_specific_policy_create_button()
        elif setting_card == "tftp-cfg":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
                self.click_device_specific_policy_create_button()
                self.click_change_not_recommended_popup_confirm_button()
            else:
                self.click_device_specific_policy_create_button()
        elif setting_card == "airprint-scan-secure-scan":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "airprint":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "airprint-fax":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "ipv4-multicast":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "ipv4-info":
            self.set_ipv4_information_setting(settings_value)
            self.click_device_specific_policy_create_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def modify_security_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Security Category
        # Security Category Settings: XML Services, Device Announcement Agent, Host USB Plug and Play, Digital Sending Service, PJL Access Commands, Remote Firmware Update, Legacy Firmware Update, Display Color Usage Job, Servcie Access Code, Restrict Color
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "jd-xml-svc":
            if settings_value == True:
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "device-announcement":
            self.set_ip_values_and_auth_status_for_device_announcement_setting(setting_card,settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "host-usb-pnp":
            self.set_plug_and_play_status(settings_value,setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "digital-sending":
            self.set_digital_sending_allow_use_and_allow_transfer_attribute(settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "pjl-command":
            if settings_value == False:
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "remote-fw-update":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "legacy-fw-update":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "color-usage-log":
            if settings_value == "false":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        elif setting_card == "svc-access-code":
            self.verify_service_access_code_textbox()
            self.click_device_specific_policy_create_button()
        elif setting_card == "restrict-color":
            self.set_restrict_color_status(settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()
               
    def modify_web_services_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Web Servcies Category
        # Web Services Category Settings : Smart Cloud Print, HP JetAdvantage, Proxy Server
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "smart-cloud-print":
            if settings_value == "true":
                self.click_set_options_settings_checkbox(setting_card)
            self.click_device_specific_policy_create_button()
        elif setting_card == "hp-jet-adv":
            hp_jetadvantage = settings_value[0]
            hp_jetadvantage_accountcreation = settings_value[1]
            if hp_jetadvantage == "true":
                self.click_proxy_device_settings_checkbox("hp-jet-adv.check")
            else:
                if hp_jetadvantage_accountcreation == "true":
                    self.click_proxy_device_settings_checkbox("hp-jet-adv.create-account")
            self.click_device_specific_policy_create_button()
        elif setting_card == "proxy-server":
            self.set_server_address_and_port_value_for_proxy_server_settings(setting_card,settings_value)
            self.click_device_specific_policy_create_button()
            self.click_change_not_recommended_popup_confirm_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()      

    def modify_supplies_category_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Supplies Category
            # Supplies Category Settings: Cartridge Threshold - Black, Cartridge Threshold - Cyan  Cartridge Very Low Action - Black, Cartridge Very Low Action - Color, Cartridge Very Low Action - Black, Cartridge Very Low Action - Color
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "cartridge-threshold-black":
            self.driver.send_keys("cartridge_threshold_black_text_box",settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "cartridge-threshold-cyan":
            self.driver.send_keys("cartridge_threshold_cyan_text_box",settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "cartridge-threshold-magenta":
            self.driver.send_keys("cartridge_threshold_magenta_text_box",settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "cartridge-threshold-yellow":
            self.driver.send_keys("cartridge_threshold_yellow_text_box",settings_value)
            self.click_device_specific_policy_create_button()
        elif setting_card == "very-low-action-black":
            self.set_cartridge_very_low_action_black(settings_value[0])
            self.click_device_specific_policy_create_button()
        elif setting_card == "very-low-action-color":
            self.set_cartridge_very_low_action_color(settings_value[1])
            self.click_device_specific_policy_create_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def modify_copier_settings_in_device_specific_policy_settings(self, setting_card=None, settings_value=None):
        # Copier Category
            # Copier Category Settings: Copy Paper Tray Selection, Copy Darkness, Copy Sharpness, Copy Optimize Text or Picture, Copy Background Cleanup, Copy Contrast
        self.click_device_specific_policy_settings_card(setting_card)
        self.click_ignore_unsupported_item_toggle()
        if setting_card == "copy-tray":        
            self.click_copy_tray_paper_option_selection_dropdown()
            if settings_value == "tray-2":
                self.select_copy_tray_paper_select_action_dropdown_option("tray-1")
            elif settings_value == "tray-1":
                self.select_copy_tray_paper_select_action_dropdown_option("manual")
            else:
                self.select_copy_tray_paper_select_action_dropdown_option("auto")
            self.click_device_specific_policy_create_button()
        elif setting_card == "copy-darkness":
            self.click_copy_darkness_option_selection_dropdown()
            if settings_value == 1:
                self.select_copy_darkness_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_darkness_select_action_dropdown_option(3)
            else:
                self.select_copy_darkness_select_action_dropdown_option(1)
            self.click_device_specific_policy_create_button()
        elif setting_card == "copy-sharpness":
            self.click_copy_sharpness_option_selection_dropdown()
            if settings_value == 1:
                self.select_copy_sharpness_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_sharpness_select_action_dropdown_option(3)
            elif settings_value == 3:
                self.select_copy_sharpness_select_action_dropdown_option(4)
            else:
                self.select_copy_sharpness_select_action_dropdown_option(1)
            self.click_device_specific_policy_create_button()
        elif setting_card == "copy-optimize":
            if settings_value == "photo":
                self.click_copy_optimize_photograph_radio_button()
            elif settings_value == "glossy":
                self.click_copy_optimize_text_radio_button()
            elif settings_value == "text":
                self.click_copy_optimize_mixed_radio_button()
            elif settings_value == "mixed":
                self.click_copy_optimize_printed_picture_radio_button()
            self.click_device_specific_policy_create_button()
        elif setting_card == "copy-bg-cleanup":
            self.click_copy_background_cleanup_policy_contextual_footer_select_action_dropdown()
            if settings_value == 1:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(2)
            elif settings_value == 2:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(3)
            elif settings_value == 3:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(1)
            else:
                self.select_copy_background_cleanup_policy_contextual_footer_select_action_dropdown_option(6)
            self.click_device_specific_policy_create_button()
        elif setting_card == "copy-contrast":
            self.click_copy_contrast_policy_contextual_footer_select_action_dropdown()
            if settings_value == 1:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(2)
            elif settings_value == 2:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(3)
            elif settings_value == 3:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(1)
            else:
                self.select_copy_contrast_policy_contextual_footer_select_action_dropdown_options(6)
            self.click_device_specific_policy_create_button()
        else:
            self.enter_device_property_value(settings_value,setting_card)
            self.click_device_specific_policy_create_button()

    def enter_bootloader_current_password(self,random_password):
        self.driver.send_keys("bootloader_current_password_textbox",random_password)

    def enter_bootloader_new_password(self,random_password):
        self.driver.send_keys("bootloader_new_password_textbox",random_password)

    def enter_bootloader_confirm_password(self, random_password):
        self.driver.send_keys("bootloader_confirm_password_textbox", random_password)

    def click_edit_setting_popup_save_button(self):
        self.driver.click("edit_setting_popup_save_button")

    def verify_pjl_password_configuration_update_in_properties_tab(self):
        for _ in range(5):
            if self.get_device_details_device_property_value("pjl-password") == "Configured":
                return True
            else:
                sleep(5)
                self.click_refresh_button()
                self.click_security_accordion()
                self.click_device_details_device_property_card("pjl-password")
        raise AssertionError("PJL Password Configuration is not updated in properties tab")

    def updating_security_accordion_snmpv1v2_widget(self):
        self.click_refresh_button()
        self.click_security_accordion()
        self.click_device_details_device_property_card("snmp-v1-v2")
    
    def verify_snmp_v1v2_read_only_update_status_in_properties_tab(self):
        for _ in range(5):
            if self.get_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read Only Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv1v2_widget()
        raise AssertionError("SNMP V1/V2 Read Only Access is not updated in properties tab")

    def verify_snmp_v1v2_read_and_write_update_status_in_properties_tab(self):
        for _ in range(5):
            if self.get_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read and Write Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv1v2_widget()
        raise AssertionError("SNMP V1/V2 Read Write Access is not updated in properties tab")

    def updating_security_accordion_snmpv3_widget(self):
        self.click_refresh_button()
        self.click_security_accordion()
        self.click_device_details_device_property_card("snmp-v3")

    def verify_snmp_v3_enabled_status_in_properties_tab(self):
        for _ in range(5):
            if self.get_device_details_device_property_value("snmp-v3-enabled") == "Enabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv3_widget()
        raise AssertionError("SNMP V3 Enabled status is not updated in properties tab")

    def verify_snmp_v3_disabled_status_in_properties_tab(self):
        for _ in range(5):
            if self.get_device_details_device_property_value("snmp-v3-enabled") == "Disabled":
                return True
            else:
                sleep(5)
                self.updating_security_accordion_snmpv3_widget()
        raise AssertionError("SNMP V3 Disabled status is not updated in properties tab")

    def remove_settings_in_device_specific_policy_tab(self, setting_name):
        self.click_device_details_policy_tab()
        self.click_device_details_policy_widget_expand_button()
        self.click_device_specific_policy_edit_button()
        self.search_policy_settings(setting_name)
        self.click_device_specific_policy_checkbox()
        self.click_device_specific_policy_next_button()
        self.click_device_specific_policy_remove_button()
        self.check_toast_successful_msg("Device-Specific Policy has been removed.")