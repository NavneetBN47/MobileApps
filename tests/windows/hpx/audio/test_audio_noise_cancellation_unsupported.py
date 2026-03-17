import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
import os
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "HPX"

class Test_Suite_Audio_Noise_Cancellation_Unsupported(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request, windows_test_setup):
        cls = cls.__class__
        cls.driver= windows_test_setup
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        os.environ['platform']=cls.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(5)
    
    #To check Gen3 devices we need tool "DCHUAppDiagTool" on desktop.we need to collect log with 
    #the help of this tool and this is third party tool and automation not possible with this tool
    
    #Ralph is Gen3 device and tc can run on gidget and thompson too but tc will fail
    @pytest.mark.consumer
    def test_01_check_noise_cancellation_on_GEN3_device_verify_there_is_no_noise_removal_C40795729(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        if os.environ.get('platform').lower() == 'ralph':
            assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
            self.fc.fd["navigation_panel"].navigate_to_pc_audio()
            time.sleep(2)
            assert bool(self.fc.fd["audio"].verify_noise_removal_show()) is False
            logging.info("Noise removal is not supported on Ralph Gen3 device")
        if (os.environ.get('platform').lower() == 'gidget') or (os.environ.get('platform').lower() == 'thompson'):
            assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
            self.fc.fd["navigation_panel"].navigate_to_pc_audio()
            time.sleep(2)
            assert bool(self.fc.fd["audio"].verify_noise_removal_show()) is True
            logging.info("Noise removal is supported all non Gen 3 devices")
