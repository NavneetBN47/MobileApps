import pytest
import json
from time import sleep
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_11_Notifications_Advanced(object):

    @pytest.mark.datacollection
    def test_01_send_notification_by_enabling_notification_and_ui_event_C32589403(self):
        """
        C32589403: Send notification by enabling notification and ui event
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendsimpleuievent toggle
        - enable the toggle button sendprebuiltnotification and upload the filterednotificationobject file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the listed notifications
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.fc.upload_single_notification_file('filteredNotificationObject.txt')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_second_build_notification_event()
        second_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_build_notification_result_text")
        assert second_build_notification_result['prebuild'] == False
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_second_filter_notification_event()
        second_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_filter_notification_result_text")
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_second_publish_notification_event()
        second_publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_publish_notification_result_text")
        assert second_publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_second_finish_notification_event()
        second_finish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_finish_notification_result_text")
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        bindings_cache_response = self.bindings_cache.verify_bindings_cache_response_text()
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    @pytest.mark.datacollection
    def test_02_enable_both_enable_ui_and_enable_notification_by_sending_multiple_cdm_objects_C32589558(self):
        """
        C32589558: Verify the response if both Enable UI Event/Enable Notification are enabled by sending multiple CDM objects
        - send ui event and notifications by uploading multiple already filtered Notification
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle buttons sendSimpleUiEvent, sendprebuiltnotification and upload multiple filterednotification files
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.fc.upload_multiple_notification_files(["filteredNotificationObject.txt", "second_filteredNotificationObject.txt"])
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_third_build_notification_event()
        third_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("third_build_notification_result_text")
        assert third_build_notification_result['prebuild'] == False
        self.data_collection_plugin.expand_second_build_notification_event()
        second_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_build_notification_result_text")
        assert second_build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_third_filter_notification_event()
        third_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("third_filter_notification_result_text")
        tree = json.loads(third_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_third_publish_notification_event()
        third_publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("third_publish_notification_result_text")
        assert third_publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_third_finish_notification_event()
        third_finish_notification_result = self.data_collection_plugin.verify_tracking_event_results("third_finish_notification_result_text")
        assert third_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_second_filter_notification_event()
        second_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_filter_notification_result_text")
        assert second_filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_second_publish_notification_event()
        second_publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_publish_notification_result_text")
        assert second_publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_second_finish_notification_event()
        second_finish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_finish_notification_result_text")
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        bindings_cache_response = self.bindings_cache.verify_bindings_cache_response_text()
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    @pytest.mark.datacollection
    def test_03_send_notification_with_value_store_values_for_multiple_cdm_filtered_objects_C32589564(self):
        """
        C32589564: send notification when value store values are set in the value store tab with multiple cdm filtered objects
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle button and click on save button
        - using data collection refApp, navigate to more and redirect to valuestore
        - fill up all the required parameters except the system serial number
        - using data collection refApp, navigate to data collection plugin
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(filteredNotificationObject, partialFiltered)
        - enable the tracking identifier toggle button
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox', 'account_login_id_textbox', 
                                                'stratus_user_id_textbox', 'device_id_textbox', 'model_number_textbox', 'tenant_id_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.app_instance_id), ('vs_stratus_user_id_textbox', self.stratus_user_id), ('vs_account_login_id_textbox', self.account_login_id),
                            ('vs_device_id_textbox', self.us_region_device_id), ('vs_model_number_textbox', '53N95A'), ('vs_tenant_id_textbox', self.tenant_id),
                            ('vs_system_serial_number_textbox', ''), ('vs_pc_device_uuid_textbox', '47a5f948-78ac-415a-9d99-18661113c2f5'), 
                            ('vs_ucde_correlation_textbox', ''), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id_1)]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_setvaluestore_btn()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_multiple_notification_files(["filteredNotificationObject.txt", "partialFiltered.txt"])
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_second_build_notification_event()
        second_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_build_notification_result_text")
        assert second_build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_second_filter_notification_event()
        second_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_filter_notification_result_text")
        assert second_filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_second_publish_notification_event()
        second_publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_publish_notification_result_text")
        assert second_publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_second_finish_notification_event()
        second_finish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_finish_notification_result_text")
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        tree = json.loads(filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        filter_id = events[0]['filter']['filterId']
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        bindings_cache_response = self.bindings_cache.verify_bindings_cache_response_text()
        self.data_collection_plugin.verify_filter_result(filter_id, bindings_cache_response)

    @pytest.mark.datacollection
    def test_04_send_multiple_notification_when_queue_is_disabled_C32589450(self):
        """
        C32589450: Send multiple notifications -Queue Disabled
        - using data collection refApp, navigate to settings and disable the queue
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button like, sendprebuiltnotification and upload multiple files(filteredNotificationObject,secondfilterednotification)
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files which are filterednotificationobject files
        - verify the listed 2 sets of notifications
        - verify whether the queue tab is empty because we have disabled the queue in settings
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.click_use_queue_policy_toggle()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_multiple_notification_files(["filteredNotificationObject.txt", "second_filteredNotificationObject.txt"])
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_second_build_notification_event()
        second_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_build_notification_result_text")
        assert second_build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_second_filter_notification_event()
        second_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_filter_notification_result_text")
        assert second_filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_second_publish_notification_event()
        second_publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_publish_notification_result_text")
        assert second_publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_second_finish_notification_event()
        second_finish_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_finish_notification_result_text")
        assert second_finish_notification_result['result'] == 'success'
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("queue_nav_btn")
        assert self.settings.verify_queue_item_lists() is False

    @pytest.mark.datacollection
    def test_05_send_ui_event_when_app_instance_id_value_assigned_to_consent_basis_id_C41381063(self):
        """
        C41381063 - Send UI event when AppInstanceId value assigned to ConsentBasisId
        """
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.app_instance_id), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id)]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_setvaluestore_btn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.select_accumulator_delete_btn()
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        metadata = self.bindings_cache.get_metadata_text()
        expected_app_instance_id = 'dacda099-22be-4435-a370-1d333ec66d2c'
        assert 'AppInstanceId' in metadata, "AppInstanceId key not found in metadata"
        assert metadata['AppInstanceId'] == expected_app_instance_id, f"Expected AppInstanceId '{expected_app_instance_id}', but got '{metadata['AppInstanceId']}'"
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'

    @pytest.mark.datacollection
    def test_06_send_sys_info_event_when_app_instance_id_value_assigned_to_consent_basis_id_C41381064(self):
        """
        C41381064 - Send SysInfo event when AppInstanceId value assigned to ConsentBasisId
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.app_instance_id), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id)]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_setvaluestore_btn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        self.data_collection_plugin.select_send_sys_info_event_btn()
        sleep(5)
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Accumulator'
        self.data_collection_plugin.select_pop_up_close_button()
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.select_accumulator_delete_btn()
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        metadata = self.bindings_cache.get_metadata_text()
        expected_app_instance_id = 'dacda099-22be-4435-a370-1d333ec66d2c'
        assert 'AppInstanceId' in metadata, "AppInstanceId key not found in metadata"
        assert metadata['AppInstanceId'] == expected_app_instance_id, f"Expected AppInstanceId '{expected_app_instance_id}', but got '{metadata['AppInstanceId']}'"
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'