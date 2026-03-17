from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import  RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

@pytest.mark.usefixtures("class_setup_fixture")
# The tests in this class will fail until https://hp-jira.external.hp.com/browse/HPXWC-32191 is fixed
class Test_Suite_Pen_Control_External_Display_Menu_Analytics(object):
    query_start_time = datetime.now(timezone.utc).isoformat()

    def turn_on_enable_this_feature_toggle(self):
        if self.fc.fd["pen_control"].get_toggle_state_enable_this_feature_toggle_switch_ltwo_page() == "0":
            self.fc.fd["pen_control"].click_enable_this_feature_toggle_switch_ltwo_page()

    def verify_analytics(self, query_start_time, action, control_name, action_detail=""):
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = analytics_test.create_custom_filter(serial_number, "PenExternalDisplay", "PcPencontrol", action, control_name, action_detail)
        analytics_test.verify_analytics(json_file, custom_filter, query_start_time, "pen_control", 5)

    def check_and_navigate_to_external_display_ltwo_page(self):
        title = self.fc.fd["pen_control"].get_pen_ltwo_page_title()
        logging.info(title)
        if title != "External display":
            logging.info(f"Page title is '{title}' instead of 'External display', navigate to the page")
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["pen_control"].click_external_display_card()
            
    @pytest.fixture(autouse=True)
    def setup(self):
        # Ensure each test starts on the "External display" page, if not, navigate to the page before each test
       self.check_and_navigate_to_external_display_ltwo_page()

    @pytest.mark.analytics
    def test_01_pen_control_click_display_selection_analytics_C52081572(self):
        Test_Suite_Pen_Control_External_Display_Menu_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["pen_control"].click_display_selection_drop_down()
            time.sleep(1)
            self.fc.fd["pen_control"].click_first_display_from_drop_down()
            time.sleep(1)
        self.verify_analytics(self.query_start_time, "OnValueChange","DisplaySelectionPicker")

    @pytest.mark.analytics
    def test_02_pen_control_click_landscape_analytics_C52081578(self):
        # Get query start time and reuse this for the next three tests that track the actions above
        Test_Suite_Pen_Control_External_Display_Menu_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()
        self.turn_on_enable_this_feature_toggle()
        for _ in range(5):
            self.fc.fd["pen_control"].click_landscape_radio_button()
            time.sleep(3)
            self.fc.fd["pen_control"].click_landscape_flipped_radio_button()
            time.sleep(3)
            self.fc.fd["pen_control"].click_portrait_orientation()
            time.sleep(1)
            self.fc.fd["pen_control"].click_portrait_flipped_orientation()
            time.sleep(1)
        self.verify_analytics(self.query_start_time,"OnChange","Landscape")

    @pytest.mark.analytics
    def test_03_pen_control_click_landscape_flipped_analytics_C52081580(self):
        self.verify_analytics(self.query_start_time,"OnChange","Landscapeflipped")

    @pytest.mark.analytics
    def test_04_pen_control_click_portrait_analytics_C52081582(self):
        self.verify_analytics(self.query_start_time,"OnChange","Portrait")

    @pytest.mark.analytics
    def test_05_pen_control_click_portrait_flipped_analytics_C52081584(self):
        self.verify_analytics(self.query_start_time,"OnChange","Portraitflipped")

    @pytest.mark.analytics
    def test_06_pen_control_click_pen_only_analytics_C52081585(self):
        # Get query start time and reuse this for the next test that track the actions above
        Test_Suite_Pen_Control_External_Display_Menu_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()
        self.turn_on_enable_this_feature_toggle()
        for _ in range(5):
            self.fc.fd["pen_control"].click_pen_only_mode()
            time.sleep(1)
            self.fc.fd["pen_control"].click_pen_and_touch_mode()
            time.sleep(1)
        self.verify_analytics(self.query_start_time,"OnChange","Penonly")

    @pytest.mark.analytics
    def test_07_pen_control_click_pen_and_touch_analytics_C52081587(self):
        self.verify_analytics(self.query_start_time,"OnChange","Penandtouch")

    @pytest.mark.analytics
    def test_08_pen_control_click_scale_mapping_analytics_C52081589(self):
        # Get query start time and reuse this for the next three tests that track the actions above
        Test_Suite_Pen_Control_External_Display_Menu_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()
        self.turn_on_enable_this_feature_toggle()
        self.fc.fd["pen_control"].swipe_down_to_element("scale_ltwo_page")
        for _ in range(5):
            self.fc.fd["pen_control"].click_scale_display_mapping()
            time.sleep(1)
            self.fc.fd["pen_control"].click_stretch_display_mapping()
            time.sleep(1)
        self.verify_analytics(self.query_start_time,"OnChange","Scale")
        
    @pytest.mark.analytics
    def test_09_pen_control_click_stretch_mapping_analytics_C52081590(self):
        self.verify_analytics(self.query_start_time,"OnChange","Stretch")

    @pytest.mark.analytics
    def test_10_pen_control_click_enable_this_feature_analytics_C52081575(self):
        # Get query start time and reuse this for the next test that track the actions above
        Test_Suite_Pen_Control_External_Display_Menu_Analytics.query_start_time = datetime.now(timezone.utc).isoformat()

        # Since turning on/off is the same action, clicking the toggle 10 times (5 each for on and off)
        for _ in range(10):
            # after turning the toggle off, the window changes to lone page. And we will have to navigate to external display page again to click the toggle. 
            self.check_and_navigate_to_external_display_ltwo_page()
            self.fc.fd["pen_control"].click_enable_this_feature_toggle_switch_ltwo_page()
            time.sleep(10)
        # using actionDetail parameter ON/OFF for getting analytics for ON and OFF separately
        self.verify_analytics(self.query_start_time,"OnChange","EnableExternalDisplayToggleOn","On")

    @pytest.mark.analytics
    def test_11_pen_control_click_disable_this_feature_analytics_C52081577(self):
        self.verify_analytics(self.query_start_time,"OnChange","EnableExternalDisplayToggleOn","Off")