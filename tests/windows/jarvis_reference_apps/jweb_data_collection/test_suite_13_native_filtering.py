import pytest
import json
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_13_Native_Filtering(object):

    @pytest.mark.datacollection
    def test_01_filter_valid_cdm_tree_C32335625(self):
        """
        C32335625 - Filter valid CDM tree
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        result = self.data_collection_plugin.get_filtered_result()
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        parsed_result = json.loads(result)
        sleep(5)
        events = parsed_result.get('events')
        sleep(5)
        assert events == valid_cdm_tree_events
    
    @pytest.mark.datacollection
    def test_02_filter_valid_cdm_tree_when_asset_unit_desktop_required_parameter_is_missing_C32335628(self):
        """
        C32335628 - Filter valid CDM tree when required parameter is missing
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        result = self.data_collection_plugin.get_filtered_result()
        assert 'ValveControllerMetadataError' in result
        assert 'The Asset Unit of Type desktop Needs an App Instance Id Value' in result

    @pytest.mark.datacollection
    def test_03_make_a_request_when_cache_is_empty_C29779395(self):
        """
        C29779395: Validate to make a request when cache is empty
        """
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.verify_metadata_text() == ''
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.disable_use_batching_policy_toggle(False)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.verify_bindings_cache_response_displays() is True

    @pytest.mark.datacollection
    def test_04_verify_queueing_an_event_C30025572(self):
        """
        C30025572: Validate queueing an event
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.disable_use_batching_policy_toggle(False)
        self.settings.enable_use_custom_batching_policy_toggle(False)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        textbox_count_value = [('count_value_textbox', '15')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Accumulator'
        self.data_collection_plugin.select_pop_up_close_button()
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.verify_accumulator_list() is True
        self.data_collection_plugin.select_accumulator_delete_btn()
        sleep(2)
        self.home.select_top_nav_button("queue_nav_btn")
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.verify_accumulator_list() is False
    
    @pytest.mark.datacollection
    def test_05_verify_queueing_an_even_with_queue_flag_not_activated_C30025573(self):
        """
        C30025573: Validate queueing an event with queue flag not activated
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.settings.disable_use_batching_policy_toggle(False)
        self.settings.enable_use_custom_batching_policy_toggle(False)
        self.settings.click_use_queue_policy_toggle()
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Accumulator'
        self.data_collection_plugin.select_pop_up_close_button()
        self.home.select_top_nav_button("queue_nav_btn")
        assert self.settings.verify_queue_item_lists() is False