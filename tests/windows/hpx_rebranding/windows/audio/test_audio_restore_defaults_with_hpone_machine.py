import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Restore_Defaults_HPOne(object):

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_restore_default_work_with_eq_C42197790(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        if self.fc.fd["audio"].verify_output_internal_device_show_on_london() is False:
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].select_output_internal_device_london()
            time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_32", 100)
        time.sleep(3)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "100", "eq value is not 100"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "50", "eq value is not 50"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_02_restore_default_work_with_hpone_C42197789(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        # select audio presets voice button
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        # check defaults settings after clicking restore defaults button
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_03_verify_music_voice_movie_option_can_select_on_london_platform_C42197675(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)
        # verify audio presets title and text
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        # verify audio presets button is show
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        time.sleep(2)
        # click audio presets music button
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(3)
        # verify audio presets button is selected
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        # verify audio voice button is show
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        time.sleep(2)
        # click audio presets voice button
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(3)
        # verify audio presets button is selected
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        # verify audio movie button is show
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        time.sleep(2)
        # click audio presets movie button
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        # verify audio presets button is selected
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"