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
    def test_01_default_modes_C42891262(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Brightness slider is not Default"
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 79, "Red value does not match"
            assert green_int >= 92, "Green value does not match"
            assert blue_int >= 53, "Blue value does not match"
            assert clear_int >= 135, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 12, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_contrast_slider_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == '0', "Contrast value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 12, "Red value does not match"
            assert green_int <= 13, "Green value does not match"
            assert blue_int <= 10, "Blue value does not match"
            assert clear_int <= 14, "Clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_entertainment_modes_C42891265(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_entertainment_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_entertainment_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Entertainment", "Brightness slider is not Entertainment"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 78, "Red value does not match"
            assert green_int >= 92, "Green value does not match"
            assert blue_int >= 53, "Blue value does not match"
            assert clear_int >= 135, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 12, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_contrast_slider_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == '0', "Contrast value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 12, "Red value does not match"
            assert green_int <= 13, "Green value does not match"
            assert blue_int <= 10, "Blue value does not match"
            assert clear_int <= 14, "Clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_srgb_web_modes_C42891267(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_sRGB_web_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_sRGB_web_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB (Web)", "Brightness slider is not sRGB (Web)"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 79, "Red value does not match"
            assert green_int >= 93, "Green value does not match"
            assert blue_int >= 54, "Blue value does not match"
            assert clear_int >= 135, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 12, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_adobe_rgb_printing_and_imaging_modes_C42891268(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_adobe_RGB_painting_and_imaging_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_adobe_RGB_painting_and_imaging_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Printing and Imaging (Adobe RGB)", "Brightness slider is not Printing and Imaging (Adobe RGB)"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 78, "Red value does not match"
            assert green_int >= 92, "Green value does not match"
            assert blue_int >= 53, "Blue value does not match"
            assert clear_int >= 135, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 12, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_display_p3_photos_and_videos_modes_C42891269(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_photos_videos_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_photos_videos_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Photos and Videos (P3 D65)", "Brightness slider is not Photos and Videos (P3 D65)"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 79, "Red value does not match"
            assert green_int >= 93, "Green value does not match"
            assert blue_int >= 54, "Blue value does not match"
            assert clear_int >= 135, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 12, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_native_modes_C42891270(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_willie_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_willie_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 81, "Red value does not match"
            assert green_int >= 95, "Green value does not match"
            assert blue_int >= 55, "Blue value does not match"
            assert clear_int >= 139, "Brightness visual does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 14, "Red value does not match"
            assert green_int <= 15, "Green value does not match"
            assert blue_int <= 13, "Blue value does not match"
            assert clear_int <= 17, "Clear value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_contrast_slider_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == '0', "Contrast value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 12, "Red value does not match"
            assert green_int <= 13, "Green value does not match"
            assert blue_int <= 10, "Blue value does not match"
            assert clear_int <= 14, "Clear value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()