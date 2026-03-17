import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # These test cases can only be run in Bopeep due to system modes and OSD controls
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_osd_display_modes_gaming_mode_C63422700(self):
        # Step 1: Navigate to gaming mode using OSD menu with robotics
        self.vcosmos.navigate_gaming_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on lone page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Gaming", f"Display Mode incorrect, expected 'Gaming' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "84", f"Brightness slider value incorrect, expected '84' but got {current_value}."

    def test_02_osd_display_modes_neutral_mode_C42892364(self):
        # Step 1: Navigate to neutral mode using OSD menu with robotics
        self.vcosmos.navigate_neutral_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display Mode incorrect, expected 'Neutral' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "76", f"Brightness slider value incorrect, expected '76' but got {current_value}."

    def test_03_osd_display_modes_movie_mode_C42892365(self):
        # Step 1: Navigate to movie mode using OSD menu with robotics
        self.vcosmos.navigate_movie_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Movie", f"Display Mode incorrect, expected 'Movie' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "20", f"Brightness slider value incorrect, expected '20' but got {current_value}."

    def test_04_osd_display_modes_reading_mode_C42892366(self):
        # Step 1: Navigate to reading mode using OSD menu with robotics
        self.vcosmos.navigate_reading_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Reading", f"Display Mode incorrect, expected 'Reading' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "52", f"Brightness slider value incorrect, expected '52' but got {current_value}."

    def test_05_osd_display_modes_night_mode_C42892367(self):
        # Step 1: Navigate to night mode using OSD menu with robotics
        self.vcosmos.navigate_night_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Night", f"Display Mode incorrect, expected 'Night' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "28", f"Brightness slider value incorrect, expected '28' but got {current_value}."

    def test_06_osd_display_modes_hp_enhance_mode_C42892368(self):
        # Step 1: Navigate to HP Enhance mode using OSD menu with robotics
        self.vcosmos.navigate_hp_enhance_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "HP enhance+", f"Display Mode incorrect, expected 'HP enhance+' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "76", f"Brightness slider value incorrect, expected '76' but got {current_value}."

    def test_07_osd_display_modes_native_mode_C42892369(self):
        # Step 1: Navigate to Native mode using OSD menu with robotics
        self.vcosmos.navigate_native_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Display Mode incorrect, expected 'Native' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "100", f"Brightness slider value incorrect, expected '100' but got {current_value}."

    def test_08_reset_from_osd_menu_C42892370(self):
        # Step 1: Navigate to Native mode using OSD menu with robotics
        self.vcosmos.navigate_native_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Verify device card is displayed
        self.fc.check_and_navigate_to_display_control_page()

        # Step 3: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Native", f"Display Mode incorrect, expected 'Native' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "100", f"Brightness slider value incorrect, expected '100' but got {current_value}."

        #step 4: Reset to defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default()
        self.vcosmos.clean_up_logs()

        # Step 5: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Neutral", f"Display Mode incorrect, expected 'Neutral' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "76", f"Brightness slider value incorrect, expected '76' but got {current_value}."

    def test_09_osd_and_hp_app_desync_modes_C52983158(self):
        # Step 1: Close HP App
        self.fc.close_myHP()
        
        # Step 2: Navigate to night mode using OSD menu with robotics
        self.vcosmos.navigate_night_mode()
        self.vcosmos.clean_up_logs()

        # Step 3: Reopen HP App
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        time.sleep(15)

        # Step 4: Verify out of sync message and see more link then select keep changes
        if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
            self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page(), "Out of sync keep changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page(), "Out of sync discard changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page(), "Out of sync cancel button not displayed."
            self.fc.fd["display_control"].click_display_control_out_of_synch_cancel_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link(), "Out of sync message see more link not displayed."
            self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
            self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()

        # Step 5: Verify brightness control elements on ltwo page
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Night", f"Display Mode incorrect, expected 'Night' but got {current_mode}."
        current_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_value == "28", f"Brightness slider value incorrect, expected '28' but got {current_value}."

    def test_10_osd_and_hp_app_desync_rgb_C52983161(self):
        # Step 1: Close HP App
        self.fc.close_myHP()

        # Step 2: Restore factory defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default()
        self.vcosmos.clean_up_logs()
        
        # Step 3: Set RGB values to zero using OSD menu with robotics
        self.vcosmos.set_red_value_zero()
        self.vcosmos.clean_up_logs()
        self.vcosmos.set_green_value_zero()
        self.vcosmos.clean_up_logs()
        self.vcosmos.set_blue_value_zero()
        self.vcosmos.clean_up_logs()

        # Step 4: Reopen HP App and navigate to advanced Display Control settings
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        time.sleep(15)

        # Step 5: Verify out of sync message and see more link then select keep changes
        if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
            self.fc.fd["display_control"].click_display_control_advanced_settings_out_of_sync_see_more_link()
            assert self.fc.fd["display_control"].verify_display_control_advancedsettings_keep_new_changes_button_lthree_page(), "Out of sync keep changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_advancedsettings_discard_changes_button_lthree_page(), "Out of sync discard changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_advancedsettings_cancel_button_lthree_page(), "Out of sync cancel button not displayed."
            self.fc.fd["display_control"].click_display_control_advancedsettings_cancel_button_lthree_page()
            assert self.fc.fd["display_control"].verify_display_control_advanced_settings_out_of_sync_see_more_link(), "Out of sync message see more link not displayed."
            self.fc.fd["display_control"].click_display_control_advanced_settings_out_of_sync_see_more_link()
            self.fc.fd["display_control"].click_display_control_advancedsettings_keep_new_changes_button_lthree_page()

        # Step 6: Verify in app color slider values are set to zero
        current_red_value = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
        assert current_red_value == "0", f"Red value is not 0 after OSD change, actual value is {current_red_value}"
        current_green_value = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
        assert current_green_value == "0", f"Green value is not 0 after OSD change, actual value is {current_green_value}"
        current_blue_value = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
        assert current_blue_value == "0", f"Blue value is not 0 after OSD change, actual value is {current_blue_value}"