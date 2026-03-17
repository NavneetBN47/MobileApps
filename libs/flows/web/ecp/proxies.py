import logging
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class ProxiesTableEmpty(Exception):
    pass

class ProxiesSearchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class FilterValueException(Exception):
    pass

class SettingsTableEmpty(Exception):
    pass

class SettingsSearchException(Exception):
    pass

class Proxies(ECPFlow):
    """
        Contains all of the elements and flows associated in Proxies section for ECP
    """
    flow_name = "proxies"

    ########################### Proxies Page ###########################

    def verify_proxies_tab(self):
        return self.driver.wait_for_object("proxies_tab", timeout=30)

    def verify_proxies_settings_tab(self):
        return self.driver.wait_for_object("settings_tab")
    
    def click_proxies_tab(self):
        return self.driver.click("proxies_tab")

    def click_proxies_settings_tab(self):
        return self.driver.click("settings_tab")
       
    def verify_proxies_search_box(self):
        return self.driver.wait_for_object("proxies_search_txt")

    def verify_proxies_filter_button(self):
        return self.driver.verify_object_string("proxies_filter_btn")
    
    def click_proxies_filter_button(self):
        return self.driver.click("proxies_filter_btn",timeout=30)
    
    def verify_hp_fleet_proxy_download_button(self):
        return self.driver.verify_object_string("hp_fleet_proxy_download_btn")

    def verify_proxies_add_button(self):
        return self.driver.verify_object_string("proxies_add_btn")
    
    def click_proxies_add_button(self):
        return self.driver.click("proxies_add_btn",timeout=30)

    def verify_proxies_column_option_gear_button(self):
        return self.driver.wait_for_object("proxies_column_option_gear_btn")

    def click_proxies_column_option_gear_button(self):
        return self.driver.click("proxies_column_option_gear_btn")

    def verify_proxies_table(self):
        return self.driver.wait_for_object("proxies_table")
    
    def verify_proxies_checkbox(self):
        if self.driver.wait_for_object("proxies_table_checkbox", timeout=30, raise_e=False) is not False:
            return True
        else:
            return False

    def verify_proxies_table_data_load(self):
        # It verifies proxies table is loaded and has lists of proxies entry.
        if self.driver.wait_for_object("proxies_table_checkbox", timeout=30, raise_e=False) is not False:
            return True
        else:
            self.verify_print_proxies_table_is_empty_msg()
            raise ProxiesTableEmpty("Proxies table is empty")
        
    def verify_print_proxies_table_is_empty_msg(self):
        self.driver.verify_object_string("proxies_table_no_item_found_msg")
        return self.driver.verify_object_string("proxies_table_add_proxy_msg")
                
    def search_proxy(self, proxy_name, raise_e=True, timeout=10):
        """
            Search proxy name in proxies table
            Should display list of proxies based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("proxies_search_txt",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("proxies_search_txt", proxy_name, press_enter=True)
        
        if self.driver.wait_for_object("proxies_table_no_item_found_lbl",raise_e=False) is not False:
            table_empty=self.driver.wait_for_object("proxies_table_no_item_found_lbl")
            logging.info(table_empty.text)
            return False
        else:
            table_entry_proxies = self.driver.find_object("proxies_table_proxy_name",multiple=True)

            for i in range(len(table_entry_proxies)):
                if proxy_name in table_entry_proxies[i].text:
                    logging.info("Proxy Name: " + table_entry_proxies[i].text+ " contains the searched string: " + proxy_name)
                    break
                else:
                    raise ProxiesSearchException("Proxy Name: " + table_entry_proxies[i].text+ " does not contain the searched string: " + proxy_name)
        return True

    def click_search_clear_button(self):
        return self.driver.click("proxies_clear_search_button")
    
    def verify_proxies_refresh_button(self):
        return self.driver.wait_for_object("proxies_refresh_section")
        
    ########################### Proxies contextual footer ###########################

    def click_proxies_checkbox(self):
        return self.driver.click("proxies_table_checkbox")

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("proxies_contextual_footer")

    def verify_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("proxies_contextual_footer",invisible=True)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("proxies_contextual_footer_cancel_button")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.verify_object_string("proxies_contextual_footer_selected_item_lbl")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("proxies_contextual_footer_select_action_dropdown")

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("proxies_contextual_footer_continue_button")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("proxies_contextual_footer_cancel_button")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("proxies_contextual_footer_continue_button")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("proxies_contextual_footer_select_action_dropdown")

    def select_contextual_footer_select_action_dropdown_option(self,option):
        options = self.driver.find_object("proxies_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == "Edit":
            options[0].click()
        elif option == "Remove":
            options[1].click()

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("proxies_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

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

    def verify_proxies_tabel_column(self,column_name,displayed=True):
        if column_name == "Connectivity":
                return self.driver.wait_for_object("proxies_table_connectivity_column", invisible=not displayed)
        elif column_name == "Last Updated":
                return self.driver.wait_for_object("proxies_table_last_updated_column", invisible=not displayed)
        elif column_name == "Date Added":
                return self.driver.wait_for_object("proxies_table_date_added_column", invisible=not displayed)
        
    ################################## Filter Side Bar ##################################################

    def verify_filter_side_bar_title(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("filter_side_bar_title", invisible=not displayed)
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

        if self.driver.wait_for_object("proxies_table_no_item_found_lbl",raise_e=False) is not False:
            return False
        else:
            table_entry_data = self.driver.find_object("proxies_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True

    def verify_proxies_filter_items_selected_text_displayed(self, displayed=True):
        return self.driver.wait_for_object("filter_side_bar_items_selected_text", invisible=not displayed)

    def get_proxies_filter_items_selected_text(self):
        return self.driver.wait_for_object("filter_side_bar_items_selected_text").text
    
    def verify_proxies_filter_clear_all_button(self):
        return self.driver.wait_for_object("filter_side_bar_items_clear_all_btn")

    def click_proxies_filter_clear_all_button(self):
        return self.driver.click("filter_side_bar_items_clear_all_btn")
    
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
        return self.driver.wait_for_object("verify_proxy_popup_code_tooltip_msg").text
    
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
    
    def verify_add_proxy_toast_message(self,proxy_name):
        return self.check_toast_successful_message(f"{proxy_name} successfully added.")

    def removing_the_existing_proxy(self):
        self.click_proxies_checkbox()
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_select_action_dropdown_option("Remove")
        self.click_contextual_footer_continue_button()
        self.click_remove_proxy_popup_remove_button()
        self.click_search_clear_button()
        self.verify_proxies_table_data_load()
        assert False == self.search_proxy("Automation-prod")

    ################################## editProxy Popup ##################################################

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
        return self.driver.send_keys("edit_proxy_popup_proxy_name_txt", proxy_name)

    def update_proxy_description(self,proxy_name):
        return self.driver.send_keys("edit_proxy_popup_desc_txt", proxy_name)

    def verify_edit_proxy_popup_cancel_button(self):
        return self.driver.verify_object_string("edit_proxy_popup_cancel_btn")

    def verify_edit_proxy_popup_save_button(self):
        return self.driver.verify_object_string("edit_proxy_popup_save_btn") 

    def click_edit_proxy_popup_cancel_button(self):
        return self.driver.click("edit_proxy_popup_cancel_btn") 

    def click_edit_proxy_popup_save_button(self):
        return self.driver.click("edit_proxy_popup_save_btn")
    
    def get_edit_proxy_popup_proxy_name_text_box_tooltip_msg(self):
        return self.driver.wait_for_object("edit_proxy_popup_proxy_name_tooltip_msg").text
    
    def clear_edit_proxy_popup_proxy_name(self):
        return self.driver.clear_text("edit_proxy_popup_proxy_name_txt")
    
    def click_edit_proxy_popup_proxy_name_text_box(self):
        return self.driver.click("edit_proxy_popup_proxy_name_txt")
    
    def verify_edit_proxy_toast_message(self,proxy_name):
        text = "{} successfully saved."
        expected_alert_message = text.format(proxy_name)
        return self.check_toast_successful_message(expected_alert_message)

    def verify_proxy_setting_tab_status(self,displayed=True):
        return self.driver.wait_for_object("settings_tab",timeout=10,invisible=not displayed)

    ############################# Settings Tab ####################################

    def verify_data_collection_preferences_tab(self):
        return self.driver.wait_for_object("data_collection_preferences_tab", timeout=10)
    
    def click_proxies_settings_help_info_button(self):
        return self.driver.click("proxies_settings_help_info_button")
    
    def click_proxies_settings_help_info_close_button(self):
        return self.driver.click("proxies_settings_help_info_close_button")
    
    def verify_proxies_settings_help_info_popup(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("proxies_settings_help_info_popup", invisible=not displayed)
        return self.driver.wait_for_object("proxies_settings_help_info_popup")

    def verify_proxies_settings_description(self):
        return self.driver.verify_object_string("proxies_settings_description")

    def click_proxies_settings_toggle_button(self):
        return self.driver.click("proxies_settings_tab_toggle_buttons")

    def proxies_settings_search(self, proxy_name, raise_e=True, timeout=10):
        """
            Search proxy name in proxies table
            Should display list of proxies based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("proxies_search_txt",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("proxies_search_txt", proxy_name, press_enter=True)
        
        if self.driver.wait_for_object("proxies_table_no_item_found_lbl",raise_e=False) is not False:
            table_empty=self.driver.wait_for_object("proxies_table_no_item_found_lbl")
            logging.info(table_empty.text)
            return False
        else:
            table_entry_proxies = self.driver.find_object("proxies_settings_table_settings_name",multiple=True)

            for i in range(len(table_entry_proxies)):
                if proxy_name in table_entry_proxies[i].text:
                    logging.info("Proxy Name: " + table_entry_proxies[i].text+ " contains the searched string: " + proxy_name)
                    break
                else:
                    raise SettingsSearchException("Proxy Name: " + table_entry_proxies[i].text+ " does not contain the searched string: " + proxy_name)
        return True
    
    def verify_proxies_settings_table_data_load(self):
        if self.driver.wait_for_object("proxies_settings_tab_toggle_buttons", timeout=30, raise_e=False) is not False:
            return True
        else:
            raise SettingsTableEmpty("Settings table is empty")

    def verify_proxies_settings_category_label(self):
        return self.driver.verify_object_string("proxies_settings_category_label")

    def verify_proxies_settings_search_box(self):
        return self.driver.wait_for_object("proxies_settings_search_box")
    
    def verify_proxies_settings_audit_log_button(self):
        return self.driver.verify_object_string("proxies_settings_audit_log_button")
    
    def verify_proxies_settings_audit_log_button_tooltip_message(self):
        # This method is used for mover hover on audit log button
        ac = ActionChains(self.wdvr)
        obj=self.driver.wait_for_object("proxies_settings_audit_log_button")
        ac.move_to_element(obj).perform()
        return self.driver.verify_object_string("proxies_settings_audit_log_button_tooltip")
    
    def verify_proxies_settings_screen_error_message(self):
        self.driver.verify_object_string("proxies_settings_warning_description_first_part")
        return self.driver.verify_object_string("proxies_settings_warning_description_end_part")

    def verify_proxies_settings_table(self):
        return self.driver.wait_for_object("proxies_settings_table")
    
    def verify_proxies_settings_toggle(self):
        if self.driver.wait_for_object("proxies_settings_tab_toggle_buttons", timeout=30, raise_e=False) is not False:
            return True
        else:
            return False

    def click_proxies_settings_filter_button(self):
        return self.driver.click("proxies_settings_filter_button" ,timeout=30)
    
    def verify_filter_side_bar_status_label(self):
        return self.driver.verify_object_string("filter_side_bar_status_label")
    
    def verify_filter_side_bar_data_collection_label(self):
        return self.driver.verify_object_string("filter_side_bar_data_collection_label")
    
    def verify_functionality_may_be_lost_popup(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("functionality_may_be_lost_popup_title", invisible=not displayed)
        return self.driver.verify_object_string("functionality_may_be_lost_popup_title")
    
    def verify_functionality_may_be_lost_popup_description(self):
        self.driver.verify_object_string("functionality_may_be_lost_popup_desc")
        return self.driver.verify_object_string("functionality_may_be_lost_popup_desc_end_part")
    
    def verify_functionality_may_be_lost_popup_settings_name(self,settings_name):
        assert settings_name == self.driver.wait_for_object("functionality_may_be_lost_popup_settings_name").text
    
    def verify_functionality_may_be_lost_popup_cancel_button(self):
        return self.driver.verify_object_string("functionality_may_be_lost_popup_cancel_btn")

    def verify_functionality_may_be_lost_popup_confirm_button(self):
        return self.driver.verify_object_string("functionality_may_be_lost_popup_confirm_btn") 

    def click_functionality_may_be_lost_popup_cancel_button(self):
        return self.driver.click("functionality_may_be_lost_popup_cancel_btn") 

    def click_functionality_may_be_lost_popup_confirm_button(self):
        return self.driver.click("functionality_may_be_lost_popup_confirm_btn")
    
    def verify_proxies_settings_warning_message(self):
        if self.driver.wait_for_object("proxies_settings_warning_description_first_part", timeout=30, raise_e=False) is not False:
            return True
        else:
            return False
    
    def verify_proxies_settings_warning_icon(self, displayed=True):
        if displayed != True:
            return self.driver.wait_for_object("proxies_settings_warning_icon", invisible=not displayed)
        return self.driver.wait_for_object("proxies_settings_warning_icon")
    
    def click_settings_catagory(self,catagory_name):
        return self.driver.click("settings_catagory_name",format_specifier=[catagory_name],timeout=20)
    
    def get_proxy_settings_names(self):
        proxy_settings = []
        all_settings = self.driver.find_object("proxies_settings_table_settings_name",multiple=True)
        for option in all_settings:
            proxy_settings.append(option.text)
        return proxy_settings
    
    def get_proxies_settings_toggle_button_status(self):
        self.driver.wait_for_object("proxies_settings_toggle_status")
        is_allowed = self.driver.get_attribute("proxies_settings_toggle_status","aria-checked")
        if is_allowed == 'true':
            return True
        return False