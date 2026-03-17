import time
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_Default_Behavior(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session

        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)     
        cls.hpid = cls.fc.fd["hpid"]   
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.hp_registration = cls.fc.fd["hp_registration"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.support_va = cls.fc.fd["support_va"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "supportdefaultbehavior.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38322611")      
    def test_01_not_choose_country(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38322611
        """
        self.fc.initial_simulate_file(self.file_path, "C38322611", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C38322611"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.verify_support_device_page()
        assert self.support_device.verify_liveassistant_card_display() is not False

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.__click_skip_btn()
        self.fc.navigate_to_support()
    
    def __click_skip_btn(self):
        if self.hp_registration.verify_skip_button_show():
            self.hp_registration.click_skip_button()