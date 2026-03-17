import ast
import json
from time import sleep, time
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web import const as w_const
from selenium.common.exceptions import *

class NoNotificationFoundException(Exception):
    pass

class DataCollectionPlugin(JwebFlow):
    flow_name = "data_collection_plugin"
    available_textboxes = ['asset_type_textbox', 'app_instance_id_textbox', 'account_login_id_textbox', 'stratus_user_id_textbox', 'device_id_textbox',
                           'country_textbox', 'edge_type_textbox', 'cdm_tree_gun_textbox', 'resource_uri_textbox', 'activity_name_textbox',
                           'screen_name_textbox', 'screen_path_textbox', 'screen_mode_textbox', 'control_name_textbox', 'control_detail_textbox', 'tenant_id_textbox']

    def expand_data_collection_method(self, method, expand=True, scroll=False):
        """
        Select the doc provider method to expand or contract the method view 
        :param method: method name to expand. Must be present within list below
        :param scroll: bool to scroll to the method if not visible
        """
        if method not in ["invalidateCache", "valveControllerMetadata", "filterCDMTrees", "filterLEDMTrees", "sendUiEventItem", "trackingEvents"]:
            raise ValueError("{}: is not a method on the doc provider page".format(method))
        if str(expand).lower() == self.driver.get_attribute("data_collection_method", attribute="aria-expanded", format_specifier=[method]):
            return True
        if scroll:
            found = self.driver.wait_for_object("data_collection_method", raise_e=False, timeout=3)
            timeout = time() + 5
            while not found and timeout > time():
                self.driver.swipe(direction="down")
                found = self.driver.wait_for_object("data_collection_method", raise_e=False, timeout=3)
        try:
            self.driver.click("data_collection_method", format_specifier=[method])
        except ElementClickInterceptedException:
            self.driver.swipe(direction="down")
            self.driver.click("data_collection_method", format_specifier=[method])

    def change_stack(self, stack):
        """
        In DataCollectionSettings, change the stack to the stack param
        """
        stack = 'staging' if stack == "stage" else stack.lower()
        if stack not in ['pie', 'prod', 'staging', 'dev']:
            raise ValueError("{}: is not a valid stack, expecting 'pie', 'prod', 'stage', 'dev'".format(stack))
        self.driver.click("stack_menu_selector")
        self.driver.click("stack_menu_item", format_specifier=[stack])

    def select_invalidate_cache_test_btn(self):
        """
        in DataCollection.invalidateCache(), select the test button
        """
        self.expand_data_collection_method("invalidateCache")
        self.driver.click("invalidate_cache_test_btn")

    def get_invalidate_cache_test_result(self):
        """
        :returns: the text result from DataCollection.invalidateCache() after selecting the test button
        """
        return self.driver.get_attribute("invalidate_cache_test_result", "text")

    def select_asset_unit_item(self, unit_type):
        """ 
        in ValveControllerMetadata, select the asset unit drop down and select unit_type
        """
        if unit_type not in ['desktop', 'mobile', 'solution']:
            raise ValueError("{}: is not a unit_type. unit_type must be: 'desktop' 'mobile' or 'solution'")
        
        self.expand_data_collection_method("valveControllerMetadata")
        self.driver.click("asset_unit_menu_selector")
        self.driver.click("drop_down_menu_item", format_specifier=[unit_type])

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        for textbox, text in texts_list:
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        Enter text into a textbox found in either the CDM or LEDM tree pages if the text value is not already present
        """
        if object_id not in self.available_textboxes:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))

        if object_id == "resource_uri_textbox":
            self.expand_data_collection_method("filterLEDMTrees")

        if self.driver.get_attribute(object_id, "value") != text:
            self.driver.click(object_id)
            self.driver.clear_text(object_id)
            self.driver.send_keys(object_id, text)

    def select_cdm_tree_file_selector(self):
        """ 
        in DataCollection.filterCDMTrees, select the choose files button
        """
        if self.driver.driver_info['platform'].lower() == 'android':
            self.driver.swipe(direction='down')
            self.driver.switch_to_webview()
            weblet_bounds = self.driver.wait_for_object("jarvis_weblet", clickable=True).get_attribute("bounds")
            comma_index = weblet_bounds.find("]") 
            weblet_pos = ast.literal_eval(weblet_bounds[:comma_index+1] + "," + weblet_bounds[comma_index+1:])
            weblet_size = weblet_pos[1][0]-weblet_pos[0][0], weblet_pos[1][1]-weblet_pos[0][1]
            self.driver.switch_to_webview(webview_url='index.html#/data_collection')
            choose_file_obj = self.driver.wait_for_object("cdm_tree_file_selector")
            choose_file_pos = self.driver.selenium.execute_script("return arguments[0].getBoundingClientRect()", choose_file_obj)
            webview_size = self.driver.wdvr.get_window_size()
            scaling_factor = weblet_size[0]/webview_size['width'], weblet_size[1]/webview_size['height']
            choose_file_center_pos = (choose_file_pos['x']+choose_file_pos['width']/2)*scaling_factor[0], \
                                        (choose_file_pos['y']+choose_file_pos['height']/2)*scaling_factor[1] + weblet_pos[0][1]
            self.driver.click_by_coordinates(x=choose_file_center_pos[0], y=choose_file_center_pos[1])
        else:
            self.driver.switch_to_webview()
            self.driver.click("done_btn", raise_e=False)
            self.driver.switch_to_webview(webview_url='index.html#/data_collection')
            if cdm_tree_file_selector := self.driver.wait_for_object("cdm_tree_file_selector", raise_e=False, timeout=2):
                if cdm_tree_file_selector.rect['y'] <= 65:
                    self.driver.swipe(direction='up', per_offset=0.75)
            self.driver.click_element_by_offset("cdm_tree_file_selector", x=0.2, y=0)

    def select_send_simple_ui_event_toggle(self):
        """
        in DataCollection.Publisher.publish, select send simple ui event toggle
        """
        self.expand_data_collection_method("sendUiEventItem")
        self.driver.click("send_simple_ui_event_toggle")

    def select_tracking_identifier_button(self):
        """
        in DataCollection.Publisher.publish, select tracking identifier button
        """
        self.driver.click("select_tracking_identifier_toggle")

    def select_include_vc_metadata_in_event_data_toggle(self):
        """
        in DataCollection.Publisher.publish, select send simple ui event button
        """
        self.driver.click("select_include_vc_metadata_in_event_data_toggle")

    def send_ui_event_to_publishing_test_button(self):
        """
        in DataCollection.Publisher.publish, select the test button 
        """
        self.expand_data_collection_method("sendUiEventItem")
        self.driver.click("send_ui_event_to_publishing_btn")

    def select_simplified_cdm_tree_result_checkbox(self, value):
        """ 
        in DataCollection.filterCDMTrees, set the 'Simplified Result' checkbox to value param
        """
        if str(value).lower() != self.driver.get_attribute("simplified_cdm_tree_result_checkbox_value", "value", displayed=False):
            self.driver.click("simplified_cdm_tree_result_checkbox_toggle")

    def select_filter_cdm_tree_test_button(self, change_check=None):
        """
        in DataCollection.filterCDMTrees, select the test button 
        """
        self.driver.click("filter_cdm_tree_test_btn", retry=5, delay=4, change_check=change_check)

    def get_filter_cdm_tree_result_text(self, get_json=True):
        """
        in DataCollection.filterCDMTrees, return the result text or json after selecting the test button
        """
        for i in range(3):
            if 'Nothing to show' in self.driver.get_attribute("filter_cdm_tree_test_result", "text"):
                sleep(4)
        
        if get_json:
            return json.loads(self.driver.get_attribute("filter_cdm_tree_test_result", "text"))
        else:
            return self.driver.get_attribute("filter_cdm_tree_test_result", "text")

    def select_ledm_tree_file_selector(self):
        """
        in DataCollection.filterLEDMTrees, select the choose files button
        """        
        if self.driver.driver_info['platform'].lower() == 'android':
            self.driver.swipe(direction='down')
            self.driver.switch_to_webview()
            weblet_bounds = self.driver.wait_for_object("jarvis_weblet").get_attribute("bounds")
            comma_index = weblet_bounds.find("]") 
            weblet_pos = ast.literal_eval(weblet_bounds[:comma_index+1] + "," + weblet_bounds[comma_index+1:])
            weblet_size = weblet_pos[1][0]-weblet_pos[0][0], weblet_pos[1][1]-weblet_pos[0][1]
            self.driver.switch_to_webview(webview_url='index.html#/data_collection')
            choose_file_obj = self.driver.wait_for_object("ledm_tree_file_selector")
            choose_file_pos = self.driver.selenium.execute_script("return arguments[0].getBoundingClientRect()", choose_file_obj)
            webview_size = self.driver.wdvr.get_window_size()
            scaling_factor = weblet_size[0]/webview_size['width'], weblet_size[1]/webview_size['height']
            choose_file_center_pos = (choose_file_pos['x']+choose_file_pos['width']/2)*scaling_factor[0], \
                                        (choose_file_pos['y']+choose_file_pos['height']/2)*scaling_factor[1] + weblet_pos[0][1]
            self.driver.click_by_coordinates(x=choose_file_center_pos[0], y=choose_file_center_pos[1])
        else:
            self.driver.switch_to_webview()
            self.driver.click("done_btn", raise_e=False)
            self.driver.switch_to_webview(webview_url='index.html#/data_collection')
            if ledm_tree_file_selector := self.driver.wait_for_object("ledm_tree_file_selector", raise_e=False, timeout=2):
                if ledm_tree_file_selector.rect['y'] <= 65:
                    self.driver.swipe(direction='up', per_offset=0.75)
            self.driver.click_element_by_offset("ledm_tree_file_selector", x=0.2, y=0)

    def select_simplified_ledm_tree_result_checkbox(self, value):
        """
        in DataCollection.filterLEDMTrees, set the 'Simplified Result' checkbox to value param
        """
        if str(value).lower() != self.driver.get_attribute("simplified_ledm_tree_result_checkbox_value", "value", displayed=False):
            self.driver.click("simplified_ledm_tree_result_checkbox_toggle")

    def select_filter_ledm_tree_test_button(self):
        """
        in DataCollection.filterLEDMTrees, select the test button 
        """
        self.driver.click("filter_ledm_tree_test_btn")

    def get_filter_ledm_tree_result_text(self, get_json=True):
        """
        in DataCollection.filterLEDMTrees, return the result text or json after selecting the test button
        """
        for i in range(3):
            if 'Nothing to show' in self.driver.get_attribute("filter_ledm_tree_test_result", "text"):
                sleep(4)

        if get_json:
            return json.loads(self.driver.get_attribute("filter_ledm_tree_test_result", "text"))
        else:
            return self.driver.get_attribute("filter_ledm_tree_test_result", "text")
        
    def select_ui_action_item(self, ui_action):
        """ 
        in SendUiEvent, select the UI action drop down and select ui_action
        """
        if ui_action not in ['ScreenDisplayed', 'ControlButtonClicked', 'ControlTileClicked', 'ControlHyperLinkClicked']:
            raise ValueError("{}: is not a valid ui_action within the UI action drop down menu".format(ui_action))
        
        self.driver.click("action_menu_selector")
        self.driver.click("drop_down_menu_item", format_specifier=[ui_action])

    def is_send_ui_event_text_button_enabled(self):
        """
        In SendUiEvent, return bool indicated if send_ui_event_test button is enabled
        """
        return self.driver.wait_for_object("send_ui_event_test_btn").get_attribute('disabled') is None

    def get_send_ui_event_test_result(self):
        """
        in SendUiEvent, return the result text
        """
        return self.driver.get_attribute("send_ui_event_test_result", "text")
    
    def select_sendprebuiltnotification_button(self):
        """
        in DataCollection.Publisher.publish, select sendprebuiltnotification button
        """
        self.expand_data_collection_method("sendUiEventItem")
        self.driver.click("send_prebuilt_notification_toggle")

    def select_mock_notification_button(self):
        """
        in DataCollection.Publisher.publish, select mock notification button, which appears after enabling sendprebuiltnotification button
        """
        self.driver.click("mock_notification_toggle")

    def get_number_of_notifications(self):
        """
        Under tracking events, return the number of event notifications on the page as an int
        """
        self.expand_data_collection_method("trackingEvents")
        try:
            assert self.driver.wait_for_object("expand_event_notification", timeout=2)
            return len(self.driver.find_object("expand_event_notification", multiple=True))
        except (TimeoutException, NoSuchElementException):
            raise NoNotificationFoundException("No Notification found under tracking events")

    def expand_notification_event(self, index=0, direction="down"):
        """
        Under tracking events, expand the second finish notification event
        :index: 0 - oldest notification at the bottom
                len(self.get_number_of_notifications()) - newest notification at the top
        """
        try: 
            self.driver.click("expand_event_notification", index=self.get_number_of_notifications()-index-1)
        except ElementClickInterceptedException:
            self.driver.swipe(direction=direction, per_offset=0.65)
            self.driver.click("expand_event_notification", index=self.get_number_of_notifications()-index-1)

    def get_tracking_event_results(self, index, get_json=True):
        """
        After event is published , list of notifications (build, filter, publish and finish) will be displayed under tracking events 
        Using this function, taking up the result text of each notifications under tracking events
        """
        if get_json:
            return json.loads(self.driver.get_attribute("notification_event_text", attribute="text", index=self.get_number_of_notifications()-index-1, displayed=False))
        else:
            return self.driver.get_attribute("notification_event_text", attribute="text", index=self.get_number_of_notifications()-index-1, displayed=False)
    
    def select_upload_notification_file_selector(self):
        """
        in webview tab.SendPrebuiltNotification, select the upload notification file button 
        """
        self.driver.click("upload_notification_file")

    def verify_filter_ids(self, index=0):
        """
        - From filter notification event result text, grabbing the result and verifying with valid result which are returned
        - Storing the first filterId in partially_filter_id
        """
        filter_notification_result = self.get_tracking_event_results(index=index)
        valve_filter_result = filter_notification_result['valveFilterResult']
        if 'Skipped' in valve_filter_result:
            assert valve_filter_result == 'Skipped due to preexisting filter operation'
        else:
            partially_filter_id_index = valve_filter_result.find('"filterId":')
            filter_id_end = valve_filter_result.find(',', partially_filter_id_index)
            filter_id = valve_filter_result[partially_filter_id_index + len('"filterId":'):filter_id_end]
            partially_filter_id = int(filter_id) 

class IOSDataCollectionPlugin(DataCollectionPlugin):
    context = "NATIVE_APP"

    def clear_textbox(self, object_id):
        """
        Enter text into a textbox found in either the CDM or LEDM tree pages 
        """
        self.driver.switch_to_webview(w_const.WEBVIEW_URL.JWEB_DATA_COLLECTION)
        self.driver.click(object_id)
        self.driver.switch_to_webview()
        self.driver.click(object_id)
        self.driver.long_press(object_id)
        self.driver.click("select_all_btn")
        self.driver.click("delete_btn")
        self.driver.click("done_btn")

    def verify_filter_result(self, filter_id, bindings_cache_response):
        """
        Pick the filter_id from filter notification text and verify the same filter id exists in binding cache response
        """
        assert str(filter_id) in bindings_cache_response, "Filter Id: {} not found within Bindings Cache Response: {}".format(filter_id, bindings_cache_response)

    def select_upload_notification_file_selector(self):
        """
        in webview tab.SendPrebuiltNotification, select the upload notification file button using Native iOS locator
        """
        self.driver.scroll("upload_notification_file")
        super().select_upload_notification_file_selector()

    def verify_filter_result_of_partially_filtered_file(self, partially_filter_id, bindings_response_filter_id, bindings_cache_response):
        """
        verify the filter id's present in the filter notification result with the filter id's present in the bindings cache response    
        """
        assert str(bindings_response_filter_id) in bindings_cache_response, "Filter Id: {} not found within Bindings Cache Response: {}".format(bindings_response_filter_id, bindings_cache_response)
        assert str(partially_filter_id) in bindings_cache_response, "Filter Id: {} not found within Bindings Cache Response: {}".format(partially_filter_id, bindings_cache_response)

    def verify_filter_result_of_multiple_partially_filtered_file(self, filter_id_list, bindings_cache_response):
        """
        verify the list of filter id's present in the filter notification result with the filter id's present in the bindings cache response    
        """
        for filter_id in filter_id_list:
            assert str(filter_id) in bindings_cache_response, "Filter Id: {} not found within Bindings Cache Response: {}".format(filter_id, bindings_cache_response)