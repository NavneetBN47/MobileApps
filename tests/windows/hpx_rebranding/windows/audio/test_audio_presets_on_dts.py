import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
import pytest
from SAF.misc.ssh_utils import SSH

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Presets_On_DTS(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_01_check_audio_presets_ui_on_DTS_machine_C42214081(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # select 3.5mm headphone
        if self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device(), "3.5mm headphone option is not displayed in output device combobox"
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(4)
        # check presets options
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_txt_show_up(), "Audio presets RPG text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_txt_show_up(), "Audio presets shooter text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_txt_show_up(), "Audio presets strategy test is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_button_show_up(), "Audio presets RPG button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_button_show_up(), "Audio presets shooter button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_button_show_up(), "Audio presets strategy button is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_02_Presets_options_can_be_selected_C42197674(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        # select 3.5mm headphone
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        if self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device(), "3.5mm headphone option is not displayed in output device combobox"
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(4)
        # check presets options
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_txt_show_up(), "Audio presets RPG text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_txt_show_up(), "Audio presets shooter text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_txt_show_up(), "Audio presets strategy test is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_button_show_up(), "Audio presets RPG button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_button_show_up(), "Audio presets shooter button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_button_show_up(), "Audio presets strategy button is not displayed"
        # select audio presets options
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.fd["audio"].click_audio_presets_RPG_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_RPG_button_status()) is True, "Audio presets RPG button is not be selected"
        self.fc.fd["audio"].click_audio_presets_shooter_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_shooter_button_status()) is True, "Audio presets shooter button is not be selected"
        self.fc.fd["audio"].click_audio_presets_strategy_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_strategy_button_status()) is True, "Audio presets strategy button is not be selected"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_03_check_presets_EQ_with_external_devices_on_non_opp_machine_C42197695(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        # select internal speaker
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_internal_speaker_on_output_device(), "Internal speaker option is not displayed in output device combobox"
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_250_show_up(), "horizontal axis 250 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_500_show_up(), "horizontal axis 500 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_1k_show_up(), "horizontal axis 1k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_2k_show_up(), "horizontal axis 2k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_4k_show_up(), "horizontal axis 4k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"
        # select 3.5mm headphone
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        # select 3.5mm headphone
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device(), "3.5mm headphone option is not displayed in output device combobox"
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(3)
        # check presets options
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_txt_show_up(), "Audio presets RPG text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_txt_show_up(), "Audio presets shooter text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_txt_show_up(), "Audio presets strategy test is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_button_show_up(), "Audio presets RPG button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_button_show_up(), "Audio presets shooter button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_button_show_up(), "Audio presets strategy button is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up() is False, "horizontal axis 32 is displayed"