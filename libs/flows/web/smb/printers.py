from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from time import sleep
import logging

class PrinterSearchException(Exception):
    pass

class DeviceSearchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class Printers(SMBFlow):
    flow_name = "printers"
    hpinstantink_learn_more_newtab_url = "https://instantink-pie1.hpconnectedpie.com/us/en/l/v2/business"
    printer_order_supplies_newtab_url = "https://www.hp.com/us-en/shop/cat/ink--toner---paper"
  
 ############################ Printer Page ###################################################
        
    def verify_printers_tab_page(self, timeout=15, raise_e=True):
        return self.driver.wait_for_object("printers_page", raise_e=raise_e, timeout=timeout)

    def verify_printer_details_section(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("printers_details_section", raise_e=raise_e, timeout=timeout)
    
    def verify_printers_page_title(self,timeout=40):
        return self.driver.verify_object_string("printer_table_title",timeout=timeout)
 
    def verify_printers_page_desc(self):
        return self.driver.verify_object_string("printer_desc")

    def verify_printer_status(self):
        self.driver.wait_for_object("printer_status", timeout=30)
    
    def verify_no_printer_added_message(self, timeout=30):
        self.driver.wait_for_object("no_printer_added_message", timeout=timeout)
    
    def get_printers_page_title(self):
        return self.driver.get_text("printer_table_title")
 
    def get_printers_page_desc(self):
        return self.driver.get_text("printer_desc")

    def verify_printer_table_empty_text(self):
        return self.driver.verify_object_string("printer_table_empty_text")

    def verify_printer_table_refresh_button(self):
        return self.driver.wait_for_object("printers_refresh_button",timeout=20)

    def verify_printer_table_last_updated_date_time(self):
        return self.driver.wait_for_object("printer_last_updated_date_time",timeout=30)

    def verify_printer_table_search_box(self):
        return self.driver.wait_for_object("search_printer_inputbox")

    def verify_printer_table_view_button(self):
        return self.driver.wait_for_object("printer_table_view_toggle_button")

    def verify_printer_card_view_button(self):
        return self.driver.wait_for_object("printer_card_toggle_button")

    def get_printer_table_first_entry_printer_name(self):
        return self.driver.get_text("table_first_entry_printer_name")
    
    def click_printer_card_view_button(self):
        return self.driver.click("printer_card_toggle_button",timeout=20)

    def click_printer_table_view_button(self):
        return self.driver.click("printer_table_view_toggle_button",timeout=20)

    def click_search_clear_button(self):
        return self.driver.js_click("search_clear_btn")

    def verify_printers_page(self, table_load=True):
        #This object make sure the table is loaded
        #If table is loaded, it verifies the table view landing
        #else verifies the card view landing of printers page
        
        if table_load:
            return self.driver.wait_for_object("printer_table", timeout=40)
        else:
            return self.driver.wait_for_object("printer_card_table", timeout=40)

    def get_printers_count(self,timeout=30):
        if self.driver.find_object("printer_table_empty",raise_e=False):
            printers_count = 0
            return printers_count
        else:
            printers_count= int((self.driver.wait_for_object("printer_total_count").text).split(" ")[1])
            return printers_count

    def search_printers(self, printer_info, raise_e=True, timeout=10):
    
        self.driver.wait_for_object("search_printer_inputbox",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("search_printer_inputbox", printer_info, slow_type=True)
        
        if self.driver.find_object("table_entry_noitemsfound_warning_message",raise_e=False) is not False:
            table_entry_printers=self.driver.find_object("table_entry_noitemsfound_warning_message")
            logging.info(table_entry_printers.text)
            return False
        else:
            table_entry_printers = self.driver.find_object("table_entry_printer_name",multiple=True)
            table_entry_printers_model_name = self.driver.find_object("table_view_entry_printer_model_name",multiple=True)
            for i in range(len(table_entry_printers)):
                if printer_info in table_entry_printers[i].text:
                    logging.info("Printer Name: " + table_entry_printers[i].text+ " contains the searched string: " + printer_info)
                    continue
                elif printer_info in table_entry_printers_model_name[i].text:
                    logging.info("Printer Model Name: " + table_entry_printers_model_name[i].text+ " contains the searched string: " + printer_info)
                    continue
                else:
                    raise PrinterSearchException("Printer Name: " + table_entry_printers[i].text+ " does not contain the searched string: " + printer_info)
        return True

    def search_printers_card_view(self, printer_info, raise_e=True, timeout=10):

        self.driver.wait_for_object("search_printer_inputbox",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("search_printer_inputbox", printer_info)
        
        if self.driver.find_object("table_entry_noitemsfound_warning_message",raise_e=False) is not False:
            table_entry_printers=self.driver.find_object("table_entry_noitemsfound_warning_message")
            logging.info(table_entry_printers.text)
            return False
        else:
            table_entry_printers = self.driver.find_object("card_view_entry_printer_name",multiple=True)
            card_entry_printers_model_name = self.driver.find_object("card_view_entry_printer_model_name",multiple=True)
            for i in range(len(table_entry_printers)):
                if printer_info in table_entry_printers[i].text:
                    logging.info("Printer Name: " + table_entry_printers[i].text+ " contains the searched string: " + printer_info)
                    continue
                elif printer_info in card_entry_printers_model_name[i].text:
                    logging.info("Printer Model Name: " + card_entry_printers_model_name[i].text+ " contains the searched string: " + printer_info)
                    continue
                else:
                    raise PrinterSearchException("Printer Name: " + table_entry_printers[i].text+ " does not contain the searched string: " + printer_info)
        return True

    def get_printers_info_in_table_view(self):
        printer_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        printer_info["printer_name"] = ((all_fields[0]).text.lower().split("\n")[0])
        # printer_info["printer_location"] = ((all_fields[1]).text.lower().split("\n")[0])
        printer_info["printer_connectivity"] = (all_fields[2]).text.lower()
        printer_info["printer_device_status"] = (all_fields[3]).text.lower()
        # printer_info["printer_security_status"] = (all_fields[4]).text.lower()
        return printer_info

    def verify_printer_table_headers(self):
        printer_table_headers = []
        headers = self.driver.find_object("printer_table_headers", multiple = True)
        for header in headers:
            printer_table_headers.append(header.text)
        return printer_table_headers
    
    def verify_printer_inline_notification_message(self, timeout=30):
        return self.driver.wait_for_object("printer_inline_notification_message", timeout=timeout)

    ################################### printers Count ####################################################
   
    def get_printers(self):
        # This method returns the online, offline and total printers count 
        connected_printers = 0
        not_connected_printers = 0
        self.driver.wait_for_object("_shared_table_entries",timeout=30)
        self.select_page_size_new("100")
        max_pages=self.get_max_page()
        for page in range(max_pages):
            self.select_page(page+1)
            rows = self.driver.find_object("_shared_table_entries",multiple=True)
            for row in rows:
                s = row.text
                if 'Connected' in s:
                    connected_printers+=1
                if 'Not connected' in s:
                    not_connected_printers+=1
        printers_page_printer_count = {"connected" : connected_printers, "notconnected" : not_connected_printers, "total_count" : connected_printers + not_connected_printers}
        return printers_page_printer_count
    
############################ Printer Card view Page ###########################################
    
    def click_card_view_printer_first_entry(self):
        return self.driver.click("printer_card_details_printer_link",timeout=20)

    def click_card_view_connected_printer_link(self):
        return self.driver.click("printer_card_details_connected_printer_link",timeout=20)

    def verify_printer_card_view_empty_text(self):
        return self.driver.verify_object_string("printer_card_view_empty_text")

    def get_printer_card_view_first_entry_printer_name(self):
        return self.driver.get_text("printer_card_details_printer_name")

    def get_printer_info_in_card_view(self):
        printer_details = {}
        printer_details["printer_name"] = self.driver.wait_for_object("printer_card_details_printer_name",timeout=20).text.lower()
        # printer_details["printer_location"] = self.driver.wait_for_object("printer_card_details_printer_location").text.lower()
        printer_details["printer_connectivity"] = self.driver.wait_for_object("printer_card_details_printer_connectivity").text.lower()
        printer_details["printer_device_status"] = self.driver.wait_for_object("printer_card_details_printer_device_status").text.lower()
        # printer_details["printer_security_status"] = self.driver.wait_for_object("printer_card_details_printer_security_status").text.lower()
        return printer_details

  ############################ Printer Details Page ###########################################

    def verify_printer_details_screen_printer_name(self):
        return self.driver.wait_for_object("printer_details_printer_name",timeout=30)

    def verify_printer_details_last_updated_date_time(self):
        return self.driver.wait_for_object("printer_details_last_updated_date_time")
    
    def get_printer_details_screen_printer_name(self):
        return self.driver.wait_for_object("printer_details_printer_name",timeout=20).text
    
    def get_printer_details_screen_printer_status(self):
        return self.driver.get_text("printer_details_printer_device_status")
    
    def get_printer_details_screen_printer_location(self):
        if self.driver.find_object("printer_details_printer_location",raise_e=False):
            return self.driver.wait_for_object("printer_details_printer_location",timeout=30).text
        else:
            logging.info("Printer location field not available for Printer")

    def get_printer_details_in_printer_details_screen(self):
        printer_details = {}
        printer_details["printer_name"] = self.driver.wait_for_object("printer_details_printer_name",timeout=20).text.lower()
        # printer_details["printer_location"] = self.driver.wait_for_object("printer_details_printer_location").text.lower()
        printer_details["printer_connectivity"] = self.driver.wait_for_object("printer_details_printer_connectivity").text.lower()
        printer_details["printer_device_status"] = self.driver.wait_for_object("printer_details_printer_device_status").text.lower()
        # printer_details["printer_security_status"] = self.driver.wait_for_object("printer_details_printer_security_status").text.lower()
        return printer_details

    def verify_connectivity_status_in_printer_details_screen(self,connectivity_status):
        assert connectivity_status == self.driver.wait_for_object("printer_details_printer_connectivity",timeout=30).text.lower()

    def verify_printer_action_dropdown_options(self):
        self.driver.wait_for_object("printer_action_dropdown_options")
    
    def click_remove_printer_action(self):
        self.driver.click("remove_printer_action")
    
    def click_printer_action_dropdown(self):
        self.driver.wait_for_object("printer_action_dropdown", timeout=30)
        sleep(5)
        return self.driver.click("printer_action_dropdown", timeout=30)

    def get_printer_action_dropdown_options(self,timeout=20):
        actual_options = []
        options = self.driver.find_object("printer_action_dropdown_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options

    def get_printer_details_screen_printer_security_status(self):
        return self.driver.wait_for_object("printer_details_printer_security_status").text

    def get_printer_details_screen_printer_connectivity_status(self):
        return self.driver.wait_for_object("printer_details_printer_connectivity").text

    def select_edit_printer_name_and_location_option(self):
        self.driver.verify_object_string("printer_details_edit_printer_name_dropdown_text")
        return self.driver.click("printer_details_edit_printer_name_dropdown",timeout=30)

    def select_install_hp_software_option(self):
        self.driver.verify_object_string("printer_details_install_hp_software_dropdown_option_text",timeout=30)
        sleep(5)
        return self.driver.click("printer_details_install_hp_software_dropdown_option",timeout=30)

    def select_edit_location_name_option(self):
        self.driver.verify_object_string("printer_details_edit_printer_location_dropdown")
        return self.driver.click("printer_details_edit_printer_location_dropdown",timeout=20)

    def verify_edit_printer_name_and_location_popup(self):
        return self.driver.wait_for_object("printer_details_edit_printer_name_and_location_popup_title",timeout=10)

    def enter_printer_name(self,printer_name):
        self.driver.clear_text("printer_details_edit_printer_name_popup_name")
        return self.driver.send_keys("printer_details_edit_printer_name_popup_name", printer_name)
    
    def enter_location_name(self,location_name):
        self.driver.clear_text("printer_details_edit_printer_name_popup_location")
        return self.driver.send_keys("printer_details_edit_printer_name_popup_location", location_name)
    
    def edit_printer_name_popup_get_printer_name(self):
        return self.driver.get_attribute("printer_details_edit_printer_name_popup_name","value")
    
    def edit_printer_name_popup_get_location_name(self):
        return self.driver.get_attribute("printer_details_edit_printer_name_popup_location","value")
    
    def edit_printer_name_popup_get_printer_location(self):
        return self.driver.get_attribute("printer_details_edit_printer_name_popup_location","value",timeout=20)

    def click_edit_printer_name_and_location_popup_cancel_button(self):
        self.driver.wait_for_object("printer_details_edit_printer_name_popup_cancel_button")
        return self.driver.click("printer_details_edit_printer_name_popup_cancel_button",timeout=20)

    def click_edit_printer_name_and_location_popup_save_button(self):
        self.driver.wait_for_object("printer_details_edit_printer_name_popup_save_button")
        return self.driver.click("printer_details_edit_printer_name_popup_save_button")

    def get_printer_name_change_request_message(self):
        self.driver.wait_for_object("printer_details_name_change_request_message")
        return self.driver.get_text("printer_details_name_change_request_message")
         
    def verify_edit_printer_name_popup_name_change_request_msg(self):
        return self.driver.wait_for_object("edit_printer_name_popup_name_change_request_msg")
    
    def get_edit_printer_name_popup_request_printer_name(self):
        return self.driver.get_text("edit_printer_name_popup_request_printer_name")
    
    def get_edit_printer_location_popup_request_printer_location(self):
        return self.driver.get_text("edit_printer_location_popup_request_printer_location")

    def verify_printer_edit_printer_name_postive_toast_notification_popup(self):
        return self.driver.verify_object_string("printer_details_edit_printer_name_postive_toast")

    def verify_printer_details_screen_estimated_supply_chart(self):
        return self.driver.wait_for_object("printer_estimated_supply_chart", timeout=30)

    def verify_printer_details_screen_printer_model(self):
        return self.driver.wait_for_object("printer_details_printer_model")

    def verify_printer_details_screen_printer_location(self,timeout=20):
        if self.driver.find_object("printer_details_printer_location",raise_e=False):
            logging.info("Printer location field not available for Printer")
        else:
            return self.driver.wait_for_object("printer_details_printer_location")

    def verify_printer_details_screen_printer_connectivity(self):
        return self.driver.wait_for_object("printer_details_printer_connectivity")

    def verify_printer_details_screen_printer_device_status(self):
        return self.driver.wait_for_object("printer_details_printer_device_status")

    def verify_printer_details_screen_printer_security_status(self):
        return self.driver.wait_for_object("printer_details_printer_security_status", timeout=30)

    def verify_printer_details_screen_action_dropdown(self):
        return self.driver.wait_for_object("printer_action_dropdown")
    
    def verify_printer_details_screen_overview_title(self):
        return self.driver.verify_object_string("printer_details_overview_label", timeout=20)

    def verify_printer_details_screen_solutions_title(self):
        return self.driver.verify_object_string("printer_details_solutions_label")

    def verify_printer_details_screen_printer_info_title(self):
        return self.driver.verify_object_string("printer_details_printer_info_label", timeout=20)

    def get_printer_details_in_printer_screen_from_smart_security(self):
        printer_details = {}
        printer_details["printer_name"] = self.driver.wait_for_object("printer_details_printer_name",timeout=20).text.lower()
        printer_details["printer_model"] = self.driver.wait_for_object("printer_details_printer_model").text.lower()
        printer_details["printer_connectivity"] = self.driver.wait_for_object("printer_details_printer_connectivity").text.lower()
        printer_details["printer_security_status"] = self.driver.wait_for_object("printer_details_printer_security_status").text.lower()
        return printer_details

    def verify_printer_details_screen_supplies_level_container(self):
        return self.driver.wait_for_object("printer_details_supplies_level_container", timeout=20)

    def verify_printer_details_screen_supplies_level_container_label(self):
        return self.driver.verify_object_string("printer_details_supplies_level_container_label", timeout=20)

    def verify_printer_details_screen_order_supplies_button(self):
        return self.driver.wait_for_object("printer_details_order_supplies_button", timeout=20)
    
    def verify_printer_details_screen_printer_supplies_cartridge_K(self):
        return self.driver.wait_for_object("printer_details_supplies_K_container", timeout=20)
    
    def verify_printer_details_screen_printer_supplies_cartridge_C(self):
        return self.driver.wait_for_object("printer_details_supplies_C_container", timeout=20)
    
    def verify_printer_details_screen_printer_supplies_cartridge_M(self):
        return self.driver.wait_for_object("printer_details_supplies_M_container", timeout=20)
    
    def verify_printer_details_screen_printer_supplies_cartridge_Y(self):
        return self.driver.wait_for_object("printer_details_supplies_Y_container", timeout=20)

    def click_printer_details_screen_order_supplies_button(self):
        return self.driver.click("printer_details_order_supplies_button", timeout=20)

    def verify_printer_order_supplies_url(self):
        return self.driver.wdvr.current_url == self.printer_order_supplies_newtab_url

############################ Printer Details - Install HP Software popup #########################################
    
    def verify_install_hp_software_popup(self):
        self.click_printer_action_dropdown()
        sleep(7)
        self.select_install_hp_software_option()
        if self.driver.wait_for_object("printer_details_install_hp_software_popup",timeout=20) is True:
            return True

    def verify_install_hp_software_popup_title(self):
        return self.driver.verify_object_string("install_hp_software_popup_title")

    def verify_install_hp_software_popup_driver_download_hyperlink(self):
        return self.driver.wait_for_object("install_hp_software_popup_download_driver_btn")

    def verify_install_hp_software_popup_cancel_button(self):
        return self.driver.wait_for_object("install_hp_software_popup_cancel_btn")

    def verify_install_hp_software_popup_install_button(self):
        return self.driver.wait_for_object("install_hp_software_popup_install_btn")

    def click_install_hp_software_popup_cancel_button(self):
        return self.driver.click("install_hp_software_popup_cancel_btn")
    
    def click_install_hp_software_popup_install_button(self):
        return self.driver.click("install_hp_software_popup_install_btn")
    
############################ Printer Acrions - Remove Printer #########################################

    def verify_remove_printer_modal(self):
        self.driver.wait_for_object("remove_printer_modal")
        assert self.driver.get_attribute("checkmark_printer_opted_out_of_privacy", "aria-checked", displayed=False) == "false", "Opted out of privacy is already checked"
        assert self.driver.get_attribute("checkmark_users_no_longer_access_printer", "aria-checked", displayed=False) == "false", "Users no longer access printer is already checked"
        assert self.driver.get_attribute("remove_button_modal", "disabled") == "true", "Remove button is enabled"

    def click_checkmark_printer_opted_out_of_privacy(self):
        self.driver.click("checkmark_printer_opted_out_of_privacy", displayed=False)

    def click_checkmark_users_no_longer_access_printer(self):
        self.driver.click("checkmark_users_no_longer_access_printer", displayed=False)

    def click_remove_printer_button(self):
        self.driver.click("remove_button_modal")

    def verify_hp_plus_benefits_removed_modal(self):
        self.driver.wait_for_object("hp_plus_benefits_removed_modal", timeout=20)

    def click_hp_plus_benefits_remove_continue_button(self):
        self.driver.click("hp_plus_benefits_remove_continue_button")

############################ Printer Details - Overview Page ###########################################

    def verify_printer_overview_serial_number_title(self):
        return self.driver.verify_object_string("printer_detail_overview_serial_number") 

    def get_printer_details_screen_overview_serial_number(self):
        return self.driver.get_text("printer_detail_overview_serial_number").split(" ")[2]    

    def verify_printer_details_screen_overview_network(self):
        return self.driver.verify_object_string("printer_detail_overview_network")

    def get_printer_details_screen_overview_network_ip_address_title(self):
        expected_ip=self.driver.wait_for_object("printer_detail_overview_network").text
        return expected_ip.split(" ")[0]

    def get_printer_overview_ip_address_title(self):
        expected_ip=self.driver.wait_for_object("printer_detail_overview_network_ip").text
        logging.info(expected_ip.split(" ")[1]).split("\n")
        return (expected_ip.split(" ")[1]).split("\n")[1]

    def get_printer_network_ip_address(self):
        expected_ip=self.driver.wait_for_object("printer_detail_overview_network_ip").text
        return (expected_ip.split("\n")[0].split(" ")[2])

    def get_printer_network_hostname(self):
        expected_ip=self.driver.wait_for_object("printer_details_screen_overview_network_host_name").text
        return (expected_ip.split("\n")[0].split(" ")[2])

    def verify_printer_details_screen_overview_network_summary_link(self):
        return self.driver.verify_object_string("printer_detail_overview_network_summary_link")
    
    def click_printer_overview_network_summary_link(self):
        return self.driver.click("printer_detail_overview_network_summary_link")

    def verify_network_summary_popup_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_title")

    def get_network_summary_popup_wired_title(self):
        actual_value = self.driver.wait_for_object("printer_details_overview_summary_wired").text.lower()
        return (actual_value.split("(")[0]).strip()

    def verify_network_summary_popup_wired_connectivity_status_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_status_title")

    def get_network_summary_popup_wired_connectivity_status(self):
        return self.driver.wait_for_object("printer_details_overview_summary_status").text
    
    def get_printer_network_summary_popup_host_name_title(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_host_name_title")
        return expected_host_name.split(":")[0]
    
    def get_printer_network_summary_popup_host_name(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_host_name_title")
        return expected_host_name.split(": ")[1]

    def get_printer_network_summary_popup_ip_address_title(self):
        expected_ip=self.driver.get_text("printer_details_overview_summary_ip_address_title")
        return expected_ip.split(":")[0]

    def get_printer_network_summary_popup_ip_address(self):
        expected_ip_addr=self.driver.get_text("printer_details_overview_summary_ip_address_title")
        return (expected_ip_addr.split(":")[1]).replace(" ","").strip()

    def get_printer_network_summary_popup_hardware_address_title(self):
        expected_hardware_title=self.driver.get_text("printer_details_overview_summary_hardware_address_title")
        return expected_hardware_title.split(":")[0]

    def get_printer_network_summary_popup_hardware_address(self):
        expected_hardware_addr=self.driver.get_text("printer_details_overview_summary_hardware_address_title")
        return expected_hardware_addr.split(":")[1]

    def get_printer_network_summary_popup_wireless_title(self):
        actual_value = self.driver.wait_for_object("printer_details_overview_summary_wireless_title").text.lower()
        return (actual_value.split("(")[0]).strip()

    def verify_printer_network_summary_popup_wireless_status_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_wireless_status_title")

    def get_printer_details_screen_overview_network_summary_screen_wireless_status(self):
        return self.driver.wait_for_object("printer_details_overview_summary_wireless_status").text

    def verify_printer_network_summary_popup_wifi_status_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_wifi_direct_title")

    def get_printer_network_summary_popup_wifi_status(self):
        return self.driver.wait_for_object("printer_details_overview_summary_wifi_direct_status").text

    def get_printer_network_summary_popup_wifi_title(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_wifi_direct_name_title")
        return expected_host_name.split(":")[0]

    def get_printer_network_summary_popup_wifi_name(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_wifi_direct_name_title")
        return expected_host_name.split(":")[1]

    def get_printer_network_summary_popup_wifi_channel_title(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_wifi_direct_channel_title")
        return expected_host_name.split(":")[0]

    def get_printer_network_summary_popup_wifi_channel(self):
        expected_host_name=self.driver.get_text("printer_details_overview_summary_wifi_direct_channel_title")
        return expected_host_name.split(":")[1]

    def verify_printer_network_summary_popup_bluetooth_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_bluetooth_title")

    def verify_printer_network_summary_popup_bluetooth_status_title(self):
        return self.driver.verify_object_string("printer_details_overview_summary_bluetooth_status_title")

    def get_printer_network_summary_popup_bluetooth_status(self):
        return self.driver.wait_for_object("printer_details_overview_summary_bluetooth_status").text

    def click_printer_network_summary_popup_close_button(self):
        return self.driver.click("printer_details_overview_summary_close_button")
        
    def verify_printer_details_screen_overview_firmware_title(self):
        return self.driver.verify_object_string("printer_details_overview_firmware_title")

    def verify_printer_details_screen_overview_firmware(self):
        return self.driver.wait_for_object("printer_details_screen_overview_firmware")
    
    def verify_printer_details_screen_overview_network_ip_address(self):
        return self.driver.wait_for_object("printer_details_screen_overview_network_ip_address")
    
    def verify_printer_details_screen_overview_network_host_name(self):
        return self.driver.wait_for_object("printer_details_screen_overview_network_host_name")
    
    def verify_printer_details_additional_settings_title(self):
        return self.driver.verify_object_string("printer_details_additional_settings_title")
    
    def click_printer_details_additional_settings_title(self):
        return self.driver.verify_object_string("printer_details_additional_settings_title")   
    
    def get_printer_details_screen_overview_firmware_number(self):
        return self.driver.get_text("printer_details_overview_firmware")

    def verify_printer_details_screen_overview_smart_security(self):
        return self.driver.verify_object_string("printer_details_overview_smart_security")

    def get_printer_details_screen_overview_smart_security(self):
        return self.driver.get_text("printer_details_overview_smart_security")

    def get_printer_overview_smart_security_status(self):
        return self.driver.wait_for_object("printer_details_overview_smart_security_status").text.split("\n")[1]

    def verify_printer_details_screen_overview_smart_security_manage_link(self):
        return self.driver.verify_object_string("printer_details_overview_smart_security_manage_link")
    
    def click_printer_overview_manage_hyperlink(self):
        return self.driver.click("printer_details_overview_smart_security_manage_link")

    def verify_smart_security_setting_page(self):
        return self.driver.wait_for_object("printer_details_overview_manage_link_solution_screen",timeout=30)

    def verify_printer_details_screen_overview_settings_scan_title(self):
        return self.driver.verify_object_string("printer_detail_scan_label")
    
    def verify_printers_details_scan_destinations_settings_is_displayed(self,displayed=True):
        return self.driver.wait_for_object("printer_detail_scan_label", timeout=30, invisible=not displayed, raise_e=False)

    def verify_printer_settings_scan_to_email(self,timeout=50):
        actual_value = self.driver.wait_for_object("printer_detail_scan_to_email_label",timeout=timeout).text
        return (actual_value.split("(")[0]).strip()
    
    def verify_printer_overview_serial_number(self):
        return self.driver.wait_for_object("printer_overview_serial_number")
    
    def verify_printer_settings_scan_to_email_desc(self):
        return self.driver.verify_object_string("printer_settings_scan_to_email_desc")
    
    def verify_printer_settings_scan_to_cloud_desc(self):
        return self.driver.verify_object_string("printer_settings_scan_to_cloud_desc")

    def verify_printer_settings_scan_to_email_setup_button(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_detail_scan_to_email_setup_button", timeout=20))

    def get_printer_settings_scan_to_email_setup_button_status(self):
        return self.driver.get_text("printer_detail_scan_to_email_setup_button")

    def click_printer_settings_scan_to_email_setup_button(self):
        return self.driver.click("printer_detail_scan_to_email_setup_button",timeout=20)

    def verify_printer_settings_scan_to_email_setup_screen(self):
        return self.driver.wait_for_object("printer_details_overview_scan_to_email_screen_title")
    
    def verify_printer_settings_scan_to_cloud(self):
        actual_value = self.driver.wait_for_object("printer_detail_scan_to_cloud_label").text
        return (actual_value.split("(")[0]).strip()

    def verify_printer_settings_scan_to_cloud_setup_button(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_detail_scan_to_cloud_setup_button", timeout=20))

    def click_printer_settings_scan_to_cloud_setup_button(self):
        return self.driver.click("printer_detail_scan_to_cloud_setup_button")

    def verify_printer_settings_scan_to_cloud_setup_screen(self):
        return self.driver.wait_for_object("printer_details_overview_scan_to_cloud_screen_title")

    def verify_printer_settings_set_up_printer_fax_title_is_displayed(self):
        if self.driver.wait_for_object("printer_details_setup_printer_fax_title", timeout=30, raise_e=False) is not False:
            return True
        else:
            logging.info("Fax setup is not present for this printer")
            return False

    def verify_printer_settings_set_up_printer_fax_title(self):
        # return self.driver.verify_object_string("printer_details_setup_printer_fax_title",timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_details_setup_printer_fax_title", timeout=30))
        return self.driver.verify_object_string("printer_details_setup_printer_fax_title")

    def verify_printer_settings_set_up_printer_fax_desc(self):
        return self.driver.verify_object_string("printer_details_setup_printer_fax_desc")

    def verify_printer_settings_set_up_printer_fax_set_up_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_details_setup_printer_fax_setup_button", timeout=20))
        return self.driver.find_object("printer_details_setup_printer_fax_setup_button")

    def click_printer_settings_set_up_printer_fax_set_up_button(self):
        return self.driver.click("printer_details_setup_printer_fax_setup_button",timeout=30)

    def click_printer_details_screen_overview_print_test_page_button(self):
        return self.driver.click("printer_details_screen_overview_print_test_page_button")

    def verify_printer_details_screen_overview_print_test_page_title(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_title")
    
    def verify_printer_details_screen_overview_print_test_page_desc(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_desc")

    def verify_printer_details_screen_overview_print_test_page_drivers_required_title(self):
        return self.driver.wait_for_object("printer_details_screen_overview_print_test_page_drivers_required_title")
    
    def verify_printer_details_screen_overview_print_test_page_drivers_required_desc(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_drivers_required_desc")
    
    def verify_printer_details_screen_overview_print_test_page_install_hp_software_hyperlink(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_install_hp_software_hyperlink")
    
    def verify_printer_details_screen_overview_print_test_page_cancel_button(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_cancel_button")
    
    def verify_printer_details_screen_overview_print_test_page_print_button(self):
        return self.driver.verify_object_string("printer_details_screen_overview_print_test_page_print_button")

    def verify_printer_details_screen_overview_print_card_title(self):
        return self.driver.verify_object_string("overview_tab_print_card_title")
    
    def verify_printer_details_screen_overview_print_test_page_button(self):
        return self.driver.wait_for_object("printer_details_screen_overview_print_test_page_button")

    def verify_overview_enable_print_anywhere_toggle_button(self):
        return self.driver.wait_for_object("overview_tab_print_anywhere_toggle_button")
    
    def verify_overview_enable_print_anywhere_toggle_button_label(self):
        return self.driver.verify_object_string("overview_tab_print_anywhere_toggle_button_label")
    
    def verify_overview_enable_print_anywhere_toggle_button_description(self):
        return self.driver.verify_object_string("overview_tab_print_anywhere_toggle_button_desc")

    def verify_overview_require_private_pickup_toggle_button(self):
        return self.driver.wait_for_object("overview_tab_private_pickup_toggle_button",timeout=30)
    
    def verify_overview_require_private_pickup_toggle_button_label(self):
        return self.driver.verify_object_string("overview_tab_private_pickup_toggle_button_label")
    
    def verify_overview_require_private_pickup_toggle_button_description(self):
        return self.driver.verify_object_string("overview_tab_private_pickup_toggle_button_desc")
    
    def get_overview_enable_print_anywhere_toggle_button_status(self):
        toggle_status = self.driver.get_attribute("overview_tab_print_anywhere_toggle_button","aria-checked")
        return toggle_status

    def get_overview_require_private_pickup_toggle_button_status(self):
        toggle_status = self.driver.get_attribute("overview_tab_private_pickup_toggle_button","aria-checked")
        return toggle_status

    def verify_overview_require_private_pickup_toggle_button_is_displayed(self, displayed=True):
        return self.driver.wait_for_object("overview_tab_private_pickup_toggle_button", timeout=30, invisible=not displayed)
        
    def click_overview_enable_print_anywhere_toggle_button(self):
        return self.driver.click("overview_tab_print_anywhere_toggle_button")

    def click_overview_require_private_pickup_toggle_button(self):
        return self.driver.click("overview_tab_private_pickup_toggle_button",timeout=30)
    
############################ Printer Details - Solutions Tab     ###########################################

    def click_printer_solutions_tab(self):
        return self.driver.click("printer_details_solutions_label",timeout=30)

    def verify_printer_details_solutions_smart_security_title_is_displayed(self):
        if self.driver.wait_for_object("printer_details_solutions_smart_security_title", timeout=30, raise_e=False) is not False:
            return True
        else:
            logging.info("Smart security entitlenment is not active for this printer")
            return False
    
    def verify_printer_solutions_smart_security_title(self):
        return self.driver.verify_object_string("printer_details_solutions_smart_security_title",timeout=30)

    def verify_printer_solutions_smart_security_description(self):
        return self.driver.verify_object_string("printer_details_solutions_smart_security_desc")

    def verify_printer_solutions_smart_security_manage_link(self):
        return self.driver.verify_object_string("printer_details_solutions_smart_security_manage_link")

    def click_printer_solutions_smart_security_manage_link(self):
        return self.driver.click("printer_details_solutions_smart_security_manage_link")

    def verify_printer_solutions_print_anywhere_title(self):
        return self.driver.verify_object_string("printer_details_solutions_print_anywhere_title")

    def verify_printer_solutions_print_anywhere_description(self):
        return self.driver.verify_object_string("printer_details_solutions_print_anywhere_desc")

    def verify_printer_solutions_print_anywhere_manage_link(self):
        return self.driver.verify_object_string("printer_details_solutions_print_anywhere_manage_link")

    def click_printer_solutions_print_anywhere_manage_link(self):
        return self.driver.click("printer_details_solutions_print_anywhere_manage_link")

    def verify_printer_solutions_print_anywhere_manage_link_is_displayed(self):
        if self.driver.wait_for_object("printer_details_solutions_print_anywhere_manage_link", timeout=30, raise_e=False) is not False:
            return True
        else:
            logging.info("Smart security entitlenment is not active for this printer")
            return False
        
    def verify_print_anywhere_screen_title(self):
        return self.driver.verify_object_string("print_anywhere_screen",timeout=30)

    def verify_printer_solutions_sustainability_title(self):
        return self.driver.verify_object_string("printer_details_solutions_sustainability_title")

    def verify_printer_solutions_sustainability_description(self):
        return self.driver.verify_object_string("printer_details_solutions_sustainability_desc")

    def verify_printer_solutions_sustainability_learn_more_link(self):
        return self.driver.verify_object_string("printer_details_solutions_sustainability_learn_more_link")

    def click_printer_solutions_sustainability_learn_more_link(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_details_solutions_sustainability_learn_more_link", timeout=20))
        return self.driver.click("printer_details_solutions_sustainability_learn_more_link")

    def verify_printer_solutions_sustainability_learn_more_link_is_displayed(self):
        if self.driver.wait_for_object("printer_details_solutions_sustainability_learn_more_link", timeout=30, raise_e=False) is not False:
            return True
        else:
            logging.info("Smart security entitlenment is not active for this printer")
            return False
    
    def verify_sustainability_screen_title(self):
        return self.driver.wait_for_object("sustainability_screen",timeout=30)

############################ Printer Details - Additional Setting tabs  ###########################################

    def click_printer_additional_setting_tab(self):
        return self.driver.click("printer_details_additional_setting_label")

    def verify_printer_details_screen_additional_settings_title(self):
        return self.driver.verify_object_string("printer_details_additional_setting_label")

    def verify_and_click_connected_printer(self):
        self.select_page_size_new("100")
        connected = "connected"
        printer_name = "HP"
        connectivity_column = self.get_header_index("connectivity")
        printername_column = self.get_header_index("device_name")
        connectivity_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[connectivity_column],multiple=True)
        printername_list = self.driver.find_object("_shared_table_printer_col_by_index", format_specifier=[printername_column],multiple=True)
        for index in range(len(connectivity_list)):
            if connected == connectivity_list[index].text.lower():
                return printername_list[index].click()
            else:
                continue
        raise DeviceSearchException("Cannot find any connected printer")
    
############################ Printer Details - Overview tab - Fax setup Wizard  ###########################################
    
    def get_printer_settings_fax_set_up_button_type(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fax_setup_button_type", timeout=20))
        return self.driver.get_text("printer_fax_setup_button_type")

    def verify_printer_settings_set_up_printer_fax_manage_button(self):
        return self.driver.wait_for_object("printer_details_setup_printer_fax_manage_button")

    def click_printer_settings_set_up_printer_fax_manage_button(self):
        return self.driver.click("printer_details_setup_printer_fax_manage_button")

    def click_printers_fax_settings_open_fax_setup_wizard_button(self):
        return self.driver.click("fax_settings_open_fax_setup_wizard_button")

    def verify_printer_details_screen_overview_tab_fax_setup_wizard_title(self):
        return self.driver.verify_object_string("printer_details_screen_overview_tab_fax_setup_wizard_title", timeout=30)

    def verify_printer_details_fax_setup_wizard_fax_settings_page_title(self):
        return self.driver.verify_object_string("printer_details_fax_setup_wizard_fax_settings_page_title")

    def verify_printer_details_fax_setup_wizard_fax_settings_label(self):
        return self.driver.verify_object_string("printer_details_fax_setup_wizard_fax_settings_label")

    def verify_printer_details_fax_setup_wizard_voice_and_internet_options_label(self):
        return self.driver.verify_object_string("printer_details_fax_setup_wizard_voice_and_internet_options_label")

    def verify_printer_details_fax_setup_wizard_setup_configuration_label(self):
        return self.driver.verify_object_string("printer_details_fax_setup_wizard_setup_configuration_label")

    def verify_printer_details_fax_setup_wizard_summary_label(self):
        return self.driver.verify_object_string("printer_details_fax_setup_wizard_summary_label")

    def verify_printer_details_fax_setup_wizard_contextual_footer(self):
        return self.driver.wait_for_object("printer_details_fax_setup_wizard_contextual_footer")

    def verify_printer_details_fax_setup_wizard_contextual_footer_cancel_button(self):
        return self.driver.wait_for_object("printer_details_fax_setup_wizard_contextual_footer_cancel_button")
    
    def click_printer_details_fax_setup_wizard_contextual_footer_cancel_button(self):
        return self.driver.click("printer_details_fax_setup_wizard_contextual_footer_cancel_button")

    def verify_printer_details_fax_setup_wizard_contextual_footer_next_button(self):
        return self.driver.wait_for_object("printer_details_fax_setup_wizard_contextual_footer_next_button")
    
    def verify_printer_details_fax_setup_wizard_contextual_footer_save_button(self):
        return self.driver.wait_for_object("printer_details_fax_setup_wizard_contextual_footer_save_button")

    def verify_printer_details_fax_setup_wizard_contextual_footer_next_button_is_not_displayed(self):
        if self.driver.find_object("printer_details_fax_setup_wizard_contextual_footer_next_button").is_enabled():
            raise UnexpectedItemPresentException("Next button is enabled")
        return True 
    
    def verify_fax_setup_wizard_fax_settings_page_edit_info_title(self):
        return self.driver.verify_object_string("fax_settings_page_edit_info_title")

    def verify_fax_setup_wizard_fax_settings_page_edit_info_description(self):
        return self.driver.verify_object_string("fax_settings_page_edit_info_description")

    def verify_fax_setup_wizard_fax_settings_page_select_country_dropdown(self):
        return self.driver.wait_for_object("fax_settings_page_select_country_dropdown")

    def verify_fax_setup_wizard_fax_settings_page_name_field(self):
        return self.driver.wait_for_object("fax_settings_page_name_field")

    def verify_fax_setup_wizard_fax_settings_page_fax_number_field(self):
        return self.driver.wait_for_object("fax_settings_page_fax_number_field")

    def verify_fax_setup_wizard_fax_settings_page_voice_calls_message(self):
        return self.driver.verify_object_string("fax_settings_page_voice_calls_message")

    def verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message(self):
        return self.driver.verify_object_string("fax_settings_page_fax_ring_calls_message")

    def verify_fax_setup_wizard_fax_settings_page_voice_calls_message_yes_option(self):
        return self.driver.verify_object_string("fax_settings_page_voice_calls_message_yes_option")

    def verify_fax_setup_wizard_fax_settings_page_voice_calls_message_no_option(self):
        return self.driver.verify_object_string("fax_settings_page_voice_calls_message_no_option")

    def verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message_yes_option(self):
        return self.driver.verify_object_string("fax_settings_page_fax_ring_calls_message_yes_option")

    def verify_fax_setup_wizard_fax_settings_page_fax_ring_calls_message_no_option(self):
        return self.driver.verify_object_string("fax_settings_page_fax_ring_calls_message_no_option")

    def enter_fax_setup_wizard_fax_settings_page_fax_name(self,fax_name):
        return self.driver.send_keys("fax_settings_page_name_field",fax_name)

    def enter_fax_setup_wizard_fax_settings_page_fax_number(self,fax_number):
        return self.driver.send_keys("fax_settings_page_fax_number_field",fax_number)
            
    def click_printer_details_fax_setup_wizard_contextual_footer_next_button(self):
        return self.driver.click("printer_details_fax_setup_wizard_contextual_footer_next_button")

    def verify_printer_details_fax_setup_wizard_voice_and_internet_options_page_title(self):
        return self.driver.verify_object_string("fax_setup_wizard_voice_and_internet_options_page_title")

    def verify_fax_setup_wizard_voice_and_internet_page_internet_service_option_text(self):
        return self.driver.verify_object_string("fax_setup_wizard_voice_and_internet_page_internet_service_text")

    def verify_fax_setup_wizard_voice_and_internet_page_computer_modem_option_text(self):
        return self.driver.verify_object_string("fax_setup_wizard_voice_and_internet_page_computer_modem_text")

    def click_printer_details_fax_setup_wizard_contextual_footer_back_button(self):
        return self.driver.click("fax_setup_wizard_contextual_footer_back_button")

    def verify_printer_details_fax_setup_wizard_contextual_footer_back_button(self,displayed=True):
        return self.driver.wait_for_object("fax_setup_wizard_contextual_footer_back_button", invisible=not displayed, raise_e=False)

    def verify_fax_setup_wizard_voice_and_internet_page_internet_service_yes_option(self):
        return self.driver.wait_for_object("fax_setup_wizard_voice_and_internet_page_internet_service_yes_option")

    def verify_fax_setup_wizard_voice_and_internet_page_internet_service_no_option(self):
        return self.driver.wait_for_object("fax_setup_wizard_voice_and_internet_page_internet_service_no_option")

    def verify_fax_setup_wizard_voice_and_internet_page_computer_modem_no_option(self):
        return self.driver.wait_for_object("fax_setup_wizard_voice_and_internet_page_computer_modem_no_option")

    def verify_fax_setup_wizard_voice_and_internet_page_internet_service_dsl_modem_option(self):
        return self.driver.wait_for_object("fax_setup_wizard_voice_and_internet_page_internet_service_dsl_modem_option")

    def verify_fax_setup_wizard_voice_and_internet_page_internet_service_dial_up_modem_option(self):
        return self.driver.wait_for_object("fax_setup_wizard_voice_and_internet_page_internet_service_dial_up_modem_option")

    def verify_printer_details_fax_setup_wizard_setup_configuration_page_title(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_title")

    def verify_fax_setup_wizard_setup_configuration_page_description_note(self):
        return self.driver.get_text("fax_setup_wizard_setup_configuration_page_description_note")

    def verify_fax_setup_wizard_setup_configuration_page_voice_line_fax_option(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_voice_line_fax_option")
    
    def verify_fax_setup_wizard_setup_configuration_page_answering_machine_option(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_answering_machine_option")
    
    def verify_fax_setup_wizard_setup_configuration_page_dsl_adsl_service_option(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_dsl_adsl_service_option")
    
    def verify_fax_setup_wizard_setup_configuration_page_dsl_adsl_modem_option(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_dsl_adsl_modem_option")
    
    def verify_fax_setup_wizard_setup_configuration_page_dial_up_modem_option(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_dial_up_modem_option")

    def verify_fax_setup_wizard_setup_configuration_page_phone_card_warning_msg(self):
        self.driver.get_text("fax_setup_wizard_setup_configuration_page_phone_card_warning_msg")
        return self.driver.verify_object_string("fax_setup_wizard_setup_configuration_page_phone_card_warning_msg")
    
    def verify_printer_details_fax_setup_wizard_setup_summary_page_title(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_title")

    def verify_fax_setup_wizard_setup_summary_page_description(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_description")

    def verify_fax_setup_wizard_setup_summary_page_company_name_label(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_company_name_label")

    def verify_fax_setup_wizard_setup_summary_page_fax_number_label(self):
        self.driver.get_text("fax_setup_wizard_setup_summary_page_fax_number_label")
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_fax_number_label")

    def verify_fax_setup_wizard_setup_summary_page_auto_answer_label(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_auto_answer_label")

    def verify_fax_setup_wizard_setup_summary_page_distinctive_ring_label(self):
        return self.driver.verify_object_string("fax_setup_wizard_setup_summary_page_distinctive_ring_label")

    def verify_fax_setup_wizard_setup_summary_page_company_name_text(self):
        return self.driver.get_text("fax_setup_wizard_setup_summary_page_company_name")

    def verify_fax_setup_wizard_setup_summary_page_fax_number(self):
        return self.driver.get_text("fax_setup_wizard_setup_summary_page_fax_number")

    def verify_fax_setup_wizard_unsaved_changes_popup(self):
        return self.driver.verify_object_string("fax_setup_wizard_unsaved_changes_popup")

    def verify_fax_setup_wizard_unsaved_changes_popup_desc(self):
        return self.driver.verify_object_string("fax_setup_wizard_unsaved_changes_popup_desc")

    def verify_fax_setup_wizard_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("fax_setup_wizard_unsaved_changes_popup_cancel_button")

    def verify_fax_setup_wizard_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("fax_setup_wizard_unsaved_changes_popup_leave_button")

    def click_fax_setup_wizard_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("fax_setup_wizard_unsaved_changes_popup_cancel_button")
    
    def click_fax_setup_wizard_unsaved_changes_popup_leave_button(self):
        return self.driver.click("fax_setup_wizard_unsaved_changes_popup_leave_button",timeout=30)
    
    def click_fax_setup_wizard_fax_settings_page_select_country_dropdown(self):
        return self.driver.click("fax_settings_page_select_country_dropdown")

    def enter_country_name_fax_setup_wizard_fax_settings_page_country_dropdown(self,country_name):
        return self.driver.send_keys("fax_settings_page_select_country_dropdown_search_field", country_name)

    def select_country_name_fax_setup_wizard_fax_settings_page_country_dropdown(self):
        return self.driver.click("fax_settings_page_country_dropdown_search_option")
        
    def verify_fax_setup_wizard_fax_settings_page_country_dropdown_no_items_msg(self):
        self.driver.wait_for_object("fax_settings_page_country_dropdown_search_no_items_found_msg",timeout=10)
        return self.driver.get_text("fax_settings_page_country_dropdown_search_no_items_found_msg")
    
    ##########################   Printer Details - HP Instant Ink tab  ##################################################  

    def verify_printer_details_screen_hpinstantink_is_displayed(self,displayed=True):
        return self.driver.wait_for_object("printer_details_hpinstantink", timeout=40,invisible=not displayed, raise_e=False) 

    def click_printer_details_screen_hpinstantink_tab(self):
        return self.driver.click("printer_details_hpinstantink")
    
    def verify_printers_details_screen_hpinstantink_tab_header(self):
        return self.driver.verify_object_string("printer_details_hpinstantink_tab_header",timeout=30)

    def verify_printer_details_hpinstantink_tab_instantink_label(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_instantink_label")

    def verify_printer_details_hpinstantink_tab_data_unavailable_msg(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_data_unavailable_msg")
    
    def verify_printer_details_hpinstantink_tab_status(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_status", timeout=30).text

    def verify_printer_details_hpinstantink_tab_description(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_description")

    def verify_printer_details_hpinstantink_tab_enrollnow_button(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_enrollnow_button",timeout=30)

    def verify_printer_details_hpinstantink_tab_learnmore_button(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_tab_learnmore_button",timeout=30)
    
    def click_printer_details_hpinstantink_tab_enrollnow_button(self):
        return self.driver.click("printer_details_hpinstantink_tab_enrollnow_button",timeout=30)

    def click_printer_details_hpinstantink_tab_learnmore_button(self):
        return self.driver.click("printer_details_hpinstantink_tab_learnmore_button",timeout=30)
    
    ############## HP Instant Ink tab - Learnmore ######################

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    def verify_hpinstantink_learnmore_newtab_url(self):
        return self.driver.wdvr.current_url == self.hpinstantink_learn_more_newtab_url

    def verify_printer_details_hpinstantink_page_title(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_page_title", timeout=30)

    ############ HP Instant Ink - Enroll now Page ##################

    def verify_printer_details_hpinstantink_enrollnow_page_title(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_enrollnow_page_title",timeout=40)

    def verify_printer_details_hpinstantink_enrollnow_page_desc(self):
        return self.driver.verify_object_string("printer_details_hpinstantink_enrollnow_page_desc")
    
    def verify_printer_details_hpinstantink_enrollnow_page_learnmore_link(self):
        return self.driver.verify_object_string("printer_details_hpinstantink_enrollnow_page_learnmore_link")

    def verify_printer_details_hpinstantink_enrollnow_page_continue_button(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_enrollnow_page_continue_button")

    def verify_printer_details_hpinstantink_enrollnow_page_backtodashboard_button(self):
        return self.driver.wait_for_object("printer_details_hpinstantink_enrollnow_page_backtodashboard_button")

    def click_hpinstantink_enrollnow_page_backtodashboard_button(self):
        return self.driver.click("printer_details_hpinstantink_enrollnow_page_backtodashboard_button")

    def click_hpinstantink_enrollnow_page_continue_button(self):
        return self.driver.click("printer_details_hpinstantink_enrollnow_page_continue_button")

    def verify_hpinstantink_tab_enrollnow_details_page_plan_widget(self):
        return self.driver.wait_for_object("hpinstantink_tab_enrollnow_details_page_plan_widget",timeout=30)

    def verify_hpinstantink_tab_enrollnow_details_page_title(self):
        return self.driver.wait_for_object("hpinstantink_tab_enrollnow_details_page_title")

    def click_hpinstantink_tab_enroll_enrollnow_page_backtodashboard_button(self):
        return self.driver.click("hpinstantink_tab_enroll_enrollnow_page_backtodashboard_button")
    
############################## Printer Details Screen - Additional Settings #################

    def click_printer_details_screen_additional_settings_tab(self):
        return self.driver.click("printer_details_additional_settings_tab")

    def verify_tools_widget_printer_information_button(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("additional_settings_printer_information_button", timeout=20))
    
    def verify_tools_widget_asset_tracking_button(self):
        return self.driver.wait_for_object("additional_settings_asset_tracking_button")
    
    def verify_tools_widget_restart_printer_button(self):
        return self.driver.wait_for_object("additional_settings_restart_printer_button")

    def verify_settings_widget_date_and_time_button(self):
        return self.driver.wait_for_object("additional_settings_date_and_time_button")

    def verify_settings_widget_international_button(self):
        return self.driver.wait_for_object("additional_settings_international_buttton")
    
#################### Printer Information Screen UI ############################33
    
    def click_additional_settings_printer_information_button(self):
        return self.driver.click("additional_settings_printer_information_button",timeout=30)
    
    def verify_additional_settings_printer_info_title(self):
        return self.driver.verify_object_string("printer_info_popup_title",timeout=30)

    def verify_additional_settings_printer_info_table_product_name_title(self):
        return self.driver.verify_object_string("printer_info_table_product_name_title",timeout=30)

    def verify_additional_settings_printer_info_table_product_number_title(self):
        return self.driver.verify_object_string("printer_info_table_product_number_title")
    
    def verify_additional_settings_printer_info_table_product_serial_number_title(self):
        return self.driver.verify_object_string("printer_info_table_product_serial_number_title")

    def verify_additional_settings_printer_info_table_service_id_title(self):
        return self.driver.verify_object_string("printer_info_table_service_id_title")

    def verify_additional_settings_printer_info_table_device_name_title(self):
        return self.driver.verify_object_string("printer_info_table_device_name_title")

    def verify_additional_settings_printer_info_table_asset_number_title(self):
        return self.driver.verify_object_string("printer_info_table_asset_number_title")

    def verify_additional_settings_printer_info_table_firmware_version_title(self):
        return self.driver.verify_object_string("printer_info_table_firmware_version_title")

    def verify_additional_settings_printer_info_table_country_region_title(self):
        return self.driver.verify_object_string("printer_info_table_country_region_title")
    
    def verify_additional_settings_printer_info_popup_close_button(self):
        return self.driver.wait_for_object("printer_info_popup_close_button")
    
    def click_additional_settings_printer_info_popup_close_button(self):
        return self.driver.click("printer_info_popup_close_button")
    
   ######################## Printer Information Data verification ###################

    def click_overview_button(self):
        return self.driver.click("overview_tab_button")
     
    def get_printer_info_product_name(self):
        return self.driver.get_text("printer_info_popup_table_product_name")
    
    def get_printer_info_popup_product_header(self):
        actual_product_name = self.driver.get_text("printer_info_popup_product_name_header")
        logging.info(actual_product_name)
        return actual_product_name

    def get_printer_info_serial_number(self):
        return self.driver.get_text("printer_info_serial_number")

    def get_printer_details_overview_serial_number(self):
        expected_serial_value = self.driver.get_text("printer_overview_serial_number")
        logging.info(expected_serial_value)
        return expected_serial_value
    
    def get_printer_info_popup_device_name(self):
        self.driver.wait_for_object("printer_info_popup_device_name",timeout=30)
        return self.driver.get_text("printer_info_popup_device_name")

    def get_printer_details_overview_device_name(self):
        expected_device_name = self.driver.get_text("overview_tab_device_name")
        logging.info(expected_device_name)
        return expected_device_name
    
    def get_printer_info_popup_firmware_version(self):
        return self.driver.get_text("printer_info_popup_firmware_version")
    
    def get_printer_details_overview_firmware_version(self):
        expected_firmware_version = self.driver.get_text("overview_tab_firmware_version")
        logging.info(expected_firmware_version)
        return expected_firmware_version

##################### Additional Settings - Asset Tracking UI #############################

    def click_additional_settings_asset_tracking_button(self):
        return self.driver.click("additional_settings_asset_tracking_button",timeout=30)
    
    def verify_additional_settings_asset_tracking_tab_title(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_title", timeout=30)

    def verify_additional_settings_asset_tracking_tab_desc(self):
        return self.driver.wait_for_object("additional_settings_asset_tracking_desc")
    
    def verify_additional_settings_asset_tracking_devicename_label(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_devicename_label")

    def verify_additional_settings_asset_tracking_asset_number_label(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_asset_number_label")

    def verify_additional_settings_asset_tracking_device_location_label(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_device_location_label")

    def verify_additional_settings_asset_tracking_company_name_label(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_company_name_label")

    def verify_additional_settings_asset_tracking_contact_person_label(self):
        return self.driver.verify_object_string("additional_settings_asset_tracking_contact_person_label")

    def verify_additional_settings_asset_tracking_cancel_button(self):
        return self.driver.wait_for_object("additional_settings_asset_tracking_cancel_button")

    def verify_additional_settings_asset_tracking_save_button(self):
        return self.driver.wait_for_object("additional_settings_asset_tracking_tab_save_button")

    def verify_additional_settings_asset_tracking_save_button_status(self,status):
        save_button=self.driver.wait_for_object("additional_settings_asset_tracking_tab_save_button")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True
    
    def click_additional_settings_asset_tracking_cancel_button(self):
        return self.driver.click("additional_settings_asset_tracking_cancel_button")

    ################## Asset tracking Information #########################################

    def get_printer_details_screens_printer_location(self):
        return self.driver.wait_for_object("printer_details_printer_location").text

    def clear_additional_settings_asset_tracking_device_name(self):
        return self.driver.clear_text("additional_settings_asset_tracking_device_name")
    
    def get_additional_settings_asset_tracking_tab_device_name(self):
        return self.driver.get_text("additional_settings_asset_tracking_device_name")

    def get_additional_settings_asset_tracking_location_name(self):
        return self.driver.get_text("additional_settings_asset_tracking_location_name")

    ################## Restart Printer window ########################################

    def click_additional_settings_restart_printer_button(self):
        return self.driver.click("additional_settings_restart_printer_button")

    def verify_additional_settings_restart_printer_title(self):
        return self.driver.verify_object_string("additional_settings_restart_printer_title", timeout=30)

    def verify_additional_settings_restart_printer_desc(self):
        return self.driver.wait_for_object("additional_settings_restart_printer_desc")
    
    def verify_additional_settings_restart_printer_warning_icon(self):
        return self.driver.wait_for_object("additional_settings_restart_printer_warning_icon")

    def verify_additional_settings_restart_printer_notification_text(self):
        return self.driver.verify_object_string("additional_settings_restart_printer_notification_text")

    def verify_additional_settings_restart_printer_cancel_button(self):
        return self.driver.wait_for_object("additional_settings_restart_printer_cancel_button")

    def verify_additional_settings_restart_printer_restart_button(self):
        return self.driver.wait_for_object("additional_settings_restart_printer_restart_button")

    def click_additional_settings_restart_printer_cancel_button(self):
        return self.driver.click("additional_settings_restart_printer_cancel_button")

    ################## Date and Time window ########################################
    
    def click_additional_settings_date_and_time_button(self):
        return self.driver.click("additional_settings_date_and_time_button")

    def verify_additional_settings_date_and_time_title(self):
        return self.driver.verify_object_string("additional_settings_date_and_time_title")
    
    def verify_additional_settings_current_printer_date_label(self):
        return self.driver.verify_object_string("additional_settings_current_printer_date_label")

    def verify_additional_settings_current_printer_date_value(self):
        return self.driver.wait_for_object("additional_settings_current_printer_date_value")

    def verify_additional_settings_current_printer_time_label(self):
        return self.driver.verify_object_string("additional_settings_current_printer_time_label")

    def verify_additional_settings_current_printer_time_value(self):
        return self.driver.wait_for_object("additional_settings_current_printer_time_value")

    def verify_additional_settings_current_printer_time_zone_label(self):
        return self.driver.verify_object_string("additional_settings_current_printer_time_zone_label")

    def verify_additional_settings_current_printer_time_zone_value(self):
        return self.driver.wait_for_object("additional_settings_current_printer_time_zone_value")
    
    def verify_additional_settings_date_and_time_note_label(self):
        return self.driver.wait_for_object("additional_settings_date_and_time_note_label")
    
    def verify_additional_settings_date_and_time_note_text1(self):
        return self.driver.verify_object_string("additional_settings_date_and_time_note_text1")
    
    def verify_additional_settings_date_and_time_note_text2(self):
        return self.driver.verify_object_string("additional_settings_date_and_time_note_text2")
    
    def verify_additional_settings_change_date_and_time_button(self):
        return self.driver.wait_for_object("additional_settings_change_date_and_time_button")
    
    def verify_additional_settings_change_date_and_time_close_button(self):
        return self.driver.wait_for_object("additional_settings_change_date_and_time_close_button")

    def click_additional_settings_change_date_and_time_button(self):
        return self.driver.click("additional_settings_change_date_and_time_button")

    ######################Change Date And Time wizard##########################

    def verify_change_date_and_time_wizard_title(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_title")

    def verify_change_date_and_time_wizard_methods(self):
        self.driver.verify_object_string("change_date_and_time_wizard_steps_select_method")
        self.driver.verify_object_string("change_date_and_time_wizard_steps_configure_settings")
        return self.driver.verify_object_string("change_date_and_time_wizard_steps_review_and_apply")   

    def verify_change_date_and_time_wizard_select_method_title(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_select_method_title")

    def verify_change_date_and_time_wizard_select_method_description(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_select_method_description")

    def verify_change_date_and_time_wizard_configure_manually_adjust_time_method(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_configure_method_manually_adjust_time")

    def verify_change_date_and_time_wizard_configure_sync_with_computer_method(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_configure_method_sync_with_computer")

    def verify_change_date_and_time_wizard_cancel_button(self):
        return self.driver.wait_for_object("change_date_and_time_wizard_cancel_button")

    def verify_change_date_and_time_wizard_next_button(self):
        return self.driver.wait_for_object("change_date_and_time_wizard_next_button")

    def click_change_date_and_time_wizard_configure_sync_with_computer_method(self):
        return self.driver.click("change_date_and_time_wizard_configure_method_sync_with_computer")

    def click_change_date_and_time_wizard_configure_manually_adjust_time_method(self):
        return self.driver.click("change_date_and_time_wizard_configure_method_manually_adjust_time")

    def click_change_date_and_time_wizard_cancel_button(self):
        return self.driver.click("change_date_and_time_wizard_cancel_button")

    def click_change_date_and_time_wizard_next_button(self):
        return self.driver.click("change_date_and_time_wizard_next_button")

    def verify_change_date_and_time_wizard_configure_settings_title(self):
        return self.driver.verify_object_string("change_date_and_time_wizard_configure_settings_title")

    def verify_configure_date_and_time_wizard_select_date_format_title(self):
        return self.driver.verify_object_string("configure_date_and_time_wizard_select_date_format_title")

    def verify_configure_date_and_time_wizard_select_time_format_title(self):
        return self.driver.verify_object_string("configure_date_and_time_wizard_select_time_format_title")

    def verify_configure_date_and_time_wizard_date_picker_dropdown(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("configure_date_and_time_wizard_date_picker_dropdown", timeout=20))    
    
    def verify_configure_date_and_time_wizard_time_format_label(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.verify_object_string("configure_date_and_time_wizard_time_format_label", timeout=20))
    
    def verify_configure_date_and_time_wizard_time_zone_title(self):
        return self.driver.verify_object_string("configure_date_and_time_wizard_time_zone_title")
    
    def verify_configure_date_and_time_wizard_time_zone_description(self):
        return self.driver.wait_for_object("configure_date_and_time_wizard_time_zone_description")
    
    def verify_configure_date_and_time_wizard_time_zone_dropdown(self):
        return self.driver.wait_for_object("configure_date_and_time_wizard_time_zone_dropdown")

    def verify_configure_date_and_time_wizard_daylight_saving_time_settings_title(self):
        return self.driver.verify_object_string("daylight_saving_time_settings_title")
        
    def verify_configure_date_and_time_wizard_daylight_saving_time_settings_description(self):
        return self.driver.verify_object_string("daylight_saving_time_settings_desc")
        
    def verify_configure_date_and_time_wizard_daylight_saving_time_settings_toggle(self):
        return self.driver.wait_for_object("daylight_saving_time_settings_toggle")
    
    def verify_configure_date_and_time_wizard_daylight_saving_time_settings_toggle_name(self):
        return self.driver.verify_object_string("daylight_saving_time_settings_toggle_name")

    def verify_configure_date_and_time_wizard_back_button(self):
        return self.driver.wait_for_object("configure_date_and_time_wizard_back_button")

    def click_configure_date_and_time_wizard_back_button(self):
        return self.driver.click("configure_date_and_time_wizard_back_button")

    ################################ Printer details - Usage Tab ##############################

    def click_printer_details_screen_usage_tab(self):
        return self.driver.click("printer_details_screen_usage_tab",timeout=20)
    
    def verify_printers_usage_data_last_updated_time(self):
        return self.driver.wait_for_object("usage_data_last_updated_time",timeout=30)
    
    def verify_printers_usage_data_last_updated_time_close_button(self):
        return self.driver.wait_for_object("usage_data_last_updated_time_close_btn",timeout=30)
    
    def verify_printers_usage_data_select_usage_view_dropdown(self):
        return self.driver.wait_for_object("usage_data_select_usage_view_dropdown")
    
    def verify_printers_usage_data_select_usage_view_year_dropdown(self):
        return self.driver.wait_for_object("usage_data_select_usage_view_year_dropdown")

    def verify_printers_usage_data_print_pages_usage_card(self):
        return self.driver.wait_for_object("usage_data_print_pages_usage_card")

    def verify_printers_usage_data_scan_usage_card(self):
        return self.driver.wait_for_object("usage_data_scan_usage_card")

    def verify_printers_usage_data_scan_usage_card_is_displayed(self):
        if self.driver.wait_for_object("usage_data_scan_usage_card", timeout=30, raise_e=False) is not False:
            return True
        else:
            logging.info("Printer:Scan settings is not supported")
            return False
    
    def click_printers_usage_data_last_updated_time_close_button(self):
        return self.driver.click("usage_data_last_updated_time_close_btn")

    def verify_printers_usage_data_last_updated_time_is_displayed(self,displayed=True):
        return self.driver.wait_for_object("usage_data_last_updated_time", timeout=30, invisible=not displayed)

    def click_printers_usage_data_select_usage_view_dropdown(self):
        return self.driver.click("usage_data_select_usage_view_dropdown",timeout=30)
    
    def click_usage_data_select_usage_view_dropdown_option(self,view_mode):
        return self.driver.click("usage_view_dropdown_monthly_option",format_specifier=[view_mode],timeout=20)

    def verify_print_pages_usage_card_title(self):
        return self.driver.verify_object_string("print_pages_usage_card_title")
    
    def verify_scan_usage_card_title(self):
        return self.driver.verify_object_string("scan_usage_card_title")
    
    def verify_print_pages_usage_card_highcharts_axis_printed_pages_title(self):
        return self.driver.verify_object_string("print_card_highcharts_axis_printed_pages_title")
    
    def verify_print_pages_usage_card_highcharts_black_and_white_button(self):
        return self.driver.wait_for_object("print_card_highcharts_black_and_white_button")
    
    def verify_print_pages_usage_card_highcharts_color_button(self):
        return self.driver.wait_for_object("print_card_highcharts_color_button")

    def verify_print_pages_usage_card_highcharts_average_use_button(self):
        return self.driver.wait_for_object("print_card_highcharts_average_use_button")

    def verify_scan_usage_card_highcharts_axis_scaned_pages_title(self):
        return self.driver.verify_object_string("scan_card_highcharts_axis_scaned_pages_title")

    def verify_scan_usage_card_highcharts_scans_button(self):
        return self.driver.wait_for_object("scan_card_highcharts_scans_button")
    
    def verify_scan_usage_card_highcharts_average_use_button(self):
        return self.driver.wait_for_object("scan_card_highcharts_average_use_button")
    
    def click_printers_usage_data_select_usage_view_year_dropdown(self):
        return self.driver.click("usage_data_select_usage_view_year_dropdown")
        
    def click_usage_data_select_usage_view_year_dropdown_option(self,year):
        return self.driver.click("usage_data_view_year_dropdown_option",format_specifier=[year])

    def verify_select_usage_view_year_dropdown_is_displayed(self,displayed=True):
        return self.driver.wait_for_object("usage_data_select_usage_view_year_dropdown", timeout=30, invisible=not displayed)

    def get_print_card_highcharts_yaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("print_card_highcharts_yaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def get_scan_card_highcharts_yaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("scan_card_highcharts_yaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def get_print_card_highcharts_xaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("print_card_highcharts_xaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def get_scan_card_highcharts_xaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("scan_card_highcharts_xaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    ##################################Scan destination screen####################################

    def verify_printer_scan_destination_screen(self):
        return self.driver.wait_for_object("scan_destination_screen_container",timeout=30)

    ############################Scan to Email setup#####################################
    
    def verify_printer_scan_to_email_setup_page_title(self):
        return self.driver.verify_object_string("printer_details_overview_scan_to_email_screen_title",timeout=30)
    
    def verify_printer_scan_to_email_setup_page_cancel_button(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_page_cancel_button")
    
    def verify_printer_scan_to_email_setup_page_save_button(self,displayed=True):
        return self.driver.wait_for_object("printer_scan_to_email_setup_page_save_button", timeout=20, invisible=not displayed, raise_e=False)
    
    def verify_printer_scan_to_email_setup_scan_destination_name_field_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_scan_destination_name_field_title")
    
    def verify_printer_scan_to_email_setup_scan_destination_name_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_scan_destination_name_field")
    
    def verify_printer_scan_to_email_setup_scan_destination_name_field_default_text(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_scan_destination_name_field_txt")

    def verify_printer_scan_to_email_setup_email_information_field_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_email_information_field_title")
    
    def verify_printer_scan_to_email_setup_email_information_field_desc(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_email_information_field_desc")

    def verify_printer_scan_to_email_setup_email_information_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_email_information_field")
    
    def verify_printer_scan_to_email_setup_email_information_field_default_text(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_email_information_field_txt")

    def click_printer_scan_to_email_setup_page_cancel_button(self):
        return self.driver.click("printer_scan_to_email_setup_page_cancel_button")

    def verify_unsaved_changes_popup(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_unsaved_changes_popup",timeout=30)

    def verify_unsaved_changes_popup_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_unsaved_changes_popup_title")
    
    def verify_unsaved_changes_popup_desc(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_unsaved_changes_popup_desc")
    
    def verify_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_unsaved_changes_popup_cancel_button")
    
    def verify_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_unsaved_changes_popup_leave_button")
    
    def click_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("printer_scan_to_email_setup_unsaved_changes_popup_cancel_button")
    
    def click_printer_scan_to_email_setup_page_cancel_button(self):
        return self.driver.click("printer_scan_to_email_setup_page_cancel_button")
    
    def click_unsaved_changes_popup_leave_button(self):
        return self.driver.click("printer_scan_to_email_setup_unsaved_changes_popup_leave_button")

    def verify_printer_scan_to_email_setup_subject_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_subject_field")
    
    def verify_printer_scan_to_email_setup_subject_field_default_text(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_subject_field_txt")

    def verify_printer_scan_to_email_setup_message_body_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_message_body_field")
    
    def verify_printer_scan_to_email_setup_message_body_field_default_text(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_message_body_field_txt")

    def verify_printer_scan_to_email_setup_settings_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_settings_field")
    
    def verify_printer_scan_to_email_setup_settings_field_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_settings_field_title")

    def verify_printer_scan_to_email_setup_file_type_dropdown(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_file_type_dropdown")
    
    def verify_printer_scan_to_email_setupfile_type_dropdown_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_file_type_dropdown_title")

    def verify_printer_scan_to_email_setup_security_pin_title(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_security_pin_title")
    
    def verify_printer_scan_to_email_setup_security_pin_toggle_btn(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_security_pin_toggle_btn")
    
    def verify_printer_scan_to_email_setup_security_pin_toggle_btn_label(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_security_pin_toggle_btn_label")
    
    def verify_printer_scan_to_email_setup_security_pin_toggle_btn_descripton(self):
        return self.driver.verify_object_string("printer_scan_to_email_setup_security_pin_toggle_btn_descripton")
    
    def verify_printer_scan_to_email_setup_security_pin_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_security_pin_field")
    
    def verify_printer_scan_to_email_setup_enter_security_pin_field(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_scan_to_email_setup_enter_security_pin_field", timeout=20))
        return self.driver.wait_for_object("printer_scan_to_email_setup_enter_security_pin_field")
    
    def verify_printer_scan_to_email_setup_confirm_security_pin_field(self):
        return self.driver.wait_for_object("printer_scan_to_email_setup_confirm_security_pin_field")
    


    
    def verify_printer_scan_destination_screen_breadcrumb(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_breadcrumb")
    
    def verify_printer_scan_destination_screen_refresh_button(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_refresh_button")
    
    def verify_printer_scan_destination_screen_last_updated_date_time(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_last_updated_date_time")

    def verify_printer_scan_destination_screen_printer_widget_container(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_widget_container")

    def verify_printer_scan_destination_screen_printer_details_container(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_details_container")
    
    def verify_printer_scan_destination_screen_printer_name(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_name")

    def verify_printer_scan_destination_screen_printer_model_name(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_model_name")
    
    def verify_printer_scan_destination_screen_printer_status(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_status")
    
    def verify_printer_scan_destination_screen_printer_status_icon(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_status_icon")
    
    def verify_printer_scan_destination_screen_printer_details_link(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_printer_details_link")

    def verify_printer_scan_destination_screen_scan_data_container(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_data_container")
    
    def verify_printer_scan_destination_screen_scan_data_email_title(self):
        return self .driver.verify_object_string("printer_scan_destination_screen_scan_data_email_title")
    
    def verify_printer_scan_destination_screen_scan_data_email_icon(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_data_email_icon")

    def verify_printer_scan_destination_screen_scan_data_email_count(self):
        return self.driver.wait_for_object("scan_destination_screen_scan_data_email_count")
    
    def verify_printer_scan_destination_screen_scan_data_cloud_title(self):
        return self.driver.verify_object_string("printer_scan_destination_screen_scan_data_cloud_title")
    
    def verify_printer_scan_destination_screen_scan_data_email_icon(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_data_cloud_icon")
    
    def verify_printer_scan_destination_screen_scan_data_cloud_count(self):
        return self.driver.wait_for_object("scan_destination_screen_scan_data_cloud_count")

    def verify_printer_scan_destination_screen_scan_tabs_container(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_tabs_container")
    
    def verify_printer_scan_destination_screen_scan_email_tab(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_email_tab")
    
    def verify_printer_scan_destination_screen_scan_cloud_tab(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_cloud_tab")

    def verify_printer_scan_destination_screen_search_field(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_search_field")
    
    def verify_printer_scan_destination_screen_scan_to_email_table(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_to_email_table")

    def click_printer_scan_destination_screen_scan_cloud_tab(self):
        return self.driver.click("printer_scan_destination_screen_scan_cloud_tab")
    
    def verify_printer_scan_destination_screen_scan_to_cloud_table(self):
        return self.driver.wait_for_object("printer_scan_destination_screen_scan_to_cloud_table")