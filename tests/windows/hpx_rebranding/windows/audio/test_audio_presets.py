import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Presets(object):
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ota
    def test_01_check_audio_presets_ui_C42214015(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(6)
        self.fc.swipe_window(direction="down", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ota
    def test_02_remember_audio_presets_settings_C42197672(self):
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(4)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        # Go back to the main page and come back to the audio page
        self.fc.swipe_window(direction="up", distance=11)
        time.sleep(4)
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        # relaunch myhp and come back to the audio page
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(6)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    @pytest.mark.ota
    def test_03_check_audio_presets_on_consumer_machine_C68164634(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(6)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        #check audio presets settings after changing
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_check_Contextual_Config_of_audio_card_should_be_same_with_Presets_selected_option_C65575171(self):
        if self.fc.fd["audio"].verify_audio_presets_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(6)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'true', "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'true', "Audio presets movie button is not be selected"
        self.fc.swipe_window(direction="up", distance=10)
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
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed in audio card"