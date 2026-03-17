import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Compatibility(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_components_not_missing_multiple_launch_C42197603(self):
        
        for i in range(5):
            self.fc.close_myHP()
            self.fc.launch_module_using_deeplink("hpx://pcaudio")
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(3)

            # check Output ui
            assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_output_source_title_show_up(), "Output source title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_output_combobox_open_button_show_up(), "Output combobox open button is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_output_volume_title_show_up(), "Output volume title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_output_volume_slider_show_up(), "Output volume slider is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_mute_txt_for_output_show_up(), "Output mute text is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_mute_toggle_for_output_show_up(), "Output mute toggle is not displayed on the " + str(i + 1) + " launch."

            # check Input ui
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_input_source_title_show_up(), "Input source title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_input_combobox_open_button_show_up(), "Input combobox open button is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_input_volume_title_show_up(), "Input volume title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_input_volume_slider_show_up(), "Input volume slider is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_mute_txt_for_input_show_up(), "Output mute text is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_mute_toggle_for_input_show_up(), "Output mute toggle is not displayed on the " + str(i + 1) + " launch."

            # check noise removal ui
            assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up(), "AI Noise Removal toggle is not displayed on the " + str(i + 1) + " launch."
    
            # check noise reduction ui
            assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed on the " + str(i + 1) + " launch."

            # check presets ui
            self.fc.swipe_window(direction="down", distance=5)
            time.sleep(2)
            assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed on the " + str(i + 1) + " launch."

            # check EQ ui
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed on the " + str(i + 1) + " launch."
            # check horizontal axis
            assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_horizontal_axis_1k_show_up(), "horizontal axis 1k is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed on the " + str(i + 1) + " launch."
            # check vertical axis
            assert self.fc.fd["audio"].verify_vertical_axis_15_show_up(), "vertical axis 15 is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_vertical_axis_0_show_up(), "vertical axis 0 is not displayed on the " + str(i + 1) + " launch."
            assert self.fc.fd["audio"].verify_vertical_axis_minus_7_show_up(), "vertical axis minus 7 is not displayed on the " + str(i + 1) + " launch."