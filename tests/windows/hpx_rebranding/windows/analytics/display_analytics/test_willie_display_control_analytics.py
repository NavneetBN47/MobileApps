import time
import pytest
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Display_Control_Analytics(object):

    @pytest.mark.analytics
    def test_01_on_hdr_switch_toggle_event_C52048337(self):
        time.sleep(3)
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnChange",
        "viewModule": "InternalDisplay",
        "controlName": "HdrSwitch",
        "controlLabel": "HdrSwitch",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page()

    @pytest.mark.analytics
    def test_02_onchange_event_contrast_setting_event_C52048339(self):
        self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()    
        query_start_time = datetime.now(timezone.utc).isoformat()
        self.fc.fd["display_control"].set_display_contrast_slider_value_for_analytics(5)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChangeEnd",
        "viewModule": "InternalDisplay",
        "controlName": "ContrastSlider",
        "controlLabel": "ContrastSlider",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    @pytest.mark.analytics
    def test_03_lbl_scheduler_switch_toggle_event_C52048340(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChange",
        "viewModule": "InternalDisplay",
        "controlName": "LblSchedulerSwitch",
        "controlLabel": "LblSchedulerSwitch",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()

    @pytest.mark.analytics
    def test_04_schedule_turnon_time_select_event_C52048342(self):
        if self.fc.fd["display_control"].get_display_control_low_blue_light_toggle_lthree_page() == "0":
            self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_low_blue_light_turnon_dropdown_lthree_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_low_blue_light_turnon_dropdown_hrs_eleven_pm_lthree_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnValueChange",
        "viewModule": "InternalDisplay",
        "controlName": "SelectTurnOnTimeDropdown",
        "controlLabel": "SelectTurnOnTimeDropdown",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()

    @pytest.mark.analytics
    def test_05_schedule_turnoff_time_select_event_C52048343(self):
        if self.fc.fd["display_control"].get_display_control_low_blue_light_toggle_lthree_page() == "0":
            self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()
        self.fc.swipe_window(direction="down", distance=3)    
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_low_blue_light_turnoff_dropdown_lthree_page()
            time.sleep(5)
            self.fc.fd["display_control"].click_display_control_low_blue_light_turnoff_dropdown_hrs_eight_am_lthree_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnValueChange",
        "viewModule": "InternalDisplay",
        "controlName": "SelectTurnOffTimeDropdown",
        "controlLabel": "SelectTurnOffTimeDropdown",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
        self.fc.fd["display_control"].click_display_control_low_blue_light_toggle_lthree_page()    