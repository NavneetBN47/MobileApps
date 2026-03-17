import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_HPPK_Analytics(object):
    
    # The test is not following the normal flow and it is inconsistent in sending the keys and getting the save events so have to close and launch the app in order to get more than 1 save events
    @pytest.mark.analytics
    def test_01_click_keysequence_save_button_event_C52043385(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            
        time.sleep(3)
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        #key sequence save button event
        for _ in range(2):
            time.sleep(2)
            self.fc.fd["hppk"].click_progkey_menucard_arrow_btn()
            self.fc.fd["hppk"].click_key_sequence_radio_btn()        
            self.fc.fd["hppk"].key_sequence_text_input("H")
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "KeySequenceSaveButton",
        "controlLabel": "KeySequenceSaveButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 2)

    @pytest.mark.analytics
    def test_02_click_keysequence_x_button_event_C52043386(self):
        #key sequence delete X button event
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "KeySequenceIconX",
        "controlLabel": "KeySequenceIconX",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 2)

    @pytest.mark.analytics
    def test_03_click_text_input_save_button_event_C52043387(self):
        time.sleep(3)
        self.fc.fd["hppk"].click_progkey_menucard_arrow_btn()
        self.fc.fd["hppk"].click_text_input_radio_btn()
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            #Text input save  button event
            time.sleep(2)            
            self.fc.fd["hppk"].input_text_input("Hello MyHP !!!")
            self.fc.fd["hppk"].click_key_text_input_save_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "SaveTextInputButton",
        "controlLabel": "SaveTextInputButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].clear_text_input("text_input_area")