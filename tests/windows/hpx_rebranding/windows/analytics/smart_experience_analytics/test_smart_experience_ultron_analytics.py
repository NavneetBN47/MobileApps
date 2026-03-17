import time
import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Smart_Experience_Analytics(object):

    @pytest.mark.analytics
    def test_01_auto_screen_dimming_on_toggle_switch_event_C52212730(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].verify_device_card_show_up()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        time.sleep(5)
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page()
        time.sleep(5)
        self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming card text is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for i in range(5):
            current_state = self.fc.fd["smart_experience"].get_auto_screen_dimming_toggle_button_state_ultron()
            if current_state == "0":
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                logging.info(f"Clicked to turn off. Attempt {i+1}/5.")
            else:
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                time.sleep(1)
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                logging.info(f"Clicked to turn off after toggling on. Attempt {i+1}/5.")

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "On",
        "viewModule": "SmartExperiences",
        "controlName": "AutoscreendimmingToggle",
        "controlLabel": "AutoscreendimmingToggle",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)

    @pytest.mark.analytics
    def test_02_auto_screen_dimming_off_toggle_switch_event_C52212731(self):
        self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming card text is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for i in range(5):
            current_state = self.fc.fd["smart_experience"].get_auto_screen_dimming_toggle_button_state_ultron()
            if current_state == "1":
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                logging.info(f"Clicked to turn on. Attempt {i+1}/5.")
            else:
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                time.sleep(1)
                self.fc.fd["smart_experience"].click_auto_screen_dimming_toggle_button_ultron()
                logging.info(f"Clicked to turn on after toggling off. Attempt {i+1}/5.")
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "Off",
        "viewModule": "SmartExperiences",
        "controlName": "AutoscreendimmingToggle",
        "controlLabel": "AutoscreendimmingToggle",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)

    @pytest.mark.analytics
    def test_03_privacy_alert_on_toggle_switch_event_C52212728(self):
        self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert card text is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for i in range(5):
            current_state = self.fc.fd["smart_experience"].get_pivacy_alert_toggle_button_state_ultron()
            if current_state == "0":
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                logging.info(f"Clicked to turn on. Attempt {i+1}/5.")
            else:
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                time.sleep(1)
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                logging.info(f"Clicked to turn on after toggling off. Attempt {i+1}/5.")
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "On",
        "viewModule": "SmartExperiences",
        "controlName": "PrivacyalertToggle",
        "controlLabel": "PrivacyalertToggle",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)

    @pytest.mark.analytics
    def test_04_privacy_alert_off_toggle_switch_event_C52212729(self):
        self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert card text is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for i in range(5):
            current_state = self.fc.fd["smart_experience"].get_pivacy_alert_toggle_button_state_ultron()
            if current_state == "1":
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                logging.info(f"Clicked to turn on. Attempt {i+1}/5.")
            else:
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                time.sleep(1)
                self.fc.fd["smart_experience"].click_pivacy_alert_toggle_button_ultron()
                logging.info(f"Clicked to turn on after toggling off. Attempt {i+1}/5.")
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "Off",
        "viewModule": "SmartExperiences",
        "controlName": "PrivacyalertToggle",
        "controlLabel": "PrivacyalertToggle",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)
    
    @pytest.mark.analytics
    def test_05_smart_experience_restore_defaults_event_C52212732(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["smart_experience"].click_restore_default_button_ltwo_page()        
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/RestoreDefault/"],
        "viewName": "RestoreDefault", 
        "action": "OnClick",
        "actionDetail": "",
        "viewModule": "SmartExperiences",
        "controlName": "RestoreDefaultButton",
        "controlLabel": "RestoreDefaultButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "internal_display", 5)     