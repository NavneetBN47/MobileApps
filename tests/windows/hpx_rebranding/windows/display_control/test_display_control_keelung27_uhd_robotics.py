import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # Tests to be executed on Keelung27 UHD with RGB robotics
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_display_modes_neutral_mode_keelung27_uhd_C53001207(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display mode is not Neutral, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 298 <= clear_int <= 338, f"Brightness value is not between 298 and 338, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 42 <= clear_int <= 82, f"Brightness value is not between 42 and 82, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_display_modes_warm_mode_keelung27_uhd_C53001213(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_warm_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_warm_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Warm", f"Display mode is not Warm, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "14", f"Brightness slider value is not 14, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 87 <= clear_int <= 127, f"Brightness value is not between 87 and 127, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "0", f"Brightness slider value is not 0, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 47 <= clear_int <= 87, f"Brightness value is not between 47 and 87 after reducing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "100", f"Brightness slider value is not 100, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 491 <= clear_int <= 531, f"Brightness value is not between 491 and 531 after increasing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_display_modes_cool_mode_keelung27_uhd_C53001217(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_cool_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_cool_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Cool", f"Display mode is not Cool, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "42", f"Brightness slider value is not 42, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 219 <= clear_int <= 259, f"Brightness value is not between 219 and 259, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "100", f"Brightness slider value is not 100, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 457 <= clear_int <= 497, f"Brightness value is not between 457 and 497 after increasing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "0", f"Brightness slider value is not 0, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 42 <= clear_int <= 82, f"Brightness value is not between 42 and 82 after reducing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_display_modes_hpenhance_mode_keelung27_uhd_C53001219(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "HP enhance+", f"Display mode is not HP enhance+, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 297 <= clear_int <= 337, f"Brightness value is not between 297 and 337, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "100", f"Brightness slider value is not 100, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 456 <= clear_int <= 496, f"Brightness value is not between 456 and 496 after increasing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "0", f"Brightness slider value is not 0, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 42 <= clear_int <= 82, f"Brightness value is not between 42 and 82 after reducing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_display_modes_native_mode_keelung27_uhd_C53001221(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page_keelung27")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page_keelung27")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Display mode is not Native, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "100", f"Brightness slider value is not 100, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 507 <= clear_int <= 547, f"Brightness value is not between 507 and 547, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "0", f"Brightness slider value is not 0, actual value is {current_brightness}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 49 <= clear_int <= 89, f"Brightness value is not between 49 and 89 after reducing brightness, actual value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_restore_default_for_keelung27_uhd_C53001226(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display mode is not neutral, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 50)
        self.fc.fd["display_control"].click_title_bar()
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "50", f"Brightness slider value is not 50, actual value is {current_brightness}"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "97", f"Green value is not 97, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "96", f"Blue value is not 96, actual value is {current_blue_value}"
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 50)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 50)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 50)
        self.fc.fd["display_control"].click_title_bar()
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "50", f"Red value is not 50, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "50", f"Green value is not 50, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "50", f"Blue value is not 50, actual value is {current_blue_value}"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 46 <= clear_int <= 86, f"Brightness value is not between 46 and 86 after adjusting RGB values, actual value is {clear_int}"
            assert 22 <= red_int <= 62, f"Red value is not between 22 and 62 after adjusting RGB values, actual value is {red_int}"
            assert 29 <= green_int <= 69, f"Green value is not between 29 and 69 after adjusting RGB values, actual value is {green_int}"
            assert 5 <= blue_int <= 45, f"Blue value is not between 5 and 45 after adjusting RGB values, actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        time.sleep(10)
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "100", f"Red value is not 100, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "97", f"Green value is not 97, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "96", f"Blue value is not 96, actual value is {current_blue_value}"
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display mode is not neutral, actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "62", f"Brightness slider value is not 62, actual value is {current_brightness}"