import os
import time
import json
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from SAF.misc import saf_misc
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_CustomProtocol(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup 
        cls.wmi = WmiUtilities(cls.driver.ssh)   
        cls.web_driver = utility_web_session 
        cls.request = request
        
        cls.fc = FlowContainer(cls.driver) 
        cls.sf = SystemFlow(cls.driver) 

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)   
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "custom_protocol.json")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32228250")     
    def test_01_when_hpx_has_been_installed(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32228250
        """
        if self.fc.is_app_open():
            self.sf.close_myhp_app()
        self.fc.launch_myHP()
        time.sleep(30)
        self.sf.close_myhp_app()
        self.fc.launch_hotkey("myhp://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        time.sleep(10)
        self.sf.close_myhp_app()
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True

    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32228251")
    def test_02_when_hpx_has_been_installed(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32228251
        """
        if self.fc.is_app_open():
            self.sf.close_myhp_app()
        self.fc.launch_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.launch_hotkey("myhp://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True

        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.launch_hotkey("myhp://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32466159")
    def test_03_when_hpx_has_been_installed(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32466159
        """
        if self.fc.is_app_open():
            self.sf.close_myhp_app()
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.click_dialog_close_btn(self.web_driver)
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.click_dialog_close_btn(self.web_driver)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
        assert self.fc.fd["support_device"].verify_support_device_page() is True

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32466160")    
    def test_04_when_hpx_has_been_installed(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32466160
        """
        if self.fc.is_app_open():
            self.sf.close_myhp_app()
        self.fc.launch_myHP()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(3)
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.launch_hotkey("hpx://support/device")
        assert self.fc.fd["support_device"].verify_support_device_page() is True

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C33646042")  
    def test_05_press_hotkey(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33646042
        """
        if self.fc.is_app_open():
            self.fc.close_myHP()
        self.fc.launch_myHP()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.close_myHP()
        self.fc.launch_hotkey("hpx://support/device")

        assert self.fc.fd["support_device"].verify_support_device_page() is not False
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False      
