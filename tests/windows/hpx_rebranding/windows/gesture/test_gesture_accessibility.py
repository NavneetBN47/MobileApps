import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

# run on snowwhite platform
@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Gesture_Accessibility_UI(object):

    def verify_images(self, image_compare_result, image_name, percentage=None, color=None):
        if percentage:
            logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        elif color:
            logging.info(f"Image comparison result at {color}% color filter: {image_compare_result}")

        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")


    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.require_platform(["not available"])
    def test_01_verify_gesture_module_increase_text_size_C51909732(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card_with_large_text_size()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_gesture_card_title_show_image, machine_name=platform, page_number=1, element="gesture_card_title", text_size=225)
            self.verify_images(image_compare_result, "gesture card title", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_pause_resume_description_container_show_image, machine_name=platform, page_number=2, element="pause_resume_description_container", text_size=225)
            self.verify_images(image_compare_result, "pause resume description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_volume_adjust_description_container_show_image, machine_name=platform, page_number=3, element="volume_adjust_description_container", text_size=225)
            self.verify_images(image_compare_result, "volume adjust description container", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=10)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_page_scroll_description_container_show_image, machine_name=platform, page_number=4, element="page_scroll_description_container", text_size=225)
            self.verify_images(image_compare_result, "page scroll description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_photo_scroll_description_container_show_image, machine_name=platform, page_number=5, element="photo_scroll_description_container", text_size=225)
            self.verify_images(image_compare_result, "photo scroll description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_feedback_message_description_show_image, machine_name=platform, page_number=6, element="feedback_message_description", text_size=225)
            self.verify_images(image_compare_result, "feedback message description", 225)


        finally: 
            self.fc.fd["gestures"].update_text_size_in_system_settings(100)

    def test_02_verify_magnify_gesture_module_C51909741(self):
        try:
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
            time.sleep(2)
            self.fc.fd["gestures"].click_search_bar_on_windows()
            self.fc.fd["gestures"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["gestures"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["gestures"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_pause_resume_description_container_show_image, machine_name=platform, page_number=7, element="pause_resume_description_container", text_size=225)
            self.verify_images(image_compare_result, "pause resume description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_volume_adjust_description_container_show_image, machine_name=platform, page_number=8, element="volume_adjust_description_container", text_size=225)
            self.verify_images(image_compare_result, "volume adjust description container", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=10)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_page_scroll_description_container_show_image, machine_name=platform, page_number=9, element="page_scroll_description_container", text_size=225)
            self.verify_images(image_compare_result, "page scroll description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_photo_scroll_description_container_show_image, machine_name=platform, page_number=10, element="photo_scroll_description_container", text_size=225)
            self.verify_images(image_compare_result, "photo scroll description container", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_feedback_message_description_show_image, machine_name=platform, page_number=11, element="feedback_message_description", text_size=225)
            self.verify_images(image_compare_result, "feedback message description", 225)

        finally:
            self.fc.fd["gestures"].close_magnifier()


    @pytest.mark.ota
    @pytest.mark.function
    def test_03_colour_filter_grayscale_gesture_module_C51909740(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["gestures"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["gestures"].verify_gesture_card_title_show_color, machine_name=platform, page_number=1, element="gesture_card_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Gesture Title", color="gray_scale_inverted")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["gestures"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
