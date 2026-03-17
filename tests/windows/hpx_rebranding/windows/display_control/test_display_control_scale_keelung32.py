import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Display_Control_scale(object):
    
    #this suite should run on all platform
    @pytest.mark.function
    def test_01_scale_check_C51600936(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #click restore default to restore all default values
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        """Test ID: C51600936
        Test Case: Verify Display Control module functionality for different scale settings.
        - Bopeep
        - Keelung 32
        - Portrait platform note book
        - Non portrait platform"""
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        #==================================================================================
        #     For Keelung32 - platform, we have scale 100%, 125%, 150%, 175%, 200%, 225%, 250%, 300%, 350% as these options are available
        #     Need to test with 150% and 350%
        #==================================================================================
        
        try:
            for scale in ["scale_150_percent","scale_350_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["display_control"].set_scale_from_settings(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                for _ in range(3):
                    if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                        break
                    else:
                        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page, machine_name=platform, page_number = 1_1, element="display_control_text_ltwo_page",scale=scale)
                self.fc.fd["display_control"].verify_scale_image(image_compare_result, "keelung32 display control lone page", scale)
                if scale in ["scale_350_percent"]:
                    self.fc.fd["display_control"].scroll_up_down(distance=5,direction="down")                    
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page, machine_name=platform, page_number = 1_2, element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale=scale)
                    self.fc.fd["display_control"].verify_scale_image(image_compare_result, "keelung32 display control lone page", scale)
                    
                #click advanced settings and verify ltwo page in display control
                self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
                #verify ltwo page in display control
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_ltwo_page, machine_name=platform, page_number = 2_1, element="display_control_advanced_display_settings_title_lthree_page",scale=scale)
                self.fc.fd["display_control"].verify_scale_image(image_compare_result, "keelung32 display control ltwo page", scale)
                if scale in ["scale_350_percent"]:
                    self.fc.fd["display_control"].scroll_up_down(distance=5,direction="down") 
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_ltwo_page, machine_name=platform, page_number = 2_2, element="display_control_restore_defaults_button_lthree_page",scale=scale)
                    self.fc.fd["display_control"].verify_scale_image(image_compare_result, "keelung32 display control ltwo page", scale)
                    self.fc.fd["display_control"].scroll_up_down(distance=12,direction="up") 
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        
        #ensure to set the scale back to 150% even if the test fails
        finally:
            if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                self.fc.fd["devicesMFE"].click_minimize_app()
            time.sleep(2)
            self.fc.fd["display_control"].set_scale_from_settings("scale_150_percent")
