import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Screen_Distance_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()


    def test_01_check_screen_distance_toggle_analytics_C52045115(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)     
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # verify screen distance toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen distance toggle is not off"
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click screen distancer button 10 times
        for _ in range(10):
            self.fc.fd["wellbeing"].click_screen_distance_toggle()
            time.sleep(3)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ScreenDistance", 
        "action": "OnChange", 
        "controlName": "ScreenDistanceToggle",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 10)

    def test_02_check_screen_distance_alert_options_select_box_analytics_C52045129(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # click screen distance toggle
        self.fc.fd["wellbeing"].click_screen_distance_toggle()
        time.sleep(2)
        # verify screen distance toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "1", "Screen distance toggle is not on"
        time.sleep(2)
        # verify alert option title is displayed
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options is not displayed"
        time.sleep(2)
        # verify defaut alert options drop down list is nudge
        assert self.fc.fd["wellbeing"].get_alert_options() == "Nudge", "Alert options is not nudge"
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click screen distancer button 5 times
        for _ in range(5):
           self.fc.fd["wellbeing"].click_alert_options()
           time.sleep(2)
           self.fc.fd["wellbeing"].select_alert_options()
           time.sleep(2)
           self.fc.fd["wellbeing"].click_alert_options()
           time.sleep(2)
           self.fc.fd["wellbeing"].select_nudge_options()
           time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_1_filter = {
        "viewName": "ScreenDistance", 
        "action": "OnValueChange", 
        "controlName": "AlertOptionsSelect",
        "controlAuxParams": "selection= Nudge",
        "serial_number": serial_number
        }

        custom_1_field = {
            "viewName": "ScreenDistance",
            "controlAuxParams": "selection= Nudge"
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_1_filter, custom_1_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 5)

        custom_2_filter = {
        "viewName": "ScreenDistance", 
        "action": "OnValueChange", 
        "controlName": "AlertOptionsSelect",
        "controlAuxParams": "selection= Alert",
        "serial_number": serial_number
        }

        custom_2_field = {
            "viewName": "ScreenDistance",
            "controlAuxParams": "selection= Alert"
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_2_filter, custom_2_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 5)

    def test_03_check_set_preferred_distance_button_analytics_C52047199(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # verify screen distance toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen distance toggle is not off"
        time.sleep(2)
        # click screen distance toggle
        self.fc.fd["wellbeing"].click_screen_distance_toggle()
        time.sleep(2)
        # verify screen distance toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "1", "Screen distance toggle is not on"
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click set preferred distance button 5 times
        for _ in range(5):
            self.fc.fd["wellbeing"].click_set_preferred_distance_toggle()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_cancel_button_on_current_set_distance_dialog()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ScreenDistance", 
        "action": "OnClick", 
        "controlName": "SetDistanceButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 5)

    def test_04_check_cancel_button_on_setting_distance_dialog_analytics_C52047666(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # verify screen distance toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen distance toggle is not off"
        time.sleep(2)
        # click screen distance toggle
        self.fc.fd["wellbeing"].click_screen_distance_toggle()
        time.sleep(2)
        # verify screen distance toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "1", "Screen distance toggle is not on"
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click cancel button on preferred distance dialog 5 times
        for _ in range(5):
            self.fc.fd["wellbeing"].click_set_preferred_distance_toggle()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_cancel_button_on_current_set_distance_dialog()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SetDistanceModal", 
        "action": "OnClick", 
        "controlName": "CancelButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 5)

    def test_05_check_set_button_on_setting_distance_dialog_analytics_C52047672(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # verify screen distance toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen distance toggle is not off"
        time.sleep(2)
        # click screen distance toggle
        self.fc.fd["wellbeing"].click_screen_distance_toggle()
        time.sleep(2)
        # verify screen distance toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "1", "Screen distance toggle is not on"
        time.sleep(2)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click set button on preferred distance dialog 5 times
        for _ in range(5):
            self.fc.fd["wellbeing"].click_set_preferred_distance_toggle()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_set_button()
            time.sleep(2)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "SetDistanceModal", 
        "action": "OnClick", 
        "controlName": "SetButton",
        "controlAuxParams": "Selection= 23.6in",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_distance_filter.json", "screen_distance", 5)