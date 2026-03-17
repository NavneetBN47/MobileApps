import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_Display_Control(object):
    
    #this suite should run on willie robotics with HDR portarit
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_hdr_on_C42891426(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        if self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()=="Select Mode":
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_default_ltwo_page")
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_default_ltwo_page")
            time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Brightness slider is not Default"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 71, "Red value doesnot match"
            assert green_int >= 83, "Green value doesnot match"
            assert blue_int >= 48, "Blue value doesnot match"
            assert clear_int >= 122, "Brightness visual doesnot match"
        self.vcosmos.clean_up_logs()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "false", "selection button is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 75, "Red value doesnot match"
            assert green_int >= 91, "Green value doesnot match"
            assert blue_int >= 53, "Blue value doesnot match"
            assert clear_int >= 132, "Brightness visual doesnot match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_control_hdr_off_C42891427(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "true", "selection button is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 69, "Red value doesnot match"
            assert green_int >= 81, "Green value doesnot match"
            assert blue_int >= 47, "Blue value doesnot match"
            assert clear_int >= 119, "Brightness visual doesnot match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_syncronization_of_windows_setting_and_hpx_C42891433(self):
        try:
            self.fc.check_and_navigate_to_display_control_page()
            self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not matching."
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int <= 13, "Red value doesnot match"
                assert green_int <= 15, "Green value doesnot match"
                assert blue_int <= 12, "Blue value doesnot match"
                assert clear_int <= 17, "brightness value doesnot match"
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            assert self.fc.fd["display_control"].get_setting_display_slider_value() == "0", "Brightness slider value is not 0"
            self.fc.fd["display_control"].set_slider_value("system_setting_brightness_slider", 100)
            assert self.fc.fd["display_control"].get_setting_display_slider_value() == "100", "Brightness slider value is not 100"
            self.fc.close_windows_settings_panel()
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int >= 79, "Red value doesnot match"
                assert green_int >= 93, "Green value doesnot match"
                assert blue_int >= 54, "Blue value doesnot match"
                assert clear_int >= 136, "Brightness visual doesnot match"
            self.vcosmos.clean_up_logs()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_display_control_page()
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching."
        finally:
            self.fc.close_windows_settings_panel()
            self.fc.launch_myHP()

    def test_04_hdr_while_battery_options_is_checked_and_on_dc_mode_C42891431(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true", "HDR toggle is disabled"
        self.vcosmos.remove_charger_and_usb()
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "false", "HDR toggle is not disabled"
        self.fc.close_myHP()
        self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_enabled_disable() == "false","HDR toggle is not disabled"
        self.vcosmos.add_charger_and_usb()

    def test_05_hdr_while_battery_options_is_unchecked_and_on_dc_mode_C42891432(self):
        try:
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_enabled_disable() == "true", "HDR toggle is not enabled"
            self.fc.close_windows_settings_panel()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_display_control_page()
            assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true", "HDR toggle is not enabled"
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        finally:
            self.fc.close_windows_settings_panel()
            self.fc.launch_myHP()

    def test_06_hdr_on_from_window_setting_C42891434(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 69, "Red value doesnot match"
            assert green_int >= 81, "Green value doesnot match"
            assert blue_int >= 47, "Blue value doesnot match"
            assert clear_int >= 119, "Brightness visual doesnot match"
        self.vcosmos.clean_up_logs()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "false", "selection button is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 75, "Red value doesnot match"
            assert green_int >= 91, "Green value doesnot match"
            assert blue_int >= 53, "Blue value doesnot match"
            assert clear_int >= 132, "Brightness visual doesnot match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        time.sleep(10)
        self.fc.close_myHP()
        self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle is on"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle is off"
        self.fc.close_windows_settings_panel()

    def test_07_hdr_off_from_window_setting_C42891435(self):
        self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle is off"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle is on"
        self.fc.close_windows_settings_panel()
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
        #  revert back changes to default for next suite as reset or reinstall will not revert the brightness value and mode back
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()