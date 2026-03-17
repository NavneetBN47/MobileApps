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
    def test_01_brightness_slider_value_remains_same_after_relaunch_the_app_C36044362(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        brghtness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if brghtness_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(5,"Brightness_slider")
        brghtness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "95"==brghtness_value,"brghtness value not increased to 95"
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        brghtness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "95"==brghtness_value,"brghtness value not increased to 95"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)

    def test_02_contrast_slider_value_remains_same_after_relaunch_the_app_C37210043(self):
        self.fc.restart_myHP()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        if contrast_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Contrast_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(15,"Contrast_slider")
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert "85"==contrast_value,"brghtness value not increased to 85"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert "85"==contrast_value,"brghtness value not increased to 85"
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
    

    def test_03_brightness_minimum_value_relaunch_C32194986(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        time.sleep(1)
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if brightness_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(100,"Brightness_slider")
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "0" == brightness_value,"Brightness slider value is not 0"
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert self.fc.fd["display_control"].get_system_brightness() == "0" ,"System Brightness is not dim"
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        time.sleep(2)
        #verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "Brightness slider is not present"
        #verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "Contrast slider is not present"
        #verify brightness slider value is 0
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "0" ,"Brightness slider value is not 0"
        #display modes are visible
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        assert self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present"
        assert self.fc.fd["display_control"].verify_default_tile() == "Default","Default Tile is not present"
        assert self.fc.fd["display_control"].verify_work_tile() == "Work","Work Tile is not present"
        assert self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present"
        assert self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present"
        assert self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present"
        assert self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present"
        assert self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present"
        assert self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present"
        assert self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present"
        assert self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)


    def test_04_brightness_maximum_value_relaunch_C32194987(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if brightness_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "100" == brightness_value,"Brightness slider value is not 100"
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert self.fc.fd["display_control"].get_system_brightness() == "100" ,"System Brightness is not high"
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        time.sleep(2)
        #verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "Brightness slider is not present"
        #verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "Contrast slider is not present"
        #verify brightness slider value is 0
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100" ,"Brightness slider value is not 100"
         #display modes are visible
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        assert self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present"
        assert self.fc.fd["display_control"].verify_default_tile() == "Default","Default Tile is not present"
        assert self.fc.fd["display_control"].verify_work_tile() == "Work","Work Tile is not present"
        assert self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present"
        assert self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present"
        assert self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present"
        assert self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present"
        assert self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present"
        assert self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present"
        assert self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present"
        assert self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)


    def test_05_brightness_medium_value_relaunch_C32194988(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if brightness_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        time.sleep(2)
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "100" == brightness_value,"Brightness slider value is not 100"
        time.sleep(2)
        self.fc.fd["display_control"].set_slider_value_decrease(50,"Brightness_slider")
        time.sleep(2)
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "50" == brightness_value,"Brightness slider value is not 50"
        self.fc.fd["audio"].click_windows_speaker_icon()
        assert self.fc.fd["display_control"].get_system_brightness() == "50" ,"System Brightness is not medium"
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        time.sleep(2)
        #verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "Brightness slider is not present"
        #verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "Contrast slider is not present"
        #verify brightness slider value is 0
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "50" ,"Brightness slider value is not 50"
        #display modes are visible
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        assert self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present"
        assert self.fc.fd["display_control"].verify_default_tile() == "Default","Default Tile is not present"
        assert self.fc.fd["display_control"].verify_work_tile() == "Work","Work Tile is not present"
        assert self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present"
        assert self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present"
        assert self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present"
        assert self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present"
        assert self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present"
        assert self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present"
        assert self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present"
        assert self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)

    def test_06_launch_display_control_via_deeplink_C49014584(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pcdisplaycontrol")
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
    
    def test_07_keyboard_dismiss_alt_f4_advance_modes_C32547082(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        self.fc.fd["display_control"].set_slider_value_increase(5,"Brightness_slider")
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_increase(5,"Contrast_slider")
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        self.fc.fd["display_control"].click_native_tile()
        assert self.fc.fd["display_control"].is_Native_tile_selected() == 'true', "Native tile is not selected"
        self.fc.fd["display_control"].press_alt_f4()
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        current_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert brightness_value == current_brightness_value,"Brightness value is not same"
        current_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert contrast_value == current_contrast_value,"Contrast value is not same"
        assert self.fc.fd["display_control"].is_Native_tile_selected() == 'true', "Native tile is not selected"
    
    def test_08_keyboard_dismiss_alt_f4_standard_modes_C32194995(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        self.fc.fd["display_control"].set_slider_value_increase(5,"Brightness_slider")
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_increase(5,"Contrast_slider")
        contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        self.fc.fd["display_control"].click_default_tile()
        assert self.fc.fd["display_control"].is_default_tile_selected() == 'true', "Default tile is not selected"
        self.fc.fd["display_control"].press_alt_f4()
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        current_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert brightness_value == current_brightness_value,"Brightness value is not same"
        current_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert contrast_value == current_contrast_value,"Contrast value is not same"
        assert self.fc.fd["display_control"].is_default_tile_selected() == 'true', "Default tile is not selected"
