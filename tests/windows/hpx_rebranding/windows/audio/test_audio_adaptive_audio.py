import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Adaptive_Audio(object):


    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_check_adaptive_audio_default_option_music_C42197816(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # check audio card is displayed
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check Presets
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        # check default option
        assert self.fc.fd["audio"].get_presets_movie_button_status() == 'false', "Audio presets movie button is be selected"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].get_presets_voice_button_status() == 'false', "Audio presets voice button is be selected"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_02_check_adaptive_audio_toggles_can_work_well_C42197812(self):
        if self.fc.fd["audio"].verify_audio_presets_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(4)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check Presets
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        # check adaptive audio toggle's status
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=3)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        assert self.fc.fd["audio"].verify_advanced_audio_settings_arrow_show_up(), "Advanced audio settings arrow is not displayed"
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)    
        assert self.fc.fd["audio"].verify_adaptive_audio_settings_title_on_detail_page_show_up(), "Adaptive audio settings title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_title_show_up(), "Adaptive audio title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_show_up(), "Adaptive audio toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_title_show_up(), "Automatic title is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_toggle_show_up(), "Automatic toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_title_show_up(), "Near to display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_title_show_up(), "Far from display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        # check toggle can work well
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        assert self.fc.fd["audio"].get_automatic_toggle_status() == "true", "Automatic toggle is not selected on details page"
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"
        time.sleep(2)
        self.fc.fd["audio"].click_near_to_display_toggle()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        assert self.fc.fd["audio"].get_automatic_toggle_status() == 'false', "Automatic toggle is selected on details page"
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'true', "Near to display toggle is not selected on details page"
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"
        time.sleep(2)
        self.fc.fd["audio"].click_far_from_display_toggle()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        assert self.fc.fd["audio"].get_automatic_toggle_status() == 'false', "Automatic toggle is selected on details page"
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'true', "Far from display toggle is not selected on details page"
        self.fc.fd["audio"].click_automatic_toggle()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        assert self.fc.fd["audio"].get_automatic_toggle_status() == 'true', "Automatic toggle is not selected on details page"
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_restore_default_work_with_adaptive_audio_C42197794(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=14)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # click movie button
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        # verify movie button is selected
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Movie button is not selected"
        time.sleep(5)
        # click adaptive audio button
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        assert self.fc.fd["audio"].verify_advanced_audio_settings_arrow_show_up(), "Advanced audio settings arrow is not displayed"
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify if adaptive audio toggle is off
        if self.fc.fd["audio"].verify_adaptive_audio_toggle_status_not_on() == "0":
            self.fc.fd["audio"].click_adaptive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        time.sleep(2)
        # verify adaptive audio settings UI
        assert self.fc.fd["audio"].verify_adaptive_audio_settings_title_on_detail_page_show_up(), "Adaptive audio settings title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_title_show_up(), "Adaptive audio title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_show_up(), "Adaptive audio toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_title_show_up(), "Automatic title is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_toggle_show_up(), "Automatic toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_title_show_up(), "Near to display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_title_show_up(), "Far from display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        # verify near to display toggle is show
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        time.sleep(2)
        # click near to display button
        self.fc.fd["audio"].click_near_to_display_toggle()
        time.sleep(2)
        # verify near to display toggle is true
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == "true", "Near to display toggle is not selected on details page"
        time.sleep(2)
        # click restore defaults button
        self.fc.fd["audio"].click_advanced_settings_restore_defaults_button()
        time.sleep(3)
        # click return button on top left
        self.fc.fd["devices_details_pc_mfe"].click_return_button_on_top_left_corner()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(3)
        # verify movie button is show
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        time.sleep(1)
        # click adaptive audio settings button
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify adaptive audio settings UI
        assert self.fc.fd["audio"].verify_adaptive_audio_settings_title_on_detail_page_show_up(), "Adaptive audio settings title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_title_show_up(), "Adaptive audio title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_show_up(), "Adaptive audio toggle is not displayed on details page"
        # verify if adaptive audio toggle is off
        if self.fc.fd["audio"].verify_adaptive_audio_toggle_status_not_on() == "0":
            self.fc.fd["audio"].click_adaptive_audio_toggle()
        time.sleep(2)
        # verify adaptive audio toggle is on
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        time.sleep(2)
        # verify automatic toggle is on
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)


    @pytest.mark.function
    @pytest.mark.consumer
    def test_04_check_adaptive_audio_ui_C42229054(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed" 
        # restore defaults button
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        # select Movie option to enable advanced audio settings
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Movie button is not selected"
        # click advanced audio settings button
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify adaptive audio settings UI
        assert self.fc.fd["audio"].verify_adaptive_audio_settings_title_on_detail_page_show_up(), "Adaptive audio settings title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_title_show_up(), "Adaptive audio title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_show_up(), "Adaptive audio toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_title_show_up(), "Automatic title is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_toggle_show_up(), "Automatic toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_title_show_up(), "Near to display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_title_show_up(), "Far from display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_05_verify_adaptive_audio_status_with_different_presets_option_C42197814(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(6)
        # verify movie button is show
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        time.sleep(1)
        # click movie button
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        # verify movie button is selected
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Movie button is not selected"
        time.sleep(5)
        # click adaptive audio button
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify if adaptive audio toggle is off
        if self.fc.fd["audio"].verify_adaptive_audio_toggle_status_not_on() == "0":
            self.fc.fd["audio"].click_adaptive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        time.sleep(2)
        # verify adaptive audio settings UI
        assert self.fc.fd["audio"].verify_adaptive_audio_settings_title_on_detail_page_show_up(), "Adaptive audio settings title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_title_show_up(), "Adaptive audio title is not displayed on details page"
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_show_up(), "Adaptive audio toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_title_show_up(), "Automatic title is not displayed on details page"
        assert self.fc.fd["audio"].verify_automatic_toggle_show_up(), "Automatic toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_title_show_up(), "Near to display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_title_show_up(), "Far from display title is not displayed on details page"
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        # verify automatic toggle is on
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)
        # verify near to display toggle is show
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        time.sleep(2)
        # click near to display button
        self.fc.fd["audio"].click_near_to_display_toggle()
        time.sleep(2)
        # verify near to display toggle is true
        assert bool(self.fc.fd["audio"].get_near_to_display_toggle_status()) is True, "Near to display toggle is not selected on details page"
        time.sleep(2)
        # verify far from display toggle is show
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        time.sleep(2)
        # click far from display button
        self.fc.fd["audio"].click_far_from_display_toggle()
        time.sleep(2)
        # verify far from display toggle is true
        assert bool(self.fc.fd["audio"].get_far_from_display_toggle_status()) is True, "Far from display toggle is not selected on details page"
        time.sleep(2)
        # verify automatic toggle is show
        assert self.fc.fd["audio"].verify_automatic_toggle_show_up(), "Automatic toggle is not displayed on details page"
        time.sleep(2)
        # click automatic button
        self.fc.fd["audio"].click_automatic_toggle()
        time.sleep(2)
        # verify automatic toggle is true
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)

        # click return button on top left
        self.fc.fd["devices_details_pc_mfe"].click_return_button_on_top_left_corner()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)

        # verify voice button is show
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        time.sleep(1)
        # click voice button
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        # verify voice button is selected
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Voice button is not selected"
        time.sleep(5)
        # click adaptive audio settings button
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify adaptive audio toggle is off
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle  is selected on details page"
        time.sleep(2)
        # verify automatic toggle is true
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)
        # verify near to display toggle is off
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        time.sleep(2)
        # verify far from display toggle is off
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"
        time.sleep(2)
    
        # click return button on top left
        self.fc.fd["devices_details_pc_mfe"].click_return_button_on_top_left_corner()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)

        # verify music button is show
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        time.sleep(1)
        # click music button
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(2)
        # verify music button is selected
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Music button is not selected"
        time.sleep(5)
        # click adaptive audio settings button
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify adaptive audio toggle is off
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle  is selected on details page"
        time.sleep(2)
        # verify automatic toggle is true
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)
        # verify near to display toggle is off
        assert self.fc.fd["audio"].get_near_to_display_toggle_status() == 'false', "Near to display toggle is selected on details page"
        time.sleep(2)
        # verify far from display toggle is off
        assert self.fc.fd["audio"].get_far_from_display_toggle_status() == 'false', "Far from display toggle is selected on details page"
        time.sleep(2)

        # click return button on top left
        self.fc.fd["devices_details_pc_mfe"].click_return_button_on_top_left_corner()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)

        # verify movie button is show
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        time.sleep(1)
        # click movie button
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        # verify movie button is selected
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Movie button is not selected"
        time.sleep(5)
        # click adaptive audio button
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # verify if adaptive audio toggle is off
        if self.fc.fd["audio"].verify_adaptive_audio_toggle_status_not_on() == "0":
            self.fc.fd["audio"].click_adaptive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_adaptive_audio_toggle_status_on() == "1", "Adaptive audio toggle is not selected on details page"
        time.sleep(2)
        # verify automatic toggle is on
        assert bool(self.fc.fd["audio"].get_automatic_toggle_status()) is True, "Automatic toggle is not selected on details page"
        time.sleep(2)
        # verify near to display toggle is show
        assert self.fc.fd["audio"].verify_near_to_display_toggle_show_up(), "Near to display toggle is not displayed on details page"
        time.sleep(2)
        # click near to display button
        self.fc.fd["audio"].click_near_to_display_toggle()
        time.sleep(2)
        # verify near to display toggle is true
        assert bool(self.fc.fd["audio"].get_far_from_display_toggle_status()) is True, "Far from display toggle is not selected on details page"
        time.sleep(2)
        # verify far from display toggle is show
        assert self.fc.fd["audio"].verify_far_from_display_toggle_show_up(), "Far from display toggle is not displayed on details page"
        time.sleep(2)
        # click far from display button
        self.fc.fd["audio"].click_far_from_display_toggle()
        time.sleep(2)
        # verify far from display toggle is true
        assert bool(self.fc.fd["audio"].get_far_from_display_toggle_status()) is True, "Far from display toggle is not selected on details page"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_06_restore_default_work_with_studio_recording_C42197795(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_mic_mode_title_show_up(), "Mic mode title is not displayed"
        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
            assert self.fc.fd["audio"].verify_studio_recording_mode_show_up(), "Studio recording is not displayed"
            self.fc.fd["audio"].click_studio_recording_items()
        elif self.fc.fd["audio"].verify_personal_show_up():
            self.fc.fd["audio"].click_personal_items()
            assert self.fc.fd["audio"].verify_studio_recording_mode_show_up(), "Studio recording is not displayed"
            self.fc.fd["audio"].click_studio_recording_items()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=6)
        assert self.fc.fd["audio"].verify_conference_show_up(), "Conference is not displayed"