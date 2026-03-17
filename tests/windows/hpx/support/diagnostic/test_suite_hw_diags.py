import time
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_HW_Diags(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session

        cls.fc = FlowContainer(cls.driver)   
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["production", "stage", "pie"]) 
    @pytest.mark.testrail("S57581.C31749683")  
    def test_01_Click_Run_hardware_diagnostics(self):
        """
        Verify it can redirect to download page if HW Diags not installed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31749683  
        """
        system_locale = self.fc.get_winsystemlocale().strip().lower()
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(5)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_run_hdware_diags()
        time.sleep(5)
        if not self.process_util.check_process_running("HpHwDiag.exe"):
            webpage = "HWDiag"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/{}-{}/help/hp-pc-hardware-diagnostics".format(system_locale.split('-')[1], system_locale.split('-')[0])
        else:
            self.process_util.kill_process("HpHwDiag.exe")

    @pytest.mark.require_priority(["High", "BVT"])            
    @pytest.mark.require_stack(["production", "stage", "pie"]) 
    @pytest.mark.exclude_platform(["grogu"]) 
    @pytest.mark.testrail("S57581.C31749684")  
    def test_02_Click_Run_hardware_diagnostics(self):
        """
        Verify it can launch HW Diags

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31749684
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_run_hdware_diags()
        time.sleep(3)
        if self.process_util.check_process_running("HpHwDiag.exe"):
            assert self.process_util.check_process_running("HpHwDiag.exe") is True
            self.process_util.kill_process("HpHwDiag.exe")

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["production", "stage", "pie"]) 
    @pytest.mark.testrail("S57581.C32281077")  
    def test_03_Click_Run_hardware_diagnostics(self):
        """
        Verify it can launch HW Diags

        https://hp-testrail.external.hp.com/index.php?/cases/view/32281077
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_run_hdware_diags()
        time.sleep(3)
        if self.process_util.check_process_running("HpHwDiag.exe"):
            assert self.process_util.check_process_running("HpHwDiag.exe") is True
            self.process_util.kill_process("HpHwDiag.exe")
        else:
            webpage = "HW_DIAGS"
            time.sleep(3)
            self.web_driver.wait_for_new_window()
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/us-en/help/hp-pc-hardware-diagnostics"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33692848") 
    @pytest.mark.exclude_platform(["grogu"])    
    def test_04_verify_fusion_HPPTU(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33692848
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_hpptu_btn()  
        assert self.process_util.check_process_running("HPPerformanceTuneup.exe") is True
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33693954") 
    @pytest.mark.exclude_platform(["grogu"])    
    def test_05_verify_fusion_AudioCheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33693954
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_audiocheck_btn()
        assert self.process_util.check_process_running("HPAudioCheck.exe") is True     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33694376") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_06_verify_fusion_oscheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33694376
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_oscheck_btn()
        assert self.process_util.check_process_running("HPOSCheck.exe") is True     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C37677023") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_07_verify_fusion_networkcheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/37677023
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        time.sleep(10)
        self.support_device.click_netcheck_btn() 
        assert self.process_util.check_process_running("HPNetworkCheck.exe") is True
