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
    def test_01_click_pc_device_card_ondevice_list_page_event_C52047664(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/"],
        "viewName": "PcDeviceCards", 
        "action": "OnLoad",
        "controlName": "",
        "controlLabel": "",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/device_details_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/device_details_filter.json", "device_details", 5)

    @pytest.mark.analytics
    def test_02_click_smart_experience_on_pcdevice_page_C52047118(self):
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "SmartexperiencesXCoreCard",
        "controlLabel": "SmartexperiencesXCoreCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    def test_03_click_copy_product_number_pcdevice_page_C52047294(self):
        self.fc.swipe_window(direction="down", distance=5)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_to_copy_product_number_lone_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/ProductInformation/"],
        "viewName": "ProductInformation",
        "viewModule": "ProductInformation", 
        "action": "OnClick",
        "controlName": "CopyProductNumberButton",
        "controlLabel": "CopyProductNumberButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    def test_04_click_copy_serial_number_pcdevice_page_C52047198(self):
        self.fc.swipe_window(direction="down", distance=5)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_to_copy_serial_number_lone_page()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/ProductInformation/"],
        "viewName": "ProductInformation",
        "viewModule": "ProductInformation", 
        "action": "OnClick",
        "controlName": "CopySerialNumberButton",
        "controlLabel": "CopySerialNumberButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)                                     