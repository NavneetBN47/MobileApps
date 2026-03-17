from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.ma_misc import ma_misc
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Security(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env() 
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31727570")  
    def test_01_security(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31727570
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
        nick_name_invalid = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['DeviceNickname_Invalid'] 
        
        self.__sign_in_HPX()

        self.support_home.select_device_card("CND7304VTB")
        self.support_device.verify_support_device_page()
        self.support_device.edit_nickname("~!@#$%^&*()_+}{\":?></.,';][=-")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_tip_value() == nick_name_invalid

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31727571")  
    def test_02_security(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31727571
        """
        self.__sign_in_HPX()

        self.support_home.select_device_card("CND7304VTB")

        self.support_device.edit_nickname("Javascript: alert(document.cookie)")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_value() in "Javascript: alert(document.cookie)"     

        self.support_device.edit_nickname("select * from xx")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_value() in "select * from xx"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31727573")  
    def test_03_security(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31727573
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
        nick_name_invalid = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['DeviceNickname_Invalid'] 

        self.__sign_in_HPX()

        self.support_home.select_device_card("CND7304VTB")

        self.support_device.edit_nickname("<font color=red>HPHP<font>")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_tip_value() == nick_name_invalid        

        self.support_device.input_nickname("<img src=x onerror=prompt(1)>")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_tip_value() == nick_name_invalid

        self.support_device.input_nickname("input{{9*9}}")
        self.support_device.click_save_nick_btn()

        assert self.support_device.get_nick_name_tip_value() == nick_name_invalid

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __sign_in_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)