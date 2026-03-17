import pytest
import json
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_data_collection_setup):
        cls = cls.__class__
        cls.stack = request.config.getoption("--stack")
        cls.driver, cls.fc = ios_jweb_data_collection_setup
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.data_valve = cls.fc.fd["data_valve"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]
        cls.weblet = cls.fc.fd["weblet"]

        cls.data_collection_test_data = cls.fc.get_data_collection_test_data(cls.stack)
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.ios_app_instance_id = cls.data_collection_test_data["ios_app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]
        cls.us_region_app_instance_id_2 = cls.data_collection_test_data["us_region_app_instance_id_2"]
        cls.app_instance_id_send_ui = cls.data_collection_test_data["app_instance_id_send_ui"]

        with open(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json")) as cdm_tree:
            cls.valid_cdm_tree = json.loads(cdm_tree.read())

    @pytest.fixture(scope="function", autouse="true")
    def data_collection_tests_setup(self):
        """ 
        Push required files to iPhone and set Data Collection stack to Dev. Upon test completion, delete pushed files
        """
        self.driver.push_file(BUNDLE_ID.FIREFOX, ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"))
        sleep(2)

        self.fc.flow_load_home_screen()
        self.fc.select_stack(self.stack)
        
        yield None
        self.driver.delete_file(BUNDLE_ID.FIREFOX, "validcdmtree.json")

    def test_01_data_collection_invalidate_cache(self):
        """
        C29821189: Invalidate bindings cache
        - using data collection refApp, navigating to the cached bindings tab and click on reset bindings, to ensure that any cache is loaded previously
        - navigating to webView tab > data collection plugin, inform all the needed parameters
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - outside of webview, navigating to the cached bindings tab to check the filterType as inclusion
        - navigate again to webview and click on invalidate cache to clear the filtering cache
        - verify "Cache Invalidated" message
        C29794271: Verify result of invalidating the bindings cache on the component reference app
        - return to the cached bindings tab
        - expected to not appear any filtering data after the cache was be cleared
        """
        self.fc.flow_load_home_screen()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        self.data_valve.select_clear_cached_bindings_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree("validcdmtree.json", "com.hp.cdm.service.eventing.version.1.resource.notification")
        sleep(3)
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        result = self.data_valve.get_v1bindings_text(json=False)
        assert "inclusion" in result
        self.home.select_webview_tab()
        self.data_collection_plugin.select_invalidate_cache_test_btn()
        self.data_collection_plugin.get_invalidate_cache_test_result() == "Cache invalidated!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert not self.data_valve.get_v1bindings_text(raise_e=False)

    def test_02_verify_invalidate_cache(self):
        """
        C29795232- Verify Invalidate cache
        - using Send UI Event, navigate through navigation bar and click on OK
        - after that navigate to data valve tab and click on bindings button
        - click on clear cached bindings button
        - verify "Cache is expired" message
        """
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        self.data_valve.select_clear_cached_bindings_button()
        assert self.data_valve.verify_bindings_cache_expired_text() == "Cache is expired"

    def test_03_make_a_request_when_the_cache_is_empty(self):
        """
        C29779395 - Make a request when the cache is empty
        - Load home screen and navigate to data valve tab
        - Click on bindings button and verify the presence of v1bindings
        - Again navigate back to home screen and click on send button
        - click on navigation bar and then click on OK
        - Navigate to data valve tab and click on bindings button,verify the absence of v1bindings
        """
        self.fc.flow_load_home_screen()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is False
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
   
    def test_04_verify_to_make_a_request_when_cache_is_expired(self):
        """
        C29779397 - Verify to make a request when cache is expired
        - Load home screen , click on send and navigate to send ui event
        - click on navigation bar and then click on OK
        - Navigate to data valve tab and click on bindings button
        - click on clear cached bindings button
        - Navigate back to home screen and click on send button and navigate to send ui event
        - Navigate to data valve tab and click on bindings button
        """
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        self.data_valve.select_clear_cached_bindings_button()
        assert self.data_valve.verify_bindings_cache_expired_text() == "Cache is expired"
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True

    def test_05_verify_to_make_a_request_when_cache_has_cached_bindings(self):
        """
        C30794744 - Verify to make a request when the cache has cached bindings
        - Load home screen and click on send button
        - navigate to send ui event and click on navigation bar , verify the event sent text and then click on OK
        - Navigate to data valve tab and click on bindings button
        - Get the initial time and store it in a variable
        - Navigate back to home screen and click on send button
        - navigate to send ui event and click on navigation bar , verify the event sent text and then click on OK
        - Navigate to data valve tab and click on bindings button
        - Get the current time and store it in a variable
        - Verify the current time is less than the initial time
        """
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        initial_time_to_expire = self.data_valve.get_bindings_time_to_expire_text()
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        current_time_to_expire = self.data_valve.get_bindings_time_to_expire_text()
        assert current_time_to_expire < initial_time_to_expire, f"Assertion failed: current time {current_time_to_expire} is not less than initial time {initial_time_to_expire}"

    def test_06_send_a_ui_event_when_required_field_has_no_data_or_empty_in_event_detail(self):
        """
        C32576215 - Send a UI event when required field has no data or empty in event detail
        - Load home screen and click on send button
        - remove the screen name text and click on navigation bar
        - verify the error type and click on back button
        - send text to screen name text and remove the action text
        - click on navigation bar and verify the error type
        - click on back button and send text to action text
        - click on navigation bar and verify the event sent popup
        - click on OK button
        """
        self.fc.flow_load_home_screen()
        self.data_valve.select_send_btn()
        self.data_valve.clear_textbox("screen_name_textbox")
        self.data_valve.click_navigation_bar()
        result = self.data_valve.verify_error_type()
        assert "invalidEvent" in result
        self.data_valve.select_back_navigation_btn()
        textbox_values = [("screen_name_textbox", "DataCollectionTab")]
        self.data_valve.send_texts_to_textboxes(textbox_values)
        self.data_valve.clear_textbox("action_textbox")
        self.data_valve.click_navigation_bar()
        result = self.data_valve.verify_error_type()
        assert "invalidEvent" in result

    def test_07_send_ui_event_when_custom_metadata_has_invalid_app_instance_id_on_settings(self):
        """
        C30794741 - Send a UI event when custom metadata has invalid appInstanceId on settings
        - Click on info button and then click on open settings button
        - Enable the value store toggle button and use custom metadata values
        - Assign the settings_app_instance_id with invalid value and launch the app
        - click on data collection tab and click on send button
        - click on navigation bar and verify the event sent popup
        - click on OK button
        - click on data valve tab and click on bindings button
        - Verify the v1bindings text is present or not
        - click on back button and click on request logs button
        - click on request logs data valve tab
        - Verify the status code is 200
        - click on back button and click on verbose logs button
        - click on filter output button and verify the reason text
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", "Invalid")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button() 
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_verbose_logs_button()
        self.data_valve.select_filter_output_btn()
        result = self.data_valve.verify_filter_output_reason_text()    
        assert "Failed to retrieve filters to the current tree" in result

    def test_08_send_ui_event_when_invalid_data_is_sent_in_event_detail(self):
        """
        C32589408 - Send a UI event when invalid data is sent in event detail
        - Load home screen and click on send button
        - remove the screen name text and put the screen name as "jdjss"
        - click on navigation bar and verify the event sent popup
        - click on OK button
        - again click on navigation bar and verify the event sent popup
        - click on OK button
        - click on data valve tab and click on bindings button
        - verify the v1bindings text is present or not
        - click on back button and click on data valve tab
        - click on request logs button and click on request logs data valve tab
        - click on data valve tab
        - Verify the first status code is 400 and second status code is 200
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_device_id", self.us_region_device_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_valve.clear_textbox("screen_name_textbox")
        textbox_values = [("screen_name_textbox", "jdjss")]
        self.data_valve.send_texts_to_textboxes(textbox_values)
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_collection_settings.ios_select_data_ingress_btn()
        assert self.data_valve.verify_data_ingress_status_code_206() == "Status Code: 206"
        assert self.data_valve.verify_data_ingress_status_code_400() == "Status Code: 400"
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
   
    def test_09_queueing_an_event(self):
        """
        C30025572 - Queueing an event
        - Click on info button and then click on open settings button
        - Disable the value store toggle button and enable the allow batch toggle button
        - Enable the queue toggle button and launch the app
        - click on data collection tab and click on send button
        - click on navigation bar and click on OK button
        - click on data valve tab and click on accumulator nav button
        - click on delete button and navigate back to home screen
        - click on data valve tab and click on queue button
        - click on data valve back button and click on data collection button
        - click on navigation bar and click on OK button
        - click on data valve tab and click on accumulator nav button
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_allow_batch_toggle_button(True)
        self.data_collection_settings.select_queue_toggle_button(True)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        self.data_valve.select_ok_btn()
        sleep(5)
        self.home.select_data_valve_tab()
        self.data_valve.select_accumulator_nav_btn()
        self.data_valve.select_delete_btn()
        self.data_valve.verify_accumulators_item_lists() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True
   
    def test_10_queueing_an_event_with_queue_flag_unactivated(self):
        """
        C30025573 - Queueing an event with queue flag unactivated
        - Click on info button and then click on open settings button
        - Disable the value store toggle button and allow batch toggle button
        - Disable the queue toggle button and launch the app
        - click on data collection tab and click on send button
        - click on navigation bar and click on OK button
        - click on data valve tab and click on queue button
        - Verify the queue item lists is present or not
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_allow_batch_toggle_button(False)
        self.data_collection_settings.select_queue_toggle_button(False)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True

    def test_11_send_a_ui_event_by_enabling_ui_event(self):
        """
        C41381071 - Send a UI event by enabling UI event
        - Load home screen and click on info button and then click on open settings button
        - Enable the value store toggle button and pass the app instance id and consent basis id
        - Load home screen and click on tracking identifier
        - click on send button and click on Nav button and verify the event sent popup
        - click on OK button and click on data valve tab
        - click on bindings button and click on data valve back button
        - click on request logs button and click on request logs data valve tab
        - Verify the status code is 200
        - click on data valve back button and click on verbose logs button
        - Click on Verbose Identifier button at index 0 and Verify the prebuilt notification text as false
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.app_instance_id_send_ui), ("ios_settings_vs_consent_basis_id", self.app_instance_id_send_ui)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.flow_load_home_screen()
        self.data_valve.select_tracking_identifier()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_verbose_logs_button()
        self.data_valve.verify_verbose_identifier_btn(index=0)
        result = self.data_valve.verify_verbose_log_built_notification_text()
        assert 'Prebuilt : false' in result

    def test_12_send_ui_events_having_same_custom_metadata_two_times_separately_to_see_merging_operation(self):
        """
        C40387610 - Send  ui events having same custom metadata two times separately to see merging operation
        - Load home screen and click on info button and then click on open settings button
        - Enable the value store toggle button and use custom batching parameters
        - Enable the allow batch toggle button and enable the verbose log switch
        - Send maximum event count as 5, minimum event count as 2 and maximum event age in seconds as 60
        - Launch the app and click on data collection tab
        - click on send button and enable the send multiple event toggle button
        - Send multiple event as 3 and click on navigation bar
        - Verify the event sent popup and click on OK button
        - click on data valve back button and click on send button
        - click on navigation bar and enable the send multiple event toggle button
        - Send multiple event as 1 and click on navigation bar
        - Verify the event not sent popup and click on OK button
        - click on data valve back button and click on data valve tab
        - click on queue button and verify the queue item lists
        - click on data valve back button and click on request logs button
        - click on request logs data valve tab
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_batching_parameters_toggle_button(True)
        self.data_collection_settings.select_allow_batch_toggle_button(True)
        self.data_collection_settings.select_enable_verbose_log_switch(True)
        textbox_values = [("maximum_event_count", "5"), ("minimum_event_count", "2"), ("maximum_event_age_in_seconds", "60")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_collection_settings.enable_send_multiple_event_toggle(True)
        self.data_collection_settings.send_multiple_event("3")
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_send_btn()
        self.data_collection_settings.enable_send_multiple_event_toggle(True)
        self.data_collection_settings.send_multiple_event("6")
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.home.select_data_valve_tab()
        self.data_valve.select_accumulator_nav_btn()
        self.data_valve.select_delete_btn()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
   
    def test_13_send_ui_events_having_different_custom_metadata_two_times_separately_to_see_if_merging_happens(self):
        """
        C40387611 - Send  ui events having different custom metadata two times separately to see if merging happens
        - Load home screen and click on info button and then click on open settings button
        - Enable the value store toggle button and use custom batching parameters
        - Enable the allow batch toggle button and enable the verbose log switch
        - Send maximum event count as 5, minimum event count as 2 and maximum event age in seconds as 60
        - Launch the app and click on data collection tab
        - click on send button and enable the send multiple event toggle button
        - Send multiple event as 6 and click on navigation bar
        - Verify the event sent popup and click on OK button
        - click on data valve back button and click on send button
        - Enable the send multiple event toggle button and send multiple event as 3
        - click on navigation bar and verify the event sent popup
        - click on OK button and click on data valve back button
        - click on data valve tab and click on accumulator nav button
        - click on delete button and click on data valve back button
        - click on queue button and verify the queue item lists
        - click on data valve back button and click on request logs button
        - click on request logs data valve tab and verify the status code is 200
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_batching_parameters_toggle_button(True)
        self.data_collection_settings.select_allow_batch_toggle_button(True)
        self.data_collection_settings.select_enable_verbose_log_switch(True)
        textbox_values = [("maximum_event_count", "5"), ("minimum_event_count", "2"), ("maximum_event_age_in_seconds", "60")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_collection_settings.enable_send_multiple_event_toggle(True)
        self.data_collection_settings.send_multiple_event("6")
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_send_btn()
        self.data_collection_settings.enable_send_multiple_event_toggle(True)
        self.data_collection_settings.send_multiple_event("3")
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.home.select_data_valve_tab()
        self.data_valve.select_accumulator_nav_btn()
        self.data_valve.select_delete_btn()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"

    def test_14_verify_to_send_a_ui_event_when_all_the_appinstanceid_value_is_assigned_to_consentbasisid(self):
        """
        C41381063 - Verify to send a UI event when all the appInstanceId value is assigned to consentBasisId
        - Click on info button and then click on open settings button
        - Assign the ios_settings_vs_consent_basis_id with ios_app_instance_id
        - Click on value store toggle button
        - Assign the ios_settings_vs_app_instance_id with app_instance_id_send_ui
        - Navigate back to home screen and click on send button
        - click on navigation bar, verify the event sent text and then click on OK
        - Navigate to data valve tab and click on accumulator nav button
        - click on delete button and navigate back to home screen
        - click on data valve tab and click on bindings button and verify the appInstanceId value
        - Verify the appInstanceId value is equal to 8e1196a9-fe74-42d2-9563-73dc486c1a97
        - Assert the appInstanceId value is equal to the expected value or not
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.app_instance_id_send_ui), ("ios_settings_vs_consent_basis_id",self.ios_app_instance_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_btn()
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        sleep(5)
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        metadata = self.data_valve.get_metadata_text()
        expected_app_instance_id = "8e1196a9-fe74-42d2-9563-73dc486c1a97"
        assert 'appInstanceId' in metadata, "appInstanceId key not found in metadata"
        assert metadata['appInstanceId'] == expected_app_instance_id, f"Expected appInstanceId '{expected_app_instance_id}', but got '{metadata['appInstanceId']}'"
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_request_logs_data_ingress_tab()
        assert self.data_valve.verify_data_ingress_status_code_200() == "Status Code: 200"

    def test_15_verify_to_send_a_system_information_event_when_appinstanceid_is_assigned_to_consentbasisid(self):
        """
        C41381064 - Verify to send a system information event when appInstanceId is assigned to consentBasisId
        - Click on info button and then click on open settings button and select toggle button
        - Assign the ios_settings_vs_app_instance_id with app_instance_id_send_ui and swipe down
        - Assign the ios_settings_vs_consent_basis_id with ios_app_instance_id and send to text boxes
        - Navigate back to home screen 
        - click on data collection button
        - click on send system information event
        - click on navigation bar 
        - click on data valve tab 
        - click on accumulator nav button
        - click on delete button
        - Navigate back to home screen
        - click on data valve tab
        - click on bindings button
        - Verify the appInstanceId value
        - Verify the appInstanceId value is equal to 8e1196a9-fe74-42d2-9563-73dc486c1a97
        - Assert the appInstanceId value is equal to the expected value or not
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.app_instance_id_send_ui), ("ios_settings_vs_consent_basis_id",self.ios_app_instance_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_send_sys_info_event()
        self.home.select_data_valve_tab()
        self.data_valve.select_accumulator_nav_btn()
        self.data_valve.select_delete_btn()
        sleep(5)
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_bindings_button()
        metadata = self.data_valve.get_metadata_text()
        expected_app_instance_id = "8e1196a9-fe74-42d2-9563-73dc486c1a97"
        assert 'appInstanceId' in metadata, "appInstanceId key not found in metadata"
        assert metadata['appInstanceId'] == expected_app_instance_id, f"Expected appInstanceId '{expected_app_instance_id}', but got '{metadata['appInstanceId']}'"
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_request_logs_data_ingress_tab()
        assert self.data_valve.verify_data_ingress_status_code_200() == "Status Code: 200"

    def test_16_send_a_batch_of_250_ui_events_at_once(self):
        """
        C40387603 - Send a batch of 250 UI events at once
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", self.us_region_app_instance_id_2)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_use_custom_batching_parameters_toggle_button(True)
        self.data_collection_settings.select_allow_batch_toggle_button(True)
        textbox_values = [("maximum_event_count", "250"),("minimum_event_count", "250"),("maximum_event_age_in_seconds", "300")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_enable_verbose_log_switch(True)
        self.data_collection_settings.select_queue_toggle_button(True)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.data_valve.select_tracking_identifier()
        self.data_valve.click_select_event_to_send()
        self.data_valve.select_ok_btn()
        self.data_valve.select_send_btn()
        self.data_collection_settings.enable_send_multiple_event_toggle(True) 
        self.data_collection_settings.send_multiple_event("250")
        self.data_valve.click_navigation_bar()
        assert self.data_valve.verify_event_sent_popup() == "Event sent"
        self.data_valve.select_ok_btn()
        self.data_valve.select_data_valve_back_button()
        self.home.select_data_valve_tab()
        sleep(5)
        self.data_valve.accumulator_flush_for_250_events()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_collection_settings.ios_select_data_ingress_btn()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_request_logs_data_valve_tab() 
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"

    def test_17_queueing_an_event_with_queue_flag_unactivated_from_weblet(self):
        """
        C30025573 - Queueing an event with queue flag un-activated
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_metadata_values_switch(False)
        self.data_collection_settings.select_allow_batch_toggle_button(False)
        self.data_collection_settings.select_queue_toggle_button(False)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True

    def test_18_make_a_request_when_the_cache_is_empty_from_weblet(self):
        """
        C29779395 - Make a request when the cache is empty
        """
        self.fc.flow_load_home_screen()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is False
        self.data_valve.select_data_valve_back_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
       
    def test_19_verify_to_make_a_request_when_cache_is_expired_from_weblet(self):
        """
        C29779397 - Make a request when the cache has expired cached bindings
        """
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        self.data_valve.verify_v1bindings_text() is True
        self.data_valve.select_clear_cached_bindings_button()
        assert self.data_valve.verify_bindings_cache_expired_text() == "Cache is expired"
        self.data_valve.verify_v1bindings_text() is False
        self.data_valve.select_data_valve_back_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert self.data_valve.verify_v1bindings_text() is True
   
    def test_20_verify_to_make_a_request_when_cache_has_cached_bindings_from_weblet(self):
        """
        C30794744 - Verify to make a request when the cache has cached bindings
        """
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        initial_time_to_expire = self.data_valve.get_bindings_time_to_expire_text()
        assert self.data_valve.verify_v1bindings_text() is True
        self.data_valve.select_data_valve_back_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        current_time_to_expire = self.data_valve.get_bindings_time_to_expire_text()
        assert current_time_to_expire < initial_time_to_expire, f"Assertion failed: current time {current_time_to_expire} is not less than initial time {initial_time_to_expire}"

    def test_21_verify_to_send_a_ui_event_when_all_the_appinstanceid_value_is_assigned_to_consentbasisid_from_weblet(self):
        """
        C41381063 - Verify to send a UI event when all the appInstanceId value is assigned to consentBasisId
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.app_instance_id_send_ui), ("ios_settings_vs_consent_basis_id",self.ios_app_instance_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        metadata = self.data_valve.get_metadata_text()
        expected_app_instance_id = "8e1196a9-fe74-42d2-9563-73dc486c1a97"
        assert 'appInstanceId' in metadata, "appInstanceId key not found in metadata"
        assert metadata['appInstanceId'] == expected_app_instance_id, f"Expected appInstanceId '{expected_app_instance_id}', but got '{metadata['appInstanceId']}'"
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        self.data_valve.select_request_logs_data_valve_tab()
        assert self.data_valve.verify_data_valve_status_code() == "Status Code: 200"
        self.data_valve.select_request_logs_data_ingress_tab()
        assert self.data_valve.verify_data_ingress_status_code_200() == "Status Code: 200"

    def test_22_queueing_an_event_from_weblet(self):
        """
        C30025572 - Queueing an event from weblet
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_allow_batch_toggle_button(True)
        self.data_collection_settings.select_queue_toggle_button(True)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_accumulator_nav_btn()
        self.data_valve.select_delete_btn()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True

    def test_23_filter_a_cdm_tree_with_a_blank_gun(self):
        """
        C32335631 -Filter a CDM tree with a blank GUN
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_device_id", self.us_region_device_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.clear_textbox("cdm_valid_gun_textbox")
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        blank_gun_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "treeNotAllowed" in blank_gun_cdm_result

    def test_24_verify_to_filter_a_valid_cdm_tree(self):
        """
        C32335625 - Verify to filter a valid CDM tree
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_device_id", self.us_region_device_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        valid_cdm_result = self.data_valve.verify_cdm_valid_filtered_result()
        valid_cdm_tree_details = self.valid_cdm_tree
        self.data_valve.verify_native_valid_cdm_tree_ui_result(valid_cdm_result, valid_cdm_tree_details)

    def test_25_verify_the_result_of_invalidate_cache_bindings(self):
        """
        C32335623 - Verify the result of invalidate Cache bindings
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_consent_basis_id", self.ios_app_instance_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        result = self.data_valve.get_v1bindings_text(json=False)
        assert "inclusion" in result
        self.data_valve.select_clear_cached_bindings_button()
        assert self.data_valve.verify_bindings_cache_expired_text() == "Cache is expired"

    def test_26_filter_a_cdm_tree_with_a_invalid_gun(self):
        """
        C32335627 - Filter a CDM tree with a invalid GUN
        """
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.clear_textbox("cdm_valid_gun_textbox")
        textbox_values = [("cdm_empty_gun_textbox", "invalid")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        invalid_gun_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "Failed to retrieve filters to the current tree" in invalid_gun_cdm_result

    def test_27_filter_invalid_cdm_tree(self):
        """
        C32335626 - Filter invalid CDM tree
        """
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_invalid_cdm_tree()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        invalid_tree_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "Failed to serialize the tree" in invalid_tree_cdm_result

    def test_28_filter_valid_cdm_tree_when_required_parameter_is_missing_for_asset_unit_desktop(self):
        """
        C32335628 - Filter valid CDM tree when required parameter is missing for asset unit desktop
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.select_asset_unit_item("Desktop")
        self.data_collection_settings.clear_textbox("settings_app_instance_id")
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        blank_gun_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "appInstanceId is required when assetUnit is mobile or desktop" in blank_gun_cdm_result

    def test_29_filter_valid_cdm_tree_when_required_parameter_is_missing_for_asset_unit_mobile(self):
        """
        C32335629 - Filter valid CDM tree when required parameter is missing for asset unit mobile
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.select_asset_unit_item("Mobile")
        self.data_collection_settings.clear_textbox("settings_app_instance_id")
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        blank_gun_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "appInstanceId is required when assetUnit is mobile or desktop" in blank_gun_cdm_result

    def test_30_filter_valid_cdm_tree_when_required_parameter_is_missing_for_asset_unit_solution(self):
        """
        C32335630 - Filter valid CDM tree when required parameter is missing for asset unit solution
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.select_asset_unit_item("Solution")
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        blank_gun_cdm_result = self.data_valve.verify_cdm_blank_gun_filtered_result()
        assert "If assetUnit is solution then assetType should be provided." in blank_gun_cdm_result

    def test_31_verify_to_filter_a_valid_multiple_cdm_tree(self):
        """
        C32335632 - Verify to filter a valid multiple CDM tree
        """
        self.fc.flow_load_home_screen()
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        textbox_values = [("settings_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_device_id", self.us_region_device_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_data_collection_tab()
        self.home.select_data_valve_tab()
        self.data_valve.select_filters_button()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_cdm()
        self.data_valve.select_add()
        self.data_valve.select_valid()
        self.data_valve.select_save()
        self.data_valve.select_selected()
        self.data_valve.select_selected_ok()
        assert self.data_valve.verify_filters_status_text() == "Filtered"
        self.data_valve.select_filtered()
        valid_cdm_result = self.data_valve.verify_cdm_valid_filtered_result()
        valid_cdm_tree_details = self.valid_cdm_tree
        self.data_valve.verify_native_valid_cdm_tree_ui_result(valid_cdm_result, valid_cdm_tree_details)
        self.data_valve.select_filters_back_btn()
        self.data_valve.select_second_filtered()
        valid_cdm_result = self.data_valve.verify_cdm_valid_filtered_result()
        valid_cdm_tree_details = self.valid_cdm_tree
        self.data_valve.verify_native_valid_cdm_tree_ui_result(valid_cdm_result, valid_cdm_tree_details)