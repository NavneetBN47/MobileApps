from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Auido_Restore_Defaults(object):
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
            time.sleep(5)
            cls.fc.launch_myHP()
            time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()  
    
    #external device name different than anyother devices and not all devices are connected to usb and 3.5 headphone. 
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_restore_defaults_ui_and_its_basic_functions_work_well_for_common_audio_settings_restore_C41043013(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        if(self.fc.fd["audio"].verify_headphones_plugin_pc_arti() == True):
            self.fc.fd["audio"].click_headphones_realtek_arti()
        #if output device start with speaker
        if(self.fc.fd["audio"].verify_speaker_on_device() == True):
            self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(2)
        #added this steps code coz restore popup has different msg as selection of app in context aware
        self.fc.fd["audio"].click_all_application_icon()
        self.fc.swipe_window(direction="down", distance=5)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()
        time.sleep(2)
        self.fc.fd["audio"].click_cancel_button_on_restore_defaults_dialog()
        time.sleep(2)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"     
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(3)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice preset is not selected"
        self.fc.fd["audio"].click_restore_button()
        time.sleep(2)
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice preset is not selected"
        self.fc.fd["audio"].click_restore_button()
        time.sleep(8)
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].click_restore_defaults_content_2_checkbox()
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        time.sleep(8)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice preset is not selected"
        self.fc.fd["audio"].click_restore_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_restore_defaults_header_show()) is False, "Restore default header is visible"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()) is False, "Restore default cancel button is visible"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_restore_defaults_works_well_with_external_device_C41043085(self):
        self.fc.reset_myhp_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["devices"].maximize_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_rpg_checkbox()
        time.sleep(2)
        assert self.fc.fd["audio"].is_rpg_status_selected() == "1", "rpg preset is not selected"
        self.fc.fd["audio"].click_restore_button()
        time.sleep(2)
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"
        time.sleep(2)


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_check_audio_control_will_work_well_after_click_Restore_Defaults_button_C41043086(self):
        self.fc.reset_myhp_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
             self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["devices"].maximize_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(3)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice preset is not selected"
        self.fc.fd["audio"].click_restore_button()
        time.sleep(2)
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music preset is not selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_check_Restore_defaults_confirmation_dialog_will_work_with_hp_factory_app_settings_well_C41552184(self):
        self.fc.reset_myhp_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["devices"].maximize_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not visible"
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar() 
        time.sleep(3)
        
        self.driver.swipe(direction="down", distance=3)
        time.sleep(5)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        selected_apps = self.fc.fd["audio"].get_restore_defaults_content_1_txt()
        assert selected_apps == "Restore the selected application settings to the default configuration?"
        time.sleep(2)
        self.fc.fd["audio"].click_cancel_button_on_restore_defaults_dialog()
        time.sleep(2)

        self.driver.swipe(direction="up", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_all_Application_icon()
        time.sleep(3)
        self.driver.swipe(direction="down", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        time.sleep(5)
        hp_factory = self.fc.fd["audio"].get_restore_defaults_content_1_txt()
        assert  hp_factory == "Restore the settings to the HP factory defaults?"
        time.sleep(2)
        self.fc.fd["audio"].click_cancel_button_on_restore_defaults_dialog()
        time.sleep(2)

        self.fc.kill_iqiyi_video_process()

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_05_check_restore_defaults_ui_and_basic_functions_C40600912(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        
        self.fc.swipe_window(direction="down", distance=5)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()
        self.fc.fd["audio"].verify_restore_defaults_x_button_show()
        time.sleep(3)
        
        self.fc.fd["audio"].click_cancel_button_on_restore_defaults_dialog()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_restore_defaults_header_show()) is False, "Restore defaults header is present"
        
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()
        self.fc.fd["audio"].verify_restore_defaults_x_button_show()
        time.sleep(3)
        
        self.fc.fd["audio"].click_x_button_on_restore_defaults_dialog()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_restore_defaults_header_show()) is False, "Restore defaults header is present"
        
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()
        self.fc.fd["audio"].verify_restore_defaults_x_button_show()
        time.sleep(3)
        
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_restore_defaults_header_show()) is False, "Restore defaults header is present"
        
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].verify_restore_defaults_header_show()
        self.fc.fd["audio"].verify_restore_defaults_content_1_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_show()
        self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()
        self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()
        self.fc.fd["audio"].verify_restore_defaults_x_button_show()
        time.sleep(3)
        
        self.fc.fd["audio"].click_restore_defaults_content_2_checkbox()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        
        assert bool(self.fc.fd["audio"].verify_restore_defaults_header_show()) is False, "Restore defaults header is present"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_content_1_show()) is False, "Restore defaults content 1 is present"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_content_2_show()) is False, "Restore defaults content 2 is present"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_content_2_checkbox_show()) is False, "Restore defaults content 2 checkbox is present"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_cancel_button_show()) is False, "Restore defaults cancel button is present"
        assert bool(self.fc.fd["audio"].verify_restore_defaults_x_button_show()) is False, "Restore defaults x button is present"