import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Restore_Defaults(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_01_check_restore_defaults_ui_C42227652(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_02_restore_default_work_with_preset_C42197788(self):
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)
        if self.fc.fd["audio"].verify_audio_presets_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(4)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Movie button is not selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    @pytest.mark.ota
    def test_03_restore_default_work_with_eq_C42197799(self):
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        if self.fc.fd["audio"].verify_eq_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=15)
            time.sleep(3)
        assert self.fc.fd["audio"].verify_eq_title_show_up(), "EQ title is not displayed"
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_32", 150)
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(5)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "0", "eq value is not 0"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_verify_audio_work_well_after_click_restore_default_button_C42197797(self):
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check audio can work well after clicking restore defaults button
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_05_restore_default_work_with_context_aware_C42197798(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        # add application
        self.fc.fd["audio"].click_add_application_button()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
        assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
        time.sleep(5)
        self.fc.fd["audio"].search_apps_on_search_frame("Access")
        time.sleep(5)
        self.fc.fd["audio"].click_searched_app_on_search_frame()
        time.sleep(3)
        self.fc.fd["audio"].click_continue_button_on_dialog()
        time.sleep(5)
        # check Presets default status
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"
        # add new presets option for added application
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        assert self.fc.fd["audio"].get_presets_music_button_status() == 'false', "Audio presets music button is be selected"
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        # make new settings for noise removal toggle
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        if self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0":
            self.fc.fd["audio"].turn_on_noise_removal()
            time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is turned off"
        # click restore defaults button
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        # verify all settings are restored to default status
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Music button is not be selected"