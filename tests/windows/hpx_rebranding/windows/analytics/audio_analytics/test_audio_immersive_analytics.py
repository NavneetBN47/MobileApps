import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Audio_Control_Analytics_Immersive(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_turn_on_off_immersive_toggle_analytics_C52040235(self):
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
            self.fc.fd["audio"].click_immersive_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "AdvancedAudioSettings", 
        "action": "OnChange", 
        "controlLabel": "ImmersiveAudio",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/audio_control_filter.json", "audio", 10)