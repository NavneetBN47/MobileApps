from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from bs4 import BeautifulSoup

pytest.app_info = "HPX"
class Test_Suite_Common(object):
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

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "support_resource.json")
        
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.fc.disable_dark_mode()
        request.addfinalizer(tab_clean_up)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env() 
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31860913")  
    def test_01_redirect_links(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31860913
        """
        system_locale = self.fc.get_winsystemlocale().strip()
        self.fc.initial_simulate_file(self.file_path, "C31857771", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31857771"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])        
        
        self.fc.select_country("US")
        if system_locale in ["en-US"]:
            self.support_device.click_user_manuals_guide(timeout=20)
            time.sleep(3)
            webpage = "UserManualAndGuide"
            self.web_driver.wait_for_new_window(timeout=20)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()

            assert current_url == "https://support.hp.com/us-en/product/setup-user-guides/hp-elitebook-830-g7-notebook-pc/31971702"
        else:
            self.support_device.verify_user_manuals_guide() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31727292")  
    def test_02_launch_hpx(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31727292
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        
        self.fc.navigate_to_support()

        self.support_home.select_device_card(self.wmi.get_serial_number())

        assert self.support_device.get_serial_number_value() == self.wmi.get_serial_number()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31727558")     
    def test_03_hpx_error(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31727558
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.fc.close_app()

        assert self.task_util.verify_eventlog('Error', 'myHP') is True

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34991465")
    @pytest.mark.exclude_platform(["grogu"])   
    def test_04_click_get_details_link_under_warranty(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34991465
        """
        self.fc.enable_dark_mode()
        system_locale = self.fc.get_winsystemlocale().strip()
        language = "sr_Latn-RS" if system_locale == "sr-BA" else system_locale
        with open(ma_misc.get_abs_path("resources/test_data/hpsa/locale/view_data_collected/{}/HPSFCollectedData.html").format(language), "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml")
            title_tag = soup.find("title")
            header = title_tag.text.strip()
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") 
        
        self.__select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_view_data_collected_link()
        assert self.support_device.get_warranty_details_content_title() == header

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34975226")   
    def test_05_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34975226
        """
        self.fc.enable_dark_mode()
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
        nick_name_invalid = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['DeviceNickname_Invalid']   

        self.__sign_in_HPX()
        
        self.support_home.select_device_card("CND7304VTB")
        self.support_device.verify_support_device_page()
        self.support_device.edit_nickname("<font color=red>HPHP<font>")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_tip_value() == nick_name_invalid  

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34991579") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_06_click_yes_on_the_warranty(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34991579
        """
        self.fc.enable_dark_mode() 
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") 
        
        self.__select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_yes_button()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33442479") 
    def test_07_change_os_dark_mode(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33442479
        """
        self.fc.enable_dark_mode() 
        self.__select_device_card(self.wmi.get_serial_number())

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################    
    def __select_device_card(self, sn):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.select_device_card(sn)

    def __sign_in_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)

    # @pytest.mark.require_priority(["Medium"])  
    # @pytest.mark.require_stack(["stage", "pie", "production"]) 
    # @pytest.mark.testrail("S57581.C31727558")   
    # def test_04_poc(self):
    #     self.task_util.get_display_resolution()
    #     self.task_util.set_display_resolution(1280, 1024)
    #     #768， 1024
    #     #1680， 1050

    # @pytest.mark.require_priority(["Medium"])  
    # @pytest.mark.require_stack(["stage", "pie", "production"]) 
    # @pytest.mark.testrail("S57581.C31727558")   
    # def test_05_poc(self):
    #     self.fc.enable_dark_mode()
    #     self.fc.disable_dark_mode()