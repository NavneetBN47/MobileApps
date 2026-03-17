import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Battery_Manager_Commercial_Analytics(object):
    
    def test_01_optimize_battery_performance_analytics_C52039877(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(10)

        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery Manager module is not present."
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["battery"].verify_optimize_battery_performancet_radio_button_ltwo(), "Optimize Battery Performance radio button is not present"
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
            time.sleep(3)
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
            time.sleep(3)

        self.fc.swipe_window(direction="up", distance=5)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)  

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/BatteryManager/"],
        "viewName": "BatteryManager", 
        "viewMode": "",
        "viewModule": "BatteryManager",
        "action": "OnChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "OptimizeBatteryPerformance",
        "controlLabel": "OptimizeBatteryPerformance",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", "battery_manager", 5)

    def test_02_maximize_battery_health_analytics_C52039878(self):
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["battery"].verify_maximize_battery_health_management_radio_button(), "Maximize Battery Health radio button is not present"
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
            time.sleep(3)
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
            time.sleep(3)

        self.fc.swipe_window(direction="up", distance=5)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)  

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/BatteryManager/"],
        "viewName": "BatteryManager", 
        "viewMode": "",
        "viewModule": "BatteryManager",
        "action": "OnChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MaximizeBatteryHealth",
        "controlLabel": "MaximizeBatteryHealth",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", "battery_manager", 5)

    def test_03_schedule_battery_charging_analytics_C52039879(self):
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["battery"].verify_schedule_battery_radio_button_ltwo(), "Schedule Battery Charging radio button is not present"
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
            time.sleep(3)
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
            time.sleep(3)
        
        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/BatteryManager/"],
        "viewName": "BatteryManager", 
        "viewMode": "",
        "viewModule": "BatteryManager",
        "action": "OnChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ScheduleBatteryCharging",
        "controlLabel": "ScheduleBatteryCharging",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/battery_manager_commercial_filter.json", "battery_manager", 5)
