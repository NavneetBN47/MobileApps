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
    def test_01_click_video_card_on_pcdevice_page_C52045087(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
            time.sleep(5)
            self.fc.fd["video_control"].click_camera_pop_up_cancel_button()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "VideoXControlCard",
        "controlLabel": "VideoXControlCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_02_click_internal_display_card_on_pcdevice_page_C52045124(self):
        time.sleep(3)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcdisplayXControlCard",
        "controlLabel": "PcdisplayXControlCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)

    @pytest.mark.analytics
    def test_03_click_presence_sensing_card_on_pcdevice_page_C52047104(self):
        self.fc.swipe_window(direction="down", distance=2)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_presence_sensing_card_lone_page()
            time.sleep(5)
            self.fc.close_windows_settings_panel()
       
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/PcDeviceActionCards/"],
        "viewName": "PcDeviceActionCards",
        "viewModule": "PcDeviceCards", 
        "action": "OnCardClick",
        "controlName": "PcXActionsPresenceCard",
        "controlLabel": "PcXActionsPresenceCard",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pc_device_filter.json", "pc_device", 5)     