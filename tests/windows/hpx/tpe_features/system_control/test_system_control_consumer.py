from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc.ssh_utils import SSH
import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_System_control_consumer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        cls.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/locale/system_control.cmd"),r"c:\test\system_control.cmd") 
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(3)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_verify_system_control_in_pc_device_C33627380(self):
        time.sleep(2)
        self.fc.restart_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_navigation_to_system_control_module_verify_default_ui_C33627385(self):
        time.sleep(4)
        self.fc.restart_myHP()
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
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_verify_all_card_tooltips_C33627413(self):
        time.sleep(5)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_control_title_consumer()) is True
        time.sleep(3)
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

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_select_each_mode_in_system_control_verify_each_mode_function_will_work_well_C33627448(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(10)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        #verify modes -smart sense, Balanced, Cool, Quiet, Performance, Power Saver
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        self.fc.fd["system_control"].click_smart_sense_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "5" == output,"Smart Sense mode is not selected"
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True,"Balanced mode is not displayed"
        self.fc.fd["system_control"].click_balanced_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "1" == output,"Balanced mode is not selected"
        assert bool(self.fc.fd["system_control"].verify_cool()) is True,"Cool mode is not displayed"
        self.fc.fd["system_control"].click_cool_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "2" == output,"Cool mode is not selected"
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True,"Quiet mode is not displayed"
        self.fc.fd["system_control"].click_quiet_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "3" == output,"Quiet mode is not selected"
        assert bool(self.fc.fd["system_control"].verify_performance()) is True,"Performance mode is not displayed"
        self.fc.fd["system_control"].click_performance_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "0" == output,"Performance mode is not selected"
        # Power saving can't be automated, because computers have to be plugged in or they shut down, add new manual case on testrail
        self.ssh.remove_file_with_suffix("c:\\test\\",".cmd")

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_05_click_each_mode_verify_each_mode_can_click_C38546889(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify modes -smart sense, Balanced, Cool, Quiet, Performance, Power Saver
        # verify smart sense mode show
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        time.sleep(1)
        # click smart sense mode
        self.fc.fd["system_control"].click_smart_sense_consumer()
        time.sleep(1)
        # verify smart sense mode is selected
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        time.sleep(1)
        # verify balanced mode show
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True,"Balanced mode is not displayed"
        time.sleep(1)
        # click balanced mode
        self.fc.fd["system_control"].click_balanced_consumer()
        time.sleep(1)
        # verify balanced mode is selected
        assert self.fc.fd["system_control"].verify_balanced_selected_consumer() =="true", "Balanced mode is not selected"
        time.sleep(1)
        # verify cool mode show
        assert bool(self.fc.fd["system_control"].verify_cool()) is True,"Cool mode is not displayed"
        time.sleep(1)
        # click cool mode
        self.fc.fd["system_control"].click_cool_consumer()
        time.sleep(1)
        # verify cool mode is selected
        assert self.fc.fd["system_control"].verify_cool_mode_selected_consumer() =="true", "Cool mode is not selected"
        time.sleep(1)
        # verify quiet mode show
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True,"Quiet mode is not displayed"
        time.sleep(1)
        # click quiet mode
        self.fc.fd["system_control"].click_quiet_consumer()
        time.sleep(1)
        # verify quiet mode is selected
        assert self.fc.fd["system_control"].verify_quiet_selected_consumer() =="true", "Quiet mode is not selected"
        time.sleep(1)
        # verify performance mode show
        assert bool(self.fc.fd["system_control"].verify_performance()) is True,"Performance mode is not displayed"
        time.sleep(1)
        # click performance mode
        self.fc.fd["system_control"].click_performance_consumer()
        time.sleep(1)
        # verify performance mode is selected
        assert self.fc.fd["system_control"].verify_performance_selected_consumer() =="true", "Performance mode is not selected"
        time.sleep(1)
        # Power saving can't be automated, because computers have to be plugged in or they shut down
        # verify power saver mode show
        assert bool(self.fc.fd["system_control"].verify_power_saver()) is True,"Power Saver mode is not displayed"
        time.sleep(1)
        # Power saving can't be automated, because computers have to be plugged in or they shut down, add new manual case on testrail
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_06_switch_back_and_relaunch_verify_setting_can_remember_C41582268(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify modes -smart sense, Balanced, Cool, Quiet, Performance, Power Saver
        # verify smart sense mode show
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        time.sleep(1)
        # click smart sense mode
        self.fc.fd["system_control"].click_smart_sense_consumer()
        time.sleep(1)
        # get smart sense mode is selected
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        time.sleep(1)
        # go to other page then back to system control page
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)   
        # verify smart sense mode is selected
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        time.sleep(1)
        # relaunch hpx app 
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify smart sense mode is selected
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        time.sleep(1)

        # verify balanced mode show
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True,"Balanced mode is not displayed"
        time.sleep(1)
        # click balanced mode
        self.fc.fd["system_control"].click_balanced_consumer()
        time.sleep(1)
        # verify balanced mode is selected
        assert self.fc.fd["system_control"].verify_balanced_selected_consumer() =="true", "Balanced mode is not selected"
        # go to other page then back to system control page
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify balanced mode is selected
        assert self.fc.fd["system_control"].verify_balanced_selected_consumer() =="true", "Balanced mode is not selected"
        time.sleep(1)
        # relaunch hpx app 
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify balanced mode is selected
        assert self.fc.fd["system_control"].verify_balanced_selected_consumer() =="true", "Balanced mode is not selected"
        time.sleep(1)

        # verify cool mode show
        assert bool(self.fc.fd["system_control"].verify_cool()) is True,"Cool mode is not displayed"
        time.sleep(1)
        # click cool mode
        self.fc.fd["system_control"].click_cool_consumer()
        time.sleep(1)
        # verify cool mode is selected
        assert self.fc.fd["system_control"].verify_cool_mode_selected_consumer() =="true", "Cool mode is not selected"
        time.sleep(1)
        # go to other page then back to system control page
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify cool mode is selected
        assert self.fc.fd["system_control"].verify_cool_mode_selected_consumer() =="true", "Cool mode is not selected"
        time.sleep(1)
        # relaunch hpx app
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify cool mode is selected
        assert self.fc.fd["system_control"].verify_cool_mode_selected_consumer() =="true", "Cool mode is not selected"
        time.sleep(1)

        # verify quiet mode show
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True,"Quiet mode is not displayed"
        time.sleep(1)
        # click quiet mode
        self.fc.fd["system_control"].click_quiet_consumer()
        time.sleep(1)
        # verify quiet mode is selected
        assert self.fc.fd["system_control"].verify_quiet_selected_consumer() =="true", "Quiet mode is not selected"
        time.sleep(1)
        # go to other page then back to system control page
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify quiet mode is selected
        assert self.fc.fd["system_control"].verify_quiet_selected_consumer() =="true", "Quiet mode is not selected"
        time.sleep(1)
        # relaunch hpx app
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify quiet mode is selected
        assert self.fc.fd["system_control"].verify_quiet_selected_consumer() =="true", "Quiet mode is not selected"
        time.sleep(1)

        # verify performance mode show
        assert bool(self.fc.fd["system_control"].verify_performance()) is True,"Performance mode is not displayed"
        time.sleep(1)
        # click performance mode
        self.fc.fd["system_control"].click_performance_consumer()
        time.sleep(1)
        # verify performance mode is selected
        assert self.fc.fd["system_control"].verify_performance_selected_consumer() =="true", "Performance mode is not selected"
        time.sleep(1)
        # go to other page then back to system control page
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify performance mode is selected
        assert self.fc.fd["system_control"].verify_performance_selected_consumer() =="true", "Performance mode is not selected"
        time.sleep(1)
        # relaunch hpx app
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify performance mode is selected
        assert self.fc.fd["system_control"].verify_performance_selected_consumer() =="true", "Performance mode is not selected"
        time.sleep(1)

        # Power saving can't be automated, because computers have to be plugged in or they shut down, add new manual case on testrail

    @pytest.mark.consumer
    @pytest.mark.function
    def test_07_turn_on_off_focus_tooogle_verify_can_turn_on_off_successfully_C44027538(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify focus mode toggle show off by default
        assert self.fc.fd["system_control"].verify_focus_mode_toggle_off_consumer() == "0", "Focus mode toggle is not off by default"
        time.sleep(1)
        # turn on focus mode toggle
        self.fc.fd["system_control"].click_focus_mode_toggle_off_consumer()
        time.sleep(1)
        # verify focus mode toggle show on
        assert self.fc.fd["system_control"].verify_focus_mode_toggle_on_consumer() == "1", "Focus mode toggle is not on"
        time.sleep(1)
        # turn off focus mode toggle
        self.fc.fd["system_control"].click_focus_mode_toggle_on_consumer()
        time.sleep(1)
        # verify focus mode toggle show off
        assert self.fc.fd["system_control"].verify_focus_mode_toggle_off_consumer() == "0", "Focus mode toggle is not off"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_08_verify_focus_mode_tips_will_show_C39031348(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(2)
        # verify focus mode text show
        assert self.fc.fd["system_control"].verify_focus_mode_text_show() == "Focus mode", "Focus mode text is not displayed"
        time.sleep(1)
        # verify dim background windows text show
        assert self.fc.fd["system_control"].verify_dim_background_windows_text_show() == "Dim background windows", "Dim background windows text is not displayed"
        time.sleep(1)
        # verify dim background windows tips show
        assert self.fc.fd["system_control"].verify_dim_background_windows_tips_icon_show() == "Dim background windowsKeep the selected window in focus while other windows dim to save battery life and keep you focused (not compatible with external displays).", "Dim background windows tips icon is not displayed"
        time.sleep(1)