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
    def test_01_click_progkey_menucard_shift_arrow_btn_C52043167(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            #Shift + programmable key menu card
            time.sleep(5)
            self.fc.fd["hppk"].click_progkey_menucard_shift_arrow_btn()
            self.fc.fd["hppk"].click_shift_plus_pk_automation_radio_btn()
            self.fc.fd["hppk"].click_shift_plus_pk_key_sequence_radio_btn()
            self.fc.fd["hppk"].click_shift_plus_pk_text_input_radio_btn()
            self.fc.fd["hppk"].click_shift_plus_pk_not_assigned_default_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()

            #Ctrl + programmable key menu card
            self.fc.fd["hppk"].click_progkey_menucard_ctl_arrow_btn()
            self.fc.fd["hppk"].click_ctrl_plus_pk_automation_radio_btn()
            self.fc.fd["hppk"].click_ctrl_plus_pk_key_sequence_radio_btn()
            self.fc.fd["hppk"].click_ctrl_plus_pk_text_input_radio_btn()
            self.fc.fd["hppk"].click_ctrl_plus_pk_not_assigned_default_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()

            #Alt + programmable key menu card
            self.fc.fd["hppk"].click_progkey_menucard_alt_arrow_btn()
            self.fc.fd["hppk"].click_alt_plus_pk_automation_radio_btn()
            self.fc.fd["hppk"].click_alt_plus_pk_key_sequence_radio_btn()
            self.fc.fd["hppk"].click_alt_plus_pk_text_input_radio_btn()
            self.fc.fd["hppk"].click_alt_plus_pk_not_assigned_default_radio_btn()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()      
       
        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard",
        "viewMode": "",
        "action": "SetCurrentCard",
        "controlName": "ShiftPKHotKeyItem",
        "controlLabel": "ShiftPKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_02_click_automation_radio_button_shift_plus_pk_key_event_C52043272(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "ShiftPK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_03_click_key_sequence_radio_button_shift_plus_pk_key_event_C52043353(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "ShiftPK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_04_click_input_text_radio_button_shift_plus_pk_key_event_C52043360(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "ShiftPK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_05_click_default_radio_button_shift_plus_pk_key_event_C52043370(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "ShiftPK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_06_click_progkey_menucard_ctrl_arrow_btn_event_C52043178(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard", 
        "viewMode": "",
        "action": "SetCurrentCard", 
        "controlName": "CtlPKHotKeyItem",
        "controlLabel": "CtlPKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)      

    @pytest.mark.analytics
    def test_07_click_automation_radio_button_ctrl_plus_pk_key_event_C52043285(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "CtlPK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_08_click_key_sequence_radio_button_ctrl_plus_pk_key_event_C52043354(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "CtlPK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_09_click_input_text_radio_button_ctrl_plus_pk_key_event_C52043361(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "CtlPK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_10_click_default_radio_button_ctrl_plus_pk_key_event_C52043371(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "CtlPK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_11_click_progkey_menucard_alt_arrow_btn_event_C52043190(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/MenuCard/"],
        "viewName": "MenuCard", 
        "viewMode": "",
        "action": "SetCurrentCard", 
        "controlName": "AltPKHotKeyItem",
        "controlLabel": "AltPKHotKeyItem",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5) 

    @pytest.mark.analytics
    def test_12_click_automation_radio_button_alt_plus_pk_key_event_C52043299(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "AltPK",
        "action": "OnChange", 
        "controlName": "AutomationRadioButton",
        "controlLabel": "AutomationRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_13_click_key_sequence_radio_button_alt_plus_pk_key_event_C52043355(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "AltPK",
        "action": "OnChange", 
        "controlName": "KeySequenceRadioButton",
        "controlLabel": "KeySequenceRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_14_click_input_text_radio_button_alt_plus_pk_key_event_C52043363(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "AltPK",
        "action": "OnChange", 
        "controlName": "TextInputRadioButton",
        "controlLabel": "TextInputRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_15_click_default_radio_button_alt_plus_pk_key_event_C52043372(self):
        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard", 
        "viewMode": "AltPK",
        "action": "OnChange", 
        "controlName": "DefaultRadioButton",
        "controlLabel": "DefaultRadioButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)         