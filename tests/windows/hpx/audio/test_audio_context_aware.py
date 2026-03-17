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
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer 
    @pytest.mark.commercial  
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_audio_context_aware_ui_C37922042(self):
        time.sleep(2)
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        
        self.fc.fd["audio"].click_add_application_btn()
        time.sleep(2)
        
        assert bool(self.fc.fd["audio"].verify_application_page_header_pop_up()) is True, "Application page header is not show"
        assert bool(self.fc.fd["audio"].verify_search_bar_show()) is True, "Search bar is not show"
        assert bool(self.fc.fd["audio"].verify_application_page_list()) is True, "Application page list is not show"
        assert bool(self.fc.fd["audio"].verify_access_app_show()) is True, "Access app is not show"
        assert bool(self.fc.fd["audio"].verify_cancel_button_on_application_page_show()) is True, "Cancel button is not show"
        assert bool(self.fc.fd["audio"].verify_add_button_on_application_page_show()) is True, "Add button is not show"
        
        self.fc.fd["audio"].click_access_app_under_application_items()
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
        
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_delete_added_application_C38315504(self):
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        if bool(self.fc.fd["audio"].verify_access_app_show()) is False:
            self.fc.fd["audio"].click_add_application_btn()
            self.fc.fd["audio"].click_access_app_under_application_items()
            self.fc.fd["audio"].click_add_button_on_application_page()
            time.sleep(2)
            assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
            assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
            time.sleep(3)
        
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(2)
        self.fc.fd["audio"].verify_delete_btn_show_on_access_app()
        self.fc.fd["audio"].click_delete_btn_on_access_app()
        time.sleep(2)
        
        assert bool(self.fc.fd["audio"].verify_delete_page_header_show()) is True, "Delete page header is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_description_show()) is True, "Delete page description is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_cancel_btn_show()) is True, "Delete page cancel button is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_continue_btn_show()) is True, "Delete page continue button is not show"
        
        self.fc.fd["audio"].click_continue_btn_on_delete_page()
        
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is False, "Access app is still show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_03_check_hover_status_on_added_applications_C38315503(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        self.fc.fd["audio"].click_add_application_btn()
        
        self.fc.fd["audio"].click_access_app_under_application_items()
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        
        self.fc.fd["audio"].click_add_application_btn()
        
        self.fc.fd["audio"].click_calculator_app_under_application_items()
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
        
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(2)
        self.fc.fd["audio"].click_delete_btn_on_access_app()
        
        assert bool(self.fc.fd["audio"].verify_delete_page_header_show()) is True, "Delete page header is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_description_show()) is True, "Delete page description is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_cancel_btn_show()) is True, "Delete page cancel button is not show"
        assert bool(self.fc.fd["audio"].verify_delete_page_continue_btn_show()) is True, "Delete page continue button is not show"
        
        self.fc.fd["audio"].click_continue_btn_on_delete_page()
        
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is False, "Access app is still show on application list"
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
        
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_added_app_cannot_add_again_C38322394(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        self.fc.fd["audio"].click_add_application_btn()
       
        self.fc.fd["audio"].click_access_app_under_application_items()
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
       
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
       
        self.fc.fd["audio"].click_add_application_btn()
        time.sleep(2)
         
        self.fc.fd["audio"].click_access_app_under_application_items()
        assert bool(self.fc.fd["audio"].verify_add_button_enabled_on_application_page()) is False, "Add button is enabled"
        time.sleep(2)
       
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
       
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
       
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(2)
        self.fc.fd["audio"].click_delete_btn_on_access_app()
        self.fc.fd["audio"].click_continue_btn_on_delete_page()
       
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is False, "Access app is still show on application list"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        time.sleep(3)
    
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_05_check_search_function_C38315506(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].click_search_bar_on_application_page()
        
        
        self.fc.fd["audio"].input_search_bar_on_application_page("cal")
        time.sleep(2)
        self.fc.fd["audio"].click_calculator_app_under_application_items()
        
        assert bool(self.fc.fd["audio"].verify_calculator_app_under_application_items()) is True, "Calculator app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_calendar_app_under_application_items()) is True, "Calendar app is not show on application list"
        
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_calculator_app_under_application_items()
        
        assert bool(self.fc.fd["audio"].verify_calculator_app_under_application_items()) is True, "Calculator app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_calendar_app_under_application_items()) is False, "Calendar app is still show on application list"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_06_check_left_right_arrow_on_application_list_C38315501(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        
        application_list = ["Access", "Calculator", "Camera", "Clock", "Notepad"]
        
        for i in range(len(application_list)):
            self.fc.fd["audio"].click_add_application_btn()
            time.sleep(2)
            self.fc.fd["audio"].input_search_bar_on_application_page(application_list[i])
            time.sleep(2)
            self.fc.fd["audio"].click_application_under_application_items()
            time.sleep(2)
            self.fc.fd["audio"].click_add_button_on_application_page()
            time.sleep(2)
            
        assert bool(self.fc.fd["audio"].verify_left_arrow_on_application_list_show()) is True, "Left arrow is not show"
        self.fc.fd["audio"].click_left_arrow_on_application_list()
        assert bool(self.fc.fd["audio"].verify_right_arrow_on_application_list_show()) is True, "Right arrow is not show"
        self.fc.fd["audio"].click_right_arrow_on_application_list()
    
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_07_uninstaled_app_still_will_show_on_application_list_C38315505(self):
        self.fc.reset_myhp_app()
        
        self.fc.fd["audio"].search_hp_privacy_settings("HP Privacy Settings")
        if self.fc.fd["audio"].verify_hp_privacy_settings_exist_on_windows() is False:
            self.fc.install_hp_privacy_settings_app()
        
        self.fc.restart_myHP()
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        self.fc.fd["audio"].click_add_application_btn()
       
        self.fc.fd["audio"].input_search_bar_on_application_page("HP Privacy Settings")
        time.sleep(2)
       
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
       
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings app is not show on application list"
        
        self.fc.uninstall_hp_privacy_settings_app()
        
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings app is not show on application list"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_hp_privacy_settings_app_under_application_items()) is True, "HP Privacy Settings app is not show on application list"
        
  
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_08_check_apps_will_show_on_application_list_automatically_C38338778(self):
        self.fc.restart_myHP()
        time.sleep(2)
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not show"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"