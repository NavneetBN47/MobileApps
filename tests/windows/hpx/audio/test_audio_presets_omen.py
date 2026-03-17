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
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
    
    #omen device arti(DTS)
    @pytest.mark.ota
    def test_01_audio_presets_eq_support_on_omen_tower_pc_dts_with_internal_speaker_3_5mm_headphone_C32348167(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        self.fc.fd["audio"].click_internal_speaker_on_arti_a()
        assert bool(self.fc.fd["audio"].verify_presets_text_show()) is True
        assert bool(self.fc.fd["audio"].verify_presets_tooltips_btn_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_music_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_equalizer_text_show()) is True
        assert bool(self.fc.fd["audio"].verify_equalizer_tooltip_icon_show()) is True
        assert bool(self.fc.fd["audio"].verify_equalizer_slider_volume_show()) is True
        
        self.fc.fd["audio"].click_headphones_realtek_arti()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_presets_text_show()) is True
        assert bool(self.fc.fd["audio"].verify_presets_tooltips_btn_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_music_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_strategy_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_rpg_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_shooter_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_equalizer_text_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_tooltip_icon_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_slider_volume_show()) is False
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is False

    @pytest.mark.ota
    def test_02_audio_presets_eq_dont_support_on_omen_tower_pc_dts_with_internal_speaker_bt_and_usb_headphone_C32355681(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        self.fc.fd["audio"].click_headset_usb()
        assert bool(self.fc.fd["audio"].verify_presets_text_show()) is False
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_music_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_text_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_tooltip_icon_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_slider_volume_show()) is False
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is False
        
        self.fc.fd["audio"].click_headset_bt_output_rameses()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_music_checkbox_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_text_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_tooltip_icon_show()) is False
        assert bool(self.fc.fd["audio"].verify_equalizer_slider_volume_show()) is False
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is False
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is False