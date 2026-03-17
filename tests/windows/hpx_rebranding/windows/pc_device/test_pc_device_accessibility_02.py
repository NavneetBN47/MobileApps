import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
#This suite should be run on eviee platform
class Test_Suite_PC_Device_Accessibility_02_UI(object):

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
    def test_01_colour_filter_grayscale_pc_device_module_C42902513(self):
        try:
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)

            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show_color, machine_name=platform, page_number=1, element="audio_control_card_lone_page", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Audio Control Card", color="gray_scale_inverted")

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=17)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_product_number_show_color, machine_name=platform, page_number=2, element="product_number", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Product Number", color="gray_scale_inverted")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
    


    def test_02_verify_magnify_pc_device_module_C53103679(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["audio"].click_search_bar_on_windows()
            self.fc.fd["audio"].search_bar_on_windows("Magnifier")

            self.fc.fd["audio"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["audio"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show_image, machine_name=platform, page_number=9, element="audio_control_card_lone_page", text_size=200)
            self.verify_images(image_compare_result, "Audio Control Card ", percentage=200)
            time.sleep(2)
            self.fc.fd["audio"].close_magnifier()
            
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)

            self.fc.fd["audio"].click_search_bar_on_windows()
            self.fc.fd["audio"].search_bar_on_windows("Magnifier")

            self.fc.fd["audio"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["audio"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_product_number_show_image, machine_name=platform, page_number=10, element="product_number", text_size=200)
            self.verify_images(image_compare_result, "PC device product number", percentage=200)

        finally:
            self.fc.fd["audio"].close_magnifier()


    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_platform(["not available"])
    def test_04_pc_device_scale_size_C42902516(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(3)
        try:
            platform=self.platform.lower()
            for scale in ["scale_150_percent","scale_175_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["task_group"].set_scale_from_settings(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show_image, machine_name=platform, page_number=26, element="audio_control_card_lone_page", text_size=scale)
                self.verify_images(image_compare_result, "PC Device page", percentage=200)

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["task_group"].set_scale_from_settings("scale_100_percent")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
    

    def test_05_verify_pc_device_page_C42902482(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show_image, machine_name=platform, page_number=27, element="audio_control_card_lone_page", text_size=200)
            self.verify_images(image_compare_result, "Audio Control Card ", percentage=200)
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["devices_details_pc_mfe"].verify_product_number_show_image, machine_name=platform, page_number=28, element="product_number", text_size=200)
            self.verify_images(image_compare_result, "PC device product number", percentage=200)

        finally:
            self.fc.fd["audio"].close_magnifier()
    
