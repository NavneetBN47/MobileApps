import time
import re
import MobileApps.resources.const.windows.const as w_const
from packaging import version
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_Fusion(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.stack = request.config.getoption("--stack")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)    
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]

        cls.fc = FlowContainer(cls.driver)  
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.hpid = cls.fc.fd["hpid"]  
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.devices = cls.fc.fd["devices"]
        cls.home = cls.fc.fd["home"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.settings = cls.fc.fd["settings"]
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "chat.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()    
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
            self.__kill_process()
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33139305") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_01_verify_fusion_resource_folder(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33139305
        """
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        assert self.driver.ssh.check_directory_exist(w_const.TEST_DATA.SUPPORT_RESOURCES_PATH) is True

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C37671718") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_02_verify_fusion_lanunch_chat(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/37671718
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], b_sign=True)   
        time.sleep(3)     
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_chat_now_btn_state() == "true"
            self.support_device.click_chatnow_btn()
            time.sleep(30)
            assert self.process_util.check_process_running("OCChat.exe") is True      
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33692848") 
    @pytest.mark.exclude_platform(["grogu"])    
    def test_03_verify_fusion_HPPTU(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33692848
        """
        version_json=self.driver.ssh.send_command('get-appxpackage *myHP* | select Version',  raise_e=False, timeout=10)
        result = re.search("([0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5})", str(version_json))
        install_build_version=result.group(1)
        print ("install_build_version: " + install_build_version)
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        file_path = "C:\\Program Files\\HP\\HP Enabling Services\\AppHelperCap.exe"
        fusion_version = self.fc.get_file_version(file_path)
        print ("fusion_version: " + fusion_version)
        # if version.parse(install_build_version) >= version.parse("31.52411.259.0") and version.parse(fusion_version) < version.parse("1.63.3600.0"):
        #     assert self.support_device.verify_hpptu_btn() is False
        # else:
        self.support_device.click_hpptu_btn()  
        assert self.process_util.check_process_running("HPPerformanceTuneup.exe") is True
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33693954") 
    @pytest.mark.exclude_platform(["grogu"])    
    def test_04_verify_fusion_AudioCheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33693954
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 

        self.support_device.click_audiocheck_btn()
        assert self.process_util.check_process_running("HPAudioCheck.exe") is True     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33694376") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_05_verify_fusion_oscheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33694376
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 

        self.support_device.click_oscheck_btn()
        assert self.process_util.check_process_running("HPOSCheck.exe") is True     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C37677023") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_06_verify_fusion_networkcheck(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/37677023
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_netcheck_btn() 
        assert self.process_util.check_process_running("HPNetworkCheck.exe") is True

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31749683") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_07_verify_fusion_diagnostic(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31749683 
        """
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
            assert current_url == "https://support.hp.com/us-en/help/hp-pc-hardware-diagnostics"
        else:
            self.process_util.kill_process("HpHwDiag.exe")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C37730621") 
    @pytest.mark.exclude_platform(["grogu"])  
    def test_08_verify_gotosettings_changed_work(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/37730621
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_settings()
        self.settings.click_privacy_tab()
        self.settings.click_privacy_clicked_btn()
        self.settings.click_no_to_all()
        self.settings.click_done_button()       
        self.fc.navigate_to_support()
        self.support_home.click_get_details_link(self.wmi.get_serial_number())
        self.support_device.click_yes_personalized_btn()
        time.sleep(3)
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        assert self.support_device.get_warranty_value(timeout = 20) != "Get details"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()

    def __select_device_card(self, serial_number, b_sign=False):
        self.__launch_HPX()
        time.sleep(3)
        if b_sign:
            self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
            time.sleep(10)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)
    
    def __kill_process(self):
        self.process_util.kill_process("OCChat.exe")
        self.process_util.kill_process("HPPerformanceTuneup.exe")
        self.process_util.kill_process("HPAudioCheck.exe")
        self.process_util.kill_process("HPOSCheck.exe")
        self.process_util.kill_process("HPNetworkCheck.exe")
        self.process_util.kill_process("HpHwDiag.exe")