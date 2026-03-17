import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):
    
    #this suite should run on non portrait systems. currently we have thompson ftc robotics setup
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_syncronization_of_windows_setting_and_hpx_C52975792(self):
        try:
            self.fc.check_and_navigate_to_display_control_page()
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(5)
            assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
            self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not matching."
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int <= 59, f"Red value does not match expected <=59 but got {red_int}"
                assert green_int <= 63, f"Green value does not match expected <=63 but got {green_int}"
                assert blue_int <= 48, f"Blue value does not match expected <=48 but got {blue_int}"
                assert clear_int <= 78, f"Brightness value does not match expected <=78 but got {clear_int}"
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "0", "Brightness slider value is not 0"
            self.fc.fd["display_control"].set_slider_value("system_setting_brightness_slider", 100)
            assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "100", "Brightness slider value is not 100"
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle is off"
            self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle is on"
            self.fc.close_windows_settings_panel()
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int >= 540, f"Red value does not match expected >=540 but got {red_int}"
                assert green_int >= 600, f"Green value does not match expected >=600 but got {green_int}"
                assert blue_int >= 400, f"Blue value does not match expected >=400 but got {blue_int}"
                assert clear_int >= 800, f"Brightness visual does not match expected >=800 but got {clear_int}"
            self.vcosmos.clean_up_logs()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_display_control_page()
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching."
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
            # revert back changes to default for next suite as reset or reinstall will not revert the brightness value and mode back
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        finally:
            self.fc.close_windows_settings_panel()
            self.fc.launch_myHP()

    def test_02_hdr_off_from_window_setting_C52975795(self):
        try:
            self.fc.check_and_navigate_to_display_control_page()
            self.fc.fd["devicesMFE"].minimize_app()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
            self.fc.close_windows_settings_panel()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int >= 490, f"Red value does not match expected >=490 but got {red_int}"
                assert green_int >= 530, f"Green value does not match expected >=530 but got {green_int}"
                assert blue_int >= 330, f"Blue value does not match expected >=330 but got {blue_int}"
                assert clear_int >= 710, f"Brightness visual does not match expected >=710 but got {clear_int}"
            self.vcosmos.clean_up_logs()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle is on"
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int <= 530, f"Red value does not match expected <=530 but got {red_int}"
                assert green_int <= 580, f"Green value does not match expected <=580 but got {green_int}"
                assert blue_int <= 390, f"Blue value does not match expected <=390 but got {blue_int}"
                assert clear_int <= 750, f"Brightness visual does not match expected <=750 but got {clear_int}"
            self.vcosmos.clean_up_logs()
        finally:
            self.fc.close_windows_settings_panel()

    def test_03_hdr_on_from_window_setting_C52975796(self):
        try:
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle is on"
            self.fc.close_windows_settings_panel()
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int <= 530, f"Red value does not match expected <=530 but got {red_int}"
                assert green_int <= 580, f"Green value does not match expected <=580 but got {green_int}"
                assert blue_int <= 390, f"Blue value does not match expected <=390 but got {blue_int}"
                assert clear_int <= 750, f"Brightness visual does not match expected <=750 but got {clear_int}"
            self.vcosmos.clean_up_logs()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_display_control_page()
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert red_int >= 490, f"Red value does not match expected >=490 but got {red_int}"
                assert green_int >= 530, f"Green value does not match expected >=530 but got {green_int}"
                assert blue_int >= 330, f"Blue value does not match expected >=330 but got {blue_int}"
                assert clear_int >= 710, f"Brightness visual does not match expected >=710 but got {clear_int}"
            self.vcosmos.clean_up_logs()
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-Process "ms-settings:display"', timeout = 10)
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle is off"
            self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle is on"
            self.fc.close_windows_settings_panel()
        finally:
            self.fc.close_windows_settings_panel()