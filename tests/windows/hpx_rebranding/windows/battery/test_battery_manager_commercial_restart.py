import pytest
import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_battery_commercial_restart_C51600391(self,request):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        #collect battery charging state
        current_battery_state_before_restart = self.fc.fd["battery"].get_current_battery_percentage_text()
        current_battery_percentage_before_restart = self.fc.fd["battery"].extract_percentage_from_text(current_battery_state_before_restart)
        logging.info("Current battery state: {}".format(current_battery_state_before_restart))
        assert self.fc.fd["battery"].verify_battery_state_charging_state(), "Battery manager page is not displayed"
        self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "changeSystemDate"', timeout = 20)
        self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        self.fc.fd["battery"].get_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_twelve_thirty_am_option_start_time_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_dropbox_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
    
        #restart device
        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"        
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(2)
        current_battery_state_after_restart = self.fc.fd["battery"].get_current_battery_percentage_text()
        current_battery_percentage_after_restart = self.fc.fd["battery"].extract_percentage_from_text(current_battery_state_after_restart)
        assert current_battery_percentage_after_restart <= current_battery_percentage_before_restart, "Battery charged during peak hours (should not charge during scheduled time)"
        logging.info("Battery state before restart: {}".format(current_battery_state_before_restart))
        logging.info("Battery state after restart: {}".format(current_battery_state_after_restart))
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)

