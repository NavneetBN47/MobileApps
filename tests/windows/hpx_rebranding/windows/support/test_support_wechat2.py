from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Wechat2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver) 
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")
        cls.__first_start_HPX(cls)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63681840")
    def test_01_hpx_rebranding(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681840
        """
        self.__close_HPX()
        self.fc.launch_hotkey("hpx://support/device")
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_hp_service_with_wechat_btn()
        self.fc.fd["devices_support_pc_mfe"].click_wechat_ok()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        if self.fc.is_app_open():
            self.sf.close_myhp_app()
        self.fc.launch_myHP()
        self.sf.close_myhp_app()

    def __close_HPX(self):
        if self.fc.is_app_open():
            self.__kill_myhp_protocol_process()

    def __kill_myhp_protocol_process(self):
        """
        Kill the myHP protocol process (myHP:AD2F1837.myHP_v10z8vjag6ke6).
        """
        self.driver.ssh.send_command('powershell taskkill /f /im HP.myHP.exe', raise_e=False, timeout=10)