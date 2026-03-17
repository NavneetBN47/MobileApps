import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Noise_cancellation_01(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.ARM
    def test_01_noise_cancellation_settings_can_be_remembered_C43809590(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].select_input_internal_device()
        time.sleep(4)
        # restore default settings
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(3)
        # check Noise Cancellation settings
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state(), "AI Noise Removal toggle is not displayed"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
        # check Mic mode settings
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up(), "Mic mode title is not displayed"
        assert self.fc.fd["audio"].verify_mic_mode_combobox_open_button_show_up(), "Mic mode combobox is not displayed"
        assert self.fc.fd["audio"].verify_conference_show_up(), "conference is not displayed"
        # Make new settings
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
            self.fc.fd["audio"].selected_personal_mode()
        else:
            self.fc.fd["audio"].verify_personal_show_up()
        assert self.fc.fd["audio"].verify_personal_show_up(), "personal is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].turn_off_noise_reduction()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(3)
        self.fc.fd["audio"].turn_on_noise_removal()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
        # check noise cancellation settings after navigating back from other page
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "back arrow shows on audio control page"
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
        assert self.fc.fd["audio"].verify_personal_show_up() is False, "personal is displayed"
        # relaunch myHP and check settings
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
        assert self.fc.fd["audio"].verify_personal_show_up() is False, "personal is displayed"
        # select external device and check settings
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_usb_external_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_usb_external_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is not enabled"
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up() is False, "Mic mode title is displayed"
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)
        self.fc.fd["audio"].turn_on_noise_removal()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.ARM
    def test_02_check_noise_removal_status_with_different_external_devices_C43809596(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=9)
        time.sleep(3)
        # check AI Noise Removal settings
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
        # select external device for Output
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_usb_external_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_35mm_external_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.ARM
    def test_03_check_noise_reduction_status_with_different_external_devices_C43809595(self):
        if self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=5)
            time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_internal_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
        # select external device for Input
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_usb_external_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_35mm_external_device()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_04_restore_default_work_with_noise_cancellation_C42197787(self):
        self.fc.reset_hp_application()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # make noise cancellation new settings
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        self.fc.fd["audio"].click_noise_removal_button()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].select_input_internal_device()
        time.sleep(4)
        # make noise cancellation new settings
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        self.fc.fd["audio"].click_noise_reduction_button()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        # check and click restore defaults button
        self.fc.fd["audio"].swipe_to_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction doesn't work with restore defaults"
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "Noise removal doesn't work with restore defaults"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_05_check_Presets_EQ_behaviors_on_opp_machine_C44728466(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"
        # select 3.5mm external device for output side
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_35mm_external_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up() is False, "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is False, "EQ title is displayed"