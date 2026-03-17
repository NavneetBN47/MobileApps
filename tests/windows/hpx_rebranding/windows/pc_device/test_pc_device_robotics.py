import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_PC_Device_Robotics(object):
    
    #this suite should run on chikorita masadanx platform
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_unplugged_battery_status_C42902485(self):
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card is not diplayed"
        assert "Charging" in self.fc.fd["devicesMFE"].verify_system_charging_status() or "Charged" in self.fc.fd["devicesMFE"].verify_system_charging_status(), "Plugged in charging status not displayed correctly"
        self.vcosmos.remove_charger_and_usb()
        assert "Charging" not in self.fc.fd["devicesMFE"].verify_system_charging_status(), "Unplugged charging status not displayed correctly"
        assert "Charged" not in self.fc.fd["devicesMFE"].verify_system_charging_status(), "Unplugged charging status not displayed correctly"
        self.vcosmos.add_charger_and_usb()
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_close_lid_behaviour_C57290880(self):
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card is not diplayed"
        self.vcosmos.openlid_closelid()
        self.vcosmos.clean_up_logs()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card is not diplayed"
