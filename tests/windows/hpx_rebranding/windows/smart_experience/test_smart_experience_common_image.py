import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    #this test case is for masadansku5
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_default_illustration_C53032399(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_presence_detection_image, machine_type="masadan_presence_detection_default_illustration")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline in masadan_presence_detection_default_illustration."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_restore_default_for_illustration_gif_C51244838(self):
        time.sleep(2)        
        self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_presence_detection_image, machine_type="masadan_hover_on_auto_hdr_default_illustration")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline in masadan_hover_on_auto_hdr_default_illustration."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        time.sleep(2)
        self.fc.fd["smart_experience"].get_focus_on_app("onlooker_detection_text_ltwo_page")
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_presence_detection_image, machine_type="masadan_hover_on_onlooker_detection_default_illustration")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline in masadan_hover_on_onlooker_detection_default_illustration."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        time.sleep(2)
        self.fc.fd["smart_experience"].click_restore_default_button_ltwo_page()
