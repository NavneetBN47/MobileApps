import pytest
import json
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_15_Native_V3bindings(object):

    @pytest.mark.datacollection
    def test_01_filter_valid_ledm_tree_v3_bindings_C42664131(self):
        """
        C42664131 - Filter valid LEDM tree v3 bindings
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("LEDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(3)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        ledm_result = self.data_collection_plugin.get_filtered_result()
        assert '/DevMgmt/ProductConfigDyn.xml' in ledm_result
        valid_ledm_tree_details = self.valid_ledm_tree
        self.data_collection_plugin.verify_native_valid_ledm_tree_ui_result(ledm_result, valid_ledm_tree_details)
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        sleep(3)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        response_data = self.bindings_cache.verify_bindings_cache_response_text()
        assert 'bindings' in response_data
        assert 'filters' in response_data['bindings']
        assert 'ledm' in response_data['bindings']['filters']
    
    @pytest.mark.datacollection
    def test_02_filter_valid_cdm_tree_v3_bindings_C42664129(self):
        """
        C42664129 - Filter valid CDM tree v3 bindings
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(3)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        result = self.data_collection_plugin.get_filtered_result()
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        parsed_result = json.loads(result)
        events = parsed_result.get('events')
        assert events == valid_cdm_tree_events
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        sleep(2)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        response_data = self.bindings_cache.verify_bindings_cache_response_text()
        assert 'bindings' in response_data
        assert 'filters' in response_data['bindings']
        assert 'cdm' in response_data['bindings']['filters']

    @pytest.mark.datacollection
    def test_03_filter_multiple_valid_and_invalid_cdm_tree_for_v3_bindings_C42664130(self):
        """
        C42664130 - Filter multiple valid and invalid CDM tree for v3 bindings
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_invalid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(3)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        valid_cdm_result = self.data_collection_plugin.get_filtered_result()
        invalid_cdm_result = self.data_collection_plugin.get_second_filtered_result()
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        parsed_result = json.loads(valid_cdm_result)
        events = parsed_result.get('events')
        assert events == valid_cdm_tree_events
        assert 'InvalidTreeError' in invalid_cdm_result
        assert 'Failed to serialize the tree' in invalid_cdm_result
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        response_data = self.bindings_cache.verify_bindings_cache_response_text()
        assert 'bindings' in response_data
        assert 'filters' in response_data['bindings']
        assert 'cdm' in response_data['bindings']['filters']

    @pytest.mark.datacollection
    def test_04_filter_multiple_valid_and_invalid_ledm_tree_for_v3_bindings_C42664132(self):
        """
        C42664132 - Filter multiple valid and invalid LEDM tree for v3 bindings
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("LEDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_combo_tree_list("LEDM")
        self.data_collection_plugin.select_invalid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(3)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        ledm_result = self.data_collection_plugin.get_filtered_result()
        assert '/DevMgmt/ProductConfigDyn.xml' in ledm_result
        valid_ledm_tree_details = self.valid_ledm_tree
        self.data_collection_plugin.verify_native_valid_ledm_tree_ui_result(ledm_result, valid_ledm_tree_details)
        invalid_ledm_result = self.data_collection_plugin.get_second_filtered_result()
        assert 'InvalidTreeError' in invalid_ledm_result
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        response_data = self.bindings_cache.verify_bindings_cache_response_text()
        assert 'bindings' in response_data
        assert 'filters' in response_data['bindings']
        assert 'ledm' in response_data['bindings']['filters']

    @pytest.mark.datacollection
    def test_05_filter_valid_ledm_tree_for_a_resource_id_C42664133(self):
        """
        C42664133 - Filter valid LEDM tree for a resource id 
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("http_proxy_nav_btn")
        self.data_collection_plugin.clear_text_from_textboxes(['http_proxy_href_textbox'])
        resource_uri_value = [('http_proxy_href_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(resource_uri_value)
        file_path = self.ledm_xml_file
        textbox_id = "http_proxy_tree_textbox"
        self.data_collection_plugin.enter_tree_http_proxy_tree_textbox(file_path, textbox_id)
        self.data_collection_plugin.select_http_proxy_filter_tree_btn()
        sleep(5)
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        response_data = self.bindings_cache.verify_bindings_cache_response_text()
        assert 'bindings' in response_data
        assert 'filters' in response_data['bindings']
        assert 'ledm' in response_data['bindings']['filters']