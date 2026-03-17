import time
import pytest
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Display_Control_Analytics(object):
    
    @pytest.mark.analytics
    def test_01_on_hdmi_link_event_C52048344(self):
        time.sleep(3)
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()

        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(1)
            self.fc.fd["display_control"].click_display_control_hdmi_link("display_control_advancedsettings_hdmi_link_lthree_page")
            self.fc.fd["display_control"].click_hdmi_link_skip_btn_lfour_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "HDMIInputOSDHelpLink",
        "controlLabel": "HDMIInputOSDHelpLink",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    @pytest.mark.analytics
    def test_02_on_hdmi_switch_event_C52048345(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
            self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "HDMIInputSwitchButton",
        "controlLabel": "HDMIInputSwitchButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_03_on_hdmi_popup_cancel_event_C52048346(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
            time.sleep(3)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "HDMIWarningCancelButton",
        "controlLabel": "HDMIWarningCancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_04_on_hdmi_popup_continue_button_event_C52048347(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
            self.fc.fd["display_control"].click_display_control_hdmi_popup_continue_text()
            time.sleep(3)
            self.fc.swipe_window(direction="up", distance=6)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "HDMIWarningContinueButton",
        "controlLabel": "HDMIWarningContinueButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)    

    def test_05_on_hdmi_popup_do_not_show_again_event_C52048348(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_hdmi_popup_page_do_not_show_again_text()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChange",
        "viewModule": "InternalDisplay",
        "controlName": "HDMIWarningDoNotShowAgainCheckBox",
        "controlLabel": "HDMIWarningDoNotShowAgainCheckBox",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_06_on_change_end_of_red_color_adjustment_setting_event_C52048349(self):
        self.fc.swipe_window(direction="down", distance=6)
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)
        self.fc.fd["display_control"].set_display_red_slider_value_for_analytics(5)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChangeEnd",
        "viewModule": "InternalDisplay",
        "controlName": "RedColorAdjustmentSlider",
        "controlLabel": "RedColorAdjustmentSlider",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_07_on_change_end_of_green_color_adjustment_setting_event_C52048350(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)
        self.fc.fd["display_control"].set_display_green_slider_value_for_analytics(5)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChangeEnd",
        "viewModule": "InternalDisplay",
        "controlName": "GreenColorAdjustmentSlider",
        "controlLabel": "GreenColorAdjustmentSlider",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_08_on_change_end_of_blue_color_adjustment_setting_event_C52048351(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)
        self.fc.fd["display_control"].set_display_blue_slider_value_for_analytics(5)
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChangeEnd",
        "viewModule": "InternalDisplay",
        "controlName": "BlueColorAdjustmentSlider",
        "controlLabel": "BlueColorAdjustmentSlider",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_09_restore_defaults_event_C52048352(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_page()        
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "RestoreDefaultsButton",
        "controlLabel": "RestoreDefaultsButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_10_restore_defaults_cancel_event_C52048353(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "RestoreDefaultWarningCancelButton",
        "controlLabel": "RestoreDefaultWarningCancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_11_restore_defaults_continue_event_C52048354(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
            time.sleep(5)
            self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnClick",
        "viewModule": "InternalDisplay",
        "controlName": "RestoreDefaultWarningContinueButton",
        "controlLabel": "RestoreDefaultWarningContinueButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)

    def test_12_restore_defaults_do_not_show_again_event_C52048355(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_do_not_show_again_checkbox_lthree_page()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/InternalDisplay/AdvancedSettings/"],
        "viewName": "AdvancedSettings", 
        "action": "OnChange",
        "viewModule": "InternalDisplay",
        "controlName": "RestoreDefaultWarningDoNotShowAgainCheckBox",
        "controlLabel": "RestoreDefaultWarningDoNotShowAgainCheckBox",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/display_control_filter.json", "internal_display", 5)                        