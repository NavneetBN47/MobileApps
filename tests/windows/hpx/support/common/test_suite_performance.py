from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Performance(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.__close_all_windows()
        request.addfinalizer(tab_clean_up)    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822643")    
    def test_01_performance(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822643
        """
        self.task_util.register_task("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "qama_hpx_msedge")
        self.task_util.start_task("qama_hpx_msedge")
        
        self.__add_browser_window("window_1", "https://www.baidu.com/")
        self.__add_browser_window("window_2", "https://www.google.com/")
        self.__add_browser_window("window_3", "https://www.baidu.com/")        
        self.__add_browser_window("window_4", "https://www.google.com/")
        self.__add_browser_window("window_5", "https://www.baidu.com/")
        self.__add_browser_window("window_6", "https://www.google.com/")
        self.__add_browser_window("window_7", "https://www.baidu.com/")
        self.__add_browser_window("window_8", "https://www.google.com/")
        
        self.__verify_HPX()
        self.task_util.stop_task("qama_hpx_msedge")
        self.process_util.kill_process("msedge.exe")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822644")  
    def test_02_performance(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822644
        """
        self.__add_browser_window("window_1", "https://www.youtube.com/watch?v=Yno7iRi60b0")
        self.__add_browser_window("window_2", "https://www.youtube.com/watch?v=_Bk7hztQBMk")
        
        time.sleep(10)

        self.__verify_HPX()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822646")  
    def test_03_performance(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822646
        """  
        self.fc.launch_hotkey("C:/Users/exec/HPXTestVideo/Generation_Impact_HP.mp4")
        self.task_util.register_task("mspaint.exe", "qama_hpx_mspaint")
        self.task_util.start_task("qama_hpx_mspaint")
        time.sleep(10)
        self.__verify_HPX()

        self.process_util.kill_process("Microsoft.Media.Player.exe")
        self.task_util.stop_task("qama_hpx_mspaint")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __add_browser_window(self, window_name, url):
        window_name = window_name
        self.web_driver.execute_script("window.open()")
        self.web_driver.add_window(window_name)
        self.web_driver.switch_window(window_name)
        self.web_driver.navigate(url)

    def __close_all_windows(self):
        window_list = []
        window_tables = self.web_driver.session_data["window_table"].keys()
        for window in window_tables:
            window_list.append(window)
        for window_name in reversed(window_list):
            self.web_driver.switch_window(window_name)
            if window_name != "main":
                self.web_driver.close_window(window_name)

    def __verify_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        system_locale = self.fc.get_winsystemlocale().strip()

        if system_locale == "zh-CN":
            system_locale = "zh-Hans"
        elif system_locale == "zh-TW":
            system_locale = "zh-Hant"
        elif system_locale == "zh-HK":
            system_locale = "zh-Hant-HK"
        elif system_locale == "sr-BA":
            system_locale = "sr-Latn-RS"

        if system_locale in ["ca-ES", "es-ES", "eu-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['hPOnePremiumDeviceSupport']
        else:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['hPOnePremiumDeviceSupport']   
        
        self.fc.navigate_to_support()
        if not self.wmi.is_grogu():
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        else:
            assert self.support_home.get_support_home_title() == hp_one_device_support