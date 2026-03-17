from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Battery_Manager(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()

    # only on ernstrom consumer device
    def test_01_battery_information_C36124632(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        if self.fc.fd["battery"].get_maximize_battery_health_toggle_status_off() == "0":
            self.fc.fd["battery"].click_maximize_battery_health_toggle_turn_on()
        if  self.fc.fd["battery"].get_maximize_battery_health_toggle_status_on() != "1":
            self.fc.fd["battery"].click_maximize_battery_health_toggle_turn_on()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_on() == "1", "maximize battery health toggle is off"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_on() == "1", "maximize battery health toggle is off"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_on() == "1", "maximize battery health toggle is off"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_on() == "1", "maximize battery health toggle is off"
        self.fc.fd["battery"].click_maximize_battery_health_toggle_turn_off()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_off() == "0","maximize battery health toggle is on"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_off() == "0","maximize battery health toggle is on"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].verify_maximize_battery_health_consumer_show()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle_status_off() == "0","maximize battery health toggle is on" 