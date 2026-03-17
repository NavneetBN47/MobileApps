from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

# Only works on Machu13x with Roo, where OneStepInking is available.
@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Status_Props_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()

    def verify_analytics(self, control_name,query_start_time):
        serial_number = self.fc.get_windows_serial_number()
        logging.info(query_start_time)
        custom_filter = analytics_test.create_custom_filter(serial_number, "PencontrolHome", "RootPencontrol", "OnClick", control_name)
        analytics_test.verify_analytics(json_file, custom_filter, self.query_start_time, "pen_control", 5)

    @pytest.fixture(autouse=True)
    # Must Run on Machu13x with Roo connected for one step inking to work
    def setup(self):
        # Ensure each test starts on the "My Pen" page, if not, navigate to the page before each test
        self.fc.check_and_navigate_to_my_pen_page()

        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        serial_number = self.fc.get_windows_serial_number()
        logging.info(f"Query Start time is: {query_start_time}")
        yield query_start_time

    @pytest.mark.analytics
    def test_01_pen_control_touch_stylus_for_status_analytics_C52074778(self,setup):     
        for _ in range(5):
            self.fc.fd["pen_control"].click_touch_stylus_for_status()
            time.sleep(1)
        self.verify_analytics("Touchstylusforstatus", setup)

    @pytest.mark.analytics
    def test_02_pen_control_radial_menu_needs_reassignment_button_analytics_C52074783(self,setup):
        if not self.fc.fd["pen_control"].get_radial_menu_needs_reassignment_button():
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_radial_slice1_button()
            self.fc.fd["pen_control"].click_radial_slice1_productivity_show_more_button()
            self.fc.fd["pen_control"].swipe_down_to_radial_slice1_apps_ms_whiteboard_radio_button()
            self.fc.fd["pen_control"].click_radial_slice1_apps_ms_whiteboard_radio_button()
            time.sleep(1)
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        for _ in range(5):
            self.fc.fd["pen_control"].click_radial_menu_needs_reassignment_button()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.verify_analytics("Radialmenuneedsreassignment", setup)

    @pytest.mark.analytics
    def test_03_pen_control_one_step_inking_needs_reassignment_analytics_C52074929(self,setup):
        if not self.fc.fd["pen_control"].get_one_step_inking_needs_reassignment_button():
            self.fc.fd["pen_control"].swipe_down_to_one_step_inking_card()
            self.fc.fd["pen_control"].click_one_step_inking_card()
            self.fc.fd["pen_control"].click_one_step_inking_ms_white_board()
            time.sleep(1)
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        for _ in range(5):
            self.fc.fd["pen_control"].click_one_step_inking_needs_reassignment_button()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.verify_analytics("Onestepinkingneedsreassignment", setup)

    @pytest.mark.analytics
    def test_04_pen_control_button_needs_reassignment_analytics_C52074790(self,setup):
        if not self.fc.fd["pen_control"].get_button_needs_reassignment_button():
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
            time.sleep(1)
            self.fc.fd["pen_control"].swipe_down_to_upper_barrel_button_ms_whiteboard()
            self.fc.fd["pen_control"].click_customize_buttons_upper_barrel_mswhiteboard_lthree_page()
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        for _ in range(5):
            self.fc.fd["pen_control"].click_button_needs_reassignment_button()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.verify_analytics("Buttonneedsreassignment", setup)