import pytest
import logging
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):
    
    #this suite should be Consumer platform thompson
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_and_hdr_on_C52975786(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #click restore so all modes and slider values restored as defaults
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page()
        time.sleep(5)
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_control_card_lone_image,machine_type="thompson_hdr_on")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_control_and_hdr_off_C52975787(self):
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_off_btn_ltwo_page()
        time.sleep(5)
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_control_card_lone_image,machine_type="thompson_hdr_off")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
