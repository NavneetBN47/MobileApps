import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from SAF.misc.ssh_utils import SSH


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_With_External_Devices(object):

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_change_output_device_and_verify_eq_slider_C42197630(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        for _ in range(3):
            if self.fc.fd["audio"].verify_output_combobox_unavailable_show_up():
                self.fc.restart_myHP()
                self.fc.fd["devicesMFE"].click_device_card()
                time.sleep(4)
                self.fc.swipe_window(direction="down", distance=2)
                time.sleep(3)
                assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
                self.fc.fd["devices_details_pc_mfe"].click_audio_card()
                time.sleep(4)
                assert self.fc.fd["audio"].verify_output_combobox_unavailable_show_up() is False, "Output combobox is still unavailable"
                break
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(3)
        # set new eq values for output device
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        eq_8k_value = self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_8k")
        time.sleep(3)
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_8k", 120)
        time.sleep(20)
        assert eq_8k_value != self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_8k"), "eq value doesn't set to 120"
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(3)
        eq_8k_value = self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_16k")
        time.sleep(3)
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_16k", 120)
        assert eq_8k_value != self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_16k"), "eq value doesn't set to 120"
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.consumer
    def test_02_eq_should_not_show_with_connect_usb_headphone_C42197632(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_usb_headphone_on_DTS()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up() is False, "horizontal axis 32 is displayed"
        self.fc.swipe_window(direction="up", distance=12)
        time.sleep(3)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(3)

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_03_check_myhp_work_well_even_presets_option_disappear_along_with_usb_headphone_C42197778(self):
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check presets settings
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_audio_presets_title_show_up()) is True, "Preset title is not visible"
        assert bool(self.fc.fd["audio"].verify_audio_presets_music_txt_show_up()) is True, "Audio presets music text is not displayed"
        assert bool(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up()) is True, "Audio presets movie text is not displayed"
        assert bool(self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up()) is True, "Audio presets voice text is not displayed"
        assert bool(self.fc.fd["audio"].verify_audio_presets_music_button_show_up()) is True, "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].verify_audio_presets_movie_button_show_up()) is True, "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].verify_audio_presets_voice_button_show_up()) is True, "Audio presets voice button is not displayed"
        assert bool(self.fc.fd["audio"].verify_eq_title_show_up()) is True, "EQ title is not displayed"
        # select usb headphone for output side
        self.fc.swipe_window(direction="up", distance=8)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_usb_headphone_on_DTS()
        time.sleep(3)
        # check eq settings
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up() is False, "Preset title is visible"
        assert bool(self.fc.fd["audio"].verify_audio_presets_music_txt_show_up()) is False, "Audio presets music text is not displayed"
        assert bool(self.fc.fd["audio"].verify_eq_title_show_up()) is False, "EQ title is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_04_check_Presets_EQ_behaviors_with_different_external_devices_C42197681(self):
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
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
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_250_show_up(), "horizontal axis 250 is not displayed"
        # select 3.5mm external device for output side
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up() is True, "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is False, "EQ title is displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_05_check_Presets_EQ_behaviors_with_USB_headphone_C42197696(self):
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
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
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        # select usb headphone for output side
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_usb_headphone_on_DTS()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up() is False, "Audio presets title is displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is False, "EQ title is displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up() is False, "horizontal axis 32 is displayed"
        self.fc.swipe_window(direction="up", distance=12)
        time.sleep(3)

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_06_check_The_Contextual_Config_of_audio_card_should_be_same_even_with_external_devices_exist_C65576932(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'true', "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_usb_headphone_on_DTS()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        if self.fc.fd["audio"].verify_back_button_on_audio_page():
            assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "Back button is not displayed on the top left of audio page"
            self.fc.fd["audio"].click_back_button_on_audio_page()
            time.sleep(4)
        else:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed in audio card"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_07_check_The_Contextual_Config_of_audio_card_should_be_same_even_with_external_devices_exist_C65576799(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_output_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_output_combobox_show_up() is True, "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(3)
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_txt_show_up(), "Audio presets RPG button is displayed"
        assert self.fc.fd["audio"].verify_audio_presets_shooter_txt_show_up(), "Audio presets shooter button is displayed"
        assert self.fc.fd["audio"].verify_audio_presets_strategy_txt_show_up(), "Audio presets strategy text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_button_show_up(), "Audio presets RPG button is not displayed"
        self.fc.fd["audio"].click_audio_presets_RPG_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_RPG_button_status() == 'true', "Audio presets RPG button is not be selected"
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(5)
        if self.fc.fd["audio"].verify_back_button_on_audio_page():
            assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "Back button is not displayed on the top left of audio page"
            self.fc.fd["audio"].click_back_button_on_audio_page()
            time.sleep(4)
        else:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_RPG_txt_show_up(), "Audio presets RPG text is not displayed in audio card"
        