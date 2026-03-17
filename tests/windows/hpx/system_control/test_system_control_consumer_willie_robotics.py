from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc.ssh_utils import SSH

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_System_control_consumer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
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
        yield 
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        cls.fc.insert_usb()
        time.sleep(2)
    
    @pytest.mark.ota
    def test_01_change_pc_power_state_verify_power_saver_will_disable_and_enable_and_power_saver_mode_will_switch_back_C37412385(self):
        self.fc.remove_usb()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
        self.fc.fd["devices"].click_system_control_card()
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_balanced()) is True,"Balanced mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_cool()) is True,"Cool mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_quiet()) is True,"Quiet mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_performance()) is True,"Performance mode is not displayed"
        assert bool(self.fc.fd["system_control"].verify_power_saver()) is True,"Power Saver mode is not displayed"
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        assert self.fc.fd["system_control"].verify_power_saver_is_enabled() =="true", "Power saver mode is not enabled"
        self.fc.fd["system_control"].click_power_saver_consumer()
        assert self.fc.fd["system_control"].verify_power_saver_selected_consumer() =="true", "Power saver mode is not selected"
        self.fc.insert_usb()
        time.sleep(5)
        assert self.fc.fd["system_control"].verify_smart_sense_selected_consumer() =="true", "Smart Sense mode is not selected"
        assert self.fc.fd["system_control"].verify_power_saver_is_enabled() =="false", "Power saver mode is enabled"
        self.fc.remove_usb()
        assert self.fc.fd["system_control"].verify_power_saver_selected_consumer() =="true", "Power saver mode is not selected"
        assert self.fc.fd["system_control"].verify_power_saver_is_enabled() =="true", "Power saver mode is enabled"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_select_each_mode_in_system_control_verify_each_mode_function_will_work_well_C37412386(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_system_control_card()
        #verify modes -smart sense, Balanced, Cool, Quiet, Performance, Power Saver
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
        assert bool(self.fc.fd["system_control"].verify_power_saver()) is True,"Power Saver mode is not displayed"
        self.fc.fd["system_control"].click_power_saver_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "4" == output,"Power saver mode is not selected"
        assert bool(self.fc.fd["system_control"].verify_smart_sense_consumer()) is True,"Smart Sense mode is not displayed"
        self.fc.fd["system_control"].click_smart_sense_consumer()
        result = self.driver.ssh.send_command("powershell 'C:\\test\\system_control.cmd' -Verb runAs")
        logging.info("Output powershell " + str(result["stdout"]))  
        output = self.fc.system_control_cmd()
        assert "5" == output,"Smart Sense mode is not selected"
        self.driver.ssh.send_command('Remove-Item "C:\\test\\system_control.cmd" -Force')