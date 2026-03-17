import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Slice2_Productivity_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
  
    @pytest.mark.analytics
    def test_01_pen_control_productivity_universal_radio_analytics_C52091854(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)

        self.fc.fd["pen_control"].click_radial_menu_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice2_button()
        time.sleep(3)
        
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice2_productivity_show_more_button()
        time.sleep(5)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all productivity options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_radial_slice2_productivity_go_forward_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_go_back_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_page_down_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_page_up_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_redo_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_copy_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_undo_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_paste_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice2_productivity_universal_radio_button()
            time.sleep(1)

        # Get the current serial number for an open search query.
        pytest.serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityUniversalselect",
        "controlLabel": "ProductivityUniversalselect",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_productivity_paste_radio_analytics_C52091877(self):

        # Carry over test start time and serial number from test 01 and query against new filter values
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityPaste",
        "controlLabel": "ProductivityPaste",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_03_pen_control_productivity_undo_radio_analytics_C52091878(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityUndo",
        "controlLabel": "ProductivityUndo",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_04_pen_control_productivity_copy_radio_analytics_C52091899(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityCopy",
        "controlLabel": "ProductivityCopy",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_05_pen_control_productivity_redo_radio_analytics_C52091901(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityRedo",
        "controlLabel": "ProductivityRedo",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)
    
    @pytest.mark.analytics
    def test_06_pen_control_productivity_page_up_radio_analytics_C52091903(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityPageup",
        "controlLabel": "ProductivityPageup",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)  
    
    @pytest.mark.analytics
    def test_07_pen_control_productivity_page_down_radio_analytics_C52098266(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityPagedown",
        "controlLabel": "ProductivityPagedown",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)           

    @pytest.mark.analytics
    def test_08_pen_control_productivity_go_back_radio_analytics_C52098267(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityGoback",
        "controlLabel": "ProductivityGoback",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_09_pen_control_productivity_go_forward_radio_analytics_C52098269(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductivityGoforward",
        "controlLabel": "ProductivityGoforward",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)