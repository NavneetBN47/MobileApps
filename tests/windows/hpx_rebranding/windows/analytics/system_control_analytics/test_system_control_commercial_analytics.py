import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_System_Control_Commercial_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_system_control_on_load_analytics_C52080189(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(2)

        for i in range(5):  
            self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)


        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnLoad",
        "controlName": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)
    
    def test_02_smart_sense_toggle_analytics_C52080197(self):
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
            self.fc.fd["system_control"].click_performance_toggle()
            time.sleep(2)
            self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "SmartSenseRadioButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 5)
    

    def test_03_peformance_toggle_analytics_C52080199(self):
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
            self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
            time.sleep(2)
            self.fc.fd["system_control"].PerformanceRadioButton()
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

    def test_04_user_switch_on_off_power_saving_mode_C52080370(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        # verify power saving mode is shown 
        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Power Saving Mode is not visible"
        time.sleep(1)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(10):
            self.fc.fd["system_control"].click_optimize_oled_toggle()
            time.sleep(2)


        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "PowerSavingModeToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 10)

    
    def test_04_user_switch_on_off_smart_resource_optimizer_toggle_C60907125(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)

        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Power Saving Mode is not visible"
        time.sleep(1)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        for _ in range(10):
            self.fc.fd["system_control"].click_smart_resource_optimizer_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SystemControl", 
        "action": "OnChange", 
        "controlName": "SmartResourceOptimizerToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/system_control_filter.json", "system_control", 10)

