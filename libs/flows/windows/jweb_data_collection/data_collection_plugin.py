from time import time
from time import sleep
import json
from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from selenium.common.exceptions import TimeoutException

class DataCollectionPlugin(JwebDataCollectionFlow):
    flow_name = "data_collection_plugin"

    def swipe_to_object(self, obj, direction="down"):
        """
        Within Data Collection Plugin, swipe to an object given a direction
        """
        for _ in range(10):
            if not self.driver.wait_for_object(obj, raise_e=False, timeout=1):
                self.driver.swipe(anchor_element="data_collection_header", direction=direction)
            else:
                return True
        else:
            return False

    def select_stack(self, stack):
        """
        Set JWeb Data Collection App to Stack to :stack: Production Stack not supported via Automation
        """
        stack = stack.lower()
        if stack == "stage": 
            stack = "staging"
        if stack not in ["staging", "pie", "dev"]:
            raise ValueError("Stack must be one of Staging, Pie, or Dev. Received: {}".format(stack))
        self.driver.click("server_stack_btn")
        self.driver.click("stack_option", format_specifier=[stack])

    def expand_data_collection_method(self, method, direction="down"):
        """
        Select the doc provider method to expand or contract the method view 
        param method: method name to expand. Must be present within list below
        """
        if method not in ['invalidateCache', 'ValveControllerMetadata', 'filterCDMTrees', 'filterLEDMTrees', 'Publisher', 'Tracking']:
            raise ValueError("{}: is not found within the Data Collection plugin".format(method))
        
        if self.driver.get_attribute("expand_data_collection_method", "ExpandCollapse.ExpandCollapseState", format_specifier=[method], timeout=10) == 'Collapsed':
            self.driver.click("expand_data_collection_method", format_specifier=[method])

    def select_invalidate_cache_button(self, direction="down"):
        """
        From the DataCollection.InvalidateCache() tab, select the Test btn to invalidate the cache
        """
        self.swipe_to_object("invalidate_cache_btn", direction=direction)
        self.expand_data_collection_method("invalidateCache")
        return self.driver.click("invalidate_cache_btn", delay=1, change_check={"wait_obj": "invalidate_cache_test_result", "cc_type": "wait_for_attribute", "wait_attribute": "Name", "displayed": False})

    def get_invalidate_cache_test_result(self):
        """
        From the DataCollection.InvalidateCache() tab, verify the result text
        """
        return self.driver.get_attribute("invalidate_cache_test_result", "Name", displayed=False)

    def select_asset_unit_item(self, unit_type):
        """ 
        in ValveControllerMetadata, select the asset unit drop down and select unit_type
        """
        self.swipe_to_object("asset_unit_menu_selector")
        self.expand_data_collection_method("ValveControllerMetadata")
        self.driver.click("asset_unit_menu_selector")
        self.driver.click("asset_unit_option", format_specifier=[unit_type])

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        
        for textbox, text in texts_list:
            self.swipe_to_object(textbox)
            self.driver.click(textbox, displayed=False)
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        Enter text into a textbox found in either the CDM or LEDM tree pages 
        """
        if object_id not in ['asset_type_textbox','app_instance_id_textbox', 'account_login_id_textbox', 'stratus_user_id_textbox', 'device_id_textbox', \
                             'tenant_id_textbox', 'edge_type_textbox', 'cdm_tree_gun_textbox', 'resource_uri_textbox', 'screen_name_textbox', 
                             'screen_name_value_textbox', 'count_value_textbox', 'http_proxy_href_textbox', 'count_text_box', 'action_value_textbox']:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))

        self.driver.click(object_id)
        self.driver.send_keys(object_id, text)

    def select_simplified_cdm_tree_result_checkbox(self, value):
        """ 
        in DataCollection.filterCDMTrees, set the 'Simplified Result' checkbox to value param
        """
        self.driver.check_box("simplified_cdm_tree_result_checkbox_toggle", uncheck=not value)

    def get_filter_cdm_tree_result_text(self, get_json=False):
        """
        in DataCollection.filterCDMTrees, return the result text or json after selecting the test button
        """
        for _ in range(3):
            if 'Nothing to show' in self.driver.get_attribute("filter_cdm_tree_test_result", "Name", displayed=False):
                sleep(4)
        
        if get_json:
            return json.loads(self.driver.get_attribute("filter_cdm_tree_test_result", "Name", displayed=False))
        else:
            return self.driver.get_attribute("filter_cdm_tree_test_result", "Name", displayed=False)

    def select_filter_cdm_tree_test_button(self):
        """
        in DataCollection.filterCDMTrees, select the test button 
        """
        self.swipe_to_object("filter_cdm_tree_test_btn")
        if not self.driver.click("filter_cdm_tree_test_btn", change_check={"wait_obj": "filter_cdm_tree_test_result", "cc_type": "wait_for_attribute", "wait_attribute": "Name", "displayed": False}, raise_e=False):
            self.driver.swipe(direction="down")
            self.driver.click("filter_cdm_tree_test_btn")
        
    def enable_senduieventitem_toggle(self):
        """
        in DataCollection.Publisher, select the sendUiEventItem toggle button
        """
        self.swipe_to_object("senduieventitem_toggle")
        self.expand_data_collection_method("Publisher")
        self.driver.click("senduieventitem_toggle", displayed=False)

    def enable_valvecontrollermetadata_toggle(self):
        """
        in DataCollection.Publisher, select the valveControllerMetadata toggle button
        """
        self.swipe_to_object("valvecontrollermetadata_toggle")
        self.expand_data_collection_method("Publisher")
        self.driver.click("valvecontrollermetadata_toggle", displayed=False)

    def click_send_ui_event_test_button(self):
        """
        in SendUiEvent, select the test button
        """
        self.driver.click("send_ui_event_test_btn", displayed=False)

    def is_send_ui_event_text_button_enabled(self):
        """
        In SendUiEvent, return bool indicated if send_ui_event_test button is enabled
        """
        return self.driver.wait_for_object("send_ui_event_test_btn").get_attribute('disabled') is None

    def get_send_ui_event_test_result(self):
        """
        in SendUiEvent, return the result text
        """
        return self.driver.get_attribute("send_ui_event_test_result", "Name", displayed=False)

    def enable_use_custommetdatavalue_toggle(self, value):
        """
        In Settings tab, enable use custom metadata values toggle
        """
        self.driver.check_box("use_custommetadatavalues_toggle", uncheck=not value)

    def select_cdm_file_tree_selector(self):
        """
        in DataCollection.filterCDMTrees, select the browse button 
        """
        self.swipe_to_object("cdm_tree_file_selector")
        self.expand_data_collection_method("filterCDMTrees")
        self.driver.click("cdm_tree_file_selector")

    def verify_valid_cdm_tree_ui_result(self, result_ui_event_details, valid_cdm_tree_events):
        """
        From the cdm tree ui result, verifying cdm UI result tree[events] and tree gun with the tree[events] and tree gun in the valid cdm tree file
        """
        assert (option in result_ui_event_details for option in valid_cdm_tree_events)

    def verify_valid_multiple_cdm_trees_ui_result(self, result_ui_event_details, result_2_ui_event_details, valid_cdm_tree_events):
        """
        From the multiple cdm trees ui result, verifying cdm UI result tree[events] and tree gun with the tree[events] and tree gun in the valid cdm tree file
        """
        assert (option in result_ui_event_details for option in valid_cdm_tree_events)
        assert (option in result_2_ui_event_details for option in valid_cdm_tree_events)

    def select_ledm_file_tree_selector(self):
        """
        in DataCollection.filterLEDMTrees, select the browse button 
        """
        self.swipe_to_object("ledm_tree_file_selector")
        self.expand_data_collection_method("filterLEDMTrees")
        self.driver.click("ledm_tree_file_selector")

    def select_simplified_ledm_tree_result_checkbox(self, value):
        """ 
        in DataCollection.filterLEDMTrees, set the 'Simplified Result' checkbox to value param
        """
        self.driver.check_box("simplified_ledm_tree_result_checkbox_toggle", uncheck=not value)

    def select_filter_ledm_tree_test_button(self):
        """
        in DataCollection.filterLEDMTrees, select the test button 
        """
        self.swipe_to_object("filter_ledm_tree_test_btn")
        if not self.driver.click("filter_ledm_tree_test_btn", change_check={"wait_obj": "filter_ledm_tree_test_result", "cc_type": "wait_for_attribute", "wait_attribute": "Name", "displayed": False}, raise_e=False):
            self.driver.swipe(direction="down")
            self.driver.click("filter_ledm_tree_test_btn")

    def get_filter_ledm_tree_result_text(self, get_json=False):
        """
        in DataCollection.filterLEDMTrees, return the result text or json after selecting the test button
        """
        for _ in range(3):
            if 'Nothing to show' in self.driver.get_attribute("filter_ledm_tree_test_result", "Name", displayed=False):
                sleep(4)
        
        if get_json:
            return json.loads(self.driver.get_attribute("filter_ledm_tree_test_result", "Name", displayed=False))
        else:
            return self.driver.get_attribute("filter_ledm_tree_test_result", "Name", displayed=False)

    def verify_valid_ledm_tree_ui_result(self, ledm_tree_ui_result, valid_ledm_tree_details):
        """
        From the ledm tree ui result, verifying ledm UI result[tree] and resource URI with the tree and URI in the valid ledm tree file
        """
        assert (option in ledm_tree_ui_result for option in valid_ledm_tree_details)

    def verify_valid_multiple_ledm_trees_ui_result(self, ledm_tree_ui_result_1, ledm_tree_ui_result_2, valid_ledm_tree_details):
        """
        From the multiple ledm trees ui result, verifying ledm UI result tree and resource URI with the tree and resource URI in the valid ledm tree file
        """
        assert (option in ledm_tree_ui_result_1 for option in valid_ledm_tree_details)
        assert (option in ledm_tree_ui_result_2 for option in valid_ledm_tree_details)

    def enable_send_prebuiltnotification_toggle(self):
        """
        in DataCollection.Publisher, select the sendprebuiltnotification toggle button
        """
        self.swipe_to_object("send_prebuiltnotification_toggle")
        self.expand_data_collection_method("Publisher")
        self.driver.click("send_prebuiltnotification_toggle", displayed=False)

    def enable_mock_notification_toggle(self):
        """
        in DataCollection.Publisher, select the mock notification toggle button
        """
        self.driver.click("mock_notification_toggle", displayed=False)

    def enable_include_trackingidentifier_toggle(self):
        """
        in DataCollection.Publisher, select the include trackingidentifier toggle button
        """
        self.driver.click("include_trackingidentifier_toggle", displayed=False)

    def expand_build_notification_event(self):
        """
        in DataCollection.Tracking events, expand the build notification button
        """
        self.swipe_to_object("expand_build_notification_event")
        self.expand_data_collection_method("Tracking")
        self.swipe_to_object("expand_build_notification_event")
        self.driver.click("expand_build_notification_event")

    def expand_filter_notification_event(self):
        """
        in DataCollection.Tracking events, expand the filter notification button
        """
        self.swipe_to_object("expand_filter_notification_event")
        self.driver.click("expand_filter_notification_event")

    def expand_publish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the publish notification button
        """
        self.swipe_to_object("expand_publish_notification_event")
        self.driver.click("expand_publish_notification_event")

    def verify_tracking_event_results(self, event_notification, get_json=True):
        """
        After event is published , list of notifications (build, filter and publish) will be displayed under tracking events 
        Using this function, taking up the result text of each notifications under tracking events
        """
        if event_notification not in ["build_notification_result_text", "filter_notification_result_text", "publish_notification_result_text",
                                        "second_build_notification_result_text", "second_filter_notification_result_text", "second_publish_notification_result_text",
                                        "second_finish_notification_result_text", "third_build_notification_result_text", "third_filter_notification_result_text",
                                        "third_publish_notification_result_text", "third_finish_notification_result_text"]:
                                     
            raise ValveError("{} not a notification listed in the tracking events".format(event_notification))
        
        for _ in range(2):
            if '' in self.driver.get_attribute("notification_result_event_text", "Name", displayed=False):
                sleep(5)
        
        if get_json:
            return json.loads(self.driver.get_attribute("notification_result_event_text", "Name", displayed=False))
        else:
            return self.driver.get_attribute("notification_result_event_text", "Name", displayed=False)
    
    def expand_finish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the finish notification button
        """
        self.swipe_to_object("expand_finish_notification_event", direction="up")
        self.driver.click("expand_finish_notification_event")

    def get_finish_notification_event_result_text(self, get_json=False):
        """
        in DataCollection.Tracking events, verify the finish notification event result text
        """
        for _ in range(2):
            if '' in self.driver.get_attribute("finish_notification_result_text", "Name", displayed=False):
                sleep(5)
        
        if get_json:
            return json.loads(self.driver.get_attribute("finish_notification_result_text", "Name", displayed=False))
        else:
            return self.driver.get_attribute("finish_notification_result_text", "Name", displayed=False)

    def verify_filter_result(self, filter_id, bindings_cache_response):
        """
        Pick the filter_id from filter notification text and verify the same filter id exists in binding cache response
        """
        assert (option in filter_id for option in bindings_cache_response)

    def select_upload_notification_file_selector(self):
        """
        in DataCollection.SendPrebuiltNotification, select the upload notification file button 
        """
        self.swipe_to_object("upload_notification_file")
        if not self.driver.click("upload_notification_file", change_check={"wait_obj": "upload_notification_file", "invisible": True}, raise_e=False):
            self.driver.swipe(direction="down")
            self.driver.click("upload_notification_file")

    def verify_filter_result_of_partially_filtered_file(self, partially_filter_id, partially_filtered_tree, bindings_response_filter_id, bindings_cache_response):
        """
        verify the filter id's present in the filter notitifcation result with the filter id's present in the bindings cache respone and partially filtered text file
        """
        assert (option in partially_filter_id for option in partially_filtered_tree)
        assert (option in bindings_response_filter_id for option in bindings_cache_response)

    def verify_finish_result_schema_validation_error(self, expected_schema_message, actual_schema_message):
        """
        Verify the expected schema error message text contains in the finish notification result
        """
        assert (message in expected_schema_message for message in actual_schema_message)

    def expand_second_build_notification_event(self):
        """
        in DataCollection.Tracking events, expand the second listed build notification button from bottom of the list
        """
        self.swipe_to_object("expand_second_build_notification_event")
        self.expand_data_collection_method("Tracking")
        self.swipe_to_object("expand_second_build_notification_event")
        self.driver.click("expand_second_build_notification_event")

    def expand_second_filter_notification_event(self):
        """
        in DataCollection.Tracking events, expand the second listed filter notification button from the bottom of the list
        """
        self.swipe_to_object("expand_second_filter_notification_event")
        self.driver.click("expand_second_filter_notification_event")

    def expand_second_publish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the second listed publish notification button from the bottom of the list
        """
        self.swipe_to_object("expand_second_publish_notification_event")
        self.driver.click("expand_second_publish_notification_event")

    def expand_second_finish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the second finish notification button from the bottom of the list
        """
        self.swipe_to_object("expand_second_finish_notification_event", direction="up")
        self.driver.click("expand_second_finish_notification_event")

    def verify_second_filter_result_of_multiple_partially_filtered_file(self, second_partially_filter_id, partially_filtered_tree, second_bindings_response_filter_id, bindings_cache_response):
        """
        verify the filter id's present in the second lited filter notitifcation from bottom of the list result with 
        the filter id's present in the bindings cache respone and partially filtered text file
        """
        assert (option in second_partially_filter_id for option in partially_filtered_tree)
        assert (option in second_bindings_response_filter_id for option in bindings_cache_response)

    def expand_third_build_notification_event(self):
        """
        in DataCollection.Tracking events, expand the third listed build notification button from bottom of the list
        """
        self.swipe_to_object("expand_third_build_notification_event")
        self.expand_data_collection_method("Tracking")
        self.swipe_to_object("expand_third_build_notification_event")
        self.driver.click("expand_third_build_notification_event")

    def expand_third_filter_notification_event(self):
        """
        in DataCollection.Tracking events, expand the third listed filter notification button from the bottom of the list
        """
        self.swipe_to_object("expand_third_filter_notification_event")
        self.driver.click("expand_third_filter_notification_event")

    def expand_third_publish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the third listed publish notification button from the bottom of the list
        """
        self.swipe_to_object("expand_third_publish_notification_event")
        self.driver.click("expand_third_publish_notification_event")

    def expand_third_finish_notification_event(self):
        """
        in DataCollection.Tracking events, expand the third finish notification button from the bottom of the list
        """
        self.swipe_to_object("expand_third_finish_notification_event", direction="up")
        self.driver.click("expand_third_finish_notification_event")

    def select_send_sys_info_event_btn(self):
        """
        From the DataCollection tab, select the send sytem info event button
        """
        self.driver.click("send_sys_info_event_btn")

    def get_event_send_pop_up_result(self):
        """
        From the DataCollection tab, verify the pop up result text
        """
        return self.driver.get_attribute("event_result_pop_up_text", "Name", displayed=False)

    def select_pop_up_close_button(self):
        """
        From the DataCollection tab, select the pop up close button
        """
        self.driver.click("pop_up_close_btn")

    def verify_accumulator_list(self):
        """
        From the Accumulator page, verify the accumulator list
        """
        return self.driver.wait_for_object("accumulator_list", format_specifier=[1], timeout=3, raise_e=False)

    def select_accumulator_delete_btn(self):
        """
        From the Accumulator page, select the delete button
        """
        self.driver.click("accumulator_delete_btn")

    def select_send_ui_event_btn(self):
        """
        From the DataCollection tab, select the send ui event button
        """
        self.driver.click("send_ui_event_btn")

    def select_enable_ui_event_checkbox(self, value):
        """
        From the DataCollection tab, select enable ui event checkbox
        """
        self.driver.check_box("enable_ui_event_checkbox", uncheck=not value)

    def select_enable_notification_checkbox(self, value):
        """
        From the DataCollection tab, select enable notification checkbox
        """
        self.driver.check_box("enable_notification_checkbox", uncheck=not value)

    def enter_cdm_tree_object_textbox(self, text):
        """
        From the DataCollection tab, enter text into the cdm tree object textbox
        """
        self.driver.send_keys("cdm_object_textbox", text)

    def select_add_notification_btn(self):
        """
        From the DataCollection tab, select the add notification button
        """
        self.driver.click("add_notification_btn")

    def select_valid_tree_btn(self):
        """
        From the Filters tab, select the valid tree button
        """
        self.driver.click("valid_tree_btn")

    def select_invalid_tree_btn(self):
        """
       From the Filters tab, select the invalid tree button
        """
        self.driver.click("invalid_tree_btn")

    def select_custom_tree_btn(self):
        """
        From the Filters tab, select the custom tree button
        """
        self.driver.click("custom_tree_btn")

    def select_combo_tree_list(self, tree_option):
        """
        From the Filters tab, select the combo tree list
        """
        self.driver.click("combo_tree_list")
        self.driver.click("combo_list_cdm_btn", format_specifier=[tree_option])

    def select_apply_filter_btn(self):
        """
        From the Filters tab, select the apply filter button
        """
        self.driver.click("apply_filter_btn")

    def select_filtered_pop_up_close_btn(self):
        """
        From the Filters tab, select the filtered pop up close button
        """
        self.driver.click("filtered_pop_up_close_btn")

    def get_filtered_result(self):
        """
        From the Filters tab, get the filtered result
        """
        return self.driver.get_attribute("filtered_values_result", "Name", displayed=False)

    def enter_custom_cdm_tree_object_textbox(self, text):
        """
        From the Filters tab, enter text into the custom cdm tree object textbox
        """
        self.driver.send_keys("custom_tree_text_box", text)

    def enter_custom_cdm_tree_gun_textbox(self, text):
        """
        From the Filters tab, enter text into the custom cdm tree gun textbox
        """
        self.driver.send_keys("custom_tree_tree_gun_text_box", text)

    def select_custom_send_tree_btn(self):
        """
        From the Filters tab, select the custom send tree button
        """
        self.driver.click("custom_send_tree_btn")
        
    def filters_error_pop_up_result(self):
        """
        From the Filters tab, get the error pop up result
        """
        return self.driver.get_attribute("filters_pop_up_text", "Name", displayed=False)
    
    def get_second_filtered_result(self):
        """
        From the Filters tab, get the second filtered result
        """
        return self.driver.get_attribute("second_filtered_values_result", "Name", displayed=False)

    def verify_native_valid_ledm_tree_ui_result(self, ledm_result, valid_ledm_tree_details):
        """
        From the ledm tree ui result, verifying ledm UI result[tree] and resource URI with the tree and URI in the valid ledm tree file
        """
        assert (option in ledm_result for option in valid_ledm_tree_details)

    def enter_tree_http_proxy_tree_textbox(self, file_path, textbox_id, chunk_size=1024, timeout=10):
        """
        From the HTTP Proxy tab, enter text into the tree http proxy tree textbox
        """
        try:
            textbox = self.driver.wait_for_object(textbox_id, timeout=timeout)
            with open(file_path, 'r') as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    textbox.send_keys(chunk)
                    sleep(5)
        except TimeoutException:
            raise TimeoutException("Failed to find {} textbox within {} seconds".format(textbox_id, timeout))

    def select_http_proxy_filter_tree_btn(self):
        """
        From the HTTP Proxy tab, select the filter tree button
        """
        self.driver.swipe(direction="down", distance=4)
        self.driver.click("http_proxy_filter_tree_btn", displayed=False)
    
    def clear_text_from_textboxes(self, object_ids):
        """
        Clear a textbox from the Native context (needed to clear completely clear textbox, list can be added as needed)
        """
        for object_id in object_ids:
            if object_id not in ['http_proxy_href_textbox', 'screen_name_value_textbox', 'action_value_textbox']:
                raise ValueError("{}: not present within list of textboxes".format(object_id))
            else:
                self.driver.click(object_id)
                self.driver.clear_text(object_id)
        return True

    def verify_queue_items_list(self):
        """
        From the Queue tab, get the length of the queue list
        """
        return len(self.driver.find_object("queue_list_item", multiple=True))

    def select_tree_remove_btn(self):
        """
        From the filters tab, select the remove button
        """
        self.driver.click("tree_remove_btn")