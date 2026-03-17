import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
import os
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "HPX"

class Test_Suite_System_Control_Platform(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request, windows_test_setup):
        cls = cls.__class__
        cls.driver= windows_test_setup
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        os.environ['platform']=cls.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(5)

#This suite exclude from warpath
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_verify_test_system_control_sanity_module_launch_C33694763(self):
        time.sleep(5)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        #Click on the Hamburger Menu icon--Hamburger button- with three lines which can be opened and closed.
        # verify home,device,support,setting in let navigation panel
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_pcdevice_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_support_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_setting_module_show()) is True
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_HPPK_card_visible()) is True
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True
        assert bool(self.fc.fd["devices"].verify_support_card_visible()) is True
        #Click on System Control Card--System Control module will be displayed with Thermal settings and power saving modes
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        #verify smart sense,cool,quiet and performance mode
        if os.environ.get('platform').lower() == 'sandwalker':
            assert bool(self.fc.fd["system_control"].verify_smart_sense()) is True
            assert bool(self.fc.fd["system_control"].verify_cool_commercial()) is True
            assert bool(self.fc.fd["system_control"].verify_quiet_commercial()) is True
            assert bool(self.fc.fd["system_control"].verify_performance_commercial()) is True
        else:
            assert bool(self.fc.fd["system_control"].verify_smart_sense()) is True
            assert bool(self.fc.fd["system_control"].verify_performance_commercial()) is True
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_system_control_ui_C33694764(self):
        #Launch HPX Application and navigate to system control page from PC Device
        time.sleep(4)
        self.fc.fd["devices"].click_pc_devices()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(4)
        #verify  Performance control followed by tooltip.
        assert bool(self.fc.fd["system_control"].verify_performance_control_title()) is True
        assert bool(self.fc.fd["system_control"].verify_performance_control_tool_tip()) is True
        assert bool(self.fc.fd["system_control"].verify_performance_control_sub_title()) is True
        assert bool(self.fc.fd["system_control"].verify_smart_sense()) is True
        assert bool(self.fc.fd["system_control"].verify_performance_commercial()) is True
        #.Hover over all tool tips present in the UI.
        #The following content should be displayed when we hover over tooltips:
        #Thermal Setting: Performance controlWhile System Control manages your PC performance, Windows power mode will not work.
        self.fc.fd["system_control"].hover_performance_control_tool_tip()
        assert self.fc.fd["system_control"].get_performance_control_tool_tip() == "Performance ControlWhile System Control manages your PC performance, Windows power mode will not work.","performance Control tool tip is not visible at system control - {}".format(self.fc.fd["system_control"].get_performence_control_tool_tip())
        #Smart Sense(Auto): Automatically adapt the system to your demand with optimization for performance, fan noise and temperature based on the application you are using, placement of the laptop, and battery status.
        self.fc.fd["system_control"].hover_smart_sense_tooltip()
        assert self.fc.fd["system_control"].get_smart_sense_tooltip() == "Smart SenseAutomatically adapt the system to your demand with optimization for performance, fan noise and temperature based on the application you are using, placement of the laptop, and battery status.","smart sence tool tip is not visible at system control - {}".format(self.fc.fd["system_control"].get_smart_sence_tooltip())
        #Cool: Ideal for situations where the device feels warm to the touch. When enabled, fan speed will increase and CPU performance decreases to cool the device.
        time.sleep(2)
        self.fc.fd["system_control"].hover_performance_tooltip_commercial()
        assert self.fc.fd["system_control"].get_performance_tooltip_commercial() == "PerformanceIdeal for software that requires heavy use of the CPU. When enabled, fan speed will increase to cool the device.","performance tool tip is not visible at system control - {}".format(self.fc.fd["system_control"].get_performance_tooltip_commercial())
    
    def test_03_dependency_check_fusion_drivers_C33694762(self):
        self.fc.stop_hpsysinfo_fusion_services()
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is False
        self.fc.close_app()
        self.fc.start_hpsysinfo_fusion_services()