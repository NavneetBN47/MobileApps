import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    #TC is specifically can only be ran in Bopeep due to system modes, All the clear value has 5 difference to validate if brightness value is between 0 to 100 in UI.
    #System will restart and install new build and restore t0 default modes,values before tc run.
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_display_modes_neutral_modes_C42892093(self):
        # Step 1: Navigate to Display Control page
        self.fc.check_and_navigate_to_display_control_page()

        # Step 2: Removing any changes coming from previous TC
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)

        # Step 3: Verify brightness control elements on L2 page
        brightness_text_ltwo_page = self.fc.fd["display_control"].verify_display_control_brightness_text_ltwo_page()
        assert brightness_text_ltwo_page == "Brightness", "Brightness text is not present."
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        # Step 4: Verify initial brightness value (should be 76)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.vcosmos.get_red_green_blue_clear_value()
        # Step 5: Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
        # Verify the clear value is within the expected range
            clear_int = int(clear)
            assert 96 <= clear_int <= 116, "Clear value is not matching"
        # Step 6: Clean up logs after verification
        self.vcosmos.clean_up_logs()
        # Step 7: Decrease brightness to 0
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Step 8: Verify LED values again after slider change
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
        # Verify that the clear value is below 20 after the decrease in brightness
            clear_int = int(clear)
            assert clear_int <= 27, "The clear value should be below 27 after reducing brightness."
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_display_modes_gaming_modes_C42892094(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_gaming_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "84", "Brightness slider value is not 84"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 94 <= clear_int <= 114, f"Brightness visual is not between 94 and 114, value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 109, f"Brightness visual is not >= 109, value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 26, f"The clear value is not below 26 after reducing brightness, value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_display_modes_reading_modes_C42892095(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_reading_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_reading_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Reading", "Brightness slider is not Reading"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "52", "Brightness slider value is not 52"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 55 <= clear_int <= 75, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 96, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 24, "The clear value is not below 24 after reducing brightness."
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_display_modes_night_modes_C42892096(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_night_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_night_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Night", "Brightness slider is not Night"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "28", "Brightness slider value is not 28"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 19 <= clear_int <= 39, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 62, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 19, "The clear value is not below 19 after reducing brightness."
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_display_modes_movie_modes_C42892097(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_movie_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_movie_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "20", "Brightness slider value is not 20"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 30 <= clear_int <= 50, f"Brightness visual is not between 30 and 50, value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 110, f"Brightness visual is not >= 110, value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 26, f"The clear value is not below 26 after reducing brightness, value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_display_modes_hpenhance_modes_C42892098(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "HP enhance+", "Brightness slider is not HP enhance+"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 88 <= clear_int <= 118, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 110, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 27, "The clear value is not below 27 after reducing brightness."
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_07_display_modes_native_modes_C42892099(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 112, f"Brightness visual is not >= 112, value is {clear_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 26, f"Brightness visual is not <= 26, value is {clear_int}"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_08_modes_navigate_C42892100(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 96 <= clear_int <= 116, "Clear value is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_gaming_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "84", "Brightness slider value is not 84"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 85 <= clear_int <= 125, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_reading_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_reading_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Reading", "Brightness slider is not Reading"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "52", "Brightness slider value is not 52"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 55 <= clear_int <= 75, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_night_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_night_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Night", "Brightness slider is not Night"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "28", "Brightness slider value is not 28"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 19 <= clear_int <= 39, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_movie_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_movie_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "20", "Brightness slider value is not 20"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 34 <= clear_int <= 54, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 111, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()