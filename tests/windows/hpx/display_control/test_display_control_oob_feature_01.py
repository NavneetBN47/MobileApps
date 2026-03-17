from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Display_control_oob_feature(object):
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
    def test_01_verify_oob_default_restore_for_video_app_C38512456(self):
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
        self.fc.fd["display_control"].click_tencent_video_app() 
        time.sleep(7)
        self.fc.get_app_brightness_value()
        self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
  
        if  self.fc.fd["display_control"].verify_advanced_title_exist() != "Advanced":
            movie_mode =self.fc.fd["display_control"].verify_movie_mode_title()
            assert movie_mode == "Movie","Movie Mode is not visible" 
            self.fc.fd["display_control"].click_night_mode() 
            night_mode = self.fc.fd["display_control"].verify_night_mode_title()
            assert night_mode == "Night","Night Mode is not visible" 
        else:
            hdr_status =self.fc.fd["display_control"].get_hdr_button_status()
            assert hdr_status == "1","HDR Mode is not Enabled" 
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "100","Brightness slider value is not 100"
            self.fc.fd["display_control"].set_slider_value_decrease(45,"Brightness_slider")
            tencent_video_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert "55"==tencent_video_brightness_value,"Brightness not decreased to 55"   
        self.fc.fd["display_control"].click_tencent_video_app()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()     
        time.sleep(5)      
        if  self.fc.fd["display_control"].verify_advanced_title_exist() != "Advanced":
            movie_mode =self.fc.fd["display_control"].verify_movie_mode_title()
            assert movie_mode == "Movie","Movie Mode is not visible"
        else:
            hdr_status =self.fc.fd["display_control"].get_hdr_button_status()
            assert hdr_status == "1","HDR Mode is not Enabled" 
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "100","Brightness slider value is not 100"   

    @pytest.mark.ota
    def test_02_verify_oob_default_restore_for_global_app_C38512457(self):
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
        self.fc.fd["display_control"].click_global_app_icon()
        self.fc.fd["display_control"].click_native_tile()
        self.fc.fd["display_control"].set_slider_value_decrease(45,"Brightness_slider")
        self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].click_global_app_icon()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        time.sleep(5)
        if  self.fc.fd["display_control"].verify_advanced_title_exist() != "Advanced":
            movie_mode =self.fc.fd["display_control"].verify_movie_mode_title()
            assert movie_mode == "Movie","Movie Mode is not visible"
            self.fc.fd["display_control"].click_global_app_icon()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "76","Brightness slider value different from default value"
            neutral_mode =self.fc.fd["display_control"].verify_natural_mode_title()
            assert neutral_mode == "Neutral","Neutral Mode is not selected by default"
        else:
            hdr_status =self.fc.fd["display_control"].get_hdr_button_status()
            assert hdr_status == "1","HDR Mode is not Enabled"  
            self.fc.fd["display_control"].click_global_app_icon()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "90","Brightness slider value different from default value"
            default_mode =self.fc.fd["display_control"].verify_default_tile()        

    @pytest.mark.ota
    def test_03_verify_oob_default_restore_for_custom_app_C38512458(self):
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
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("Calculator")
        self.fc.fd["display_control"].click_to_select_calculator_app()
        time.sleep(5)
        self.fc.fd["display_control"].click_add_btn()
        self.fc.fd["display_control"].click_to_select_calculator_app()
        calculator_app=self.fc.fd["display_control"].verify_calculator_app()
        assert calculator_app == "Calculator","Calculator is not visible at Add Application"
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_native_tile()
        self.fc.fd["display_control"].set_slider_value_decrease(45,"Brightness_slider")
        self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        time.sleep(7)
        if  self.fc.fd["display_control"].verify_advanced_title_exist() != "Advanced":
            movie_mode =self.fc.fd["display_control"].verify_movie_mode_title()
            assert movie_mode == "Movie","Movie Mode is not visible"
            self.fc.fd["display_control"].click_global_app_icon()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "76","Brightness slider value different from default value"
            neutral_mode =self.fc.fd["display_control"].verify_natural_mode_title()
            assert neutral_mode == "Neutral","Neutral Mode is not selected by default"
        else:
            hdr_status =self.fc.fd["display_control"].get_hdr_button_status()
            assert hdr_status == "1","HDR Mode is not Enabled"  
            self.fc.fd["display_control"].click_global_app_icon()                    
            value =self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
            assert value == "90","Brightness slider value different from default value"
            default_mode =self.fc.fd["display_control"].verify_default_tile() 
            assert default_mode == "Default"," Default Mode is not selected by default"
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_to_delete_calculator_app() 
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()  

        
    @pytest.mark.ota
    def test_04_deleting_oob_disney_plus_app_from_app_settings_C38512459(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        disney_plus=self.fc.fd["display_control"].verify_disney_plus_app()
        assert disney_plus == "Disney+","Disney plus is not visible at Add Application" 
        self.fc.fd["display_control"].click_disney_plus_app() 
        self.fc.fd["display_control"].click_to_delete_disney_plus_app()
        time.sleep(3)
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        # if self.fc.fd["display_control"].verify_disney_plus_app() is False:
        assert (self.fc.fd["display_control"].verify_disney_plus_app()) is False,"Disney Plus app is not deleted from the list"
       

    @pytest.mark.ota
    def test_05_deleting_oob_tencent_video_app_from_aap_settings_C38512460(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        tencent_video=self.fc.fd["display_control"].verify_tencent_video_app()
        assert tencent_video == "腾讯视频","Tencent Video is not visible at Add Application"
        self.fc.fd["display_control"].click_tencent_video_app()
        self.fc.fd["display_control"].click_to_delete_tencent_video_app()
        time.sleep(3)
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert (self.fc.fd["display_control"].verify_tencent_video_app()) is False,"Tencent video app is not deleted from the list"
        


    @pytest.mark.ota
    def test_06_deleting_oob_iqiyi_video_app_from_aap_settings_C38512461(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        iqiyi=self.fc.fd["display_control"].verify_iqiyi_app()
        assert iqiyi == "爱奇艺","iqiyi is not visible at Add Application"
        self.fc.fd["display_control"].click_iqiyi_app()
        self.fc.fd["display_control"].click_to_delete_iqiyi_video_app()
        time.sleep(3)
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert (self.fc.fd["display_control"].verify_iqiyi_app()) is False,"IQIYI video app is not deleted from the list"
   

    @pytest.mark.ota
    def test_07_add_disney_plus_application_in_the_app_list_C38512462(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("Disney+")
        time.sleep(5)
        self.fc.fd["display_control"].click_disney_plus_app()
        time.sleep(15)
        self.fc.fd["display_control"].click_add_btn()
        time.sleep(5)
        self.fc.fd["display_control"].click_disney_plus_app()
        disney_plus_app=self.fc.fd["display_control"].verify_disney_plus_app()
        assert disney_plus_app == "Disney+","Disney+ is not visible at Add Application"



    @pytest.mark.ota
    def test_08_add_tencent_video_application_in_the_app_list_C38512464(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("腾讯视频")
        time.sleep(5)
        self.fc.fd["display_control"].click_tencent_video_app()
        time.sleep(15)
        self.fc.fd["display_control"].click_add_btn()
        self.fc.fd["display_control"].click_tencent_video_app()
        time.sleep(5)
        tencent_app=self.fc.fd["display_control"].verify_tencent_video_app()
        assert tencent_app == "腾讯视频","tencent_app is not visible at Add Application"


    @pytest.mark.ota
    def test_09_add_iqiyi_application_in_the_app_list_C38512463(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].verify_add_application_text()
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("爱奇艺")
        time.sleep(10)
        self.fc.fd["display_control"].click_iqiyi_app()
        time.sleep(15)
        self.fc.fd["display_control"].click_add_btn()
        time.sleep(5)
        self.fc.fd["display_control"].click_iqiyi_app()
        time.sleep(5)
        iqiyi_app=self.fc.fd["display_control"].verify_iqiyi_app()
        assert iqiyi_app == "爱奇艺","IQIYI  is not visible at Add Application"


    @pytest.mark.ota
    def test_10_uninstall_disney_plus_application_from_the_device_C38512465(self):
        self.fc.uninstall_videos_app_from_ms_store("Disney+")
        time.sleep(5)
        self.sf.click_start_btn_taskbar()
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert (self.fc.fd["display_control"].verify_disney_plus_app()) is False,"Disney Plus app is not unistalled from the Device"
        self.fc.uninstall_videos_app_from_ms_store("爱奇艺") 
        time.sleep(5)
        self.fc.uninstall_videos_app_from_ms_store("腾讯视频")
        time.sleep(5)   
        self.fc.close_myHP()  
        #To switch back to US region
        self.fc.change_system_region_to_united_states()           