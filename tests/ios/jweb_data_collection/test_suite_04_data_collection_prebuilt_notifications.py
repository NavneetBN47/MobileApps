import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID
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

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send files to iOS Device, and delete file once tests are complete
        """
        
        file_names = ["partialFiltered.json", "filteredNotificationObject.json", "empty.json", "invalid.json", "second_partial_filtered.json"]
        for file_name in file_names:
            if file_name == "second_partial_filtered.json":
                self.driver.push_file(BUNDLE_ID.FIREFOX, input_file=ma_misc.get_abs_path(f"resources/test_data/jweb/partialFiltered.json"), file_name="second_partial_filtered.json")
            else:
                self.driver.push_file(BUNDLE_ID.FIREFOX, ma_misc.get_abs_path(f"resources/test_data/jweb/{file_name}"))
            sleep(2)

        yield None

        for file_name in file_names:
            self.driver.delete_file(BUNDLE_ID.FIREFOX, file_name)

    def test_01_send_prebuilt_notification_with_mockup_notification_enabled(self):
        """
         C38257143: Send a notification with mockup notification enabled
         - navigate to settings tab, disable value store toggle
         - using data collection refApp, navigate to webview tab > data collection plugin
         - fill up all the required parameters in valvecontroller metadata component
         - enable sendprebuiltnotification and mockup notification toggle buttons
         - enable the valvecontrollermetadata and tracking identifier toggle buttons
         - click on the send ui test button
         - verify the listed notifications
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id), 
                         ("stratus_user_id_textbox", self.stratus_user_id), ("device_id_textbox", self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.data_collection_plugin.select_mock_notification_button()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert 'Service Error' in first_publish_notification_result['httpRequestError'], "Service Error not found in httpRequestError"
        self.data_collection_plugin.expand_notification_event(index=1)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_finish_notification_result['result'] == 'failure'

    def test_02_send_notification_by_uploading_partially_filtered_notification_file(self):
        """
        C32603173: Send notifications by only enabling notification for partially filtered Notification
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendprebuiltnotification toggle button
        - upload partialFiltered.json cdm object
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the preBuild status as "True"
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the responseCode = 200
        - In finish notification event, verify the result = success
        - assert the filter id from Filter Notification results is exists in bindings cache response
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("partialFiltered")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        partially_filter_id = events[0]['filter']['filterId']
        bindings_response_filter_id = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result_of_partially_filtered_file(partially_filter_id, bindings_response_filter_id, bindings_cache_response)

    def test_03_send_notification_by_uploading_empty_cdm_object(self):
        """
        C32603181: Send notifications by uploading empty cdm object
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendprebuiltnotification toggle button
        - upload empty.json cdm object
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - navigate to data valve tab
        - verify the notification event entries in the verbose logs
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id_send_ui), 
                         ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("empty")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.home.select_data_valve_tab()
        self.data_valve.select_verbose_logs_button()
        self.data_valve.select_verbose_logs_finish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Finish Notification Status: failure' in result
        self.data_valve.select_verbose_logs_back_button()
        self.data_valve.select_verbose_logs_publish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Publish Notification Status: The operation couldn’t be completed' in result

    def test_04_send_notification_by_uploading_invalid_cdm_objects(self):
        """
        C32603189: Send a notification by only enabling notification when invalid data sent over CDM object
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendprebuiltnotification toggle button
        - upload invalid.json cdm object
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - navigate to data valve tab
        - verify the notification event entries in the verbose logs
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id_send_ui), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("invalid")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.home.select_data_valve_tab()
        self.data_valve.select_verbose_logs_button()
        self.data_valve.select_verbose_logs_finish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Finish Notification Status: failure' in result
        self.data_valve.select_verbose_logs_back_button()
        self.data_valve.select_verbose_logs_publish_notification()
        result = self.data_valve.verify_verbose_log_text()
        assert 'Publish Notification Status: The operation couldn’t be completed' in result

    def test_05_send_notification_by_uploading_already_filtered_notification_file(self):
        """
        C32603172: Send notifications by only enabling notification for already filtered Notification object
        - using data collection refApp, navigate to webview tab > data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendprebuiltnotification toggle button
        - upload filteredNotificationObject.json cdm object
        - enable the tracking identifier and valvecontrollermetadata toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the preBuild status as "True"
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the responseCode = 200
        - In finish notification event, verify the result = success
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.app_instance_id_send_ui), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("filteredNotificationObject")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_filter_notification_result['valveFilterResult'] == 'Skipped due to pre-existing filter operation'
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'

    def test_06_send_notification_with_required_parameter_is_missing(self):
        """
        C32603182: Send notification with required parameter is missing when asset unit is 'solution'
        - using data collection refApp, navigate to webview tab
        - inform all the needed parameters, set asset unit as solution and leave asset type,account login id and stratus user id are empty
        - enable the toggle button sendprebuiltnotification and upload the partialFiltered file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "valveFilterResult: If assetUnit is solution then assetType should be provided."
        - In publish notification event, verify the "ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", ""), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("partialFiltered")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_filter_notification_result['valveFilterResult'] == 'If assetUnit is solution then assetType should be provided.'
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['httpRequestError'])
        assert "valveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_07_send_notification_by_enabling_notification_and_ui_event(self):
        """
        C32603174: Send notification by enabling notification and ui event
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendsimpleuievent toggle
        - enable the toggle button sendprebuiltnotification and upload the filteredNotificationObject file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the listed notifications
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("filteredNotificationObject")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'] is False
        self.data_collection_plugin.expand_notification_event(index=1)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert second_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=1)['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        second_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert second_filter_notification_result['valveFilterResult'] == 'Skipped due to pre-existing filter operation'
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert second_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=5)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    def test_08_send_notification_when_custom_metadata_with_blank_appinstanceid_on_settings_tab(self):
        """
        C32603177: Send notifications when custom metadata has <blank> appinstanceId in settings tab
        - navigate to Settings tab, enable the custom metadata toggle and leave the appinstanceId as <blank>
        - navigate to webview tab, fill up the metadata valve controller parameter values
        - enable the toggle button like sendprebuiltnotification and upload the partialFiltered file
        - enable the tracking identifier toggle
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "valveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.clear_textbox("settings_app_instance_id")
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", ""), 
                          ("stratus_user_id_textbox", self.stratus_user_id_send_ui), ("device_id_textbox", self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("partialFiltered")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
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

    def test_09_send_notification_when_value_store_values_are_set(self):
        """
        C32603187: Send a notification when values store values are set
         - navigate to settings tab, enable values store toggle
         - fill up all the required valvecontroller parameters under values store
         - using data collection refApp, navigate to webview tab
         - enable sendprebuiltnotification and upload the partialFiltered text file
         - enable the tracking identifier toggle button
         - click on the send ui test button
         - verify the published notifications under tracking events by expanding one by one notification
         - In build notification event, verify the Pre-build status as "True"
         - verify the filter notification event with respective valid assertion
         - In publish notification event, verify the status code = 200
         - In finish notification event, verify the result = success
         - assert the filter ids from Filter Notification results is exists in bindings cache response
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_vs_stratus_user_id", self.stratus_user_id_send_ui), ("ios_settings_vs_account_login_id", self.account_login_id_send_ui), 
                         ("ios_settings_vs_tenant_id", self.tenant_id_send_ui)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("partialFiltered")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        partially_filter_id = events[0]['filter']['filterId']
        bindings_response_filter_id = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result_of_partially_filtered_file(partially_filter_id, bindings_response_filter_id, bindings_cache_response)

    def test_10_send_ui_event_when_values_store_values_set_to_null(self):
        """
        C32603176: Send a notification when values store values are set as null
        - navigate to settings tab, enable values store toggle
        - using data collection refApp, navigate to webview tab
        - enable sendprebuiltnotification button and upload the partialFiltered file
        - enable tracking identifier toggle button
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", ""), ("ios_settings_vs_stratus_user_id", ""), 
                         ("ios_settings_vs_account_login_id", ""), ("ios_settings_vs_consent_basis_id", "")]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file("partialFiltered")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
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

    def test_11_send_notification_with_value_store_values_for_multiple_cdm_filtered_objects(self):
        """
        C32603192: send notification when value store values are set in the value store tab with multiple cdm filtered objects
         - navigate to settings tab, enable values store toggle
         - fill up all the required valvecontroller parameters under values store
         - using data collection refApp, navigate to webview tab
         - enable the toggle button sendprebuiltnotification and upload multiple files(filteredNotificationObject, partialFiltered)
         - enable the tracking identifier toggle button
         - click on the send ui test button
         - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
         - assert the filter id from Filter Notification results is exists in bindings cache response
        """
        self.weblet.select_info_button()
        self.weblet.select_open_settings_button()
        self.data_collection_settings.select_value_store_toggle_button(True)
        textbox_values = [("ios_settings_vs_app_instance_id", self.us_region_app_instance_id_1), ("ios_settings_vs_stratus_user_id", self.stratus_user_id_send_ui), 
                         ("ios_settings_vs_account_login_id", self.account_login_id_send_ui), ("ios_settings_vs_tenant_id", self.tenant_id_send_ui), 
                         ("ios_settings_vs_consent_basis_id", self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.fc.launch_app()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(["partialFiltered", "filteredNotificationObject"])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert second_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=1)['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_filter_notification_result['valveFilterResult'] == 'Skipped due to pre-existing filter operation'
        self.data_collection_plugin.expand_notification_event(index=3)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=4)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert first_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        second_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=5)
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        partially_filter_id = events[0]['filter']['filterId']
        bindings_response_filter_id = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=6)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        assert second_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=7)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert second_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result_of_partially_filtered_file(partially_filter_id, bindings_response_filter_id, bindings_cache_response)

    def test_12_send_notification_by_uploading_multiple_both_partially_and_filteredNotificationObjects(self):
        """
        C32603185: send notifications by only enabling notification with multiple cdm filtered objects
         - using data collection refApp, navigate to webview tab
         - fill up all the required parameters in valvecontroller metadata component
         - enable the toggle button like sendprebuiltnotification and upload multiple files(filteredNotificationObject, partialFiltered)
         - enable the valvecontrollermetadata and tracking identifier toggle buttons
         - click on the send ui test button
         - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
         - assert the filter id from Filter Notification results is exists in bindings cache response
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", self.stratus_user_id), ("device_id_textbox", self.us_region_device_id), ("tenant_id_textbox", self.tenant_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(["filteredNotificationObject", "partialFiltered"])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert second_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=1)['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        assert first_filter_notification_result['valveFilterResult'] == 'Skipped due to pre-existing filter operation'
        self.data_collection_plugin.expand_notification_event(index=3)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=4)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert first_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        second_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=5)
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        partially_filter_id = events[0]['filter']['filterId']
        bindings_response_filter_id = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=6)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        assert second_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=7)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert second_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        self.data_collection_plugin.verify_filter_result_of_partially_filtered_file(partially_filter_id, bindings_response_filter_id, bindings_cache_response)

    def test_13_send_notification_by_uploading_multiple_partially_filtered_notification_files(self):
        """
        C32603184: send notifications by only enabling notification by uploading multiple partially filtered Notification
         - using data collection refApp, navigate to webview tab
         - fill up all the required parameters in valvecontroller metadata component
         - enable the toggle button sendprebuiltnotification and upload multiple partially filtered Notification files
         - enable the valvecontrollermetadata and tracking identifier toggle buttons
         - click on the send ui test button
         - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
         - We will be getting each notification count as 2 , as we have uploaded 2 files
         - verify the listed 2 sets of notifications
         - assert the filter id from Filter Notification results is exists in bindings cache response
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), 
                          ("stratus_user_id_textbox", self.stratus_user_id), ("device_id_textbox", self.us_region_device_id), ("tenant_id_textbox", self.tenant_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(["partialFiltered.json", "second_partial_filtered.json"])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert second_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=1)['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        second_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id_1 = events[0]['filter']['filterId']
        filter_id_2 = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=3)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id_3 = events[0]['filter']['filterId']
        filter_id_4 = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=4)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=5)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=5)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_bindings_button()
        bindings_cache_response = self.data_valve.get_v1bindings_text(json=False)
        filter_id_list = [filter_id_1, filter_id_2, filter_id_3, filter_id_4]
        self.data_collection_plugin.verify_filter_result_of_multiple_partially_filtered_file(filter_id_list, bindings_cache_response)

    def test_14_send_multiple_notification_when_queue_is_disabled(self):
        """
        C32603179: Send multiple notifications - Queue Disabled
        - using data collection refApp, navigate to settings and disable the queue
        - using data collection refApp, navigate to navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(partialFiltered.json, second_partial_filtered.json)
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        - verify whether the queue tab is empty because we have disabled the queue in settings
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [("asset_type_textbox", ""), ("app_instance_id_textbox", self.us_region_app_instance_id_1), ("stratus_user_id_textbox", self.stratus_user_id), 
                          ("device_id_textbox", self.us_region_device_id), ("tenant_id_textbox", self.tenant_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(["partialFiltered.json", "second_partial_filtered.json"])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!', "UI event Sent! message not found in Sent UI Event Test Result"
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=0)['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert second_build_notification_result['preBuild'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results(index=1)['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        second_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id_1 = events[0]['filter']['filterId']
        filter_id_2 = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=3)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        tree = json.loads(first_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id_3 = events[0]['filter']['filterId']
        filter_id_4 = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_notification_event(index=4)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=5)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=5)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        assert first_publish_notification_result['valveControllerHttpResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_valve_tab()
        self.data_valve.select_queue_button()
        assert self.data_valve.verify_queue_item_lists() is True