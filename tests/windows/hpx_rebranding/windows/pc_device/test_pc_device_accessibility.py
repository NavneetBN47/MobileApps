import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
#This suite should be run on masadansku5 platform
class Test_Suite_PC_Device_Commercial_Accessibility_UI(object):

    def verify_images(self, image_compare_result, image_name, percentage):
        logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")


    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.require_platform(["not available"])
    def test_01_verify_pc_device_module_increase_text_size_C53103678(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show_image, machine_name=platform, page_number=1, element="audio_control_card_lone_page", text_size=225)
            self.verify_images(image_compare_result, "Audio Control Card", 225)

            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=17)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_product_number_show_image, machine_name=platform, page_number=2, element="product_number", text_size=225)
            self.verify_images(image_compare_result, "PC device product number", 225)

        finally: 
            self.fc.fd["wellbeing"].update_text_size_in_system_settings(100)