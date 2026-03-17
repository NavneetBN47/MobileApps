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
        cls.fc.launch_myHP()
        time.sleep(5)

    #all commercial devices
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_non_supported_platform_C33694767(self):
        self.fc.restart_app()
        time.sleep(2)
        if os.environ.get('platform').lower() == 'warpath16w':
            self.fc.fd["navigation_panel"].verify_navigationicon_show()
            self.fc.fd["navigation_panel"].navigate_to_pc_device()
            assert bool(self.fc.fd["devices"].verify_system_control_card()) is False
            logging.info("System Control card is not visible for Non supported platform")
        else:
            logging.info("The test case is supposed to be executed only on warpath16w but current device is {}".format(os.environ.get('platform').lower()))      

    #This test is to verify the system control module only if the device is of gen 11 this is valid for only conmercial
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_supported_platform_C42567878(self):
        time.sleep(5)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        result = self.driver.ssh.send_command('''powershell "Get-WmiObject -Namespace root\HP\InstrumentedBIOS -Class HP_BIOSSetting | where-object name -eq 'Feature Byte'| select value"''')
        logging.info("the feature byte value is : {}".format(str(result['stdout'])))
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        if str(result['stdout']).find('r4') != -1 and str(result['stdout']).find('rP') != -1:
            time.sleep(5)
            assert bool(self.fc.fd["devices"].verify_system_control_card()) is True, "System control is not displayed for the device {} which is gen11".format(os.environ.get('platform').lower())
            self.fc.fd["navigation_panel"].navigate_to_system_control()
            time.sleep(3)
            assert bool(self.fc.fd["system_control"].verify_performance_control_title()) is True
        else:
            logging.info("The device in which the test is running is not a gen11 commercial device")
            assert bool(self.fc.fd["devices"].verify_system_control_card()) is False, "System control is visible for the device {} which is not gen11".format(os.environ.get('platform').lower())