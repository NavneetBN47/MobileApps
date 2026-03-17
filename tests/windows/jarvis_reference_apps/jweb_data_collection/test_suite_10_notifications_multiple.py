import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_10_Notifications_Multiple(object):

    @pytest.mark.datacollection
    def test_01_send_notification_by_uploading_multiple_already_filtered_notification_objects_C32589494(self):
        """
        C32589494: Send notifications by only enabling notification by uploading multiple already filtered Notification
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload multiple filterednotification files
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
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

    @pytest.mark.datacollection
    def test_02_send_notification_by_uploading_both_partially_and_filtered_notification_objects_C32589544(self):
        """
        C32589544: Send notifications by only enabling notification for both partially filtered and already filtered Notification objects
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload both partially filtered and filterednotification objects
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_multiple_notification_files(["filteredNotificationObject.txt", "partialFiltered.txt"])
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
    def test_03_send_notification_by_uploading_both_partially_and_filtered_notification_objects_C32589511(self):
        """
        C32589511: Send notifications by only enabling notification for 2 partially filtered Notification objects
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle button sendprebuiltnotification and upload 2 partially filtered notification objects
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification from bottom of the list
        - We will be getting each notification count as 2 , as we have uploaded 2 files
        - verify the listed 2 sets of notifications
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_send_prebuiltnotification_toggle()
        self.fc.upload_multiple_notification_files(["partialFiltered.txt", "second_partialFiltered.txt"])
        self.data_collection_plugin.click_send_ui_event_test_button()
        self.data_collection_plugin.expand_second_build_notification_event()
        second_build_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_build_notification_result_text")
        assert second_build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_build_notification_event()
        build_notification_result = self.data_collection_plugin.verify_tracking_event_results("build_notification_result_text")
        assert build_notification_result['prebuild'] == True
        self.data_collection_plugin.expand_second_filter_notification_event()
        second_filter_notification_result = self.data_collection_plugin.verify_tracking_event_results("second_filter_notification_result_text")
        tree = json.loads(second_filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        second_partially_filter_id = events[0]['filter']['filterId']
        second_bindings_response_filter_id = events[1]['filter']['filterId']
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
        self.data_collection_plugin.verify_second_filter_result_of_multiple_partially_filtered_file(second_partially_filter_id, partially_filtered_tree, second_bindings_response_filter_id, bindings_cache_response)

    @pytest.mark.datacollection
    def test_04_verify_response_if_both_enable_ui_event_and_enable_notification_are_disabled_C32589561(self):
        """
        C32589561: verify the response if both enable ui event and enable notification are disabled
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the valvecontrollermetadata and tracking identifier toggle buttons
        - click on the send ui test button
        - verify the response error from verbose log screen
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'Data Collection'
        self.home.select_top_nav_button("verbose_logs_nav_btn")
        result = self.verbose_logs.get_verbose_logs_response_error(get_json=False).split('\n')
        assert result[1] == "EventData was missing 'events' and 'notifications' array"

    @pytest.mark.datacollection
    def test_05_send_ui_event_and_notification_with_mockup_notification_enabled_C32613218(self):
        """
        C32613218: Send an ui event and notification with mockup notification enabled
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable sendsimpleuievent toggle
        - enable the toggle button sendprebuiltnotification and enable mockup notification toggle
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
        self.data_collection_plugin.enable_mock_notification_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
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
        filter_id  = events[0]['filter']['filterId']
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