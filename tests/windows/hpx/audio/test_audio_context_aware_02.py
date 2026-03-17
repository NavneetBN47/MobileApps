from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Auido_Context_Aware(object):
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
            time.sleep(3)
        yield "install hp privacy settings"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
        cls.fc.install_hp_privacy_settings_app()
        cls.fc.kill_disney_video_process()
        cls.fc.kill_tencent_video_process()
        cls.fc.kill_iqiyi_video_process()
        cls.fc.kill_calculator_process()
        time.sleep(2)
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_Music_option_will_be_selected_even_we_relaunch_myhp_C38481141(self):
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_output_device_speaker()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar() 
        time.sleep(3)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.kill_iqiyi_video_process()
        
        self.fc.restart_myHP()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_all_application_icon()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.sf.close_myhp_app()
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_check_uninstalled_app_will_not_show_on_application_page_C39805450(self):
        self.fc.reset_myhp_app()
        self.fc.fd["audio"].search_hp_privacy_settings("HP Privacy Settings")
        if self.fc.fd["audio"].verify_hp_privacy_settings_exist_on_windows() is True:
            self.fc.uninstall_hp_privacy_settings_app()
        time.sleep(3)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        self.fc.fd["audio"].click_add_application_btn()
       
        self.fc.fd["audio"].input_search_bar_on_application_page("HP Privacy Settings")
        time.sleep(2)
       
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_page()) is True, "HP Privacy Settings is not present"
        time.sleep(2)
        self.fc.fd["audio"].click_cancel_button_on_application_page()
        self.sf.close_myhp_app()
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_check_applications_will_sync_between_with_audio_control_and_display_control_C38645719(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        
        self.fc.fd["display_control"].verify_add_application_text()
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("Calculator")
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_add_btn()
        self.fc.fd["display_control"].click_to_select_calculator_app()
        calculator_app=self.fc.fd["display_control"].verify_calculator_app()
        assert calculator_app == "Calculator","Calculator is not visible at Add Application"
        
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        
        self.fc.fd["audio"].search_hp_privacy_settings("HP Privacy Settings")
        if self.fc.fd["audio"].verify_hp_privacy_settings_exist_on_windows() is False:
            self.fc.install_hp_privacy_settings_app()
        
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("HP Privacy Settings")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
       
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings is not present"
        
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings is not present"
        
        self.fc.fd["display_control"].click_to_select_calculator_app()
        time.sleep(2)
        self.fc.fd["display_control"].click_to_delete_calculator_app()
        time.sleep(5)
        self.fc.fd["audio"].click_continue_btn_on_delete_page()
        time.sleep(5)
        
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is False, "Calculator app is present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings is not present"
        
        
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is False, "Calculator app is present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings is not present"
        self.sf.close_myhp_app()
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_check_Presets_option_will_not_change_when_using_common_apps_not_on_application_list_C38322282(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        self.fc.swipe_window(direction="down", distance=3)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar() 
        time.sleep(3)
        if not self.fc.fd["audio"].verify_movie_preset():
            self.fc.fd["audio"].click_myhp_on_task_bar()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.swipe_window(direction="up", distance=3)
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        time.sleep(3)
        self.fc.fd["audio"].click_to_select_calculator_app()
        time.sleep(3)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.fd["audio"].launch_common_apps("Calculator")
        self.fc.fd["audio"].click_myhp_on_task_bar()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        time.sleep(2)
        
        self.fc.close_calculator_app()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.kill_iqiyi_video_process()
        time.sleep(4)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.fd["audio"].launch_common_apps("Calculator")
        self.fc.fd["audio"].click_myhp_on_task_bar()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.fc.close_calculator_app()
        self.sf.close_myhp_app()
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_05_check_music_will_be_selected_when_using_added_common_apps_C39815918(self):
        self.fc.reset_myhp_app() 
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        self.fc.fd["audio"].click_output_device_speaker()
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        
        self.fc.fd["display_control"].click_to_select_calculator_app()
        time.sleep(3)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.reset_myhp_app()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devices"].maximize_app()
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        
        self.fc.fd["audio"].click_preset_movie()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        self.fc.fd["audio"].launch_common_apps("Calculator")
        time.sleep(5)
        
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.close_calculator_app()
        self.sf.close_myhp_app()
        
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_06_check_any_new_settings_for_IMAX_apps_can_be_remembered_C37924600(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].click_tencent_app_on_application_list()
        time.sleep(5)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1" , "Movie status is not selected"
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.fd["audio"].click_all_application_icon()
        time.sleep(5)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.fd["audio"].click_tencent_app_on_application_list()
        time.sleep(5)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.fc.fd["audio"].click_all_application_icon()
        time.sleep(5)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("腾讯视频")
        self.fc.fd["audio"].click_tencent_on_task_bar()
        time.sleep(5)
        
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.kill_tencent_video_process()
        self.sf.close_myhp_app()