from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from SAF.decorator.saf_decorator import string_validation
from time import sleep
import logging


class UnexpectedItemPresentException(Exception):
    pass

class DeviceSearchException(Exception):
    pass

class PrinterSearchException(Exception):
    pass

class Solutions(SMBFlow):
    flow_name = "solutions"
    solutions_learn_more_hp_plus_page_url = "https://www.hp.com/us-en/printers/hp-plus.html"

 ############################ Solutions Screen Page  ############################   

    @string_validation("solutions_overview_title")
    def verify_solutions_title(self):
        return self.driver.wait_for_object("solutions_overview_title",timeout=30)

    @string_validation("solutions_overview_description")
    def verify_solutions_description(self):
        return self.driver.wait_for_object("solutions_overview_description")

    @string_validation("solutions_hpPlus_name")
    def verify_solutions_hp_plus_title(self):
        return self.driver.wait_for_object("solutions_hpPlus_name")
        
    def verify_solutions_hp_plus_status(self):
        return self.driver.wait_for_object("solutions_hp_plus_status_label")

    def verify_solutions_hp_plus_description(self):
        return self.driver.wait_for_object("solutions_hp_plus_description").text.split(".")[0]

    def verify_solutions_printers_status_activated_text(self):
        return self.driver.wait_for_object("solutions_printers_activated_label")

    def get_solutions_printers_activated_count(self):
        return int((self.driver.wait_for_object("solutions_printers_activated_label").text).split(" ")[0])

    @string_validation("solutions_hpPlus_action")
    def verify_solutions_learn_more_about_hp_plus_link(self):
        return self.driver.wait_for_object("solutions_hpPlus_action",timeout=20)

    @string_validation("solutions_smartSecurity_title")
    def verify_solutions_smart_security_title(self):
        return self.driver.wait_for_object("solutions_smartSecurity_title")

    @string_validation("solutions_smartSecurity_description")
    def verify_solutions_smart_security_description(self):
        return self.driver.wait_for_object("solutions_smartSecurity_description")

    def verify_solutions_smart_security_button(self):
        return self.driver.wait_for_object("solutions_smart_security_button")

    @string_validation("solutions_printAnywhere_title")
    def verify_solutions_print_anywhere_title(self):
        return self.driver.wait_for_object("solutions_printAnywhere_title")

    @string_validation("solutions_printAnywhere_description")
    def verify_solutions_print_anywhere_description(self):
        return self.driver.wait_for_object("solutions_printAnywhere_description")

    def verify_solutions_print_anywhere_button(self):
        return self.driver.wait_for_object("solutions_print_anywhere_button")

    @string_validation("solutions_forestFirst_title")
    def verify_solutions_sustainability_forest_first_title(self):
        return self.driver.wait_for_object("solutions_forestFirst_title")

    @string_validation("solutions_forestFirst_description")
    def verify_solutions_sustainability_forest_first_description(self):
        return self.driver.wait_for_object("solutions_forestFirst_description")

    def verify_solutions_sustainability_forest_first_button(self):
        return self.driver.wait_for_object("solutions_sustainability_forest_first_button")

    @string_validation("solutions_hpSmartPro_name")
    def verify_solutions_hp_smart_pro_title(self):
        return self.driver.wait_for_object("solutions_hpSmartPro_name")
    
    def verify_solutions_hp_smart_pro_is_displayed(self,displayed=True):
        return self.driver.wait_for_object("solutions_hpSmartPro_name", timeout=40, invisible=not displayed, raise_e=False)

    def verify_solutions_hp_smart_pro_status(self):
        return self.driver.verify_object_string("solutions_hp_smart_pro_status_label")

    def verify_solutions_hp_smart_pro_status(self):
        return self.driver.wait_for_object("solutions_hp_smart_pro_status_label")

    def verify_solutions_hp_smart_pro_description(self):
        return self.driver.wait_for_object("solutions_hp_smart_pro_description").text.split(".")[0]

    @string_validation("solutions_hpSmartPro_action")
    def verify_solutions_discover_all_features_link(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("solutions_hpSmartPro_action", timeout=20))

    @string_validation("solutions_scanPro_title")
    def verify_solutions_scan_destinations_title(self):
        return self.driver.wait_for_object("solutions_scanPro_title")

    @string_validation("solutions_scanPro_description")
    def verify_solutions_scan_destinations_description(self):
        return self.driver.wait_for_object("solutions_scanPro_description")

    @string_validation("solutions_advScan_title")
    def verify_solutions_advanced_scan_title(self):
        return self.driver.wait_for_object("solutions_advScan_title")

    @string_validation("solutions_advScan_description")
    def verify_solutions_advanced_scan_description(self):
        return self.driver.wait_for_object("solutions_advScan_description")

    def click_solutions_learn_more_about_hp_link(self):
        return self.driver.click("solutions_hpPlus_action",timeout=20)

    def click_solutions_smart_security_button(self):
        return self.driver.click("solutions_smart_security_button",timeout=30)

    def click_solutions_print_anywhere_button(self):
        return self.driver.click("solutions_print_anywhere_button",timeout=30)

    def click_solutions_sustainability_forest_first_button(self):
        return self.driver.click("solutions_sustainability_forest_first_button",timeout=20)

    def click_solutions_discover_all_features_link(self):
        return self.driver.click("solutions_hpSmartPro_action",timeout=20)

############################ Discover All Feature Screen Page  ############################  

    def verify_solutions_discover_all_hp_smart_pro_page_title(self):
        return self.driver.wait_for_object("solution_discover_all_hp_smart_pro_title",timeout=20)

############################ Learn More Screen Page  ############################  

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    def verify_solutions_learn_more_hp_plus_page_title(self):
        return self.driver.wait_for_object("smart_pro_hp_plus_page")
    
    def verify_solutions_learn_more_hp_plus_page_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.solutions_learn_more_hp_plus_page_url

############################ Common Functions ###################################

    def smart_security_search_printers(self, printer_info, raise_e=True, timeout=10):
    
        self.driver.wait_for_object("smart_security_search_box",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("smart_security_search_box", printer_info, press_enter=True)
        
        if self.driver.find_object("table_entry_noitemsfound_warning_message",raise_e=False) is not False:
            table_entry_printers=self.driver.find_object("table_entry_noitemsfound_warning_message")
            logging.info(table_entry_printers.text)
            return False
        else:
            table_entry_printers = self.driver.find_object("table_entry_printer_name",multiple=True)
            for i in range(len(table_entry_printers)):
                if printer_info in table_entry_printers[i].text:
                    logging.info("Printer Name: " + table_entry_printers[i].text+ " contains the searched string: " + printer_info)
                    continue
                else:
                    raise PrinterSearchException("Printer Name: " + table_entry_printers[i].text+ " does not contain the searched string: " + printer_info)
        return True


    def verify_smart_security_page_load(self, table_load=True):
        #This object make sure the table is loaded
        #Doesn't work if no entries are found
        if table_load:
            return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=20)
        else:
            return self.driver.wait_for_object("table_entry_load", timeout=20)

    def click_search_clear_button(self):
        return self.driver.click("search_clear_btn")

############################ Smart Security Screen Page  ###################################

    def verify_smart_security_title(self):
        return self.driver.verify_object_string("smart_security_header",timeout=30)

    def verify_smart_security_description(self):
        return self.driver.verify_object_string("smart_security_description")

    def verify_smart_security_refresh_button(self):
        return self.driver.wait_for_object("smart_security_refresh_button")

    def verify_smart_security_last_refresh_date_time(self):
        return self.driver.wait_for_object("smart_security_refresh_date")

    def get_smart_security_last_refresh_date_time(self): 
        return self.driver.wait_for_object("smart_security_refresh_date").text

    def verify_smart_security_search_textbox(self):
        return self.driver.wait_for_object("smart_security_search_box")

    def click_smart_security_refresh_button(self):
        return self.driver.click("smart_security_refresh_button")
    
    def verify_smart_security_table_empty(self):
        return self.driver.verify_object_string("table_empty")

    def get_smart_security_pagination_count(self): 
        return int((self.driver.wait_for_object("smart_securit_pagination_count", timeout=30).text).split(" ")[1])

    def verify_smart_security_table_headers(self):
        smart_security_table_headers = []
        headers = self.driver.find_object("smart_security_table_headers", multiple = True)
        for header in headers:
            smart_security_table_headers.append(header.text)
        return smart_security_table_headers

    def get_printers_count(self,timeout=20):
        if self.driver.find_object("printer_table_empty",raise_e=False):
            printers_count = 0
            return printers_count
        else:
            printers_count= int((self.driver.wait_for_object("printer_total_count").text).split(" ")[1])
            return printers_count

############################ Print Anywhere Screen Page  ###################################

    def verify_print_anywhere_page_table_loads(self, table_load=True):
        #This object make sure the table is loaded
        #Doesn't work if no entries are found
        #sleep added, as the table takes longer time to load 
        sleep(10)
        if table_load:
            return self.driver.wait_for_object("print_anywhere_table_entry", timeout=30, displayed=False)
        else:
            return self.driver.wait_for_object("printer_table_empty", timeout=30)

    def verify_print_anywhere_title(self):
        return self.driver.verify_object_string("print_anywhere_header",timeout=30)
    
    def verify_print_anywhere_tab_title(self):
        return self.driver.verify_object_string("print_anywhere_tab",timeout=30)

    def verify_print_anywhere_description(self):
        return self.driver.verify_object_string("print_anywhere_description")

    def verify_print_anywhere_detail_description(self):
        return self.driver.verify_object_string("print_anywhere_detail_description")

    def verify_print_anywhere_refresh_button(self):
        return self.driver.wait_for_object("print_anywhere_refresh_button")

    def verify_print_anywhere_last_refresh_date_time(self):
        return self.driver.wait_for_object("print_anywhere_refresh_date")

    def get_print_anywhere_last_refresh_date_time(self): 
        return self.driver.wait_for_object("print_anywhere_refresh_date").text

    def verify_print_anywhere_search_textbox(self):
        return self.driver.wait_for_object("print_anywhere_search_box")

    def verify_print_any_where_table_first_entry(self):
        return self.driver.wait_for_object("print_anywhere_table_entry")

    def verify_print_anywhere_table_headers(self):
        print_anywhere_table_headers = []
        headers = self.driver.find_object("print_anywhere_table_headers", multiple=True)
        for header in headers:
            header_text = header.text.strip()
        
            if 'ascending sorted' in header_text:
                header_text = header_text.replace('ascending sorted', '').strip()
            if header_text != '':
                print_anywhere_table_headers.append(header_text)
        return print_anywhere_table_headers
    
    def click_print_anywhere_refresh_button(self):
        return self.driver.click("print_anywhere_refresh_button",timeout=5)

    def get_solutions_print_anywhere_toggle_button_status(self):
        toggle_status = self.driver.get_attribute("print_anywhere_toggle_button_status","aria-checked")
        return toggle_status
    
    def get_solutions_private_pickup_toggle_button_status(self):
        toggle_status = self.driver.get_attribute("private_pickup_toggle_button_status","aria-checked")
        return toggle_status

############################ Smart Security Detail Screen  ###################################    
    def click_printer_first_entry_link(self):
        return self.driver.click("smart_security_first_entry_link",timeout=20)

    def verify_smart_security_detail_screen_printer_name(self):
        return self.driver.wait_for_object("smart_security_printer_detail_name",timeout=30)

    def verify_smart_security_detail_screen_printer_model(self):
        return self.driver.wait_for_object("smart_security_printer_detail_model")

    def verify_smart_security_detail_screen_printer_location(self):
        return self.driver.wait_for_object("smart_security_printer_detail_location")

    def verify_smart_security_detail_screen_printer_connectivity(self):
        return self.driver.wait_for_object("smart_security_printer_detail_connectivity",timeout=30)

    def verify_smart_security_detail_screen_printer_security_status(self):
        return self.driver.wait_for_object("smart_security_printer_detail_security_status")

    def verify_smart_security_detail_screen_printer_detail_link(self):
        return self.driver.wait_for_object("smart_security_printer_detail_link")

    def get_printer_info_in_smart_scurity_table_view(self):
        printer_info_table = {}
        connected = "connected"
        connectivity_column = self.get_header_index("connectivity")
        printername_column = self.get_header_index("device_name")
        connectivity_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[connectivity_column],multiple=True)
        printername_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[printername_column],multiple=True)
        for index in range(len(connectivity_list)):
            logging.info(str(connectivity_list[index].text.lower()))
            if connected == connectivity_list[index].text.lower():
                entry = self.get_total_table_entries(total_len=False)[index]
                all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
                printer_info_table["printer_name"] =  all_fields[0].text.split("\n")[0].lower()
                printer_info_table["printer_model"] =  all_fields[0].text.split("\n")[1].lower()
                printer_info_table["printer_connectivity"] =  all_fields[2].text.lower()
                printer_info_table["printer_security_status"] =  all_fields[3].text.lower()
                printername_list[index].click()
                return printer_info_table
            else:
                continue
        raise DeviceSearchException("Cannot find any connected printer")

    def get_printer_info_in_smart_scurity_detail_screen(self):
        printer_details = {}
        printer_details["printer_name"] = self.driver.wait_for_object("smart_security_printer_detail_name",timeout=20).text.lower()
        printer_details["printer_model"] = self.driver.wait_for_object("smart_security_printer_detail_model").text.lower()
        printer_details["printer_connectivity"] = self.driver.wait_for_object("smart_security_printer_detail_connectivity").text.lower()
        printer_details["printer_security_status"] = self.driver.wait_for_object("smart_security_printer_detail_security_status").text.lower()
        return printer_details

    def click_smart_security_detail_screen_printer_detail_link(self):
        return self.driver.click("smart_security_printer_detail_link",timeout=20)

    def verify_smart_security_detail_screen_refresh_button(self):
        return self.driver.wait_for_object("smart_security_detail_refresh_button")

    def click_smart_security_detail_screen_refresh_button(self):
        return self.driver.click("smart_security_detail_refresh_button")

    def verify_smart_security_detail_screen_refresh_text(self):
        return self.driver.wait_for_object("smart_security_detail_refresh_label")

    def verify_security_monitoring_toggle_button(self):
        return self.driver.wait_for_object("smart_security_toggle_button")

    def click_security_monitoring_toggle_button(self):
        return self.driver.click("smart_security_toggle_button",timeout=25)

    def verify_security_monitoring_title(self):
        return self.driver.wait_for_object("smart_security_monitor_title")

    def verify_security_monitoring_status(self):
        return self.driver.wait_for_object("smart_security_monitor_status")

    def get_security_monitoring_status(self):
        return self.driver.wait_for_object("smart_security_monitor_status").text

    def get_security_monitoring_toggle_status(self):
        self.driver.wait_for_object("smart_security_toggle_status", timeout=30)
        return self.driver.get_attribute("smart_security_toggle_status","aria-checked")
    
    def get_security_monitoring_toggle_status_message(self):
        return self.driver.wait_for_object("smart_security_monitoring_toggle_status_message", timeout=80).text

    def get_security_monitoring_desc(self):
        return self.driver.wait_for_object("smart_security_monitor_desc").text

    def verify_security_monitoring_popup_title(self):
        return self.driver.verify_object_string("security_monitor_popup_title")
    
    def verify_security_monitoring_popup_desc(self):
        self.driver.verify_object_string("security_monitor_popup_desc")
        return self.driver.verify_object_string("security_monitor_popup_descb")

    def verify_security_monitoring_popup_cancel_button(self):
        return self.driver.verify_object_string("security_monitor_cancel_btn")

    def verify_security_monitoring_popup_turnoff_button(self):
        return self.driver.verify_object_string("security_monitor_turnoff_btn")

    def click_security_monitoring_popup_cancel_button(self):
        return self.driver.click("security_monitor_cancel_btn")

    def click_security_monitoring_popup_turnoff_button(self):
        return self.driver.click("security_monitor_turnoff_btn",timeout=25)

    def verify_security_settings_title(self):
        return self.driver.verify_object_string("smart_security_setting_title", timeout =50)

    def verify_security_settings_desc(self):
        return self.driver.verify_object_string("smart_security_setting_desc", timeout=30)
        
    def verify_admin_password_title(self):
        return self.driver.verify_object_string("smart_security_admin_pswd", timeout=40)

    def verify_admin_password_tool_tip(self):
        return self.driver.wait_for_object("smart_security_admin_pswd_accordion_btn")
    
    def click_admin_password_tool_tip(self):
        return self.driver.click("smart_security_admin_pswd_accordion_btn")

    def verify_admin_password_pop_up_title(self):
        return self.driver.verify_object_string("smart_security_admin_pswd_popup_title",timeout=10)

    def verify_admin_password_pop_up_desc(self):
        self.driver.verify_object_string("smart_security_admin_pswd_popup_desca")
        return self.driver.verify_object_string("smart_security_admin_pswd_popup_descb")

    def verify_admin_password_pop_up_close_button(self):
        return self.driver.wait_for_object("smart_security_popup_close")

    def click_admin_password_pop_up_close_button(self):
        return self.driver.click("smart_security_popup_close")

    def verify_admin_password_expand_button(self):
        return self.driver.wait_for_object("smart_security_admin_pswd_expand_button")

    def click_admin_password_expand_button(self):
        return self.driver.click("smart_security_admin_pswd_expand_button")

    def verify_admin_password_status_desc(self):
        return self.driver.verify_object_string("smart_security_admin_pswd_status_desc")

    def verify_automatic_firmware_update_title(self):
        return self.driver.verify_object_string("smart_security_firmware")

    def verify_automatic_firmware_update_tool_tip(self):
        return self.driver.wait_for_object("smart_security_firmware_accordion_btn")
    
    def click_automatic_firmware_update_tool_tip(self):
        return self.driver.click("smart_security_firmware_accordion_btn")

    def verify_automatic_firmware_update_pop_up_title(self):
        expected_text = "Automatic firmware updates"
        self.driver.wait_for_object("smart_security_firmware_popup_title")
        actual_text = self.driver.get_text("smart_security_firmware_popup_title")
        return self.compare_strings(expected_text, actual_text)

    def verify_automatic_firmware_update_pop_up_desc(self):
        self.driver.verify_object_string("smart_security_firmware_popup_desca")
        return self.driver.verify_object_string("smart_security_firmware_popup_descb")

    def verify_automatic_firmware_update_pop_up_close_button(self):
        return self.driver.wait_for_object("smart_security_firmware_popup_close")

    def click_automatic_firmware_update_pop_up_close_button(self):
        return self.driver.click("smart_security_firmware_popup_close")

    def verify_automatic_firmware_update_expand_button(self):
        return self.driver.wait_for_object("smart_security_firmware_expand_button")

    def click_automatic_firmware_update_expand_button(self):
        return self.driver.click("smart_security_firmware_expand_button")

    def verify_automatic_firmware_update_toggle_button(self):
        return self.driver.wait_for_object("smart_security_firmware_toggle_btn",timeout=10)

    def click_automatic_firmware_update_toggle_button(self):
        return self.driver.click("smart_security_firmware_toggle_btn")

    def verify_automatic_firmware_update_status_desc(self):
        return self.driver.verify_object_string("smart_security_firmware_status_desc")

    def verify_snmp_title(self):
        return self.driver.verify_object_string("smart_security_snmp")

    def verify_snmp_tool_tip(self):
        return self.driver.wait_for_object("smart_security_snmp_accordion_btn")
    
    def click_snmp_tool_tip(self):
        return self.driver.click("smart_security_snmp_accordion_btn")

    def verify_snmp_v3_tool_tip(self):
        return self.driver.wait_for_object("smart_security_snmp_v3_accordion_btn")

    def click_snmp_v3_tool_tip(self):
        return self.driver.click("smart_security_snmp_v3_accordion_btn")

    def verify_snmp_v3_pop_up_desc(self):
        self.driver.verify_object_string("smart_security_snmp_v3_popup_desca")
        return self.driver.verify_object_string("smart_security_snmp_v3_popup_descb")

    def verify_snmp_v3_pop_up_close_button(self):
        return self.driver.wait_for_object("smart_security_snmp_v3_popup_close")

    def click_snmp_v3_pop_up_close_button(self):
        return self.driver.js_click("smart_security_snmp_v3_popup_close")

    def verify_snmp_v3_expand_button(self):
        return self.driver.wait_for_object("smart_security_snmp_v3_expand_button")

    def click_snmp_v3_expand_button(self):
        return self.driver.click("smart_security_snmp_v3_expand_button")

    def verify_snmp_pop_up_title(self):
        return self.driver.verify_object_string("smart_security_snmp_popup_title")

    def verify_snmp_pop_up_desc(self):
        self.driver.verify_object_string("smart_security_snmp_popup_desca")
        return self.driver.verify_object_string("smart_security_snmp_popup_descb")

    def verify_snmp_pop_up_close_button(self):
        return self.driver.wait_for_object("smart_security_snmp_popup_close")

    def click_snmp_pop_up_close_button(self):
        return self.driver.click("smart_security_snmp_popup_close")

    def verify_snmp_expand_button(self):
        return self.driver.wait_for_object("smart_security_snmp_expand_button")

    def click_snmp_expand_button(self):
        return self.driver.click("smart_security_snmp_expand_button")

    def verify_snmp_toggle_button(self):
        return self.driver.wait_for_object("smart_security_snmp_toggle_btn")

    def click_snmp_toggle_button(self):
        return self.driver.click("smart_security_snmp_toggle_btn")

    def verify_snmp_status_desc(self):
        return self.driver.verify_object_string("smart_security_snmp_status_desc")

    def click_printer_details_link(self):
        return self.driver.click("printer_details_link")

    def verify_snmp_v3_label(self):
        return self.driver.verify_object_string("snmp_v3_label")

    def verify_snmp_v1_v2_label(self):
        return self.driver.verify_object_string("snmp_v1_v2_label")

    def get_snmp_v1_v2_toggle_status(self):
        return self.driver.get_attribute("snmp_v1_v2_toggle_status","aria-checked")

    def get_snmp_v3_toggle_status(self):
        return self.driver.get_attribute("snmp_v3_toggle_status","aria-checked")

    def verify_snmp_v3_toggle_turned_on_warning_label(self):
        return self.driver.verify_object_string("snmp_v3_toggle_turned_on_warning_label",timeout=90)

    def verify_snmp_v3_toggle_turned_on_warning_desc(self):
        return self.driver.verify_object_string("snmp_v3_toggle_turned_on_warning_desc")

    def click_snmp_v3_toggle_button(self):
        return self.driver.click("snmp_v3_toggle_status")

    def verify_snmp_v1_v2_toggle_turned_on_warning_label(self):
        return self.driver.verify_object_string("snmp_v1_v2_toggle_turned_on_warning_label",timeout=90)

    def verify_snmp_v1_v2_toggle_turned_on_warning_desc(self):
        return self.driver.verify_object_string("snmp_v1_v2_toggle_turned_on_warning_desc")

    def click_snmp_v1_v2_expand_button(self):
        return self.driver.click("smart_security_snmp_expand_button")

    def click_snmp_v1_v2_toggle_button(self):
        return self.driver.click("snmp_v1_v2_toggle_status")

    def verify_snmp_v3_user_name_label(self):
        return self.driver.verify_object_string("snmp_v3_user_name_label")

    def verify_snmp_v3_user_name_text_box(self):
        return self.driver.wait_for_object("snmp_v3_user_name_text_box")

    def verify_snmp_v3_authentication_passphrase_label(self):
        return self.driver.verify_object_string("snmp_v3_authentication_passphrase_label")

    def verify_snmp_v3_authentication_passphrase_set_passphrase_text_box(self):
        return self.driver.wait_for_object("snmp_v3_authentication_passphrase_set_passphrase_text_box")

    def verify_snmp_v3_authentication_passphrase_confirm_passphrase_text_box(self):
        return self.driver.wait_for_object("snmp_v3_authentication_passphrase_confirm_passphrase_text_box")

    def verify_snmp_v3_privacy_passphrase_label(self):
        return self.driver.verify_object_string("snmp_v3_privacy_passphrase_label")

    def verify_snmp_v3_privacy_passphrase_set_passphrase_text_box(self):
        return self.driver.wait_for_object("snmp_v3_privacy_passphrase_set_passphrase_text_box")

    def verify_snmp_v3_privacy_passphrase_confirm_passphrase_text_box(self):
        return self.driver.wait_for_object("snmp_v3_privacy_passphrase_confirm_passphrase_text_box")

    def verify_snmp_v3_save_button_status(self,status):
        save_button=self.driver.wait_for_object("snmp_v3_save_button_status")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True

    def verify_snmp_v3_user_name_text_box_with_passing_single_text(self, username):
        return self.driver.send_keys("snmp_v3_user_name_text_box_with_passing_single_text",username)

    def verify_snmp_v3_user_name_text_box_with_single_text_error_message(self):
        return self.driver.verify_object_string("snmp_v3_user_name_text_box_with_single_text_error_message")

    def verify_snmp_v3_user_name_text_box_with_single_text_error_message_status(self,displayed=True):
        self.driver.wait_for_object("snmp_v3_user_name_text_box_with_single_text_error_message",invisible=not displayed)

    def verify_snmp_v3_Authentication_set_passphrase_with_passing_single_text(self, setpass):
        return self.driver.send_keys("snmp_v3_Authentication_set_passphrase_with_passing_single_text", setpass)

    def verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message(self):
        return self.driver.verify_object_string("snmp_v3_Authentication_set_passphrase_with_single_text_error_message")

    def verify_snmp_v3_Authentication_set_passphrase_with_single_text_error_message_status(self,displayed=True):
        return self.driver.wait_for_object("snmp_v3_Authentication_set_passphrase_with_single_text_error_message",invisible=not displayed)

    def verify_snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text(self, confirmpass):
        return self.driver.send_keys("snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text",confirmpass)

    def verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message(self):
        return self.driver.verify_object_string("snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message")

    def verify_snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message_status(self,displayed=True):
        return self.driver.wait_for_object("snmp_v3_Authentication_confirm_passphrase_with_single_text_error_message",invisible=not displayed)

    def verify_snmp_v3_privacy_set_passphrase_with_passing_single_text(self, setpass):
        return self.driver.send_keys("snmp_v3_privacy_set_passphrase_with_passing_single_text", setpass)

    def verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message(self):
        return self.driver.verify_object_string("snmp_v3_privacy_set_passphrase_with_single_text_error_message")

    def verify_snmp_v3_privacy_set_passphrase_with_single_text_error_message_status(self,displayed=True):
        return self.driver.wait_for_object("snmp_v3_privacy_set_passphrase_with_single_text_error_message",invisible=not displayed)

    def verify_snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text(self, confirmpass):
        return self.driver.send_keys("snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text", confirmpass)

    def verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message(self):
        return self.driver.verify_object_string("snmp_v3_privacy_confirm_passphrase_with_single_text_error_message")

    def verify_snmp_v3_privacy_confirm_passphrase_with_single_text_error_message_status(self,displayed=True):
        return self.driver.wait_for_object("snmp_v3_privacy_confirm_passphrase_with_single_text_error_message",invisible=not displayed)

    def verify_snmp_v3_user_name_text_box_with_passing_valid_text(self, valid_username):
        return self.driver.send_keys("snmp_v3_user_name_text_box_with_passing_single_text", valid_username)

    def verify_snmp_v3_Authentication_set_passphrase_with_passing_valid_text(self, setpass):
        return self.driver.send_keys("snmp_v3_Authentication_set_passphrase_with_passing_single_text", setpass)

    def verify_snmp_v3_Authentication_confirm_passphrase_with_passing_valid_text(self, confirmpass):
        return self.driver.send_keys("snmp_v3_Authentication_confirm_passphrase_with_passing_wrong_single_text", confirmpass)

    def verify_snmp_v3_privacy_set_passphrase_with_passing_valid_text(self, setpass):
        return self.driver.send_keys("snmp_v3_privacy_set_passphrase_with_passing_single_text", setpass)

    def verify_snmp_v3_privacy_confirm_passphrase_with_passing_valid_text(self, confirmpass):
        return self.driver.send_keys("snmp_v3_privacy_confirm_passphrase_with_passing_wrong_single_text", confirmpass)
    
    def get_printer_status(self):
        return self.driver.wait_for_object("smart_security_printer_status").text

    def verify_security_monitoring_field_text(self):
        return self.driver.verify_object_string("security_monitoring_field_text")

    def verify_unable_to_load_error_message(self):
        return self.driver.verify_object_string("unable_to_load_error_message")

    def verify_try_again_hyperlink(self):
        return self.driver.verify_object_string("try_again_hyperlink")

    def click_smart_security_detail_screen_printer_details_hyperlink(self):
        return self.driver.click("security_detail_screen_printer_details_hyperlink")

    def verify_printer_details_overview_label(self):
        return self.driver.verify_object_string("printer_details_overview_label")

    def verify_smart_security_printer_details_screen_unsaved_changes_popup_label(self):
        return self.driver.verify_object_string("smart_security_printer_details_screen_unsaved_changes_popup_label")

    def verify_smart_security_printer_details_screen_unsaved_changes_popup_description(self):
        return self.driver.verify_object_string("smart_security_printer_details_screen_unsaved_changes_popup_description")

    def verify_smart_security_printer_details_screen_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("smart_security_printer_details_screen_unsaved_changes_popup_cancel_button")

    def verify_smart_security_printer_details_screen_unsaved_changes_leave_button(self):
        return self.driver.wait_for_object("smart_security_printer_details_screen_unsaved_changes_leave_button")

    def click_smart_security_printer_details_screen_unsaved_changes_leave_button(self):
        return self.driver.click("smart_security_printer_details_screen_unsaved_changes_leave_button")

    def verify_and_click_connected_printer(self):
        self.select_page_size_new("100")
        connected = "connected"
        connectivity_column = self.get_header_index("connectivity")
        printername_column = self.get_header_index("device_name")
        connectivity_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[connectivity_column],multiple=True)
        printername_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[printername_column],multiple=True)
        for index in range(len(connectivity_list)):
            logging.info(str(connectivity_list[index].text.lower()))
            if connected == connectivity_list[index].text.lower():
                logging.info(str(printername_list[index].text))
                return printername_list[index].click()
            else:
                continue
        raise DeviceSearchException("Cannot find any connected printer")