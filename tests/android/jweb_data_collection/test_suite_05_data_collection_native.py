import pytest
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
import json

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_05_Data_Collection_Native(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_data_collection_setup):
        cls = cls.__class__
        cls.stack = request.config.getoption("--stack")
        cls.driver, cls.fc = android_jweb_data_collection_setup
        cls.home = cls.fc.fd["home"]
        cls.data_valve = cls.fc.fd["data_valve"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_service = cls.fc.fd["data_collection_service"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]
        cls.local_files = cls.fc.fd["local_files"]

        cls.data_collection_test_data = cls.fc.get_data_collection_test_data(cls.stack)
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.app_instance_id_send_ui = cls.data_collection_test_data["app_instance_id_send_ui"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]

        cls.expected_batching_content = { "enabled": True, "minEventsPerNotification": 10, "maxEventsPerNotification": 250,
                                      "eventAgeInSeconds": 300, "evaluationFrequencyInSeconds": 60}

        with open(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json")) as cdm_tree:
            cls.valid_cdm_tree = json.loads(cdm_tree.read())

    @pytest.fixture(scope="function", autouse="true")
    def data_collection_home_setup(self):
        self.fc.flow_load_home_screen()
        self.fc.select_stack(self.stack)

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send files to Android Device, and delete file once tests are complete
        """
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "validcdmtree.json"), overwrite=True)
        yield None
        self.driver.clean_up_device_folder(TEST_DATA.MOBILE_DOWNLOAD)

    def test_01_verify_invalidate_cache(self):
        """
        C32335624: Verify invalidate cache on the native component reference app
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_send_sys_info_event_button()
        self.home.select_cached_bindings_tab()
        self.data_collection_service.select_bindings_delete_button()
        self.data_valve.get_v1bindings_text() is False   

    def test_02_verify_result_invalidate_bindings_cache(self):
        """
        C32335623: Verify result of invalidate the bindings cache on the native component reference app
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        assert self.data_collection_service.get_filterd_cdm_text() == 'Filtered'
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True

    def test_03_filter_valid_cdm_tree(self):
        """
        C32335625: Filter valid CDM tree
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        parsed_result = json.loads(result)
        events = parsed_result.get('events')
        assert events == self.valid_cdm_tree['events']

    def test_04_filter_invalid_cdm_tree(self):
        """
        C32335626: Filter invalid CDM tree
        """
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_invalid_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'InvalidTreeError' in result, "failed to get InvalidTreeError from result, result: {}".format(result)
   
    def test_05_filter_cdm_tree_when_required_parameter_missing_for_desktop(self):
        """
        C32335628: Filter a valid CDM tree when a required parameter is missing for Desktop asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("desktop")
        self.data_collection_settings.select_settings_save_button() 
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'ValveControllerMetadataError' in result, "failed to get ValveControllerMetadataError from result, result: {}".format(result)
        assert 'appInstanceId is required when assetUnit is mobile or desktop' in result, "failed to get appInstanceId is required when assetUnit is mobile or desktop from result, result: {}".format(result)

    def test_06_filter_cdm_tree_when_required_parameter_missing_for_mobile(self):
        """
        C32335629: Filter a valid CDM tree when a required parameter is missing for mobile asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        self.data_collection_settings.select_settings_save_button()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'ValveControllerMetadataError' in result, "failed to get ValveControllerMetadataError from result, result: {}".format(result)
        assert 'appInstanceId is required when assetUnit is mobile or desktop' in result, "failed to get appInstanceId is required when assetUnit is mobile or desktop from result, result: {}".format(result)    

    def test_07_1_filter_cdm_tree_when_required_parameter_missing_for_solution(self):
        """
        C32335630: Filter a valid CDM tree when a required parameter is missing for solution asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("solution")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1), 
                          ('settings_stratus_user_id', self.stratus_user_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        parsed_result = json.loads(result)
        events = parsed_result.get('events')
        assert events == self.valid_cdm_tree['events']  

    def test_07_2_filter_cdm_tree_when_required_parameter_missing_for_solution(self):
        """
        C32335630: Filter a valid CDM tree when a required parameter is missing for solution asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("solution")
        textbox_values = [('settings_asset_type', ''), ('settings_stratus_user_id', self.stratus_user_id)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'ValveControllerMetadataError' in result, "failed to get ValveControllerMetadataError from result, result: {}".format(result)

    def test_07_3_filter_cdm_tree_when_required_parameter_missing_for_solution(self):
        """
        C32335630: Filter a valid CDM tree when a required parameter is missing for solution asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("solution")
        textbox_values = [('settings_asset_type', 'instantInk'), ('settings_stratus_user_id', '')]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'ValveControllerMetadataError' in result, "failed to get ValveControllerMetadataError from result, result: {}".format(result)

    def test_07_4_filter_cdm_tree_when_required_parameter_missing_for_solution(self):
        """
        C32335630: Filter a valid CDM tree when a required parameter is missing for solution asset unit
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("solution")
        textbox_values = [('settings_device_id', self.us_region_device_id),('settings_stratus_user_id', '')]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(2)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        assert 'ValveControllerMetadataError' in result, "failed to get ValveControllerMetadataError from result, result: {}".format(result)
    
    def test_08_filter_valid_cdm_tree_after_enabling_v3_endpoint(self):
        """
        C42664129: Filter valid CDM tree after enabling V3 endpoint
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_batching_switch(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        assert self.data_collection_service.get_filterd_cdm_text() == 'Filtered'
        self.home.select_cached_bindings_tab()
        bindings_result = self.data_collection_service.get_telemetry_text()
        parsed_result = json.loads(bindings_result)
        result = parsed_result['telemetryClientConfiguration']
        assert 'batching' in result, "Batching key not found in result"
        assert result['batching'] == self.expected_batching_content, "Batching content does not match"
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        result = self.data_collection_service.get_data_valve_controller_status_code()
        assert 'code=200' in result, "failed to get code=200 from result, result: {}".format(result) 

    def test_09_filter_multiple_valid_and_invalid_cdm_trees_at_once_after_enabling_v3_endpoint(self):
        """
        C42664130: Filter multiple valid and invalid CDM trees at once after enabling V3 endpoint
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_add_invalid_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        assert self.data_collection_service.get_filterd_cdm_text() == 'Filtered'
        self.home.select_cached_bindings_tab()
        bindings_result = self.data_collection_service.get_telemetry_text()
        parsed_result = json.loads(bindings_result)
        result = parsed_result['telemetryClientConfiguration']
        assert 'batching' in result, "Batching key not found in result"
        assert result['batching'] == self.expected_batching_content, "Batching content does not match"
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        result = self.data_collection_service.get_data_valve_controller_status_code()
        assert 'code=200' in result, "failed to get code=200 from result, result: {}".format(result)     

    def test_10_filter_CDM_tree_with_invalid_GUN(self):
        """
        C32335627: Filter CDM tree with invalid GUN
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.set_tree_gun_box_value("invalid")
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        self.data_collection_service.select_filtered_cdm_tree()
        result = self.data_collection_service.get_filter_cdm_text_popup_content()
        parsed_result = json.loads(result)
        events = parsed_result.get('errorType')
        assert events == "TreeNotAllowed", "Expected 'TreeNotAllowed' but got '{}'".format(events)

    def test_11_send_ui_event_when_custom_metadata_has_invalid_app_instance_id_on_settings(self):
        """
        C30794741: Send UI event when custom metadata has invalid AppInstanceId on settings
        """ 
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_app_instanced_id', 'invalid')]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True 
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        result = self.data_collection_service.get_data_valve_controller_status_code()
        assert 'code=200' in result, "failed to get code=200 from result, result: {}".format(result) 
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_verbose_logs_button()
        result = self.data_collection_service.get_verbose_logs_content_text()
        assert "Failed to retrieve filters to the current tree" in result

    def test_12_make_a_request_when_the_cache_is_empty(self):
        """
        C29779395: Make a request when the cache is empty
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is False 
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True

    def test_13_make_a_request_when_the_cache_has_expired_cached_bindings(self):
        """
        C29779397: Make a request when the cache has expired cached bindings
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True
        self.data_collection_service.select_bindings_delete_button()
        self.data_valve.get_v1bindings_text() is False
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True

    def test_14_make_a_request_when_the_cache_has_cached_bindings(self):
        """
        C30794744: Make a request when the cache has cached bindings
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_cached_bindings_tab()
        initial_time_to_expire = self.data_collection_service.get_bindings_time_to_expire_text()
        self.data_valve.get_v1bindings_text() is True
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_cached_bindings_tab()
        current_time_to_expire = self.data_collection_service.get_bindings_time_to_expire_text()
        assert current_time_to_expire < initial_time_to_expire, f"Assertion failed: current time {current_time_to_expire} is not less than initial time {initial_time_to_expire}"

    def test_15_verify_merging_by_send_ui_event_same_custom_metadata_two_times_seperately(self):
        """
        C40387610 - Verify merging by sending UI event with same custom metadata two times separately
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_batching_switch(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("3")
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("1")
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        data_valve_count = self.data_collection_service.verify_count_of_data_valve_ingress()
        assert data_valve_count == 1, "Data valve count does not match"
        self.data_collection_service.select_data_ingress_btn()
        data_ingress_count = self.data_collection_service.verify_count_of_data_valve_ingress()
        assert data_ingress_count == 1, "Data ingress count does not match"

    def test_16_verify_merging_by_send_ui_event_different_custom_metadata_two_times_seperately(self):
        """
        C40387611 - Verify merging by sending UI event with different custom metadata two times separately
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_batching_switch(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.app_instance_id_send_ui)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("1")
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_batching_switch(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("3")
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        data_valve_count = self.data_collection_service.verify_count_of_data_valve_ingress()
        assert data_valve_count == 2, "Data valve count does not match"
        self.data_collection_service.select_data_ingress_btn()
        data_ingress_count = self.data_collection_service.verify_count_of_data_valve_ingress()
        assert data_ingress_count == 2, "Data ingress count does not match"

    def test_17_filter_multiple_valid_cdm_trees_at_once(self):
        """
        C32335632: Filter multiple valid CDM trees at once
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.home.select_filter_cdm_ledm_tab()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_add_valid_cdm_button()
        self.data_collection_service.select_add_button()
        self.data_collection_service.select_apply_filter_button()
        sleep(5)
        assert self.data_collection_service.get_filterd_cdm_text() == 'Filtered'

    def test_18_queueing_an_event(self):
        """
        C30025572: Queueing an event
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_use_custom_metadata_values_switch(True)
        self.data_collection_settings.native_select_asset_unit_item("mobile")
        textbox_values = [('settings_device_id', self.us_region_device_id), ('settings_app_instanced_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("20")
        self.data_collection_service.select_send_button()
        sleep(2)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.home.select_data_collection_service_tab()
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_list_queue_item_button()
        self.data_collection_service.verify_queue_contents() is True 

    def test_19_queueing_an_event_when_queue_flag_unactivated(self):
        """
        C30025573: Queueing an event with queue flag unactivated
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_queue_toggle_button(False)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.set_number_of_calls_value("20")
        self.data_collection_service.select_send_button()
        sleep(2)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.data_collection_service.select_list_queue_item_button()
        self.data_collection_service.verify_queue_contents() is False 

    def test_20_send_ui_event_when_app_instance_id_value_assigned_to_consent_basis_id(self):
        """
        C41381063: Send UI event when AppInstanceId value assigned to ConsentBasisId
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', self.app_instance_id), ('settings_vs_consent_basis_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.data_collection_service.select_send_ui_event_option('Simple Ui Event')
        self.data_collection_service.select_next_button()
        self.data_collection_service.select_send_button()
        sleep(5)
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.home.select_cached_bindings_tab()
        self.data_collection_service.select_binding_filter_button()
        metadata = self.data_valve.get_bindings_filter()
        expected_app_instance_id = 'fc7dfc6b-bf5c-4382-8016-b8da6c7503d9'
        assert 'appInstanceId' in metadata, "appInstanceId key not found in metadata"
        assert metadata['appInstanceId'] == expected_app_instance_id, f"Expected appInstanceId '{expected_app_instance_id}', but got '{metadata['appInstanceId']}'"
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        result = self.data_collection_service.get_data_valve_controller_status_code()
        assert 'code=200' in result, "failed to get code=200 from result, result: {}".format(result)

    def test_21_send_sys_info_event_when_app_instance_id_value_assigned_to_consent_basis_id(self):
        """
        C41381064: Send SysInfo event when AppInstanceId value assigned to ConsentBasisId
        """
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', self.app_instance_id), ('settings_vs_consent_basis_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_send_sys_info_event_button()
        sleep(5)
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.home.select_cached_bindings_tab()
        self.data_collection_service.select_binding_filter_button()
        metadata = self.data_valve.get_bindings_filter()
        expected_app_instance_id = 'fc7dfc6b-bf5c-4382-8016-b8da6c7503d9'
        assert 'appInstanceId' in metadata, "appInstanceId key not found in metadata"
        assert metadata['appInstanceId'] == expected_app_instance_id, f"Expected appInstanceId '{expected_app_instance_id}', but got '{metadata['appInstanceId']}'"
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_request_logs_button()
        self.data_collection_service.select_data_value_btn()
        result = self.data_collection_service.get_data_valve_controller_status_code()
        assert 'code=200' in result, "failed to get code=200 from result, result: {}".format(result)