import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    #new Keelung32 with 100 display scale. 
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_display_modes_p3d65_modes_C51248477(self):
        #clean up any logs that might be present before test
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Brightness slider is not P3(D65)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 728, f"Clear value was not greater than 728. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0 , 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 79, f"Clear value was not less than 79. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_display_modes_bt79d65_modes_C51248476(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "BT709 (D65)", "Brightness slider is not BT709 (D65))"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "6", "Brightness slider value is not 6"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 79, f"Clear value was not less than 79. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 728, f"Clear value was not greater than 728. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_display_modes_srgbd65_modes_C51248475(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB D65", "Brightness slider is not sRGB(D65)"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 300, f"Clear value was not greater than 300, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 728, f"Clear value was not greater than 728, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 79, f"Clear value was not less than 79. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_display_modes_native_modes_C51248474(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page_keelung32")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Selected dropdown item is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 820, f"Clear value was not greater than 820, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 86, f"Clear value was not less than 86, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_display_modes_hpenhance_modes_C51248473(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page_keelung32")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "HP enhance+", "Brightness slider is not HP enhance+"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 300, f"Clear value was not greater than 300, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 722, f"Clear value was not greater than 722, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 79, f"Clear value was not less than 79, actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_display_modes_cool_modes_C51248472(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_cool_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_cool_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Cool", "Brightness slider is not cool"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "22", "Brightness slider value is not 22"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 157, f"Clear value was not greater than 157. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 580, f"Clear value was not greater than 580. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 67, f"Clear value was not less than 67. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_07_display_modes_warm_modes_C51248471(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_warm_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_warm_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Warm", "Brightness slider is not Warm"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "6", "Brightness slider value is not 6"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 88, f"Clear value was not greater than 88. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 81, f"Clear value was not less than 81. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 755, f"Clear value was not greater than 755. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_08_modes_neutral_C51248469(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_neutral_ltwo_page_keelung32")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_neutral_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 300, f"Clear value was greater than 300. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 735, f"Clear value was not greater than 735. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 79, f"Clear value was not less than 79. Actual value: {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()