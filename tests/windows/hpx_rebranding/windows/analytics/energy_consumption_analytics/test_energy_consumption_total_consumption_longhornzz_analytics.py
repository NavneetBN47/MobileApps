import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Energy_Consumption_Analytics(object):

    def test_01_energy_consumption_total_consumption_dropdown_analytics_C52213464(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(10)

        assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy Consumption module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].select_value_from_total_energy_consumption_dropdown("last_month")
            time.sleep(2)
            self.fc.fd["energy_consumption"].select_value_from_total_energy_consumption_dropdown("last_week")
            time.sleep(2)

        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)
    
        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter_month = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnValueChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "TotalEnergyConsumptionDropDown",
        "controlLabel": "TotalEnergyConsumptionDropDown",
        "controlAuxParams": "selection=LastMonth",
        "serial_number": serial_number
        }

        custom_field_month = {
            "controlAuxParams": "selection=LastMonth"
        }

        custom_filter_week = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnValueChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "TotalEnergyConsumptionDropDown",
        "controlLabel": "TotalEnergyConsumptionDropDown", 
        "controlAuxParams": "selection=LastWeek",
        "serial_number": serial_number
        }

        custom_field_week = {
            "controlAuxParams": "selection=LastWeek"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_month, custom_field_month)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_week, custom_field_week)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_02_energy_consumption_show_more_button_analytics_C52213477(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=8)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_show_more_button()
            time.sleep(2)
            self.fc.fd["energy_consumption"].click_show_less_button()
            time.sleep(2)

        self.fc.swipe_window(direction="up", distance=8)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter_month = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "TotalEnergyConsumptionShowMoreButton",
        "controlLabel": "TotalEnergyConsumptionShowMoreButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }
        
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_month)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
   
    def test_03_energy_consumption_show_less_button_analytics_C52213478(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=8)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_show_more_button()
            time.sleep(2)
            self.fc.fd["energy_consumption"].click_show_less_button()
            time.sleep(2)

        self.fc.swipe_window(direction="up", distance=8)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter_month = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "TotalEnergyConsumptionShowLessButton",
        "controlLabel": "TotalEnergyConsumptionShowLessButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }
        
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_month)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)