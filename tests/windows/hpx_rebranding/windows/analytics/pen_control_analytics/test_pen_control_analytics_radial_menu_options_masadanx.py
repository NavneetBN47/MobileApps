from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"


@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Control_Radial_Menu_Analytics(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        # Ensure each test starts on the "Customize Radial Menu" page, if not, navigate to the page before each test
        title = self.fc.fd["pen_control"].get_radial_menu_page_title()
        logging.info(title)
        if title != "Customize radial menu":
            logging.info(f"Page title is '{title}' instead of 'Customize radial menu'. Navigate to the page")
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["pen_control"].click_radial_menu_button()

        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        yield query_start_time

    def click_slice_button_and_verify_analytics(self, setup, slice_name):
        for _ in range(5):
            # Get the click_radial_slice method based on the slice_name eg. click_radial_slice1()
            slice_button_method = getattr(self.fc.fd["pen_control"], f"click_radial_{slice_name.lower()}_button", None)
            slice_button_method()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, "CustomizeButtons", "PcPencontrol","OnClick", slice_name)
        analytics_test.verify_analytics(json_file, custom_filter, setup, "pen_control", 5)

    @pytest.mark.analytics
    def test_01_pen_control_click_slice1_analytics_C52080089(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice1")

    @pytest.mark.analytics
    def test_02_pen_control_click_slice2_analytics_C52080090(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice2")

    @pytest.mark.analytics
    def test_03_pen_control_click_slice3_analytics_C52080369(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice3")

    @pytest.mark.analytics
    def test_04_pen_control_click_slice4_analytics_C52081178(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice4")

    @pytest.mark.analytics
    def test_05_pen_control_click_slice1_analytics_C52081195(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice5")

    @pytest.mark.analytics
    def test_06_pen_control_click_slice6_analytics_C52081198(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice6")

    @pytest.mark.analytics
    def test_07_pen_control_click_slice7_analytics_C52081199(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice7")

    @pytest.mark.analytics
    def test_08_pen_control_click_slice8_analytics_C52081200(self, setup):
        self.click_slice_button_and_verify_analytics(setup, "Slice8")