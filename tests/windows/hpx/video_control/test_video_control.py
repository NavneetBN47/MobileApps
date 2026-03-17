from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Video_Control(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        
        
    def test_01_verify_video_control_displayed_C33310991(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(1)
        if bool (self.fc.fd["hp_registration"].verify_hpone_page_show()):
            self.fc.fd["hp_registration"].click_hpone_page_skip_btn()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(5)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_video_control_auto_frame()) is True
        time.sleep(2)
        

    
    def test_02_turn_on_off_autoframe_C33318907(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(1)
        if bool (self.fc.fd["hp_registration"].verify_hpone_page_show()):
            self.fc.fd["hp_registration"].click_hpone_page_skip_btn()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(5)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_video_control_auto_frame()) is True
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "0"
        time.sleep(1)
        self.fc.fd["video_control"].click_auto_frame_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "1"
        time.sleep(1)
        self.fc.fd["video_control"].click_auto_frame_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "0"
        time.sleep(1)

    
    def test_03_turn_on_off_enhance_C33318911(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(1)
        if bool (self.fc.fd["hp_registration"].verify_hpone_page_show()):
            self.fc.fd["hp_registration"].click_hpone_page_skip_btn()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(5)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_video_control_Enhance()) is True
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "0"
        time.sleep(2)
        self.fc.fd["video_control"].click_enhance_btn()
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "1"
        time.sleep(2)
        self.fc.fd["video_control"].click_enhance_btn()
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "0"
        time.sleep(2)
    
    def test_04_fist_launch_verify_all_settings_will_show_default_settings_C33318893(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(5)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_video_control_auto_frame()) is True
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "0"
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_video_control_Enhance()) is True
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "0"
        time.sleep(1)
        self.fc.fd["video_control"].move_down_for_restore("restore_default")
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_video_control_background_off_status() == "Off"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_mixer_tab_show()) is True
        time.sleep(2)
        self.fc.fd["video_control"].click_mixer_tab() 
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_picture_in_picture_status() == "Picture in picture"
        time.sleep(2)

    def test_05_first_use_experience_tutoial_message_C33596998(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(1)
        self.fc.close_myHP()
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_help_icon_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_help_icon()
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_video_control_auto_frame()) is True
        time.sleep(1)

    def test_06_restore_default_settings_in_camera_tab_C33318895(self):
        self.fc.re_install_app(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_smartcamV3_module()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_enhance_your_video_experience_show()) is True
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_lets_get_your_show()) is True
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_tutorial_next_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_tutorial_next_button() 
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_video_control_auto_frame()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_auto_frame_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "1"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_video_control_Enhance()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_enhance_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "1"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_backlight_adjustment_text_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_backlight_adjustment_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_backlight_adjustment_toggle_status() == "1"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_lowlight_adjustment_text_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_lowlight_adjustment_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_lowlight_adjustment_toggle_status() == "1"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_natural_tone_text_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_natural_tone_btn()
        time.sleep(2)
        assert self.fc.fd["video_control"].verify_natural_tone_toggle_status() == "1"
        time.sleep(1)
        self.fc.fd["video_control"].move_down_for_restore("restore_default")
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_background_blur_text_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_background_blur_btn()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_background_blur_status() == "Blur"
        time.sleep(1)
        self.fc.fd["video_control"].click_mixer_tab() 
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_layout1_icon_show() is True
        time.sleep(1)
        self.fc.fd["video_control"].click_layout1_icon() is True
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_layout1_icon_status() == "Layout 1"
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_camera_settings_text_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_camera_settings_text() is True
        time.sleep(1)
        assert bool(self.fc.fd["video_control"].verify_restore_button_show()) is True
        time.sleep(1)
        self.fc.fd["video_control"].click_restore_button()
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_video_control_background_off_status() == "Off"
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_auto_frame_toggle_status() == "0"
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_enhance_toggle_status() == "0"
        time.sleep(1)
        self.fc.fd["video_control"].click_mixer_tab() 
        time.sleep(1)
        assert self.fc.fd["video_control"].verify_layout1_icon_status () == "Layout 1"
        time.sleep(1)



        
        
        
        



