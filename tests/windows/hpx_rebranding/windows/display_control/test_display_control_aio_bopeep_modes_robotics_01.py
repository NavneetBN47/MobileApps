import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # Test cases is to verify the functionality of display control in Native mode and contrast settings on Bopeep
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_renavigate_native_mode_C61425786(self):
        # Step 1: Navigate to Display Control page
        self.fc.check_and_navigate_to_display_control_page()

        # Step 2:Reverting any changes from previous TC
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)

        # Step 3: Verify brightness control elements on L2 page and display mode is Native
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_last_display_mode()
        if self.fc.fd["display_control"].verify_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")=="Native" and self.fc.fd["display_control"].is_item_onscreen("display_modes_select_box_option_native_ltwo_page") == True:
            self.fc.fd["display_control"].click_title_bar()
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        else:
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Brightness slider is not Native, expected 'Native' but got {current_mode}."
        # Step 4: Verify initial brightness value (should be 100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()

        # Step 5: Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 110 <= clear_int <= 150, f"Clear value is not matching, expected between 110 and 150, got {clear_int}"

        # Step 6: Clean up logs after verification
        self.vcosmos.clean_up_logs()

        # Step 7: Decrease brightness to 80
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 80)
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "80", f"Brightness slider value is not 80, got '{current_value}'"

        # Step 8: Toggle contrast and verify default value
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        current_value = self.fc.fd["display_control"].get_contrast_slider_value()
        assert current_value == "100", f"Contrast slider value is not 100, expected '100' but got '{current_value}'"

        # Step 9: Decrease contrast to 80
        self.fc.fd["display_control"].set_slider_value("display_control_contrast_slider_ltwo_page", 80)
        self.vcosmos.get_red_green_blue_clear_value()

        # Step 10: Verify LED values again after slider change
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 70 <= clear_int <= 110, f"The clear value should be between 70 and 110 after reducing brightness, got {clear_int}."
        self.vcosmos.clean_up_logs()

        # Step 11: navigate to other display mode
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_movie_ltwo_page")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Movie", f"Brightness slider is not Movie, expected 'Movie' but got {current_mode}."
        self.vcosmos.get_red_green_blue_clear_value()

        # Step 12:Verify LED values again after display mode change
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 70, f"The clear value should be below 70 after reducing changing modes, got {clear_int}."
        self.vcosmos.clean_up_logs()

        # Step 13: navigate back to Native display mode
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Brightness slider is not Native, expected 'Native' but got {current_mode}."

        # Step 14:Verify LED brightness and contrast slider and toggle values
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "80", "Brightness slider value is not 80"
        assert self.fc.fd["display_control"].get_contrast_slider_value() == "80", "Contrast slider value is not 80"
        self.vcosmos.get_red_green_blue_clear_value()

        # Step 15:Verify LED values again after returning to Native mode
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert 70 <= clear_int <= 110, f"The clear value should be between 70 and 110 after returning to Native display mode, got {clear_int}."
        self.vcosmos.clean_up_logs()

       # Reverting any changes
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_contrast_minimum_value_relaunch_C42891128(self):
        # Step 1: Renavigate to Display Control page
        self.fc.check_and_navigate_to_display_control_page()

        # Step 2: Reverting any changes from previous TC
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)

        # Step 3: Verify brightness control elements on L2 page and display mode is Native
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_last_display_mode()
        if self.fc.fd["display_control"].verify_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")=="Native" and self.fc.fd["display_control"].is_item_onscreen("display_modes_select_box_option_native_ltwo_page") == True:
            self.fc.fd["display_control"].click_title_bar()
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Brightness slider is not Native, expected 'Native' but got {current_mode}."

        # Step 4: Toggle contrast and verify default value
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        current_value = self.fc.fd["display_control"].get_contrast_slider_value()
        assert current_value == "100", f"Contrast slider value is not 100, expected '100' but got '{current_value}'"

        # Step 5: Verify LED values before slider change
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 100, f"The clear value should be greater than or equal to 100 before adjusting contrast, got {clear_int}."
        self.vcosmos.clean_up_logs()

        # Step 6: Decrease contrast to 80
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_contrast_slider_ltwo_page", 0, 0, 100)

        # Step 7: Verify LED values again after slider change
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 18, f"The clear value should be less than or equal to 18 after adjusting contrast, got {clear_int}."
        self.vcosmos.clean_up_logs()

        # Step 8: relaunch HP app and navigate to Display Control page
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()

         # Step 9: Verify brightness control elements on L2 page and display mode is Native
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Brightness slider is not Native, expected 'Native' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_contrast_slider_value()
        assert current_value == "0", f"Contrast slider value is not 0, expected '0' but got '{current_value}'"

        # Step 10: Verify LED values again after relaunch
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int <= 18, f"The clear value should be less than or equal to 18 after adjusting contrast, got {clear_int}."
        self.vcosmos.clean_up_logs()

        # Reverting any changes
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)