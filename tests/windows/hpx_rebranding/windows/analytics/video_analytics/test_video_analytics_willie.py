import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Video_Analytics(object):

    @pytest.mark.analytics
    def test_01_cancel_event_C52213474(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()   
        self.fc.fd["devicesMFE"].verify_device_card_show_up()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card.text == "Video", "Video card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
        time.sleep(5)
        assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
        assert self.fc.fd["video_control"].verify_camera_pop_up_cancel_button(), "Camera Pop up Cancel text is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["video_control"].click_camera_pop_up_cancel_button()
            time.sleep(10)
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",    
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/VideoControlModal/"],
        "viewName": "VideoControlModal",
        "action": "OnClick",
        "controlName": "CancelButton",
        "controlLabel": "CancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/video_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/video_control_filter.json", "video", 5)

    @pytest.mark.analytics
    def test_02_continue_event_C52213471(self):        
        assert self.fc.fd["video_control"].verify_camera_pop_up_continue_button(), "Camera Pop up continue button is not displayed"
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["video_control"].click_camera_pop_up_continue_button()
            self.fc.kill_msstore_process()
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",    
        "viewHierarchy": ["base:/", "mfe:/PcDeviceCards/VideoControlModal/"],
        "viewName": "VideoControlModal",
        "action": "OnClick",
        "controlName": "ContinueButton",
        "controlLabel": "ContinueButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/video_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/video_control_filter.json", "video", 5)