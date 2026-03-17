from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

# The tests in this class will fail until https://hp-jira.external.hp.com/browse/HPXWC-32191 is fixed
@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Control_One_Step_Inking_Menu_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()
    logging.info(f"Query Start time is: {query_start_time}")

    def verify_analytics(self, control_name):
        serial_number = self.fc.get_windows_serial_number()
        logging.info(self.query_start_time)
        custom_filter = analytics_test.create_custom_filter(serial_number, "OneStepInking", "PcPencontrol", "OnChange", control_name)
        analytics_test.verify_analytics(json_file, custom_filter, self.query_start_time, "pen_control", 5)

    @pytest.mark.analytics
    def test_01_pen_control_click_pen_menu_analytics_C52081565(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_one_step_inking_card()
        self.fc.fd["pen_control"].click_one_step_inking_open_app_cancel_button()
        for _ in range(5):
            self.fc.fd["pen_control"].click_one_step_inking_pen_menu()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_one_note()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_ms_white_board()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_snipping_tool()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_screen_snipping()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_open_app()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_open_app_cancel_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_one_step_inking_disabled()
            time.sleep(1)
        self.verify_analytics("Penmenu")

    @pytest.mark.analytics
    def test_02_pen_control_click_one_note_analytics_C52081566(self):
        self.verify_analytics("OneNote")

    @pytest.mark.analytics
    def test_03_pen_control_click_ms_white_board_analytics_C52081567(self):
        self.verify_analytics("MSWhiteboard")

    @pytest.mark.analytics
    def test_04_pen_control_click_snipping_tool_analytics_C52081568(self):
        self.verify_analytics("Snippingtool")

    @pytest.mark.analytics
    def test_05_pen_control_click_screen_snipping_analytics_C52081569(self):
        self.verify_analytics("ScreensnippingRadioButton")

    @pytest.mark.analytics
    def test_06_pen_control_click_disabled_analytics_C52081570(self):
        self.verify_analytics("DisabledRadioButton")

    @pytest.mark.analytics
    def test_07_pen_control_click_open_app_analytics_C52081571(self):
        self.verify_analytics("OpenappRadioButton")
