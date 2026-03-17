from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_Display_Setting(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request,windows_test_setup):
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
        yield
        cls.fc.close_windows_settings_panel()
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)

    #this suite should run on willie
    def test_01_display_setting_C32603677(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True
        #click on work title
        self.fc.fd["display_control"].click_work_tile()
        self.mode=self.fc.fd["display_control"].verify_work_tile()
        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["home"].verify_color_profile_in_display_setting()) is True
        assert self.fc.fd["home"].get_work_color_profile_in_setting() == self.mode
        #select any mode in setting
        self.fc.fd["home"].click_mode_in_display_setting()
        self.fc.fd["home"].click_select_low_blue_light_in_setting()
        self.fc.fd["audio"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].is_low_blue_light_tile_selected()) == True
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
    
    def test_02_display_setting_color_profile_C32603657(self):
        self.fc.restart_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True
        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["home"].verify_color_profile_in_display_setting()) is True
        #click color profile combo in display setting
        self.fc.fd["home"].click_mode_in_display_setting()
        assert self.fc.fd["home"].get_default_color_profile_in_setting() == "Default", "Default color profile is not selected"
        assert self.fc.fd["home"].get_entertainment_color_profile_in_setting() == "Entertainment", "Entertainment color profile is not selected"
        assert self.fc.fd["home"].get_low_blue_light_color_profile_in_setting() == "Low Blue Light", "Low Blue Light color profile is not selected"
        assert self.fc.fd["home"].get_low_light_color_profile_in_setting() == "Low Light", "Low light color profile is not selected"
        assert self.fc.fd["home"].get_native_color_profile_in_setting() == "Native", "Native color profile is not selected"
        assert self.fc.fd["home"].get_photos_and_videos_color_profile_in_setting() == "Photos and Videos (P3-D65)", "Photos and Videos color profile is not selected"
        assert self.fc.fd["home"].get_printing_and_imaging_color_profile_in_setting() == "Printing and Imaging (Adobe RGB)", "Printing and Imaging color profile is not selected"
        assert self.fc.fd["home"].get_web_rgb_color_profile_in_setting() == "Web(sRGB)", "Web(sRGB) color profile is not selected"
        assert self.fc.fd["home"].get_work_color_profile_in_setting() == "Work", "Work color profile is not selected"
        #closing setting so latest tc execution will not be affected
        self.fc.fd["home"].click_close()
    
    @pytest.mark.ota
    def test_03_changing_switching_display_modes_through_windows_settings_C41042198(self):
        self.fc.close_myHP()
        self.fc.open_system_settings_display()
        self.fc.fd["home"].click_mode_in_display_setting()
        self.fc.fd["home"].select_native_color_profile_in_setting()
        self.fc.launch_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True, "Brightness slider is not present"
        assert bool(self.fc.fd["display_control"].verify_app_out_of_sync_show()) is True, "App out of sync is not shown"
        self.fc.fd["display_control"].click_see_more_link()
        assert bool(self.fc.fd["display_control"].verify_not_synchronized_title()) is True, "Not Synchronized title is not shown"
        assert bool(self.fc.fd["display_control"].verify_discard_changes_button_show()) is True, "Discard changes button is not shown"
        assert bool(self.fc.fd["display_control"].verify_keep_new_changes_button_show()) is True, "Keep new changes button is not shown"
        assert bool(self.fc.fd["display_control"].verify_close_btn_on_restore_popup()) is True, "Close button is not shown"
        self.fc.fd["display_control"].click_keep_new_changes_button()
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
        self.fc.close_myHP()
        self.fc.open_system_settings_display()
        self.fc.fd["home"].click_mode_in_display_setting()
        self.fc.fd["home"].select_low_blue_light_color_profile_in_setting()
        self.fc.launch_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["display_control"].verify_app_out_of_sync_show()) is True, "App out of sync is not shown"
        self.fc.fd["display_control"].click_see_more_link()
        self.fc.fd["display_control"].click_discard_changes_button()
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
    
    @pytest.mark.ota
    def test_04_lbl_scheduler_C41063337(self):
        self.fc.close_myHP()
        #Launch the Windows settings application
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        #change the Brightness value fron Windows settings application
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(20)
            system_brightness_value = int(self.sf.get_windows_brightness_value())
        else:
            self.sf.windows_brightness_increase(20)
            system_brightness_value = int(self.sf.get_windows_brightness_value())        
        self.sf.click_windows_battery_icon()
        #Launch the HPX application
        self.fc.launch_myHP()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        #Navigate to Display Control Module
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True, "Brightness slider is not present"
        self.fc.fd["display_control"].click_advaced_setting()
        #Turn on LBL scheduler through advanced settings and schedule the current time from advanced settings
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        print("time",self.fc.get_current_time())
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        #inline notification for out of sync should Display
        assert bool(self.fc.fd["display_control"].verify_app_out_of_sync_show()) is True, "App out of sync is not shown"
        #Click on see more hyper link of inline notification
        self.fc.fd["display_control"].click_see_more_link()
        #.App settings not synchronized, , prompt message should be display and with 3 options-1. Discard changes,2. Keep new changes,3.Cancel button
        assert bool(self.fc.fd["display_control"].verify_not_synchronized_title()) is True, "Not Synchronized title is not shown"
        assert bool(self.fc.fd["display_control"].verify_discard_changes_button_show()) is True, "Discard changes button is not shown"
        assert bool(self.fc.fd["display_control"].verify_keep_new_changes_button_show()) is True, "Keep new changes button is not shown"
        assert bool(self.fc.fd["display_control"].verify_close_btn_on_restore_popup()) is True, "Close button is not shown"
        #If we click on Keep New changes button-changes are made through advanced settings should be synchronized to HPX application
        #If we click on Discard changes button-changes are made in the advanced settings should not be synchronized to HPX application
        self.fc.fd["display_control"].click_keep_new_changes_button()
        assert system_brightness_value == int(self.fc.fd["display_control"].get_brightness_slider_value_100()), "Brightness value is not same as system brightness value"
        self.fc.close_myHP()
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        #change the Brightness value from Windows settings application
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(20)
            system_brightness_value = int(self.sf.get_windows_brightness_value())
        else:
            self.sf.windows_brightness_increase(20)
            system_brightness_value = int(self.sf.get_windows_brightness_value())        
        self.sf.click_windows_battery_icon()
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True, "Brightness slider is not present"
        assert bool(self.fc.fd["display_control"].verify_app_out_of_sync_show()) is True, "App out of sync is not shown"
        self.fc.fd["display_control"].click_see_more_link()
        self.fc.fd["display_control"].click_discard_changes_button()
        assert system_brightness_value != int(self.fc.fd["display_control"].get_brightness_slider_value_100()), "Brightness value is not same as system brightness value"
