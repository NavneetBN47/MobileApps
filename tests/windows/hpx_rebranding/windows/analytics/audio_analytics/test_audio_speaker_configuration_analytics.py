import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Audio_Control_Analytics_Speaker_Configuration(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_click_external_speaker_settings_toggle_analytics_C52040238(self):
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
        "controlLabel": "ExternalSpeakerSettings",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)
    

    def test_02_click_paly_all_button_analytics_C52077315(self):
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

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_play_all_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "PlayAllButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_03_select_external_speaker_settings_radio_buttons_analytics_C52078199(self):
        if self.fc.fd["audio"].verify_external_speaker_settings_text_show_up() is False:
            time.sleep(2)
            self.fc.restart_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=18)
            time.sleep(3)
            assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
            time.sleep(2)
            self.fc.fd["audio"].click_external_speaker_settings()
            time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)
        
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_speaker_configuration_open_option()
            time.sleep(2)
            self.fc.fd["audio"].select_speaker_configuration_option_surround()
            self.fc.fd["audio"].click_speaker_configuration_open_option()
            time.sleep(2)
            self.fc.fd["audio"].select_speaker_configuration_option_stereo()
            self.fc.fd["audio"].click_speaker_configuration_open_option()
            time.sleep(2)
            self.fc.fd["audio"].select_speaker_configuration_option_quad()

        serial_number = self.fc.get_windows_serial_number()

        custom_surround_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "SpeakerConfigSelect",
        "controlAuxParams": "SpeakerConfigSelectSurround",
        "serial_number": serial_number
        }
        custom_field_surround = {
            "controlAuxParams": "Surround"
        }

        custom_quad_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "SpeakerConfigSelect",
        "controlAuxParams": "SpeakerConfigSelectQuad",
        "serial_number": serial_number
        }
        custom_field_quad = {
            "controlAuxParams": "Quad"
        }

        custom_stereo_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "SpeakerConfigSelect",
        "controlAuxParams": "SpeakerConfigSelectStereo",
        "serial_number": serial_number
        }
        custom_field_stereo = {
            "controlAuxParams": "Stereo"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_surround_filter, custom_field_surround)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_stereo_filter, custom_field_stereo)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_quad_filter, custom_field_quad)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)


    def test_04_click_multiple_straming_toggle_analytics_C52078200(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        if self.fc.fd["audio"].verify_multistreaming_toggle_on_show_up() is False:
            self.fc.fd["audio"].click_multistreaming_toggle_off_state()
            assert self.fc.fd["audio"].verify_multistreaming_toggle_on_show_up() , "Multistreaming toggle is not displayed"
            time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_multistreaming_toggle_on_state()
            time.sleep(2)
            self.fc.fd["audio"].click_multistreaming_toggle_off_state()

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnChange", 
        "controlLabel": "MultiStreaming",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_05_click_front_left_speaker_analytics_C52078201(self):
        if self.fc.fd["audio"].verify_front_left_speaker_title_show_up() is False:
            time.sleep(2)
            self.fc.restart_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
            self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
            time.sleep(2)
            # click external speaker settings restore default button
            self.fc.fd["audio"].click_external_speaker_settings_restore_default()
            time.sleep(3)
            self.fc.swipe_window(direction="up", distance=16)
            time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_title_show_up(), "Front left speaker title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_play_button_show_up(), "Front left speaker play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_front_left_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "FrontLeftSpeakerPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_05_click_front_right_speaker_analytics_C52078205(self):
        if self.fc.fd["audio"].verify_front_right_speaker_title_show_up() is False:
            time.sleep(2)
            self.fc.restart_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
            self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
            time.sleep(2)
            # click external speaker settings restore default button
            self.fc.fd["audio"].click_external_speaker_settings_restore_default()
            time.sleep(3)
            self.fc.swipe_window(direction="up", distance=16)
            time.sleep(2)
        assert self.fc.fd["audio"].verify_front_right_speaker_title_show_up(), "Front right speaker title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_right_speaker_play_button_show_up(), "Front right speaker play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_front_right_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "FrontRightSpeakerPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_07_click_back_left_speaker_analytics_C52078208(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_quad_show_up(), "Speaker configuration option quad is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].select_speaker_configuration_option_quad()
        time.sleep(2)  
        assert self.fc.fd["audio"].verify_back_left_speaker_title_show_up(), "Back left speaker title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_back_left_speaker_play_button_show_up(), "Back left speaker play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_back_left_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "BackLeftSpeakerPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_08_click_back_right_speaker_analytics_C52079881(self):
        if self.fc.fd["audio"].verify_back_right_speaker_title_show_up() is False:
            time.sleep(2)
            self.fc.restart_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
            self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
            time.sleep(2)
            # click external speaker settings restore default button
            self.fc.fd["audio"].click_external_speaker_settings_restore_default()
            time.sleep(3)
            self.fc.swipe_window(direction="up", distance=16)
            time.sleep(2)
            self.fc.fd["audio"].click_speaker_configuration_open_option()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speaker_configuration_option_quad_show_up(), "Speaker configuration option quad is not displayed"
            time.sleep(2)
            self.fc.fd["audio"].select_speaker_configuration_option_quad()
            time.sleep(2)  
        assert self.fc.fd["audio"].verify_back_right_speaker_title_show_up(), "Back right speaker title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_back_right_speaker_play_button_show_up(), "Back right speaker play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_back_right_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "BackRightSpeakerPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


    def test_09_click_subwoofer_speaker_analytics_C52079901(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up(), "Speaker configuration option surround is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].select_speaker_configuration_option_surround()
        time.sleep(2)  
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_subwoofer_title_show_up(), "Subwoofer title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_subwoofer_play_button_show_up(), "Subwoofer play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_back_left_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "SubwooferPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)


   def test_10_click_center_speaker_analytics_C52079904(self):
    if self.fc.fd["audio"].verify_center_speaker_title_show_up() is False:
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up(), "Speaker configuration option surround is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].select_speaker_configuration_option_surround()
        time.sleep(2)  
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_center_speaker_title_show_up(), "Center speaker title is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_center_speaker_play_button_show_up(), "Center speaker play button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["audio"].click_center_speaker_play_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "CenterSpeakerPlayButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 5)

    
    def test_11_click_front_left_speaker_distance_open_button_analytics_C52078203(self):
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up(), "Speaker configuration option surround is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].select_speaker_configuration_option_surround()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_distance_open_button_show_up(), "Front left speaker distance open button is not displayed"
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_front_left_speaker_distance_open_button()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "FrontLeftSpeakerDistanceOpenButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)

    
    def test_12_click_front_left_volume_open_button_analytics_C52078204(self):
        if self.fc.fd["audio"].verify_front_left_speaker_volume_open_button_show_up() is False:
            time.sleep(2)
            self.fc.restart_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
            self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
            time.sleep(2)
            # click external speaker settings restore default button
            self.fc.fd["audio"].click_external_speaker_settings_restore_default()
            time.sleep(3)
            self.fc.swipe_window(direction="up", distance=16)
            time.sleep(2)
            self.fc.fd["audio"].click_speaker_configuration_open_option()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up(), "Speaker configuration option surround is not displayed"
            time.sleep(2)
            self.fc.fd["audio"].select_speaker_configuration_option_surround()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_front_left_speaker_volume_open_button_show_up(), "Front left speaker volume open button is not displayed"
            time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["audio"].click_front_left_speaker_volume_open_button()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {
        "viewName": "ExternalSpeakerSettings", 
        "action": "OnClick", 
        "controlLabel": "FrontLeftSpeakerVolumeOpenButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)