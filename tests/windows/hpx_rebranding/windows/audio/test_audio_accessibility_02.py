import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
#This suite should be run on masadansku5 platform
class Test_Suite_Audio_Accessibility_02_UI(object):

    def verify_images(self, image_compare_result, image_name, percentage=None, color=None):
        if percentage:
            logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        elif color:
            logging.info(f"Image comparison result at {color}% color filter: {image_compare_result}")

        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")


    def test_01_verify_magnify_audio_module_C50723579(self):
        try:
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            # check audio card is displayed
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.fd["audio"].click_search_bar_on_windows()
            self.fc.fd["audio"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["audio"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["audio"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_image, machine_name=platform, page_number=5, element="output_title", text_size=200)
            self.verify_images(image_compare_result, "output_title", percentage=200)

            self.fc.fd["audio"].scroll_down_to_element("input_title")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_input_title_show_up_image, machine_name=platform, page_number=6, element="input_title", text_size=200)
            self.verify_images(image_compare_result, "input_title", percentage=200)

            self.fc.fd["audio"].scroll_down_to_element("audio_presets_movie_txt")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up_image, machine_name=platform, page_number=7, element="audio_presets_movie_txt", text_size=200)
            self.verify_images(image_compare_result, "audio_presets_movie_txt", percentage=200)

        finally:
            self.fc.fd["audio"].close_magnifier()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_colour_filter_grayscale_audio_module_C50723578(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            # check audio card is displayed
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_color, machine_name=platform, page_number=1, element="output_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Output Title", color="gray_scale_inverted")

            self.fc.fd["audio"].scroll_down_to_element("input_title")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_input_title_show_up_color, machine_name=platform, page_number=2, element="input_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Input Title", color="gray_scale_inverted")

            self.fc.fd["audio"].scroll_down_to_element("audio_presets_movie_txt")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up_color, machine_name=platform, page_number=3, element="audio_presets_movie_txt", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Audio Presets Movie Text", color="gray_scale_inverted")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_system_color_mode_audio_module_C50723576(self):
        try:
            self.fc.fd["audio"].select_system_color_mode("light_mode")
            time.sleep(3)

            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            # check audio card is displayed
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_system_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Output Title")

            self.fc.fd["audio"].scroll_down_to_element("input_title")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_input_title_show_up_system_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Input Title")

            self.fc.fd["audio"].scroll_down_to_element("audio_presets_movie_txt")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up_system_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Audio Presets Movie Text")

            time.sleep(2)

            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_system_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Output Title")

            self.fc.fd["audio"].scroll_down_to_element("input_title")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_input_title_show_up_system_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Input Title")

            self.fc.fd["audio"].scroll_down_to_element("audio_presets_movie_txt")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up_system_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Audio Presets Movie Text")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["audio"].revert_system_color_mode()
    

    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_platform(["not available"])
    def test_04_audio_scale_size_C42197601(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        try:
            platform=self.platform.lower()
            for scale in ["scale_150_percent","scale_175_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["task_group"].set_scale_from_settings(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                self.fc.swipe_to_top()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_image, machine_name=platform, page_number=10, element="output_title", text_size=scale)
                self.verify_images(image_compare_result, "output_title", percentage=200)

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["task_group"].set_scale_from_settings("scale_100_percent")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        