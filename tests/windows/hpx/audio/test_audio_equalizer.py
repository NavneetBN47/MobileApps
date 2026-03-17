import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Auido_Equalizer(object):
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
            time.sleep(5)
        yield "select internal speaker"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        cls.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        time.sleep(3)

    #RangeValue.Value are different for different device London and grogu
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_equalizer_UI_C31745544(self):
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()    
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        if (self.fc.fd["audio"].verify_internal_speaker_output_device() == True):
            self.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        else:
            logging.info("Internal speaker Device is not available")
        if (self.fc.fd["audio"].verify_microphone_array_amd_input_device() == True):
            self.fc.fd["audio"].click_microphone_array_amd_input_device()
        else:
            logging.info("Microphone Array AMD Input Device is not available")
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)

        assert self.fc.fd["audio"].verify_equalizer_text_show() is True, "Equalizer text is not visible"
        assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show() is True, "Equalizer tooltip not visible"
        assert self.fc.fd["audio"].verify_equalizer_slider_volume_show() is True, "Equalizer slider 32 not visible"

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_tooltip_equalizer_C32377138(self):
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["audio"].click_equalizer_tootip_icon()
        time.sleep(1)
        eq_sound_tooltip_message = self.fc.fd["audio"].get_equalizer_tootip_txt()
        time.sleep(2)
        assert eq_sound_tooltip_message == "Use the sliders to change the equalizer."
        time.sleep(2)
        self.fc.fd["audio"].click_equalizer_tootip_icon()

    @pytest.mark.consumer
    @pytest.mark.function
    def test_03_restore_defaults_button_will_work_well_with_equalizer_C37540498(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(75,"equalizer_slider_32volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_64volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(60,"equalizer_slider_8kvolume")
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        time.sleep(5)
        restored_32volume = self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume")
        assert restored_32volume == "50", "Equalizer slider 32 value is not 50"
        time.sleep(5)
        restored_64volume = self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume")
        assert restored_64volume == "50", "Equalizer slider 64 value is not 50"
        time.sleep(5)
        restored_8kvolume = self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume")
        assert restored_8kvolume == "50", "Equalizer slider 8k value is not 50"

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_check_Presets_EQ_3bars_will_not_show_with_USB_headphone_C33144985(self):
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        self.fc.fd["audio"].click_headset_tab()
        time.sleep(3)
        
        assert self.fc.fd["audio"].verify_presets_text_show() is False, "Presets text is not visible"
        assert bool(self.fc.fd["audio"].verify_auto_preset_show()) is False, "Auto preset is not show"
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is False, "Voice checkbox is not show"
        assert self.fc.fd["audio"].verify_music_checkbox_show() is False, "Music checkbox is not show"
        assert self.fc.fd["audio"].verify_equalizer_text_show() is False, "Equalizer text is not visible"
        assert self.fc.fd["audio"].verify_sound_text_show() is False, "Sound text is not show"
        assert self.fc.fd["audio"].verify_bass_text_show() is False, "Bass text is not show"
        assert self.fc.fd["audio"].verify_treble_text_show() is False, "Treble text is not show"
        assert self.fc.fd["audio"].verify_width_text_show() is False, "Width text is not show"
        time.sleep(2)

        self.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        time.sleep(3)