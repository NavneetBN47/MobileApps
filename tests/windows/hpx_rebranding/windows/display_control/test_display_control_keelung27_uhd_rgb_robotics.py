import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # Tests to be executed on Keelung27 UHD with RGB robotics

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_rgb_visual_neutral_mode_keelung27_uhd_C53001229(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display mode is not Neutral, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "97", f"Green value is not 97, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "96", f"Blue value is not 96, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert 297 <= clear_int <= 337, f"Brightness value is not between 297 and 337, actual value is {clear_int}"
            assert 179 <= red_int <= 219, f"Red value is not between 179 and 219, actual value is {red_int}"
            assert 223 <= green_int <= 263, f"Green value is not between 223 and 263, actual value is {green_int}"
            assert 111 <= blue_int <= 151, f"Blue value is not between 111 and 151, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "0", f"Red value is not 0, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "0", f"Green value is not 0, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "100", f"Blue value is not 100, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert 41 <= clear_int <= 81, f"Brightness value is not between 41 and 81 after adjusting RGB, actual value is {clear_int}"
            assert 7 <= red_int <= 37, f"Red value is not between 7 and 37 after adjusting RGB, actual value is {red_int}"
            assert 14 <= green_int <= 54, f"Green value is not between 14 and 54 after adjusting RGB, actual value is {green_int}"
            assert 69 <= blue_int <= 109, f"Blue value is not between 69 and 109 after adjusting RGB, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_rgb_visual_warm_mode_keelung27_uhd_C53001231(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_warm_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_warm_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Warm", f"Display mode is not Warm, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "14", f"Brightness slider value is not 14, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "92", f"Green value is not 92, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "80", f"Blue value is not 80, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert 87 <= clear_int <= 127, f"Brightness value is not between 87 and 127, actual value is {clear_int}"
            assert 51 <= red_int <= 91, f"Red value is not between 51 and 91, actual value is {red_int}"
            assert 60 <= green_int <= 100, f"Green value is not between 60 and 100, actual value is {green_int}"
            assert 17 <= blue_int <= 57, f"Blue value is not between 17 and 57, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "0", f"Green value is not 0, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "0", f"Blue value is not 0, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 24 <= clear_int <= 64, f"Brightness value is not between 24 and 64 after adjusting RGB, actual value is {clear_int}"
            assert 23 <= red_int <= 63, f"Red value is not between 23 and 63 after adjusting RGB, actual value is {red_int}"
            assert 0 <= green_int <= 33, f"Green value is not between 0 and 33 after adjusting RGB, actual value is {green_int}"
            assert 0 <= blue_int <= 25, f"Blue value is not between 0 and 25 after adjusting RGB, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_rgb_visual_cool_mode_keelung27_uhd_C53001233(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_cool_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_cool_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Cool", f"Display mode is not Cool, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "42", f"Brightness slider value is not 42, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "88", f"Red value is not 88, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "90", f"Green value is not 90, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "100", f"Blue value is not 100, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 218 <= clear_int <= 258, f"Brightness value is not between 218 and 258, actual value is {clear_int}"
            assert 129 <= red_int <= 169, f"Red value is not between 129 and 169, actual value is {red_int}"
            assert 163 <= green_int <= 203, f"Green value is not between 163 and 203, actual value is {green_int}"
            assert 77 <= blue_int <= 117, f"Blue value is not between 77 and 117, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "0", f"Red value is not 0, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "0", f"Green value is not 0, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "100", f"Blue value is not 100, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 25 <= clear_int <= 65, f"Brightness value is not between 25 and 65 after adjusting RGB, actual value is {clear_int}"
            assert 0 <= red_int <= 33, f"Red value is not between 0 and 33 after adjusting RGB, actual value is {red_int}"
            assert 5 <= green_int <= 45, f"Green value is not between 5 and 45 after adjusting RGB, actual value is {green_int}"
            assert 47 <= blue_int <= 87, f"Blue value is not between 47 and 87 after adjusting RGB, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_rgb_visual_hp_enhance_mode_keelung27_uhd_C53001235(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "HP enhance+", f"Display mode is not HP enhance+, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "97", f"Green value is not 97, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "96", f"Blue value is not 96, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 297 <= clear_int <= 337, f"Brightness value is not between 297 and 337, actual value is {clear_int}"
            assert 179 <= red_int <= 219, f"Red value is not between 179 and 219, actual value is {red_int}"
            assert 223 <= green_int <= 263, f"Green value is not between 223 and 263, actual value is {green_int}"
            assert 111 <= blue_int <= 151, f"Blue value is not between 111 and 151, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "0", f"Red value is not 0, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "100", f"Green value is not 100, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "0", f"Blue value is not 0, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 135 <= clear_int <= 175, f"Brightness value is not between 135 and 175 after adjusting RGB, actual value is {clear_int}"
            assert 57 <= red_int <= 97, f"Red value is not between 57 and 97 after adjusting RGB, actual value is {red_int}"
            assert 167 <= green_int <= 207, f"Green value is not between 167 and 207 after adjusting RGB, actual value is {green_int}"
            assert 7 <= blue_int <= 47, f"Blue value is not between 7 and 47 after adjusting RGB, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_rgb_visual_native_mode_keelung27_uhd_C53001237(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Display mode is not Native, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "100", f"Brightness slider value is not 100, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "100", f"Green value is not 100, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "100", f"Blue value is not 100, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 450 <= clear_int <= 490, f"Brightness value is not between 450 and 490, actual value is {clear_int}"
            assert 273 <= red_int <= 313, f"Red value is not between 273 and 313, actual value is {red_int}"
            assert 344 <= green_int <= 384, f"Green value is not between 344 and 384, actual value is {green_int}"
            assert 187 <= blue_int <= 227, f"Blue value is not between 187 and 227, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "0", f"Red value is not 0, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "0", f"Green value is not 0, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "100", f"Blue value is not 100, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 71 <= clear_int <= 111, f"Brightness value is not between 71 and 111 after adjusting RGB, actual value is {clear_int}"
            assert 5 <= red_int <= 45, f"Red value is not between 5 and 45 after adjusting RGB, actual value is {red_int}"
            assert 30 <= green_int <= 70, f"Green value is not between 30 and 70 after adjusting RGB, actual value is {green_int}"
            assert 113 <= blue_int <= 153, f"Blue value is not between 113 and 153 after adjusting RGB, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()