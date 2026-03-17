import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Studio_Recording(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_studio_recording_show_up_C42197742(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        # check studio recording mode with internal device
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up() is True, "Mic mode doesn't show up"
        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
        elif self.fc.fd["audio"].verify_personal_show_up():
            self.fc.fd["audio"].click_personal_items()
        else:
            self.fc.fd["audio"].click_studio_recording_items()
        assert self.fc.fd["audio"].verify_studio_recording_mode_show_up(), "Studio recording is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_remember_studio_recording_state_after_relaunch_hpx_C42197747(self):
        if self.fc.fd["audio"].verify_studio_recording_mode_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=5)
            time.sleep(3)
        # select internal device
            assert self.fc.fd["audio"].verify_mic_mode_title_show_up() is True, "Mic mode title doesn't show up"
            if self.fc.fd["audio"].verify_conference_show_up():
                self.fc.fd["audio"].click_conference_items()
            elif self.fc.fd["audio"].verify_personal_show_up():
                self.fc.fd["audio"].click_personal_items()
                self.fc.fd["audio"].click_studio_recording_items()
            else:
                self.fc.fd["audio"].verify_studio_recording_mode_show_up()
            time.sleep(3)
        self.fc.fd["audio"].verify_studio_recording_mode_show_up(), "Studio recording is not displayed"
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=5)
        self.fc.fd["audio"].verify_studio_recording_mode_show_up(), "Studio recording is not displayed after relaunch"