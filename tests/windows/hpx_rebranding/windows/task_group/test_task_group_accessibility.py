import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Task_Group_Accessibility_UI(object):

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
    def test_01_verify_task_group_module_increase_text_size_C52986249(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["task_group"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=8)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
            time.sleep(2)
            assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group create new button is not displayed"

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["task_group"].verify_task_group_create_new_show_image, machine_name=platform, page_number=1, element="task_group_create_new_button", text_size=225)
            self.verify_images(image_compare_result, "Task Group Create New Button", 225)


        finally: 
            self.fc.fd["task_group"].update_text_size_in_system_settings(100)
    

    def test_02_verify_magnify_task_group_module_C52986252(self):
        try:
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
            time.sleep(2)
            self.fc.fd["task_group"].click_search_bar_on_windows()
            self.fc.fd["task_group"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["task_group"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["task_group"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            self.fc.fd["task_group"].scroll_to_element("task_group_title")
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["task_group"].verify_task_group_create_new_show_image, machine_name=platform, page_number=2, element="task_group_create_new_button", text_size=225)
            self.verify_images(image_compare_result, "Task Group Create New Button", 225)

        finally:
            self.fc.fd["task_group"].close_magnifier()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_navigate_to_each_button_use_tab_C52986248(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)

        self.fc.fd["task_group"].press_tab("task_group_title")
        time.sleep(2)
        assert self.fc.fd["task_group"].is_focus_on_element("task_group_title"), "Task group title is not focused"
        time.sleep(2)
        self.fc.fd["task_group"].press_tab("task_group_create_new_button")
        time.sleep(2)
        assert self.fc.fd["task_group"].is_focus_on_element("task_group_create_new_button"), "Task group create new button is not focused"
        time.sleep(2)

        self.fc.fd["task_group"].press_reverse_tab("task_group_title")
        time.sleep(2)
        assert self.fc.fd["task_group"].is_focus_on_element("task_group_title"), "Task group title is not focused"
        time.sleep(2)
        self.fc.fd["task_group"].press_reverse_tab("task_group_create_new_button")
        time.sleep(2)
        assert self.fc.fd["task_group"].is_focus_on_element("task_group_create_new_button"), "Task group create new button is not focused"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_colour_filter_grayscale_task_group_module_C52986251(self):
        try:
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["task_group"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["task_group"].verify_create_new_button__show_color, machine_name=platform, page_number=1, element="task_group_create_new_button", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Task Group Create New Button", color="gray_scale_inverted")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["task_group"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

    
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_platform(["not available"])
    # This case currently has a issue and needs to be commented out first to avoid affecting other cases.

    def test_05_task_group_scale_size_C52986250(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        try:
            platform=self.platform.lower()
            for scale in ["scale_150_percent", "scale_175_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["task_group"].set_scale_from_settings_for_task_group_module(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                for _ in range(3):
                    if self.fc.fd["task_group"].verify_task_group_title_show():
                        break
                    else:
                        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                self.fc.swipe_to_top()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["task_group"].verify_task_group_create_new_show_scale, machine_name=platform, page_number=6, element="task_group_create_new_button", text_size=scale)
                self.verify_images(image_compare_result, "Task Group Create New Button", percentage=200)

        finally:
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_minimize_app()
            time.sleep(3)
            self.fc.fd["task_group"].set_scale_from_settings_for_task_group_module("scale_100_percent")
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()