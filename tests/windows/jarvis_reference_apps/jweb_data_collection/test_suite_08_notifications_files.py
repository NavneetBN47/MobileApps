import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_08_Notifications_Files(object):

    @pytest.mark.datacollection
    def test_01_send_notification_by_uploading_partially_filtered_notification_file_C32589402(self):
        """
        C32589402, C32603173: Send notifications by only enabling notification for already filtered Notification
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the partially filterednotification file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the filterid in the "valveFilterResult" by comparing it from uploaded partially filtered file
          and bindings cache response
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', 'dacda099-22be-4435-a370-1d333ec66d2c'),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        tree = json.loads(filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        partially_filter_id = events[0]['filter']['filterId']
        bindings_response_filter_id = events[1]['filter']['filterId']
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'
        partially_filtered_tree = self.partially_filtered
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        bindings_cache_response = self.bindings_cache.verify_bindings_cache_response_text()
        self.data_collection_plugin.verify_filter_result_of_partially_filtered_file(partially_filter_id, partially_filtered_tree, bindings_response_filter_id, bindings_cache_response)
   
    @pytest.mark.datacollection
    def test_02_send_notification_by_uploading_empty_cdm_objects_C32589452(self):
        """
        C32589452: Send notification by only enabling notification when CDM object as empty
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the empty cdm object file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - Navigate to Verbose logs tab, verify the Invalid CDM Event error response "Events and notifications are empty"
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('empty.rtf')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.home.select_top_nav_button("verbose_logs_nav_btn")
        result = self.verbose_logs.get_verbose_logs_response_error(get_json=False).split('\n')
        assert result[1] == 'Events and notifications are empty'

    @pytest.mark.datacollection
    def test_03_send_notification_when_custom_metadata_with_invalid_appinstanceid_on_settings_tab_C32589565(self):
        """
        C32589565: Send a notification when custom metadata has "Invalid" appinstanceid on settings
        - using data collection refApp, navigate to data collection plugin
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enter the appinstanceId as invalid
        - enable verbose logs toggle and click on save button
        - navigate to weblet page, enter the valvecontroller metadata values and appinstanceId as invalid
        - enable the toggle button sendprebuiltnotification and upload the partialfiltered file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In finish notification event, verify the "message": "Local Schema Validation Failed. Does your app instance id:" contains
        - In finish notification event, verify the result = failure
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.settings.send_text_to_textbox('app_instance_id_textbox','invalid')
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', 'invalid'), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        actual_schema_message = finish_notification_result['message']
        expected_schema_message = "Local Schema Validation Failed. Does your app instance id:"
        self.data_collection_plugin.verify_finish_result_schema_validation_error(expected_schema_message, actual_schema_message)
        assert finish_notification_result['result'] == 'failure'

    @pytest.mark.datacollection
    def test_04_send_notification_by_uploading_invalid_cdm_objects_C32589559(self):
        """
        C32589559: Send notification by only enabling notification with invalid cdm object
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the invalid cdm object file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - Navigate to Verbose logs tab, verify the Invalid CDM Event error response "Events and notifications are empty"
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('invalid.rtf')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.home.select_top_nav_button("verbose_logs_nav_btn")
        result = self.verbose_logs.get_verbose_logs_response_error(get_json=False).split('\n')
        assert result[1] == 'Events and notifications are empty'

    @pytest.mark.datacollection
    def test_05_send_ui_event_when_value_store_values_set_to_null_C32589406(self):
        """
        C32589406: Send an UI event when valuestore values are set as null
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose toggle and click on save
        - using data collection refApp, click on more button and navigate to value Store
        - clear all the given native content of the textboxes
        - click on set value store button
        - navigate to weblet, enable sendsimpleuievent toggle and tracking identifier toggle
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "reason": "The Asset Unit of Type desktop Needs an App Instance Id Value"
        - In finish notification event, verify the result = failure
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox', 'account_login_id_textbox', 
                                                'stratus_user_id_textbox', 'device_id_textbox', 'model_number_textbox', 'tenant_id_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("value_store_nav_btn")
        self.value_store.clear_text_from_textboxes(['vs_app_instance_id_textbox', 'vs_stratus_user_id_textbox', 'vs_account_login_id_textbox', 'vs_device_id_textbox',
                               'vs_model_number_textbox', 'vs_tenant_id_textbox', 'vs_system_serial_number_textbox', 'vs_pc_device_uuid_textbox',
                               'vs_ucde_correlation_textbox', 'vs_consent_basis_id_textbox'])
        self.value_store.click_setvaluestore_btn()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == False
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult']['reason'] == 'The Asset Unit of Type desktop Needs an App Instance Id Value'
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'failure'