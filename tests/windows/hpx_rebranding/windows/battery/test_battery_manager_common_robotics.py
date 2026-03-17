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
    def test_01_battery_manager_device_status_C52989938(self):
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        battery_state = self.fc.fd["device_card"].get_device_battery_charging_state()
        assert "Charged" in battery_state or "Charging" in battery_state, f"Battery is not in Charged or Charging state, current state: {battery_state}"
        self.vcosmos.remove_charger_and_usb()
        self.vcosmos.clean_up_logs()
        battery_state = self.fc.fd["device_card"].get_device_battery_charging_state()
        assert "Battery" in battery_state, f"Battery is not in Battery state, current state: {battery_state}"
        self.vcosmos.add_charger_and_usb()
        self.vcosmos.clean_up_logs()
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()