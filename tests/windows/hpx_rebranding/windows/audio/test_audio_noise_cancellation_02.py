import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Noise_Cancellation_02(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_noise_cancellation_on_gen3_device_C43809594(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False, "AI Noise Removal title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up() is False, "AI Noise Removal tooltip is displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() is False, "AI Noise Removal toggle is displayed"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        if not self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up():
            time.sleep(2)
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].click_input_internal_mic_commercial()
            time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed"