import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Topbutton_Doublepress_Additional_Actions_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    @pytest.mark.analytics
    def test_01_pen_control_click_on_more_actions_button_C52086238(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)
        self.fc.fd["pen_control"].click_customize_buttons()
        time.sleep(3)        
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
        self.fc.fd["pen_control"].click_customize_topbutton_doublepress()
        self.fc.swipe_window(direction="down", distance=15)
        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_more_link_top_button_double_press()
            time.sleep(1)
            self.fc.fd["pen_control"].click_media_control_chevron_down_arrow()
            time.sleep(1)
            self.fc.fd["pen_control"].click_media_control_chevron_down_arrow()
            time.sleep(1)

        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/TopbuttonDoublepress/"],
        "viewName": "TopbuttonDoublepress", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MoreActionButton",
        "controlLabel": "MoreActionButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_click_on_change_to_open_app_button_C52086239(self):    
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(3)        
        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_customize_button_open_app_text()
            time.sleep(3)
            self.fc.fd["pen_control"].select_administrative_tools()
            time.sleep(3)
            self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_windows_search_text()
            time.sleep(3)
            
        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/TopbuttonDoublepress/"],
        "viewName": "TopbuttonDoublepress", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ChangeAppToOpenButton",
        "controlLabel": "ChangeAppToOpenButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)