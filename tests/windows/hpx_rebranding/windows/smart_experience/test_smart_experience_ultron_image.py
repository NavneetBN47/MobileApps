import logging
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    #This suite should run on Ultron devices only
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_01_presence_detection_ultron_default_illustration_C53033390(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "Presence detection is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        self.fc.fd["smart_experience"].hover_on_element("auto_screen_dimming_text_ltwo_page")       
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["smart_experience"].verify_presence_detection_image, machine_type="ultron_presence_detection_default_illustration")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline in ultron_presence_detection_default_illustration."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
