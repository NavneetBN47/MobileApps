import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#The baseline images are taken against Machu13x3 with Moonracer Pen, so need to run against that.
@pytest.mark.usefixtures("class_setup_fixture_for_desktop")
class Test_Suite_PenControl_Images_UI_MoonRacer(object):

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_01_moonracer_pen_image_C53040210(self):
        # Ensure the test starts on the MyPen page; navigate there if not already.
        self.fc.check_and_navigate_to_my_pen_page()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_image, pen_type="moonracer")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "LOne image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        self.fc.fd["pen_control"].click_customize_buttons()
        time.sleep(1)
        # This is a workaround to get to the default image to show up. Hovering on one of the barrel buttons and then hovering on something outside seem to be the only way. 
        self.driver.hover("customize_upper_barrel_button")
        time.sleep(1)
        self.driver.hover("restore_default_customize_button_ltwo_page")

        # Verify customize buttons default image
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="default", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Default customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        # Verify customize buttons upper barrel image
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="upper", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Upper barrel customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        # Verify customize buttons lower barrel image
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="lower", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Lower barrel customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        # Verify customize buttons top button image
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="top_single", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Lower barrel customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        self.fc.fd["pen_control"].click_double_press_button_commercial()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="top_double", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Lower barrel customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        self.fc.fd["pen_control"].click_long_press_button_commercial()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="top_long", pen_type="moonracer")
        if image_compare_result is not None:
            assert image_compare_result, "Lower barrel customize buttons image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
    
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_sensitivity_lwo_image, pen_type="moonracer")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Pen sensitivity card image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
