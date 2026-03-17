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
         
    def test_01_energy_consumption_onload_analytics(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(10)

        assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy Consumption module is not present."

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(3) 

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnLoad", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "",
        "controlLabel": "",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_02_energy_consumption_dropdown_selection_analytics_C52081172(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(5)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].select_value_from_consumption_trends_dropdown("last_6_days")
            time.sleep(2)
            self.fc.fd["energy_consumption"].select_value_from_consumption_trends_dropdown("last_6_months")
            time.sleep(2)
            self.fc.fd["energy_consumption"].select_value_from_consumption_trends_dropdown("last_12_hours")
            time.sleep(2)
            
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()


        custom_filter_12_hours = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnValueChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ConsumptionTrendsDropDown",
        "controlLabel": "ConsumptionTrendsDropDown",
        "controlAuxParams": "selection=Last12Hours",
        "serial_number": serial_number
        }

        custom_field_12_hours = {
            "controlAuxParams": "selection=Last12Hours"
        }

        custom_filter_6_days = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnValueChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ConsumptionTrendsDropDown",
        "controlLabel": "ConsumptionTrendsDropDown", 
        "controlAuxParams": "selection=Last6Days",
        "serial_number": serial_number
        }

        custom_field_6_days = {
            "controlAuxParams": "selection=Last6Days"
        }

        custom_filter_6_months = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnValueChange", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ConsumptionTrendsDropDown",
        "controlLabel": "ConsumptionTrendsDropDown",
        "controlAuxParams": "selection=Last6Months",
        "serial_number": serial_number
        }

        custom_field_6_months = {
            "controlAuxParams": "selection=Last6Months"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_12_hours, custom_field_12_hours)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_6_days, custom_field_6_days)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter_6_months, custom_field_6_months)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_03_energy_consumption_learn_more_go_beyond_analytics_C52213463(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_small_go_beyond_hyperlink()
            time.sleep(2)
            
        # close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption",  
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick",    
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "LearMoreGoBeyondLink",
        "controlLabel": "LearMoreGoBeyondLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_04_adjust_power_and_sleep_analytics_C52213465(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_how_to_adjust_power_and_sleep_settings_in_windows_link()
            time.sleep(2)

        # close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)      

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "HowToAdjustPowerAndSleepSettingsInWindowsLink",
        "controlLabel": "HowToAdjustPowerAndSleepSettingsInWindowsLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_05_caring_for_your_battery_link_analytics_C52213466(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_caring_for_your_battery_in_windows_link()
            time.sleep(2)

        # close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "CaringForYourBatteryInWindowsLink",
        "controlLabel": "CaringForYourBatteryInWindowsLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_06_battery_saving_link_analytics_C52213467(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            
            self.fc.fd["energy_consumption"].click_battery_saving_tips_for_windows_link()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "BatterySavingTipsForWindowsLink",
        "controlLabel": "BatterySavingTipsForWindowsLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_07_change_windows_power_mode_link_analytics_C52213468(self):

        assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy Consumption module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_change_the_power_mode_for_your_windows_pc_link()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)       

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ChangeThePowerModeForYourWindowsPcLink",
        "controlLabel": "ChangeThePowerModeForYourWindowsPcLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_08_manage_background_activity_link_analytics_C52213469(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_manage_background_activity_for_apps_in_windows_link()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ManageBackgroundActivityForAppsInWindowsLink",
        "controlLabel": "ManageBackgroundActivityForAppsInWindowsLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)

    def test_09_learn_more_energy_recommendations_link_analytics_C52213470(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_learn_more_about_energy_recommendations_microsoft_support_link()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "LearnMoreAboutEnergyRecommendationsMicrosoftSupportLink",
        "controlLabel": "LearnMoreAboutEnergyRecommendationsMicrosoftSupportLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
    
    def test_10_product_carbon_footprint_link_analytics_C52213472(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_product_carbon_footprint_link_text()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ProductCarbonFootprintLink",
        "controlLabel": "ProductCarbonFootprintLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
    
    def test_11_learn_more_about_go_beyond_link_analytics_C52213473(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_go_beyond_hyperlink()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "LearnMoreAboutGoBeyondLink",
        "controlLabel": "LearnMoreAboutGoBeyondLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)
    
    def test_12_energy_and_the_environment_link_analytics_C52213476(self):
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)   

        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            self.fc.fd["energy_consumption"].click_energy_environment_link()
            time.sleep(2)

        #close opened Microsft Edge windows
        self.driver.ssh.send_command('taskkill /IM msedge.exe /F',  timeout=10)

        self.fc.swipe_window(direction="up", distance=15)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)        

        # Get the current time as the starting time for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ['base:/', 'mfe:/EnergyConsumption/'],
        "viewName": "EnergyConsumption", 
        "viewMode": "",
        "viewModule": "EnergyConsumption",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "EnergyAndTheEnvironmentEpagovLink",
        "controlLabel": "EnergyAndTheEnvironmentEpagovLink",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/energy_consumption_filter.json", "energy_consumption", 5)