import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Audio_Control_Analytics_Thompson(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_select_mic_mode_options_analytics_C52040229(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        if self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() != "1":
            self.fc.fd["audio"].click_noise_reduction_button()
            time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(5)
            self.fc.fd["audio"].click_mic_mode_combobox_open_button()
            time.sleep(5)
            self.fc.fd["audio"].selected_conferenece_mode()
            time.sleep(5)
            self.fc.fd["audio"].click_mic_mode_combobox_open_button()
            time.sleep(5)
            self.fc.fd["audio"].selected_personal_mode()
        
        time.sleep(2)
        serial_number = self.fc.get_windows_serial_number()

        custom_personal_filter = {
        "viewName": "BasicSettings", 
        "action": "OnValueChange", 
        "controlAuxParams": "Personal",
        "serial_number": serial_number
        }

        custom_field_personal = {
            "controlAuxParams": "Personal"
        }

        custom_conference_filter = {
        "viewName": "BasicSettings", 
        "action": "OnValueChange", 
        "controlAuxParams": "Conference",
        "serial_number": serial_number
        }

        custom_field_conference = {
            "controlAuxParams": "Conference"
        }

        time.sleep(2)
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_personal_filter, custom_field_personal)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)

        time.sleep(2)
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_conference_filter, custom_field_conference)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)
    


    def test_02_check_eq_sliders_analytics_C52040230(self):
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        eq_8k_value = self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_8k")
        time.sleep(3)
        if eq_8k_value < "12":
            self.fc.fd["audio"].set_audio_input_slider_value_increase_for_analytics("horizontal_axis_8k", 5)
            time.sleep(3)
        else:
            self.fc.fd["audio"].set_eq_slider_value_decrease_for_analytics("horizontal_axis_8k", 5)
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlLabel": "EqSlider",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_03_click_restore_button_analytics_C52040232(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "action": "OnClick", 
        "controlLabel": "RestoreDefaultsButton",
        "serial_number": serial_number
        }

        custom_field = {
            "viewName": "BasicSettings",
            "controlAuxParams": "Click"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter, custom_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 1)
    

    def test_04_click_advanced_settings_analytics_C52040233(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
            self.fc.fd["audio"].click_back_button_on_audio_page()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnClick", 
        "controlLabel": "AdvancedAudioSettings",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)

