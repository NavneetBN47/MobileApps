from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Control_Sensitivity_Menu_Analytics(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        # Ensure each test starts on the "Pen sensitivity" page,
        # And if not, navigate to the page before each test
        title = self.fc.fd["pen_control"].get_sensitivity_menu_page_title()
        logging.info(title)
        if title != "Pen sensitivity":
            logging.info(f"Page title is '{title}' instead of 'Pen sensitivity'. Check if Pen Card is visible")
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["pen_control"].click_pen_sensitivity_card()

        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        logging.info(f"Query Start time is: {query_start_time}")
        yield query_start_time

    @pytest.mark.analytics
    def test_01_pen_control_click_sensitivity_pressure_slider_analytics_C52081593(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_pen_sensitivity_pressure_slider()
            time.sleep(1)

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, "PenSensitivity", "PcPencontrol","OnChangeEnd", "SensitivityPressureSlider")
        analytics_test.verify_analytics(json_file, custom_filter, setup, "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_click_sensitivity_tilt_slider_analytics_C52081596(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_pen_sensitivity_tilt_slider()
            time.sleep(1)

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, "PenSensitivity", "PcPencontrol","OnChangeEnd", "SensitivityTiltSlider")
        analytics_test.verify_analytics(json_file, custom_filter, setup, "pen_control", 5)