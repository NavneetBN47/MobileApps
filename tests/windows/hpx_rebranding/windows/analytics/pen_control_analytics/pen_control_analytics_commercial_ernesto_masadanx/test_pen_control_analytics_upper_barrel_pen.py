import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Upper_Barrel_Pen_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
  
    @pytest.mark.analytics
    def test_01_pen_control_pen_touch_onoff_radio_analytics_C52081616(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)

        self.fc.fd["pen_control"].click_customize_buttons()
        time.sleep(3)
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_productivity_arrow_icon()
        time.sleep(3)

        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        time.sleep(5)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_customize_button_disabled_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_pen_menu_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_fifth_click_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_fourth_click_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_middle_click_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_left_click_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_right_click_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_erase_text()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_button_touch_on_off_text()
            time.sleep(1)

        # Get the current serial number for an open search query.
        pytest.serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenTouchonoff",
        "controlLabel": "PenTouchonoff",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_pen_erase_radio_analytics_C52081625(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenErase",
        "controlLabel": "PenErase",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_03_pen_control_pen_right_click_radio_analytics_C52081617(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenRightclick",
        "controlLabel": "PenRightclick",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_04_pen_control_pen_left_click_radio_analytics_C52081619(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenLeftclick",
        "controlLabel": "PenLeftclick",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_05_pen_control_pen_middle_click_radio_analytics_C52081622(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenMiddleclick",
        "controlLabel": "PenMiddleclick",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_06_pen_control_pen_fourth_click_radio_analytics_C52081624(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenFourthclick",
        "controlLabel": "PenFourthclick",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_07_pen_control_pen_fifth_click_radio_analytics_C52081627(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenFifthclick",
        "controlLabel": "PenFifthclick",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_08_pen_control_pen_menu_radio_analytics_C52081628(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenPenmenu",
        "controlLabel": "PenPenmenu",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_09_pen_control_pen_disabled_radio_analytics_C52081631(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Upperbarrelbutton/"],
        "viewName": "Upperbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "PenDisabled",
        "controlLabel": "PenDisabled",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)
