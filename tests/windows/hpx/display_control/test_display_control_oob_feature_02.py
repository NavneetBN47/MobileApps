from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Display_control_oob_feature_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        region = "China"
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        time.sleep(5)
        #To install Disney+ app from MS store
        if region == "China":
            time.sleep(5)
            cls.fc.change_system_region_to_united_states()
        cls.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
        time.sleep(20)
        cls.fc.change_system_region_to_china()
        time.sleep(10)
        cls.fc.kill_msstore_process()
        time.sleep(15)
        cls.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
        time.sleep(15)
        cls.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
        time.sleep(15)
        cls.fc.kill_msstore_process()
        time.sleep(5)
        cls.fc.launch_myHP()
        yield "change_system_region_to_united_states"
        time.sleep(2)
        cls.fc.change_system_region_to_united_states()
        time.sleep(2)  

    #this suite should run on bopeep
    @pytest.mark.ota
    def test_01_restore_default_oob_settings_C38792930(self):
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        tencent_video=self.fc.fd["display_control"].verify_tencent_video_app()
        assert tencent_video == "腾讯视频","Tencent Video is not visible at Add Application"
        iqiyi=self.fc.fd["display_control"].verify_iqiyi_app()
        assert iqiyi == "爱奇艺","iqiyi is not visible at Add Application"
        disney_plus=self.fc.fd["display_control"].verify_disney_plus_app()
        assert disney_plus == "Disney+","Disney plus is not visible at Add Application" 
        time.sleep(5)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.fd["display_control"].click_restore_pop_up_windows_cancel_button()
        time.sleep(3)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.fd["display_control"].get_restore_pop_up_windows_cancel_text() == "Cancel","Cancel button is not visible"
        time.sleep(3)
        self.fc.fd["display_control"].click_restore_pop_up_do_not_show_checkbox()
        time.sleep(3)
        self.fc.fd["display_control"].click_continue_button_dialog()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(2)
        assert self.fc.fd["display_control"].verify_restore_factory_settings_continue() is False,"Restore Factory Settings is visible"
    
    @pytest.mark.ota
    def test_02_verify_oob_default_with_any_application_in_the_app_list_2_C38512455(self):
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        tencent_video=self.fc.fd["display_control"].verify_tencent_video_app()
        assert tencent_video == "腾讯视频","Tencent Video is not visible at Add Application"
        iqiyi=self.fc.fd["display_control"].verify_iqiyi_app()
        assert iqiyi == "爱奇艺","iqiyi is not visible at Add Application"
        disney_plus=self.fc.fd["display_control"].verify_disney_plus_app()
        assert disney_plus == "Disney+","Disney plus is not visible at Add Application" 
        time.sleep(5)
        self.fc.fd["display_control"].click_tencent_video_app()
        self.fc.fd["display_control"].click_restore_default_button()
        value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert value == "100","Brightness slider value is not 100"
        slider_value = int(self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider"))
        while slider_value != 55:
            decrement_amount = min(slider_value - 55, 10)
            self.fc.fd["display_control"].set_slider_value_decrease(decrement_amount,"Brightness_slider")
            slider_value = int(self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider"))
        tencent_video_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "55"==tencent_video_brightness_value,"Brightness not decreased to 55"   
        if  self.fc.fd["display_control"].verify_advanced_title_exist() != "Advanced":
            movie_mode =self.fc.fd["display_control"].verify_movie_mode_title()
            assert movie_mode == "Movie","Movie Mode is not visible"
            self.fc.fd["display_control"].verify_add_application_text()
            self.fc.fd["display_control"].click_add_application_btn()
            self.fc.fd["display_control"].search_application("Calculator")
            self.fc.fd["display_control"].click_to_select_calculator_app()
            self.fc.fd["display_control"].click_add_btn()
            self.fc.fd["display_control"].click_to_select_calculator_app()
            self.fc.fd["display_control"].verify_calculator_app() 
            self.fc.fd["display_control"].click_to_select_calculator_app()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "76","Brightness slider value different from default value"
            neutral_mode =self.fc.fd["display_control"].verify_natural_mode_title()
            assert neutral_mode == "Neutral","Neutral Mode is not selected by default"
        else:
            hdr_status =self.fc.fd["display_control"].get_hdr_button_status()
            assert hdr_status == "1","HDR Mode is not Enabled"  
            self.fc.fd["display_control"].click_to_select_calculator_app()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "90","Brightness slider value different from default value"
            default_mode =self.fc.fd["display_control"].verify_default_tile()
            assert default_mode == "Default"," Default Mode is not selected by default"
        time.sleep(10)   
        self.fc.fd["display_control"].click_restore_default_button()
        time.sleep(10) 
        self.fc.fd["display_control"].click_tencent_video_app()
        self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        self.fc.fd["display_control"].click_restore_default_button() 
        time.sleep(5)
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_to_delete_calculator_app()
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()
        time.sleep(5)
    
    @pytest.mark.ota
    def test_03_uninstall_tencent_video_application_from_the_device_C38512466(self):
        self.fc.uninstall_videos_app_from_ms_store("腾讯视频") 
        time.sleep(5)
        self.sf.click_start_btn_taskbar()
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert (self.fc.fd["display_control"].verify_tencent_video_app()) is False,"Tencent video app is not uninstalled from the device"
    

    @pytest.mark.ota
    def test_04_uninstall_iqiyi_video_application_from_the_device_C38512467(self):
        self.fc.uninstall_videos_app_from_ms_store("爱奇艺")
        time.sleep(5)
        self.sf.click_start_btn_taskbar()
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert (self.fc.fd["display_control"].verify_iqiyi_app()) is False,"IQIYI video app is not uninstalled from the Device"
        self.fc.close_myHP()         
        self.fc.uninstall_videos_app_from_ms_store("Disney+")
        time.sleep(5)   
        self.fc.close_myHP()         
        #To switch back to US region
        self.fc.change_system_region_to_united_states()
