from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest

pytest.app_info = "HPX"
class Test_Suite_Rebranding(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.support_rebranding = cls.fc.fd["support_rebranding"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "support_resource.json")
        
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.fc.disable_dark_mode()
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])    
    def test_01_poc(self):
        """
        rebrand poc test
        """
        self.fc.restart_app()
        self.support_rebranding.click_rebranding_btn1()
        self.support_rebranding.click_rebranding_btn1()
        self.support_rebranding.get_rebranding_btn2_text()
        self.support_rebranding.click_rebranding_btn3()
        self.support_rebranding.click_rebranding_btn4()
        self.support_rebranding.input_sn("123456")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])    
    def test_02_poc(self):
        """
        rebrand poc test
        """
        self.fc.restart_app()
        self.support_rebranding.click_rebranding_btn5()
        self.support_rebranding.click_rebranding_btn6()
        self.support_rebranding.click_country_dropdown()
        self.support_rebranding.click_country_option("China")
        self.support_rebranding.click_show_more_btn()    
        self.support_rebranding.click_show_more_btn()

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])    
    def test_03_poc(self):
        """
        rebrand poc test
        """
        self.fc.restart_app()
        self.support_rebranding.click_rebranding_btn5()
        self.support_rebranding.click_start_va_btn()