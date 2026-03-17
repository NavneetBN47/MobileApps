from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_HDR_Portrait(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.fc.launch_myHP()
        time.sleep(5)
        yield "close windows settings panel"
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    #this suite should run on willie
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_first_launch_and_dependency_check_C37999234(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        assert self.process_util.check_process_running("DisplayControlService.exe") == True, "DisplayControlService.exe is not running"
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light() == "0", "Low blue light toggle is not off"
        time.sleep(2)
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        assert self.fc.fd["display_control"].verify_restore_default_button() == "Restore Defaults", "Restore Defaults button is not present"
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() is True, "Brightness slider is not present"
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() is True, "Contrast slider is not present"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button is not off"
        assert self.fc.fd["display_control"].get_hdr_windows_settings_text() == "Windows display settings", "Windows display settings is not present"


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_02_verify_tooltips_C37999235(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_tooltips_icon()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_hdr_tooltips_text() == "Experience the full color gamut of your high dynamic-range screen", "HDR tooltips text is not correct"

    @pytest.mark.ota
    def test_03_verify_turn_on_hdr_button_C37999238(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        if(self.fc.fd["display_control"].get_hdr_button_status() == "0"):
            self.fc.fd["display_control"].click_hdr_button()

        time.sleep(2)
        assert self.fc.fd["display_control"].click_work_tile() == False, "Work tile is not clickable"

        time.sleep(2)
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == True, "Disable button is not present"
        assert self.fc.fd["display_control"].get_hdr_disable_text() == "Disable HDR to use all features.", "HDR disable text is not correct"

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_button()


    def test_04_verify_turn_off_hdr_button_C37999239(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        self.driver.swipe(direction="down", distance=2)
        time.sleep(2)
        if self.fc.fd["display_control"].get_hdr_button_status() != "0":
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()

        self.fc.fd["display_control"].click_work_tile()

        time.sleep(2)
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == False, "Disable button is present"
        assert self.fc.fd["display_control"].verify_hdr_disable_text() == False, "HDR disable text is present"
        self.fc.fd["display_control"].click_hdr_button()


    @pytest.mark.ota
    def test_05_turn_off_hdr_on_inline_C37999240(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        if self.fc.fd["display_control"].get_hdr_button_status() == "0":
            time.sleep(2)
            self.fc.fd["display_control"].click_hdr_button()

        time.sleep(2)
        self.fc.fd["display_control"].click_disable_button()

        time.sleep(2)
        self.fc.fd["display_control"].click_work_tile()
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == False, "Disable button is present"
        assert self.fc.fd["display_control"].verify_hdr_disable_text() == False, "HDR disable text is present"
        self.fc.fd["display_control"].click_hdr_button()


    @pytest.mark.ota
    def test_06_verify_windows_display_setting_C37999237(self):
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()

        time.sleep(2)

        assert self.sf.verify_windows_use_hdr_button_show() == True, "Use HDR button is not present"

        time.sleep(2)
        self.sf.minimize_windows_settings()

        assert self.sf.verify_windows_use_hdr_button_show() == False, "Use HDR button is present"

        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()
        assert self.sf.verify_windows_use_hdr_button_show() == True, "Use HDR button is not present"
        time.sleep(2)
        self.sf.minimize_windows_settings()

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_07_sync_with_windows_settings_C37999245(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.fd["display_control"].set_slider_value_increase(100, "Brightness_slider")
        time.sleep(5)
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
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "Brightness slider value is not 100"


    
    @pytest.mark.ota
    def test_08_turn_on_from_windows_settings_C37999246(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
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

        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(1)
        assert self.fc.fd["display_control"].get_hdr_button_status() == "1", "HDR button is not on"
        time.sleep(2)
        assert self.fc.fd["display_control"].click_work_tile() == False, "Work tile is not clickable"
        time.sleep(2)
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == True, "Disable button is not present"
        assert self.fc.fd["display_control"].get_hdr_disable_text() == "Disable HDR to use all features.", "HDR disable text is not correct"

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_button()

        time.sleep(5)
        self.fc.fd["display_control"].click_work_tile()
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == False, "Disable button is present"
        assert self.fc.fd["display_control"].verify_hdr_disable_text() == False, "HDR disable text is present"
        self.fc.fd["display_control"].click_hdr_button()


    @pytest.mark.ota
    def test_09_turn_off_from_windows_settings_C37999247(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
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
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button is not off"
        self.fc.fd["display_control"].click_work_tile()
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == False, "Disable button is present"
        assert self.fc.fd["display_control"].verify_hdr_disable_text() == False, "HDR disable text is present"

        time.sleep(2)
        self.fc.fd["display_control"].click_hdr_button()

        time.sleep(5)
        assert self.fc.fd["display_control"].click_work_tile() == False, "Work tile is not clickable"
        time.sleep(2)
        assert self.fc.fd["display_control"].verfiy_disable_button_show() == True, "Disable button is not present"
        assert self.fc.fd["display_control"].get_hdr_disable_text() == "Disable HDR to use all features.", "HDR disable text is not correct"
        time.sleep(2)
        self.fc.fd["display_control"].click_disable_button()

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_10_verify_restore_default_settings_function_C37999249(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(3)
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_title() == "Restore defaults", "Restore defaults title is not correct"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_subtitle() == "Restore the settings to the HP factory defaults?", "Restore defaults subtitle is not correct"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_do_not_show_text() == "Do not show again", "Do not show again text is not correct"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_cancel_text() == "Cancel", "Cancel text is not correct"
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_continue_text() == "Continue", "Continue text is not correct"
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button is not off"
        self.fc.fd["display_control"].set_slider_value_increase(5, "Brightness_slider")
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "95", "Brightness slider value is not 95"
        time.sleep(5)
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
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button is not off"
        time.sleep(2)
        self.fc.fd["display_control"].set_slider_value_decrease(5, "Brightness_slider")
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "85", "Brightness slider value is not 85"
        time.sleep(5)
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        assert self.sf.get_windows_brightness_value() == "85", "Windows brightness value is not 85"
        time.sleep(2)
        self.driver.swipe(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_hdr_button_status() == "0", "HDR button is not off"

    # Test case should run only on portrait devices
    def test_11_Display_control_C33267396(self):
        time.sleep(3)
        try:
            result = self.driver.ssh.send_command( '''Get-Package -Name "*HP Display Control*" | Select-Object Name, Version''')['stdout'].strip()
            logging.info(f"The current devices has {result}")
            is_package_version_present = (result !="")
            is_display_control_service_preinstall_file_present = self.driver.ssh.send_command( '''Test-Path -Path "{}" -PathType Container'''.format(w_const.TEST_DATA.DISPLAY_CONTROL_SERVIVE))['stdout'].strip()
            is_hpdc_preinstall_file_present = self.driver.ssh.send_command( '''Test-Path -Path "{}" -PathType Container'''.format(w_const.TEST_DATA.HPDC_SERVICE))['stdout'].strip()
            is_hpdc_installed = is_package_version_present and is_display_control_service_preinstall_file_present and is_hpdc_preinstall_file_present
            assert is_hpdc_installed, "HPDC service is not install please install it manually"
        except Exception as e:
            logging.error(str(e))
            assert False, "HPDC service is not install please install it manually"