import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Level_03(object):

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_adjust_internal_speaker_input_volume_slider_max_verify_that_system_volume_is_adjusted_C42197648(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        self.fc.fd["audio"].set_audio_input_slider_value_increase(10)
        time.sleep(20)
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(4)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize() is False:
            self.fc.open_system_settings_sound()
            time.sleep(3)
        self.fc.fd["audio"].click_on_system_settings_maximize_button()
        time.sleep(3)
        system_input_value = self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert round(float(system_input_value)) >= 40, "Internal speaker input value is not reflected on windows setting"
        self.fc.close_windows_settings_panel()
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_set_input_volume_slider_max_C42197661(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        if self.fc.fd["audio"].verify_input_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=5)
            time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(30)
        assert round(float(self.fc.fd["audio"].get_input_slider_value())) == 100, "Input slider value can be set correctly"

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_set_output_volume_slider_max_C42197662(self):
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].set_audio_output_slider_value_increase(100)
        time.sleep(30)
        assert round(float(self.fc.fd["audio"].get_output_slider_value())) == 100, "Output slider value can be set correctly"

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_remember_audio_level_settings_C42197665(self):
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # set new settings for output volume
        self.fc.fd["audio"].set_audio_output_slider_value_increase(100)
        time.sleep(9)
        assert round(float(self.fc.fd["audio"].get_output_slider_value())) == 100, "Output slider value can be set correctly"
        time.sleep(8)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # set new settings for input volume
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(20)
        assert round(float(self.fc.fd["audio"].get_input_slider_value())) == 100, "Input slider value can be set correctly"
        time.sleep(5)
        # check output value after relaunching myhp
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert round(float(self.fc.fd["audio"].get_output_slider_value())) == 100, "Output slider value is not remembered after relaunching myhp"
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert round(float(self.fc.fd["audio"].get_input_slider_value())) == 100, "Input slider value can be set correctly"
        time.sleep(5)


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_turn_on_off_mute_toggle_C52414864(self):
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        # check output mute toggle
        self.fc.fd["audio"].click_mute_toggle_for_output()
        time.sleep(2)
        assert self.fc.fd["audio"].get_mute_toggle_for_output_status() == "1", "Output mute toggle is not turned on"
        self.fc.fd["audio"].click_mute_toggle_for_output()
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_output_status() == "0", "Output mute toggle is not turned off"
        time.sleep(3)
        # check input mute toggle
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        # check input mute toggle
        self.fc.fd["audio"].click_mute_toggle_for_input()
        time.sleep(2)
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "1", "Input mute toggle is not turned on"
        self.fc.fd["audio"].click_mute_toggle_for_input()
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0", "Input mute toggle is not turned off"