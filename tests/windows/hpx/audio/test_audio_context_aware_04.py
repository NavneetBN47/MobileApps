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
    def test_01_check_any_new_settings_for_non_IMAX_apps_can_be_remembered_C40528902(self):
        self.fc.reset_myhp_app()
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
        
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(3)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("Disney+")
        time.sleep(5)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["audio"].click_disney_plus_on_application_list()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.kill_disney_video_process()
        time.sleep(3)
        self.fc.fd["audio"].launch_common_apps("Calculator")
        time.sleep(5)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(2)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"

        time.sleep(2)
        self.fc.close_calculator_app()
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_check_any_new_settings_for_added_apps_can_be_remembered_C40670278(self):
        self.fc.reset_myhp_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        if self.fc.fd["audio"].verify_calculator_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_btn()
            self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
            time.sleep(2)
            self.fc.fd["audio"].click_application_under_application_items()
            time.sleep(2)
            self.fc.fd["audio"].click_add_button_on_application_page()
            time.sleep(2)
            assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        self.fc.fd["audio"].click_aiqiyi_app_on_application_list()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        
        self.fc.fd["audio"].click_to_select_calculator_app()
        time.sleep(3)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.fd["audio"].click_preset_movie()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar()
        time.sleep(3)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.fc.kill_iqiyi_video_process()
        time.sleep(2)
        self.fc.fd["audio"].launch_common_apps("Calculator")
        time.sleep(3)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(2)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.close_calculator_app()
        self.fc.fd["audio"].click_aiqiyi_app_on_application_list()
        time.sleep(5)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        time.sleep(2)
        self.sf.close_myhp_app()
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_03_check_restore_defaults_button_just_works_with_selected_app_C38322283(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True,"Tencent app is not present"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        time.sleep(3)
        
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar()
        if not self.fc.fd["audio"].verify_movie_preset():
            self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(3)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(3)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.fc.kill_iqiyi_video_process()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(8)
        self.fc.swipe_window(direction="up", distance=2)
        time.sleep(2)
        self.fc.fd["audio"].click_aiqiyi_app_on_application_list()
        time.sleep(5)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.fd["audio"].verify_calculator_app_show_on_application_list()
        self.fc.fd["audio"].click_to_select_calculator_app()
        time.sleep(5)
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.sf.close_myhp_app()

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_check_preset_option_switch_from_movie_to_music_when_click_global_application_icon_C39540512(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_output_device_speaker()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        time.sleep(2)
        self.fc.fd["audio"].click_disney_plus_on_application_list()
        time.sleep(5)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        self.fc.fd["audio"].click_all_Application_icon()
        time.sleep(5)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.sf.close_myhp_app()

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_05_check_preset_option_will_switch_to_Movie_when_we_are_using_IMAX_apps_C38338916(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_output_device_speaker()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        
        self.fc.fd["audio"].launch_IMAX_apps("爱奇艺")
        time.sleep(5)
        self.fc.fd["audio"].click_aiqiyi_on_task_bar() 
        time.sleep(3)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.kill_iqiyi_video_process()
        self.fc.fd["audio"].click_preset_music()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.fd["audio"].launch_IMAX_apps("腾讯视频")
        time.sleep(5)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(3)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.kill_tencent_video_process()
        time.sleep(3)
        self.fc.fd["audio"].click_preset_voice()
        assert self.fc.fd["audio"].is_voice_status_selected() == "1", "Voice status is not selected"
        self.fc.fd["audio"].launch_IMAX_apps("Disney+")
        time.sleep(5)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(5)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        self.fc.kill_disney_video_process()
        self.fc.fd["audio"].click_preset_music()
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"