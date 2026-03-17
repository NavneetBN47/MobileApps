from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Auido_Studio_Recording(object):
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
            cls.fc.launch_app()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

            
    # suite only supported on bopeep thompson and arti   
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_audio_studio_recording_support_machine_C37640785(self):
        time.sleep(2)
        self.fc.restart_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        assert bool(self.fc.fd["audio"].verify_studio_recording_show()) is True, "Studio Recording is not show"

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_audio_studio_recording_ui_C37638106(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is True, "Studio Recording is not show"
        assert self.fc.fd["audio"].get_studio_recording_text() == "Studio Recording", "Studio Recording text is not show"
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_noise_reduction_disable_studio_recording_selected_C38000663(self):
        time.sleep(2)
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference checkbox is not selected"
        
        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is True, "Studio Recording is not show"
        assert self.fc.fd["audio"].get_studio_recording_text() == "Studio Recording", "Studio Recording text is not show"
        
        self.fc.fd["audio"].click_studio_recording_btn()
        assert self.fc.fd["audio"].is_studio_recording_btn_selected() == "1", "Studio Recording button is not selected"
        
        if not self.fc.fd["audio"].check_noise_reduction_btn_status():
            print("Noise Reduction is disabled")
            
        self.fc.fd["audio"].click_conference_checkbox()
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference checkbox is not selected"
        
        self.fc.fd["audio"].check_noise_reduction_btn_status()
        time.sleep(2)
        
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_studio_recording_mode_just_support_internal_mic_C37638204(self):
        time.sleep(2)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_headphone_plugin_pc()
        assert self.fc.fd["audio"].is_headphone_plugin_pc_selected() == "2", "Headphone Plugin PC is not selected"

        if self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            assert self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() == "2", "Internal Speaker is not selected"

        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is True, "Studio Recording is not show"

        self.fc.fd["audio"].click_headset_output_for_mm()
        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is False, "Studio Recording is show"
        self.fc.fd["audio"].click_headset_usb_input()
        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is False, "Studio Recording is show"
        self.fc.fd["audio"].click_input_mic_icon_input_device()
        assert bool(self.fc.fd["audio"].verify_studio_recording_checkbox_show()) is False, "Studio Recording is show"

        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        assert self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() == "2", "Internal Speaker is not selected"
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_check_studio_recording_mode_will_be_remembered_even_i_relaunch_myhp_C39040941(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_microphone_array_in_all_devices()
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction is not enabled"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference checkbox is not selected"
        self.fc.fd["audio"].click_studio_recording_btn()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert self.fc.fd["audio"].is_studio_recording_btn_selected() == "1", "Studio Recording button is not selected"
        self.fc.close_app()
        time.sleep(2)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_studio_recording_btn_selected() == "1", "Studio Recording button is not selected"
        
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_restore_defaults_works_well_with_studio_recording_mode_C40530634(self):
        self.fc.re_install_app_and_skip_fuf(self.driver.session_data["installer_path"])
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_microphone_array_in_all_devices()
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction is not enabled"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference checkbox is not selected"
        self.fc.fd["audio"].click_studio_recording_btn()
        assert self.fc.fd["audio"].is_studio_recording_btn_selected() == "1", "Studio Recording button is not selected"
        
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["audio"].click_restore_button() 
        self.fc.fd["audio"].click_continue_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=3)
        assert self.fc.fd["audio"].is_studio_recording_btn_selected() == "0", "Studio Recording button is not selected"
        self.fc.close_app()