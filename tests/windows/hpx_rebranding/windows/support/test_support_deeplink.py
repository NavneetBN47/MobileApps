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
class Test_Suite_Deeplink(object):
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
    @pytest.mark.testrail("S57581.C63681828")
    def test_01_hpx_rebranding_C63681828(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681828
        """
        self.__close_HPX()
        self.fc.launch_hotkey("myhp://support/device")
        time.sleep(10)
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63681836")   
    def test_02_hpx_rebranding_C63681836(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681836
        """
        self.__close_HPX()
        self.fc.launch_hotkey("hpx://support/device")
        time.sleep(10)
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63681837")
    def test_03_hpx_rebranding_C63681837(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681837
        """
        self.__close_HPX()
        self.fc.launch_hotkey("myhp://support")
        time.sleep(10)
        assert self.fc.fd["devicesMFE"].verfiy_device_container_show() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63681838")   
    def test_04_hpx_rebranding_C63681838(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681838
        """
        self.__close_HPX()
        self.fc.launch_hotkey("hpx://support")
        time.sleep(10)
        assert self.fc.fd["devicesMFE"].verfiy_device_container_show() == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63681839")
    def test_05_hpx_rebranding_C63681839(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681839
        """
        self.__close_HPX()
        self.fc.launch_hotkey("myhp://support-va")
        time.sleep(10)
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63681840")
    def test_06_hpx_rebranding_C63681840(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63681840
        """
        self.__close_HPX()
        self.fc.launch_hotkey("hpx://support-va")
        time.sleep(10)
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

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