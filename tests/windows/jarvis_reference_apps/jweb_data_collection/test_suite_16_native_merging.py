import pytest
import json
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_16_Native_Merging(object):

    @pytest.mark.datacollection
    def test_01_verify_merging_by_send_ui_event_same_custom_metadata_two_times_seperately_C40387610(self):
        """
        C40387610 - Verify merging by sending UI event with same custom metadata two times separately
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_2), ('device_id_textbox', self.us_region_device_id), 
                          ('model_number_textbox', self.model_number), ('batching_max_event_notification_textbox', self.batching_max_event_notification), ('batching_min_event_notification_textbox', self.batching_min_event_notification),
                          ('batching_max_event_age_textbox', self.batching_max_event_age), ('batching_evaluation_frequency_textbox', self.batching_evaluation_frequency)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        textbox_count_value = [('count_text_box', '3')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        textbox_count_value = [('count_text_box', '1')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(2)
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.verify_accumulator_list() is True
        self.data_collection_plugin.select_accumulator_delete_btn()
        sleep(2)
        self.home.select_top_nav_button("requests_nav_btn")
        request_url = self.request.get_request_log_url()
        if 'clientdatavalvecontroller' not in request_url:
            data_valve_request_url = self.request.get_request_log_url(index=1)
            assert data_valve_request_url, "Failed to find Data Valve Requst URL"
        if 'clienttelemetry' not in request_url:
            telemetry_request_url = self.request.get_request_log_url(index=0)
            assert telemetry_request_url, "Failed to find Client Telemetry Requst URL"

    @pytest.mark.datacollection
    def test_02_verify_merging_by_send_ui_event_different_custom_metadata_two_times_seperately_C40387611(self):
        """
        C40387611 - Verify merging by sending UI event with different custom metadata two times separately
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), 
                          ('model_number_textbox', self.model_number), ('batching_max_event_notification_textbox', self.batching_max_event_notification), ('batching_min_event_notification_textbox', '5'),
                          ('batching_max_event_age_textbox', '300'), ('batching_evaluation_frequency_textbox', self.batching_evaluation_frequency)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        textbox_count_value = [('count_text_box', '1')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        self.home.select_top_nav_button("settings_nav_btn")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_2), ('device_id_textbox', self.us_region_device_id), 
                          ('model_number_textbox', self.model_number), ('batching_max_event_notification_textbox', self.batching_max_event_notification), ('batching_min_event_notification_textbox', '5'),
                          ('batching_max_event_age_textbox', '300'), ('batching_evaluation_frequency_textbox', self.batching_evaluation_frequency)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        textbox_count_value = [('count_text_box', '3')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(2)
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.verify_accumulator_list() is True
        self.data_collection_plugin.select_accumulator_delete_btn()
        self.home.select_top_nav_button("queue_nav_btn")
        queue_items_list = self.data_collection_plugin.verify_queue_items_list()
        assert queue_items_list == 2, "Queue items count does not match"
        sleep(3)
        self.home.select_top_nav_button("requests_nav_btn")
        request_url = self.request.get_request_log_url()
        if 'clientdatavalvecontroller' not in request_url:
            data_valve_request_url_first = self.request.get_request_log_url(index=0)
            assert data_valve_request_url_first, "Failed to find Data Valve Requst URL"
            data_valve_request_url_second = self.request.get_request_log_url(index=1)
            assert data_valve_request_url_second, "Failed to find Data Valve Requst URL"
        if 'clienttelemetry' not in request_url:
            telemetry_request_url_first = self.request.get_request_log_url(index=2)
            assert telemetry_request_url_first, "Failed to find Client Telemetry Requst URL"
            telemetry_request_url_second = self.request.get_request_log_url(index=3)
            assert telemetry_request_url_second, "Failed to find Client Telemetry Requst URL"

    @pytest.mark.datacollection
    def test_03_filter_multiple_valid_cdm_tree_C32335632(self):
        """
        C32335632 - Filter multiple valid CDM tree
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', '53N95A')]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(5)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        valid_cdm_result_1 = self.data_collection_plugin.get_filtered_result()
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        parsed_result = json.loads(valid_cdm_result_1)
        events = parsed_result.get('events')
        assert events == valid_cdm_tree_events
        self.data_collection_plugin.select_tree_remove_btn()
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        sleep(5)
        self.data_collection_plugin.select_filtered_pop_up_close_btn()
        valid_cdm_result_2 = self.data_collection_plugin.get_filtered_result()
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        parsed_result = json.loads(valid_cdm_result_2)
        events = parsed_result.get('events')
        assert events == valid_cdm_tree_events

    @pytest.mark.datacollection
    def test_04_send_ui_event_when_invalid_data_sent_in_event_detail_C32589408(self):
        """
        C32589408 - Send ui event when invalid data sent in event detail
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(False)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        textbox_invalid_value = [('screen_name_value_textbox', 'jdhs')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_invalid_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(4)
        self.home.select_top_nav_button("requests_nav_btn")
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("requests_nav_btn")
        self.request.verify_request_url_table()

    @pytest.mark.datacollection
    def test_05_send_a_batch_of_250_ui_events_at_once_C40387603(self):
        """
        C40387603 - Send a batch of 250 UI events at once
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_2), ('device_id_textbox', self.us_region_device_id), 
                          ('model_number_textbox', self.model_number), ('batching_max_event_notification_textbox', '250'), ('batching_min_event_notification_textbox', '250'),
                          ('batching_max_event_age_textbox', '3600'), ('batching_evaluation_frequency_textbox', self.batching_evaluation_frequency)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.fc.handle_toggle()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_enable_ui_event_checkbox(True)
        self.data_collection_plugin.select_enable_notification_checkbox(False)
        textbox_count_value = [('count_text_box', '250')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_count_value)
        self.data_collection_plugin.select_send_ui_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent.'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("accumulator_nav_btn")
        self.data_collection_plugin.verify_accumulator_list() is True
        self.data_collection_plugin.select_accumulator_delete_btn()
        sleep(5)
        self.home.select_top_nav_button("requests_nav_btn")
        request_url = self.request.get_request_log_url()
        if 'clientdatavalvecontroller' not in request_url:
            data_valve_request_url_first = self.request.get_request_log_url(index=0)
            assert data_valve_request_url_first, "Failed to find Data Valve Requst URL"
            data_valve_request_url_second = self.request.get_request_log_url(index=1)
            assert data_valve_request_url_second, "Failed to find Data Valve Requst URL"
        if 'clienttelemetry' not in request_url:
            telemetry_request_url_first = self.request.get_request_log_url(index=2)
            assert telemetry_request_url_first, "Failed to find Client Telemetry Requst URL"
            telemetry_request_url_second = self.request.get_request_log_url(index=3)
            assert telemetry_request_url_second, "Failed to find Client Telemetry Requst URL"