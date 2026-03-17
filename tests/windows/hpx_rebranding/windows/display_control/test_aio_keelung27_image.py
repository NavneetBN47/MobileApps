import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
#The baseline images are taken from keelung 27, so need to run against that.
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_DisplayControl_Images(object):

    # def test_figma_C53000435(self):
    #     self.fc.maximize_and_verify_device_card()
    #     self.fc.swipe_window(direction="down", distance=6)
    #     self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
    #     self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
    #     self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
    #     image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_control_card_lone_image, machine_type="keelung27")
    #     # Only assert if screenshot comparison actually happened
    #     if image_compare_result is not None:
    #         assert image_compare_result, "LOne image did not match the baseline."
    #     else:
    #         logging.info("No screenshot comparison performed (context manager not active)")
    #     #click advanced display settings
    #     self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
    #     time.sleep(2)
    #     self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
    #     self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    #     image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_control_card_ltwo_page, machine_type="keelung27")
    #     # Only assert if screenshot comparison actually happened
    #     if image_compare_result is not None:
    #         assert image_compare_result, "Advanced settings image did not match the baseline."
    #     else:
    #         logging.info("No screenshot comparison performed (context manager not active)")
