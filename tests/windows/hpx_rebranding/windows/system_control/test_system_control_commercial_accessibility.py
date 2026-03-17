import pytest
import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

# This suite should be run on eviee platform
@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_System_Control_Commercial_Accessibility_UI(object):

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
    def test_01_verify_system_control_module_increase_text_size_C50723555(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
            time.sleep(3)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_smart_sense_title_show_image, machine_name=platform, page_number=1, element="smart_sense_title_commercial", text_size=225)
            self.verify_images(image_compare_result, "Smart Sense Title", 225)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_power_saving_mode_title_show_image, machine_name=platform, page_number=2, element="power_saving_mode_title", text_size=225)
            self.verify_images(image_compare_result, "Power Saving Mode Title", 225)

            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_optimize_oled_title_show_image, machine_name=platform, page_number=3, element="optimize_oled_title", text_size=225)
            self.verify_images(image_compare_result, "Optimize OLED Title", 225)

        finally: 
            self.fc.fd["system_control"].update_text_size_in_system_settings(100)

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_colour_filter_grayscale_C50723563(self):
        try:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["system_control"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
            assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "system control card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
            if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_color_filter_commercial)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["system_control"].revert_system_color_filter()    
    

    @pytest.mark.function
    def test_03_system_color_mode_system_control_module_C50723561(self):
        try:
            self.fc.fd["system_control"].select_system_color_mode("light_mode")
            self.fc.restart_myHP()
            platform=self.platform.lower()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
            time.sleep(3)

            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_system_control_title_show_mode, mode="light_mode")
            self.verify_images(image_compare_result, "System Control Title")

            time.sleep(2)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["system_control"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["system_control"].verify_system_control_title_show_mode, mode="dark_mode")
            self.verify_images(image_compare_result, "System Control Title")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["system_control"].revert_system_color_mode()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_system_control_restart_machine_verify_state_C51244958(self, request):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)

        if self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "0":
            time.sleep(2)
            self.fc.fd["system_control"].click_optimize_oled_toggle()
            time.sleep(2)
        else:
            time.sleep(2)
            self.fc.fd["system_control"].click_optimize_oled_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_optimize_oled_toggle()
        
        time.sleep(2)
        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)

        assert self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "1", "Optimize OLED toggle state did not persist after restart"


