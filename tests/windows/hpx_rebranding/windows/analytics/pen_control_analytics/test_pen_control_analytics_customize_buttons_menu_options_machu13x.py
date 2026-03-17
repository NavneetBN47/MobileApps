from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Control_Customize_Buttons_Menu_Analytics(object):

    def verify_analytics(self, setup, action, control_name):
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, "CustomizeButtons", "PcPencontrol", action, control_name)
        analytics_test.verify_analytics(json_file, custom_filter, setup, "pen_control", 5)

    @pytest.fixture(autouse=True)
    def setup(self):
        # Ensure each test starts on the "Customize buttons" page, if not, navigate to the page before each test
        title = self.fc.fd["pen_control"].get_pen_ltwo_page_title()
        logging.info(title)
        if title != "Customize buttons":
            logging.info(f"Page title is '{title}' instead of 'Customize buttons', navigate to the page")
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["pen_control"].click_customize_buttons()

        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        logging.info(f"Query Start time is: {query_start_time}")
        yield query_start_time

    @pytest.mark.analytics
    def test_01_pen_control_click_upper_barrel_button_analytics_C52080049(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_customize_upper_barrel_button()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "OnClick","Upperbarrelbutton")

    @pytest.mark.analytics
    def test_02_pen_control_click_lower_barrel_button_analytics_C52080061(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_customize_lower_barrel_button()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "OnClick","Lowerbarrelbutton")

    @pytest.mark.analytics
    def test_03_pen_control_click_single_press_button_analytics_C52080062(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_single_press_button_commercial()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "OnClick","TopbuttonSinglepress")

    @pytest.mark.analytics
    def test_04_pen_control_click_double_press_button_analytics_C52080063(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_double_press_button_commercial()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "OnClick","TopbuttonDoublepress")

    @pytest.mark.analytics
    def test_05_pen_control_click_long_press_button_analytics_C52080064(self, setup):
        for _ in range(5):
            self.fc.fd["pen_control"].click_long_press_button_commercial()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "OnClick","TopbuttonLongpress")

