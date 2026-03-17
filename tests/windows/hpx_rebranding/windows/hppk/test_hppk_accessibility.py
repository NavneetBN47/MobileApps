import logging
import pytest
import time
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Accessibility(object):
    #Run these on London 

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_colour_filter_grayscale_C42901071(self):
        try:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["hppk"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_hppk_card()
            assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["hppk"].verify_color_filter)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["hppk"].revert_system_color_filter()    
