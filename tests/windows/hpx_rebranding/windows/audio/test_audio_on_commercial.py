import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
from SAF.misc.ssh_utils import SSH


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_functional_standalone_app")
class Test_Suite_Audio_Control_Commercial(object):


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ota
    def test_01_check_audio_presets_on_commercial_machine_C42197691(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        # verify audio card is displayed on commercial machine
        if self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up() is False:
            self.fc.uninstall_audio_standalone_app_for_commercial_machine()
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # select internal speaker
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_internal_speaker_commercial()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        # verify audio presets UI on commercial machine
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_txt_show_up(), "Audio presets auto text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_button_show_up(), "Audio presets auto button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert bool(self.fc.fd["audio"].get_audio_presets_auto_button_status()) is True, "Audio presets auto button is not be selected"


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.OTA
    def test_02_check_presets_EQ_with_external_devices_on_commercial_machine_C42197694(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_commercial()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Preset title is not visisible"
        assert self.fc.fd["audio"].verify_audio_presets_auto_txt_show_up(), "Audio presets auto text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"
        # select 3.5mm headphone
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        # select 3.5mm headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_35mm_headphone_commercial()
        time.sleep(5)
        # check presets options
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_txt_show_up(), "Audio presets auto text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_button_show_up(), "Audio presets auto button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is False, "EQ title is displayed"
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_commercial()
        time.sleep(4)
        # check EQ options
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Preset title is not visisible"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
       

    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.OTA
    def test_03_check_audio_control_on_commercial_machine_C42197739(self):
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(2)
        if self.fc.fd["audio"].verify_audio_title_on_header_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check Output ui
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_source_title_show_up(), "Output source title is not displayed"
        # make sure presets & eq will show up with internal speaker
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_commercial()
        time.sleep(2)
        # check Input ui
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed"
        assert self.fc.fd["audio"].verify_input_source_title_show_up(), "Input source title is not displayed"
        # check Presets ui
        self.fc.swipe_window(direction="down", distance=7)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_txt_show_up(), "Audio presets auto text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        # check EQ ui
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_eq_title_show_up(), "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"       
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.OTA
    def test_04_check_presets_option_will_change_to_music_with_non_IMAX_apps_C56033772(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check context aware ui 
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check presets default option and select non-default option
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_auto_txt_show_up(), "Audio presets auto text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not selected"
        # add non-IMAX application
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "Add application button is not displayed"
        self.fc.fd["audio"].click_add_application_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
        assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
        self.fc.fd["audio"].search_apps_on_search_frame("Access")
        time.sleep(2)
        self.fc.fd["audio"].click_searched_app_on_search_frame()
        time.sleep(3)
        self.fc.fd["audio"].click_continue_button_on_dialog()
        time.sleep(4)
        # check presets option with non-IMAX apps
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_05_studio_recording_only_show_when_internal_device_C42197744(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        # select 3.5mm headphone
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        # select 3.5mm headphone
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_input_35mm_headphone_commercial()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up() is False, "Mic mode title is displayed"
        assert self.fc.fd["audio"].verify_studio_recording_mode_show_up() is False, "Studio recording is displayed"
        # select internal device
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_input_internal_mic_commercial()
        time.sleep(4)
        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
        elif self.fc.fd["audio"].verify_personal_show_up():
            self.fc.fd["audio"].click_personal_items()
        else:
            self.fc.fd["audio"].click_studio_recording_items()
        assert self.fc.fd["audio"].verify_studio_recording_mode_show_up() is True, "Studio recording is not displayed"


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_06_check_eq_ui_on_commercial_machine_C68235204(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_commercial()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(3)
        # check EQ
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        # check horizontal axis
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_250_show_up(), "horizontal axis 250 is not displayed"
        # check vertical axis
        assert self.fc.fd["audio"].verify_vertical_axis_6_show_up(), "vertical axis 6 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_3_show_up(), "vertical axis 3 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_0_show_up(), "vertical axis 0 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_3_show_up(), "vertical axis minus 3 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_6_show_up(), "vertical axis minus 6 is not displayed"


    @pytest.mark.function
    @pytest.mark.commercial
    def test_07_check_noise_removal_status_with_different_devices_C66761602(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(5)
        # select 3.5mm headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_35mm_headphone_commercial()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up() is True, "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
         # check noise removal toggle status
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"
        self.fc.fd["audio"].click_noise_removal_button()
        time.sleep(4)
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'true' or ai_noise_removal_state == True, "Noise removal toggle is not enabled after clicking"
        # select USB headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_usb_headphone_commercial()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up() is True, "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"
        # select internal device
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_internal_mic_commercial()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up() is True, "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"
        # select USB headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_usb_headphone_commercial()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"
        # select internal device
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_internal_mic_commercial()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"
        # select 3.5mm headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_output_35mm_headphone_commercial()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up() is True, "Noise removal toggle is not displayed"
        ai_noise_removal_state = self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle()
        assert ai_noise_removal_state == 'false' or ai_noise_removal_state == False, "Noise removal toggle is enabled by default"


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ota
    def test_08_check_audio_will_not_show_with_standalone_app_on_commercial_machine_C42197741(self):
        # install audio standalone app
        self.fc.install_audio_standalone_app_for_commercial_machine()
        time.sleep(5)
        # relaunch myhp app to check audio control
        self.fc.restart_myHP()
        time.sleep(4)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        # verify audio card is not displayed after installing audio standalone app
        assert self.fc.fd["audio"].verify_audio_control_card_show_up() is False, "Audio card is displayed after installing audio standalone app"
        # Uninstall audio standalone app
        self.fc.uninstall_audio_standalone_app_for_commercial_machine()
        time.sleep(5)
        # relaunch myhp app to check audio control
        self.fc.restart_myHP()
        time.sleep(4)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_control_card_show_up(), "Audio card is not displayed after uninstalling audio standalone app"