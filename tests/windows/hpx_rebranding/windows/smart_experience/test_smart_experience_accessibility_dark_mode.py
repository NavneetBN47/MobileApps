import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smt_Exp_Accessibility(object):
    #Should be run on MasadaNX and machu13x-below tc need to run on 2 platforms
    
    @pytest.mark.function
    def test_01_hpx_dark_mode_visibility_C51244782(self):
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        try:
            self.fc.maximize_and_verify_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_detection_card()
            assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "presence detection card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
            time.sleep(5)
            self.fc.enable_dark_mode()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_dark_mode, machine_type=platform, mode="dark_mode")
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")

        finally:
                self.fc.disable_dark_mode()

    @pytest.mark.function
    def test_02_hpx_disable_dark_mode_visibility_C51244783(self):
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        self.fc.disable_dark_mode()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_dark_mode, machine_type=platform, mode="disable_dark_mode")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")