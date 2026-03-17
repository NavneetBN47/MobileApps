import pytest
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_12_Native_Basic(object):

    @pytest.mark.datacollection
    def test_01_send_a_batch_of_250_and_1_sys_info_event_during_fresh_install_of_app_C40387607(self):
        """
        C40387607 - Send a batch of 250 and 1 sys info event during fresh install of app
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
        textbox_count_value = [('count_text_box', '251')]
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

    @pytest.mark.datacollection
    def test_02_send_system_info_event_when_invalid_data_sent_in_event_detail_C32275905(self):
        """
        C32275905 - Send system info event when invalid data sent in event detail
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
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(3)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.verify_bindings_cache_response_displays() is True
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        self.home.select_top_nav_button("requests_nav_btn")
        assert self.request.get_second_attempt_data_valve_controller_status_code() == '200'
        assert self.request.get_first_attempt_data_valve_controller_status_code() == '200'

    @pytest.mark.datacollection
    def test_03_verify_invalidate_cache_C29795232(self):
        """
        C29795232:  Validate invalidate cache functionality, Invalidates consent data that is locally cached by the Data Collection component
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
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        self.bindings_cache.select_bindings_invalidate_cache_btn()
        assert self.bindings_cache.get_bindings_time_to_expire_text() == 'Expired'

    @pytest.mark.datacollection
    def test_04_verify_to_make_a_request_when_cache_is_expired_C29779397(self):
        """
        C29779397: Validate to make a request when cache is expired
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
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        self.bindings_cache.select_bindings_invalidate_cache_btn()
        assert self.bindings_cache.get_bindings_time_to_expire_text() == 'Expired'
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        assert self.bindings_cache.get_bindings_time_to_expire_text() != 'Expired'

    @pytest.mark.datacollection
    def test_05_verify_to_make_a_request_when_cache_has_cached_bindings_C30794744(self):
        """
        C30794744: Validate to make a request when cache has cached bindings
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
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        initial_time_to_expire = self.bindings_cache.get_bindings_time_to_expire_text()
        self.home.select_top_nav_button("data_collection_service_nav_btn")
        self.data_collection_plugin.select_send_sys_info_event_btn()
        assert self.data_collection_plugin.get_event_send_pop_up_result() == 'Event sent to the Queue'
        self.data_collection_plugin.select_pop_up_close_button()
        sleep(5)
        self.home.select_top_nav_button("bindings_cache_nav_btn")
        current_time_to_expire = self.bindings_cache.get_bindings_time_to_expire_text()
        assert current_time_to_expire < initial_time_to_expire, f"Current time to expire ({current_time_to_expire}) is not less than initial time to expire ({initial_time_to_expire})"