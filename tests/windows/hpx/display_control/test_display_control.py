import re
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request,windows_test_setup):
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
            cls.fc.launch_myHP()
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)

    #This suite should run on willie
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_verify_brightness_contrast_strings_on_display_control_ui_C32194961(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        assert self.fc.fd["display_control"].verify_brightness_contrast_label() == "Brightness & Contrast","Brightness & Contrast label is not present or visible"
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True,"Brightness slider is not present or visible"
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True,"Contrast slider is not present or visible"
        self.driver.swipe(direction="down", distance=3)
        assert self.fc.fd["display_control"].verify_restore_default_button() == "Restore Defaults","Restore defaults button is not present or visible"
        assert self.fc.fd["display_control"].verify_myhp_logo_is_present() == True,"My HP logo is not present or visible"

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_02_verify_standard_mode_strings_on_display_control_ui_C32194962(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        self.driver.swipe(direction="down", distance=2)
        assert self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present"
        assert self.fc.fd["display_control"].verify_default_tile() == "Default","Default Tile is not present"
        assert self.fc.fd["display_control"].verify_work_tile() == "Work","Work Tile is not present"
        assert self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present"
        assert self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present"
        assert self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present"

    @pytest.mark.ota
    def test_03_verify_advanced_mode_strings_on_display_control_ui_C32194963(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        self.driver.swipe(direction="down", distance=2)
        assert self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present"
        assert self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present"
        assert self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present"
        assert self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present"
        assert self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present"

    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_verify_app_brightness_slider_is_same_as_system_set_up_C36044360(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if app_brightness_value!="100":
            self.fc.fd["display_control"].set_slider_value_increase(100-int(app_brightness_value),"Brightness_slider")
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "100"==app_brightness_value,"Brightness not increased to 100"
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert "100" ==self.fc.fd["display_control"].get_system_brightness()
        self.fc.fd["audio"].click_windows_speaker_icon()
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        time.sleep(3)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "90"==app_brightness_value,"Brightness not increased to 90"
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert "90" ==self.fc.fd["display_control"].get_system_brightness()
        self.fc.fd["audio"].click_windows_speaker_icon()
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)

    def test_05_verify_app_contrast_slider_displays_correctly_as_set_up_C36044361(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        if app_contrast_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Contrast_slider")
        app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert "100"==app_contrast_value,"Volumn not increased to 100"
        app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        if app_contrast_value!=50:
            self.fc.fd["display_control"].set_slider_value_decrease(45,"Contrast_slider")
        app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert "55"==app_contrast_value,"Volumn not increased to 55"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
    
    def test_06_standard_modes_restore_defaults_C32195006(self):
        time.sleep(3)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        time.sleep(3)
        #need to click restore defaults button coz need every setting as by defaults
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        br_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        #select low blue light mode
        self.fc.fd["display_control"].click_low_blue_light_tile()
        assert bool(self.fc.fd["display_control"].is_low_blue_light_tile_selected()) == True,"Low Blue Light mode is not selected"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        assert bool(self.fc.fd["display_control"].is_default_tile_selected()) == True,"Default tile is not selected"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == br_value,"Brightness value is not restored"
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == contrast_value,"Contrast value is not restored"
        self.fc.fd["display_control"].click_advaced_setting()
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light() == '0', "Low Blue Light scheduler is on"
        assert self.fc.fd["display_control"].turn_on_hr_combo_advanced_settings_is_enable() == 'false',"Advanced settings is not disabled"
        assert self.fc.fd["display_control"].turn_off_hr_combo_advanced_settings_is_enable() == 'false',"Advanced settings is not disabled"
        assert self.fc.fd["display_control"].get_turn_on_am_pm_advanced_settings() == "pm", "Turn on time is not in PM"
        assert self.fc.fd["display_control"].get_turn_off_am_pm_advanced_settings() == "am", "Turn off time is not in AM"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
    
    def test_07_advance_modes_restore_defaults_C32195007(self):
        time.sleep(3)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        time.sleep(3)
        #need to click restore defaults button coz need every setting as by defaults
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        br_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        self.fc.fd["display_control"].click_native_tile()
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native mode is not selected"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        assert bool(self.fc.fd["display_control"].is_default_tile_selected()) == True,"Default tile is not selected"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == br_value,"Brightness value is not restored"
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == contrast_value,"Contrast value is not restored"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
