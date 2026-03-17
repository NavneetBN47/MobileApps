import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):
    
    #this suite should run on willie robotics with HDR off 
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_srgb_web_relaunch_C42891271(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_sRGB_web_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_sRGB_web_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB (Web)", "Brightness slider is not sRGB (Web)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 69, "Red value does not match"
            assert green_int >= 81, "Green value does not match"
            assert blue_int >= 46, "Blue value does not match"
            assert clear_int >= 118, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB (Web)", "Brightness slider is not sRGB (Web)"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_rgb_printing_and_reimaging_relaunch_C42891272(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_adobe_RGB_painting_and_imaging_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_adobe_RGB_painting_and_imaging_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Printing and Imaging (Adobe RGB)", "Brightness slider is not Printing and Imaging (Adobe RGB)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 67, "Red value does not match"
            assert green_int >= 80, "Green value does not match"
            assert blue_int >= 46, "Blue value does not match"
            assert clear_int >= 118, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Printing and Imaging (Adobe RGB)", "Brightness slider is not Printing and Imaging (Adobe RGB)"

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_display_p3_photos_and_videos_relaunch_C42891273(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_photos_videos_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_photos_videos_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Photos and Videos (P3 D65)", "Brightness slider is not Photos and Videos (P3 D65)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 68, "Red value does not match"
            assert green_int >= 81, "Green value does not match"
            assert blue_int >= 47, "Blue value does not match"
            assert clear_int >= 118, "Brightness visual does not match"
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Photos and Videos (P3 D65)", "Brightness slider is not Photos and Videos (P3 D65)"

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_native_mode_relaunch_C42891274(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_willie_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_willie_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 71, "Red value does not match"
            assert green_int >= 83, "Green value does not match"
            assert blue_int >= 48, "Blue value does not match"
            assert clear_int >= 122, "Brightness visual does not match"
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        #revert back changes to default for next suite as reset or reinstall will not revert the brightness value and mode back
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()