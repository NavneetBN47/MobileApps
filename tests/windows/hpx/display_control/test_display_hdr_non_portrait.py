from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_HDR_Non_Portrait(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.fc.launch_myHP()
        time.sleep(3)
        yield "close windows settings panel"
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    #this suite should run on bucky
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_first_launch_and_dependency_check_C37999254(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        assert self.process_util.check_process_running("DisplayControlService.exe") == False, "DisplayControlService.exe is running"

        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()

        time.sleep(2)
        assert self.fc.fd["display_control"].verify_restore_default_button() == "Restore Defaults", "Restore Defaults button is not displayed"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"
        assert self.fc.fd["display_control"].get_hdr_windows_settings_text() == "Windows display settings", "Windows display settings text is not displayed"


    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_tooltips_C37999255(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_tooltips_icon()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_hdr_tooltips_text() == "Experience the full color gamut of your high dynamic-range screen", "HDR tooltips text is not displayed"

    def test_03_verify_turn_on_hdr_button_C37999258(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)

        if self.fc.fd["display_control"].get_hdr_button_status() == "0":
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()
        else:
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()

        assert self.fc.fd["display_control"].get_hdr_button_status() == "1", "HDR button status is not 1"


    def test_04_verify_turn_off_hdr_button_C37999259(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)

        if self.fc.fd["display_control"].get_hdr_button_status() == "0":
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()
        else:
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()

        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"

    def test_05_verify_windows_display_setting_C37999257(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()

        time.sleep(2)

        assert self.sf.verify_windows_use_hdr_button_show() == True, "Windows use HDR button is not displayed"

        time.sleep(2)
        self.sf.minimize_windows_settings()

        assert self.sf.verify_windows_use_hdr_button_show() == False, "Windows use HDR button is displayed"

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()
        assert self.sf.verify_windows_use_hdr_button_show() == True, "Windows use HDR button is not displayed"
        time.sleep(2)
        self.sf.minimize_windows_settings()
    

    
    def test_06_turn_on_from_windows_settings_C37999267(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()

        if self.sf.get_windows_hdr_button_status() == "0":
            self.sf.click_windows_hdr_button()
        else:
            self.sf.click_windows_hdr_button()
            time.sleep(5)
            self.sf.click_windows_hdr_button()

        time.sleep(5)
        self.fc.close_windows_settings_panel()

        time.sleep(2)
        assert self.fc.fd["display_control"].get_hdr_button_status() == "1", "HDR button status is not 1"
        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_button()

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()
        assert self.sf.get_windows_hdr_button_status() == "0", "Windows HDR button status is not 0"
        time.sleep(3)
        self.fc.close_windows_settings_panel()


    def test_07_turn_off_from_windows_settings_C37999268(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()

        if self.sf.get_windows_hdr_button_status() == "0":
            self.sf.click_windows_hdr_button()
            time.sleep(5)
            self.sf.click_windows_hdr_button()
        else:
            self.sf.click_windows_hdr_button()

        time.sleep(5)
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_button()

        time.sleep(5)
        self.fc.fd["display_control"].click_windows_display_settings()
        self.sf.get_windows_hdr_button_status() == "1"
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.fd["display_control"].click_hdr_button()
    

    @pytest.mark.require_sanity_check(["sanity"])
    def test_08_sync_with_windows_settings_C37999264(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].set_slider_value_increase(100, "Brightness_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "Brightness slider value is not 100"

        time.sleep(2)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        assert self.sf.get_windows_brightness_value() == "100", "Windows brightness value is not 100"
        time.sleep(2)

        self.sf.windows_brightness_decrease(100)
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "0", "Brightness slider value is not 0"

        time.sleep(2)
        self.sf.windows_brightness_increase(100)

        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "Brightness slider value is not 100"
    

    @pytest.mark.require_sanity_check(["sanity"])
    def test_09_verify_restore_default_settings_function_C37999265(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        time.sleep(5)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_title() == "Restore defaults", "Restore defaults title is not displayed"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_subtitle() == "Restore the settings to the HP factory defaults?", "Restore defaults subtitle is not displayed"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_do_not_show_text() == "Do not show again", "Do not show again text is not displayed"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_cancel_text() == "Cancel", "Cancel text is not displayed"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_continue_text() == "Continue", "Continue text is not displayed"
        time.sleep(5)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"
        self.fc.fd["display_control"].set_slider_value_increase(5, "Brightness_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "95", "Brightness slider value is not 95"
        time.sleep(2)
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        assert self.sf.get_windows_brightness_value() == "95", "Windows brightness value is not 95"
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(5)
        self.fc.fd["display_control"].click_restore_pop_up_do_not_show_checkbox()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"
        time.sleep(2)
        self.fc.fd["display_control"].set_slider_value_decrease(5, "Brightness_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "85", "Brightness slider value is not 85"
        time.sleep(2)
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        assert self.sf.get_windows_brightness_value() == "85", "Windows brightness value is not 85"
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button status is not 0"