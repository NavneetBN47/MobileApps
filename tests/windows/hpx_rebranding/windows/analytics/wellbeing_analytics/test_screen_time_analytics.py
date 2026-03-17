import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
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

    def test_01_check_screen_time_toggle_analytics_C52044081(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        time.sleep(1)
        # verify screen time default toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        time.sleep(1)

        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click screen time button 10 times
        for _ in range(10):
            self.fc.fd["wellbeing"].click_screen_time_toggle()
            time.sleep(3)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ScreenTime", 
        "action": "OnChange", 
        "controlName": "ScreenTimeToggle",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 10)

    def test_02_check_send_a_reminder_toggle_analytics_C52044327(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)

        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        time.sleep(1)
        # verify screen time bar chart is displayed
        assert self.fc.fd["wellbeing"].verify_screen_time_bar_chart_show_up(), "Screen time bar chart is not displayed"
        time.sleep(1)
        # judging screen time toggle is off
        if self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0":
            self.fc.fd["wellbeing"].click_screen_time_toggle()
            time.sleep(2)
        # verify screen time toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "1", "Screen time toggle is not on"
        time.sleep(2)
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(1)


        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click screen time button 10 times
        for _ in range(10):
            self.fc.fd["wellbeing"].click_send_a_reminder_toggle()
            time.sleep(3)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "ScreenTime", 
        "action": "OnChange", 
        "controlName": "ReminderToggle",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 10)     

    def test_03_check_send_a_reminder_interval_drop_down_list_analytics_C52044642(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        time.sleep(1)
        # verify screen time bar chart is displayed
        assert self.fc.fd["wellbeing"].verify_screen_time_bar_chart_show_up(), "Screen time bar chart is not displayed"
        time.sleep(1)
        # judging screen time toggle is off
        if self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0":
            self.fc.fd["wellbeing"].click_screen_time_toggle()
            time.sleep(2)
        # verify screen time toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "1", "Screen time toggle is not on"
        time.sleep(2)
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(1)
        # click send a reminder toggle
        self.fc.fd["wellbeing"].click_send_a_reminder_toggle()
        time.sleep(2)
        # verify send a reminder toggle is on
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "1", "Send a reminder toggle is not on"
        time.sleep(2)


        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click alert options in drop down list 5 times
        for _ in range(5):
            self.fc.fd["wellbeing"].click_reminder_interval()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_reminder_interval_1_hour()
            time.sleep(3)
            self.fc.fd["wellbeing"].click_reminder_interval()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_reminder_interval_2_hour()
            time.sleep(3)
            self.fc.fd["wellbeing"].click_reminder_interval()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_reminder_interval_4_hour()
            time.sleep(3)
            self.fc.fd["wellbeing"].click_reminder_interval()
            time.sleep(2)
            self.fc.fd["wellbeing"].click_reminder_interval_30_mins()
            time.sleep(3)


        serial_number = self.fc.get_windows_serial_number()

        custom_1_filter = {
        "viewName": "ScreenTime", 
        "action": "OnValueChange", 
        "controlName": "ReminderSelect",
        "controlAuxParams": "selection=1 hour",
        "serial_number": serial_number
        }

        custom_1_field = {
            "viewName": "ScreenTime",
            "controlAuxParams": "selection=1 hour"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_1_filter, custom_1_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 5)   


        custom_2_filter = {
        "viewName": "ScreenTime", 
        "action": "OnValueChange", 
        "controlName": "ReminderSelect",
        "controlAuxParams": "selection=2 hours",
        "serial_number": serial_number
        }

        custom_2_field = {
            "viewName": "ScreenTime",
            "controlAuxParams": "selection=2 hours"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_2_filter, custom_2_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 5)   
        
        custom_3_filter = {
        "viewName": "ScreenTime", 
        "action": "OnValueChange", 
        "controlName": "ReminderSelect",
        "controlAuxParams": "selection=4 hours",
        "serial_number": serial_number
        }

        custom_3_field = {
            "viewName": "ScreenTime",
            "controlAuxParams": "selection=4 hours"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_3_filter, custom_3_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 5)   
        
        custom_4_filter = {
        "viewName": "ScreenTime", 
        "action": "OnValueChange", 
        "controlName": "ReminderSelect",
        "controlAuxParams": "selection=30 minutes",
        "serial_number": serial_number
        }

        custom_4_field = {
            "viewName": "ScreenTime",
            "controlAuxParams": "selection=30 minutes"
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", custom_4_filter, custom_4_field)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/screen_time_filter.json", "screen_time", 5)   