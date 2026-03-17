import pytest
import time
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_battery_consumer_restart_C51602120(self,request):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"        
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        #This is a workaround as sometimes the battery manager title is not detected properly, and it lands to L0 instead of battery manager L2
        if not self.fc.fd["battery"].verify_battery_manager_title_ltwo():
            assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
            self.fc.close_myHP()
            time.sleep(5)
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
        
        if self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0":
            max_battery_health_toggle_state = "0"
        else:
            max_battery_health_toggle_state = "1"

        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"        
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
         #This is a workaround as sometimes the battery manager title is not detected properly, and it lands to L0 instead of battery manager L2
        if not self.fc.fd["battery"].verify_battery_manager_title_ltwo():
            assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
            self.fc.close_myHP()
            time.sleep(5)
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
        
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == max_battery_health_toggle_state, "Maximize Battery Health toggle state is not retained after restart"
        self.fc.close_myHP()
