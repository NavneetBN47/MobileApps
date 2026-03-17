import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
import pytest
import os,sys
import shutil
import logging
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "HPX"
class Test_Suite_Performance(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        cls.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        cls.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/properties.json"),cls.remote_artifact_path+"properties.json")    
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.st = time.time()

    def test_01_second_launch_app_online_verify_the_launch_time_is_less_than_2_seconds_C32016317(self):
        control_pc_text = self.fc.fd["home"].verify_control_your_pc()
        assert control_pc_text=="Control your PC","Control Your Pc text not visible"
        self.et = time.time()
        # get the execution time
        elapsed_time = self.et - self.st
        print('Execution time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"

    def test_02_verify_less_than_2_seconds_upon_clicking_home_panel_from_detail_panel_C32016319_1(self):
        self.st = time.time()  
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        home_Menu_text = self.fc.fd["navigation_panel"].verify_home_menu_navigation()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Home Menu panel open time', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Home"==home_Menu_text,"Home menu is not visible"

    def test_03_verify_less_than_2_seconds_upon_clicking_power_manager_panel_from_detail_panel_C32016319_2(self):
        power_Manager_text = self.fc.fd["navigation_panel"].verify_powermanager_menu_navigation()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Power Manager Menu panel open time', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Power Manager"==power_Manager_text,"Power Manager menu is not visible"

    def test_04_verify_less_than_2_seconds_upon_clicking_devices_panel_from_detail_panel_C32016319_3(self):
        self.st = time.time() 
        devices_Menu_text = self.fc.fd["navigation_panel"].verify_devices_menu_navigation()
        self.et = time.time()
        print('Devices panel open time:', elapsed_time, 'seconds')
        elapsed_time = self.et - self.st
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Devices"==devices_Menu_text,"Devices menu is not visible"

    def test_05_verify_less_than_2_seconds_upon_clicking_support_panel_from_detail_panel_C32016319_4(self):    
        self.st = time.time() 
        support_Menu_text = self.fc.fd["navigation_panel"].verify_support_menu_navigation()
        self.et = time.time()
        print('Support Panel opn time:', elapsed_time, 'seconds')
        elapsed_time = self.et - self.st
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Support"==support_Menu_text,"Support menu is not visible"

    def test_06_verify_less_than_2_seconds_upon_clicking_settings_panel_from_detail_panel_C32016319_5(self):   
        self.st = time.time() 
        settings_Menu_text = self.fc.fd["navigation_panel"].verify_settings_menu_navigation()
        self.et = time.time()
        print('Setting panel open time:', elapsed_time, 'seconds')
        elapsed_time = self.et - self.st
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Settings"==settings_Menu_text,"Settings menu is not visible"

    def test_07_click_pc_device_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_1(self):
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('PC Device open time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "PC Device"==pc_Device_Menu_text,"PC Device menu is not visible"

    @pytest.mark.require_platform(["grogu"])
    def test_08_click_pen_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_2(self):
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        pen_control_submenu_text = self.fc.fd["devices"].verify_pen_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Pen Control open time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert "Pen Control"==pen_control_submenu_text,"Pen Control submenu is not visible"

    def test_09_verify_audio_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_3(self):
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Audio Control time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert audio_control_text=="Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)

    def test_10_click_audio_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_4(self):
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_devices()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Audio Control time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert audio_control_text=="Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)

    def test_11_verify_video_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_5(self):
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        video_control_text = self.fc.fd["devices"].verify_video_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Video Control time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert video_control_text=="Video control","Video Control is not visible at PC Device - {}".format(video_control_text)

    def test_12_click_video_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_6(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_video_control()
        self.fc.fd["devices"].click_pc_devices()
        Video_control_text = self.fc.fd["home"].verify_video_control()
        self.fc.fd["devices"].close_hp_video_app()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Video Control time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert Video_control_text=="Video control","Video Control is not visible at PC Device - {}".format(video_control_text)
        
    def test_13_verify_RGB_keyboard_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_7(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        rgb_keyword_text = self.fc.fd["devices"].verify_rgb_keyword()        
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('RGB Keyboard time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert rgb_keyword_text=="RGB keyboard","RGB keyboard is not visible at PC Device - {}".format(rgb_keyword_text)
    
    def test_14_click_RGB_keyboard_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_8(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_rgb_keyword()
        self.fc.fd["devices"].click_pc_devices()
        rgb_keyword_text = self.fc.fd["devices"].verify_rgb_keyword()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('RGB Keyword time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert rgb_keyword_text=="RGB keyboard","RGB keyboard is not visible at PC Device - {}".format(rgb_keyword_text)

    def test_15_verify_programmable_key_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_9(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()        
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Programmable Key Action Item time :', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert programmable_key_text=="Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        
    def test_16_click_programmable_key_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_10(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu() 
        self.fc.fd["devices"].click_programmable_key()
        self.fc.fd["devices"].click_pc_devices()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()        
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Programmable Key Action Item time:', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert programmable_key_text=="Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)

    def test_17_verify_support_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_11(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        support_text = self.fc.fd["devices"].verify_support_action_card()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Support time :', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert support_text=="Support","Support is not visible at PC Device - {}".format(support_text)
        
    def test_18_click_support_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_12(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu() 
        self.fc.fd["navigation_panel"].click_PC_device_menu()    
        self.fc.fd["devices"].click_support_action_card()
        self.fc.fd["devices"].click_back()
        support_text = self.fc.fd["devices"].verify_support_action_card()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Support time :', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert support_text=="Support","Support is not visible at PC Device - {}".format(support_text)
        self.st = time.time() 
        self.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")

    @pytest.mark.require_platform(["grogu"])
    def test_19_verify_display_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_13(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()       
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Display Control time :', elapsed_time, 'seconds')
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert display_control_text=="Display Control","Display Control is not visible at PC Device - {}".format(display_control_text)

    @pytest.mark.require_platform(["grogu"])
    def test_20_click_display_control_module_check_the_time_Online_verify_the_time_is_less_than_2_seconds_C32016394_14(self):    
        self.st = time.time() 
        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()  
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["devices"].click_pc_devices()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        self.et = time.time()
        elapsed_time = self.et - self.st
        print('Display Control time :', elapsed_time, 'seconds')
        self.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        assert elapsed_time<=2,"Execution time is more than 2 seconds"
        assert display_control_text=="Display Control","Display Control is not visible at PC Device - {}".format(display_control_text)
        
        
            
   
        
   
