import os
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc.ssh_utils import SSH
import MobileApps.resources.const.windows.const as w_const
import pytest
import time, logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Battery_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_bcm_maximize_battery_health_functions_C36124634(self):
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()
        time.sleep(2)
        assert self.fc.fd["battery"].get_charge_option_title_text() == "Charging Options"
        time.sleep(2)
        self.fc.fd["battery"].click_optimize_charging_box()
        time.sleep(2)
        assert self.fc.fd["battery"].get_optimize_battery_box_toggle_status() == "1"
        time.sleep(2)
        self.fc.fd["battery"].click_maximize_charging_box()
        time.sleep(2)
        assert self.fc.fd["battery"].get_maximize_battery_box_toggle_status() == "1"

        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        assert self.fc.fd["battery"].get_maximize_battery_box_toggle_status() == "0"
    

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_days_of_week_C36124635(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()
        time.sleep(2)
        self.fc.fd["battery"].click_optimize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        assert self.fc.fd["battery"].get_sunday_text() == "Sunday"
        assert self.fc.fd["battery"].get_monday_text() == "Monday"
        assert self.fc.fd["battery"].get_tuesday_text() == "Tuesday"
        assert self.fc.fd["battery"].get_wednesday_text() == "Wednesday"
        assert self.fc.fd["battery"].get_thursday_text() == "Thursday"
        assert self.fc.fd["battery"].get_friday_text() == "Friday"
        assert self.fc.fd["battery"].get_saturday_text() == "Saturday"

  

    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_mps_consistency_C36124648(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        assert bool(self.fc.fd["battery"].verify_battery_title_show()) is True
        time.sleep(2)
        self.fc.launch_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["battery"].verify_battery_title_show()) is True

        self.fc.fd["navigation_panel"].navigate_to_settings()
        assert self.fc.fd["settings"].verify_privacy_tab() is True

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_battery_module()
        assert bool(self.fc.fd["battery"].verify_battery_title_show()) is True

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_replace_start_end_time_C38970832(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        assert bool(self.fc.fd["battery"].verify_battery_title_show()) is True
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()

        time.sleep(2)
        self.fc.fd["battery"].click_sunday_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_time_sunday()
        time.sleep(2)
        self.fc.fd["battery"].click_sunday_end_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_time_sunday_2_am()
        assert self.fc.fd["battery"].get_invalid_end_label() == "Invalid end time"

        time.sleep(2)
        self.fc.fd["battery"].click_sunday_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_time_sunday_start()
        time.sleep(2)
        self.fc.fd["battery"].click_sunday_end_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_time_sunday_end()

        assert self.fc.fd["battery"].verify_start_time_missing_text_show() is False
        assert self.fc.fd["battery"].verify_end_time_missing_text_show() is False
