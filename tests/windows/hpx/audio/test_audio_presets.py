import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Auido_Presets(object):
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
            time.sleep(2)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_check_audio_presets_options_grogu_C32796913(self):
        self.fc.restart_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_presets_text_show() is True
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        time.sleep(2)

        bass_value_music = int(self.fc.fd["audio"].get_slider_value("bass_slider"))

        if bass_value_music >= 100:
            self.fc.fd["audio"].set_slider_value_decrease(20,"bass_slider")
            time.sleep(2)
            assert self.fc.fd["audio"].get_slider_value("bass_slider") != "90", "bass value is 90"
        else:
            self.fc.fd["audio"].set_slider_value_increase(1,"bass_slider")
            time.sleep(2)
            bass_value_music_changed = int(self.fc.fd["audio"].get_slider_value("bass_slider"))
            assert bass_value_music == bass_value_music_changed - 1, {}.format("bass_value_music not reduce 1")
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=1)
        time.sleep(2)

        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)

        bass_value_voice = int(self.fc.fd["audio"].get_slider_value("bass_slider"))

        if bass_value_music >= 100:
            self.fc.fd["audio"].set_slider_value_decrease(20,"bass_slider")
            time.sleep(2)
            assert self.fc.fd["audio"].get_slider_value("bass_slider") != "90", "bass value is 90"
        else:
            self.fc.fd["audio"].set_slider_value_increase(1,"bass_slider")
            time.sleep(2)
            bass_value_music_changed = int(self.fc.fd["audio"].get_slider_value("bass_slider"))
            assert bass_value_voice == bass_value_music_changed - 1, {}.format("bass_value_music not reduce 1")
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        time.sleep(2)

        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        time.sleep(2)
        
        self.fc.fd["audio"].set_slider_value_decrease(100,"bass_slider")
        bass_slider_value_movie = int(self.fc.fd["audio"].get_slider_value("bass_slider"))
        assert bass_slider_value_movie != 100, "bass_slider_value_movie is 100"
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        

    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_tooltip_sound_button_C32377130(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        time.sleep(2)
        
        assert self.fc.fd["audio"].verify_sound_text_show() is True
        assert self.fc.fd["audio"].verify_sound_tooltips_btn_show() is True
        
        self.fc.fd["audio"].click_sound_tooltips_btn()
        time.sleep(1)
        sound_tooltip_message = self.fc.fd["audio"].get_sound_tooltips_text()
        assert sound_tooltip_message == "Use the sliders to change the audio"
        time.sleep(2)
        self.fc.fd["audio"].click_sound_tooltips_btn()
        self.fc.fd["audio"].click_preset_music()
    

    @pytest.mark.consumer
    def test_03_check_movie_voice_music_on_London_C32770329(self):
        self.fc.restart_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_preset_music_show()) is True
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True

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
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["not available"])
    def test_04_slide_width_slider_C32770335(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"width_slider")
        time.sleep(2)
        width_value = self.fc.fd["audio"].get_slider_value("width_slider")
        assert width_value == "100", "width value is not equaled to 100"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["not available"])
    def test_05_slide_treble_slider_C32770336(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"treble_slider")
        time.sleep(2)
        treble_value = self.fc.fd["audio"].get_slider_value("treble_slider")
        assert treble_value == "100", "treble value is not equaled to 100"
        
        
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["not available"])
    def test_06_slide_bass_slider_C32789790(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"bass_slider")
        time.sleep(2)
        bass_value = self.fc.fd["audio"].get_slider_value("bass_slider")
        assert bass_value == "100", "bass value is not equaled to 100"
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.require_platform(["not available"])
    def test_07_verify_slider_value_should_save_C31745582(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=1)
        
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is True
        
        self.fc.fd["audio"].set_slider_value_increase(100,"bass_slider")
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"treble_slider")
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"width_slider")
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_decrease(100,"bass_slider")
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_decrease(100,"treble_slider")
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_decrease(100,"width_slider")
        time.sleep(2)
        bass_value = self.fc.fd["audio"].get_slider_value("bass_slider")
        assert bass_value == "0", "bass value is not equaled to 0"
        treble_value = self.fc.fd["audio"].get_slider_value("treble_slider")
        assert treble_value == "0", "treble value is not equaled to 0"
        width_value = self.fc.fd["audio"].get_slider_value("width_slider")
        assert width_value == "0", "width value is not equaled to 0"
        
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)        
        assert self.fc.fd["audio"].get_slider_value("bass_slider") != "0", "bass value is 0"       
        assert self.fc.fd["audio"].get_slider_value("treble_slider") != "0", "treble value is 0"       
        assert self.fc.fd["audio"].get_slider_value("width_slider") != "0", "width value is 0" 
        self.fc.fd["audio"].set_slider_value_increase(100,"bass_slider")
        self.fc.fd["audio"].set_slider_value_increase(100,"treble_slider")
        self.fc.fd["audio"].set_slider_value_increase(100,"width_slider")
        time.sleep(2)
        
        self.fc.fd["audio"].set_slider_value_decrease(10,"bass_slider")
        self.fc.fd["audio"].set_slider_value_decrease(5,"treble_slider")
        self.fc.fd["audio"].set_slider_value_decrease(10,"width_slider")
        
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        
        bass_value = self.fc.fd["audio"].get_slider_value("bass_slider")
        assert bass_value == "0", "bass value is 0" 
        treble_value = self.fc.fd["audio"].get_slider_value("treble_slider")
        assert treble_value == "0", "treble value is 0" 
        width_value = self.fc.fd["audio"].get_slider_value("width_slider")
        assert width_value == "0", "width value is 0"
        
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        assert self.fc.fd["audio"].get_slider_value("bass_slider") == "90", "bass value is not equaled to 90" 
        assert self.fc.fd["audio"].get_slider_value("treble_slider") == "95", "treble value is not equaled to 95"
        assert self.fc.fd["audio"].get_slider_value("width_slider") == "90", "width value is not equaled to 90"
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_08_restore_defaults_button_work_well_with_presets_C32881468(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(6)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.require_platform(["not available"])
    def test_09_restore_defaults_button_will_work_well_with_presets_app_C37540395(self):
        self.fc.re_install_app_and_skip_fuf(self.driver.session_data["installer_path"])
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_auto_preset_show()) is True
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(6)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"
        #verify all 3 bars have different values
        self.fc.swipe_window(direction="down", distance=2)
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is True
        bass_slider_music_value_before_change= self.fc.fd["audio"].get_slider_value("bass_slider")
        trible_slider_music_value_before_change= self.fc.fd["audio"].get_slider_value("treble_slider")
        width_slider_music_value_before_change= self.fc.fd["audio"].get_slider_value("width_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"bass_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"treble_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"width_slider")
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        bass_slider_music_value_after_change= self.fc.fd["audio"].get_slider_value("bass_slider")
        trible_slider_music_value_after_change= self.fc.fd["audio"].get_slider_value("treble_slider")
        width_slider_music_value_after_change= self.fc.fd["audio"].get_slider_value("width_slider")
        assert bass_slider_music_value_before_change == bass_slider_music_value_after_change, "Restore defaults doesn't work with bass slider"
        assert trible_slider_music_value_before_change == trible_slider_music_value_after_change, "Restore defaults doesn't work with treble slider"
        assert width_slider_music_value_before_change == width_slider_music_value_after_change, "Restore defaults doesn't work with width slider"
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice is not be selected"
        #verify all 3 bars have different values
        self.fc.swipe_window(direction="down", distance=2)
        assert bool(self.fc.fd["audio"].verify_bass_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_trible_slider_show()) is True
        assert bool(self.fc.fd["audio"].verify_width_slider_show()) is True
        bass_slider_voice_value_before_change= self.fc.fd["audio"].get_slider_value("bass_slider")
        trible_slider_voice_value_before_change= self.fc.fd["audio"].get_slider_value("treble_slider")
        width_slider_voice_value_before_change= self.fc.fd["audio"].get_slider_value("width_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"bass_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"treble_slider")
        self.fc.fd["audio"].set_slider_value_increase(1,"width_slider")
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        bass_slider_voice_value_after_change= self.fc.fd["audio"].get_slider_value("bass_slider")
        trible_slider_voice_value_after_change= self.fc.fd["audio"].get_slider_value("treble_slider")
        width_slider_voice_value_after_change= self.fc.fd["audio"].get_slider_value("width_slider")
        assert bass_slider_voice_value_before_change == bass_slider_voice_value_after_change, "Restore defaults doesn't work with bass slider"
        assert trible_slider_voice_value_before_change == trible_slider_voice_value_after_change, "Restore defaults doesn't work with treble slider"
        assert width_slider_voice_value_before_change == width_slider_voice_value_after_change, "Restore defaults doesn't work with width slider"
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_10_remember_presets_selected_when_re_launch_hpx_C38331202(self):
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not be selected"

        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice is not be selected"

        time.sleep(2)
        self.fc.restart_app()

        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        # time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice is not be selected"
        