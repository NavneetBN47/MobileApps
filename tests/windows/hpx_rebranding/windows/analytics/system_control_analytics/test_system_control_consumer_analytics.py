import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_System_Control_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_click_banalced_toggle_analytics_C52276653(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_balanced_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "BalancedRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)
    
    def test_02_click_cool_toggle_analytics_C52276676(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_balanced_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "CoolRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)
    

    def test_03_click_quiet_toggle_analytics_C52276769(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_quiet_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "QuietRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)

    
    def test_04_click_performance_toggle_analytics_C52276922(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_performance_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "PerformanceRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)

    
    def test_05_click_power_saver_toggle_analytics_C52276923(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_powersaver_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "PowerSaverRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)

    
    def test_06_turn_on_off_focus_mode_toggle_analytics_C52276925(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            time.sleep(2)
            self.fc.fd["system_control"].click_focus_mode_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "FocusModeToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)

    def test_07_click_smart_sence_radio_toggle_verify_send_analytics_C52276649(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(5):
            self.fc.fd["system_control"].click_cool_toggle()
            time.sleep(2)
            assert self.fc.fd["system_control"].get_system_control_cool_radiobutton_is_selected(), "Cool toggle is not selected"
            time.sleep(2)
            self.fc.fd["system_control"].click_smart_sense_radio_button()
            time.sleep(2)
            assert self.fc.fd["system_control"].get_system_smart_sense_radiobutton_is_selected(), "Smart Sense radio button is not selected"
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "AutoRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)
    