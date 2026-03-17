import pytest
from time import sleep
import json

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
        cls.account_login_id = cls.data_collection_test_data["account_login_id"]
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.ios_app_instance_id = cls.data_collection_test_data["ios_app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]

        cls.app_instance_id_send_ui = cls.data_collection_test_data["app_instance_id_send_ui"]
        cls.account_login_id_send_ui = cls.data_collection_test_data["account_login_id_send_ui"]
        cls.stratus_user_id_send_ui = cls.data_collection_test_data["stratus_user_id_send_ui"]
        cls.device_id_send_ui = cls.data_collection_test_data["device_id_send_ui"]
        cls.edge_type_send_ui = cls.data_collection_test_data["edge_type_send_ui"]
        cls.tenant_id_send_ui = cls.data_collection_test_data["tenant_id_send_ui"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]

    @pytest.fixture(scope="function", autouse="true")
    def data_collection_home_setup(self):
        self.fc.flow_load_home_screen()
        self.fc.select_stack(self.stack)
    
    def test_01_send_ui_event_with_valid_values(self):
        """
        C30482040: Send a UI event checking metadata within the Bindings and Request tab
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", "03e2611f-4481-43d7-aae9-239ace2928a5"), 
                         ("stratus_user_id_textbox", "618db54b8d8f7425c87790c1"), ("device_id_textbox", "13eb5ae1-13a5-4ef4-aa0f-8e810101ffd2")]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"

    def test_02_send_ui_event_with_empty_field(self):
        """
        C30482041: Given a missing ScreenName value, verify that SendUi test button is disabled
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", "03e2611f-4481-43d7-aae9-239ace2928a5"), 
                          ("stratus_user_id_textbox", "618db54b8d8f7425c87790c1"), ("device_id_textbox", "13eb5ae1-13a5-4ef4-aa0f-8e810101ffd2")]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.clear_textbox("screen_name_textbox")
        assert self.data_collection_plugin.is_send_ui_event_text_button_enabled() is False

    def test_03_send_ui_event_with_empty_custom_metadata(self):
        """
        C30482042: Send a UI event when custom metadata has empty required parameters on Settings
        - In JWebDataCollection settings, check textbox using custom empty Metadata values
        - Within Data collection Plugin, SendUI event, and verify result is not present within the Bindings and Requests tab
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("stratus_user_id_textbox", "618db54b8d8f7425c87790c1"), 
                         ("device_id_textbox", "13eb5ae1-13a5-4ef4-aa0f-8e810101ffd2")]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        assert not self.data_valve.get_v1bindings_text()
        self.data_valve.select_data_valve_back_button()
        self.data_valve.select_request_logs_button()
        assert self.data_valve.verify_request_log_url() is False

    def test_04_send_ui_event_when_values_store_values_set(self):
        """
        C32603186: Send a ui event when values store values are set
        - navigate to settings tab, enable values store toggle
        - fill up all the required valvecontroller parameters under value store
        - using data collection refApp, navigate to webview tab > data collection plugin
        - enable sendsimpleuievent
        - enable the tracking identifier toggle button
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the responseCode = 200
        - In finish notification event, verify the result = success
        """
        if self.stack == "pie":
            pytest.skip("No SendUI Values available for Pie Stack")
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.ios_app_instance_id), ("ios_settings_vs_stratus_user_id", self.stratus_user_id_send_ui),
                          ("ios_settings_vs_tenant_id", self.tenant_id_send_ui), ("ios_settings_vs_consent_basis_id", self.ios_app_instance_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'] is False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['valveControllerHttpResponse'])
        assert "'responseCode': 200" in telemetry_response_str
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    def test_05_send_ui_event_when_values_store_values_set_to_null(self):
        """
        C32603175: Send a ui event when values store values are set as null
        - navigate to settings tab, enable values store toggle
        - clear all the valvecontroller parameters under value store
        - using data collection refApp, navigate to webview tab > data collection plugin
        - enable sendsimpleuievent and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", ""),("ios_settings_vs_stratus_user_id", ""), 
                          ("ios_settings_vs_account_login_id", ""), ("ios_settings_vs_tenant_id", ""), ("ios_settings_vs_consent_basis_id", "") ]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'] is False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['httpRequestError'])
        assert "valveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_06_send_ui_event_when_required_values_are_missing_in_value_store(self):
        """
        C32603191: Send an ui event when required values are missing in value store
        - navigate to settings tab, enable values store toggle
        - fill up the valvecontroller parameters and leave "appinstanceid" field as blank 
        - using data collection refApp, navigate to webview tab > data collection plugin
        - enable sendsimpleuievent and include tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        if self.stack == "pie":
            pytest.skip("No SendUI Values available for Pie Stack")
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", ""), ("ios_settings_vs_stratus_user_id", self.stratus_user_id_send_ui), 
                          ("ios_settings_vs_account_login_id", self.account_login_id_send_ui), ("ios_settings_vs_tenant_id", self.tenant_id_send_ui),
                          ("ios_settings_vs_consent_basis_id", '')]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'] is False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['httpRequestError'])
        assert "valveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_07_send_ui_event_when_invalid_data_sent_in_event_detail(self):
        """
        C32603178: send ui event when invalid data is sent in event detail
         - navigate to settings tab, disable value store toggle
         - using data collection refApp, navigate to webview tab > data collection plugin
         - fill up all the required parameters in valvecontroller metadata component
         - enable the SendSimpleUiEvent, valvecontrollermetadata and tracking identifier toggle buttons
         - enter "invalid" value in the screen name field (required field)
         - click on the send ui test button twice
         - navigate to request tab, click on data ingress and verify the status code should be 206 for first attempt
         - navigate to request tab, click on data ingress and verify the status code should be 400 for second attempt
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(False)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                         ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.clear_textbox("screen_name_textbox")
        self.data_collection_plugin.send_texts_to_textboxes([('screen_name_textbox','invalid')])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        sleep(5)
        self.home.select_data_valve_tab()
        self.data_valve.select_request_logs_button()
        self.data_collection_settings.ios_select_data_ingress_btn()
        self.data_collection_settings.verify_data_ingress_controller_status_code("Status Code: 400")
        self.data_collection_settings.verify_data_ingress_controller_status_code("Status Code: 206")

    def test_08_send_ui_event_by_enabling_ui_event(self):
        """
        C32603171: Send a UI event by enabling UI event
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required valvecontroller parameters
        - enable sendsimpleuievent toggle button
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the preBuild status as "False"
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the responseCode = 200
        - In finish notification event, verify the result = success
        - Navigate to data valve tab and select the bindings cache button
        - assert the filter id from Filter Notification results is exists in bindings cache response
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == "UI event Sent!"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'] == False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    def test_09_verify_response_if_both_enable_ui_event_and_enable_notification_are_disabled(self):
        """
        C32603190: Verify the response if both Enable UI Event/Enable Notification are disabled
        - navigate to settings tab, enable the verbose logs toggle
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendsimpleuievent toggle button
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - navigate to data valve tab
        - verify the notification event entries in the verbose logs
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id_send_ui), 
                         ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.expand_data_collection_method("sendUiEventItem")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_valve_tab()
        self.data_valve.select_verbose_logs_button()
        self.data_valve.select_verbose_logs_finish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Finish Notification Status: failure' in result
        self.data_valve.select_verbose_logs_back_button()
        self.data_valve.select_verbose_logs_publish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Publish Notification Status: The operation couldn’t be completed' in result

    def test_10_send_ui_event_with_empty_field(self):
        """
        C32603180: Send a UI event when required field has no data or empty in event detail
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendsimpleuievent toggle
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - clear ScreenName field and verify that SendUi test button is disabled
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id_send_ui), 
                         ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.clear_textbox("screen_name_textbox")
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        assert self.data_collection_plugin.is_send_ui_event_text_button_enabled() is False