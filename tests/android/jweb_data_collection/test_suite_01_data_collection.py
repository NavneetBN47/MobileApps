from time import sleep
import pytest
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Data_Collection(object):
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
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]

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

    def test_01_data_collection_verify_result_invalidate_cache(self):
        """
        C29821189: Invalidate bindings cache
        - using data collection refApp, navigating to the cached bindings tab and click on reset bindings, to ensure that any cache is loaded previously
        - navigating to webView tab > data collection plugin, inform all the needed parameters
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - outside of webview, navigating to the cached bindings tab to check the filterType as inclusion
        - navigate again to webview and click on invalidate cache to clear the filtering cache
        - verify 'Cache Invalidated' message
        C29794271: Verify result of invalidating the bindings cache on the component reference app
        - return to the cached bindings tab
        - expected to not appear any filtering data after the cache was be cleared
        """
        self.home.select_cached_bindings_tab()
        self.data_valve.select_reset_bindings_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', cdm_btn_change_check={"cc_type": "wait_for_attribute", "wait_obj": "filter_cdm_tree_test_result", "wait_attribute": "text"})
        self.home.select_cached_bindings_tab()
        result = self.data_valve.get_v1bindings_text()
        assert 'inclusion' in result
        self.home.select_webview_tab()
        self.data_collection_plugin.select_invalidate_cache_test_btn()
        assert self.data_collection_plugin.get_invalidate_cache_test_result() == 'Cache invalidated!'
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text(False) == ''

    def test_02_make_a_request_when_the_cache_is_empty(self):
        """
        C29779395: Make a request when the cache is empty
        """
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is False 
        self.home.select_webview_tab()   
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)   
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True 
       
    def test_03_make_a_request_when_the_cache_has_expired_cached_bindings(self):
        """
        C29779397: Make a request when the cache has expired cached bindings
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)   
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True
        self.data_collection_service.select_bindings_delete_button()
        self.data_valve.get_v1bindings_text() is False
        self.home.select_webview_tab()  
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        self.data_valve.get_v1bindings_text() is True

    def test_04_make_a_request_when_the_cache_has_cached_bindings(self):
        """
        C30794744: Make a request when the cache has cached bindings
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)   
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        initial_time_to_expire = self.data_collection_service.get_bindings_time_to_expire_text()
        self.data_valve.get_v1bindings_text() is True
        self.home.select_webview_tab()  
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_cached_bindings_tab()
        current_time_to_expire = self.data_collection_service.get_bindings_time_to_expire_text()
        assert current_time_to_expire < initial_time_to_expire, f"Assertion failed: current time {current_time_to_expire} is not less than initial time {initial_time_to_expire}"

    def test_05_queueing_an_event(self):
        """
        C30025572: Queueing an event
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_queue_toggle_button(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab() 
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)   
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.home.select_data_collection_service_tab()
        self.home.select_filter_cdm_ledm_tab()
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_list_queue_item_button()
        self.data_collection_service.verify_queue_contents() is True

    def test_06_send_ui_event_when_app_instance_id_value_assigned_to_consent_basis_id(self):
        """
        C41381063: Send UI event when AppInstanceId value assigned to ConsentBasisId
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_queue_toggle_button(True)
        self.data_collection_settings.select_allow_batch_switch(True)
        self.data_collection_settings.select_values_store_toggle_button(True)
        textbox_values = [('settings_vs_app_instance_id', self.us_region_app_instance_id_1), ('settings_vs_consent_basis_id', self.us_region_app_instance_id_1)]
        self.data_collection_settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_tracking_identifier_button()
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
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

    def test_07_queueing_an_event_when_queue_flag_unactivated(self):
        """
        C30025573: Queueing an event with queue flag unactivated
        """
        self.fc.flow_load_home_screen()
        self.data_collection_service.select_settings_button()
        sleep(5)
        self.data_collection_settings.select_queue_toggle_button(False)
        self.data_collection_settings.select_settings_save_button()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)   
        self.data_collection_plugin.select_send_simple_ui_event_toggle() 
        self.data_collection_plugin.select_include_vc_metadata_in_event_data_toggle()
        self.data_collection_plugin.send_ui_event_to_publishing_test_button()
        assert self.data_collection_plugin.get_send_ui_event_test_result() == 'UI event Sent!'
        self.home.select_data_collection_service_tab()
        self.data_collection_service.select_accumulator_button()
        self.data_collection_service.select_accumulator_flush_button()
        self.data_collection_service.select_accumulator_back_button()
        self.data_collection_service.select_list_queue_item_button()
        self.data_collection_service.verify_queue_contents() is False  