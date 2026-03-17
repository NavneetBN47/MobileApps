import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_HPPK_Analytics(object):

    @pytest.mark.analytics
    def test_01_click_programmable_key_events_C52043120(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            #programmable key menu card
            time.sleep(3)
            self.fc.fd["hppk"].click_progkey_menucard_arrow_btn()
            self.fc.fd["hppk"].click_automation_radio_btn()
            self.fc.fd["hppk"].click_key_sequence_radio_btn()
            self.fc.fd["hppk"].click_text_input_radio_btn()
            self.fc.fd["hppk"].click_hp_prog_key_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()

            #support key menu card
            self.fc.fd["hppk"].click_hpone_support_key_menucard_arrow_btn()
            self.fc.fd["hppk"].click_hp_support_key_automation_radio_btn()
            self.fc.fd["hppk"].click_key_sequence_spk_radio_btn()
            self.fc.fd["hppk"].click_text_input_spk_radio_btn()
            self.fc.fd["hppk"].click_hp_support_spk_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
   
            #pc device menu card
            self.fc.fd["hppk"].click_hpone_pc_device_menucard_arrow_btn()
            self.fc.fd["hppk"].click_automation_pcpk_radio_btn()
            self.fc.fd["hppk"].click_key_sequence_pcpk_radio_btn()
            self.fc.fd["hppk"].click_text_input_pcpk_radio_btn()
            self.fc.fd["hppk"].click_hp_pc_device_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard",
        "viewMode": "",
        "action": "SetCurrentCard",
        "controlName": "PKHotKeyItem",
        "controlLabel": "PKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_02_click_automation_radio_button_pk_key_event_C52043226(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_03_click_key_sequence_radio_button_pk_key_event_C52043314(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_04_click_input_text_radio_button_pk_key_event_C52043356(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_05_click_hpprog_key_radio_button_pk_key_event_C52043364(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)                       

    @pytest.mark.analytics
    def test_06_click_support_page_key_event_C52043140(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard", 
        "viewMode": "",
        "action": "SetCurrentCard", 
        "controlName": "SPKHotKeyItem",
        "controlLabel": "SPKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_07_click_automation_radio_button_spk_key_event_C52043244(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "SPK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_08_click_keysequence_radio_button_spk_key_event_C52043330(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "SPK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_09_click_text_input_radio_button_spk_key_event_C52043358(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "SPK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_10_click_hp_support_radio_button_spk_key_event_C52043365(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "SPK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)                   

    @pytest.mark.analytics
    def test_11_click_pcdevice_page_key_event_C52043152(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard", 
        "viewMode": "",
        "action": "SetCurrentCard", 
        "controlName": "PCPKHotKeyItem",
        "controlLabel": "PCPKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_12_click_automation_radio_button_pcpk_key_event_C52043259(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PCPK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_13_click_key_sequence_radio_button_pcpk_key_event_C52043342(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PCPK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_14_click_input_text_radio_button_pcpk_key_event_C52043359(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PCPK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_15_click_hppcdevice_radio_button_pcpk_key_event_C52043367(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "PCPK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)                                      