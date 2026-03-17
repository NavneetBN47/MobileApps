from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import MobileApps.resources.const.windows.const as w_const
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_System_control_consumer(object):
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
        yield 
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_verify_system_control_in_pc_device_C37412381(self):
        time.sleep(2)
        self.fc.restart_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
    

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_02_verify_navigation_to_system_control_module_verify_default_ui_C37412383(self):
        time.sleep(4)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
        self.fc.fd["devices"].click_system_control_card()
        assert bool(self.fc.fd["system_control"].verify_performance_control_title_consumer()) is True
        assert bool(self.fc.fd["system_control"].verify_system_control_subtitle()) is True
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True,"Balanced mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_cool()) is True,"Cool mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True,"Quiet mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_performance()) is True,"Performance mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_power_saver()) is True,"Power Saver mode is not displayed"
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_03_verify_system_control_show_on_support_devices_01_C37412387(self):
        #launch hpx with consumer device(willie\herbie\sammy\oski\tuffy\bopeep)-verify system control module show on the support devices
        time.sleep(4)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
    
    
    def test_04_system_control_ui_validation_for_system_control_C37678119(self):
        time.sleep(5)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_control_title_consumer()) is True
        #---------all 6 modes are visible-------
        assert bool(self.fc.fd["system_control"].verify_system_control_title_tooltip_consumer()) is True, "Tooltip is not visible"
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart sense is not visible"
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True, "Balanced is not visible"
        assert bool(self.fc.fd["system_control"].verify_cool()) is True, "Cool is not visible"
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True, "Quiet is not visible"
        assert bool(self.fc.fd["system_control"].verify_performance()) is True, "Performance is not visible"
        assert bool(self.fc.fd["system_control"].verify_power_saver()) is True, "Power saver is not visible"
        #---------tooltip for all 6 modes-------
        self.fc.fd["system_control"].click_smart_sense_tool_tip_consumer()
        assert self.fc.fd["system_control"].get_smart_sense_tooltip_consumer() == "Smart SenseAutomatically adapt the system to your demand with optimization for performance, fan noise and temperature based on the application you are using, placement of the laptop, and battery status."
        self.fc.fd["system_control"].click_balanced_tooltip_consumer()
        assert self.fc.fd["system_control"].get_balanced_tooltip_consumer()  == "BalancedBalances fan speed, performance, and temperature."
        self.fc.fd["system_control"].click_cool_tooltip_consumer()
        assert self.fc.fd["system_control"].get_cool_tooltip_consumer() == "CoolIdeal for situations where the device feels warm to the touch. When enabled, fan speed will increase and CPU performance decreases to cool the device."
        self.fc.fd["system_control"].click_quiet_tooltip_consumer()
        assert self.fc.fd["system_control"].get_quiet_tooltip_consumer() == "QuietIdeal for quiet environments. When enabled, the fan will not turn on or will operate at minimum speed. CPU performance will decrease."
        self.fc.fd["system_control"].click_performance_tooltip_consumer()
        assert self.fc.fd["system_control"].get_performance_tooltip_consumer() == "PerformanceIdeal for software that requires heavy use of the CPU. When enabled, fan speed will increase to cool the device."
        self.fc.fd["system_control"].click_power_saver_tooltip_consumer()
        assert self.fc.fd["system_control"].get_power_saver_tooltip_consumer() == "Power SaverPreserve power to extend PC battery life. This feature will limit CPU performance. The feature is only available when the PC is not connected to AC power."
    
    def test_05_remember_system_control_settings_even_relaunch_app_or_switch_back_from_other_module_C41569395(self):
        time.sleep(5)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_control_title_consumer()) is True
        self.fc.fd["system_control"].click_performance_consumer()
        assert bool(self.fc.fd["system_control"].verify_performance_selected_consumer()) is True
        self.fc.fd["energy_consumption"].click_setting_module()
        assert self.fc.fd["settings"].verify_settings_header() == "Settings"
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_selected_consumer()) is True
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_selected_consumer()) is True

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_06_Optimize_oled_power_consumption_non_supported_platform_C33694776(self):
        self.fc.launch_myHP()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].get_oled_toggle_text())is False, "OLED toggle text is invisible"
        assert bool(self.fc.fd["system_control"].verify_oled_toggle_off()) is False, "OLED toggle is invisible"