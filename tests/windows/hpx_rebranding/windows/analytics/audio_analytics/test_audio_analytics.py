import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Audio_Control_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_change_output_volume_slider_analytics_C52040141(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        if self.fc.fd["audio"].get_output_slider_value() == "100":
            self.fc.fd["audio"].set_audio_output_slider_value_decrease_for_analytics(5)
        else:
            self.fc.fd["audio"].set_audio_output_slider_value_increase_for_analytics(5)

        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)
    


    def test_02_turn_on_off_output_mute_toggle_analytics_C52040142(self):
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            self.fc.fd["audio"].click_mute_toggle_for_output()
            time.sleep(2)

        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)


    def test_03_turn_on_off_noise_removal_toggle_analytics_C52040179(self):
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            self.fc.fd["audio"].click_noise_removal_button()
            time.sleep(2)

        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)
    

    def test_04_change_input_volume_analytics_C52040224(self):
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(3)

        if self.fc.fd["audio"].get_input_slider_value() == "100":
            self.fc.fd["audio"].set_audio_input_slider_value_decrease_for_analytics(5)
        else:
            self.fc.fd["audio"].set_audio_input_slider_value_increase_for_analytics(5)
        
        time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)
    

    def test_05_turn_on_off_input_mute_toggle_analytics_C52040225(self):
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(10):
            self.fc.fd["audio"].click_mute_toggle_for_input()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)


    def test_06_turn_on_off_noise_reduction_analytics_C52040226(self):
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        
        for _ in range(10):
            self.fc.fd["audio"].click_noise_reduction_button()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)
    

    def test_07_turn_on_off_speak_swap_toggle_analytics_C52040234(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_speaker_swap_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "SpeakerSwap",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)


    def test_08_select_presets_options_analytics_C52040227(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_audio_presets_movie_button()
            self.fc.fd["audio"].click_audio_presets_music_button()
            self.fc.fd["audio"].click_audio_presets_voice_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_movie_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlLabel": "SelectedPresetMovie",
        "controlAuxParams": "Movie",
        "serial_number": serial_number
        }
        custom_field_movie = {
            "controlAuxParams": "Movie"
        }

        custom_music_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlLabel": "SelectedPresetMusic",
        "controlAuxParams": "Music",
        "serial_number": serial_number
        }
        custom_field_music = {
            "controlAuxParams": "Music"
        }

        custom_voice_filter = {
        "viewName": "BasicSettings", 
        "action": "OnChange", 
        "controlLabel": "SelectedPresetVoice",
        "controlAuxParams": "Voice",
        "serial_number": serial_number
        }
        custom_field_voice = {
            "controlAuxParams": "Voice"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_movie_filter, custom_field_movie)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_music_filter, custom_field_music)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_voice_filter, custom_field_voice)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)