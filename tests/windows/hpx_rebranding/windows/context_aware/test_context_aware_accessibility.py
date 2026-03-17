import pytest
import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
# This suite should be run on keelung27 platform

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Context_Aware_Accessibility_UI(object):

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
    def test_01_verify_context_aware_module_increase_text_size_C51570681(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=4)
            if self.fc.fd["display_control"].verify_display_control_support_popup() == True:
                self.fc.fd["display_control"].click_display_control_ok_support_popup_button()

            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
            
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_all_application_button_ltwo_page_image, machine_name=platform, page_number=1, element="all_application_button_ltwo_page", text_size=225)
            self.verify_images(image_compare_result, "All Applications Button", 225)

            time.sleep(2)
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_add_app_cancel_button_ltwo_page_image, machine_name=platform, page_number=2, element="add_app_cancel_onpopup_window_page", text_size=225)
            self.verify_images(image_compare_result, "Add App Cancel Button", 225)


        finally: 
            self.fc.fd["context_aware"].update_text_size_in_system_settings(100)

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_colour_filter_grayscale_C51570689(self):
        try:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["context_aware"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "display control card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_color_filter_page1)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")

            time.sleep(2)
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            image_compare_result_2 = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_color_filter_page2)
            # Only assert if screenshot comparison actually happened
            if image_compare_result_2 is not None:
                assert image_compare_result_2, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["context_aware"].revert_system_color_filter()
    

    @pytest.mark.function
    def test_03_system_color_mode_context_aware_module_C51570687(self):
        try:
            self.fc.fd["context_aware"].select_system_color_mode("light_mode")
            self.fc.restart_myHP()
            time.sleep(2)
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=4)
            if self.fc.fd["display_control"].verify_display_control_support_popup() == True:
                self.fc.fd["display_control"].click_display_control_ok_support_popup_button()

            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)

            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_all_application_button_ltwo_page_mode, mode="light_mode")
            self.verify_images(image_compare_result, "All Applications Button")

            time.sleep(2)
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_add_app_cancel_button_ltwo_page_mode, mode="light_mode")
            self.verify_images(image_compare_result, "Add App Cancel Button")
            time.sleep(2)
            self.fc.fd["context_aware"].click_add_app_cancel_button_ltwo_page()
            time.sleep(2)

            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["context_aware"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_all_application_button_ltwo_page_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "All Applications Button")

            time.sleep(2)
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            time.sleep(2)

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_add_app_cancel_button_ltwo_page_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "Add App Cancel Button")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["context_aware"].revert_system_color_mode()
    

    @pytest.mark.function
    def test_04_verify_magnify_context_aware_module_C51570690(self):
        try:
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=4)
            if self.fc.fd["display_control"].verify_display_control_support_popup() == True:
                self.fc.fd["display_control"].click_display_control_ok_support_popup_button()

            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)

            self.fc.fd["context_aware"].click_search_bar_on_windows()
            self.fc.fd["context_aware"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["context_aware"].reset_zoom()
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["context_aware"].zoom_in()
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_all_application_button_ltwo_page_image, machine_name=platform, page_number=3, element="all_application_button_ltwo_page", text_size=225)
            self.verify_images(image_compare_result, "All Applications Button", 225)

            time.sleep(2)
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["context_aware"].verify_add_app_cancel_button_ltwo_page_image, machine_name=platform, page_number=4, element="add_app_cancel_onpopup_window_page", text_size=225)
            self.verify_images(image_compare_result, "Add App Cancel Button", 225)

        finally:
            self.fc.fd["context_aware"].close_magnifier()
    

    @pytest.mark.function
    def test_05_adding_application_and_restart_machine_C57268585(self, request):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"

        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"

        self.fc.fd["display_control"].search_apps_on_search_frame("Access")
        time.sleep(2)
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        time.sleep(4)
        assert bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is True, "Access app is not added in the application list"
        time.sleep(2)

        time.sleep(2)
        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)

        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
        time.sleep(2)
        assert bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is True, "Access app is not added in the application list"
