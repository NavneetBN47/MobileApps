import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # These test cases can only be run in Bopeep due to OSD controls
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_osd_rgb_adjustment_visual_sync_C42892363(self):

        # Step 1: Navigate to Display Control page
        self.fc.check_and_navigate_to_display_control_page()

        # Step 1: Restore factory defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default()
        self.vcosmos.clean_up_logs()

        # Step 2: Set RGB values to zero using OSD menu with robotics
        self.vcosmos.set_red_value_zero()
        self.vcosmos.clean_up_logs()
        self.vcosmos.set_green_value_zero()
        self.vcosmos.clean_up_logs()
        self.vcosmos.set_blue_value_zero()
        self.vcosmos.clean_up_logs()

        # Step 3: Verify Blue value adjustment using robotics LED bot
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 13, f"Red value is not less than or equal to 13, actual value: {red_int}"
            assert green_int <= 15, f"Green value is not less than or equal to 15, actual value: {green_int}"
            assert blue_int <= 12, f"Blue value is not less than or equal to 12, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()

    def test_02_osd_rgb_adjustment_slider_sync_C42892371(self):

        # Step 1: Verify device card is still displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 2: Navigate to advanced display settings page
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()

        # Step 3: Verify RGB elements on lthree page
        red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert red_value == "0", f"Red value is not 0, actual value: {red_value}"
        green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert green_value == "0", f"Green value is not 0, actual value: {green_value}"
        blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert blue_value == "0", f"Blue value is not 0, actual value: {blue_value}"

    def test_03_osd_rgb_adjustment_hp_enhance_C42892372(self):
        # Step 1: Navigate to HP Enhance mode using OSD menu with robotics
        self.vcosmos.navigate_hp_enhance_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify rgb slider controls are not present on lthree page
        assert not self.fc.fd["display_control"].verify_display_control_low_blue_light_red_slider_lthree_page(), "Red slider is present on lthree page"
        assert not self.fc.fd["display_control"].verify_display_control_low_blue_light_green_slider_lthree_page(), "Green slider is present on lthree page"
        assert not self.fc.fd["display_control"].verify_display_control_low_blue_light_blue_slider_lthree_page(), "Blue slider is present on lthree page"

        # Step 5: Restore factory defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default()
        self.vcosmos.clean_up_logs()