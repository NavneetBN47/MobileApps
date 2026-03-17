import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control_scale(object):
    
    #this suite should run on all platform
    @pytest.mark.function
    def test_01_scale_check_C51600936(self):
        """Test ID: C51600936
        Test Case: Verify Display Control module functionality for different scale settings.
        - Bopeep
        - Keelung 32
        - Portrait platform note book
        - Non portrait platform"""
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")

        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #need to restore all values to default before starting the test
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(2)
        #==================================================================================
        #     For testudo - Portrait platform, we have scale 100%, 125%, 150%, 175%, 200% as these options are available
        #     need to test with 150% and 200%
        #==================================================================================
        
        try:
            for scale in ["scale_150_percent","scale_200_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["display_control"].set_scale_from_settings(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                time.sleep(2)
                for _ in range(3):
                    if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                        break
                    else:
                        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

                if self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page():
                    self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
                    self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page, machine_name=platform, page_number = 1, element="display_control_text_ltwo_page",scale=scale)
                self.fc.fd["display_control"].verify_scale_image(image_compare_result, "testudo display control lone page", scale)
                time.sleep(2)              

        #ensure to set the scale back to 125% even if the test fails
        finally:
            if self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display":
                self.fc.fd["devicesMFE"].click_minimize_app()
            time.sleep(2)
            self.fc.fd["display_control"].set_scale_from_settings("scale_125_percent")
