import logging
import pytest
import time
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Battery_Accessibility(object):
    # Should be run on MasadaNX
    
    def verify_images(self,image_compare_result,image):
        if image_compare_result is not None:
            assert image_compare_result, f"{image} image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_magnifier_battery_C60186377(self):
        try:
            platform=self.platform.lower()
            logging.info(f"Starting battery manageability test for platform: {platform}")
            self.fc.maximize_and_verify_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            time.sleep(2)
            
            self.fc.fd["battery"].zoom_in()
            self.fc.fd["battery"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["battery"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_magnifier, machine_type=platform, percent="200")
            self.verify_images(image_compare_result, "verify_magnifier_200")
            self.fc.fd["battery"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_magnifier, machine_type=platform, percent="100")
            self.verify_images(image_compare_result, "verify_magnifier_100")
        finally:
            self.fc.fd["battery"].close_magnifier()
            self.fc.close_myHP()