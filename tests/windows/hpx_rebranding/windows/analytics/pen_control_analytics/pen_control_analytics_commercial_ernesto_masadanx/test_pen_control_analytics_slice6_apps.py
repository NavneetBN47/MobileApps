import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Slice6_Apps_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
   
    @pytest.mark.analytics
    def test_01_pen_control_apps_windows_search_radio_analytics_C52120683(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)

        self.fc.fd["pen_control"].click_radial_menu_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice6_button()
        time.sleep(3)
        
        self.fc.fd["pen_control"].click_radial_slice6_productivity_universal_radio_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_productivity_arrow_icon()
        time.sleep(3)
        self.fc.fd["pen_control"].click_pen_arrow_icon()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice6_productivity_show_more_button()
        time.sleep(5)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all productivity options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_radial_slice6_apps_onenote_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_open_app_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice_add_application_cancel_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_email_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_web_browser_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_switch_app_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_screen_snipping_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_ms_whiteboard_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_apps_windows_search_radio_button()
            time.sleep(1)
            

        # Get the current serial number for an open search query.
        pytest.serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsWindowssearch",
        "controlLabel": "AppsWindowssearch",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_apps_ms_whiteboard_radio_analytics_C52120687(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsMSWhiteboard",
        "controlLabel": "AppsMSWhiteboard",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_03_pen_control_apps_screen_snipping_radio_analytics_C52120720(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsScreensnipping",
        "controlLabel": "AppsScreensnipping",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_04_pen_control_apps_switch_application_radio_analytics_C52120785(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsSwitchApplication",
        "controlLabel": "AppsSwitchApplication",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_05_pen_control_apps_web_browser_radio_analytics_C52120786(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsWebbrowser",
        "controlLabel": "AppsWebbrowser",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_06_pen_control_apps_email_radio_analytics_C52120793(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsEmail",
        "controlLabel": "AppsEmail",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_07_pen_control_apps_open_app_radio_analytics_C52120794(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsOpenapp",
        "controlLabel": "AppsOpenapp",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_08_pen_control_apps_onenote_app_radio_analytics_C52120808(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "AppsOneNote",
        "controlLabel": "AppsOneNote",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)                                        