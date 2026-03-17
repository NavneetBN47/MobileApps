import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class AccordianExpandException(Exception):
    pass

class CheckBoxException(Exception):
    pass

class AttributeException(Exception):
    pass

class DropDownCannotExpandException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class ReportsSearchException(Exception):
    pass

class Reports(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "reports"

    def verify_reports_page(self, table_load=True):
        if table_load:
            return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        else:
            return self.driver.wait_for_object("_shared_page_header_title", timeout=30)

    def verify_accordian_expand_btn(self):
        return self.driver.wait_for_object("reports_accordian_btn")
    
    def verify_footer_banner(self):
        return self.driver.wait_for_object("reports_footer_banner")

    def verify_download_footer_banner(self):
        return self.driver.wait_for_object("download_footer_banner")

    def verify_download_table_load(self):
        return self.driver.wait_for_object("download_all_body_checkbox", displayed=False)

    def verify_delete_popup_visible(self, visible=True):
        self.verify_confirm_delete_popup()
        if visible:
            return self.driver.get_attribute('reports_delete_popup_modal', "aria-hidden", displayed=False) == "true"
        else:
            return self.driver.get_attribute('reports_delete_popup_modal', "aria-hidden", displayed=False) == "false"
            
    def verify_check_all_state(self, checked=True):
        if checked:
            checked = "true"
        else:
            checked = "false"
        if self.driver.get_attribute("check_all_checkbox", 'aria-checked', displayed=False) != checked:
            raise CheckBoxException("Check all checkbox should be checked: " + checked)    
        return True

    def verify_all_check_box_state(self, checked=True):
        self.verify_check_all_state(checked=checked)
        if checked:
            checked = "true"
        else:
            checked = "false"
        all_check_box = self.driver.find_object("all_accordian_checkboxs", multiple=True)
        for box in all_check_box:
            if box.get_attribute("aria-checked") != checked:
                raise CheckBoxException("Not all check boxes are checked: " + checked)    
        return True

    def verify_download_select_all_status(self, status):
        actual_status = self.driver.get_attribute("download_header_checkbox", "aria-checked", displayed=False)
        if actual_status != status:
            raise CheckBoxException("Header checkbox status expect: " + status + " actual status: " + actual_status)
        return True

    def verify_download_all_checkbox_status(self, status):
        all_table_checkbox = self.driver.find_object("download_all_body_checkbox", multiple=True)
        for box in all_table_checkbox:
            box_attribute = box.get_attribute("aria-checked")
            if box_attribute != status:
                raise CheckBoxException("Checkbox expected status: " + status +" actual status: " + box_attribute)
        return True

    def verify_download_footer(self, total_selected):
        self.driver.wait_for_object("reports_footer_cancel_btn")
        self.driver.wait_for_object("footer_continue_btn")
        selected_label = self.driver.wait_for_object("download_footer_selected_number_lbl").text.split(" ")[0]
        if total_selected != int(selected_label):
            raise AttributeException("Total selected: " + str(total_selected) + " selected_label: " + str(selected_label))
        self.driver.wait_for_object("download_select_next_step_dropdown")
        self.open_select_next_step_dropdown()
        download_focused = self.driver.get_attribute("download_select_next_step_dropdown_download_option", "data-focus")
        if download_focused != "true":
            raise AttributeException("Download option focused: " + download_focused + " expected: " + "true")
        self.driver.wait_for_object("download_select_next_step_dropdown_delete_option")
        return True
    
    def verify_generate_report_footer(self, total_selected):
        self.driver.wait_for_object("reports_footer_cancel_btn")
        self.driver.wait_for_object("footer_continue_btn")       
        selected_label = self.driver.wait_for_object("generate_report_footer_selected_number_lbl").text.split(" ")[0]
        if total_selected != int(selected_label):
            raise AttributeException("Total selected: " + str(total_selected) + " selected_label: " + str(selected_label))   
        return True    

    def verify_confirm_delete_popup(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("reports_delete_popup_delete_btn", timeout=timeout, displayed=False, raise_e=raise_e)

    def select_footer_next_step_dropdown(self, option):
        self.open_select_next_step_dropdown()
        return self.driver.click("download_select_next_step_dropdown_" + option + "_option")

    def generate_report(self, no_items_found_only=False):
        #Generic generate report
        #Param: no_items_found_only -> only generate reports if none are found 
        self.click_download_tab()
        if no_items_found_only:
            no_items_found = self.driver.wait_for_object("_shared_no_items_found_img", timeout=5, raise_e=False)
            if no_items_found is False:
                return True
        self.click_generate_report_tab()
        self.click_check_all_checkbox()
        self.verify_footer_banner()
        self.click_footer_continue()
        return True

    def click_table_checkbox_by_index(self, index):
        return self.driver.find_object("download_all_body_checkbox", index=index).click()

    def check_all_check_box(self):
        #Cannot click normally, need to work around it with wait and displayed=False
        self.click_check_all_checkbox()
        all_check_box = self.driver.find_object("all_accordian_checkboxs", multiple=True)
        for box in all_check_box:
            if box.get_attribute("aria-checked") != "true":
                raise CheckBoxException("Check all checkbox did not check all the boxes")
        return True

    def check_summary_check_box(self, summary_name, checked=True):
        obj_name = summary_name + "_summary_checkbox"
        obj_checked = self.driver.get_attribute(obj_name, "aria-checked", displayed=False) == "true"
        if (obj_checked and checked) or (not obj_checked and not checked):
            return True
        else:
            #Can't use regular click need the displayed = False
            self.driver.wait_for_object(obj_name, displayed=False).click()
            obj_checked = self.driver.get_attribute(obj_name, "aria-checked", displayed=False) == "true"
            if obj_checked != checked:
                raise CheckBoxException("Cannot check checkbox: " + obj_name) 

    def expand_accordian(self, expand=True):
        accordian_is_expand = self.driver.get_attribute("reports_accordian_btn", "aria-expanded") == "true"
        if (accordian_is_expand and expand) or not accordian_is_expand and not expand:
            return True
        else:
            self.driver.click("reports_accordian_btn")
            accordian_is_expand = self.driver.get_attribute("reports_accordian_btn", "aria-expanded") == "true"
            if accordian_is_expand != expand:
                raise AccordianExpandException("Cannot change accordian to expand=" + str(expand))

    def click_delete_popup_btn(self, button):
        return self.driver.js_click("reports_delete_popup_" + button + "_btn", displayed=False)

    def click_check_all_checkbox(self):
        return self.driver.wait_for_object("check_all_checkbox",displayed=False).click()

    def click_footer_cancel(self):
        return self.driver.click("reports_footer_cancel_btn")

    def click_footer_continue(self):
        return self.driver.click("footer_continue_btn")

    def click_download_tab(self):
        return self.driver.click("download_tab",timeout=10)

    def open_select_next_step_dropdown(self, retry=3):
        for _ in range(retry):
            self.driver.click("download_select_next_step_dropdown")
            sleep(1)
            if self.driver.get_attribute("download_select_next_step_dropdown", "aria-expanded")== "true":
                return True
        raise DropDownCannotExpandException("Cannot expand the select next step drop down after: " + str(retry) + " tries")

    def click_generate_report_tab(self):
        return self.driver.click("generate_report_tab")
    
    def click_table_checkbox_by_index(self, index):
        return self.driver.find_object("download_all_body_checkbox", index=index).click()

    def click_table_header_checkbox(self):
        return self.driver.click("download_header_checkbox", displayed=False)
        
    ################################## ECP 0.55 ##################################################

    def verify_reports_search_box(self):
        return self.driver.wait_for_object("reports_serach_txt")

    def verify_reports_generate_button(self):
        return self.driver.verify_object_string("reports_generate_btn")

    def verify_reports_filter_button(self):
        return self.driver.verify_object_string("reports_filter_btn")

    def verify_reports_column_option_gear(self):
        return self.driver.wait_for_object("reports_column_option_gear")

    ################################### Contextual Footer ########################################

    def click_reports_checkbox(self):
        return self.driver.click("reports_table_checkbox",timeout=10)

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("reports_contextual_footer_cancel_btn")

    def verify_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("reports_contextual_footer_cancel_btn",invisible=True)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("reports_contextual_footer_cancel_btn")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.verify_object_string("reports_contextual_footer_selected_item_label")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("reports_contextual_footer_select_action_dropdown")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("reports_contextual_footer_select_action_dropdown")

    def select_contextual_footer_select_action_dropdown_option(self,option):
        options = self.driver.find_object("reports_contextual_footer_select_action_dropdown_options", multiple = True)
        if option == "Save as PDF":
            options[0].click()
        elif option == "Save as XLSX":
            options[1].click()
        elif option == "Edit":
            options[2].click()
        elif option == "Delete":
            options[3].click()

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("reports_contextual_footer_continue_btn")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("reports_contextual_footer_cancel_btn")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("reports_contextual_footer_continue_btn")

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("reports_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    ################################### Generate Report Page ########################################

    def verify_generate_report_title(self):
        return self.driver.verify_object_string("generate_report_title")

    def click_reports_generate_button(self):
        return self.driver.click("reports_generate_btn")

    def verify_reports_table(self,report_name):
        if self.driver.wait_for_object("reports_table_no_reports_label",timeout=20,raise_e=False) is not False:
            self.click_reports_generate_button()
            self.click_report_category_dropdown()
            self.select_report_category_option("security")
            self.click_report_type_dropdown()
            self.select_report_type_option("executiveSummary")
            self.enter_report_name(report_name)
            self.select_device_group("All")
            self.click_select_device_group_select_button()
            self.click_generate_button()
            #Two toast are present at same time, which is causing stale element reference
            self.dismiss_toast()
            self.dismiss_toast()
        else:
            return True

    def select_device_group(self,group_name):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("select_device_group_btn", timeout=10))
        self.driver.click("select_device_group_btn")
        return self.driver.click("select_device_group_group_name",format_specifier=[group_name],timeout=10)

    def click_select_device_group_select_button(self):
        return self.driver.click("select_device_group_select_btn")

    def click_generate_button(self):
        return self.driver.click("generate_report_generate_btn")

    def verify_generate_report_toast_message(self,report_name):
        text = "Generating {} completed successfully."
        expected_alert_message= text.format(report_name)
        return self.check_toast_successful_message(expected_alert_message)
    
    def click_report_category_dropdown(self):
        return self.driver.click("generate_report_category_dropdown", timeout=20)

    def select_report_category_option(self,option):
        return self.driver.click("generate_report_select_category_dropdown_option",format_specifier=[option])
    
    def click_report_type_dropdown(self):
        return self.driver.click("generate_report_type_dropdown", timeout=30)

    def select_report_type_option(self,option):
        return self.driver.click("generate_report_select_type_dropdown_option",format_specifier=[option])
	
    def verify_report_category_dropdown_title(self):
        return self.driver.verify_object_string("generate_report_category_title")

    def verify_report_category_dropdown(self):
        return self.driver.wait_for_object("generate_report_category_dropdown")
    
    def verify_report_type_dropdown_title(self):
        return self.driver.verify_object_string("generate_report_type_title")

    def verify_report_type_dropdown(self,status):
        if status == True:
            if self.driver.get_attribute("generate_report_type_dropdown","aria-disabled") == "true":
                raise UnexpectedItemPresentException("Report type dropdown is disabled")
            return True
        else:
            if self.driver.get_attribute("generate_report_type_dropdown","aria-disabled") == "false":
                raise UnexpectedItemPresentException("Report type dropdown is enabled")
            return True
    
    def verify_report_name_title(self):
        return self.driver.verify_object_string("generate_report_name_title")
    
    def verify_report_name_field(self):
        return self.driver.wait_for_object("edit_report_report_name_txt")
    
    def verify_device_group_title(self):
        return self.driver.verify_object_string("generate_report_device_group_title")

    def verify_device_group_decription(self):
        return self.driver.verify_object_string("generate_report_device_group_decription")

    def verify_select_device_group_button(self):
        return self.driver.verify_object_string("select_device_group_btn")   
    
    def verify_schedule_time_option_title(self):
        return self.driver.verify_object_string("generate_report_schedule_time_option_title")
    
    def verify_schedule_email_option_title(self):
        return self.driver.verify_object_string("generate_report_schedule_email_option_title")
    
    def verify_generate_report_page_cancel_button(self):
        return self.driver.wait_for_object("generate_report_cancel_btn")
        
    def verify_generate_report_page_generate_button(self):
        return self.driver.wait_for_object("generate_report_generate_btn")  
    
    def verify_report_category_dropdown_options(self,displayed=True):
        return self.driver.wait_for_object("generate_report_select_category_dropdown_options", invisible=not displayed)
    
    def get_generate_report_category_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("generate_report_select_category_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
        
    def verify_generate_report_category_deployment_option(self,status):
        self.driver.wait_for_object("report_category_dropdown_deployment_option")
        if status == True:
            if self.driver.get_attribute("report_category_dropdown_deployment_option","aria-disabled") == "true":
                raise UnexpectedItemPresentException("Deployment option is disabled")
            return True
        else:
            if self.driver.get_attribute("report_category_dropdown_deployment_option","aria-disabled") == "false":
                raise UnexpectedItemPresentException("Deployment option is enabled")
            return True

    def verify_generate_report_category_roam_for_business_option(self,status):
        self.driver.wait_for_object("report_category_dropdown_business_option")
        if status == True:
            if self.driver.get_attribute("report_category_dropdown_business_option","aria-disabled") == "true":
                raise UnexpectedItemPresentException("Roam for Business option is disabled")
            return True
        else:
            if self.driver.get_attribute("report_category_dropdown_business_option","aria-disabled") == "false":
                raise UnexpectedItemPresentException("Roam for Business option is enabled")
            return True

    def verify_generate_report_category_security_option(self,status):
        self.driver.wait_for_object("report_category_dropdown_security_option")
        if status == True:
            if self.driver.get_attribute("report_category_dropdown_security_option","aria-disabled") == "true":
                raise UnexpectedItemPresentException("Security option is disabled")
            return True
        else:
            if self.driver.get_attribute("report_category_dropdown_security_option","aria-disabled") == "false":
                raise UnexpectedItemPresentException("Security option is enabled")
            return True 
        
    def get_generate_report_type_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("generate_report_select_type_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def verify_report_type_dropdown_options(self,displayed=True):
        return self.driver.wait_for_object("generate_report_select_type_dropdown_options", invisible=not displayed)
    
    def verify_report_view_sample_button(self,status):
        if status == "disabled":
            if self.driver.wait_for_object("generate_report_view_sample_button").is_enabled():
                raise UnexpectedItemPresentException(" Edit Report Contextual Save Button is enabled")
            return True
        else:
            if self.driver.wait_for_object("generate_report_view_sample_button").is_enabled() is False:
                raise UnexpectedItemPresentException(" Edit Report Contextual Save Button is disabled")
            return True
    
    def click_report_view_sample_button(self):
        return self.driver.click("generate_report_view_sample_button",timeout=20)

    def verify_generate_sample_report_page(self):
        return self.driver.wait_for_object("sample_report_page",timeout=30)
    
    def click_generate_sample_report_page_cancel_button(self):
        return self.driver.click("sample_report_page_cancel_button")

    def verify_sample_report_page_title(self,expected_title):
        page_title = self.driver.get_text("sample_report_page_title")
        actual_report_title = (page_title.split(": ")[1]).strip()
        assert actual_report_title == expected_title

    def click_reports_select_device_group(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("select_device_group_btn", timeout=10))
        return self.driver.click("select_device_group_btn")
    
    def verify_reports_select_device_group_popup(self):
        return self.driver.wait_for_object("select_device_group_popup_title", timeout=20)
    
    def verify_reports_select_device_group_popup_title(self):
        return self.driver.verify_object_string("select_device_group_popup_title",timeout=20)

    def verify_reports_select_device_group_popup_description(self):
        return self.driver.verify_object_string("select_device_group_popup_decription")

    def verify_reports_select_device_group_popup_cancel_button(self):
        return self.driver.wait_for_object("select_device_group_cancel_btn")

    def verify_reports_select_device_group_popup_select_button(self,status):
        deployment_option = self.driver.wait_for_object("select_device_group_select_btn")
        if status == "disabled":
            if deployment_option.is_enabled():
                raise UnexpectedItemPresentException("Select button is enabled")
            return True
        else:
            if not deployment_option.is_enabled():
                raise UnexpectedItemPresentException("Select button is disabled")
            return True
        
    def click_reports_device_group_popup_cancel_button(self):
        return self.driver.click("select_device_group_cancel_btn")

    def verify_report_category_warning_message(self):
        return self.driver.verify_object_string("generate_report_category_warning_message")

    def verify_report_type_warning_message(self):
        return self.driver.verify_object_string("generate_report_type_warning_message")
        
    def verify_device_group_warning_message(self):
        return self.driver.verify_object_string("generate_report_device_group_warning_message")
    
    def verify_report_name_field_empty_warning_message(self):
        return self.driver.verify_object_string("generate_report_name_field_empty_warning_message")
    
    def verify_report_name_field_error_warning_message(self):
        return self.driver.verify_object_string("generate_report_name_field_error_warning_message")
    
    def click_generate_report_page_cancel_button(self):
        return self.driver.click("generate_report_cancel_btn")  
    
    ####################################### Edit Report Page ########################################

    def verify_edit_report_title(self):
        return self.driver.verify_object_string("edit_report_title")

    def verify_edit_report_descriptopn(self):
        return self.driver.verify_object_string("edit_report_desc")

    def enter_report_name(self,report_name):
        return self.driver.send_keys("edit_report_report_name_txt",report_name)

    def verify_edit_report_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("edit_report_contextual_cancel_btn")

    def verify_edit_report_contextual_footer_save_button(self):
        return self.driver.verify_object_string("edit_report_contextual_save_btn")

    def verify_edit_report_save_button_status(self,status):
        if status == "disabled":
            if self.driver.find_object("edit_report_contextual_save_btn").is_enabled():
                raise UnexpectedItemPresentException(" Edit Report Contextual Save Button is enabled")
            return True
        else:
            if self.driver.find_object("edit_report_contextual_save_btn").is_enabled() is False:
                raise UnexpectedItemPresentException(" Edit Report Contextual Save Button is disabled")
            return True

    def click_edit_report_contextual_footer_cancel_button(self):
        return self.driver.click("edit_report_contextual_cancel_btn")

    def click_edit_report_contextual_footer_save_button(self):
        return self.driver.click("edit_report_contextual_save_btn")

    def verify_edit_report_toast_message(self,report_name):
        text = "Editing {} successfully completed."
        expected_alert_message= text.format(report_name)
        return self.check_toast_successful_message(expected_alert_message)

    def verify_edit_report_category_title(self):
        return self.driver.verify_object_string("edit_report_category_title")

    def verify_edit_report_category_type(self,expected_category_type):
        actual_category_type = self.driver.get_text("edit_report_category_type_value")
        assert actual_category_type == expected_category_type
    
    def verify_edit_report_type_title(self):
        return self.driver.verify_object_string("edit_report_type_title")

    def verify_edit_report_type(self,expected_report_type):
        actual_report_type = self.driver.get_text("edit_report_type_value")
        assert actual_report_type == expected_report_type
    
    def verify_edit_report_name_field_title(self):
        return self.driver.verify_object_string("edit_report_name_title")
    
    def verify_edit_report_name_field(self,expected_report_name):
        expected_report_name = self.driver.get_text("edit_report_report_name_txt")
        assert expected_report_name == expected_report_name
    
    def verify_edit_report_device_group_title(self):
        return self.driver.verify_object_string("edit_report_device_group_title")
        
    def verify_edit_report_contextual_footer(self):
        return self.driver.wait_for_object("edit_report_contextual_footer")
    
    def clear_report_name_field(self):
        return self.driver.clear_text("edit_report_report_name_txt")
    
    def verify_edit_report_name_field_empty_warning_message(self):
        return self.driver.verify_object_string("edit_report_name_field_empty_warning_message",timeout=30)

    def verify_edit_report_name_field_error_warning_message(self):
        return self.driver.verify_object_string("edit_report_name_field_error_warning_message")        

    ####################################### Delete Report Popup ########################################

    def verify_delete_report_popup_title(self):
        return self.driver.verify_object_string("delete_report_popup_title")

    def verify_delete_report_popup_descriptopn(self):
        return self.driver.verify_object_string("delete_report_popup_desc")

    def verify_delete_report_popup_cancel_button(self):
        return self.driver.verify_object_string("delete_report_popup_cancel_btn")

    def verify_delete_report_popup_delete_button(self):
        return self.driver.verify_object_string("delete_report_popup_delete_btn")

    def click_delete_report_popup_cancel_button(self):
        return self.driver.click("delete_report_popup_cancel_btn")

    def click_delete_report_popup_delete_button(self):
        return self.driver.click("delete_report_popup_delete_btn")

    def verify_delete_report_toast_message(self,no_of_report):
        text = "Deleting {} reports successfully completed." 
        expected_alert_message = text.format(no_of_report)
        return self.check_toast_successful_message(expected_alert_message)

    ####################################### Report Details ########################################

    def get_reports_table_entry_details(self):
        device_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        device_info["report_name"] = all_fields[1].text.lower()
        device_info["report_type"] = all_fields[3].text.lower()
        device_info["report_generated"] = all_fields[4].text.lower()
        return device_info   

    def verify_report_details(self):
        details_info = {}
        details_info["report_name"] = self.driver.wait_for_object("report_details_report_name",timeout=30).text.lower()
        details_info["report_type"] = self.driver.wait_for_object("report_details_report_type").text.lower()
        details_info["report_generated"] = self.driver.wait_for_object("report_details_report_generated").text.lower()
        return details_info

    def search_report(self, report_name, raise_e=True, timeout=10):
        # 
        self.driver.wait_for_object("reports_serach_txt",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("reports_serach_txt", report_name,press_enter=True)
        if self.driver.wait_for_object("reports_table_no_item_found_lbl",raise_e=False) is not False:
            table_entry_reports=self.driver.wait_for_object("reports_table_no_item_found_lbl")
            logging.info(table_entry_reports.text)
            return False
        else:
            table_entry_reports = self.driver.find_object("reports_table_report_name_lbl",multiple=True)
            for i in range(len(table_entry_reports)):
                if report_name.lower() in table_entry_reports[i].text.lower():
                    logging.info("Report Name: " + table_entry_reports[i].text+ " contains the searched string: " + report_name)
                    return True
                else:
                    if raise_e:
                        raise ReportsSearchException("Report Name: " + table_entry_reports[i].text+ " does not contain the searched string: " + report_name)
                    else:
                        return False
                    
    def click_search_clear_button(self):
        return self.driver.click("reports_clear_search_button")

    ################################## Column Options Popup ##################################################

    def click_reports_column_option_settings_gear_button(self):
        return self.driver.click("reports_column_option_gear")

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
        if option == "Report Name":
            options[0].click()
        elif option == "Category":
            options[1].click()
        elif option == "Report Type":
            options[2].click()
        elif option == "Date Generated":
            options[3].click()
        elif option == "Status":
            options[4].click()

    def verify_customers_tabel_column(self,column_name,displayed=True):
        if column_name == "Report Name":
                return self.driver.wait_for_object("reports_table_report_name_column", invisible=not displayed)
        elif column_name == "Category":
                return self.driver.wait_for_object("reports_table_catagory_column", invisible=not displayed)
        elif column_name == "Report Type":
                return self.driver.wait_for_object("reports_table_report_type_column", invisible=not displayed)
        elif column_name == "Date Generated":
                return self.driver.wait_for_object("reports_table_date_generated_column", invisible=not displayed)
        elif column_name == "Status":
                return self.driver.wait_for_object("reports_table_status_column", invisible=not displayed)

##########################################Reports details page#############################################

    def get_reports_list_report_type_value(self):
        # return self.driver.get_text("report_list_report_type_value")
        report_type = self.get_header_index("report_type")
        report_type_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[report_type],multiple=True)
        for index in range(len(report_type_list)):
            actual_report_type = self.driver.get_text("report_list_report_type_value")
        return actual_report_type
    
    def get_reports_list_generated_date_value(self):
        # return self.driver.get_text("report_list_generated_date_value")
        date_generated = self.get_header_index("date_generated")
        date_generated_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[date_generated],multiple=True)
        for index in range(len(date_generated_list)):
            actual_date_generated = self.driver.get_text("report_list_generated_date_value")
        return actual_date_generated
    
    def get_report_details_report_title(self):
        self.driver.wait_for_object("report_details_report_title",timeout=40)
        return self.driver.get_text("report_details_report_title")
    
    def get_report_details_report_type_value(self):
        return self.driver.get_text("report_details_report_type_value")
    
    def get_report_details_page_generated_date_value(self):
        return self.driver.get_text("report_details_page_generated_date_value")

    def get_report_details_page_customer_name(self):
        return self.driver.get_text("report_details_page_customer_name").strip()
    
    def verify_report_details_page_save_as_pdf_button(self):
        return self.driver.verify_object_string("report_details_page_pdf_button")
    
    def verify_report_details_page_save_as_xlsx_button(self):
        return self.driver.verify_object_string("report_details_page_xlsx_button")
    
    def click_report_details_page_summary_card(self):
        return self.driver.click("report_details_page_summary_card")

    def verify_report_details_page_summary_card_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_page_summary_card")
        is_expanded = self.driver.get_attribute("report_details_page_summary_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
    
    def click_report_details_page_device_assessment_summary_card(self):
        return self.driver.click("report_details_page_device_assessment_summary_card")

    def verify_report_details_page_device_assessment_summary_card_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_page_device_assessment_summary_card")
        is_expanded = self.driver.get_attribute("report_details_page_device_assessment_summary_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'    
    
    def click_report_details_page_policy_items_assessed_card(self):
        return self.driver.click("report_details_policy_items_assessed_card")

    def verify_report_details_page_policy_items_assessed_card_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_policy_items_assessed_card")
        is_expanded = self.driver.get_attribute("report_details_policy_items_assessed_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
    
    def click_report_details_page_risk_summary_card_card(self):
        return self.driver.click("report_details_page_risk_summary_card")

    def verify_report_details_page_risk_summary_card_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_page_risk_summary_card")
        is_expanded = self.driver.get_attribute("report_details_page_risk_summary_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
    
    def click_report_details_page_solutions_entitled_card(self):
        return self.driver.click("report_details_page_solutions_entitled_card")

    def verify_report_details_page_solutions_entitled_card_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_page_solutions_entitled_card")
        is_expanded = self.driver.get_attribute("report_details_page_solutions_entitled_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
    
    def verify_report_details_page_device_assessment_summary_card_component(self):
        return self.driver.verify_object_string("assessment_summary_card_title")
    
    def verify_device_assessment_summary_card_assessed_device_status_title(self):
        return self.driver.verify_object_string("assessed_device_status_title")
    
    def verify_device_assessment_summary_card_not_assessed_device_status_title(self):
        return self.driver.verify_object_string("not_assessed_device_status_title")

    def verify_report_details_page_policy_items_assessed_card_component(self):
        return self.driver.verify_object_string("policy_items_assessed_card_title")
    
    def verify_policy_items_assessed_status_by_policy_items_title(self):
        return self.driver.verify_object_string("assessed_status_by_policy_items_title")
    
    def verify_policy_items_assessed_status_by_feature_category_title(self):
        return self.driver.verify_object_string("assessed_status_by_feature_category_title")

    def verify_report_details_page_risk_summary_card_component(self):
        return self.driver.verify_object_string("risk_summary_card_title")
    
    def verify_report_details_page_solutions_entitled_card_component(self):
        return self.driver.verify_object_string("solutions_entitled_card_title")
    
    def verify_reports_details_page_assessment_status_list_table(self):
        return self.driver.wait_for_object("reports_details_assessment_status_list_table")
    
    def verify_reports_details_page_search_field(self):
        return self.driver.wait_for_object("reports_details_search_field")

    def verify_reports_details_page_filter_button(self):
        return self.driver.wait_for_object("reports_details_filter_button")

    def verify_reports_details_page_column_option_button(self):
        return self.driver.wait_for_object("reports_details_column_option_button")

    def verify_policy_items_assessed_count_title(self):
        return self.driver.verify_object_string("policy_items_count_title")

    def click_report_details_page_policy_items_assessed_count_card(self):
        return self.driver.click("report_details_policy_items_count_card")
    
    def verify_report_details_page_policy_items_assessed_count_expanded(self,expanded=True):
        self.driver.wait_for_object("report_details_policy_items_count_card")
        is_expanded = self.driver.get_attribute("report_details_policy_items_count_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_job_summary_card_title(self):
        return self.driver.click("job_summary_card_title")

    def verify_job_summary_card_title(self):
        return self.driver.verify_object_string("job_summary_card_title")
    
    def verify_job_summary_card_expanded(self,expanded=True):
        self.driver.wait_for_object("job_summary_card_title")
        is_expanded = self.driver.get_attribute("job_summary_card_title","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def verify_reports_details_page_job_summary_table(self):
        return self.driver.wait_for_object("reports_details_assessment_status_list_table")