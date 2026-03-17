import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):
   

    # this tc is triggering peaktime to trigger notification.
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_schedule_battery_charging_reset_schedule_button_functionality_C51250229(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=6)
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
    
        time.sleep(5)  # Wait for the notification to appear
        start_charging_text = self.fc.fd["battery"].get_start_charging_notification_text()
        time.sleep(3)
        assert "In Charging Scheduler" in start_charging_text,"start charging in notification is not visible - {}".format(start_charging_text)
        self.fc.fd["battery"].verify_reset_schedule_button_ltwo()
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        assert self.fc.fd["battery"].verify_end_charging_notification() is True, "end charging notification is not visible"
        self.fc.fd["battery"].scroll_to_element("threshold_dropdown_ltwo")
        assert self.fc.fd["battery"].get_threshold_dropdown_ltwo() == "20%", "value is not 20%"

    @pytest.mark.function
    def test_02_switching_charging_options_through_ui_C51250244(self):
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
        start_charging_text = self.fc.fd["battery"].get_start_charging_notification_text()
        time.sleep(3)
        assert "In Charging Scheduler" in start_charging_text,"start charging in notification is not visible - {}".format(start_charging_text)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        assert self.fc.fd["battery"].verify_end_charging_notification() is True, "end charging notification is not visible"

    @pytest.mark.function
    def test_03_invalid_peak_shift_on_a_current_day_C51250242(self):
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        #added step to clean notification from previous tc and settings made from 72 to 77
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_notifications_in_windows_notification_clearup()
        self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
        for _ in range(4):
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_sunday_twelve_am_option_ltwo()
            self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_endtime_sunday()
            assert self.fc.fd["battery"].verify_start_charging_notification() is False, "start charging in notification is visible"
            self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
            assert self.fc.fd["battery"].verify_notifications_in_windows_notification_for_myhp() is False, "start charging in notification is visible in notification bar"
            #fucntionality check step 3
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
            self.fc.fd["battery"].verify_reset_schedule_button_ltwo()
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            assert self.fc.fd["battery"].verify_end_charging_notification() is False, "end charging notification is visible"
            self.fc.fd["battery"].scroll_to_element("threshold_dropdown_ltwo")
            assert self.fc.fd["battery"].get_threshold_dropdown_ltwo() == "20%", "value is not 20%"

    @pytest.mark.function
    def test_04_invoke_functionalities_C51250243(self):
        self.fc.swipe_window(direction="up", distance=4)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        for _ in range(4):
            self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
            self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_endtime_sunday()
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
            assert self.fc.fd["battery"].get_error_invalid_start_time_ltwo() == 'Invalid start time'
            assert self.fc.fd["battery"].get_error_invalid_end_time_ltwo() == 'Invalid end time'
            assert self.fc.fd["battery"].verify_start_charging_notification() is False, "start charging in notification is  visible"
            self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
            assert self.fc.fd["battery"].verify_notifications_in_windows_notification_for_myhp() is False, "start charging in notification is visible in notification bar"
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()

    @pytest.mark.function
    def test_05_reset_schedule_button_functionality_C51250246(self):
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
        start_charging_text = self.fc.fd["battery"].get_start_charging_notification_text()
        time.sleep(3)
        assert "In Charging Scheduler" in start_charging_text,"start charging in notification is not visible - {}".format(start_charging_text)
        self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].verify_reset_schedule_button_ltwo()
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        assert self.fc.fd["battery"].verify_end_charging_notification() is True, "end charging notification is not visible"

    @pytest.mark.function
    def test_06_on_clicking_in_end_schedule_notification_C51250255(self):
        #removing notification from  previous tc validate this tc step 133 and 134.
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_notifications_in_windows_notification_clearup()
        self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
        start_charging_text = self.fc.fd["battery"].get_start_charging_notification_text()
        time.sleep(5)
        assert "In Charging Scheduler" in start_charging_text,"start charging in notification is not visible - {}".format(start_charging_text)
        self.fc.close_myHP()
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_start_charging_notification()
        #needs time to land homepage after click
        time.sleep(8)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_07_charging_scheduler_notifications_C51250239(self):
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        self.fc.swipe_window(direction="down", distance=14)
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_notifications_in_windows_notification_clearup()
        self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
        self.fc.fd["battery"].verify_reset_schedule_button_ltwo()
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        assert self.fc.fd["battery"].verify_end_charging_notification() is True, "end charging notification is not visible"
        self.fc.close_myHP()
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_end_charging_notification()
        #needs time to land homepage after click
        time.sleep(8)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
        time.sleep(5)
        start_charging_text = self.fc.fd["battery"].get_start_charging_notification_text()
        time.sleep(5)
        assert "In Charging Scheduler" in start_charging_text,"start charging in notification is not visible - {}".format(start_charging_text)
        self.fc.close_myHP()
        self.fc.fd["battery"].click_notification_tab_with_notification_taskbar()
        self.fc.fd["battery"].click_start_charging_notification()
        #needs time to land homepage after click
        time.sleep(8)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        #revert back time
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)
        #need time to sync type with current time
        time.sleep(10)
        self.fc.close_myHP()