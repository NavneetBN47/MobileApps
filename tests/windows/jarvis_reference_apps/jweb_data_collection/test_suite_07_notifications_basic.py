import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_07_Notifications_Basic(object):

    @pytest.mark.datacollection
    def test_01_send_an_ui_event_without_enabling_send_prebuilt_notification_C32589336(self):
        """
        C32589336: send an ui event without enabling sendprebuiltnotification from weblet
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle buttons like, SendSimpleUiEvent, valvecontrollermetadata and tracking identifier
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "valveFilterResult" with the filterId by comparing it from bindings cache
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        - Extract the filter_id from filter notification text and verify the same filter id exists in binding cache response
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == False
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        tree = json.loads(filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        event_tree = events[1]
        filter_id = event_tree['filter']['filterId']
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
    def test_02_send_notification_with_mock_up_notification_enabled_C32613217(self):
        """
        C32613217, C38257143: send a notification, by enabling mock-up notification from weblet
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle buttons like sendprebuiltnotification, valvecontrollermetadata and tracking identifier
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "valveFilterResult": "Skipped due to preexisting filter"
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.data_collection_plugin.enable_mock_notification_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'

    @pytest.mark.datacollection
    def test_03_send_notification_when_custom_metadata_required_field_is_empty_C32589454(self):
        """
        C32589454, C30482042: send a notification when custom metadata required field is empty and verify the response error
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle and click on save button
        - using data collection refApp, navigate to data collection plugin
        - fill up the required parameters in valvecontroller metadata component and leave the assetType as empty
        - enable the toggle buttons like sendprebuiltnotification, valvecontrollermetadata and tracking identifier
        - click on the send ui test button
        - verify the published build notifications appeared under tracking events by expanding it
        - In build notification event, verify the Pre-build status as "True"
        - navigate to verbose logs tab and verify the response error
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.data_collection_plugin.enable_mock_notification_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.home.select_top_nav_button("verbose_logs_nav_btn")
        result = self.verbose_logs.get_verbose_logs_response_error(get_json=False).split('\n')
        response = json.loads(result[3])
        assert response['result'] == 'failure'

    @pytest.mark.datacollection
    def test_04_send_notification_by_uploading_already_filtered_notification_file_C32589401(self):
        """
        C32589401: Send notifications by only enabling notification for already filtered Notification
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload the filterednotification file
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "valveFilterResult": "Skipped due to preexisting filter"
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('filteredNotificationObject.txt')
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult'] == 'Skipped due to preexisting filter'
        self.data_collection_plugin.expand_publish_notification_event()
        publish_notification_result = self.data_collection_plugin.verify_tracking_event_results("publish_notification_result_text")
        assert publish_notification_result['telemetryServiceResponse']['responseCode'] == 200
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'success'

    @pytest.mark.datacollection
    def test_05_send_notification_when_custom_metadata_with_blank_appinstanceid_on_settings_tab_C32589409(self):
        """
        C32589409, C32603177: Send notifications when custom metadata has <blank> appinstanceId in settings tab
        - using data collection refApp, navigate to data collection plugin
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle and click on save button
        - navigate to weblet, enable the toggle button like sendprebuiltnotification and upload the partialfiltered file
        - enable the tracking identifier toggle
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "reason": "The Asset Unit of Type desktop Needs an App Instance Id Value"
        - In finish notification event, verify the result = failure
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_single_notification_file('partialFiltered.txt')
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_filter_notification_event()
        filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("filter_notification_result_text")
        assert filter_notification_result['valveFilterResult']['reason'] == 'The Asset Unit of Type desktop Needs an App Instance Id Value'
        self.data_collection_plugin.expand_finish_notification_event()
        finish_notification_result = self.data_collection_plugin.get_finish_notification_event_result_text(get_json=True)
        assert finish_notification_result['result'] == 'failure'