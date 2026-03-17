from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/dock_filter.json"


@pytest.mark.usefixtures("class_setup_fixture_for_desktop")
class Test_Suite_Dock_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()

    def verify_analytics(self,query_start_time, view_name, view_module, action, control_name):
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, view_name, view_module, action, control_name)
        analytics_test.verify_analytics(json_file, custom_filter, query_start_time, "dock", 5)

    @pytest.fixture(autouse=True)
    def setup(self):
        # Ensure each test starts on the "My Dock" page, if not, navigate to the page before each test
        self.fc.check_and_navigate_to_my_dock_page()
        time.sleep(3)
        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        logging.info(f"Query Start time is: {query_start_time}")
        yield query_start_time

    @pytest.mark.analytics
    def test_01_on_load_product_information_analytics_C53017796(self, setup):
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
            self.fc.fd["devicesMFE"].click_dock_station_card()
            time.sleep(1)
        self.verify_analytics(setup, "ProductInformation", "ProductInformation", "OnLoad", "")

    @pytest.mark.analytics
    def test_02_click_copy_serial_button_analytics_C53017991(self, setup):
        self.fc.fd["dock_station"].swipe_down_to_product_information_section()
        self.driver.swipe(direction="down", distance=2)
        for _ in range(5):
            self.fc.fd["dock_station"].click_copy_serial_number_button()
            time.sleep(1)
            # Move mouse over to somewhere else so that the clicked tool-tip disappears
            self.fc.fd["dock_station"].hover_over_product_information_section()
            time.sleep(1)
        self.verify_analytics(setup, "ProductInformation", "ProductInformation", "OnClick", "CopySerialNumberButton")


    @pytest.mark.analytics
    def test_03_click_contact_us_button_analytics_C53017994(self, setup):
        for _ in range(5):
            self.fc.fd["dock_station"].swipe_down_to_contact_us_button()
            self.fc.fd["dock_station"].click_contact_us_button()
            time.sleep(1)
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.verify_analytics(setup, "Support", "SupportCard", "OnClick", "ContactUsButton")