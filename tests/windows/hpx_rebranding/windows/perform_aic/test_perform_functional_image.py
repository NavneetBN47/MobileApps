import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):

    # #this suite should run on snow white
    # @pytest.mark.function
    # @pytest.mark.ota
    # def test_01_ai_companion_ui_C57033743(self):
    #     button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
    #     assert button_verified, "HP AI Assistant button is not visible on header"
    #     self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
    #     time.sleep(2)
    #     image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["aic"].verify_perform_aic_ltwo_page, machine_type="snowwhite_image_ltwo")
    #     # Only assert if screenshot comparison actually happened
    #     if image_compare_result is not None:
    #         assert image_compare_result, "Perform AIC L2 page image did not match the baseline."
    #     else:
    #         logging.info("No screenshot comparison performed (context manager not active)")
    #     time.sleep(2)
    #     self.fc.fd["aic"].click_aic_window(7)
    #     time.sleep(5)
    #     self.fc.fd["aic"].enter_text_in_search_box("Turn on my camera")
    #     self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
    #     self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
    #     time.sleep(5)
    #     self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
    #     time.sleep(10)
    #     image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["aic"].verify_perform_aic_ltwo_page, machine_type="snowwhite_image_ltwo_turn_on_camera_response")
    #     # Only assert if screenshot comparison actually happened
    #     if image_compare_result is not None:
    #         assert image_compare_result, "Perform AIC response L3 page image did not match the baseline."
    #     else:
    #         logging.info("No screenshot comparison performed (context manager not active)")