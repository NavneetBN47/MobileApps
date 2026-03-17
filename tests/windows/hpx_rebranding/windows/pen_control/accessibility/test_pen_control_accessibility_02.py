import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Pen_Accessibility_UI(object):
# This suite should only run on all commercial platforms with pen support. Testing can be performed using different pens — Trio, Moonracer, and Roo.
# for Roo pen need to run script on machu with Roo pen connected

    def verify_dark_mode(self,pen_name):
        try:
            self.fc.enable_dark_mode()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_mode, pen_name=pen_name, page_number=1, element="connected_text_lone_page", mode="dark_mode", raise_e=False)
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
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_mode, pen_name=pen_name, page_number=1, element="connected_text_lone_page", mode=theme, raise_e=False)
                # Only assert if screenshot comparison actually happened
                if image_compare_result is not None:
                    assert image_compare_result, "LOne image did not match the baseline."
                else:
                    logging.info("No screenshot comparison performed (context manager not active)")          
        finally:
            self.fc.set_windows_contrast_theme_from_settings("none_contrast_theme")
                
    @pytest.mark.require_platform(["not available"])
    def test_01_dark_mode_C53056338(self):
        pen_name = self.fc.navigate_to_pen_card_and_get_pen_name()
        # "HP Rechargeable Active Pen G3" --> Moonracer
        # "HP Nested Pen" --> Roo
        # "HP 705 Rechargeable Multi Pen" --> Trio
        if pen_name in ["HP Rechargeable Active Pen G3", "HP Nested Pen", "HP 705 Rechargeable Multi Pen"]:
            self.verify_dark_mode(pen_name)
        else:
            logging.info("No compatible pen connected for dark mode verification.")
      
    @pytest.mark.require_platform(["not available"])
    def test_02_windows_high_contrast_C53056342(self):
        pen_name = self.fc.navigate_to_pen_card_and_get_pen_name()
        if pen_name in ["HP Rechargeable Active Pen G3", "HP Nested Pen", "HP 705 Rechargeable Multi Pen"]:
            self.verify_windows_mode_contrast(pen_name)
        else:
            logging.info("No compatible pen connected for dark mode verification.")

