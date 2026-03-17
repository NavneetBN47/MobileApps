import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Audio_Control_Analytics_Adaptive(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_turn_on_off_adaptive_audio_toggle_analytics_C52040236(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_adaptive_audio_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "AdaptiveAudio",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)


    def test_02_select_adaptive_audio_settings_radio_buttons_analytics_C52040237(self):
        if self.fc.fd["audio"].verify_adaptive_audio_toggle_status_not_on() == "0":
            self.fc.fd["audio"].click_adaptive_audio_toggle()
            time.sleep(3)
            assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "adaptive audio toggle is on now"

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_near_to_display_toggle()
            self.fc.fd["audio"].click_far_from_display_toggle()
            self.fc.fd["audio"].click_automatic_toggle()

        serial_number = self.fc.get_windows_serial_number()

        custom_near_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "AdvancedAudioRadio",
        "controlAuxParams": "AdvancedAudioRadioNearToDisplay",
        "serial_number": serial_number
        }
        custom_field_near = {
            "controlAuxParams": "NearToDisplay"
        }

        custom_far_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "AdvancedAudioRadio",
        "controlAuxParams": "AdvancedAudioRadioFarFromDisplay",
        "serial_number": serial_number
        }
        custom_field_far = {
            "controlAuxParams": "FarFromDisplay"
        }

        custom_automatic_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "AdvancedAudioRadio",
        "controlAuxParams": "AdvancedAudioRadioAutomatic",
        "serial_number": serial_number
        }
        custom_field_automatic = {
            "controlAuxParams": "Automatic"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_near_filter, custom_field_near)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_far_filter, custom_field_far)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_automatic_filter, custom_field_automatic)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)