import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Gestures_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_turn_on_off_pause_resume_analytics_C52275332(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            if self.fc.fd["gestures"].verify_gestures_unavailable_notification_show():
                self.fc.swipe_window(direction="down", distance=7)
                time.sleep(2)
                self.fc.fd["gestures"].click_gesture_restore_default_button()
                time.sleep(2)
                self.fc.swipe_window(direction="up", distance=7)
                time.sleep(2)
            time.sleep(3)
            self.fc.fd["gestures"].click_pause_resume_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnChange", 
        "controlName": "PauseResumeToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    

    def test_02_turn_on_off_volume_adjust_analytics_C52276555(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            if self.fc.fd["gestures"].verify_gestures_unavailable_notification_show():
                self.fc.swipe_window(direction="down", distance=7)
                time.sleep(2)
                self.fc.fd["gestures"].click_gesture_restore_default_button()
                time.sleep(2)
                self.fc.swipe_window(direction="up", distance=7)
                time.sleep(2)
            time.sleep(3)
            self.fc.fd["gestures"].click_volume_adjust_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnChange", 
        "controlName": "VolumeAdjustToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    
    def test_03_turn_on_off_page_scroll_analytics_C52276632(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            if self.fc.fd["gestures"].verify_gestures_unavailable_notification_show():
                self.fc.swipe_window(direction="down", distance=7)
                time.sleep(2)
                self.fc.fd["gestures"].click_gesture_restore_default_button()
                time.sleep(2)
                self.fc.swipe_window(direction="up", distance=7)
                time.sleep(2)
            time.sleep(3)
            self.fc.fd["gestures"].click_page_scroll_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnChange", 
        "controlName": "PageScrollToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    
    def test_04_turn_on_off_photo_scroll_analytics_C52276634(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=7)
        time.sleep(2)

        for _ in range(10):
            time.sleep(2)
            self.fc.fd["gestures"].click_gesture_restore_default_button()
            time.sleep(3)
            self.fc.fd["gestures"].click_photo_scroll_toggle()
            time.sleep(2)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnChange", 
        "controlName": "PhotoScrollToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    
    def test_05_turn_on_off_pause_resume_try_out_analytics_C52276637(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            time.sleep(3)
            self.fc.fd["gestures"].click_pause_resume_try_out_button()
            time.sleep(3)
            self.fc.fd["gestures"].click_play_pause_first_cancel_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnClick", 
        "controlName": "PauseResumeTryOutButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    

    def test_06_turn_on_off_volume_adjust_try_out_analytics_C52276639(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            time.sleep(3)
            self.fc.fd["gestures"].click_volume_adjust_try_out_button()
            time.sleep(3)
            self.fc.fd["gestures"].click_volume_adjust_first_cancel_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnClick", 
        "controlName": "VolumeAdjustTryOutButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    

    def test_07_turn_on_off_page_scroll_try_out_analytics_C52276642(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            time.sleep(3)
            self.fc.fd["gestures"].click_page_scroll_try_out_button()
            time.sleep(3)
            self.fc.fd["gestures"].click_page_scroll_first_cancel_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnClick", 
        "controlName": "PageScrollTryOutButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    

    def test_08_turn_on_off_photo_scroll_try_out_analytics_C52276640(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            time.sleep(3)
            self.fc.fd["gestures"].click_photo_scroll_try_out_button()
            time.sleep(3)
            self.fc.fd["gestures"].click_photo_scroll_first_cancel_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnClick", 
        "controlName": "PhotoScrollTryOutButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)
    

    def test_09_turn_on_off_feedback_try_out_analytics_C52276644(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)

        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(10):
            time.sleep(3)
            self.fc.fd["gestures"].click_feedback_message_toggle()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnChange", 
        "controlName": "FeedbackToggle",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 10)


    def test_10_click_restore_default_button_analytics_C52276646(self):
        time.sleep(2)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        query_start_time = datetime.now(timezone.utc).isoformat()

        for _ in range(5):
            time.sleep(3)
            self.fc.fd["gestures"].click_gesture_restore_default_button()
            time.sleep(3)

        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Gestures", 
        "action": "OnClick", 
        "controlName": "RestoreDefaultButton",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/gestures_filter.json", "gestures", 5)
    

