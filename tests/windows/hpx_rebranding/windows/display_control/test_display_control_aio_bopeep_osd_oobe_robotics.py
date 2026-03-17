import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe_robotics")
class Test_Suite_Display_Control(object):

    # These test cases can only be run in Bopeep due to OSD controls
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_oobe_application_osd_sync_rgb_C42891327(self):
        try:
            # Step 1: Navigate to and verify Disney + app settings in Display Control
            self.fc.check_and_navigate_to_display_control_page()
            # Restore all apps default values in case of previous case failure
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(20)
            assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
            assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
            assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            time.sleep(5)
            assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
            # Restore Disney + default values in case of previous case failure
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(20)
            current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
            assert current_mode == "Movie", f"Display mode is not Movie, actual value is {current_mode}"

            # Step 2: Set display mode to Neutral using OSD menu with robotics
            self.vcosmos.navigate_neutral_mode()
            self.vcosmos.clean_up_logs()

            # Step 3: Verify Neutral mode and Disney + app retains selection
            assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected after OSD change"
            current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
            assert current_mode == "Neutral", f"Display mode is not Neutral after oobe change, actual value is {current_mode}"

            # Step 4: Navigate to advanced settings and verify RGB values
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"

            # Step 5: Set RGB values to zero using OSD menu with robotics
            self.vcosmos.set_red_value_zero()
            self.vcosmos.clean_up_logs()
            self.vcosmos.set_green_value_zero()
            self.vcosmos.clean_up_logs()
            self.vcosmos.set_blue_value_zero()
            self.vcosmos.clean_up_logs()

            # Step 6: Verify Disney + retains selection and color value adjustment using robotics LED bot
            assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected after OSD change"
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0 after OSD change"
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0 after OSD change"
            assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0 after OSD change"
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

            # Step 7: close HP app and open Disney+ app to verify rgb values are retained
            self.fc.close_myHP()
            self.fc.fd["display_control"].launch_all_apps("Disney+")
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert clear_int <= 14, f"Clear value is not less than or equal to 14, actual value: {clear_int}"
                assert red_int <= 12, f"Red value is not less than or equal to 12, actual value: {red_int}"
                assert green_int <= 13, f"Green value is not less than or equal to 13, actual value: {green_int}"
                assert blue_int <= 10, f"Blue value is not less than or equal to 10, actual value: {blue_int}"
        finally:
            self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)

    def test_02_oobe_with_osd_and_hp_app_closed_C42891328(self):
        try:
            # Step 1: Navigate to and verify Disney + app settings in Display Control
            self.fc.check_and_navigate_to_display_control_page()
            # Restore all apps default values in case of previous case failure
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(20)
            assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
            assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
            assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            time.sleep(5)
            assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
            # Restore Disney + default values in case of previous case failure
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
            time.sleep(20)
            current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
            assert current_mode == "Movie", f"Display mode is not Movie, actual value is {current_mode}"

            # Step 2: Close HP App and open Disney+ app
            self.fc.close_myHP()
            self.fc.fd["display_control"].launch_all_apps("Disney+")

            # Step 3: Set display mode to Neutral using OSD menu with robotics
            self.vcosmos.navigate_neutral_mode()
            self.vcosmos.clean_up_logs()

            # Step 4: Set RGB values to zero using OSD menu with robotics
            self.vcosmos.set_red_value_zero()
            self.vcosmos.clean_up_logs()
            self.vcosmos.set_green_value_zero()
            self.vcosmos.clean_up_logs()
            self.vcosmos.set_blue_value_zero()
            self.vcosmos.clean_up_logs()

            # Step 5: Verify color value adjustment using robotics LED bot
            self.vcosmos.get_red_green_blue_clear_value()
            red, green, blue, clear = self.vcosmos.verify_led_values()
            if red is not None and green is not None and blue is not None and clear is not None:
                clear_int = int(clear)
                red_int = int(red)
                green_int = int(green)
                blue_int = int(blue)
                assert clear_int <= 14, f"Clear value is not less than or equal to 14, actual value: {clear_int}"
                assert red_int <= 12, f"Red value is not less than or equal to 12, actual value: {red_int}"
                assert green_int <= 13, f"Green value is not less than or equal to 13, actual value: {green_int}"
                assert blue_int <= 10, f"Blue value is not less than or equal to 10, actual value: {blue_int}"
            self.vcosmos.clean_up_logs()

            # Step 6: Close Disney + and Reopen HP App and verify settings are retained
            self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)        
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            if "Restore HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            time.sleep(10)
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
            assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
            assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            time.sleep(5)
            assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
            current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
            assert current_mode == "Neutral", f"Display mode is not Neutral after oobe change, actual value is {current_mode}"
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
            current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
            assert current_red_value == "0", f"Red value is not 0 after OSD change, actual value is {current_red_value}"
            current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
            assert current_green_value == "0", f"Green value is not 0 after OSD change, actual value is {current_green_value}"
            current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
            assert current_blue_value == "0", f"Blue value is not 0 after OSD change, actual value is {current_blue_value}"
        finally:
            self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)