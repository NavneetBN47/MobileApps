from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
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
        time.sleep(4)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    
    def round_up(self,output_value):
        return round(float(output_value))

    #doesnot support thompson only can run in any devices.
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_adjust_internal_speaker_input_volume_slider_max_verify_that_system_volume_is_adjusted_C31675698(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].select_microphone_usb_audio_external_device()
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert 100==self.round_up(input_value),"Volume is not increased 100%"
        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_sound()
        logging.info(f"Maximize {self.fc.fd['audio'].verify_system_settings_window_maximize()}")
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            logging.info(f"Maximize {self.fc.fd['audio'].verify_system_settings_window_maximize()}")
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
    
        self.fc.fd["audio"].search_text("windows_system_sound_more_sound_settings_tab")

        self.fc.fd["audio"].click_windows_system_sound_more_sound_settings_tab()
        self.fc.fd["audio"].click_system_sound_recording_tab()
        self.fc.fd["audio"].click_sound_microphone_array_tab()
        self.fc.fd["audio"].click_sound_microphone_array_properties_tab()
        self.fc.fd["audio"].click_sound_microphone_array_properties_levels_tab()

        value =self.fc.fd["audio"].set_system_sound_microphone_value_decrease(80)
        assert "20"==value,"Microphone volume not decreased to 20"
        self.sf.click_start_btn()
        self.sf.click_search_box()
        time.sleep(3)
        self.sf.enter_text_search_box()
        time.sleep(3)
        self.sf.click_on_open_tab_from_start_menu()

        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert 20==self.round_up(input_value),"Volume not decreased to 20"
        self.fc.fd["devices"].minimize_app()
        self.fc.fd["audio"].click_close_microphone_array_properties_window()
        self.fc.fd["audio"].click_close_sound_window()
        time.sleep(20)
        self.fc.close_windows_settings_panel()
        self.fc.close_myHP()


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_adjust_internal_microphone_input_volume_slider_verify_that_system_input_volume_is_adjusted_C31675831(self):
        self.fc.launch_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100-self.round_up(input_value),"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "100"==input_value,"Volume not increased to 100"

        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_sound()
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            logging.info(f"Maximize {self.fc.fd['audio'].verify_system_settings_window_maximize()}")
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        self.driver.swipe(direction="down", distance=3) 
        value=self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert self.round_up(value) == 100,"usb volume not in sync with system volume"
        self.fc.close_windows_settings_panel()
        self.fc.close_myHP()
 

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_remember_audio_levels_settings_even_relaunch_app_or_switch_back_from_other_module_C33605329(self):
        self.fc.launch_myHP()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)== 100,"Volumn not increased to 100"
        if self.round_up(output_value)!=50:
            self.fc.fd["audio"].set_slider_value_decrease(50,"output_slider")
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")    
        assert self.round_up(output_value)== 50,"Volumn not decreased to 50" 

        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100: 
            self.fc.fd["audio"].set_slider_value_increase(100,"input_slider")
        time.sleep(5)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert self.round_up(input_value)== 100,"Volumn not increased to 100"
        if self.round_up(input_value)!=50:
            self.fc.fd["audio"].set_slider_value_decrease(50,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")    
        assert self.round_up(input_value)== 50,"Volumn not decreased to 50"

        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert self.round_up(input_value)== 50,"Input Slider value is not matching"
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)== 50,"Output Slider value is not matching"
        #relaunch app and verify input/output slider value
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert self.round_up(input_value)== 50,"Input Slider value is not matching"
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)== 50,"Output Slider value is not matching"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_check_audio_control_even_relaunch_multiple_times_C41369968(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(5)

        for i in range(5):
            self.fc.launch_myHP_to_audio_control_page()
            self.fc.fd["audio"].select_microphone_usb_audio_external_device()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_output_title() is True, "Output title is not displayed"
            assert self.fc.fd["audio"].verify_output_icon() is True, "Output icon is not displayed"
            assert self.fc.fd["audio"].verify_input_icon() is True, "Input icon is not displayed"
            assert self.fc.fd["audio"].verify_noise_removal_show() is True, "Noise removal is not displayed"
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
            assert self.fc.fd["audio"].verify_noise_eduction_show() is True, "Noise reduction is not displayed"
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
            assert self.fc.fd["audio"].verify_mic_mode_text_show() is True, "Mic mode is not displayed"
            assert self.fc.fd["audio"].verify_conference_text_show() is True, "Conference is not displayed"
            assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not selected"
            assert self.fc.fd["audio"].verify_personal_text_show() is True, "Personal is not displayed"
            assert self.fc.fd["audio"].verify_presets_text_show() is True, "Presets is not displayed"
            assert self.fc.fd["audio"].verify_presets_tooltips_btn_show() is True, "Presets tooltips is not displayed"
            assert self.fc.fd["audio"].verify_voice_checkbox_show() is True, "Voice checkbox is not displayed"
            assert self.fc.fd["audio"].verify_music_checkbox_show() is True, "Music checkbox is not displayed"
            assert self.fc.fd["audio"].verify_movie_checkbox_show() is True, "Movie checkbox is not displayed"
            self.driver.swipe(direction="down", distance=4)
            time.sleep(5)
            assert self.fc.fd["audio"].verify_equalizer_text_show() is True, "Equalizer text is not visible"
            assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show() is True, "Equalizer tooltip not visible"
            assert self.fc.fd["audio"].verify_equalizer_slider_volume_show() is True, "Equalizer slider 32 not visible"
            assert bool(self.fc.fd["audio"].verify_restore_defaults_button_show()) is True, "Restore defaults button not visible"
            self.driver.swipe(direction="up", distance=4)
            time.sleep(5)
            self.fc.close_myHP()
            time.sleep(5)

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_adjust_internal_speaker_output_volume_slider_verify_that_system_volume_is_adjusted_C31675808(self):
        self.fc.launch_myHP()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(5)
        
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert self.fc.fd["audio"].get_system_volume() == "100", "System volume is not 100"
        self.fc.fd["audio"].click_windows_speaker_icon()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=50:
            self.fc.fd["audio"].set_slider_value_decrease(50,"output_slider")

        self.fc.fd["audio"].click_windows_speaker_icon()
        assert self.fc.fd["audio"].get_system_volume() == "50", "System volume is not 50"
        self.fc.fd["audio"].click_windows_speaker_icon()
        