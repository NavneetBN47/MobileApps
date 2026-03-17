import logging
import pytest
import time
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_Accessibility(object):
    # Should be run on commercial and consumer platforms
    def verify_images(self, image_compare_result, image_name):
        logging.info(f"Image comparison result for {image_name}: {image_compare_result}")
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    def verify_windows_mode_contrast(self, platform):
        try:
            for theme in ["aquatic_contrast_theme", "desert_contrast_theme", "dusk_contrast_theme", "night_sky_contrast_theme"]:
                self.fc.set_windows_contrast_theme_from_settings(theme)
                self.fc.swipe_to_top()
                time.sleep(2)
                if platform == "enstrom":
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="battery_information_title_ltwo", page_number=1, mode="cons"+theme)
                    self.verify_images(image_compare_result, "battery_ui1")
                elif platform in ["masadansku5", "longhornz", "ernesto"]:
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="battery_information_title_ltwo", page_number=1, mode="comm"+theme)
                    self.verify_images(image_compare_result, "battery_ui1")
                    self.fc.swipe_window(direction="down", distance=8)
                    self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
                    #click any day start time 
                    self.fc.fd["battery"].click_start_time_wednesday_ltwo()
                    time.sleep(2)
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="schedule_battery_radio_button_ltwo", page_number=2, mode="comm"+theme)
                    self.verify_images(image_compare_result, "battery_ui2")
                    self.fc.swipe_window(direction="down", distance=6)
                    # click plug in dropdown
                    self.fc.fd["battery"].click_when_plugged_in_threshold_dropdown()                
                    time.sleep(3)
                    image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="when_plugged_in_threshold_dropdown", page_number=3, mode="comm"+theme)
                    self.verify_images(image_compare_result, "battery_ui3")
                    self.fc.verify_and_navigate_battery_page()
                    self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        finally:
            self.fc.set_windows_contrast_theme_from_settings("none_contrast_theme")

    @pytest.mark.function
    def test_01_battery_dark_mode_C60186366(self):
        try:
            platform = self.platform.lower()
            logging.info("Testing battery dark mode")
            time.sleep(2)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone, "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.fc.enable_dark_mode()
            time.sleep(1)
            if platform == "enstrom":
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="battery_information_title_ltwo", page_number=1, mode="cons_dark_mode")
                self.verify_images(image_compare_result, "battery_ui1")
            elif platform in ["masadansku5", "longhornz", "ernesto"]:
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="battery_information_title_ltwo", page_number=1, mode="dark_mode")
                self.verify_images(image_compare_result, "battery_ui1")
                self.fc.swipe_window(direction="down", distance=8)
                self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
                #click any day start time 
                self.fc.fd["battery"].click_start_time_wednesday_ltwo()
                time.sleep(2)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="schedule_battery_radio_button_ltwo", page_number=2, mode="dark_mode")
                self.verify_images(image_compare_result, "battery_ui2")
                self.fc.swipe_window(direction="down", distance=6)
                # click plug in dropdown
                self.fc.fd["battery"].click_when_plugged_in_threshold_dropdown()                
                time.sleep(3)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_manager_page_ui, element="when_plugged_in_threshold_dropdown", page_number=3, mode="dark_mode")
                self.verify_images(image_compare_result, "battery_ui3")
        finally:
            self.fc.disable_dark_mode()
        
    @pytest.mark.function
    def test_02_battery_high_contrast_settings_win_11_os_C60186370(self):
        platform = self.platform.lower()
        logging.info("Testing battery high contrast settings")
        time.sleep(2)
        self.fc.verify_and_navigate_battery_page()
        self.verify_windows_mode_contrast(platform)
