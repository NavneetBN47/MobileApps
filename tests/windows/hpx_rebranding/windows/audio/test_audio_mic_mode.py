import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Mic_Mode(object):
 
   
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_01_check_mic_mode_ui_C42320612(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        # select internal device for output
        if self.fc.fd["audio"].verify_output_internal_device_show() is False:
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_output_internal_device_show():
                self.fc.fd["audio"].select_output_internal_device()
                time.sleep(3)
            elif self.fc.fd["audio"].verify_output_internal_speaker_commercial_show_up():
                self.fc.fd["audio"].click_output_internal_speaker_commercial()
                time.sleep(2)
            else:
                self.fc.fd["audio"].click_internal_speaker_for_divinity_output_device()
                time.sleep(2)
        # select internal device for input
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_internal_device_show():
                self.fc.fd["audio"].select_input_internal_device()
                time.sleep(3)
            elif self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up():
                self.fc.fd["audio"].click_input_internal_mic_commercial()
                time.sleep(2)
            else:
                self.fc.fd["audio"].click_internal_mic_for_divinity_input_device()
                time.sleep(2)
        # restore default settings by clicking restore defaults button
        self.fc.swipe_window(direction="down", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up(), "Mic mode title is not displayed"
        assert self.fc.fd["audio"].verify_mic_mode_combobox_open_button_show_up(), "Mic mode combobox is not displayed"
        assert self.fc.fd["audio"].verify_conference_show_up(), "conference is not displayed"
   
 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_check_mic_mode_with_different_device_C43809589(self):
        if self.fc.fd["audio"].verify_input_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_internal_device_show():
                self.fc.fd["audio"].select_input_internal_device()
                time.sleep(3)
            else:
                self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up()
                self.fc.fd["audio"].click_input_internal_mic_commercial()
                time.sleep(2)
        # restore default settings by clicking restore defaults button
        self.fc.swipe_window(direction="down", distance=9)
        time.sleep(2)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is not enabled"
        assert self.fc.fd["audio"].verify_conference_show_up() is True, "Conference is not displayed"
        # check input device
        if self.fc.fd["audio"].verify_input_35mm_external_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_35mm_external_device_show():
                self.fc.fd["audio"].select_input_35mm_external_device()
                time.sleep(3)
            else:
                self.fc.fd["audio"].verify_input_35mm_headphone_commercial_show_up()
                self.fc.fd["audio"].click_input_35mm_headphone_commercial()
                time.sleep(2)
        # restore default settings by clicking restore defaults button
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is not enabled"
        assert self.fc.fd["audio"].verify_conference_show_up() is False, "Conference is displayed"
        if self.fc.fd["audio"].verify_input_usb_external_device_show_up() is False:
            assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_usb_external_device_show_up():
                self.fc.fd["audio"].select_input_usb_external_device()
                time.sleep(3)
            else:
                self.fc.fd["audio"].verify_input_usb_headphone_commercial_show_up()
                self.fc.fd["audio"].click_input_usb_headphone_commercial()
                time.sleep(2)
        # restore default settings by clicking restore defaults button
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is not enabled"
        assert self.fc.fd["audio"].verify_conference_show_up() is False, "Conference is displayed"
        time.sleep(3)
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_internal_device_show():
                self.fc.fd["audio"].select_input_internal_device()
                time.sleep(3)
            else:
                self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up()
                self.fc.fd["audio"].click_input_internal_mic_commercial()
                time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1"
        assert self.fc.fd["audio"].verify_conference_show_up() is True, "Conference is not displayed"
        time.sleep(3)
 
 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_03_check_mic_mode_with_hidden_when_turn_off_noise_reduction_C43809591(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        # make sure there is internal device
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_internal_device_show():
                self.fc.fd["audio"].select_input_internal_device()
                time.sleep(3)
            elif self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up():
                self.fc.fd["audio"].click_input_internal_mic_commercial()
                time.sleep(2)
            else:
                self.fc.fd["audio"].click_internal_mic_for_divinity_input_device()
                time.sleep(2)
        # restore default settings by clicking restore defaults button
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is not enabled"
        assert self.fc.fd["audio"].verify_conference_show_up() is True, "Conference is not displayed"
        self.fc.fd["audio"].turn_off_noise_reduction()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_conference_show_up() is False, "Conference is displayed"
        time.sleep(3)
        self.fc.fd["audio"].turn_on_noise_reduction()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_conference_show_up() is True, "Conference is not displayed"
 
   
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_04_check_mic_mode_tooltip_ui_C49136658(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)
        # make sure there is internal device
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            if self.fc.fd["audio"].verify_input_internal_device_show():
                self.fc.fd["audio"].select_input_internal_device()
                time.sleep(3)
            elif self.fc.fd["audio"].verify_input_internal_mic_commercial_show_up():
                self.fc.fd["audio"].click_input_internal_mic_commercial()
                time.sleep(2)
            else:
                self.fc.fd["audio"].click_internal_mic_for_divinity_input_device()
                time.sleep(2)
        # check mic mode tooltip
        assert self.fc.fd["audio"].verify_mic_mode_tooltip_show_up() is True, "Mic mode tooltip is not displayed"
        self.fc.fd["audio"].click_mic_mode_tooltip_contents()
        time.sleep(2)
        if self.fc.fd["audio"].get_mic_mode_tooltip_contents() == "Conference: Reduces background noise when multiple people are speaking.":
            assert self.fc.fd["audio"].get_mic_mode_tooltip_contents() == "Conference: Reduces background noise when multiple people are speaking."
        else:
            assert self.fc.fd["audio"].get_mic_mode_tooltip_contents() == "Personal: Reduces the background noise when only one person is speaking."