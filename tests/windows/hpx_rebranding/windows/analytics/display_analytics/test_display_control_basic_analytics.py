import time
import pytest
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Display_Control_Analytics(object):

    @pytest.mark.analytics
    def test_01_on_internal_display_mfe_load_analytics_C52048334(self):
        time.sleep(3)
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(10)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",    
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/"],
        "viewName": "InternalDisplay",
        "action": "OnLoad",
        "controlName": "",
        "controlLabel": "",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
    
    @pytest.mark.analytics
    def test_02_on_change_end_event_of_brightness_setting_C52048335(self):
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."        
        query_start_time = datetime.now(timezone.utc).isoformat()
        print("query_start_time",query_start_time)
        self.fc.fd["display_control"].set_display_brightness_slider_value_for_analytics(5)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnChangeEnd",
        "viewModule": "InternalDisplay",
        "controlName": "BrightnessSlider",
        "controlLabel": "BrightnessSlider",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)
 
    @pytest.mark.analytics
    def test_03_on_advanced_settings_navigation_button_click_C52048338(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "AdvancedSettingsNavigationButton",
        "controlLabel": "AdvancedSettingsNavigationButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)    
              