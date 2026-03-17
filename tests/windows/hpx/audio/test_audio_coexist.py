from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Coexist(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
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
        yield "uninstall audio standalone"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
        cls.fc.kill_chrome_process()
        time.sleep(2)
        cls.fc.uninstall_audio_standalone()
        time.sleep(2)

        
    def round_up(self,input_value):
        return round(float(input_value))

    # This suite is only supported on gidget because standalone notification is only visible on gidget
    # Need to put the HPAudioCenter standalone app build to the target machine path: C:\build\HPAudioCenter_1.51.339.0_x64.appxbundle_Windows10_PreinstallKit if want to run this cases
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_audio_module_not_show_standalone_installed_C32387060(self):
        time.sleep(4)
        self.fc.install_audio_standalone()
        time.sleep(4)
        self.sf.close_myhp_app()
        time.sleep(3)
        self.fc.launch_myHP() 

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon not visible"
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        
        assert bool(self.fc.fd["navigation_panel"].verify_pc_audio_show_on_PCdevice()) is True, "PC Audio not visible"
        
        self.fc.uninstall_audio_standalone()
        time.sleep(2)
        self.sf.close_myhp_app()
        time.sleep(3)
        self.fc.launch_myHP()
        time.sleep(3)
        
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon not visible"
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_audio_show_on_PCdevice()) is True,"PC Audio not visible"
        self.sf.close_myhp_app()
        
        
    @pytest.mark.ota
    def test_02_check_audio_experience_dialog_pop_up_C36262333(self):
        
        time.sleep(5)
        self.fc.install_audio_standalone()
        time.sleep(5)
        self.fc.fd["audio"].launch_standalone_app("HP Audio Center")
        time.sleep(8)
        assert bool(self.fc.fd["audio"].verify_standalone_app_header_show()) is True, "Standalone App header not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_one_show()) is True, "Standalone App contents one not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_two_title_show()) is True, "Standalone App contents two title not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_two_text1_show()) is True, "Standalone App contents two text1 not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_two_text2_show()) is True, "Standalone App contents two text2 not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_two_text3_show()) is True, "Standalone App contents two text3 not visible"
        assert bool(self.fc.fd["audio"].verify_open_myhp_show()) is True, "Open MyHP button not visible"
        assert bool(self.fc.fd["audio"].verify_not_now_show()) is True, "Not Now button not visible"
        time.sleep(3)
        
        self.fc.uninstall_audio_standalone()
        time.sleep(3)
        
        
    @pytest.mark.ota
    def test_03_check_not_now_button_C36262378(self):
        self.fc.install_audio_standalone()
        time.sleep(5)
        self.fc.fd["audio"].launch_standalone_app("HP Audio Center")
        time.sleep(5)
        assert bool(self.fc.fd["audio"].verify_standalone_app_header_show()) is True, "Standalone App header not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_one_show()) is True, "Standalone App contents one not visible"
        assert bool(self.fc.fd["audio"].verify_open_myhp_show()) is True, "Open MyHP button not visible"
        assert bool(self.fc.fd["audio"].verify_not_now_show()) is True, "Not Now button not visible"
        time.sleep(3)
        
        self.fc.fd["audio"].click_not_now_button()
        time.sleep(5)
        assert bool(self.fc.fd["audio"].verify_standalone_app_header_show()) is False, "Standalone App header still visible"
    
        self.fc.close_standalone_app()

        self.fc.fd["audio"].launch_standalone_app("HP Audio Center")
        time.sleep(5)
        assert bool(self.fc.fd["audio"].verify_standalone_app_header_show()) is True, "Standalone App header not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_one_show()) is True, "Standalone App contents one not visible"
        assert bool(self.fc.fd["audio"].verify_open_myhp_show()) is True, "Open MyHP button not visible"
        assert bool(self.fc.fd["audio"].verify_not_now_show()) is True, "Not Now button not visible"
        time.sleep(3)
        self.fc.close_standalone_app()
        self.fc.uninstall_audio_standalone()
    
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_click_open_myhp_on_standalone_app_dialog_verify_hpx_can_be_launched_C36262345(self):
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.install_audio_standalone()
        time.sleep(4)
        self.fc.fd["audio"].launch_standalone_app("HP Audio  Center")
        time.sleep(8)
        assert bool(self.fc.fd["audio"].verify_standalone_app_header_show()) is True, "Standalone App header not visible"
        assert bool(self.fc.fd["audio"].verify_standalone_app_contents_one_show()) is True, "Standalone App contents one not visible"
        assert bool(self.fc.fd["audio"].verify_open_myhp_show()) is True, "Open MyHP button not visible"
        assert bool(self.fc.fd["audio"].verify_not_now_show()) is True, "Not Now button not visible"
        self.fc.fd["audio"].click_to_open_my_hp_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        assert self.fc.fd["audio"].verify_output_title() is True, "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_icon() is True, "Output icon is not displayed"
        assert self.fc.fd["audio"].verify_input_icon() is True, "Input icon is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_show() is True, "Noise removal is not displayed"
        assert self.fc.fd["audio"].verify_noise_eduction_show() is True, "Noise reduction is not displayed"
        self.fc.fd["audio"].select_microphone_usb_audio_external_device()
        self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_mic_mode_text_show() is True, "Mic mode is not displayed"
        assert self.fc.fd["audio"].verify_conference_text_show() is True, "Conference is not displayed"
        assert self.fc.fd["audio"].verify_personal_text_show() is True, "Personal is not displayed"
        assert self.fc.fd["audio"].verify_voice_checkbox_show() is True, "Voice checkbox is not show"
        assert self.fc.fd["audio"].verify_music_checkbox_show() is True, "Music checkbox is not show"
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True, "Movie checkbox is not show"

        self.fc.close_myHP() 
        self.fc.uninstall_audio_standalone()

    def test_05_make_new_settings_on_both_myhp_and_standalone_app_check_audio_control_can_work_well_C36962580(self):
        time.sleep(5)
        self.fc.install_audio_standalone()
        time.sleep(2)
        self.fc.fd["audio"].launch_standalone_app("HP Audio Center")
        time.sleep(3)
        self.fc.fd["audio"].click_not_now_button()
        self.fc.fd["audio"].click_output_speaker_radio_button()
        self.fc.fd["audio"].set_slider_value_increase(100,"audio_control_speaker_volume_slider")
        output_value = self.fc.fd["audio"].get_slider_value("audio_control_speaker_volume_slider")
        assert "100"==output_value,"Volume not increased to 100"
        self.fc.fd["audio"].set_slider_value_decrease(10,"audio_control_speaker_volume_slider")
        output_value = self.fc.fd["audio"].get_slider_value("audio_control_speaker_volume_slider")
        assert "90"==output_value,"Volume not decreased to 90"

        self.fc.fd["audio"].set_slider_value_increase(100,"audio_control_input_microphone_array_volume_slider")
        input_value = self.fc.fd["audio"].get_slider_value("audio_control_input_microphone_array_volume_slider")
        assert "100"==input_value,"Volume not increased to 100"
        self.fc.fd["audio"].set_slider_value_decrease(10,"audio_control_input_microphone_array_volume_slider")
        input_value = self.fc.fd["audio"].get_slider_value("audio_control_input_microphone_array_volume_slider")
        assert "90"==input_value,"Volume not decreased to 90"
        self.fc.close_standalone_app()
        time.sleep(2)
        self.fc.launch_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)==90,"Volume not decreased to 90"
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert self.round_up(input_value)== 90,"Volume not decreased to 90" 
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value) == 90:
            self.fc.fd["audio"].set_slider_value_increase(5,"output_slider")
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)== 95,"Volume not increased to 95"
        if self.round_up(input_value)== 90:
            self.fc.fd["audio"].set_slider_value_decrease(5,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")    
        assert self.round_up(input_value)== 85,"Volume not decreased to 85"

        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].get_slider_value("input_slider") == "85", "volume is not 100"
        assert self.fc.fd["audio"].get_slider_value("output_slider") == "95", "volume is not 100"
        self.fc.close_myHP()

        self.fc.fd["audio"].launch_standalone_app("HP Audio Center")
        time.sleep(2)
        self.fc.fd["audio"].click_not_now_button()
        time.sleep(3)
           
        output_value = self.fc.fd["audio"].get_slider_value("audio_control_speaker_volume_slider")
        assert "95"==output_value,"Volume not increased to 95"
        input_value = self.fc.fd["audio"].get_slider_value("audio_control_input_microphone_array_volume_slider")
        assert "85"==input_value,"Volume not increased to 85"
        self.fc.fd["audio"].click_audio_control_restore_button()
        self.fc.uninstall_audio_standalone()