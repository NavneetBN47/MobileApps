import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Energy_Consumption_Accessibility(object):
    # Should be run on masadan,ernesto(desktop,laptop)

    def verify_images(self, image_compare_result, image_name, platform):
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline for {platform}."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    def verify_windows_mode_contrast(self, platform):
        try:
            for theme in ["aquatic_contrast_theme", "desert_contrast_theme", "dusk_contrast_theme", "night_sky_contrast_theme"]:
                self.fc.set_windows_contrast_theme_from_settings(theme)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_energy_consumption_page,machine_name=platform,page_number=1,element="energy_consumption_header",mode=theme, raise_e=False)
                self.verify_images(image_compare_result,"energy_consumption_page1", platform)
                self.fc.swipe_window(direction="down", distance=6)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_energy_consumption_page,machine_name=platform,page_number=2,element="energy_environment_link",mode=theme, raise_e=False)
                self.verify_images(image_compare_result,"energy_consumption_page2", platform)
                self.fc.swipe_window(direction="up", distance=6)
        finally:
            self.fc.set_windows_contrast_theme_from_settings("none_contrast_theme")

    @pytest.mark.function
    def test_01_dark_mode_C51250977(self):
        platform = self.platform.lower()
        try:
            time.sleep(2)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy consumption card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
            self.fc.enable_dark_mode()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_energy_consumption_page,machine_name=platform,page_number=1,element="energy_consumption_header",mode="dark", raise_e=False)
            self.verify_images(image_compare_result,"energy_consumption_page1", platform)
            self.fc.swipe_window(direction="down", distance=6)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_energy_consumption_page,machine_name=platform,page_number=2,element="energy_environment_link",mode="dark", raise_e=False)
            self.verify_images(image_compare_result,"energy_consumption_page2", platform)
            self.fc.swipe_window(direction="up", distance=6)
        finally:
            self.fc.disable_dark_mode()
    
    @pytest.mark.function
    def test_02_personalization_windows_high_contrast_C51250976(self):
        platform = self.platform.lower()
        self.fc.fd["energy_consumption"].verify_and_navigate_energy_consumption_page()
        time.sleep(3)
        self.verify_windows_mode_contrast(platform)