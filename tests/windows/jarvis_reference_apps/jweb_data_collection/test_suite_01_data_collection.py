import pytest
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_01_Data_Collection_Services(object):

    @pytest.mark.datacollection
    def test_01_verify_invalidate_cache_C32335624(self):
        """
        C32335624, C29821189: Validate invalidate cache functionality, Invalidates consent data that is locally cached by the Data Collection component
        - Under DataCollection.invalidateCache(), after clicking on Test button, "Cache Invalidated!" text should be verified
        """
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_invalidate_cache_button()
        assert self.data_collection_plugin.get_invalidate_cache_test_result() == 'Cache invalidated!'

    @pytest.mark.datacollection
    def test_02_data_collection_verify_result_invalidate_cache_C32335623(self):
        """
        C32335623, C29794271: Verify result of invalidating the bindings cache on the component reference app
        - navigating to data collection plugin, inform all the needed parameters
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - outside of Weblet, navigating to the binding cache tab to check the binding cache data displays
        - navigate again to Weblet and click on invalidate cache and verify the "Cache invalidated" message
        - return to the cache bindings tab
        - verify the time to expire shows as "Expired" after the cache invalidated
        """
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.binding_cache_metadata_text()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_invalidate_cache_button(direction="up")
        assert self.data_collection_plugin.get_invalidate_cache_test_result() == 'Cache invalidated!'
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.get_bindings_time_to_expire_text() == 'Expired'

    @pytest.mark.datacollection
    def test_03_send_ui_event_with_valid_values_C32335645(self):
        """
        C32335645, C30482040: Send a UI event checking metadata within the Bindings and Request tab
        - Within Data collection Plugin, SendUI event, and verify result should present within the Bindings and Requests tab
        """
        filter_trees_options_bindings_cache = ["AppInstanceId", "AssetType", "AssetUnit", "Country", "DeviceId", "StratusUserId"]
        filter_trees_options_request_url = ["appInstanceId={}".format(self.app_instance_id),
                                            "assetType={}".format(self.asset_type), "country=US", "deviceId={}".format(self.device_id), "stratusUserId={}".format(self.stratus_user_id)]
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_valvecontrollermetadata_toggle()
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'Data Collection'
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        metadata = self.bindings_cache.get_metadata_text()
        self.bindings_cache.verify_metadata_json(metadata, filter_trees_options_bindings_cache)
        self.home.select_top_nav_button("weblet_page_nav_btn")
        assert self.data_collection_plugin.is_send_ui_event_text_button_enabled()
        self.home.select_top_nav_button("requests_nav_btn")
        data_valve_request_url = self.request.get_request_log_url()
        if 'clientdatavalvecontroller' not in data_valve_request_url:
            data_valve_request_url = self.request.get_request_log_url(index=1)
        assert data_valve_request_url, "Failed to find Data Valve Requst URL"
        self.request.verify_data_valve_request_url(data_valve_request_url, filter_trees_options_request_url)

    @pytest.mark.datacollection
    def test_04_send_ui_event_with_empty_custom_metadata_C32335647(self):
        """
        C32335647, C30482042: In JWebDataCollection settings, check textbox using custom empty Metadata values
        - Within Data collection Plugin, SendUI event, and verify result is not present within the Bindings and Requests tab
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.verify_metadata_text() == ''
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.verify_reqeust_log_url() is False
    
    @pytest.mark.datacollection
    def test_05_send_ui_event_when_app_instance_id_value_assigned_to_consent_basis_id_C41381063(self):
        """
        C41381063 - Send UI event when AppInstanceId value assigned to ConsentBasisId
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("value_store_nav_btn")
        textbox_values = [('vs_app_instance_id_textbox', self.app_instance_id), ('vs_consent_basis_id_textbox', self.us_region_app_instance_id)]
        self.value_store.send_texts_to_textboxes(textbox_values)
        self.value_store.click_setvaluestore_btn()
        self.home.select_top_nav_button("weblet_page_nav_btn")
        self.data_collection_plugin.enable_senduieventitem_toggle()
        self.data_collection_plugin.click_send_ui_event_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'Data Collection'
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.select_accumulator_delete_btn()
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        self.home.select_top_nav_button("settings_nav_btn")
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        metadata = self.bindings_cache.get_metadata_text()
        expected_app_instance_id = 'dacda099-22be-4435-a370-1d333ec66d2c'
        assert 'AppInstanceId' in metadata, "AppInstanceId key not found in metadata"
        assert metadata['AppInstanceId'] == expected_app_instance_id, f"Expected AppInstanceId '{expected_app_instance_id}', but got '{metadata['AppInstanceId']}'"
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'