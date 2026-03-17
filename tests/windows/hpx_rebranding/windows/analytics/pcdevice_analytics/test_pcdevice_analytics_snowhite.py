import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_PcDevice_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    @pytest.mark.analytics
    def test_01_click_audio_card_on_pcdevice_page_C52045123(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcaudioXCoreCard",
        "controlLabel": "PcaudioXCoreCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)


    @pytest.mark.analytics
    def test_02_click_system_control_card_on_pcdevice_page_C52045132(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcsystemcontrolXSettingsCard",
        "controlLabel": "PcsystemcontrolXSettingsCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_03_click_wellbeing_card_on_pcdevice_page_C52046533(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcwellbeingXCoreCard",
        "controlLabel": "PcwellbeingXCoreCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_04_click_gesture_card_on_pcdevice_page_C52045128(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcgestureXCoreCard",
        "controlLabel": "PcgestureXCoreCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_05_click_touchpad_on_pcdevice_page_C52045127(self):
        self.fc.swipe_window(direction="down", distance=4)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PctrackpadXHaptictouchpadCard",
        "controlLabel": "PctrackpadXHaptictouchpadCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_06_click_energy_consumption_card_on_pcdevice_page_C52045126(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcecometerXSettingsCard",
        "controlLabel": "PcecometerXSettingsCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    def test_07_click_battery_manager_card_on_pcdevice_page_C52045125(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcbatterymanagerXSettingsCard",
        "controlLabel": "PcbatterymanagerXSettingsCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    def test_08_click_programmable_key_card_on_pcdevice_page_C52045749(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards",  
        "action": "OnCardClick",
        "controlName": "ProgkeyXSettingsCard",
        "controlLabel": "ProgkeyXSettingsCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)                                      