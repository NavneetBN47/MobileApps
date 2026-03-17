import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Performance_External_Speaker_Settings(object):

    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_check_audio_cpu_and_memory_usage_external_speaker_settings_page_C64809571(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)  
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        assert self.fc.get_machine_cpu_usage() < 100, "CPU usage is too high before testing audio performance"
        time.sleep(2)
        assert self.fc.get_memory_usage_percentage() < 100, "Memory usage is too high before testing audio performance"
        time.sleep(2)

        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=19)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        assert self.fc.get_machine_cpu_usage() < 100, "CPU usage is too high before testing audio performance"
        time.sleep(2)
        assert self.fc.get_memory_usage_percentage() < 100, "Memory usage is too high before testing audio performance"
