import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Lower_Barrel_Additional_Actions_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    @pytest.mark.analytics
    def test_01_pen_control_click_on_hover_click_toggle_switch_C52083754(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
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
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_lowerbarrel_hover_click_toggle_button_lthree_page()
            time.sleep(1)
            self.fc.fd["pen_control"].click_lowerbarrel_hover_click_toggle_button_lthree_page()
            time.sleep(1)

        # Get the current serial number for an open search query.
        pytest.serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Lowerbarrelbutton/"],
        "viewName": "Lowerbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnChange", 
        "actionDetail": "On",
        "actionAuxParams": "",
        "controlName": "HoverClickToggleOn",
        "controlLabel": "HoverClickToggleOn",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_click_on_hover_click_toggle_switch_C52083755(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Lowerbarrelbutton/"],
        "viewName": "Lowerbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnChange", 
        "actionDetail": "Off",
        "actionAuxParams": "",
        "controlName": "HoverClickToggleOff",
        "controlLabel": "HoverClickToggleOff",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_03_pen_control_click_on_more_actions_button_C52084815(self):
        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
            time.sleep(1)
            self.fc.fd["pen_control"].click_productivity_chevron_down_arrow()
            time.sleep(1)
            self.fc.fd["pen_control"].click_productivity_chevron_down_arrow()
            time.sleep(1)

        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Lowerbarrelbutton/"],
        "viewName": "Lowerbarrelbutton", 
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
    def test_04_pen_control_click_on_edit_customization_button_C52084816(self):
        self.fc.fd["pen_control"].click_customize_back_button()
        self.fc.fd["pen_control"].click_my_pen_button()
        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_customize_buttons()
            time.sleep(1)
            self.fc.fd["pen_control"].click_my_pen_button()
            time.sleep(1)

        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Lowerbarrelbutton/"],
        "viewName": "Lowerbarrelbutton", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "EditCustomizationButton",
        "controlLabel": "EditCustomizationButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_05_pen_control_click_on_change_to_open_app_button_C52084817(self):

        self.fc.fd["pen_control"].click_customize_buttons()
        time.sleep(3)
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()        
        self.fc.fd["pen_control"].click_productivity_arrow_icon()
        self.fc.fd["pen_control"].click_pen_arrow_icon()
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
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
            self.fc.fd["pen_control"].click_customize_button_email_text()
            time.sleep(1)

        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Lowerbarrelbutton/"],
        "viewName": "Lowerbarrelbutton", 
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