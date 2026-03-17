import pytest
from time import sleep
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_09_Notifications_ValueStore(object):

    @pytest.mark.datacollection
    def test_01_send_notification_when_value_store_values_set_to_null_C32589407(self):
        """
        C32589407: Send a notification when valuestore values are set as null
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle and click on save button
        - using data collection refApp, click on more button and navigate to value Store
        - clear all the given native content of the textboxes
        - click on set value store button
        - navigate to weblet, enable sendPrebuiltNotification and upload the partialFiltered file
        - enable tracking identifier toggle
        - click on the send ui test button
        - verify the published notifications appeared under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
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

    @pytest.mark.datacollection
    def test_02_send_ui_event_when_invalid_data_sent_in_event_details_C32589408(self):
        """
        C32589408: Send an UI event when invalid data sent in event details
        - using data collection refApp, navigate to data collection plugin
        - fill up all the required parameters in valvecontroller metadata component
        - enable the toggle buttons like, SendSimpleUiEvent, valvecontrollermetadata and tracking identifier
        - enter "invalid" value in screen name field (required field)
        - click on the send ui test button twice
        - navigate to request tab, verify the status code should be 206 or first attempt
        - navigate to request tab, verify the status code should be 400 or second attempt
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_include_trackingidentifier_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
        textbox_invalid_value = [('screen_name_textbox', 'invalid')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_invalid_value)
        self.data_collection_plugin.click_send_ui_event_test_button()
        sleep(3)
        self.data_collection_plugin.click_send_ui_event_test_button()
        sleep(5)
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        assert self.request.get_first_attempt_data_valve_controller_status_code() == '206'
    
    @pytest.mark.datacollection
    def test_03_send_ui_event_when_value_store_values_are_set_C32589555(self):
        """
        C32589555: Send an ui event when value store values are set
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle and click on save button
        - using data collection refApp, click on more button and navigate to value Store
        - fill up the parameters and click on set value store
        - using data collection refApp, navigate to data collection plugin
        - enable sendsimpleuievent and include trackingidentifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "valveFilterResult" with the filterId by comparing it from bindings cache
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        - Extract the filter_id from filter notification text and verify the same filter id exists in binding cache response
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.us_region_app_instance_id), ('vs_stratus_user_id_textbox', self.stratus_user_id), ('vs_account_login_id_textbox', self.account_login_id),
                            ('vs_device_id_textbox', self.us_region_device_id), ('vs_model_number_textbox', '53N95A'), ('vs_tenant_id_textbox', self.tenant_id),
                            ('vs_system_serial_number_textbox', '5CH2346D20'), ('vs_pc_device_uuid_textbox', '47a5f948-78ac-415a-9d99-18661113c2f5'), 
                            ('vs_ucde_correlation_textbox', ''), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id_1)]
        self.value_store.send_texts_to_textboxes(textbox_values)
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
        tree = json.loads(filter_notification_result['valveFilterResult']['tree'])
        events = tree['events']
        event_tree = events[0]
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
    def test_04_send_notification_when_value_store_values_are_set_C32589556(self):
        """
        C32589556: Send a notification when value store values are set
        - navigate to settings tab, enable  the custom metadata value checkbox and clear the necessary parameter fields
        - enable the verbose logs toggle and click on save button
        - using data collection refApp, click on more button and navigate to value Store
        - fill up the parameters and click on set value store
        - using data collection refApp, navigate to data collection plugin
        - enable sendprebuiltnotification and upload the partialFiltered text file
        - enable include trackingidentifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "True"
        - In filter notification event, verify the "valveFilterResult" with the filterId by comparing it from bindings cache
        - In publish notification event, verify the status code = 200
        - In finish notification event, verify the result = success
        - Extract the filter_id from filter notification text and verify the same filter id exists in binding cache response
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.us_region_app_instance_id), ('vs_stratus_user_id_textbox', self.stratus_user_id), ('vs_account_login_id_textbox', self.account_login_id),
                            ('vs_device_id_textbox', self.us_region_device_id), ('vs_model_number_textbox', '53N95A'), ('vs_tenant_id_textbox', self.tenant_id),
                            ('vs_system_serial_number_textbox', '5CH2346D20'), ('vs_pc_device_uuid_textbox', '47a5f948-78ac-415a-9d99-18661113c2f5'), 
                            ('vs_ucde_correlation_textbox', ''), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id_1)]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_setvaluestore_btn()
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
    def test_05_send_ui_event_when_required_values_are_missing_in_value_Store_C32589562s(self):
        """
        C32589562: Send an ui event when required values are missing in value store
        - navigate to settings tab, enable the custom metadata value checkbox and clear the necessary parameter fields
        - enable verbose logs toggle button and click on save button
        - using data collection refApp, click on more button and navigate to value Store
        - fill up the key names in remove key text box "appinstanceid", "ConsentBasisId" and "SystemSerialNumber" to remove
        - click on remove valuestore button
        - fill up the parameters and leave "appinstanceid", "ConsentBasisId and "SystemSerialNumber" fields as blank 
        - click on set value store
        - using data collection refApp, navigate to data collection plugin
        - enable sendsimpleuievent and include trackingidentifier toggle buttons
        - click on the send ui test button
        - verify the published notifications under tracking events by expanding one by one notification
        - In build notification event, verify the Pre-build status as "False"
        - In filter notification event, verify the "reason": "The Asset Unit of Type desktop Needs an App Instance Id Value"
        - In finish notification event, verify the result = failure
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.enable_use_custom_metadata_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.settings.enable_verbose_logs_toggle(True)
        self.home.select_top_nav_button("more_nav_btn", raise_e=False)
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_remove_keys_textbox', 'ConsentBasisId,SystemSerialNumber,ApplicationInstanceId')]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_removevaluestore_btn()
        textbox_values = [('vs_app_instance_id_textbox', ''), ('vs_stratus_user_id_textbox', self.stratus_user_id), ('vs_account_login_id_textbox', self.account_login_id),
                            ('vs_device_id_textbox', self.device_id), ('vs_model_number_textbox', 'K7G93A'), ('vs_tenant_id_textbox', self.tenant_id),
                            ('vs_system_serial_number_textbox', ''), ('vs_pc_device_uuid_textbox', '47a5f948-78ac-415a-9d99-18661113c2f5'), 
                            ('vs_ucde_correlation_textbox', ''), ('vs_consent_basis_id_textbox', '')]
        self.value_store.send_texts_to_textboxes(textbox_values)
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