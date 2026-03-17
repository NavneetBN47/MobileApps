import json
from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from selenium.common.exceptions import *

class DataValve(JwebDataCollectionFlow):
    flow_name = "data_valve"
    available_textboxes = ['screen_name_textbox', 'action_textbox']

    def select_bindings_button(self):
        """
        Selects the Bindings page button from the Data Valves Page
        """
        self.driver.click("bindings_button")

    def select_filters_button(self):
        """
        Selects the Filters page button from the Data Valves Page
        """
        self.driver.click("filters_button")

    def select_request_logs_button(self):
        """
        Selects the Request Logs page button from the Data Valves Page
        """
        self.driver.click("request_logs_button")

    def select_verbose_logs_button(self):
        """
        Selects the Verbose Logs page button from the Data Valves Page
        """
        self.driver.click("verbose_logs_button")

    def select_queue_button(self):
        """
        Selects the Queue page button from the Data Valves Page
        """
        self.driver.click("queue_button")

    def select_data_valve_back_button(self):
        """
        Selects the back button in the top navigation of a selected Data Valve page
        """
        self.driver.click("data_valves_nav_button")

    def get_newest_request_log_url(self, raise_e=False):
        """
        From the Request Logs page, return the url found in the Data Valve request
        """
        return self.driver.get_attribute("newest_data_valve_request_url", "text", raise_e=raise_e)

    def get_metadata_text(self):
        """
        From the Bindings tab, return the Metadata json at the top of the page
        """
        return json.loads(self.driver.get_attribute("metadata_json", "text"))

    def verify_request_log_url(self):
        """
        From the Request Logs page, return bool representing presence of request url
        """
        return not self.driver.wait_for_object("newest_data_valve_request_url", timeout=3, raise_e=False) is False

    def verify_metadata_text(self):
        """
        From the Bindings tab, return bool representing presence of Metadata
        """
        return not self.driver.wait_for_object("metadata_json", timeout=3, raise_e=False) is False

    def select_clear_cached_bindings_button(self):
        """
        From the Bindings tab, selecting trash can button
        """
        self.driver.click("clear_cached_bindings") 

    def get_v1bindings_text(self, json=True, raise_e=False): 
        """
        From the Bindings tab, return the v1/bindings json at the bottom of the page
        """
        result = self.driver.get_attribute("v1bindings_json", "text", raise_e=raise_e)
        if not result and not raise_e:
            return result
        else:
            return json.loads(result) if json else result

    def verify_v1bindings_text(self):
        """
        From the Bindings tab, return bool representing presence of v1bindings
        """
        return not self.driver.wait_for_object("v1bindings_json", raise_e=False) is False

    def verify_verbose_log_text(self):
        """
        From the Verbose Logs page, return the verbose logs
        """
        return self.driver.get_attribute("verbose_log_text", "text")

    def select_verbose_logs_finish_notification(self):
        """
        From the Verbose Logs page, select the finish notification
        """
        self.driver.click("verbose_log_finish_notification") 

    def select_verbose_logs_publish_notification(self):
        """
        From the Verbose Logs page, select the publish notification
        """
        self.driver.click("verbose_log_publish_notification") 

    def select_verbose_logs_back_button(self):
        """
        From the Verbose Logs detailed page, select the back button
        """
        self.driver.click("verbose_logs_back_button")

    def verify_queue_item_lists(self): 
        """ 
        in queue tab extract the content to verify whether the screen is empty
        """
        return bool(self.driver.wait_for_object("queue_list", timeout=3, raise_e=False))

    def select_send_btn(self):
        """
        Selects the send button from home screen
        """
        self.driver.click("send_btn")

    def click_navigation_bar(self):
        """
        Clicks the navigation bar
        """
        self.driver.click("navigation_bar")

    def verify_event_sent_popup(self):
        """
        Verify that the event sent popup is displayed
        """
        return self.driver.get_attribute("event_sent_text", "text")

    def select_ok_btn(self):
        """
        Clicks the OK button
        """
        self.driver.click("select_ok_btn")

    def verify_bindings_cache_expired_text(self):
        """
        Verify the cache expired text in data valve
        """
        return self.driver.get_attribute("cache_expired_text", "text")

    def verify_error_type(self):
        """
        Verify the error type
        """
        return self.driver.get_attribute("error_type", "text")

    def select_back_navigation_btn(self):
        """
        Selects the back navigation button
        """
        self.driver.click("back_navigation_btn")

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        for textbox, text in texts_list:
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        Enter text into a textbox found in either the native if the text value is not already present
        """
        if object_id not in self.available_textboxes:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))
        
        if self.driver.get_attribute(object_id, "value") != text:
            self.driver.click(object_id)
            self.driver.clear_text(object_id)
            self.driver.send_keys(object_id, f'{text}\n')

    def clear_textbox(self, object_id):
        """
        Clear the text from a textbox
        """
        self.driver.clear_text(object_id)

    def get_bindings_time_to_expire_text(self):
        """
        Get the current time of bindings
        """
        return self.driver.get_attribute("time", "text")

    def select_request_logs_data_valve_tab(self):
        """
        Selects the request logs data valve tab
        """
        self.driver.click("request_logs_data_valve_tab")

    def verify_data_valve_status_code(self):
        """
        Verify the data valve status code
        """
        return self.driver.get_attribute("data_valve_status_code", "text")

    def select_filter_output_btn(self):
        """
        Selects the filter output button
        """
        self.driver.click("filter_output_btn")

    def verify_filter_output_reason_text(self):
        """
        Verify the filter output reason text
        """
        return self.driver.get_attribute("filter_output_reason_text", "text")

    def select_accumulator_nav_btn(self):
        """
        Selects the Accumulator nav button
        """
        self.driver.click("accumulator_nav_btn")
   
    def select_delete_btn(self):
        """
        Selects the delete button
        """
        self.driver.click("delete_btn")
   
    def select_tracking_identifier(self):
        """
        Selects the tracking identifier
        """
        self.driver.click("tracking_identifier")
   
    def verify_data_ingress_status_code_206(self):
        """
        Verify the data ingress status code 206
        """
        return self.driver.get_attribute("data_ingress_status_code_206", "text")
   
    def verify_data_ingress_status_code_400(self):
        """
        Verify the data ingress status codes 400
        """
        return self.driver.get_attribute("data_ingress_status_code_400", "text")
   
    def verify_accumulators_item_lists(self):
        """
        Verify the accumulators item lists
        """
        return bool(self.driver.wait_for_object("accumulators_item_lists", timeout=3, raise_e=False))

    def verify_verbose_identifier_btn(self, index, direction="down"):
        """
        Selects the verbose identifier button based on the index

        """
        num_identifiers = self.get_number_of_tracking_identifiers()
        try:
            self.driver.click("tracking_identifier_nav_btn", index=num_identifiers - index - 1)
        except ElementClickInterceptedException:
            self.driver.swipe(direction=direction, per_offset=0.65)
            self.driver.click("tracking_identifier_nav_btn", index=num_identifiers - index - 1)

    def get_number_of_tracking_identifiers(self):
        """
        Get the number of tracking identifiers in the verbose logs page
        """
        try:
            assert self.driver.wait_for_object("tracking_identifier_nav_btn", timeout=2)
            return len(self.driver.find_object("tracking_identifier_nav_btn", multiple=True))
        except (TimeoutException, NoSuchElementException):
            raise NoNotificationFoundException("No Tracking Identifiers found under Verbose Logs")

    def verify_verbose_log_built_notification_text(self):
        """
        Verify the verbose log built notification text
        """
        self.driver.swipe(direction="down")
        return self.driver.get_attribute("verbose_log_prebuilt_notification_text", "text")

    def verify_data_ingress_status_code_200(self):
        """
        Verify the data ingress status code 200
        """
        return self.driver.get_attribute("data_ingress_status_code_200", "text")
    
    def select_request_logs_data_ingress_tab(self):
        """
        Selects the request logs data ingress tab
        """
        self.driver.click("request_logs_data_ingress_tab")

    def select_send_sys_info_event(self):
        """
        Selects the send sys info event from home screen
        """
        self.driver.click("send_sys_info_event")

    def click_select_event_to_send(self):
        """
        Selects the select event to send from home screen
        """
        self.driver.click("select_event_to_send")

    def accumulator_flush_for_250_events(self):
        """
        Flush the accumulator for 250 events
        """
        self.select_accumulator_nav_btn()
        end_time = time.time() + 50
        while time.time() < end_time:
            pass
        self.select_delete_btn()

    def select_cdm(self):
        """
        Selects the CDM from the Filters page
        """
        self.driver.click("cdm")
   
    def select_add(self):
        """
        Selects the Add from the Filters page
        """
        self.driver.click("add")
   
    def select_valid(self):
        """
        Selects the valid from the Filters page
        """
        self.driver.click("valid")
   
    def select_save(self):
        """
        Selects the save from the Filters page
        """
        self.driver.click("save")

    def select_valid_result_text(self):
        """
        Selects the valid result text from the Filters page
        """
        self.driver.click("valid_result_text")

    def select_selected(self):
        """
        Selects the selected from the Filters page
        """
        self.driver.click("selected")

    def select_selected_ok(self):
        """
        Selects the ok from the Filters page
        """
        self.driver.click("ok")
    
    def select_filtered(self):
        """
        Selects the filtered from the Filters page
        """
        self.driver.click("filtered")

    def verify_filters_applying_text(self):
        """
        Verify the filters applying text
        """
        return self.driver.get_attribute("filters_text", "text")

    def verify_filters_status_text(self):
        """
        Verify the filters status text
        """
        return self.driver.get_attribute("filters_status_text", "text")

    def verify_cdm_valid_filtered_result(self):
        """
        Verify the cdm valid filtered result
        """
        return self.driver.get_attribute("cdm_valid_filtered_result", "text")

    def verify_native_valid_cdm_tree_ui_result(self, valid_cdm_result, valid_cdm_tree_details):
        """
        Verify the cdm tree ui result
        """
        assert (option in valid_cdm_result for option in valid_cdm_tree_details)

    def verify_cdm_blank_gun_filtered_result(self):
        """
        Verify the cdm blank gun filtered result
        """
        return self.driver.get_attribute("cdm_blank_gun_result", "text")

    def select_invalid_cdm_tree(self):
        """
        Selects the Invalid cdm tree from the Filters page
        """
        self.driver.click("invalid")
    
    def select_filters_back_btn(self):
        """
        Selects the back button from the Filters page
        """
        self.driver.click("filters_back_btn")

    def select_second_filtered(self):
        """
        Selects the second filtered from the Filters page
        """
        self.driver.click("second_filtered")