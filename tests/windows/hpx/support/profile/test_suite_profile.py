from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.api_utility import APIUtility
from SAF.misc import saf_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Profile(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session

        cls.fc = FlowContainer(cls.driver)       
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.devices = cls.fc.fd["devices"]
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352656")  
    def test_01_sign_in_on_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352656
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352657")  
    def test_02_sign_in_PC_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352657
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        time.sleep(10)
        self.fc.navigate_to_PC_device()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352661")  
    def test_03_sign_in_on_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352661
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352662") 
    def test_04_sign_in_on_support_details_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352662
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(5)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.click_back_btn()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352664") 
    def test_05_sign_in_on_settings_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352664
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_settings()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352676") 
    def test_06_sign_out_remote_device_detail_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352676    
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.select_device_card("5CD73931QW")
        self.fc.sign_out(self.web_driver)
        assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not None

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352699") 
    def test_07_sign_out_on_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352699
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        time.sleep(3)
        self.fc.sign_out(self.web_driver)
        assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not None

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352701") 
    def test_08_sign_out_and_sign_in_another_account(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352701
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18
        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("hpxtest001@gmail.com", "hpsa@rocks_335", self.web_driver)
        self.support_home.verify_device_display("CND2390V1J")
        count = self.support_home.get_device_count()
        assert count == 15

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])     
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33352709") 
    def test_09_sign_out_and_sign_in_another_account(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33352709
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(5)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        time.sleep(3)
        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("hpxtest001@gmail.com", "hpsa@rocks_335",  self.web_driver)
        self.support_home.click_back_btn()
        self.support_home.verify_device_display("CND2390V1J")
        count = self.support_home.get_device_count()
        assert count == 15

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33353849") 
    def test_10_reopen_myHP(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33353849
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()     
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        time.sleep(3)
        self.fc.restart_app()
        self.fc.maximize_window()  
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18
        
