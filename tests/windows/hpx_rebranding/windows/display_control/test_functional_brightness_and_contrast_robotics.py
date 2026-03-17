import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):
   
    #this suite should run on willie /tc already seperate for bopeep AIO
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_wibrightness_C42891118(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 107, "Red value does not match"
            assert green_int >= 127, "Green value does not match"
            assert blue_int >= 72, "Blue value does not match"
            assert clear_int >= 186 , "Brightness visual clear value does not match"
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 50)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "50", "Brightness slider value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert 33 <= red_int <= 73, "Red value does not match"
            assert 42 <= green_int <= 82, "Green value does not match"
            assert 19 <= blue_int <= 59, "Blue value does not match"
            assert 68 <= clear_int <= 108, "Brightness visual clear value does not match"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 16, "Red value does not match"
            assert green_int <= 17, "Green value does not match"
            assert blue_int <= 13, "Blue value does not match"
            assert clear_int <= 22, "Brightness visual clear value does not match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_settings_brightness_C42891121(self):
        try:
            self.fc.check_and_navigate_to_display_control_page()
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(5)
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            self.fc.fd["system_control"].set_slider_value("system_setting_brightness_slider", 100)
            assert self.fc.fd["system_control"].get_system_setting_brightness_slider() == "100", "System settings brightness slider value is not 100"
            self.fc.close_windows_settings_panel()
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int >= 80, "Red value does not match"
                assert green_int >= 85, "Green value does not match"
                assert blue_int >= 50, "Blue value does not match"
                assert clear_int >= 130 , "Brightness visual clear value does not match"
            self.vcosmos.clean_up_logs()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_display_control_page()
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching after adjusting system brightness value."
            # revert back changes to default for next suite as reset or reinstall will not revert the brightness value and mode back
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        finally:
            self.fc.close_windows_settings_panel()
            self.fc.launch_myHP()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_wicontrast_C42891122(self):
        self.fc.check_and_navigate_to_display_control_page()
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
            assert red_int <= 85, "Red value does not match"
            assert green_int <= 97, "Green value does not match"
            assert blue_int <= 65, "Blue value does not match"
            assert clear_int <= 135, "The clear value is not at accepted value after reducing contrast."
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_contrast_slider_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == '100', "Contrast value is not matching."
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 97, "Red value does not match"
            assert green_int >= 97, "Green value does not match"
            assert blue_int >= 65, "Blue value does not match"
            assert clear_int >= 170, "The clear value is not at accepted value after increasing contrast."
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()