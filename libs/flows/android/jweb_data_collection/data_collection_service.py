import json
from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class DataCollectionService(JwebDataCollectionFlow):
    flow_name = "data_collection_service"

    def select_settings_button(self):
        """
        From the Data Collection Service page, select the settings icon (wrench) in the top right corner
        """
        self.driver.click("data_collection_settings_btn")

    def select_request_logs_button(self):
        """
        From the Data Collection Service page, select the Request Logs button 
        """
        self.driver.click("request_logs_btn")

    def get_newest_request_log_url(self, expect_value=True):
        """
        From the Request Logs page, return the latest URL request 
        """
        if expect_value:
            return self.driver.get_attribute("request_log_url", "text")
        else:
            return self.driver.wait_for_object("request_log_url", timeout=3, raise_e=False)
        
    def select_data_ingress_btn(self):
        """
        From the Request Logs page, select data ingress button
        """
        self.driver.click("data_ingress_btn")

    def select_data_value_btn(self):
        """
        From the Request Logs page, select data value button
        """
        self.driver.click("data_value_btn")

    def get_second_attempt_data_ingress_controller_status_code(self):
        """
        From the Request Logs page, verify the status code from the second attempt url found in the Data ingress request
        """
        return self.driver.get_attribute("data_ingress_second_attempt_status_code", "text")

    def get_first_attempt_data_ingress_controller_status_code(self):
        """
        From the Request Logs page, verify the status code from the first attempt url found in the Data ingress request
        """
        return self.driver.get_attribute("data_ingress_first_attempt_status_code", "text")
    
    def get_data_valve_controller_status_code(self):
        """
        From the Request Logs page, verify the status code from Data valve request
        """
        return self.driver.get_attribute("data_valve_status_code", "text")
    
    def select_verbose_logs_button(self):
        """
        From the Data Collection Service page, select the verbose logs button 
        """
        self.driver.click("verbose_logs_btn")

    def get_verbose_logs_result(self):
        """
        In verbose logs, get the result text
        """
        return self.driver.get_attribute("verbose_logs_text", "text")

    def select_list_queue_item_button(self):
        """
        From the Data Collection Service page, select the list queue button 
        """
        self.driver.click("list_queue_item")

    def verify_queue_item_lists(self): 
        """ 
        in queue tab extract the content to verify whether the screen is empty
        """
        return not self.driver.wait_for_object("rv_queue_list", timeout=3, raise_e=False) is False
    
    def select_send_sys_info_event_button(self):
        """
        select the send sys info event button
        """
        self.driver.click("send_sys_info_event_btn") 

    def select_bindings_delete_button(self):
        """
        in bindings tab.select delete button
        """
        self.driver.click("bindings_delete_btn") 

    def verify_bindings_contents(self): 
        """ 
        in bindings tab extract the content to verify whether the screen is empty
        """
        return not self.driver.wait_for_object("binding_content", timeout=3, raise_e=False) is False
    
    def select_add_valid_cdm_button(self):
        """
        in filter CDM/LEDM tab.select add valid cdm button
        """
        self.driver.click("add_valid_btn")

    def select_add_button(self):
        """
        in filter CDM/LEDM tab.select add valid button
        """
        self.driver.click("add_btn")

    def select_apply_filter_button(self):
        """
        in filter CDM/LEDM tab.select apply filter button
        """
        self.driver.click("apply_filters_btn")

    def select_filtered_cdm_tree(self):
        """
        click filtered in CDM tab
        """
        self.driver.click("filter_json")
    
    def get_filterd_cdm_text(self):
        """
        get the text of the filter notification
        """
        return self.driver.get_attribute("filter_json", "text")
    
    def get_filter_cdm_text_popup_content(self):
        """
        get the text of the filter notification
        """
        return self.driver.get_attribute("filter_text", "text")
    
    def select_add_invalid_button(self):
        """
        in filter CDM/LEDM tab.select add invalid button  
        """
        self.driver.click("add_invalid_btn")        

    def select_send_ui_event_option(self, option):
        """ 
        in data collection tab, select the send ui event option
        """
        if option not in ['Simple Ui Event', 'Notifications', 'UI event with Notifications']:
            raise ValueError("{}: is not a valid option within the send ui event drop down menu".format(option))
        
        self.driver.click("simple_ui_event")
        self.driver.click("simple_ui_event_dropdown", format_specifier=[option])

    def select_accumulator_button(self):
        """
        in data collection service tab.select accumulator button
        """
        self.driver.click("accumulator_btn")

    def select_accumulator_flush_button(self):
        """
        in accumulator tab.select accumulator flush button 
        """
        self.driver.click("flush_btn") 

    def select_accumulator_back_button(self):
        """
        in accumulator tab.select accumulator back button 
        """
        self.driver.click("back_btn") 

    def select_binding_filter_button(self):
        """
        in binding tab.select binding filter button from list
        """
        self.driver.click("bindings_filter_btn") 

    def select_next_button(self):
        """
        in data collection tab.select next button 
        """
        self.driver.click("next_btn") 

    def select_send_button(self):
        """
        in data collection tab.select send button 
        """
        self.driver.click("send_btn") 

    def get_telemetry_text(self):
        """
        get the text of telemetry conetent from bindings tab 
        """
        return self.driver.get_attribute("telemetry_content", "text")

    def set_tree_gun_box_value(self, text):
        """
        Clears the content of the input field identified by 'tree_gun_box' and sets it to the provided value.
        """
        self.driver.send_keys("tree_gun_box", text) 

    def set_number_of_calls_value(self, text):
        """
        Clears the content of the input field identified by nuber of calls and sets it to the provided value.
        """
        self.driver.send_keys("number_of_calls", text)  
	
    def verify_count_of_data_valve_ingress(self):
        """
        From the data valve tab, get the length of the data valve list
        """
        return len(self.driver.find_object("count_title", multiple=True))

    def get_verbose_logs_content_text(self):
        """
        get the text of the filter notification
        """
        return self.driver.get_attribute("verbose_logs_content", "text")

    def verify_queue_contents(self): 
        """ 
        in list queue items tab extract the content to verify whether the screen is empty
        """
        return not self.driver.wait_for_object("list_queue_content", timeout=3, raise_e=False) is False 

    def get_bindings_time_to_expire_text(self):
        """
        Get the current time of bindings
        """
        return self.driver.get_attribute("time", "text")