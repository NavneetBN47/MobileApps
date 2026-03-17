import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_functional_MEP_notification")
class Test_Suite_Audio_On_ARM_01(object):


    @pytest.mark.function
    @pytest.mark.ARM
    def test_01_check_MEP_with_external_device_C49136467(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_internal_mic_for_divinity_input_device_show_up(), "Internal mic for Divinity input device is not displayed"
        self.fc.fd["audio"].click_internal_mic_for_divinity_input_device()
        time.sleep(4)
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
                assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                self.fc.fd["audio"].click_input_device_on_windows()
                time.sleep(5)
            # check input mic on windows
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            else:
                for _ in range(3):
                    self.fc.close_windows_settings_panel()
                    time.sleep(3)
                    self.fc.open_system_settings_sound()
                    time.sleep(5)
                    if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                        self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                        self.fc.fd["audio"].click_input_mic_on_windows()
                        time.sleep(5)
                        break
                    else:
                        assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                        self.fc.fd["audio"].click_input_device_on_windows()
                        time.sleep(5)
                        assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
                        break
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(5)
        # check mep notification toast pops up after selecting MEP option on windows
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.launch_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up(), "Learn more link is not displayed on myHP"
        # check audio functionality after enable MEP
        noise_reduction_state = self.fc.fd["audio"].is_enabled_noise_reduction_toggle()
        assert noise_reduction_state == 'false' or noise_reduction_state == False, "Noise reduction toggle is enabled after enable MEP"
        # select external device for audio
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_35mm_headphone_for_divinity_output_device()
        time.sleep(4)
        # check audio features after select external devices
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False, "AI Noise Removal title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up() is False, "AI Noise Removal tooltip is displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() is False, "AI Noise Removal toggle is displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Mic mode title is displayed"
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_35mm_headphone_for_divinity_input_device()
        time.sleep(3)
        # check audio features after select external devices
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is True, "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up() is True, "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up() is True, "AI Noise Reduction toggle is not displayed"
        noise_reduction_state = self.fc.fd["audio"].is_enabled_noise_reduction_toggle()
        assert noise_reduction_state == 'false' or noise_reduction_state == False, "Noise reduction toggle is enabled after enable MEP"
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_02_check_audio_will_recover_by_click_link_on_myhp_C49136461(self):
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.close_myHP()
            time.sleep(3)
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
                assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                self.fc.fd["audio"].click_input_device_on_windows()
                time.sleep(5)
            # check input mic on windows
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            else:
                for _ in range(3):
                    self.fc.close_windows_settings_panel()
                    time.sleep(3)
                    self.fc.open_system_settings_sound()
                    time.sleep(5)
                    if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                        self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                        self.fc.fd["audio"].click_input_mic_on_windows()
                        time.sleep(5)
                        break
                    else:
                        assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                        self.fc.fd["audio"].click_input_device_on_windows()
                        time.sleep(5)
                        assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
                        break
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.close_windows_settings_panel()
            time.sleep(5)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(5)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up(), "Learn more link is not displayed on myHP"
        # check audio functionality after enable MEP
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled after enable MEP"
        # click learn more link on MEP
        self.fc.fd["audio"].click_learn_more_link_on_mep()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_go_to_windows_sound_settings_button_on_mep_pop_up_dialog_show_up(), "Learn more link page is not displayed"
        self.fc.fd["audio"].click_go_to_windows_sound_settings_button_on_mep_pop_up_dialog()
        time.sleep(4)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        self.fc.fd["audio"].click_non_mep_option_on_windows()
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check MEP will keep disable on myHP even with external devices
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up() is False, "Windows sound settings displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up() is False, "Learn more link is displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up() is False, "Learn more link is displayed on myHP"
        # select internal device for audio
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_for_divinity_output_device()
        time.sleep(4)
        # restore audio to default settings
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'true' or ai_noise_removal_state == True, "Noise removal toggle is not enabled after enable MEP"


    @pytest.mark.function
    @pytest.mark.ARM
    def test_03_check_noise_removal_status_with_different_devices_C49136436(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        if self.fc.fd["audio"].verify_mep_ui_show_up() is True:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
                assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                self.fc.fd["audio"].click_input_device_on_windows()
                time.sleep(5)
            # check input mic on windows
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            else:
                for _ in range(3):
                    self.fc.close_windows_settings_panel()
                    time.sleep(3)
                    self.fc.open_system_settings_sound()
                    time.sleep(5)
                    if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                        self.fc.fd["audio"].click_on_system_settings_maximize_button()
                        break
                    if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                        self.fc.fd["audio"].click_input_mic_on_windows()
                        time.sleep(5)
                        break
                    else:
                        assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                        self.fc.fd["audio"].click_input_device_on_windows()
                        time.sleep(5)
                        assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
            if self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up() is False:
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
                self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
                time.sleep(5)
                self.fc.fd["audio"].click_non_mep_option_on_windows()
                time.sleep(5)
            # check mep notification toast pops up after selecting MEP option on windows
            self.fc.close_windows_settings_panel()
            time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        # select usb device for audio
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_usb_headphone_for_divinity_output_device()
        time.sleep(4)
        # check audio features after select devices
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False, "AI Noise Removal title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up() is False, "AI Noise Removal tooltip is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is False, "AI Noise Removal toggle is displayed"
         # select 35mm device for audio
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_35mm_headphone_for_divinity_output_device()
        time.sleep(4)
        # check audio features after select devices
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False, "AI Noise Removal title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up() is False, "AI Noise Removal tooltip is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is False, "AI Noise Removal toggle is displayed"
         # select internal device for audio
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_internal_speaker_for_divinity_output_device()
        time.sleep(4)
        # restore audio to default settings
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check audio features after select devices
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is True, "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up() is True, "AI Noise Removal tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "AI Noise Removal toggle is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"


    @pytest.mark.function
    @pytest.mark.ARM
    def test_04_check_noise_reduction_status_with_different_devices_C59592928(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        if self.fc.fd["audio"].verify_mep_ui_show_up() is True:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
                assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                self.fc.fd["audio"].click_input_device_on_windows()
                time.sleep(5)
            # check input mic on windows
            if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            else:
                for _ in range(3):
                    self.fc.close_windows_settings_panel()
                    time.sleep(3)
                    self.fc.open_system_settings_sound()
                    time.sleep(5)
                    if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                        self.fc.fd["audio"].click_on_system_settings_maximize_button()
                        break
                    if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                        self.fc.fd["audio"].click_input_mic_on_windows()
                        time.sleep(5)
                        break
                    else:
                        assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                        self.fc.fd["audio"].click_input_device_on_windows()
                        time.sleep(5)
                        assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
            if self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up() is False:
                self.fc.fd["audio"].click_input_mic_on_windows()
                time.sleep(5)
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
                self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
                time.sleep(5)
                self.fc.fd["audio"].click_non_mep_option_on_windows()
                time.sleep(5)
            # check mep notification toast pops up after selecting MEP option on windows
            self.fc.close_windows_settings_panel()
            time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        # select usb device for audio
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_usb_headphone_for_divinity_input_device()
        time.sleep(4)
        # check audio features after select devices
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is False, "AI Noise Reduction title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up() is False, "AI Noise Reduction tooltip is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up() is False, "AI Noise Reduction toggle is displayed"
         # select 35mm device for audio
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_35mm_headphone_for_divinity_input_device()
        time.sleep(4)
        # check audio features after select devices
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is True, "AI Noise Reduction title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up() is True, "AI Noise Reduction tooltip is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up() is True, "AI Noise Reduction toggle is displayed"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
         # select internal device for audio
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_internal_mic_for_divinity_input_device()
        time.sleep(4)
        # restore audio to default settings
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check audio features after select devices
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is True, "AI Noise Reduction title is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up() is True, "AI Noise Reduction tooltip is displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up() is True, "AI Noise Reduction toggle is displayed"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"