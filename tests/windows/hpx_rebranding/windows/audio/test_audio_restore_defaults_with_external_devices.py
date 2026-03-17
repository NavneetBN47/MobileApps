import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Restore_Defaults_With_External_Devices(object):

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_restore_default_work_with_audio_level_C42197786(self):
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # set new settings for output internal speaker
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(6)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_internal_speaker_on_arti()
        time.sleep(3)
        self.fc.fd["audio"].set_audio_output_slider_value_increase(100)
        time.sleep(3)
        self.fc.fd["audio"].click_mute_toggle_for_output()
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_output_status() == "1", "Mute toggle for Output is not set to 1"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        # set new settings for input device-usb headphone
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_usb_external_device_arti()
        time.sleep(3)
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(3)
        self.fc.fd["audio"].click_mute_toggle_for_input()
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "1", "Mute toggle for Input is not set to 1"
        # click restore defaults button
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # verify the settings will be restored to default
        self.fc.swipe_window(direction="up", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].get_output_slider_value() == "40", "Audio output slider doesn't roll back"
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0", "Mute toggle for Input is not set to 0"
        assert self.fc.fd["audio"].get_input_slider_value() != "40", "Audio input slider doesn't roll back"
        assert self.fc.fd["audio"].get_mute_toggle_for_output_status() == "0", "Mute toggle for Output is not set to 1"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_02_restore_default_work_with_external_device_C42197796(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # select 3.5mm headphone for Output device and Input device
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_35mm_external_device_arti()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_35mm_external_device_arti()
        time.sleep(5)
        # set new settings for input device
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up() is True, "Audio presets title doesn't show up"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # check settings will be restored to default
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=4)
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets movie button is not be selected"