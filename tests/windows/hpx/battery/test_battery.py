import os
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc.ssh_utils import SSH
import MobileApps.resources.const.windows.const as w_const
import pytest
import time, logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Battery(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        os.environ['platform']=cls.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()

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


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_battery_information_C36124632(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        assert self.fc.fd["battery"].get_info_title_text() == "Battery Information", "Battery title text Mismatch"
        assert self.fc.fd["battery"].get_new_capacity_text() == "New Capacity", "New Capacity text Mismatch"
        assert self.fc.fd["battery"].get_max_capacity_text() == "Maximum Capacity", "Maximum Capacity text Mismatch"
        assert self.fc.fd["battery"].get_temperature_text() == "Temperature", "Temperature text Mismatch"
        assert self.fc.fd["battery"].get_serial_numer_text() == "Serial Number", "Serial Number text Mismatch"
        assert self.fc.fd["battery"].get_battery_health_text() == "Battery Health", "Battery Health text Mismatch"
    

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_battery_clear_schedule_C36124638(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_battery_module()
        time.sleep(3)
        self.fc.fd["battery"].verify_battery_title_show()
        time.sleep(3)
        assert bool(self.fc.fd["battery"].verify_three_am_item_show()) is False, "The 3:00AM item of battery should not show."
        time.sleep(2)
        if self.fc.fd["battery"].get_schedule_charging_box_toggle_status() == "1":
            self.fc.fd["battery"].click_maximize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_sunday_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_three_am_item()
        time.sleep(2)
        assert self.fc.fd["battery"].get_sunday_start_dropdown() == "SundayStart time03:00", "SundayStart time03:00 text Mismatch"
        time.sleep(2)
        self.fc.fd["battery"].click_sunday_end_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_four_am_item()
        time.sleep(2)
        assert self.fc.fd["battery"].get_sunday_end_dropdown() == "SundayEnd time04:00", "SundayStart time04:00 text Mismatch"
        time.sleep(2)
        self.fc.fd["battery"].click_start_charge_dropdown_list()
        time.sleep(2)
        self.fc.fd["battery"].click_battery_thirty_percent()
        time.sleep(2)
        assert self.fc.fd["battery"].get_start_charge_dropdown_list() == "30%", "The start charge dropdown list should show 30%."
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=7)
        self.fc.fd["battery"].click_clear_schedule()
        time.sleep(2)
        assert bool(self.fc.fd["battery"].verify_three_am_item_show()) is False, "The 3:00AM item of battery should not show."
        time.sleep(2)
        assert bool(self.fc.fd["battery"].verify_four_am_item_show()) is False, "The 4:00AM item of battery should not show."
        time.sleep(2)
        assert self.fc.fd["battery"].get_start_charge_dropdown_list() == "20%", "The start charge dropdown list should show 20%."
        time.sleep(2)

    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_no_crash_C36124646(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.driver.swipe(direction="down", distance=4)
        self.driver.swipe(direction="up", distance=3)
        assert self.fc.fd["battery"].get_info_title_text() == "Battery Information", "Battery text Mismatch"
    

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_charge_options_ui_C36124631(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        assert self.fc.fd["battery"].get_charge_option_title_text() == "Charging Options", "Charging Options text Mismatch"
        assert self.fc.fd["battery"].get_charge_option_subtitle_text() == "Battery manager allows you to customize when and how much your battery charges in order to slow the natural battery aging process and prolong its useful life.", "Battery manager allows... text Mismatch"
        assert self.fc.fd["battery"].get_optimize_battery_text() == "Optimize battery performance", "Optimize battery performance text Mismatch"
        assert self.fc.fd["battery"].get_max_battery_text() == "Maximize battery health", "Maximize battery health text Mismatch"
        assert self.fc.fd["battery"].get_schdedule_battery_text() == "Schedule battery charging", "Schedule battery charging text Mismatch"
    

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_battery_health_screen_C36124633(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(5)
        if self.fc.fd["battery"].get_health_normal_text() == "Normal":
            assert self.fc.fd["battery"].get_health_normal_text() == "Normal", "Normal text Mismatch"
        else:
            assert self.fc.fd["battery"].get_health_calibrate() == "Calibrate", "Calibrate text Mismatch"
    

    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_stop_fusion_check_battery_module_C37961397(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        assert bool(self.fc.fd["battery"].verify_battery_title_show()) is True, "Bttery title is not visible."
        
        time.sleep(2)
        self.fc.close_app()
        time.sleep(2)
        self.driver.ssh.send_command('powershell taskkill /f /im SysInfoCap.exe', raise_e=False, timeout=10)
        time.sleep(2)
        self.driver.ssh.send_command('powershell taskkill /f /im NetworkCap.exe', raise_e=False, timeout=10)

        time.sleep(2)
        self.fc.launch_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        assert bool(self.fc.fd["navigation_panel"].navigate_to_battery_module()) is False, "Bttery module should not be visible."

        time.sleep(2)
        self.driver.ssh.send_command('powershell Start-Service -Name HPNetworkCap', raise_e=False, timeout=10)
        time.sleep(2)
        self.driver.ssh.send_command('powershell Start-Service -Name HPSysInfoCap', raise_e=False, timeout=10)

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_07_battery_manager_using_deep_link_C44257770(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.fd["battery"].open_battery_manager_from_run()
        time.sleep(2)
        self.fc.fd["battery"].verify_battery_title_show()
        time.sleep(2)
        assert self.fc.fd["battery"].get_info_title_text() == "Battery Information", "Battery title text Mismatch"
        assert self.fc.fd["battery"].get_new_capacity_text() == "New Capacity", "New Capacity text Mismatch"
        assert self.fc.fd["battery"].get_max_capacity_text() == "Maximum Capacity", "Maximum Capacity text Mismatch"
        assert self.fc.fd["battery"].get_temperature_text() == "Temperature", "Temperature text Mismatch"
        assert self.fc.fd["battery"].get_serial_numer_text() == "Serial Number", "Serial Number text Mismatch"
        assert self.fc.fd["battery"].get_battery_health_text() == "Battery Health", "Battery Health text Mismatch"
        self.fc.close_myHP()

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_08_system_reaches_full_charge_C44257220(self):
        time.sleep(3)
        self.fc.restart_myHP()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()
        time.sleep(2)
        actual_battery_percenth_text=self.fc.fd["battery"].get_battery_percentage_text()
        if actual_battery_percenth_text.strip() == "100%":
            actual_charging_text = self.fc.fd["battery"].get_charging_text()
            assert actual_charging_text == "Fully Charged", "Fully Charged text is not present though the battery is at 100%"
        else:
            logging.info("This test is to verify Fully charged text only when battery percentage is 100 and here it is less than 100, hence skipped")
