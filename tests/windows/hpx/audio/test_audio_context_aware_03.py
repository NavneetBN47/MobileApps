
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
        cls.fc.launch_myHP()
        time.sleep(3)
        yield
        cls.fc.kill_calculator_process()


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_context_aware_support_all_platforms_C38644305(self):
        self.fc.restart_myHP()
        time.sleep(2)
        
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not present"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not present"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not present"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not present"
        assert bool(self.fc.fd["display_control"].verify_add_application_text()) is True, "Add application text is not present"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_check_add_application_C42612652(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        time.sleep(3)
        self.sf.close_myhp_app()


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_check_app_new_settings_and_global_icon_work_well_C43160413(self):
        self.fc.reset_myhp_app()
        time.sleep(4)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_speaker()
        assert bool(self.fc.fd["audio"].verify_context_aware_show()) is True, "Context aware is not present"
        time.sleep(2)

        self.fc.fd["audio"].click_add_application_btn()
        self.fc.fd["audio"].input_search_bar_on_application_page("calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_application_under_application_items()
        time.sleep(2)
        self.fc.fd["audio"].click_add_button_on_application_page()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        time.sleep(3)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.fd["audio"].click_preset_movie()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"

        self.sf.close_myhp_app()
        time.sleep(2)
        self.fc.fd["audio"].launch_common_apps("Calculator")
        time.sleep(2)
        self.fc.launch_myHP()
        time.sleep(4)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.kill_calculator_process()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        self.fc.fd["audio"].click_to_select_calculator_app()
        time.sleep(2)
        assert self.fc.fd["audio"].is_calculator_on_application_list_selected() == "2", "calculator app is not selected"
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"
        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        self.fc.fd["audio"].click_all_Application_icon()
        time.sleep(5)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"

        self.fc.fd["audio"].click_to_select_calculator_app()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        assert self.fc.fd["audio"].is_calculator_on_application_list_selected() == "2", "calculator app is not selected"
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"

        self.fc.fd["audio"].launch_common_apps("Calculator")
        time.sleep(4)
        self.fc.fd["audio"].click_myhp_on_task_bar()
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_calculator_app_show_on_application_list()) is True, "Calculator app is not present"
        assert self.fc.fd["audio"].is_calculator_on_application_list_selected() == "2", "calculator app is not selected"
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie status is not selected"

        assert bool(self.fc.fd["audio"].verify_all_application_icon_show()) is True, "All application icon is not show"
        self.fc.fd["audio"].click_all_Application_icon()
        time.sleep(5)
        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music status is not selected"
        self.fc.kill_calculator_process()