import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    # These test cases can only be run in Bopeep due to system modes and OSD controls
    @pytest.mark.function
    def test_01_osd_reset_desync_C52983163(self):
        # Step 1: Navigate to Gaming mode using OSD menu with robotics
        self.vcosmos.navigate_gaming_mode()
        self.vcosmos.clean_up_logs()

        # Step 2: Close HP App
        self.fc.close_myHP()

        # Step 3: Restore factory defaults using OSD menu with robotics
        self.vcosmos.restore_factory_default()
        self.vcosmos.clean_up_logs()

        # Step 4: Reopen HP App and navigate to Display Control settings
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()

        # Step 5: Verify out of sync message and see more link then select keep changes
        if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
            self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page(), "Out of sync keep changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page(), "Out of sync discard changes button not displayed."
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page(), "Out of sync cancel button not displayed."
            self.fc.fd["display_control"].click_display_control_out_of_synch_cancel_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link(), "Out of sync message see more link not displayed."
            self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
            self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()

        # Step 6: Verify application settings properly reflect OSD settings
        brightness_text_ltwo_page = self.fc.fd["display_control"].verify_display_control_brightness_text_ltwo_page()
        assert brightness_text_ltwo_page == "Brightness", "Brightness text is not present."
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_osd_brightness_slider_C52983148(self):
        try:
            # Step 1: Close HP App
            self.fc.close_myHP()

            # Step 2: Restore factory defaults using OSD menu with robotics
            self.vcosmos.restore_factory_default()
            self.vcosmos.clean_up_logs()

            # Step 3: Adjust brightness to 0 using OSD menu with robotics
            self.vcosmos.set_brightness_value_zero()
            self.vcosmos.clean_up_logs()

            # Step 4: Reopen HP App and navigate to Display Control settings
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            if "Restore HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            time.sleep(10)
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(15)

            # Step 5: Verify out of sync message and see more link then select keep changes
            if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
                self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
                assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page(), "Out of sync keep changes button not displayed."
                assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page(), "Out of sync discard changes button not displayed."
                assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page(), "Out of sync cancel button not displayed."
                self.fc.fd["display_control"].click_display_control_out_of_synch_cancel_button_ltwo_page()
                assert self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link(), "Out of sync message see more link not displayed."
                self.fc.fd["display_control"].click_display_control_out_of_sync_see_more_link()
                self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()

            # Step 6: Verify application settings properly reflect OSD settings
            brightness_text_ltwo_page = self.fc.fd["display_control"].verify_display_control_brightness_text_ltwo_page()
            assert brightness_text_ltwo_page == "Brightness", "Brightness text is not present."
            assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        finally:
            #restore defaults and close app
            self.vcosmos.restore_factory_default()
            self.vcosmos.clean_up_logs()