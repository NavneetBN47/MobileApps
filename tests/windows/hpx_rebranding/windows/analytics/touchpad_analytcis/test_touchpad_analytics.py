import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
import requests
import json
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Screen_Time_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    def test_01_check_touchpad_enable_gesture_control_toggle_analytics_C52048039(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        # click touchpad card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # verify toupad text show
        self.fc.fd["touchpad"].verify_touchpad_title_show(), "The touchpad title is not shown"
        time.sleep(1)
        # verify enable gesture control button state =0
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "The enable gesture control button state is not 0"
        time.sleep(1)

        # Click enable_gesture_control_toggle 5 times
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "1", "The enable gesture control button state is not 1"
        time.sleep(1)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "The enable gesture control button state is not 0"
        time.sleep(1)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "1", "The enable gesture control button state is not 1"
        time.sleep(1)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "The enable gesture control button state is not 0"
        time.sleep(1)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "1", "The enable gesture control button state is not 1"
        time.sleep(1)

        # get serial number
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewHierarchy": ["base:/", "mfe:/Touchpad/"],
        "viewName": "Touchpad", 
        "action": "OnChange", 
        "serial_number": serial_number
        }

        # Based on the actions we have done compared to the number of events.
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", "touchpad", 5)


    def test_02_click_adjust_feedback_intensity_link_and_verify_analytics_will_send_C52275318(self):
        time.sleep(3)
        self.fc.restart_app()  
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        # click touchpad card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # verify toupad text show
        self.fc.fd["touchpad"].verify_touchpad_title_show(), "The touchpad title is not shown"
        time.sleep(1)
        # verify ajust feedback intensity link show
        self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show(), "The adjust feedback intensity link is not shown"
        time.sleep(1)

        # click adjust feedback intensity link
        for _ in range(5):
            self.fc.fd["touchpad"].click_adjust_feedback_intensity_link()
            time.sleep(2)
            self.fc.close_windows_settings_panel()
            time.sleep(1)

        # get serial number
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewHierarchy": ["base:/", "mfe:/Touchpad/"],
        "viewName": "Touchpad", 
        "action": "OnClick", 
        "serial_number": serial_number
        }

        # Based on the actions we have done compared to the number of events.
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", "touchpad", 5)


    def test_03_click_restore_default_button_and_verify_analytics_will_send_C52275325(self):
        time.sleep(3)
        self.fc.restart_app()  
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        # click touchpad card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # verify toupad text show
        self.fc.fd["touchpad"].verify_touchpad_title_show(), "The touchpad title is not shown"
        time.sleep(1)
        # verify restore default button show
        self.fc.fd["touchpad"].verify_restore_default_button_show(), "The restore default button is not shown"
        time.sleep(1)

        # click restore default button
        for _ in range(5):
            self.fc.fd["touchpad"].click_restore_default_button()
            time.sleep(2)

        # get serial number
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewHierarchy": ["base:/", "mfe:/Touchpad/"],
        "viewName": "Touchpad", 
        "action": "OnClick", 
        "serial_number": serial_number
        }

        # Based on the actions we have done compared to the number of events.
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", "touchpad", 5)

    def test_04_check_touchapd_onload_analytics_will_send_C52417380(self):
        time.sleep(3)
        self.fc.restart_app()  
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # check onload analytics 5 times
        for _ in range(5):
            self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
            time.sleep(2)
            self.fc.fd["touchpad"].click_return_button_on_top_left_corner()
            time.sleep(5)


        # get serial number
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewHierarchy": ["base:/", "mfe:/Touchpad/"],
        "viewName": "Touchpad", 
        "action": "OnLoad", 
        "serial_number": serial_number
        }

        # Based on the actions we have done compared to the number of events.
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/touchpad_filter.json", "touchpad", 5)