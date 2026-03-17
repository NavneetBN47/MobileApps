import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#This suite should be run on herbie platform
@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Touchpad_Accessibility_UI(object):

    def verify_images(self, image_compare_result, image_name, percentage=None, color=None):
        if percentage:
            logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        elif color:
            logging.info(f"Image comparison result at {color}% color filter: {image_compare_result}")

        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")


    @pytest.mark.function
    def test_01_system_color_mode_touchpad_module_C51909724(self):
        try:
            self.fc.fd["touchpad"].select_system_color_mode("light_mode")
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
            self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_touchpad_title_show_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Touchpad Title")

            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["touchpad"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_touchpad_title_show_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Touchpad Title")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["touchpad"].revert_system_color_mode()
    

    def test_02_verify_magnify_touchpad_module_C51909727(self):
        try:
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
            self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
            time.sleep(3)
            self.fc.fd["touchpad"].click_search_bar_on_windows()
            self.fc.fd["touchpad"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["touchpad"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["touchpad"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_touchpad_title_show_image, machine_name=platform, page_number=5, element="touchpad_title", text_size=200)
            self.verify_images(image_compare_result, "touchpad_= title", percentage=200)

        finally:
            self.fc.fd["touchpad"].close_magnifier()


    @pytest.mark.ota
    @pytest.mark.function
    def test_03_colour_filter_grayscale_touchpad_module_C51909726(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
            self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["touchpad"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_touchpad_title_show_color, machine_name=platform, page_number=1, element="touchpad_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Touchpad Title", color="gray_scale_inverted")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["touchpad"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
