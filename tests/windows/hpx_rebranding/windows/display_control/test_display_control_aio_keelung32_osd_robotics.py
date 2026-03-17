import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # These test cases can only be run on Keelung 32 with Joystick Robotics due to OSD controls
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_osd_joystick_button_C51248487(self):

        # Step 0: Navigate to Display Control page
        self.fc.check_and_navigate_to_display_control_page()

        # Step 1: Restore factory defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "P3 (D65)", f"Display mode is not P3 (D65), actual mode is: {current_mode}"

        # Step 2: Change display modes to each mode available and validate changes in app
        self.vcosmos.navigate_neutral_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display mode is not Neutral, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_warm_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Warm", f"Display mode is not Warm, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_cool_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Cool", f"Display mode is not Cool, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_hp_enhance_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "HP enhance+", f"Display mode is not HP enhance+, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_native_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Display mode is not Native, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_srgb_d65_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "sRGB D65", f"Display mode is not sRGB D65, actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()
        self.vcosmos.navigate_bt709_d65_mode_keelung32()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "BT709 (D65)", f"Display mode is not BT709 (D65), actual mode is: {current_mode}"
        self.vcosmos.restore_factory_default_keelung32()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_osd_joystick_button_left_sync_C51248491(self):

        # Step 0: reset display settings to factory defaults and close HP app
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        self.fc.close_myHP()

        # Step 2: change mode using joystick left button with robotics
        self.vcosmos.navigate_warm_mode_keelung32()

        # Step 3: relaunch myHP and verify mode change
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Warm", f"Display mode is not Warm, actual mode is: {current_mode}"
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_osd_joystick_hdmi_feature_C51248595(self):
        try:
            # Step 1: Restore factory defaults using OSD menu with robotics
            self.vcosmos.restore_factory_default_keelung32()

            # Step 2: switch to HDMI input from Weller and verify RGB
            self.vcosmos.switch_to_hdmi_input_keelung32()
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert 25 <= red_int <= 45, f"Red value is not greater than 25 or less than 45, actual value: {red_int}"
                assert 3 <= green_int <= 23, f"Green value is not greater than 3 or less than 23, actual value: {green_int}"
                assert blue_int <= 10, f"Blue value is not less than or equal to 10, actual value: {blue_int}"

        finally:
            # Step 3: Return to PC input defaults using OSD menu with robotics
            time.sleep(20) # wait to ensure OSD menu is closed
            self.vcosmos.switch_to_pc_input_keelung32()