import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time


pytest.app_info = "HPX"
class Test_Suite_Auido_Presets_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(2)
    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_audio_presets_UI_C32316713(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_presets_text_show() is True, "Presets text is not show"
        assert self.fc.fd["audio"].verify_presets_tooltips_btn_show() is True, "Presets tooltips button is not show"
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_movie_preset()) is True, "Movie preset is not show"
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True, "Voice checkbox is not show"
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True, "Music checkbox is not show"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        
        assert self.fc.fd["audio"].verify_sound_text_show() is False, "Sound text should not show"
        assert self.fc.fd["audio"].verify_bass_text_show() is False, "Bass text is should not show"
        assert self.fc.fd["audio"].verify_treble_text_show() is False, "Treble text should not show"
        assert self.fc.fd["audio"].verify_width_text_show() is False, "Width text should not show"
        time.sleep(2)
    
    
    #suite change to thompson since they should support cycle >= 24C1 on OPP type machine
    @pytest.mark.ota
    @pytest.mark.consumer
    def test_02_select_movie_voice_music_checkbox_C33407732(self,install_app):
        self.fc.restart_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        time.sleep(2)
        
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
        
        self.fc.fd["audio"].click_preset_movie()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie is not be selected"
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice is not be selected"
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
        
    
    @pytest.mark.consumer
    def test_03_check_presets_eq_support_with_internal_speaker_and_headphone_C40430914(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)

        if  self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            time.sleep(2)

        assert self.fc.fd["audio"].verify_presets_text_show() is True
        assert self.fc.fd["audio"].verify_presets_tooltips_btn_show() is True
        time.sleep(2)
        assert self.fc.fd["audio"].verify_movie_checkbox_show() is True
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(5)

        assert self.fc.fd["audio"].verify_equalizer_text_show() is True
        assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show() is True
        assert self.fc.fd["audio"].verify_equalizer_slider_volume_show() is True

        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headphone_on_pc_selected() == "2", "headphone is not be selected"
        time.sleep(2)

        assert self.fc.fd["audio"].verify_presets_text_show() is True
        assert self.fc.fd["audio"].verify_presets_tooltips_btn_show() is True
        time.sleep(2)
        assert self.fc.fd["audio"].verify_movie_checkbox_show() is True
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True
        assert self.fc.fd["audio"].verify_strategy_checkbox_show() is True
        assert self.fc.fd["audio"].verify_rpg_checkbox_show() is True
        assert self.fc.fd["audio"].verify_shooter_checkbox_show() is True
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)

        assert self.fc.fd["audio"].verify_equalizer_text_show() is False
        assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show() is False
        assert self.fc.fd["audio"].verify_equalizer_slider_volume_show() is False