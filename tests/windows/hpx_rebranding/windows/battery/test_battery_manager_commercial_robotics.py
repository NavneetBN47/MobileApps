import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#Tests designed to run on MasadaNX robotics device with USB and charger plug/unplug robotics

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_Battery_Control(object):
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_battery_manager_charging_and_discharging_status_C51250250(self):
        try:
            self.fc.launch_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=6)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
            time.sleep(2)
            battery_state = self.fc.fd["battery"].get_battery_charging_state()
            assert battery_state == "Charging", f"Battery is not in charging state, current state: {battery_state}"
            self.vcosmos.remove_charger_and_usb()
            self.vcosmos.clean_up_logs()
            battery_state = self.fc.fd["battery"].get_battery_charging_state()
            assert battery_state == "Discharging", f"Battery is not in discharging state, current state: {battery_state}"
            self.vcosmos.add_charger_and_usb()
            self.vcosmos.clean_up_logs()
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
            self.fc.swipe_window(direction="up", distance=6)
            battery_state = self.fc.fd["battery"].get_battery_charging_state()
            assert battery_state == "Fully charged", f"Battery is not in fully charged state, current state: {battery_state}"
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        finally:
            self.fc.close_myHP()

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_battery_manager_scheduler_notification_start_and_stop_unplugged_C51250236(self):
        try:
            self.fc.launch_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=6)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
            self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            self.vcosmos.remove_charger_and_usb()
            self.vcosmos.clean_up_logs()
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
            self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
            self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
            assert self.fc.fd["battery"].verify_start_charging_notification() is not False, "Start charging notification toast is not displayed with system unplugged"
            assert self.fc.fd["battery"].get_start_charging_notification_text() == "New notification from HP, In Charging Scheduler, .. 1 of 1", "Start charging notification text is not \"In Charging Scheduler\""
            self.fc.fd["battery"].click_retask_notification_toast_x_button()
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            time.sleep(5)  # Wait for end charging notification
            assert self.fc.fd["battery"].verify_end_charging_notification() is not False, "End charging notification toast is not displayed with system unplugged"
            assert self.fc.fd["battery"].get_end_charging_notification_text() == "New notification from HP, Charging Scheduler Ended, .. 1 of 1", "End charging notification text is not \"Charging Scheduler Ended\""
            self.fc.fd["battery"].click_retask_notification_toast_x_button()
            self.vcosmos.rapid_unplug()
            self.vcosmos.clean_up_logs()
            assert self.fc.fd["battery"].verify_start_charging_notification() is False, "Start charging notification toast displayed after rapid unplug"
            self.fc.fd["battery"].scroll_to_element("optimize_battery_performance_radio_button_ltwo")
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        finally:
            self.fc.close_myHP()
            self.vcosmos.add_charger_and_usb()
            self.vcosmos.clean_up_logs()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_battery_manager_scheduler_notification_start_and_stop_plugged_in_C51250237(self):
        try:
            self.fc.launch_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=6)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
            self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
            self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
            self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
            assert self.fc.fd["battery"].verify_start_charging_notification() is not False, "Start charging notification toast is not displayed with system plugged in"
            assert self.fc.fd["battery"].get_start_charging_notification_text() == "New notification from HP, In Charging Scheduler, .. 1 of 1", "Start charging notification text is not \"In Charging Scheduler\""
            self.fc.fd["battery"].click_retask_notification_toast_x_button()
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            time.sleep(5)  # Wait for end charging notification
            assert self.fc.fd["battery"].verify_end_charging_notification() is not False, "End charging notification toast is not displayed with system plugged in"
            assert self.fc.fd["battery"].get_end_charging_notification_text() == "New notification from HP, Charging Scheduler Ended, .. 1 of 1", "End charging notification text is not \"Charging Scheduler Ended\""
            self.fc.fd["battery"].click_retask_notification_toast_x_button()
            self.vcosmos.rapid_unplug()
            self.vcosmos.clean_up_logs()
            assert self.fc.fd["battery"].verify_start_charging_notification() is False, "Start charging notification toast displayed after rapid unplug"
            self.fc.fd["battery"].scroll_to_element("optimize_battery_performance_radio_button_ltwo")
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        finally:
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_battery_manager_scheduler_notification_unplug_C51600295(self):
        try:
            self.fc.launch_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=6)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
            self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
            self.fc.fd["battery"].get_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_start_time_sunday_ltwo()
            self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
            self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
            self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
            assert self.fc.fd["battery"].verify_start_charging_notification() is not False, "Start charging notification toast is not displayed"
            assert self.fc.fd["battery"].get_start_charging_notification_text() == "New notification from HP, In Charging Scheduler, .. 1 of 1", "Start charging notification text is not"
            self.fc.fd["battery"].click_retask_notification_toast_x_button()
            self.vcosmos.rapid_unplug()
            self.vcosmos.clean_up_logs()
            assert self.fc.fd["battery"].verify_start_charging_notification() is False, "Start charging notification toast displayed after rapid unplug"
            self.fc.fd["battery"].click_reset_schedule_button_ltwo()
            self.fc.fd["battery"].scroll_to_element("optimize_battery_performance_radio_button_ltwo")
            self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        finally:
            self.fc.close_myHP()
            self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)