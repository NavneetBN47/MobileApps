import json
import pytest
from time import sleep
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Data_Collection(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_data_collection_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_data_collection_setup
        cls.home = cls.fc.fd["home"]
        cls.data_valve = cls.fc.fd["data_valve"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_service = cls.fc.fd["data_collection_service"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]
        cls.local_files = cls.fc.fd["local_files"]
        cls.stack = request.config.getoption("--stack")

        cls.data_collection_test_data = cls.fc.get_data_collection_test_data(request.config.getoption("--stack"))
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]

        cls.app_instance_id_send_ui = cls.data_collection_test_data["app_instance_id_send_ui"]
        cls.account_login_id_send_ui = cls.data_collection_test_data["account_login_id_send_ui"]
        cls.stratus_user_id_send_ui = cls.data_collection_test_data["stratus_user_id_send_ui"]
        cls.device_id_send_ui = cls.data_collection_test_data["device_id_send_ui"]
        cls.edge_type_send_ui = cls.data_collection_test_data["edge_type_send_ui"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]
        cls.tenant_id_send_ui = cls.data_collection_test_data["tenant_id_send_ui"]

        with open(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json")) as cdm_tree:
            cls.valid_cdm_tree = json.loads(cdm_tree.read())

        with open(ma_misc.get_abs_path("resources/test_data/jweb/partialFiltered.txt")) as partially_filtered_object:
            cls.partially_filtered = json.loads(partially_filtered_object.read())

    @pytest.fixture(scope="function", autouse="true")
    def data_collection_home_setup(self):
        self.fc.flow_load_home_screen()
        self.fc.select_stack(self.stack)

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send files to Android Device, and delete file once tests are complete
        """
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "validcdmtree.json"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validledm.xml"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "validledm.xml"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/partialFiltered.txt"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "partialFiltered.txt"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/second_partialFiltered.txt"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "second_partialFiltered.txt"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/filteredNotificationObject.txt"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "filteredNotificationObject.txt"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/second_filteredNotificationObject.txt"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "second_filteredNotificationObject.txt"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/empty.rtf"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "empty.rtf"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/invalid.rtf"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "invalid.rtf"), overwrite=True)
        yield None
        self.driver.clean_up_device_folder(TEST_DATA.MOBILE_DOWNLOAD)

    def test_01_send_ui_event_with_valid_values(self):
        """
        C30482040: Send a UI event checking metadata within the Bindings and Request tab
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        metadata = self.data_valve.get_bindings_filter()
        assert 'appInstanceId' in metadata
        assert 'assetType' in metadata
        assert 'assetUnit' in metadata
        assert 'country' in metadata
        assert 'deviceId' in metadata
        assert 'stratusUserId' in metadata
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        data_valve_request_url = self.data_collection_service.get_newest_request_log_url()
        assert 'appInstanceId={}'.format(self.app_instance_id) in data_valve_request_url
        assert 'assetType=' in data_valve_request_url
        assert 'assetUnit=mobile' in data_valve_request_url
        assert 'country=US' in data_valve_request_url
        assert 'deviceId={}'.format(self.device_id) in data_valve_request_url

    def test_02_send_ui_event_with_empty_field(self):
        """
        C30482041: Given a missing ScreenName value, verify that SendUi test button is disabled
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.send_texts_to_textboxes([('screen_name_textbox', '')])
        assert self.data_collection_plugin.is_send_ui_event_text_button_enabled() is False

    def test_03_send_ui_event_with_empty_custom_metadata(self):
        """
        C30482042: Send a UI event when custom metadata has empty required parameters on Settings
        - In JWebDataCollection settings, check textbox using custom empty Metadata values
        - Within Data collection Plugin, SendUI event, and verify result is not present within the Bindings and Requests tab
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(2)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.select_settings_back_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''),  
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        assert len(self.data_valve.get_bindings_filter(False)) == 0
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        assert self.data_collection_service.get_newest_request_log_url(False) is False

    def test_04_send_prebuilt_notification_with_mockup_notification_enabled(self):
        """
        C38257143: Send a notification with mockup notification enabled
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and enable mockup notification toggle
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the listed notifications
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.data_collection_plugin.select_mock_notification_button()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt']
        self.data_collection_plugin.expand_notification_event(index=1)
        self.data_collection_plugin.verify_filter_ids(index=1)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=400" in telemetry_response_str, f"expecting responseCode=400 in telemetryServiceResponse:{telemetry_response_str}"
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_05_send_notification_by_uploading_already_filtered_notification_file(self):
        """
        C32603172: Send notifications by only enabling notification for already filtered Notification object
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the filterednotification file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-built status as "True"
        - In filter notification event, verify the "valveFilterResult": "Skipped due to preexisting filter operation"
        - In publish notification event, verify the response code = 200
        - In finish notification event, verify the result = success
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('filteredNotificationObject.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt']
        self.data_collection_plugin.expand_notification_event(index=1)
        self.data_collection_plugin.verify_filter_ids(index=1)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response_str
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
        - In build notification event, verify the Pre-built status as "True"
        - In filter notification event, verify the "Reason: assetType alongside with accountLoginId or stratusUserId are required when assetUnit is solution"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt']
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: Both assetType and stratusUserId are required when assetUnit is 'solution,"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: ValveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_07_send_ui_event_when_values_store_values_set_to_null(self):
        """
        C32603176: Send a notification when values store values are set as null
        - navigate to settings tab, enable values store toggle
        - clear all the valvecontroller parameters under values store and save it
        - using data collection refApp, navigate to webview tab
        - enable sendsimpleuievent and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = ['settings_vs_app_instance_id', 'settings_vs_stratus_user_id', 
                          'settings_vs_device_id', 'settings_vs_model_number', 'settings_vs_tenant_id']
        self.data_collection_settings.clear_text_from_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt'] == False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: ValveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_08_send_notification_when_values_store_values_set_to_null(self):
        """
        C32589598: Send a notification when values store values are set as null
        - navigate to settings tab, enable values store toggle
        - clear all the valvecontroller parameters under values store and save it
        - using data collection refApp, navigate to webview tab
        - enable sendprebuiltnotification and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = ['settings_vs_app_instance_id', 'settings_vs_stratus_user_id',
                          'settings_vs_device_id', 'settings_vs_model_number', 'settings_vs_tenant_id']
        self.data_collection_settings.clear_text_from_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt']
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: ValveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_09_send_ui_event_when_required_values_are_missing_in_values_store(self):
        """
        C32589613: Send an ui event when required values are missing in values store
        - navigate to settings tab, enable values store toggle
        - fill up the parameters and leave "appinstanceid" field as blank 
        - click on save button
        - using data collection refApp, navigate to webview tab
        - enable sendsimpleuievent and include trackingidentifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "Reason": "appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', ''), 
                            ('settings_vs_model_number', 'K7G93A'), ('settings_vs_tenant_id', '1625df0c-4932-4e8c-ace7-84f56d966fce')]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt'] == False
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: ValveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_10_send_notification_when_custom_metadata_with_blank_appinstanceid_on_settings_tab(self):
        """
        C32603177: Send notifications when custom metadata has <blank> appinstanceId in settings tab
        - using data collection refApp, navigate to settings tab and disable the values store switch
        - enable use custom metadata switch
        - Leave the appinstanceId and assetType as <blank>
        - click on save button
        - navigate to webview tab, enable the sendprebuiltnotification toggle button and upload the partialfiltered file
        - enable the tracking identifier toggle
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-built status as "True"
        - In filter notification event, verify the "Reason: appInstanceId is required when assetUnit is mobile or desktop"
        - In publish notification event, verify the "Error Type: ValveControllerMetadataError"
        - In finish notification event, verify the result = failure
        """                                                                         
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.clear_text_from_textbox(['settings_asset_type', 'settings_app_instanced_id'])
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt']
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: appInstanceId is required when assetUnit is mobile or desktop"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: ValveControllerMetadataError" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_11_send_ui_event_when_invalid_data_sent_in_event_detail(self):
        """
        C32589600: send ui event when invalid data is sent in event detail
        - using data collection refApp, navigate to settings tab and disable the values store switch and save it
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the SendSimpleUiEvent, valvecontrollermetadata and tracking identifier toggle buttons
        - enter "invalid" value in the screen name field (required field)
        - click on the send ui test button twice
        - navigate to request tab, click on data ingress and  verify the status code should be 206 or first attempt
        - navigate to request tab, click on data ingress and verify the status code should be 400 or second attempt
        """
        if self.stack == "pie":
            pytest.skip("No SendUI Values available for Pie Stack")
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(False)
        self.data_collection_settings.select_settings_save_button()	
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id_send_ui), ('device_id_textbox', self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_send_simple_ui_event_toggle()
        self.data_collection_plugin.send_texts_to_textboxes([('screen_name_textbox','invalid')])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        sleep(5)
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        sleep(5)
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_ingress_btn()
        assert self.data_collection_service.get_second_attempt_data_ingress_controller_status_code() == 'Status Code: 400'
        assert self.data_collection_service.get_first_attempt_data_ingress_controller_status_code() == 'Status Code: 206'

    def test_12_send_notification_by_uploading_empty_cdm_object(self):
        """
        C32603181: Send notifications by uploading empty cdm object
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the empty cdm object
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - Navigate to Verbose logs tab, verify the Invalid CDM Event error response "An error occurred while processing notification: Please provide a notification object to continue"
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('empty.rtf')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_verbose_logs_button()
        verbose_result = self.data_collection_service.get_verbose_logs_result()
        expected_reason = "An error occurred while processing notification: Please provide a notification object to continue"
        assert expected_reason in verbose_result, "Verbose logs does not contain expected reason {}".format(verbose_result)

    def test_13_send_notification_by_uploading_invalid_cdm_objects(self):
        """
        C32603189: Send a notification by only enabling notification when invalid data sent over CDM object
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the invalid cdm object file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - Navigate to Verbose logs tab, verify the Invalid CDM Event error response "An error occurred while processing notification: Please provide a notification object to continue"
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                         ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('invalid.rtf')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_verbose_logs_button()
        verbose_result = self.data_collection_service.get_verbose_logs_result()
        expected_reason = "An error occurred while processing notification: Please provide a notification object to continue"
        assert expected_reason in verbose_result, "Verbose logs does not contain expected reason {}".format(verbose_result)

    def test_14_verify_response_if_both_enable_ui_event_and_enable_notification_are_disabled(self):
        """
        C32589612: verify the response if both enable ui event and enable notification are disabled
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - Navigate to Verbose logs tab, verify the Invalid CDM Event error response "An error occurred while processing notification: Please provide a notification object to continue"
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.expand_data_collection_method("sendUiEventItem")
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_verbose_logs_button()
        verbose_result = self.data_collection_service.get_verbose_logs_result()
        expected_reason = "An error occurred while processing notification: Please provide a notification object to continue"
        assert expected_reason in verbose_result, "Verbose logs does not contain expected reason {}".format(verbose_result)

    def test_15_send_notification_by_uploading_partially_filtered_notification_file(self):
        """
        C32603173: Send notifications by only enabling notification for partially filtered Notification
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the partialFiltered file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-built status as "True"
        - From filter notification event result, grab the filter id
        - Grab the filterId from partially filtered text file and store it in partially_filtered_tree_filter_id
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                         ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        self.data_collection_plugin.verify_filter_ids(index=1)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'

    def test_16_send_notification_by_uploading_multiple_already_filtered_notification_objects(self):
        """
        C32589605: Send notifications by only enabling notification by uploading multiple already filtered Notification
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload multiple filterednotification files
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(['filteredNotificationObject.txt', 'second_filteredNotificationObject.txt'])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert second_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        self.data_collection_plugin.verify_filter_ids(index=2)
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        telemetry_response = str(second_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        self.data_collection_plugin.verify_filter_ids(index=5)
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'

    def test_17_send_notification_when_value_store_values_are_set(self):
        """
        C32603187: Send a notification when values store values are set
        - navigate to settings tab, enable values store toggle
        - fill up all the required valvecontroller parameters under values store
        - click on save button
        - using data collection refApp, navigate to webview tab
        - enable sendprebuiltnotification and upload the partialFiltered text file
        - enable the tracking identifier toggle button
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - verify the filter notification event with respective valid assertion
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', self.us_region_app_instance_id_1), 
                            ('settings_vs_model_number', 'K7G93A'), ('settings_vs_tenant_id', self.tenant_id_send_ui)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        self.data_collection_plugin.verify_filter_ids(index=1)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'success'

    def test_18_send_notification_with_value_store_values_for_multiple_cdm_filtered_objects(self):
        """
        C32603192: send notification when value store values are set in the value store tab with multiple cdm filtered objects
        - navigate to settings tab, enable values store toggle
        - fill up all the required valvecontroller parameters under values store
        - click on save button
        - using data collection refApp, navigate to webview tab
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(filteredNotificationObject, partialFiltered)
        - enable the tracking identifier toggle button
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', self.us_region_app_instance_id_1),
                            ('settings_vs_model_number', 'K7G93A'), ('settings_vs_tenant_id', self.tenant_id_send_ui)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(['partialFiltered.txt', 'filteredNotificationObject.txt'])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert second_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.verify_tracking_events()['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        self.data_collection_plugin.verify_filter_ids(index=2)
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        telemetry_response = str(second_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        self.data_collection_plugin.verify_filter_ids(index=5)
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'

    def test_19_send_notification_by_uploading_multiple_both_partially_and_filtered_notification_objects(self):
        """
        C32603185: send notifications by only enabling notification with multiple cdm filtered objects
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(filteredNotificationObject, partialFiltered)
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                        ('stratus_user_id_textbox', self.stratus_user_id_send_ui), ('device_id_textbox', self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(['partialFiltered.txt', 'filteredNotificationObject.txt'])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert second_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        self.data_collection_plugin.verify_filter_ids(index=2)
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        telemetry_response = str(second_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        self.data_collection_plugin.verify_filter_ids(index=5)
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'

    def test_20_send_notification_by_uploading_multiple_partially_filtered_notification_files(self):
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
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                        ('stratus_user_id_textbox', self.stratus_user_id_send_ui), ('device_id_textbox', self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(['partialFiltered.txt', 'second_partialFiltered.txt'])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert second_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        self.data_collection_plugin.verify_filter_ids(index=2)
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        telemetry_response = str(second_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        self.data_collection_plugin.verify_filter_ids(index=5)
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'

    def test_21_send_notification_when_custom_metadata_with_invalid_appinstanceid_on_settings_tab(self):
        """
        C32589615: Send a notification when custom metadata has "Invalid" appinstanceid on settings
        - using data collection refApp, navigate to settings tab and disable the values store
        - fill the appinstanceid field as invalid
        - click on save button
        - using data collection refApp, navigate to webview tab
        - fill up all the required parameters in valvecontroller metadata component except appinstanceid and fill it with invalid
        - enable the toggle button sendprebuiltnotification and upload the partialFiltered file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "Reason: Failed to retrieve filters to the current tree"
        - In publish notification event, verify the "Error Type: TreeNotAllowed"
        - In finish notification event, verify the result = failure
        """  
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(False)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        sleep(2)
        self.data_collection_settings.send_text_to_textbox('settings_app_instanced_id', 'invalid')
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', 'invalid'),
                        ('stratus_user_id_textbox', self.stratus_user_id_send_ui), ('device_id_textbox', self.device_id_send_ui)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_filter_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        valve_filter_result = str(first_filter_notification_result['valveFilterResult'])
        expected_reason = "Reason: Failed to retrieve filters to the current tree"
        assert expected_reason in valve_filter_result, "valve filter result does not contain expected reason {}".format(valve_filter_result)
        self.data_collection_plugin.expand_notification_event(index=2)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=2)
        telemetry_response_str = str(first_publish_notification_result['message'])
        assert "Error Type: TreeNotAllowed" in telemetry_response_str, "Error Type does not exist {}".format(telemetry_response_str)
        self.data_collection_plugin.expand_notification_event(index=3)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        assert first_finish_notification_result['result'] == 'failure'

    def test_22_send_multiple_notification_when_queue_is_disabled(self):
        """
        C32603179: Send multiple notifications - Queue Disabled
        - using data collection refApp, navigate to settings and disable the queue
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(filteredNotificationObject.txt, partialFiltered.txt)
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        - verify whether the queue tab is empty because we have disabled the queue in settings
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_queue_toggle_button(False)
        self.data_collection_settings.select_values_store_toggle_button(False)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                        ('stratus_user_id_textbox', '618db54b8d8f7425c87790c1'), ('device_id_textbox', '362721d3-79f5-495f-b553-5cee8580ee70')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.select_sendprebuiltnotification_button()
        self.fc.upload_multiple_notification_files(['filteredNotificationObject.txt', 'partialFiltered.txt'])
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        sleep(5)
        self.data_collection_plugin.expand_notification_event(index=0)
        second_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=0)
        assert second_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=1)
        first_build_notification_result = self.data_collection_plugin.get_tracking_event_results(index=1)
        assert first_build_notification_result['prebuilt'], "Build Notification assertion error {}".format(self.data_collection_plugin.get_tracking_event_results()['error'])
        self.data_collection_plugin.expand_notification_event(index=2)
        self.data_collection_plugin.verify_filter_ids(index=2)
        self.data_collection_plugin.expand_notification_event(index=3)
        second_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=3)
        telemetry_response = str(second_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=4)
        second_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=4)
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_notification_event(index=5)
        self.data_collection_plugin.verify_filter_ids(index=5)
        self.data_collection_plugin.expand_notification_event(index=6)
        first_publish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=6)
        telemetry_response = str(first_publish_notification_result['telemetryServiceResponse'])
        assert "responseCode=200" in telemetry_response
        self.data_collection_plugin.expand_notification_event(index=7)
        first_finish_notification_result = self.data_collection_plugin.get_tracking_event_results(index=7)
        assert first_finish_notification_result['result'] == 'success'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_list_queue_item_button()
        self.data_collection_service.verify_queue_item_lists() is False