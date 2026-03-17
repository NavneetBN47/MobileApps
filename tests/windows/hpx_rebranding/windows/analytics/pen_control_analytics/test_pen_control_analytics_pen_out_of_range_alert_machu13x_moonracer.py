from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

@pytest.mark.usefixtures("class_setup_fixture")
# will work only on Machu13x with MoonRacer 
class Test_Suite_Pen_Out_Of_Range_Alerts_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()

    def verify_analytics(self, control_name):
        serial_number = self.fc.get_windows_serial_number()
        logging.info(self.query_start_time)
        custom_filter = analytics_test.create_custom_filter(serial_number, "PencontrolHome", "RootPencontrol", "OnChange", control_name)
        analytics_test.verify_analytics(json_file, custom_filter, self.query_start_time, "pen_control", 5)

    @pytest.mark.analytics
    def test_01_pen_control_pen_out_of_range_toggle_off_analytics_C52080026(self):
        self.fc.check_and_navigate_to_my_pen_page()

        # Check the toggle state and if it ON, turn it OFF so that we can have a consistent starting point. 
        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_out_of_range_alert()
        logging.info(f"Toggle State of Pen Out Of Range Alert: {toggle_state}")
        if toggle_state == "1":
            self.fc.fd["pen_control"].click_notification_tab_toggle_off_switch_lone_page()
            time.sleep(3)

        # Set query start time now so that the click above is not counted against the analytics. 
        Test_Suite_Pen_Out_Of_Range_Alerts_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["pen_control"].click_notification_tab_toggle_switch_lone_page()
            time.sleep(3)
            self.fc.fd["pen_control"].click_notification_tab_toggle_off_switch_lone_page()
            time.sleep(3)
        self.verify_analytics("PenOutOfRangeToggleOff")

    @pytest.mark.analytics
    def test_02_pen_control_pen_out_of_range_toggle_on_analytics_C52080032(self):
        self.verify_analytics("PenOutOfRangeToggleOn")
