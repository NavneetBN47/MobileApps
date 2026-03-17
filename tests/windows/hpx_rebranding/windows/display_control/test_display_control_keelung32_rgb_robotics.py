import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restore_default_for_keelung32_C51248478(self):
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Brightness slider is not P3(D65)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "BT709 (D65)", "Brightness slider is not BT709 (D65))"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "6", "Brightness slider value is not 6"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_rgb_visual_p3d65_mode_C51248486(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Brightness slider is not P3(D65)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 300, f"Brightness visual does not match found {clear_int}, expected >=300"
            assert red_int >= 170, f"Red value does not match found {red_int}, expected >=170"
            assert green_int >= 227, f"Green value does not match found {green_int}, expected >=227"
            assert blue_int >= 147, f"Blue value does not match found {blue_int}, expected >=147"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_rgb_visual_bt709d65_mode_C51248485(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "BT709 (D65)", "Brightness slider is not BT709 (D65))"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "6", "Brightness slider value is not 6"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 84, f"Brightness visual does not match found {clear_int}, expected >=84"
            assert red_int >= 43, f"Red value does not match found {red_int}, expected >=43"
            assert green_int >= 58, f"Green value does not match found {green_int}, expected >=58"
            assert blue_int >= 33, f"Blue value does not match found {blue_int}, expected >=33"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 5, f"Brightness visual does not match found {clear_int}, expected <=5"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_rgb_visual_srgb_d65_mode_C51248484(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB D65", "Brightness slider is not sRGB D65"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 300, f"Brightness visual does not match found {clear_int}, expected >=300"
            assert red_int >= 178, f"Red value does not match found {red_int}, expected >=178"
            assert green_int >= 227, f"Green value does not match found {green_int}, expected >=227"
            assert blue_int >= 146, f"Blue value does not match found {blue_int}, expected >=146"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_rgb_visual_native_mode_C51248483(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 817, f"Brightness visual does not match found {clear_int}, expected >=817"
            assert red_int >= 507, f"Red value does not match found {red_int}, expected >=507"
            assert green_int >= 617, f"Green value does not match found {green_int}, expected >=617"
            assert blue_int >= 380, f"Blue value does not match found {blue_int}, expected >=380"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 14, "Brightness visual does not match"
            assert red_int <= 5, "Red value does not match"
            assert green_int <= 5, "Green value does not match"
            assert blue_int <= 5, "Blue value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_rgb_visual_hpenhance_mode_C51248482(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "HP enhance+", "Brightness slider is not HP enhance+"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "97", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "96", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 300, f"Brightness visual does not match found {clear_int}, expected >=300"
            assert red_int >= 179, f"Red value does not match found {red_int}, expected >=179"
            assert green_int >= 225, f"Green value does not match found {green_int}, expected >=225"
            assert blue_int >= 147, f"Blue value does not match found {blue_int}, expected >=147"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, "Brightness visual does not match"
            assert red_int <= 5, "Red value does not match"
            assert green_int <= 5, "Green value does not match"
            assert blue_int <= 5,  "Blue value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_07_rgb_visual_cool_mode_C51248481(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_cool_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_cool_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Cool", "Brightness slider is not Cool"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "22", "Brightness slider value is not 22"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "88", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "90", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 156, f"Brightness visual does not match found {clear_int}, expected >=156"
            assert red_int >= 81, f"Red value does not match found {red_int}, expected >=81"
            assert green_int >= 112, f"Green value does not match found {green_int}, expected >=112"
            assert blue_int >= 87, f"Blue value does not match found {blue_int}, expected >=87"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_08_rgb_visual_warm_mode_C51248480(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_warm_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_warm_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Warm", "Brightness slider is not Warm"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "6", "Brightness slider value is not 6"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "92", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "80", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 88, f"Brightness visual does not match found {clear_int}, expected >=88"
            assert red_int >= 50, f"Red value does not match found {red_int}, expected >=50"
            assert green_int >= 61, f"Green value does not match found {green_int}, expected >=61"
            assert blue_int >= 25,  f"Blue value does not match found {blue_int}, expected >=25"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5,  f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_09_rgb_visual_neutral_mode_C51248479(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_neutral_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_neutral_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not Neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "97", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "96", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 300, f"Brightness visual does not match found {clear_int}, expected >=300"
            assert red_int >= 179, f"Red value does not match found {red_int}, expected >=179"
            assert green_int >= 227, f"Green value does not match found {green_int}, expected >=227"
            assert blue_int >= 147, f"Blue value does not match found {blue_int}, expected >=147"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 10, f"Brightness visual does not match found {clear_int}, expected <=10"
            assert red_int <= 5, f"Red value does not match found {red_int}, expected <=5"
            assert green_int <= 5, f"Green value does not match found {green_int}, expected <=5"
            assert blue_int <= 5, f"Blue value does not match found {blue_int}, expected <=5"
        self.vcosmos.clean_up_logs()
        self.fc.swipe_window(direction="up", distance=6)
        self.navigate_from_advanced_settings()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()