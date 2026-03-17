import time
import logging
from time import sleep

from time import sleep
from datetime import datetime,timedelta
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow
from SAF.misc import saf_misc
from itertools import groupby 
class WrongToastException(Exception):
    pass

class NoPrinterException(Exception):
    pass

class CannotFindTaskException(Exception):
    pass

class PolicyNameChangeFailedException(Exception):
    pass

class StringComparisonException(Exception):
    pass

class DateComparisonException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class TaskStatusNotExpected(Exception):
    pass

class CannotFindPolicyException(Exception):
    pass

class CannotFindLanguageOptionException(Exception):
    pass

class IncorrectSortException(Exception):
    pass

class PolicyNoncompliantException(Exception):
    pass

class CannotFindPolicySettingsTypeException(Exception):
    pass

class SettingValueMismatchException(Exception):
    pass

class DropDownCannotExpandException(Exception):
    pass

class EndpointSecurity(ECPFlow):
    flow_name = "endpoint_security"

    total_online_devices = 0
    total_offline_devices = 0

    # Following variavles are permission option index, used for permission dropdown.
    READ_ONLY=0
    READ_WRITE=1
    DISABLE=2

    def return_section_div(self, section):
        return self.driver.wait_for_object(section + "_section")
    
    def select_security_trends_dropdown(self,option_name):
        self.driver.click("overview_security_trends_dropdown",timeout=40)
        sleep(10)
        options = self.driver.find_object("overview_security_trends_dropdown_options",multiple=True)
        if option_name == "Last 24 hours":
            options[0].click()
        elif option_name == "Last 7 days":
            options[1].click()
        elif option_name == "Last 30 days":
            options[2].click()
        return self.verify_status_content("status_content")
    
    def click_entitled_devices(self):
        return self.driver.click("entitled_devices")
    
    def click_devices_tab(self):
        return self.driver.click("devices_tab",timeout=10)
    
    def click_policies_tab(self):
        return self.driver.click("policies_tab",timeout=10)

    def click_tasks_tab(self):
        return self.driver.click("tasks_tab")

    def click_export_all(self):
        return self.driver.click("export_all_button", timeout=10)
    
    def click_cancel_button(self):
        return self.driver.click("cancel_button")
    
    def click_export_button(self):
        return self.driver.click("submit_button")
    
    def get_all_entitled_devices(self):
        for _ in range(6):
            try:
                int(self.driver.wait_for_object("total_online_devices").text)
            except ValueError:
                logging.debug("The number hasn't loaded yet")
                sleep(5)
        self.total_online_devices = int(self.driver.wait_for_object("total_online_devices").text)
        self.total_offline_devices = int(self.driver.wait_for_object("total_offline_devices").text)
    
    def get_devices_detail_info(self):
        device_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        device_info["model_name"] = all_fields[0].text
        device_info["assessment"] = all_fields[1].text
        device_info["connectivity_status"] = all_fields[3].text
        device_info["serial_number"] = all_fields[4].text
        return device_info
    
    def run_task_by_name(self, task_name, task_state=True):
        #param: task_state - True -> start the task, if the task is scheduled then cancel first then start
        #                    False -> End the task, if the task has not been started then start it first then cancel it
        self.verify_table_loaded(timeout=10)
        all_tasks = self.driver.find_object("_shared_table_entries", multiple=True)

        for task in all_tasks:
            if task_name in task.text:
                all_fields = self.driver.find_object("_shared_table_entry_all_cols", multiple=True, root_obj=task)
                status = all_fields[1].text
                if (status == "Idle" and not task_state) or (status in ["Scheduled", "In progress"] and task_state):
                    #This cancels previously incorrect state
                    self.change_task_state()
                    self.dismiss_toast()
                #Change the state
                self.change_task_state()
                if task_state:
                    self.check_toast_successful_message("The task has been started successfully.")
                    #self.driver.wdvr.refresh()
                    self.verify_table_loaded(timeout=5)
                    if self.get_task_status_by_name(task_name).lower() == "idle":
                        raise TaskStatusNotExpected(f"After starting {task_name} the status of the status is still idle")
                else:
                    self.check_toast_successful_message("The task has been canceled successfully.")
                    self.driver.wdvr.refresh()
                    self.verify_table_loaded(timeout=5)
                    if self.get_task_status_by_name(task_name).lower() != "idle":
                        raise TaskStatusNotExpected(f"After canceling {task_name} the status of the status is not idle")                    
                return True
        raise CannotFindTaskException("Cannot find the task: " + task_name)

    def get_task_status_by_name(self, task_name, raise_e=False):
        self.verify_table_loaded(timeout=10)
        all_tasks = self.driver.find_object("_shared_table_entries", multiple=True)
        for task in all_tasks:
            if task_name in task.text:
                return self.driver.find_object("_shared_table_all_col_by_index", format_specifier=["2"], root_obj=task).text    
        else:
            if raise_e:
                raise TaskStatusNotExpected(f"Could not find the task {task_name}")
            else:
                return ""
            

    def verify_task_status_by_name(self, task_name, expected_status, timeout=60, raise_e=True):
        timeout_t = time.time() + timeout
        while timeout_t > time.time():
            self.driver.wdvr.refresh()
            time.sleep(5)
            cur_status = self.get_task_status_by_name(task_name)
            if cur_status.lower() == expected_status.lower():
                return True

        if raise_e:
            raise TaskStatusNotExpected(f"Task '{task_name}' status did not change to {expected_status} after {timeout} seconds")
        else:
            return False

    def select_reports_dropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("reports_dropdown", timeout=30))
        return self.driver.click("reports_dropdown", timeout=10)

    def change_task_state(self):
        self.driver.click("three_dot_menu")
        self.driver.click("floating_button")

    def click_task_by_name(self, task_name):
        all_tasks = self.driver.find_object("_shared_table_entries", multiple=True)
        for task in all_tasks:
            if task_name in task.text:
                task_col =self.driver.find_object("_shared_table_entry_all_cols", multiple=True, root_obj=task)[0]
                return self.driver.click("_shared_table_entry_col_link", root_obj=task_col)
        raise CannotFindTaskException("Cannot find the task: " + task_name)

    def click_task_history_button(self):
        self.driver.click("task_history_button")

    def click_rename_button(self):
        return self.driver.click("polities_pencil_btn")

    def change_policy_name(self, new_policy_name):
        self.click_rename_button()
        self.verify_policies_rename_popup()
        self.driver.send_keys("policies_rename_txt", new_policy_name, press_enter=True)
        self.driver.click("policies_rename_popup_rename_btn")

    def get_policy_name(self):
        return self.driver.wait_for_object("policies_detail_title").text
    
    def click_apply_task_to_dropdown_option(self):
        self.driver.click("apply_task_dropdown")
        return self.driver.click("apply_task_dropdown_option")
    
    def change_task_type(self): 
        assess_only = self.driver.find_object("task_type_assess_only")
        assess_and_remediate = self.driver.find_object("task_type_assess_and_remediate")
        if assess_only.is_selected():
            assess_and_remediate.click()
        else:
            assess_only.click()
    
    def click_task_change_save_button(self):
        return self.driver.click("task_change_save_button")

    def click_task_change_cancel_button(self):
        return self.driver.click("task_change_cancel_button")
    
    def get_task_type_from_task_table(self):
        return self.driver.wait_for_object("task_table_task_type").text

    def get_task_type_from_task_details_page(self):
        assess_only = self.driver.find_object("task_type_assess_only")
        assess_and_remediate = self.driver.find_object("task_type_assess_and_remediate")
        if assess_only.is_selected():
            selected_tasktype = assess_only.get_attribute("value")
        else:
            selected_tasktype = assess_and_remediate.get_attribute("value")

    def click_snmpv3_policy_settings(self):
        return self.driver.click("policy_settings_snmpv3_accordion") 

    def enable_snmpv3_setting(self):
        is_enabled = self.driver.get_attribute("policy_settings_snmpv3_toggle","aria-checked")
        if is_enabled == 'false':
            return self.driver.click("policy_settings_snmpv3_toggle")
        return True   

    def enable_account_lockout(self):
        is_enabled = self.driver.get_attribute("policy_account_lockout_toggle","aria-checked")
        if is_enabled == 'false':
            return self.driver.js_click("policy_account_lockout_toggle")
        return True
       
    def enter_maximum_attempts(self,attempts):
        return self.driver.send_keys("policy_max_attempts_txt", attempts)

###################################### Verifys #######################################
    def verify_next_and_prev_nav(self):
        self.click_next_nav()
        self.verify_table_displaying_correctly_new(25)
        self.click_prev_nav()
        self.verify_table_displaying_correctly_new(25)

    def verify_policy_name_change(self, new_policy_name):
        current_policy_name = self.get_policy_name()
        self.change_policy_name(new_policy_name)
        changed_policy_name = self.get_policy_name()
        self.change_policy_name(current_policy_name)

        if changed_policy_name != new_policy_name:
            raise PolicyNameChangeFailedException("The policy name change failed! Expected -> " + new_policy_name + " Actual -> " + changed_policy_name)
        else:
            return True

    def verify_endpoint_security(self):
        return self.driver.wait_for_object("endpoint_security_title")

    def click_hp_secure_fleet_manager(self,timeout=30):
        return self.driver.click("solutions_secure_fleet_manager",timeout=timeout)

    def verify_security_dashboard(self,title,timeout=30):
        return self.driver.wait_for_object(title,timeout=timeout)
    
    def verify_security_trend_loaded(self):
        return self.driver.wait_for_object('overview_security_trends_assessment_rate', timeout=10)

    def verify_security_trend_dropdown_current_option(self,expect_option):
        current_option = self.driver.wait_for_object("overview_security_trends_dropdown").text
        return current_option == expect_option
    
    def verify_status_content(self,status_content,timeout=5):
        return self.driver.wait_for_object(status_content,timeout=timeout)
    
    def verify_selected_tab(self,tab_name):
        selected_option = self.driver.wait_for_object(tab_name).get_attribute("aria-selected")
        assert selected_option == 'true'

    def verify_devices_detail_loaded(self):
        return self.driver.wait_for_object("details_device_title", timeout=10)

    def verify_status_devices(self):
        online_devices = 0
        offline_devices = 0
        self.driver.wait_for_object("_shared_table_entries",timeout=10)
        rows = self.driver.find_object("_shared_table_entries",multiple=True)
        for row in rows:
            s = row.text
            # row_content = s.split("\n")
            if('Online' in s):
                online_devices+=1
            if('Offline' in s):
                offline_devices+=1
        assert online_devices == self.total_online_devices
        assert offline_devices == self.total_offline_devices

    def search_device(self,search_keys):
        return self.driver.send_keys("_shared_search_box",search_keys,slow_type=True, press_enter=True)
    
    def verify_export_popup(self):
        return self.driver.wait_for_object("export_popup_window")

    def check_toast_successful_message(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_message").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)
        
    def dismiss_toast_successful_message(self):
        return self.driver.click("bottom_toast_dismiss_button")

    def check_toast_successful_msg(self, expected_message):
        actual_message = self.driver.wait_for_object("bottom_toast_msg").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)


    def verify_devices_details_list_synced_with_device_tab(self):
        details_info = {}
        self.verify_devices_detail_loaded()

        details_info["model_name"] = self.driver.wait_for_object("details_device_title").text
        details_info["assessment"] = self.driver.wait_for_object("details_device_assessment_status").text
        details_info["connectivity_status"] = self.driver.wait_for_object("details_device_status").text
        details_info["serial_number"] = self.driver.wait_for_object("details_device_serial").text
        return details_info
    
    def verify_refresh_device_tab_functionality(self):
        cur_time = self.get_sync_time_info()
        sleep(1)
        self.click_refresh_button()
        self.verify_table_loaded()
        new_time = self.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def verify_refresh_device_detail_functionality(self):
        cur_time = self.get_sync_time_info()
        sleep(1)
        self.click_refresh_button()
        self.verify_devices_detail_loaded()
        new_time = self.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def verify_reports_dropdown_options(self):
        return self.driver.wait_for_object("reports_dropdown_options",timeout=15)

    def verify_task_history_modal(self):
        return self.driver.wait_for_object("history_popup_label")

    def verify_policies_rename_popup(self):
        return self.driver.wait_for_object("policies_rename_popup")
    
    def verify_apply_task_default_dropdown_value(self):
        expected_default_text = "All Devices"
        actual_default_text = self.driver.wait_for_object("apply_task_dropdown_default_value").text
        self.compare_strings(expected_default_text, actual_default_text)
    
    def verify_max_attempts_error_icon(self):
        return self.driver.wait_for_object("policy_max_attempts_error_icon")

    def verify_max_attempt_invalid_error_message(self):
        expected_error_message="Requires an integer value from 3 to 30."
        actual_error_message=self.driver.get_text("policies_max_attempts_error_label")  
        self.compare_strings(expected_error_message, actual_error_message)

    def verify_save_button_is_disabled(self):
        if self.driver.find_object("policy_settings_save_button").is_enabled():
            raise UnexpectedItemPresentException("Save button is enabled")
        return True 
    
###################################### Asserts ####################################
    def assert_total_devices(self):
        self.driver.wait_for_object("graph_devices",timeout=10)
        devices = self.driver.find_object("graph_devices",multiple=True)
        assert int(self.driver.find_object("total_graph_devices").text.split(" ")[1]) == int(devices[0].text)+int(devices[1].text)

################################## Reports ########################################

    def select_report(self, option):
        # self.driver.wait_for_object("reports_dropdown_area",timeout=30)  # Dropdown area removed from the UI, So commenting this line
        self.select_reports_dropdown()
        sleep(5)
        return self.driver.click("select_device_" + option + "_option",timeout=30)
    
    def verify_device_report_type(self,report_type):
        if report_type == "assessment":
            return self.driver.verify_object_string("device_assessment_report_type",timeout=15)
        else:
            return self.driver.verify_object_string("device_remediation_report_type",timeout=15)

    def verify_device_report_description(self):
        return self.driver.verify_object_string("device_report_desc")
        
    def verify_details_report_loaded(self):
        return self.driver.wait_for_object("report_date",timeout=15,raise_e=False)

    def verify_details_report_dropdown_default_option(self,expect_option):
        default_option = self.driver.wait_for_object("device_details_detail_report_dropdown").text
        assert default_option == expect_option
    
    def verify_details_report_dropdown_options(self,expected_options):
        actual_options = []
        self.driver.click("device_details_detail_report_dropdown",timeout=10)
        all_options = self.driver.find_object("overview_security_trends_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        assert expected_options == actual_options

    def select_details_report_timeframe_dropdown(self,option_name):
        self.driver.click("device_details_detail_report_dropdown",timeout=20)
        options = self.driver.find_object("overview_security_trends_dropdown_options",multiple=True)
        if option_name == "Last 7 days":
            options[1].click()
        elif option_name == "Last 30 days":
            options[2].click()
        elif option_name == "Last 1 day":                                                        
            options[0].click()
        return self.verify_details_report_loaded()

    def verify_report_content_expanded(self):
        is_expanded = self.driver.get_attribute("report_content","aria-expanded")
        assert is_expanded == 'true'

    def verify_report_content_collapsed(self):
        is_expanded = self.driver.get_attribute("report_content","aria-expanded")
        assert is_expanded == 'false'

    def click_report_content(self):
        return self.driver.click("report_content")


################################### Export Report Pop-up ########################################   
    def click_device_report_export_btn(self):
        self.driver.click("device_report_export_btn")

    def verify_device_remediation_details_popup_title(self, title):
        actual_title = self.driver.wait_for_object("export_popup_title").text
        if actual_title == title:
            return True
        else:
            raise StringComparisonException("Device Remediation Details popup title mismatch, expected title text: "+title+ " actual title text: "+actual_title)

    def verify_device_assessment_details_popup_title(self, title):
        actual_title = self.driver.wait_for_object("export_popup_title").text
        if actual_title == title:
            return True
        else:
            raise StringComparisonException("Device Remediation Details popup title mismatch, expected title text: "+title+ " actual title text: "+actual_title)

    def verify_export_popup_subtitle(self):
        actual_subtitle = self.driver.wait_for_object("export_popup_subtitle").text
        expected_subtitle = 'Select a file format you would like to use for your exported report. Once completed, your file will appear in the "Downloads" menu.'
        if actual_subtitle == expected_subtitle:
            return True
        else:
            raise StringComparisonException("Export popup subtitle mismatch, expected subtitle text: "+expected_subtitle+ " actual subtitle text: "+actual_subtitle)

    def verify_export_popup_default_format(self, expected_format):
        actual_format = self.driver.wait_for_object("export_popup_format_dropdown").text
        if actual_format == expected_format:
            return True
        else:
            raise StringComparisonException("Default format mismatch, expected format: "+expected_format+"actual format: "+actual_format)
    
    def click_export_popup_format_dropdown(self):
        self.driver.click("export_popup_format_dropdown")

    def verify_export_popup_cancel_button(self):
        return self.driver.wait_for_object("cancel_button")

    def verify_export_popup_export_button(self):
        return self.driver.wait_for_object("submit_button")

    def verify_export_dialog_popup(self, option):
        if option == "assessment":
            self.verify_device_assessment_details_popup_title("Export Device Assessment Details")
        elif option == "remediation":
            self.verify_device_remediation_details_popup_title("Export Device Remediation Details")
        self.verify_export_popup_subtitle()
        self.verify_export_popup_default_format("PDF")
        self.click_export_popup_format_dropdown()
        self.verify_export_popup_cancel_button()
        self.verify_export_popup_export_button()

    def get_report_dates(self):
        all_report_dates = []
        self.driver.wait_for_object("report_date",timeout=20)
        all_reports=self.driver.find_object("report_date",multiple=True)
        for report in all_reports:
            str_date=report.text
            all_report_dates.append(str_date[:11])
        return all_report_dates

    def verify_reports_displaying_correctly_for(self,time_frame):
        is_report_loaded = self.select_details_report_timeframe_dropdown(time_frame)
        if is_report_loaded:
            all_report_dates=self.get_report_dates()
            for dates in all_report_dates:

                # getting the date from web app as a string and converting to datetime
                str_date = dates.replace(" ", "-")
                report_date = datetime.strptime(str_date, '%b-%d-%Y')

                # getting the current date and converting to a specific format for comparison
                today = datetime.today().strftime('%Y-%m-%d')
                today = datetime.strptime(today, '%Y-%m-%d')
                if time_frame == "Last 7 days":
                    no_of_days=7
                elif time_frame == "Last 30 days":
                    no_of_days=30
                elif time_frame == "Last 1 day":                                                        
                    no_of_days=1
                margin = timedelta(days=no_of_days)
                if (today - margin <= report_date) is not True:
                    raise DateComparisonException("Report Date: " + str(report_date)+" is not in the time frame of "+time_frame)
            return True
        else:
            logging.info("No Reports are avilable for "+time_frame)
            return False

    def click_policy_settings_snmp_v1_v2_button(self):
        return self.driver.click("policy_settings_snmpv1_v2_accordion")

    def get_policy_settings_snmp_v1_v2_severity_dropdown_option(self):
        return self.driver.wait_for_object("policy_settings_severity_dropdown").text

    def set_policy_settings_snmp_v1_v2_severity_dropdown_value(self,option):
        self.driver.click("policy_settings_severity_dropdown")
        return self.driver.click("policy_settings_severity_option",format_specifier=[option])
    
    def click_policy_settings_cancel_button(self):
        return self.driver.click("policy_settings_cancel_button")

    def click_policy_settings_save_button(self):
        return self.driver.click("policy_settings_save_button")

    ######################## Reset pop-up #################################################
    
    def verify_policy_reset_settings_popup_title(self):
        expected_title= "Reset Settings ?"
        actual_title=self.driver.get_text("policy_reset_settings_popup_title")
        self.compare_strings(expected_title, actual_title)

    def verify_policy_reset_settings_popup_description(self):
        expected_desc= "Any changes made to this policy will be reset to default configurations."
        actual_desc=self.driver.get_text("policy_reset_settings_popup_desc")
        self.compare_strings(expected_desc, actual_desc)

    def verify_policy_reset_settings_popup_review_changes_button(self):
        return self.driver.wait_for_object("policy_reset_settings_popup_review_changes_button")

    def verify_policy_reset_settings_popup_cancel_button(self):
        return self.driver.wait_for_object("policy_reset_settings_popup_cancel_button")

    def verify_policy_reset_settings_popup_reset_button(self):
        return self.driver.wait_for_object("policy_reset_settings_popup_reset_button")
        
    def click_policy_reset_settings_popup_reset_button(self):
        return self.driver.click("policy_reset_settings_popup_reset_button")

    def click_policy_reset_settings_popup_review_changes_button(self):
        return self.driver.click("policy_reset_settings_popup_review_changes_button")

    def click_policy_reset_settings_popup_cancel_button(self):
        return self.driver.click("policy_reset_settings_popup_cancel_button")

    def click_policy_reset_button(self):
        return self.driver.click("policy_settings_reset_button")

    def verify_policy_reset_settings_review_chnages(self, expected_settings_name):
        actual_settings_name = self.driver.wait_for_object("policy_settings_snmp_v1v2_name_in_preview").text
        assert actual_settings_name == expected_settings_name

    def click_review_changes_popup_close_button(self):
        return self.driver.click("policy_review_changes_close_button")

    def click_policy_settings(self,setting_name):
        return self.driver.click("policy_settings_accordion",format_specifier=[setting_name])

    def get_policy_settings_severity_dropdown_option(self,setting_name):
        return self.driver.wait_for_object("policy_settings_shared_severity_dropdown",format_specifier=[setting_name]).text

    def get_snmp_v1v2_policy_settings_permission_dropdown_option(self):
        return self.driver.wait_for_object("policy_settings_snmp_v1v2_permission_dropdown").text
    
    def get_policy_settings_unsupported_selection(self, setting_name):
        ignore = self.driver.find_object("policy_settings_unsupported_ignore_radio_button" ,format_specifier=[setting_name])
        if ignore.is_selected():
            return "ignore"
        else:
            return "fail"

    def get_policy_settings_remediation_selection(self,setting_name):
        enable = self.driver.find_object("policy_settings_remediation_enable_radio_button",format_specifier=[setting_name])
        if enable.is_selected():
            return "enable"
        else:
            return "disable"


    def set_policy_settings_severity_dropdown_value(self,setting_name,option):
        self.driver.click("policy_settings_shared_severity_dropdown",format_specifier=[setting_name])
        return self.driver.click("policy_settings_shared_severity_dropdown_option",format_specifier=[setting_name,option])

    def set_snmp_v1v2_policy_settings_permission_dropdown_option(self,option):
        self.driver.click("policy_settings_snmp_v1v2_permission_dropdown")
        return self.driver.click("policy_settings_snmp_v1v2_permission_dropdown_option",format_specifier=[option])

    def set_policy_settings_unsupported_value(self,setting_name,option):
        if option == "ignore":
            return self.driver.click("policy_settings_unsupported_ignore_radio_button",displayed=False, format_specifier=[setting_name])
        else:
            return self.driver.click("policy_settings_unsupported_fail_radio_button", displayed=False, format_specifier=[setting_name])

    
    def set_policy_settings_remediation_value(self,setting_name,option):
        if option == "enable":
            return self.driver.click("policy_settings_remediation_enable_radio_button", displayed=False, format_specifier=[setting_name])
        else:
            return self.driver.click("policy_settings_remediation_disable_radio_button", displayed=False,format_specifier=[setting_name])

    def change_snmp_v1v2_device_settings_permission(self,permission_option):
        if  permission_option == "Read Only Enabled":
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.DISABLE)
        elif permission_option == "Read and Write Enabled":
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.READ_ONLY)
        elif permission_option == "Disable":                                                        
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.READ_ONLY)

    def set_snmp_v1v2_device_settings_permission(self,permission_option):
        if  permission_option == "Read Only Enabled":
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.READ_ONLY)
        elif permission_option == "Read and Write Enabled":
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.READ_WRITE)
        elif permission_option == "Disable":                                                        
            self.set_snmp_v1v2_policy_settings_permission_dropdown_option(self.DISABLE)
    
    ########################################## ECP 0.45 Journey Updates #############################################

    def search_policy(self, policy_name):
        return self.driver.send_keys("policy_search_field", policy_name)

    def verify_table_policy_by_name(self, policy_name, policy_search=False, policy_status=None):
        self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        if policy_search:
            self.search_policy(policy_name)

        policy_name_column = self.get_header_index("policy_name")
        policy_name_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_name_column], multiple=True)
        
        if policy_status is not None:
            policy_status_column = self.get_header_index("policy_status")
            policy_status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_status_column], multiple=True)

        for index in range(len(policy_name_list)):
            if policy_name.lower() == policy_name_list[index].text.lower():
                if policy_status is not None and policy_status.lower() != policy_status_list[index].text.lower():
                    return False
                else:
                    return True

        raise CannotFindPolicyException(f"Cannot find policy: {policy_name}")

    def verify_device_policy_compliance_by_serial_number(self, device_name, serial_number, compliance="Compliant"):
        self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        serial_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[3],multiple=True)
        compliance_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[2],multiple=True)

        for index in range(len(serial_list)):
            if serial_number.lower() != serial_list[index].text.lower():
                continue
            if compliance.lower() != compliance_list[index].text.lower():
                return False
            else:
                return True

        raise CannotFindDeviceException(f"Cannot find: {device_name} with serial number: {serial_number}")

    ######################## 0.45 #################################################

    def click_policy_checkbox(self):
        return self.driver.click("policies_table_checkbox")

    def verify_contextual_footer(self,displayed=True):
        return self.driver.wait_for_object("policies_contextual_footer", invisible=not displayed)

    def verify_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("policies_contextual_footer_cancel_button")

    def verify_contextual_footer_selected_item_label(self):
        return self.driver.wait_for_object("policies_selected_label")

    def verify_contextual_footer_select_action_dropdown(self):
        return self.driver.wait_for_object("policies_contextual_footer_select_action_dropdown")

    def verify_contextual_footer_continue_button(self):
        return self.driver.verify_object_string("policies_contextual_footer_continue_button")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("policies_contextual_footer_select_action_dropdown")

    def get_contextual_footer_select_action_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("policies_contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("policies_contextual_footer_cancel_button")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("policies_contextual_footer_continue_button")

    def select_action_dropdown_option(self,option):
        return self.driver.click("policies_select_action_dropdown_option",format_specifier=[option])

    def get_policy_settings_names(self):
        settings_names = []
        self.click_first_entry_link()
        self.driver.wait_for_object("policies_details_settings_names",timeout=10)
        all_settings = self.driver.find_object("policies_details_settings_names",multiple=True)
        for setting in all_settings:
            settings_names.append(setting.text)
        return settings_names

    def click_policies_breadcrumb(self):
        return self.driver.click("policies_all_policy_breadcrumb")

    def click_policy_save_button(self):
        return self.driver.click("edit_policy_save_button")

    def click_are_you_sure_popup_save_button(self):
        return self.driver.click("confirm_policy_save_button")

    def click_confirm_policy_save_button(self):
        return self.driver.click("confirm_popup_policy_save_button")

    def update_policy_name(self,policy_name):
        self.driver.wait_for_object("edit_policy_policy_name_txt",timeout=10)
        return self.driver.send_keys("edit_policy_policy_name_txt", policy_name)

    def click_remove_policy_popup_remove_button(self):
        return self.driver.click("remove_policy_popup_remove_button")

    def click_create_policy_button(self):
        return self.driver.click("policies_create_btn")
    
    def enter_policy_name(self,policy_name):
        return self.driver.send_keys("create_policy_policy_name_txt",policy_name)

    def select_policy_settings_type(self, setting_type, retry=3):
        self.driver.wait_for_object("create_policy_policy_setting_type_dropdown", timeout=20)
        self.driver.click("create_policy_policy_setting_type_dropdown")

        # Loop to ensure dropdown options are visible
        for _ in range(3):  # Retry up to 3 times
            all_options = self.driver.find_object("create_policy_policy_setting_type_dropdown_options", multiple=True)
            if all_options:
                break
            time.sleep(3)  # Wait for 3 second before retrying
            self.driver.click("create_policy_policy_setting_type_dropdown")  # Click dropdown again to retry
        
        for option in all_options:
            if setting_type == option.text:
                return option.click()
        raise CannotFindPolicySettingsTypeException("Cannot find policy settings type: " + setting_type)
    
    def click_create_policy_next_button(self):
        return self.driver.click("create_policy_next_btn")
    
    def search_create_policy_settings(self,setting_name):
        return self.driver.send_keys("create_policy_search_txt",setting_name)

    def click_select_policy_settings_checkbox(self):
        return self.driver.click("create_policy_settings_checkbox")
    
    def click_create_policy_create_button(self):
        return self.driver.click("create_policy_create_button")
    
    def click_create_policy_done_button(self):
        return self.driver.click("create_policy_done_button",timeout=5)
    
    def get_policy_status(self):
        return self.driver.wait_for_object("policies_status").text
    
    def get_policies_assigned_group_name(self):
        return self.driver.wait_for_object("policies_assigned_group_name").text
    
    def click_create_policy_confirm_button(self):
        #For some settings confirm button is coming before done button, so to handle this below click is used.
        return self.driver.click("change_not_recommended_popup_confirm_button", timeout=10, raise_e=False)
    
    def click_create_set_options_tab_delete_button(self):
        return self.driver.click("create_set_options_tab_delete_button")
    
    def create_policy(self,policy_name,policy_settings=None,modify_settings=None,settings_status=None,category_type=None):
        self.click_create_policy_button()
        self.enter_policy_name(policy_name)
        self.select_policy_settings_type(setting_type="Skip Template")
        self.click_create_policy_next_button()
        if policy_settings != None:
            self.search_create_policy_settings(policy_settings)
        self.click_select_policy_settings_checkbox()
        self.click_create_policy_next_button()
        if category_type == "Devices":
            self.modify_device_policy_settings(modify_settings,settings_status)
        elif category_type == "Network":
            self.modify_network_policy_settings(modify_settings,settings_status)
        elif category_type == "File System":
            self.modify_file_system_policy_settings(modify_settings,settings_status)
        elif category_type == "Digital Sending":
            self.modify_digital_sending_policy_settings(modify_settings,settings_status)
        elif category_type == "Fax":
            self.modify_fax_policy_settings(modify_settings,settings_status)
        elif category_type == "Solutions":
            self.modify_solutions_policy_settings_functionality(modify_settings)
        elif category_type == "Web Services":
            self.modify_web_services_policy_settings(modify_settings,settings_status)
        elif modify_settings != None:
            self.modify_policy_setting(modify_settings,settings_status)
        self.click_create_policy_create_button()
        self.click_create_policy_confirm_button()
        self.click_create_policy_done_button()

    def create_information_tab_setting_policy(self,policy_name,policy_settings=None,modify_settings=None,settings_status=None):
        self.click_create_policy_button()
        self.enter_policy_name(policy_name)
        self.select_policy_settings_type(setting_type="Skip Template")
        self.click_create_policy_next_button()
        if policy_settings != None:
            self.search_create_policy_settings(policy_settings)
        self.click_select_policy_settings_checkbox()
        self.click_create_policy_next_button()
        self.click_create_set_options_tab_delete_button() 
        if modify_settings != None:
            self.modify_policy_setting(modify_settings,settings_status)
        self.click_create_policy_create_button()
        self.click_create_policy_confirm_button()
        self.click_create_policy_done_button()

    def verify_policy_details_card(self,expanded=True):
        self.driver.wait_for_object("policy_details_card")
        is_expanded = self.driver.get_attribute("policy_details_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_policy_details_card(self):
        return self.driver.click("policy_details_card")

    def verify_policy_details_card_policy_name(self,policy_name):
        assert policy_name == self.driver.wait_for_object("policy_details_card_policy_name").text

    def verify_policy_details_card_edit_button(self):
        return self.driver.verify_object_string("policy_details_card_edit_btn")

    def click_policy_details_card_more_button(self):
        return self.driver.click("policy_details_card_more_btn",timeout=10)

    def verify_policy_details_card_remove_option(self):
        return self.driver.wait_for_object("policy_details_card_remove_option")

    def click_policy_details_card_remove_option(self):
        return self.driver.click("policy_details_card_remove_option")

    def verify_policy_details_policy_settings_search(self,settings_name):
        self.driver.wait_for_object("policy_details_search_txt")
        self.driver.send_keys("policy_details_search_txt", settings_name)
        search_result = self.driver.find_object("policies_details_settings_names",multiple=True)
        for i in range(len(search_result)):
            if settings_name in search_result[i].text.replace("&nbsp;"," "):
                logging.info("Policy Settings: " + search_result[i].text.replace("&nbsp;"," ") + " contains the searched string: " + settings_name)
                break
            else:
                raise CannotFindPolicyException("Policy Settings: " + search_result[i].text.replace("&nbsp;","") + " does not contain the searched string: " + settings_name)
        return True

    def verify_policy_settings_card(self,expanded=False):
        self.driver.wait_for_object("policy_settings_card")
        is_expanded = self.driver.get_attribute("policy_settings_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_policy_settings_card(self):
        return self.driver.click("policy_settings_card")

    def verify_edit_policy_title(self):
        return self.driver.verify_object_string("edit_policy_title")

    def verify_edit_policy_description(self):
        return self.driver.verify_object_string("edit_policy_desc")

    def verify_edit_policy_refresh_button(self):
        return self.driver.wait_for_object("_shared_sync_button")

    def verify_edit_policy_policy_name_text_field(self):
        return self.driver.wait_for_object("edit_policy_policy_name_txt")

    def verify_edit_policy_note_text_field(self):
        return self.driver.wait_for_object("edit_policy_note_txt")

    def verify_edit_policy_search_box(self):
        return self.driver.wait_for_object("policy_details_search_txt")

    def verify_edit_policy_add_button(self):
        return self.driver.verify_object_string("edit_policy_add_button")

    def verify_are_you_sure_to_save_this_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("policy_save_confirm_popup", invisible=not displayed)

    def verify_are_you_sure_to_save_this_policy_popup_description(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_desc")

    def verify_are_you_sure_to_save_this_policy_popup_policy_name(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_policy_name")

    def verify_are_you_sure_to_save_this_policy_popup_cancel_button(self):
        return self.driver.verify_object_string("policy_save_confirm_popup_cancel_button")

    def verify_are_you_sure_to_save_this_policy_popup_save_button(self):
        return self.driver.verify_object_string("confirm_policy_save_button")

    def click_are_you_sure_to_save_this_policy_popup_cancel_button(self):
        return self.driver.click("policy_save_confirm_popup_cancel_button")

    ########################### Settings Not Saved Pop-up ###########################

    def verify_settings_not_saved_popup(self,displayed=True):
        return self.driver.wait_for_object("settings_not_saved_title", invisible=not displayed)

    def verify_settings_not_saved_popup_title(self):
        return self.driver.verify_object_string("settings_not_saved_title")

    def verify_settings_not_saved_popup_desc(self):
        self.driver.verify_object_string("settings_not_saved_desc_one")
        return self.driver.verify_object_string("settings_not_saved_desc_two")

    def verify_settings_not_saved_popup_cancel_button(self):
        return self.driver.verify_object_string("settings_not_saved_cancel_btn")

    def click_settings_not_saved_popup_cancel_button(self):
        return self.driver.click("settings_not_saved_cancel_btn")

    def verify_settings_not_saved_popup_leave_button(self):
        return self.driver.verify_object_string("settings_not_saved_leave_btn")

    def click_settings_not_saved_popup_leave_button(self):
        return self.driver.click("settings_not_saved_leave_btn")
    
    def get_updated_policy_name(self):
        return self.driver.get_text("create_policy_policy_name_txt")
    
    def verify_policy_page_title(self):
        return self.driver.verify_object_string("policy_page_title")
    
    def verify_contextual_footer_save_button(self):
        return self.driver.wait_for_object("edit_policy_save_button")
    
#########################Assignments tab#######################

    def click_assignments_tab(self):
        return self.driver.click("assignments_tab",timeout=5)
    
    def select_group(self,group_name):
        return self.driver.click("assignments_group_name",format_specifier=[group_name],timeout=20)

    def click_assignments_add_policy_button(self):
        return self.driver.click("assignments_add_policy_btn",timeout=5)
    
    def click_add_policies_checkbox(self):
        return self.driver.click("assignments_add_policy_table_checkbox",timeout=10)
    
    def click_add_policy_button(self):
        return self.driver.click("assignments_add_policy_add_btn",timeout=5)
    
    def click_assess_and_remediate_dropdown_option(self,option):
        self.driver.click("assignments_dropdown")
        options = self.driver.find_object("assignments_dropdown_options", multiple = True)
        if option == "Assess and Remediate":
            options[0].click()
        elif option == "Assess Only":
            options[1].click()
    
    def click_assignments_action_button(self):
        return self.driver.click("assignments_action_btn",timeout=5)
    
    def search_add_policy(self,policy_name):
        self.driver.send_keys("policy_search_txt", policy_name)
        if self.driver.find_object("policies_table_no_item_found",raise_e=False) is not False:
            return False
        else:
            sleep(10)
            table_entry_policies = self.driver.find_object("add_policies_table_policy_name",multiple=True)
            print(table_entry_policies)
            for i in range(len(table_entry_policies)):
                if policy_name in table_entry_policies[i].text:
                    logging.info("Policy Name: " + table_entry_policies[i].text + " contains the searched string: " + policy_name)
                    break
                else:
                    raise PolicySearchException("Policy Name: " + table_entry_policies[i].text + " does not contain the searched string: " + policy_name)
            return True
    
    def click_assignments_delete_policy_button(self):
        return self.driver.click("assignments_delete_policy_btn",timeout=5)

##############################Solutions###########################################
    
    def verify_devices_assigned_policy(self,policy_name):
        self.driver.wait_for_object("solutions_assigned_policy", format_specifier=[policy_name],timeout=40) #timeout increased to 40 seconds to load the policy
        if self.driver.find_object("solutions_assigned_policy", format_specifier=[policy_name], raise_e=False) is not False:
            return True
        else:
            raise CannotFindPolicyException("Assigned Policy report not found")

    def open_recently_ran_report(self):
        self.click_report_content()

    def get_report_result(self):
        return self.driver.wait_for_object("solutions_device_details_latest_report_result",timeout=10).text

    def click_policy_details_card_edit_button(self):
        return self.driver.click("policy_details_card_edit_btn")

    def click_llmnr_policy_settings_accordion(self):
        return self.driver.click("policy_settings_llmnr_accordion",timeout=10)
    
    def click_llmnr_settings_toggle(self):
        return self.driver.click("policy_settings_llmnr_toggle")

    def click_policy_view_details_link(self):
        return self.driver.click("policy_details_view_link",timeout=10)
        
    def verify_assignments_contextual_footer(self):
        return self.driver.wait_for_object("assignment_contextual_footer",timeout=30)

    def verify_assignments_contextual_footer_cancel_button(self):
        return self.driver.verify_object_string("assignment_contextual_footer_cancel_button")

    def verify_assignments_contextual_footer_action_button(self):
        return self.driver.wait_for_object("assignments_action_btn")
    
    def verify_assignments_contextual_footer_is_not_displayed(self):
        return self.driver.wait_for_object("assignment_contextual_footer_cancel_button",invisible=True)
    
    def click_assignments_contextual_footer_cancel_button(self):
        return self.driver.click("assignment_contextual_footer_cancel_button")
    
    def select_assignments_policy_name(self):
        return self.driver.click("assignments_table_policy_name")
    
    def get_assignments_policy_preview_name(self):
        return self.driver.wait_for_object("assignments_policy_preview_title",timeout=10).text
    
    def verify_assignments_policy_settings_title(self):
        return self.driver.verify_object_string("assignments_policy_preview_settings_title")

    def verify_assignments_policy_settings_card(self,expanded=False):
        self.driver.wait_for_object("policy_settings_card")
        is_expanded = self.driver.get_attribute("policy_settings_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def click_assignments_policy_setting_card(self):
        return self.driver.click("policy_settings_card")
    
    def click_assignments_policy_preview_close_button(self):
        return self.driver.click("assignments_policy_preview_close_btn")
    
    def click_change_policy_priority_button(self):
        return self.driver.click("change_policy_priority_button")

    def verify_change_policy_priority_popup_title(self):
        return self.driver.verify_object_string("change_policy_priority_popup_title")

    def verify_change_policy_priority_popup_description(self):
        return self.driver.verify_object_string("change_policy_priority_popup_desc")

    def verify_change_policy_priority_popup_reset_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_reset_btn")

    def verify_change_policy_priority_popup_cancel_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_cancel_btn")

    def verify_change_policy_priority_popup_save_button(self):
        return self.driver.verify_object_string("change_policy_priority_popup_save_btn")

    def verify_change_policy_priority_popup_close_button(self):
        return self.driver.wait_for_object("change_policy_priority_popup_close_btn")

    def get_policy_priority(self):
        policy_names = []
        all_policies = self.driver.find_object("assignment_tab_polices_names",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        return policy_names

    def click_change_policy_priority_checkbox(self,option=0):
        policy_checkbox = self.driver.find_object("change_policy_priority_checkbox",multiple=True)
        return policy_checkbox[option].click()

    def verify_change_policy_priority_popup_up_arrow_button(self):
        return self.driver.wait_for_object("change_policy_priority_up_arrow")

    def verify_change_policy_priority_popup_down_arrow_button(self):
        return self.driver.wait_for_object("change_policy_priority_down_arrow")

    def click_change_policy_priority_down_arrow(self):
        return self.driver.click("change_policy_priority_down_arrow")

    def get_all_policy_names_from_add_policy_popup(self):
        policy_names = []
        all_policies = self.driver.find_object("add_policies_popup_policy_name",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        policy_names.sort()
        return policy_names

    def click_change_policy_priority_up_arrow(self):
        return self.driver.click("change_policy_priority_up_arrow")

    def click_change_policy_priority_save_button(self):
        return self.driver.click("change_policy_priority_popup_save_btn")

    def click_change_policy_priority_cancel_button(self):
        return self.driver.click("change_policy_priority_popup_cancel_btn")

    def verify_change_policy_priority_popup(self,displayed=True):
        return self.driver.wait_for_object("change_policy_priority_popup_title", invisible=not displayed)

    def click_change_policy_priority_popup_close_button(self):
        return self.driver.click("change_policy_priority_popup_close_btn")

    def get_all_policy_names(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        policy_names.sort()
        return policy_names

    def verify_add_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("add_policies_popup_title", invisible=not displayed)

    def verify_add_policy_popup_title(self):
        return self.driver.verify_object_string("add_policies_popup_title")

    def verify_add_policy_popup_description(self):
        return self.driver.verify_object_string("add_policies_popup_desc")

    def verify_add_policy_popup_search_box(self):
        return self.driver.wait_for_object("policy_search_txt")

    def verify_add_policy_popup_cancel_button(self):
        return self.driver.verify_object_string("add_policies_popup_cancel_button")

    def verify_add_policy_popup_add_button(self):
        return self.driver.verify_object_string("assignments_add_policy_add_btn")

    def verify_add_policy_popup_close_button(self):
        return self.driver.wait_for_object("add_policies_popup_close_button")

    def click_add_policy_popup_close_button(self):
        return self.driver.click("add_policies_popup_close_button")

    def verify_add_policy_popup_add_button_status(self,status):
        save_button=self.driver.wait_for_object("assignments_add_policy_add_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True

    def click_add_policy_popup_cancel_button(self):
        return self.driver.click("add_policies_popup_cancel_button")

    def click_edit_policy_add_button(self):
        return self.driver.click("edit_policy_add_button")

    def search_policy_settings_in_add_policy_popup(self,policy_setting):
        return self.driver.send_keys("add_policy_popup_search_txt", policy_setting)
        
    def click_add_policy_checkbox(self):
        return self.driver.click("add_policy_popup_policy_checkbox")

    def click_add_policy_popup_add_button(self):
        return self.driver.click("add_policy_popup_add_button")

    def get_policy_settings_count(self):
        self.driver.wait_for_object("policies_details_settings_names",timeout=10)
        all_settings = self.driver.find_object("policies_details_settings_names",multiple=True)
        return len(all_settings)

    def click_remove_policy_settings_trash_button(self):
        return self.driver.click("edit_policy_settings_trash_button")

    def remove_policy(self,policy_name):
        self.search_policy(policy_name)
        self.click_policy_checkbox()
        self.click_contextual_footer_select_action_dropdown()
        self.select_action_dropdown_option("remove")
        self.click_contextual_footer_continue_button()
        self.click_remove_policy_popup_remove_button()

    def click_edit_policy_screen_add_policy_popup_cancel_button(self):
        return self.driver.click("add_policy_popup_cancel_button")

    def verify_add_policy_pop_up(self,displayed=True):
        return self.driver.wait_for_object("add_policy_pop_up_title", invisible=not displayed)

    def verify_add_policy_pop_up_title(self):
        return self.driver.verify_object_string("add_policy_pop_up_title")

    def verify_add_policy_related_items(self):
        return self.driver.wait_for_object("add_policy_related_item")

    def verify_add_policy_cancel_button(self):
        return self.driver.verify_object_string("add_policy_popup_cancel_button")

    def verify_add_policy_add_button(self):
        return self.driver.verify_object_string("add_policy_popup_add_button")

    def verify_add_policy_popup_search_funtionality(self,settings_name):
        self.driver.send_keys("add_policy_popup_search_txt", settings_name)
        search_result = self.driver.find_object("add_policy_search_policy_setting_names",multiple=True)
        for i in range(len(search_result)):
            if settings_name in search_result[i].text.replace("&nbsp;"," "):
                logging.info("Policy Settings: " + search_result[i].text.replace("&nbsp;"," ") + " contains the searched string: " + settings_name)
                break
            else:
                raise CannotFindPolicyException("Policy Settings: " + search_result[i].text.replace("&nbsp;","") + " does not contain the searched string: " + settings_name)
        return True

    def verify_create_policy_step2_title(self):
        return self.driver.verify_object_string("create_policy_step2_title")

    def verify_create_policy_step2_description(self):
        return self.driver.verify_object_string("create_policy_step2_desc")

    def verify_create_policy_step2_related_items(self):
        return self.driver.wait_for_object("add_policy_related_item")

    def verify_create_policy_popup(self,displayed=True):
        return self.driver.wait_for_object("create_policy_title", invisible=not displayed)
    
    def verify_create_policy_popup_title(self):
        return self.driver.verify_object_string("create_policy_title")
    
    def verify_basic_info_screen_step_title(self):
        return self.driver.verify_object_string("create_policy_basic_info_step_title")
    
    def verify_basic_info_screen_step_description(self):
        return self.driver.verify_object_string("create_policy_basic_info_step_description")
    
    def verify_basic_info_screen_policy_name_field(self):
        return self.driver.wait_for_object("create_policy_policy_name_txt")

    def verify_basic_info_screen_policy_settings_type_dropdown(self):
        return self.driver.wait_for_object("create_policy_policy_setting_type_dropdown",timeout=20)
    
    def verify_basic_info_screen_policy_name_field_error_msg(self):
        self.click_create_policy_next_button()
        return self.driver.verify_object_string("create_policy_basic_info_policy_error_msg")

    def verify_basic_info_screen_policy_settings_type_error_msg(self):
        return self.driver.verify_object_string("create_policy_basic_info_policy_settings_type_error_msg")
    
    def verify_basic_info_screen_note_field(self):
        return self.driver.wait_for_object("create_policy_basic_info_note_field") 
    
    def verify_create_policy_next_button_status(self,status):
        save_button=self.driver.wait_for_object("create_policy_next_btn")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True 
    
    def verify_create_policy_cancel_button(self):
        return self.driver.verify_object_string("create_policy_cancel_btn")

    def click_create_policy_cancel_button(self):
        return self.driver.click("create_policy_cancel_btn")

    def verify_create_policy_back_button(self):
        return self.driver.verify_object_string("create_policy_back_button")

    def verify_create_policy_step3_title(self):
        return self.driver.verify_object_string("create_policy_step3_title")
    
    def verify_create_policy_step3_description(self):
        return self.driver.verify_object_string("create_policy_step3_desc")

    def verify_create_policy_create_button(self):
        return self.driver.verify_object_string("create_policy_create_button")

    def verify_policy_created_successfully_popup_title(self):
        return self.driver.verify_object_string("policy_created_successfully_popup_title")

    def verify_policy_created_successfully_popup_description(self):
        return self.driver.verify_object_string("policy_created_successfully_popup_desc")

    def verify_policy_created_successfully_popup_policy_name(self,policy_name):
        self.driver.verify_object_string("policy_created_successfully_popup_policy_name_label")
        assert policy_name == self.driver.wait_for_object("policy_created_successfully_popup_policy_name").text

    def verify_policy_created_successfully_popup_done_button(self):
        return self.driver.verify_object_string("create_policy_done_button")

    ############################## Column Option Popup ###########################################

    def click_policies_column_options_gear_button(self):
        return self.driver.click("policies_column_option_gear_button")
    
    def select_polices_column_option(self):
        return self.driver.click("policies_column_option_button")
    
    def select_polices_compliance_option(self):
        return self.driver.click("policies_compliance_option_button")
    
    def select_polices_last_run_option(self):
        return self.driver.click("policies_last_run_option_button")

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
    
    def click_column_options_popup_reset_to_default_button(self):
        return self.driver.click("column_options_popup_reset_to_default_btn")

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def reverting_to_default_column_options(self):
        self.click_policies_column_options_gear_button()
        self.select_polices_column_option()
        self.click_column_options_popup_reset_to_default_button()
        self.click_column_options_popup_save_button()

    def click_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "Policy Name":
            options[0].click()
        elif option == "Status":
            options[1].click()
        elif option == "Assigned to":
            options[2].click()
        elif option == "Category":
            options[3].click()
        elif option == "Modified by":
            options[4].click()
        elif option == "Last modified":
            options[5].click()

    def verify_policies_table_column(self,column_name,displayed=True):
        if column_name == "Category":
                return self.driver.wait_for_object("policies_table_catagory_column", invisible=not displayed)
        elif column_name == "Modified by":
                return self.driver.wait_for_object("policies_table_modifiedby_column", invisible=not displayed)
        elif column_name == "Last modified":
                return self.driver.wait_for_object("policies_table_last_modified_column", invisible=not displayed)
        
    def verify_solutions_title(self):
        return self.driver.verify_object_string("solutions_title",timeout=30)

###########################################Policies-Devices###################################################
    def verify_policies_devices_page(self, table_load=True):
        #This object make sure the table is loaded
        #Doesn't work if no entries are found
        if table_load:
            return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, displayed=False)
        else:
            return self.driver.wait_for_object("_shared_table_entries", timeout=30)
    
    def verify_policies_devices_refresh_btn(self):
        return self.driver.wait_for_object("_shared_sync_button")

    def verify_policies_devices_search_device_name_txtbox(self):
        return self.driver.wait_for_object("policies_devices_search_device_name_field")
    
    def verify_policies_devices_column_option_gear_button(self):
        return self.driver.wait_for_object("policies_devices_gear_button")
    
    def verify_policies_devices_groups_title(self):
        return self.driver.verify_object_string("policies_devices_group_title")
    
    def verify_policies_devices_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title")

    def verify_policies_devices_column_options_popup_reset_to_default_button(self):
        return self.driver.verify_object_string("column_options_popup_reset_to_default_btn")

    def verify_policies_devices_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("policies_devices_column_options_popup_cancel_btn")

    def verify_policies_devices_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")
    
    def verify_policies_devices_table_sort(self, field, sort_order):
        #Params: field -> Which field to check the order for 
        #        sort_order -> The order the field should follow 
        header_index = self.get_header_index(field)
        policy_names = []
        all_policies = [i.text for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]
        order_set = [i[0] for i in groupby(all_policies)]
        for policy_name in order_set:
            policy_names.append((policy_name.split(" ")[0]).strip())

        if not saf_misc.list_is_sub(policy_names, sort_order):
            raise IncorrectSortException("Excected sort order: " + str(sort_order), " Actual sort order: " + str(policy_names))
        return True

    def verify_policies_devices_detail_loaded(self):
        return self.driver.wait_for_object("policy_device_details_title", timeout=30)

    def verify_device_details_policy_tab(self):
        return self.driver.wait_for_object("device_details_policy_tab")
    
    def click_device_details_policy_tab(self):
        return self.driver.click("device_details_policy_tab")
    
    def verify_devices_details_list_synced_with_policies_device_tab(self):
        details_info = {}
        self.verify_policies_devices_detail_loaded()

        details_info["model_name"] = self.driver.wait_for_object("policy_device_details_title").text
        details_info["compliance_status"] = self.driver.wait_for_object("policy_device_details_compliance_status").text
        # details_info["serial_number"] = self.driver.wait_for_object("details_device_serial").text
        # details_info["policy"] = self.driver.wait_for_object("policy_device_details_policy").text
        return details_info
    
    def verify_policy_device_details_basic_info_card(self,expanded=True):
        self.driver.wait_for_object("policy_device_details_basic_info_card")
        is_expanded = self.driver.get_attribute("policy_device_details_basic_info_card","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'

    def verify_device_details_policy_compliance_status_card(self):
        self.driver.wait_for_object("policy_device_details_compliance_status_card")
        # is_expanded = self.driver.get_attribute("policy_device_details_compliance_status_card","aria-expanded")
        # if expanded:
        #     assert is_expanded == 'true'
        # else:
        #     assert is_expanded == 'false'
    
    def verify_policy_device_details_compliance_status_card_title(self):
        return self.driver.verify_object_string("policy_device_details_compliance_status_title")
    
    def verify_device_details_policy_run_now_button(self):
        return self.driver.wait_for_object("device_details_policy_run_now_button")
    
    def verify_device_details_policy_widget_policy_card(self):
        return self.driver.wait_for_object("device_details_policy_widget_card")
    
    def verify_device_details_policy_widget_edit_button(self):
        return self.driver.wait_for_object("device_details_policy_widget_edit_button")
    
    def verify_device_details_policy_tab_policy_widget_collapse(self):
        is_expanded = self.driver.get_attribute("device_details_policies_tab_policy_widget_expand_button","aria-expanded")
        assert  is_expanded == 'false'
    
    def verify_device_details_policy_tab_policy_widget_expand(self):
        is_expanded = self.driver.get_attribute("device_details_policies_tab_policy_widget_expand_button","aria-expanded")
        assert  is_expanded == 'true'
    
    def click_device_details_policy_tab_policy_widget(self):
        return self.driver.click("device_details_policies_tab_policy_widget_expand_button")
    
    def verify_policies_device_details_collapsed(self):
        is_expanded = self.driver.get_attribute("device_details_policies_tab_policy_widget_expand_button","aria-expanded")
        assert is_expanded == 'false'
    
    def get_policies_devices_column_options_popup_options(self):
        actual_options = []
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options
    
    def get_policies_devices_detail_info(self):
        device_info = {}
        entry = self.get_total_table_entries(total_len=False)[0]
        all_fields = self.driver.find_object("_shared_table_entry_all_cols",multiple=True, root_obj=entry)
        device_info["model_name"] = all_fields[0].text
        
        actual_value = all_fields[1].text
        device_info["compliance_status"] =(actual_value.split(" ")[0]).strip()
        # device_info["serial_number"] = all_fields[2].text
        # device_info["policy"] = all_fields[3].text
        return device_info

    def click_policies_devices_column_option_gear_button(self):
        return self.driver.click("policies_devices_gear_button")

    def click_policy_device_details_basic_info_card(self):
        return self.driver.click("policy_device_details_basic_info_card")
    
    def click_device_details_policy_compliance_status_card(self):
        return self.driver.click("policy_device_details_compliance_status_card")
    
    def click_policies_devices_tab(self,timeout=20):
        return self.driver.click("policies_devices_tab")
    
    def get_policies_device_list_policy_name(self):
        policy_name = self.get_header_index("policy")
        policy_name_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_name],multiple=True)
        for index in range(len(policy_name_list)):
            actual_policy_name = self.driver.get_text("device_entry_list_policy_status")
        return actual_policy_name
    
    def get_device_detail_policy_tab_policy_name(self):
        return self.driver.get_text("device_detail_policy_tab_policy_text")
    
    def get_device_page_policy_list(self):
        policy_name = self.get_header_index("devices_tab_policies")
        policy_name_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_name],multiple=True)
        for index in range(len(policy_name_list)):
            actual_policy_name = self.driver.get_text("device_page_policy_status")
        return actual_policy_name
    
    def get_policies_device_list_compliance_status(self):
        policy_status = self.get_header_index("compliance")
        policy_status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_status],multiple=True)
        for index in range(len(policy_status_list)):
            actual_status = self.driver.get_text("device_entry_list_compliance_status")
            actual_compliance_status = (actual_status.split(" ")[0]).strip()
        return actual_compliance_status
    
    def get_device_detail_policy_tab_compliance_status(self):
        return self.driver.get_text("device_detail_policy_tab_compliance_status")

    def get_policies_compliance_status_widget_compliance_status_reason(self):
        return self.driver.get_text("policies_compliance_status_widget_compliance_status_reason")
    
    def get_device_page_compliance_status(self):
        policy_status = self.get_header_index("devices_tab_policy_compliance")
        policy_status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[policy_status],multiple=True)
        for index in range(len(policy_status_list)):
            actual_status = self.driver.get_text("device_page_policy_compliance_status")
            actual_compliance_status = (actual_status.split(" ")[0]).strip()
        return actual_compliance_status
    
    def get_device_detail_policy_tab_policy_name(self):
        return self.driver.get_text("device_detail_policy_tab_policy_text")

    def verify_policies_device_details_policy_name(self,expected_name):
        actual_name = self.driver.get_text("policy_device_details_policy")
        assert actual_name == expected_name
    
    def verify_policies_device_details_compliance_policy_status(self,actual_status):
        #actual_status = self.driver.wait_for_object("policy_device_details_compliance_status").text
        if actual_status == "Compliant":
            return True
        elif actual_status == "Noncompliant":
            return True
        elif actual_status == "Unknown":
            raise UnexpectedItemPresentException("Compliance status is Unknown")

    def verify_policies_device_details_compliance_total_policy_settings(self,expected_count,timeout=30):
        actual_count = self.driver.get_text("policy_device_details_total_policy_count")
        actual_policy_count = (actual_count.split(" ")[0]).strip()
        assert actual_policy_count == expected_count

    def remove_assigned_policies_from_all_groups(self):
        all_policies = self.driver.find_object("assignments_delete_policy_btn", multiple=True)
        for policies in all_policies:
            self.click_assignments_delete_policy_button()
        
        self.click_assignments_action_button()
        self.check_toast_successful_message("Policy unassigned successfully.")
    
    def verify_no_policy_is_assigned_to_all_groups(self):
        if self.driver.find_object("assignmentss_table_no_item_found", raise_e=False) is not False:
            logging.info("No policy is assigned to the all groups")
            return True
        else:
            return False
    
    def verify_policies_device_details_assigned_policy_name(self,policy_name):
        priority_policy = self.driver.get_text("policy_device_details_priority_policy_name_2")
        # Split the string and join the parts after "Priority X."
        parts = priority_policy.split(" ")
        priority_policy_name = " ".join(parts[2:]).strip()
        assert priority_policy_name == policy_name
    
    def verify_policies_device_details_assigned_policy_compliance_status(self,compliance_status):
        actual_compliance_status = self.driver.get_text("policy_device_details_priority_compliance_status")
        assert actual_compliance_status == compliance_status
    
    def click_policies_device_details_assigned_policy_priority_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("policy_device_details_priority_2_policy_button"))
        return self.driver.click("policy_device_details_priority_2_policy_button")
    
    def verify_policies_device_details_assigned_policy_setting_name(self,setting_name):
        self.driver.wait_for_object("policy_device_details_policy_settings_name", format_specifier=[setting_name],timeout=20)
        if self.driver.find_object("policy_device_details_policy_settings_name", format_specifier=[setting_name], raise_e=False) is not False:
            return True
        else:
            raise CannotFindPolicyException("Assigned Policy Setting not found in the Policy name")

    def verify_policies_device_details_assigned_policy_priority_1_expanded(self):
        self.driver.wait_for_object("policy_device_details_priority_1_policy_button")

    def click_policies_device_details_assigned_policy_priority_1_expanded(self):
        return self.driver.click("policy_device_details_priority_1_policy_button")

    def verify_policies_device_details_assigned_policy_priority_2_expanded(self,expanded=True):
        self.driver.wait_for_object("policy_device_details_priority_2_policy_button")
        is_expanded = self.driver.get_attribute("policy_device_details_priority_2_policy_button","aria-expanded")
        if expanded:
            assert is_expanded == 'true'
        else:
            assert is_expanded == 'false'
    
    def verify_compliance_status_empty_in_policies_devices_details_page(self, timeout=20):
        return self.driver.find_object("compliance_status_no_item_found")
    
    def get_low_priority_policy_name(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        low_priority_policy = policy_names[-1]
        return low_priority_policy
    
    def get_high_priority_policy_name(self):
        policy_names = []
        all_policies = self.driver.find_object("_shared_table_entries_with_link",multiple=True)
        for policy_name in all_policies:
            policy_names.append(policy_name.text)
        high_priority_policy = policy_names[0]
        return high_priority_policy
    
    def get_policies_device_details_policy_names(self):
        return self.driver.wait_for_object("policy_device_details_policy").text

    def verify_policies_device_details_low_priority_policy_name(self,low_priority_policy):
        self.driver.wait_for_object("policy_device_details_low_priority_policy_name", format_specifier=[low_priority_policy],timeout=20)
        if self.driver.find_object("policy_device_details_low_priority_policy_name", format_specifier=[low_priority_policy], raise_e=False) is not False:
            return True
        else:
            raise CannotFindPolicyException("Assigned Low priority Policy not found")
    
    def verify_policies_device_details_low_priority_policy_overridden_status(self,low_priority_policy_status):
        self.driver.wait_for_object("policy_device_details_low_priority_policy_status", format_specifier=[low_priority_policy_status],timeout=20)
        if self.driver.find_object("policy_device_details_low_priority_policy_status", format_specifier=[low_priority_policy_status], raise_e=False) is not False:
            return True
        else:
            raise CannotFindPolicyException("Assigned Low priority Policy status not found")
    
    def click_policies_device_details_low_priority_policy_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("policy_device_details_low_priority_policy_button")) 
        return self.driver.click("policy_device_details_low_priority_policy_button") 
    
    def click_policies_device_details_low_priority_policy_settings_button(self):
        return self.driver.click("policy_device_details_low_priority_policy_settings_button", timeout=30) 
    
    def verify_policies_device_details_low_priority_policy_warning_icon(self):
        return self.driver.find_object("policy_device_details_low_priority_policy_warning_icon")
    
    def verify_policies_device_details_low_priority_policy_warning_message(self,warning_message):
        actual_warning_message = self.driver.get_text("policy_device_details_low_priority_policy_warning_message")
        assert warning_message == actual_warning_message
    
    def click_policies_device_details_high_priority_policy_settings_button(self):
        return self.driver.click("policy_device_details_high_priority_policy_settings_button",timeout=30) 
    
    def verify_policies_device_details_high_priority_policy_warning_icon(self,compliance_status,policy_setting):
        if compliance_status ==  "Compliant":
            return self.driver.find_object("policy_device_details_high_priority_policy_checkmark_icon",format_specifier=[policy_setting])
        elif compliance_status == "Noncompliant":
            return self.driver.find_object("policy_device_details_high_priority_policy_warning_icon",format_specifier=[policy_setting])
    
    def verify_policies_device_details_high_priority_policy_warning_message(self,warning_message,compliance_status):
        if compliance_status ==  "Compliant":
            return True
        elif compliance_status == "Noncompliant":
            actual_warning_message = self.driver.get_text("policy_device_details_high_priority_policy_warning_message")
            assert warning_message == actual_warning_message
    
    def verify_policies_device_list_compliance_status_when_no_policy_assigned(self,compliance_status):
        if compliance_status == "Unknown":
            return True
        else:
            raise UnexpectedItemPresentException("Compliance status has not changed to Unknown")

    def verify_policies_device_list_compliance_status(self,compliance_status):
        if compliance_status == "Compliant":
            return True
        elif compliance_status == "Noncompliant":
            return True
        elif compliance_status == "Unknown":
            raise UnexpectedItemPresentException("Compliance status is Unknown")
        
    def click_solutions_device_tab_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "Assessment":
            options[1].click()
        elif option == "Status":
            options[2].click()
        elif option == "Connectivity":
            options[3].click()
        elif option == "Serial Number":
            options[4].click()
        elif option == "Policies":
            options[5].click()
        elif option == "Group":
            options[6].click()

    def verify_solutions_device_table_column(self,column_name,displayed=True):
        if column_name == "Assessment":
                return self.driver.wait_for_object("solutions_device_table_assessmnet_column", invisible=not displayed)
        elif column_name == "Connectivity":
                return self.driver.wait_for_object("solutions_device_table_connectivity_column", invisible=not displayed)
        elif column_name == "Policies":
                return self.driver.wait_for_object("solutions_device_table_policies_column", invisible=not displayed)
        
    def click_create_policy_policy_settings_card(self,settings_name):
        return self.driver.click("create_policy_set_option_policy_card",format_specifier=[settings_name])
    
    def click_ignore_unsupported_item_toggle(self):
        return self.driver.click("ignore_unsupported_item_toggle")
    
    def select_control_panel_language(self,language):
        # Currenty we only supports 3 options Russian,Spanish and English.
        # Languae code for English = en, Russian = ru, Spanish = es
        lang_dict = {"English": "en", "Russian": "ru", "Spanish": "es"}
        self.driver.click("control_panel_language_dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("control_panel_language_option",format_specifier=[lang_dict[language]]))
        return self.driver.click("control_panel_language_option",format_specifier=[lang_dict[language]])
        
    def enter_company_name(self,company_name):
        return self.driver.send_keys("company_name_txt",company_name)
    
    def enter_device_name(self,device_name):
        return self.driver.send_keys("device_name_txt",device_name)
    
    def unassign_policy_from_group(self,group_name,policy_name):
        self.click_assignments_tab()
        if self.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.click_policy_assignments_side_groups_btn()
        self.select_group(group_name)
        self.click_assignments_delete_policy_button()
        self.click_assignments_action_button()
        self.check_toast_successful_message("Policy unassigned successfully.")
        self.dismiss_toast()
        self.click_policies_tab()
        self.verify_table_loaded()
        self.remove_policy(policy_name)
    
    def verify_policies_compliance_status(self, serial_number):
        for counter in range(10):
            if self.get_device_detail_policy_tab_compliance_status() == "Compliant":
                return True
            else:
                self.click_refresh_button()
                sleep(10) # Adding time out to load the page 
        raise PolicyNoncompliantException("Assigned Policy is Non Compliant")

    def click_ignore_unentitled_item_toggle(self):
        return self.driver.click("ignore_unentitled_item_toggle")

    def click_ws_discovery_option(self):
        return self.driver.click("web_service_discovery_checkbox")

    def click_bonjour_option(self):
        return self.driver.click("bonjour_checkbox")

    def click_slp_option(self):
        return self.driver.click("slp_checkbox")

    def click_airprint_option(self):
        return self.driver.click("airprint_checkbox")

    def click_ipp_option(self):
        return self.driver.click("ipp_checkbox")

    def click_ipps_option(self):
        return self.driver.click("ipps_checkbox")

    def click_lpd_option(self):
        return self.driver.click("lpd_checkbox")
    
    def click_remediation_toggle(self):
        return self.driver.click("remediation_item_toggle")
    
    def click_tcp_option(self):
        return self.driver.click("tcp_checkbox")
    
    def click_ws_print_option(self):
        return self.driver.click("ws_print_checkbox")

    def click_wins_port_option(self):
        return self.driver.click("wins_port_checkbox")

    def click_wins_registration_option(self):
        return self.driver.click("wins_registration_checkbox")
    
    def click_llmnr_option(self):
        return self.driver.click("llmnr_checkbox")

    def click_airprint_fax_option(self):
        return self.driver.click("airprint_fax_checkbox")

    def click_airprint_scan_and_secure_scan_option(self):
        return self.driver.click("airprint_scan_and_secure_scan_checkbox")
    
    def click_dhcp_v4_compliance_option(self):
        return self.driver.click("dhcp_v4_compliance_checkbox")
    
    def click_ipv4_multicast_option(self):
        return self.driver.click("ipv4_multicast_checkbox")

    def click_postscript_security_option(self):
        return self.driver.click("postscript_security_checkbox")
    
    def click_csrf_prevention_option(self):
        return self.driver.click("csrf_prevention_checkbox")

    def click_verify_certificate_option(self):
        return self.driver.click("verify_certificate_checkbox")
    
    def click_pjl_access_commands_option(self):
        return self.driver.click("pjl_access_commands_checkbox")
    
    def verify_service_access_code_textbox(self):
        if self.driver.find_object("service_access_code_textbox_disabled").is_enabled():
            raise UnexpectedItemPresentException("TextBox is enabled")
        return True 
    
    def verify_secure_boot_presence_option_is_disabled(self):
        if self.driver.find_object("secure_boot_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True 
    
    def verify_intrusion_detection_presence_option_is_disabled(self):
        if self.driver.find_object("intrusion_detection_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True 

    def verify_whitelisting_presence_option_is_disabled(self):
        if self.driver.find_object("whitelisting_presence_checkbox").is_enabled():
            raise UnexpectedItemPresentException("Checkbox is enabled")
        return True 

    def click_remote_fw_update_option(self):
        return self.driver.click("remote_fw_update_checkbox")
    
    def click_auto_firmware_update_option(self):
        return self.driver.click("auto_firmware_update_checkbox")

    def click_direct_connect_ports_option(self):
        return self.driver.click("direct_connect_ports_checkbox")

    def click_require_https_redirect_option(self):
        return self.driver.click("require_https_redirect_checkbox")

    def click_embedded_web_server_access_checkbox(self):
        return self.driver.click("embedded_web_server_access_checkbox")
    
    def enter_control_panel_timeout_value(self,timeout_value):
        return self.driver.send_keys("enter_control_panel_timeout",timeout_value)

    def click_disk_encryption_inactive_status(self):
        return self.driver.click("disk_encryption_inactive_status")
    
    def click_snmp_v1v2_disable_option(self):
        return self.driver.click("snmp_v1v2_disable_radio_btn")

    def click_snmp_v1v2_read_only_radio_btn(self):
        return self.driver.click("snmp_v1v2_read_only_radio_btn")

    def click_snmp_v1v2_read_write_radio_btn(self):
        return self.driver.click("snmp_v1v2_read_write_radio_btn")

    def click_snmp_v3_option(self):
        return self.driver.click("snmp_v3_checkbox")
    
    def click_host_usb_plug_and_play_option(self):
        return self.driver.click("host_usb_plug_and_play_checkbox")

    def click_proxy_device_settings_checkbox(self, setting_name):
        return self.driver.click("proxy_device_settings_checkbox", format_specifier=[setting_name])
    
    def click_ps_access_option(self):
        return self.driver.click("ps_access_option")

    def click_pjl_access_option(self):
          return self.driver.click("pjl_access_option")
    
    def click_require_admin_password_for_access_option(self):
        return self.driver.click("require_admin_password_for_access_option")
    
    def click_display_print_page_option(self):
        return self.driver.click("display_print_page_option")

    def click_display_job_log_option(self):
        return self.driver.click("display_job_log_option")
    
    def click_time_services_do_not_sync_network_time_server(self):
        return self.driver.click("time_services_do_not_sync_network_time_server")
    
    def click_time_services_automatic_sync_custom_network_time_server(self):
        return self.driver.click("time_services_automatic_sync_custom_network_time_server")

    def verify_policy_assignments_side_groups_btn_is_enabled(self):
        return self.driver.wait_for_object("policy_assignments_side_groups",raise_e=False)
   
    def click_policy_assignments_side_groups_btn(self):
        return self.driver.click("policy_assignments_side_groups_expand_btn")

    def verify_app_deployment_warning_label(self):
        self.driver.wait_for_object("app_depolyment_warning_label")
   
    def verify_app_deployment_remove_btn(self):
        self.driver.wait_for_object("app_depolyment_remove_btn")
   
    def verify_zero_items_selected_label(self):
        self.driver.wait_for_object("app_depolyment_zero_items_selected_label")
   
    def verify_items_not_found_label(self):
        self.driver.wait_for_object("app_depolyment_no_items_found_label")
   
    def app_deployment_select_app_common_version_btn(self):
        self.driver.click("app_deployment_select_app_common_version_option_btn")
   
    def click_devices_expand_btn_is_enabled(self):
        return self.driver.wait_for_object("device_groups_side_btn",raise_e=False)
   
    def click_devices_expand_btn(self):
        return self.driver.click("device_groups_side_expand_btn")

    def add_policy_to_device_group(self,group_name,policy_name):
        self.click_assignments_tab()
        if self.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.click_policy_assignments_side_groups_btn()
        self.select_group(group_name)
        self.click_assignments_add_policy_button()
        self.search_add_policy(policy_name)
        self.click_add_policies_checkbox()
        self.click_add_policy_button()
        self.click_assignments_action_button()
        self.click_create_policy_done_button()
        # self.check_toast_successful_message("Policy assigned successfully.")

    def verify_assessment_status_report(self):
        # self.click_hp_secure_fleet_manager()  # Solution- Devices tab got removed from the UI, So commenting this line
        # self.click_devices_tab()
        # self.verify_table_loaded()
        # self.click_policy_assignments_side_groups_btn()
        # self.select_group(group_name)
        # self.click_first_entry_link()
        # self.verify_devices_assigned_policy(policy_name)
        self.select_report("assessment")
        self.verify_details_report_loaded()
        for count in range(10):
            if self.get_report_result() == "Passed":
                return True
            else:
                sleep(5)
                self.click_refresh_button()
                self.select_report("assessment")
                self.verify_details_report_loaded()
                # self.open_recently_ran_report()
    
        raise SettingValueMismatchException("Assigned Setting Value is Mismatch")
    
    def update_temporary_and_standard_retain_jobs_setting_attributes(self, settings_status):
        stored_jobs_enabled_status = settings_status[0]
        temporary_stored_job_status = settings_status[1]
        standard_stored_job_status = settings_status[2]

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

    def update_time_services_setting_attributes(self, settings_status):
        time_services_system_time_sync = settings_status[0]
        time_services_address = settings_status[1]
        local_port = settings_status[2]
        synchronize_time = settings_status[3]
        if time_services_system_time_sync == "ntp":
            self.click_time_services_do_not_sync_network_time_server()
        else:
            self.click_time_services_automatic_sync_custom_network_time_server()
            self.driver.send_keys("time_services_server_address_ip", time_services_address )
            self.driver.send_keys("time_services_port_value", local_port)
            self.driver.send_keys("time_services_hours_value",synchronize_time )

    def update_information_tab_setting_attributes(self, settings_status):
        information_tab_status = settings_status[0]
        display_job_log_status = settings_status[1]
        display_print_job_log_status = settings_status[2]
        if information_tab_status == "false":
            self.click_require_admin_password_for_access_option()
        if display_job_log_status == "false":
            self.click_display_print_page_option()
        if display_print_job_log_status == "false":
            self.click_display_job_log_option()

    def update_web_encryption_setting_attributes(self, settings_status):
        tls_minimum_protocol_version = settings_status[0]
        tls_maximum_protocol_version = settings_status[1]
        if tls_minimum_protocol_version == "tls1_0":
            self.driver.click("web_encryption_min_tls_1.1_version")
        elif tls_minimum_protocol_version == "tls1_1":
            self.driver.click("web_encryption_min_tls_1.2_version")
        elif tls_minimum_protocol_version == "tls1_2":
            self.driver.click("web_encryption_min_tls_1.0_version")
        if tls_maximum_protocol_version == "tls1_1":
            self.driver.click("web_encryption_max_tls_1.2_version")
        elif tls_maximum_protocol_version == "tls1_2":
            self.driver.click("web_encryption_max_tls_1.3_version")
        else:
            self.driver.click("web_encryption_max_tls_1.1_version")

    def update_fax_receive_setting_attributes(self, settings_status):
        fax_receive_status = settings_status[0]
        fax_receive_method_status = settings_status[1]
        ringer_volume_status = settings_status[2]
        rings_to_answer_status = settings_status[3]
        if fax_receive_status == "false":
            self.driver.click("fax_receive_setting_checkbox")
            if fax_receive_method_status != "ipFax":
                self.driver.click("fax_receive_ip_fax_method_option")
            else:
                self.set_fax_receive_internal_modem_attributes(ringer_volume_status,rings_to_answer_status)

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

    def set_email_address_message_in_email_setting_attributes(self,settings_status):
        address_filed_restrictions =  settings_status[0]
        default_from_value = settings_status[1]
        default_from_email =  settings_status[2]
        default_display_name = settings_status[3]
        default_from_user_editable = settings_status[4]
        to_sign_in_required = settings_status[5]
        user_editable_to = settings_status[6]
        cc_sign_in_required = settings_status[7]
        user_ediatable_cc = settings_status[8]
        bcc_sign_in_required = settings_status[9]
        user_editable_bcc = settings_status[10]
        email_subject_name = settings_status[11]
        user_editable_subject = settings_status[12]
        email_body_message = settings_status[13]
        user_editable_body = settings_status[14]
        allow_invaild_email_address = settings_status[15]
        email_message_user_editable = settings_status[16]
        encrypt_email_user_editable = settings_status[17]
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

    def set_sleep_settings(self,settings_status):
        # sleep_auto_off_timer_status=settings_status[0]
        sleep_mode_values=settings_status[1]
        auto_on_events_status=settings_status[2]
        auto_off_after_sleep_values=settings_status[3]
        self.driver.send_keys("sleep_settings_sleep_mode_textbox",sleep_mode_values)
        if auto_on_events_status == "powerButtonPress":
            self.driver.click("sleep_settings_wake_all_events_radio_button")
        else:
            self.driver.click("sleep_settings_wake_network_port_radio_button")
        self.driver.send_keys("sleep_settings_auto_off_textbox",auto_off_after_sleep_values)

    def update_cross_origin_resource_sharing_setting_attributes(self,settings_status):
        cross_enable_status = settings_status[0]
        random_site_name = settings_status[1]
        random_site_name_2 = settings_status[2]
        if cross_enable_status == "false":
            self.driver.click("cross_origin_resource_sharing_checkbox")
            self.driver.click("cross_setting_add_button")
            self.driver.send_keys("cross_origin_resource_sharing_textbox",random_site_name)
            self.driver.click("cross_origin_add_site_name_popup_add_button")
            self.remove_added_site_name_functionality(random_site_name_2)

    def remove_added_site_name_functionality(self,random_site_name_2):
        self.driver.click("cross_setting_add_button")
        self.driver.send_keys("cross_origin_resource_sharing_textbox",random_site_name_2)
        self.driver.click("cross_origin_add_site_name_popup_add_button")
        self.driver.click("cross_table_checkbox")
        self.driver.click("cross_setting_remove_button")

    def click_set_options_settings_checkbox(self, modify_setting=None):
        return self.driver.click("set_options_settings_checkbox", format_specifier=[modify_setting])

    def click_printer_firmware_sha1_code_signing_checkbox(self):
        return self.driver.click("printer_firmware_sha1_code_signing_checkbox")

    def update_configuration_precedence_method_setting_value(self, settings_status):
        configuration_precedence_order_value = settings_status[0]
        configuration_precedence_order_method = settings_status[1]
        
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

    def set_restrict_color_status(self,settings_status):
        color_settings = settings_status[0]
        restrict_by_user_permissions = settings_status[1]
        restrict_by_application = settings_status[2]
        default_permission = settings_status[3]
        application_name = settings_status[4]
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
                
    def modify_network_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "ws-discovery":
            if settings_status == "false":
                self.click_ws_discovery_option()
        elif modify_setting == "bonjour":
            if settings_status == "false":
                self.click_bonjour_option()
        elif modify_setting == "slp":
            if settings_status == "false":
                self.click_slp_option()
        elif modify_setting == "airprint":
            if settings_status == "false":
                self.click_airprint_option()
        elif modify_setting == "ipp":
            if settings_status == "false":
                self.click_ipp_option()
        elif modify_setting == "ipps":
            if settings_status == "true":
                self.click_ipps_option()
        elif modify_setting == "lpd-lpr":
            if settings_status == "true":
                self.click_lpd_option()
        elif modify_setting == "tcpip-print":
            self.click_remediation_toggle()
            if settings_status == "true":
                self.click_tcp_option()
        elif modify_setting == "ws-print":
            if settings_status == "false":
                self.click_ws_print_option()
        elif modify_setting == "wins-port":
            if settings_status == "false":
                self.click_wins_port_option()
        elif modify_setting == "wins-registration":
            if settings_status == "false":
                self.click_wins_registration_option()
        elif modify_setting == "llmnr":
            if settings_status == "false":
                self.click_llmnr_option()
        elif modify_setting == "airprint-fax":
            if settings_status == "false":
                self.click_airprint_fax_option()
        elif modify_setting == "airprint-scan-secure-scan":
            if settings_status == "false":
                self.click_airprint_scan_and_secure_scan_option()
        elif modify_setting == "dhcp-v4-compliance":
            if settings_status == "true":
                self.click_dhcp_v4_compliance_option()
        elif modify_setting == "ipv4-multicast":
            if settings_status == "false":
                self.click_ipv4_multicast_option()
        elif modify_setting == "telnet":
            if settings_status == "false":
                self.driver.click("telnet_checkbox")
        elif modify_setting == "tftp-cfg":
            if settings_status == "false":
                self.driver.click("tftp_configuration_file_checkbox")
        elif modify_setting == "ftp-print":
            if settings_status == "false":
                self.driver.click("ftp_print_checkbox")
        elif modify_setting == "configuration-precedence":
            self.update_configuration_precedence_method_setting_value(settings_status)

    def modify_device_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "ctrl-panel-language":
            if settings_status == "es":
                self.select_control_panel_language("Russian")
            else:
                self.select_control_panel_language("Spanish")
        elif modify_setting == "company-name":
            self.enter_company_name(settings_status)
        elif modify_setting == "device-name":
            self.enter_device_name(settings_status)
        elif modify_setting == "retain-jobs":
            self.update_temporary_and_standard_retain_jobs_setting_attributes(settings_status)
        elif modify_setting == "sleep-settings":
            self.set_sleep_settings(settings_status)
 
    def modify_file_system_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "fs-access-protocol":
            ps_file_system_access_enabled_status = settings_status[0]
            pjl_file_system_access_enabled_status = settings_status[1]
            if ps_file_system_access_enabled_status == "false":
                self.click_ps_access_option()
            if pjl_file_system_access_enabled_status == "false":
                self.click_pjl_access_option()
        elif modify_setting == "file-erase":
            if settings_status == "secureFastErase":
                self.driver.click("file_erase_non_secure_radio_button")

    def modify_digital_sending_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "save-to-network-folder":
            if settings_status == "true":
                self.driver.click("save_to_network_folder_checkbox")
        elif modify_setting == "save-to-share-point":
            if settings_status == "true":
                self.driver.click("save_to_sharepoint_checkbox")
        elif modify_setting == "save-to-email":
            if settings_status == "true":
                self.driver.click("send_to_email_checkbox")
        elif modify_setting == "email-message":
            self.click_ignore_unsupported_item_toggle()
            self.set_email_address_message_in_email_setting_attributes(settings_status)

    def modify_policy_setting(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "ps-security":
            if settings_status == "false":
                self.click_postscript_security_option()
        elif modify_setting == "csrf-prevention":
            if settings_status == "true":
                self.click_csrf_prevention_option()
        elif modify_setting == "verify-certificate":
            if settings_status == "false":
                self.click_verify_certificate_option()
        elif modify_setting == "pjl-command":
            if settings_status == "false":
                self.click_pjl_access_commands_option()
        elif modify_setting == "svc-access-code":
            self.verify_service_access_code_textbox()
        elif modify_setting == "secure-boot-presence":
            self.verify_secure_boot_presence_option_is_disabled()
        elif modify_setting == "intrusion-detect-presence":
            self.verify_intrusion_detection_presence_option_is_disabled()
        elif modify_setting == "whitelist-presence":
            self.verify_whitelisting_presence_option_is_disabled()
        elif modify_setting == "remote-fw-update":
            if settings_status == "false":
                self.click_remote_fw_update_option()
        elif modify_setting == "auto-fw-update":
            if settings_status == "true":
                self.click_auto_firmware_update_option()
        elif modify_setting == "dc-ports":
            if settings_status == "false":
                self.click_direct_connect_ports_option()
        elif modify_setting == "https-redirect":
            if settings_status == "true":
                self.click_require_https_redirect_option()
        elif modify_setting == "ews-access":
            pass
        elif modify_setting == "ctrl-panel-timeout":
                self.enter_control_panel_timeout_value(settings_status)
        elif modify_setting == "disk-encryption":
            pass
        elif modify_setting == "snmp-v1-v2":
            if settings_status == "true":
                self.click_snmp_v1v2_disable_option()
        elif modify_setting == "snmp-v3":
            if settings_status == "true":
                self.click_snmp_v3_option()
        elif modify_setting == "host-usb-pnp":
            self.update_host_usb_plug_and_play_setting_attributes(settings_status)
        elif modify_setting == "info-tab":
            self.update_information_tab_setting_attributes(settings_status)
        elif modify_setting == "pjl-password":
            self.click_remediation_toggle()
        elif modify_setting == "time-services":
            self.update_time_services_setting_attributes(settings_status)
        elif modify_setting == "web-encryption":
            self.update_web_encryption_setting_attributes(settings_status)
        elif modify_setting == "jd-xml-svc":
            if settings_status == "false":
                self.driver.click("hp_jetdirect_xml_service_checkbox")
        elif modify_setting == "legacy-fw-update":
            if settings_status == "false":
                self.driver.click("legacy_fw_update_checkbox")
        elif modify_setting == "cors":
            self.update_cross_origin_resource_sharing_setting_attributes(settings_status)
        elif modify_setting == "remote-fw-update":
            self.click_set_options_settings_checkbox(modify_setting)
        elif modify_setting == "restrict-color":
            self.set_restrict_color_status(settings_status)

    def modify_fax_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "fax-receive":
            self.click_ignore_unsupported_item_toggle()
            self.update_fax_receive_setting_attributes(settings_status)

    def modify_web_services_policy_settings(self,modify_setting,settings_status):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        if modify_setting == "smart-cloud-print":
            if settings_status == "true":
                self.driver.click("smart_cloud_print_checkbox")

    def modify_solutions_policy_settings_functionality(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_printer_on_agent_checkbox")
        self.driver.click("app_deployment_select_app_printer_on_agent_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")
   
    def verify_app_deployment_select_app_printer_on_agent_checkbox(self):
        return self.driver.wait_for_object("app_deployment_select_app_printer_on_agent_checkbox",raise_e=True)
 
    def uninstal_added_app_in_app_deployment_settings(self,modify_setting):
        self.driver.click("app_deployment_setting_accordion")
        self.driver.click("app_deployment_uninstall_unlisted_app")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("app_deployment_app_name_table_checkbox"))
        self.driver.click("app_deployment_app_name_table_checkbox")
        self.driver.click("app_deployment_remove_btn")
        self.driver.click("app_deployment_select_app_save_btn")

    def add_regus_plugin_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_regus_plugin_checkbox")
        self.driver.click("app_deployment_select_app_regus_plugin_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_sharepoint_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_sharepoint_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_sharepoint_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_box_and_hp_for_clio_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_box_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_box_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_hp_for_clio_checkbox", timeout=30)
        self.driver.click("app_deployment_select_hp_for_clio_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_dropbox_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_dropbox_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_dropbox_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_google_drive_hp_for_onedrive_and_hp_for_onedrive_business_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_google_drive_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_google_drive_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_hp_for_onedrive_checkbox", timeout=30)
        self.driver.click("app_deployment_select_hp_for_onedrive_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_hp_for_onedrive_business_checkbox", timeout=30)
        self.driver.click("app_deployment_select_hp_for_onedrive_business_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_universal_print_and_hp_mail_flow_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_universal_print_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_universal_print_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_hp_mail_flow_checkbox", timeout=30)
        self.driver.click("app_deployment_select_hp_mail_flow_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")

    def add_hp_for_dropbox_lite_survey_and_lrs_authenticator_app_in_app_deployment_settings(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.driver.click("app_deployment_do_not_uninstall_unlisted_app")
        self.driver.click("app_deployment_select_app_btn")
        sleep(10) # Giving time out to load the select app pop-up
        self.driver.click("app_deployment_select_app_hp_for_dropbox_checkbox",timeout=30)
        self.driver.click("app_deployment_select_hp_for_dropbox_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_lite_survey_app_checkbox", timeout=30)
        self.driver.click("app_deployment_select_lite_survey_app_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_lrs_authenticator_checkbox", timeout=30)
        self.driver.click("app_deployment_select_lrs_authenticator_dropdown")
        self.app_deployment_select_app_common_version_btn()
        self.driver.click("app_deployment_select_app_save_btn")
   
    def modify_solutions_policy_settings_ui(self,modify_setting):
        self.click_create_policy_policy_settings_card(modify_setting)
        self.click_ignore_unsupported_item_toggle()
        self.driver.click("app_deployment_checkbox")
        self.verify_app_deployment_warning_label()
        self.verify_app_deployment_remove_btn()
        self.verify_zero_items_selected_label()
        self.verify_items_not_found_label()
        self.click_create_policy_cancel_button()
    
    def create_policy_for_app_deployment(self,policy_name,policy_settings=None,modify_settings=None,settings_status=None,category_type=None):
        self.click_create_policy_button()
        self.enter_policy_name(policy_name)
        self.select_policy_settings_type(setting_type="Skip Template")
        self.click_create_policy_next_button()
        if policy_settings != None:
            self.search_create_policy_settings(policy_settings)
        self.click_select_policy_settings_checkbox()
        self.click_create_policy_next_button()
        self.modify_solutions_policy_settings_ui(modify_settings)

    def verify_policies_compliance_status_for_app_deployment_setting(self, serial_number):
        for __ in range(37): # To install and uninstall the app the remediation will takes time, so increasing the time out
            if self.get_device_detail_policy_tab_compliance_status() == "Compliant":
                return True
            else:
                self.click_refresh_button()
                sleep(37) # Adding time out to load the page 
        raise PolicyNoncompliantException("Assigned Policy is Non Compliant")

    def create_policy_for_app_deployment_with_regus_plugin(self,policy_name,policy_settings=None,modify_settings=None):
        self.click_create_policy_button()
        self.enter_policy_name(policy_name)
        self.select_policy_settings_type(setting_type="Skip Template")
        self.click_create_policy_next_button()
        if policy_settings != None:
            self.search_create_policy_settings(policy_settings)
        self.click_select_policy_settings_checkbox()
        self.click_create_policy_next_button()
        self.add_regus_plugin_app_in_app_deployment_settings(modify_settings)
        self.click_create_policy_create_button()
        self.click_create_policy_confirm_button()
        self.click_create_policy_done_button()