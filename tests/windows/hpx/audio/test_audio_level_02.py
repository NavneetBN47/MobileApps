from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
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
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    
    def round_up(self,output_value):
        return round(float(output_value))

   #test 1 and 2 thompson due to external device name but can run in any devices.
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_connect_usb_headphone_and_change_volume_from_myhp_verify_the_change_should_get_reflected_on_windows_setting_C31807179(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        self.fc.fd["audio"].click_headset_tab()
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        self.fc.fd["audio"].set_slider_value_increase(100 - self.round_up(output_value),"output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert 100==self.round_up(output_value),"Volume is not increased 100%"
        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_sound()
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()

        output_value1=self.fc.fd["audio"].get_windows_system_sound_output_volume_tab()
        assert 100==self.round_up(output_value1),"Volume is not increased 100%"
        assert self.round_up(output_value) == self.round_up(output_value1),"usb volume not in sync with system volume"
        self.fc.close_windows_settings_panel()

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_connect_35_headphone_and_change_volume_from_myhp_verify_the_change_should_get_reflected_on_windows_setting_C31807182(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=50:
            if self.round_up(output_value)>50:
                self.fc.fd["audio"].set_slider_value_decrease(50,"output_slider")
            else:
                self.fc.fd["audio"].set_slider_value_increase(50,"output_slider")
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert 50==self.round_up(output_value),"Volume is not increased 50%"
        self.fc.fd["devices"].minimize_app()
        self.fc.open_system_settings_sound()
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()

        output_value1=self.fc.fd["audio"].get_windows_system_sound_output_volume_tab()
        assert 50==self.round_up(output_value1),"Volume is not increased 50%"
        assert self.round_up(output_value) == self.round_up(output_value1),"3.5 volume not in sync with system volume"
        self.fc.close_windows_settings_panel() 
