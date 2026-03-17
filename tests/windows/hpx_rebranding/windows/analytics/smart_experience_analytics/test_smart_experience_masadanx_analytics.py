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

    #need to run on MasadanxSku4
    @pytest.mark.analytics
    def test_01_enable_sure_view_on_toggle_switch_event_C52212724(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].verify_device_card_show_up()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Camera and presence detection card is not present."
        time.sleep(5)
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page()
        assert self.fc.fd["smart_experience"].verify_enable_sure_view_ltwo_page(), "Enable Sure View card text is not displayed"
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "0":
                self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
        current_state = self.fc.fd["smart_experience"].get_enable_sure_view_toggle_button_state()
        if current_state == "1":
            self.fc.fd["smart_experience"].click_enable_sure_view_toggle_button()
            logging.info("Clicked to turn off Sure View.")

        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for i in range(5):
            self.fc.fd["smart_experience"].click_enable_sure_view_toggle_button()
            logging.info(f"Clicked to turn on. Attempt {i+1}/5.")
            time.sleep(2)
            self.fc.fd["smart_experience"].click_enable_sure_view_toggle_button()            
            logging.info(f"Clicked to turn off after toggling on. Attempt {i+1}/5.")

        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "On",
        "viewModule": "SmartExperiences",
        "controlName": "SureviewToggle",
        "controlLabel": "SureviewToggle",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)

    @pytest.mark.analytics
    def test_02_enable_sure_view_off_toggle_switch_event_C52212725(self):
        custom_filter = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", "mfe:/SmartExperiences/FeatureCard/"],
        "viewName": "FeatureCard", 
        "action": "OnChange",
        "actionDetail": "Off",
        "viewModule": "SmartExperiences",
        "controlName": "SureviewToggle",
        "controlLabel": "SureviewToggle",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/smart_experience_filter.json", "vision_ai", 5)      