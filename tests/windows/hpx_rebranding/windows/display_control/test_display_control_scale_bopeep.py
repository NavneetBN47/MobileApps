import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control_scale(object):
    #create image verification method for this testing
    
    #this suite should run on all platform
    @pytest.mark.function
    def test_01_scale_check_C51600936(self):
        """Test ID: C51600936
        Test Case: Verify Display Control module functionality for different scale settings.
        - Bopeep
        - Keelung 32
        - Portrait platform note book
        - Non portrait platform"""

        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #click restore defaults so all values should be restored as defaults
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()

        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        #==================================================================================
        #     For Bopeep - platform, we have scale 100%, 125%, 150%, 175%, 200%, 225% as these options are available
        #     Need to validate scaling with 125% and 225%
        #==================================================================================
        try:
            for scale in ["scale_125_percent","scale_225_percent"]:
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
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page, machine_name=platform, page_number=1_1, element="display_control_text_ltwo_page", scale=scale)
                self.fc.fd["display_control"].verify_scale_image(image_compare_result, "Bopeep display control lone page", scale)
                if scale in ["scale_225_percent"]:
                    self.fc.fd["display_control"].scroll_to_element("display_control_advanced_settings_restore_defaults_button_ltwo_page")
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page, machine_name=platform, page_number=1_2, element="display_control_advanced_settings_restore_defaults_button_ltwo_page", scale=scale)
                    self.fc.fd["display_control"].verify_scale_image(image_compare_result, "Bopeep display control lone page", scale)
                    self.fc.fd["display_control"].scroll_to_element("display_control_text_ltwo_page")
                time.sleep(2)
                #click advanced settings and verify ltwo page in display control
                self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
                #verify ltwo page in display control
                if scale in ["scale_225_percent"]:
                    self.fc.swipe_window(direction="down", distance=2)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_ltwo_page, machine_name=platform, page_number=2_1, element="display_control_advanced_display_settings_title_lthree_page", scale=scale)
                self.fc.fd["display_control"].verify_scale_image(image_compare_result, "Bopeep display control ltwo page", scale)
                if scale in ["scale_225_percent"]:
                    self.fc.fd["display_control"].scroll_to_element("display_control_restore_defaults_button_lthree_page")
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_ltwo_page, machine_name=platform, page_number=2_2, element="display_control_restore_defaults_button_lthree_page", scale=scale)
                    self.fc.fd["display_control"].verify_scale_image(image_compare_result, "Bopeep display control ltwo page", scale)
                    self.fc.fd["display_control"].scroll_to_element("display_control_advanced_display_settings_title_lthree_page")
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        
        #ensure to set the scale back to 100% even if the test fails
        finally:
            if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["display_control"].set_scale_from_settings("scale_100_percent")