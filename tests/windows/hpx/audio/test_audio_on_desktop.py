from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Desktop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    
    def round_up(self,input_value):
        return round(float(input_value))
 
    # TC 1 to 6 can only run on arti as external speaker only connected to arti other devices comes with speakers.
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_adjust_headphone_output_volume_slider_verify_that_system_input_volume_is_adjusted_C31675810(self):
        time.sleep(2)
        self.fc.restart_myHP()
        
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_headphones_realtek_arti()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(5)
        
        self.fc.fd["audio"].click_windows_speaker_icon()
        time.sleep(2)
        assert "100" ==self.fc.fd["audio"].get_system_volume(), "system volume is not 100"
        self.fc.fd["audio"].click_windows_speaker_icon()
        

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_adjust_usb_headphone_output_volume_slider_verify_that_system_input_volume_is_adjusted_C31675809(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_headset_tab()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(5)
        
        self.fc.fd["audio"].click_windows_speaker_icon()
        time.sleep(2)
        assert "100" ==self.fc.fd["audio"].get_system_volume(), "system volume is not 100"
        self.fc.fd["audio"].click_windows_speaker_icon()
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_restore_defaults_button_works_well_with_audio_level_C37542498(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_headset_tab()
        self.fc.fd["audio"].click_headset_usb_output()
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(10,"output_slider")
        time.sleep(5)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(10,"input_slider")
        self.fc.fd["audio"].click_input_mute_button()
        input_mute = self.fc.fd["audio"].get_input_mute_button_name()
        if "On" in input_mute:
            self.fc.fd["audio"].click_input_mute_button()
        time.sleep(2)
        assert "Off" in self.fc.fd["audio"].get_input_mute_button_name(),"Mic is not mute"
        
        output_mute = self.fc.fd["audio"].get_output_mute_button_name()
        if "On" in output_mute:
            self.fc.fd["audio"].click_output_mute_button()
        assert "Off" in self.fc.fd["audio"].get_output_mute_button_name(),"Speaker is not mute"
        time.sleep(2)
        
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=4)
        
        myhp_mic_status = self.fc.fd["audio"].get_input_mute_button_name()
        assert "Off" in myhp_mic_status,"App Mic is unmute -{}" .format(myhp_mic_status)
        myhp_speaker_status=self.fc.fd["audio"].get_output_mute_button_name()
        assert "Off" in myhp_speaker_status,"App Speaker is unmute -{}" .format(myhp_speaker_status)
        output_value_restored = self.fc.fd["audio"].get_slider_value("output_slider")
        output_value = output_value_restored
        
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_adjust_usb_headset_input_volume_slide_verify_that_system_input_volume_adjusted_C31675849(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_headset_usb_output()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(10,"input_slider")
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("input_slider")
        self.fc.close_myHP()
        self.fc.open_system_settings_sound()
        
        self.fc.swipe_window(direction="down", distance=3)
        value=self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert self.round_up(value) == self.round_up(output_value),"usb volume not in sync with system volume"
        self.fc.close_windows_settings_panel()
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_adjust_3_5mm_headset_input_volume_slider_verify_that_system_input_volume_is_adjusted_C31675850(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        #verify 3.5mm headset for input device is visible
        self.fc.fd["audio"].verify_home_audio_show()
        assert bool(self.fc.fd["audio"].verify_3_5mm_headphone_input_device()) is True, "3.5mm headset is not visible"
        self.fc.fd["audio"].select_headphone_input_device()
        time.sleep(2)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_decrease(10,"input_slider")
        time.sleep(5)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        self.fc.close_myHP()
        self.fc.open_system_settings_sound()
        self.fc.swipe_window(direction="down", distance=6)
        input_value=self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert self.round_up(input_value) == self.round_up(input_value),"usb volume not in sync with system volume"
        self.fc.close_windows_settings_panel()
        

    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_check_DTS_audio_presets_C32610259(self):
        self.fc.launch_myHP()
        time.sleep(2)
        if not self.fc.fd["audio"].verify_movie_preset():
            self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        
        self.fc.fd["audio"].click_headphones_realtek_arti()
        time.sleep(2)
    
        assert self.fc.fd["audio"].verify_presets_text_show() is True, "Presets text is not visible"
        assert self.fc.fd["audio"].verify_presets_tooltips_btn_show() is True, "Presets tooltips button is not visible"
        time.sleep(2)
        
        assert self.fc.fd["audio"].verify_movie_checkbox_show() is True, "Movie checkbox is not visible"
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True, "Voice checkbox is not visible"
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True, "Music checkbox is not visible"
        assert self.fc.fd["audio"].verify_strategy_checkbox_show() is True, "Strategy checkbox is not visible"
        assert self.fc.fd["audio"].verify_rpg_checkbox_show() is True, "RPG checkbox is not visible"
        assert self.fc.fd["audio"].verify_shooter_checkbox_show() is True, "Shooter checkbox is not visible"

        assert self.fc.fd["audio"].is_music_status_selected() == "1", "music option is not be selected"
        
        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "movie option is not be selected"
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "voice option is not be selected"
        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "music option is not be selected"

        self.fc.fd["audio"].click_strategy_checkbox()
        time.sleep(2)
        assert self.fc.fd["audio"].is_strategy_status_selected() == "1", "strategy option is not be selected"
        
        self.fc.fd["audio"].click_rpg_checkbox()
        time.sleep(2)
        assert self.fc.fd["audio"].is_rpg_status_selected() == "1", "rpg option is not be selected"
       
        self.fc.fd["audio"].click_shooter_checkbox()
        time.sleep(2)
        assert self.fc.fd["audio"].is_shooter_status_selected() == "1", "shooter option is not be selected"
        
        self.fc.fd["audio"].click_preset_music()

