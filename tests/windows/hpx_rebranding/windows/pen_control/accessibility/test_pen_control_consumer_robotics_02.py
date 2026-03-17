import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Pen_Accessibility_UI(object):
# This suite should only run on willie(consumer) for Avicii pen need to run script

    def dark_mode_verification(self,pen_name):
        try:
            self.fc.enable_dark_mode()
            self.fc.check_and_navigate_to_my_pen_page()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_mode, pen_name=pen_name, page_number=1, element="pen_name_on_lone_page", mode="dark_mode", raise_e=False)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.disable_dark_mode()
    
    def verify_windows_mode_contrast(self,pen_name):
        try:
            for theme in ["aquatic_contrast_theme", "desert_contrast_theme", "dusk_contrast_theme", "night_sky_contrast_theme"]:
                self.fc.set_windows_contrast_theme_from_settings(theme)
                image_compare_rsult = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_mode, pen_name=pen_name, page_number=1, element="connected_text_lone_page", mode=theme, raise_e=False)
                # Only assert if screenshot comparison actually happened
                if image_compare_result is not None:
                    assert image_compare_result, "LOne image did not match the baseline."
                else:
                    logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.set_windows_contrast_theme_from_settings("none_contrast_theme")

    @pytest.mark.function
    @pytest.mark.require_platform(["not available"])
    def test_01_dark_mode_C53056338(self):
        self.vcosmos.introduce_pen()
        self.vcosmos.clean_up_logs()
        pen_name = self.fc.navigate_to_pen_card_and_get_pen_name()
        logging.info(f"Connected pen name: {pen_name}")
        if pen_name == "HP Digital Pen":
            self.dark_mode_verification(pen_name)
        else:
            logging.info("No compatible pen connected for dark mode verification.")
    
    @pytest.mark.function
    @pytest.mark.require_platform(["not available"])
    def test_02_windows_high_contrast_C53056342(self):
        self.vcosmos.introduce_pen()
        self.vcosmos.clean_up_logs()
        pen_name = self.fc.navigate_to_pen_card_and_get_pen_name()
        logging.info(f"Connected pen name: {pen_name}")
        if pen_name == "HP Digital Pen":
            self.verify_windows_mode_contrast(pen_name)
        else:
            logging.info("No compatible pen connected for dark mode verification.")