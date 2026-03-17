import time
import pytest
import logging
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Display_Control_Analytics(object):

    @pytest.mark.analytics
    def test_01_on_mode_change_select_event_C52048336(self):
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
            print("query_start_time",query_start_time)
            list_of_options = ["Neutral", "Warm", "Cool", "HP enhance+", "Native"]
            options = {
                "Neutral": "display_modes_select_box_option_neutral_ltwo_page",
                "Warm": "display_modes_select_box_option_warm_ltwo_page_keelung32",
                "Cool": "display_modes_select_box_option_cool_ltwo_page_keelung32",
                "HP enhance+": "display_modes_select_box_option_hp_enhance_ltwo_page_keelung32",
                "Native": "display_modes_select_box_option_native_ltwo_page_keelung32",
            }
            for option, element_name in options.items():
                if option in list_of_options:
                    logging.info(f"Checking brightness value for {option} mode")
                    self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                    time.sleep(3)
                    self.fc.fd["display_control"].scroll_down_display_modes_list_window()
                    time.sleep(3)
                    self.fc.fd["display_control"].select_display_modes_dropdown_value(element_name)
                    time.sleep(3)
            serial_number = self.fc.get_windows_serial_number()
            custom_filter = {    
            "version": "2.0.0",   
            "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
            "viewName": "BasicSettings", 
            "action": "OnValueChange",
            "viewModule": "InternalDisplay",
            "controlName": "DisplayModeSelect",
            "controlLabel": "DisplayModeSelect",
            "serial_number": serial_number
            }
            analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
            analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    @pytest.mark.analytics
    def test_02_on_out_of_sync_settings_modal_cancel_button_click_event_C52048356(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        self.fc.set_system_brightness_value()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()        
            self.fc.fd["display_control"].click_display_control_out_of_synch_cancel_button_ltwo_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "OutOfSyncModalCancelButton",
        "controlLabel": "OutOfSyncModalCancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    @pytest.mark.analytics
    def test_03_on_out_of_sync_settings_modal_discard_changes_button_click_event_C52048357(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.set_system_brightness_value()
            self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()        
            self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "OutOfSyncModalDiscardChangesButton",
        "controlLabel": "OutOfSyncModalDiscardChangesButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    @pytest.mark.analytics
    def test_04_on_out_of_sync_settings_modal_keep_new_changes_button_click_event_C52048359(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.set_system_brightness_value()
            self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()        
            self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/BasicSettings/"],
        "viewName": "BasicSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "OutOfSyncModalKeepChangesButton",
        "controlLabel": "OutOfSyncModalKeepChangesButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)