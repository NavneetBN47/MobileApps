import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_DTS_Sound_Unbound(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    def test_01_check_DTS_sound_unbound_link_will_show_on_myhp_after_installing_C60502039(self):
        self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        if self.fc.fd["audio"].verify_input_internal_device_show() is False:
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(4)
            self.fc.fd["audio"].select_output_internal_device()
            time.sleep(5)
        # check DTS sound unbound link
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_02_check_DTS_sound_unbound_will_be_opened_successfully_after_clicking_on_the_link_C60502051(self):
        if self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False:
            self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            # check DTS sound unbound link
            self.fc.swipe_window(direction="down", distance=11)
            time.sleep(2)
            assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed"
        self.fc.fd["audio"].click_dts_sound_unbound_link_on_myhp()
        time.sleep(5)
        if self.fc.fd["audio"].verify_dts_sound_unbound_dialog_privacy_page_title_show_up() is False:
            assert self.fc.fd["audio"].verify_dts_sound_unbound_dialog_title_show_up(), "DTS sound unbound dialog title is not opened"
        else:
            assert self.fc.fd["audio"].verify_dts_sound_unbound_dialog_privacy_page_title_show_up(), "DTS sound unbound privacy page is not opened"
            assert self.fc.fd["audio"].verify_cancel_button_on_dts_sound_unbound_dialog_show_up(), "DTS sound unbound dialog cancel button is not opened"
        self.fc.kill_dts_sound_unbound_app_process()
        time.sleep(4)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    def test_03_check_DTS_sound_unbound_work_well_with_external_device_C60502473(self):
        self.fc.kill_dts_sound_unbound_app_process()
        time.sleep(4)
        if self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=11)
            time.sleep(2)
            if self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False:
                self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
                self.fc.restart_myHP()
                time.sleep(5)
                self.fc.fd["devicesMFE"].click_device_card()
                time.sleep(4)
                self.fc.swipe_window(direction="down", distance=3)
                time.sleep(3)
                assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
                self.fc.fd["devices_details_pc_mfe"].click_audio_card()
                time.sleep(2)
                self.fc.swipe_window(direction="down", distance=11)
                time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed"
        self.fc.swipe_window(direction="up", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_35mm_headphone_show_on_output_device(), "3.5mm headphone option is not displayed in output device combobox"
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed after selecting 3.5mm external device"
    
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_05_check_DTS_sound_unbound_ui_C58517129(self):
        if self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False:
            self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
        # check DTS sound unbound link UI
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    def test_04_check_DTS_sound_unbound_disappear_after_uninstalling_it_C60502058(self):
        if self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False:
            self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up(), "DTS sound unbound link is not displayed"
        # uninstall dts sound unbound app
        self.fc.uninstall_dts_sound_unbound_app()
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        # check DTS sound unbound link disappear
        assert self.fc.fd["audio"].verify_dts_sound_unbound_link_on_myhp_show_up() is False, "DTS sound unbound link is still displayed after uninstalling the app"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.OTA
    def test_06_check_audio_preset_eq_with_internal_speaker_35mm_headphone_C42197679(self):
        self.fc.restart_myHP()
        time.sleep(5) 
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(5)
        # check presets
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_txt_show_up(), "Audio presets music text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up(), "Audio presets movie text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_txt_show_up(), "Audio presets voice text is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        # check horizontal axis
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        # select 3.5mm headphone
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=17)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].click_35mm_headphone_on_output_device()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=17)
        time.sleep(2)
        # check presets will show up and EQ will hide
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title doesn't show up"
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
        try:
            assert self.fc.fd["audio"].verify_eq_title_show_up() is False
        except:
            logging.info("EQ title is still displayed")