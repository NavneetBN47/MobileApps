from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

# will work only on Machu13x with MoonRacer 
# this class will fail until https://hp-jira.external.hp.com/browse/HPXWC-32313 is fixed
@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Alerts_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()

    def verify_analytics(self, control_name):
        serial_number = self.fc.get_windows_serial_number()
        logging.info(self.query_start_time)
        custom_filter = analytics_test.create_custom_filter(serial_number, "PencontrolHome", "RootPencontrol", "OnChange", control_name)
        analytics_test.verify_analytics(json_file, custom_filter, self.query_start_time, "pen_control", 5)

    @pytest.mark.analytics
    def test_01_pen_control_pen_not_detected_toggle_off_analytics_C52080024(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].swipe_to_alert_when_pen_is_idle_text()

        # Check the toggle state and if it ON, turn it OFF so that we can have a consistent starting point. 
        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_not_detected_alert()
        logging.info(f"Toggle State of Pen Not Detected Alert: {toggle_state}")
        if toggle_state == "1":
            self.fc.fd["pen_control"].click_pen_not_detected_alert_toggle_off()
            time.sleep(3)

        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_power_saving_alert()
        logging.info(f"Toggle State of Pen Power Saving Alert: {toggle_state}")
        if toggle_state == "1":
            self.fc.fd["pen_control"].click_power_saving_alert_toggle_off()
            time.sleep(3)
        # Set query start time now so that the click above is not counted against the analytics. 
        Test_Suite_Pen_Alerts_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["pen_control"].click_pen_not_detected_alert_toggle_on()
            time.sleep(3)
            self.fc.fd["pen_control"].click_power_saving_alert_toggle_on()
            time.sleep(3)
            self.fc.fd["pen_control"].click_pen_not_detected_alert_toggle_off()
            time.sleep(3)
            self.fc.fd["pen_control"].click_power_saving_alert_toggle_off()
            time.sleep(3)
        self.verify_analytics("PenNotDetectedAlertToggleOn")

    @pytest.mark.analytics
    def test_02_pen_control_pen_not_detected_toggle_on_analytics_C52080027(self):
        self.verify_analytics("PenNotDetectedAlertToggleOff")

    @pytest.mark.analytics
    def test_03_pen_control_pen_power_saving_toggle_on_analytics_C52080025(self):
        self.verify_analytics("PowerSavingToggleOn")

    @pytest.mark.analytics
    def test_04_pen_control_pen_power_saving_toggle_off_analytics_C52080028(self):
        self.verify_analytics("PowerSavingToggleOff")