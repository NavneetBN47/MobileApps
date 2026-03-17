import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#This suite should be run on snowwhite platform
@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Wellbeing_Accessibility_UI(object):

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
    def test_01_verify_wellbeing_module_increase_text_size_C51909702(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card_with_large_text_size()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
            time.sleep(1)
            self.fc.fd["devicesMFE"].restore_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_time_title_show_up_image, machine_name=platform, page_number=1, element="screen_time_title", text_size=225)
            self.verify_images(image_compare_result, "Screen Time Title", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=10)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_distance_title_show_up_image, machine_name=platform, page_number=2, element="screen_distance_title", text_size=225)
            self.verify_images(image_compare_result, "Screen Distance Title", 225)

        finally: 
            self.fc.fd["wellbeing"].update_text_size_in_system_settings(100)


    @pytest.mark.function
    def test_02_verify_magnify_wellbeing_module_C51909711(self):
        try:
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
            self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
            time.sleep(1)
            self.fc.fd["devicesMFE"].restore_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_search_bar_on_windows()
            self.fc.fd["wellbeing"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["wellbeing"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["wellbeing"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_time_title_show_up_image, machine_name=platform, page_number=7, element="screen_time_title", text_size=200)
            self.verify_images(image_compare_result, "screen_time_title", percentage=200)

            self.fc.fd["wellbeing"].scroll_down_to_element("set_preferred_distance_title")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_distance_title_show_up_image, machine_name=platform, page_number=8, element="screen_distance_title", text_size=200)
            self.verify_images(image_compare_result, "screen_distance_title", percentage=200)

        finally:
            self.fc.fd["audio"].close_magnifier()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_colour_filter_grayscale_wellbeing_module_C51909710(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
            self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
            time.sleep(1)
            self.fc.fd["devicesMFE"].restore_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["wellbeing"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_time_title_show_up_color, machine_name=platform, page_number=1, element="screen_time_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Screen Time Title", color="gray_scale_inverted")

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=12)
            time.sleep(2)

            if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_distance_title_show_up_color, machine_name=platform, page_number=2, element="screen_distance_title", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Screen Distance Title", color="gray_scale_inverted")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["wellbeing"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_system_color_mode_wellbeing_module_C51909708(self):
        try:
            self.fc.fd["wellbeing"].select_system_color_mode("light_mode")
            time.sleep(2)
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
            self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
            time.sleep(1)
            self.fc.fd["devicesMFE"].restore_app()
            time.sleep(2)
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(2)

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_time_title_show_up_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Screen Time Title")

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_distance_title_show_up_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Screen Distance Title")

            time.sleep(2)

            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["wellbeing"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_time_title_show_up_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Screen Time Title")

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["wellbeing"].verify_screen_distance_title_show_up_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Screen Distance Title")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["wellbeing"].revert_system_color_mode()