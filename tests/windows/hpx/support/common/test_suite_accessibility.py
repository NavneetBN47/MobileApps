from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.ma_misc import ma_misc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Accessibility(object):
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

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "accessibility.json")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822667")    
    def test_01_accessibility(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822667
        """
        for _ in range(10):
            self.driver.ssh.send_command("Start-Process myHP:AD2F1837.myHP_v10z8vjag6ke6")
            if self.fc.is_app_open():
                self.driver.ssh.send_command("Stop-Process -Force -name HP.myHP")
            time.sleep(3)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822668")   
    def test_02_accessibility(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822668
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(5)
        self.support_home.enter_keys_to_visit_link(Keys.ARROW_DOWN)
        self.support_home.enter_keys_to_device_card(Keys.ENTER, self.wmi.get_serial_number())

        assert self.support_device.get_serial_number_value() == self.wmi.get_serial_number()       

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822669")   
    def test_03_accessibility(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822669
        """
        self.__sign_in_HPX()
        time.sleep(5)
        self.support_home.enter_keys_to_device_card(Keys.TAB, self.wmi.get_serial_number())
        self.support_home.enter_keys_to_device_card(Keys.TAB, "CND7304VTB")
        self.support_home.enter_keys_to_device_card(Keys.ARROW_RIGHT, "CN44OCA018")
        self.support_home.enter_keys_to_device_card(Keys.ARROW_DOWN, "7CD524006F")
        self.support_home.enter_keys_to_device_card(Keys.ARROW_UP, "CN222191QR")
        self.support_home.enter_keys_to_device_card(Keys.ARROW_LEFT, "7CD524006F")
        self.support_home.enter_keys_to_device_card(Keys.ARROW_LEFT, "CN44OCA018")
        self.support_home.enter_keys_to_device_card(Keys.ENTER, "CND7304VTB")

        assert self.support_device.get_serial_number_value() == "CND7304VTB"      

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822671")  
    def test_04_accessibility(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822671
        """
        self.__sign_in_HPX()
        self.support_home.verify_device_display(self.wmi.get_serial_number())
        self.support_home.enter_keys_to_device_card(Keys.TAB, self.wmi.get_serial_number())
        self.support_home.enter_keys_to_device_card(Keys.TAB, "CND7304VTB")
        self.support_home.enter_keys_to_device_card(Keys.TAB, "CN44OCA018")
        self.support_home.enter_keys_to_device_card(Keys.TAB, "7CD524006F")

        self.support_home.enter_keys_to_device_card(Keys.SHIFT + Keys.TAB, "7CD524006F")
        self.support_home.enter_keys_to_device_card(Keys.SHIFT + Keys.TAB, "CN44OCA018")
        self.support_home.enter_keys_to_device_card(Keys.ENTER, "CND7304VTB")

        self.fc.select_country("US")
        self.support_device.verify_virual_repair_center_display()
        self.support_device.enter_keys_virtual_repair_center(Keys.TAB)
        self.support_device.enter_keys_service_center_locator(Keys.TAB)
        self.support_device.enter_keys_support_forum(Keys.TAB)

        # self.support_device.enter_keys_product_support_center(Keys.SHIFT + Keys.TAB)
        self.support_device.enter_keys_support_forum(Keys.SHIFT + Keys.TAB)
        self.support_device.enter_keys_service_center_locator(Keys.SHIFT + Keys.TAB)
        self.support_device.enter_keys_virtual_repair_center(Keys.SHIFT + Keys.TAB)

        assert self.support_device.get_serial_number_value() == "CND7304VTB"     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822673")  
    def test_05_accessibility(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822673
        """
        with pytest.raises(NoSuchWindowException, match="Message: Currently selected window has been closed\n"):

            self.__sign_in_HPX()
            
            self.support_home.enter_keys_to_device_card(Keys.ALT + Keys.F4, self.wmi.get_serial_number())

            self.fc.launch_app()
            self.fc.maximize_window()
            self.fc.navigate_to_support()
        
            self.support_home.select_device_card("CND7304VTB")
            self.support_device.click_edit_nick_btn()
            
            self.support_device.enter_keys_to_nick_edit(Keys.ALT + Keys.F4)          
            time.sleep(3)

            self.fc.fd["display_control"].verify_myhp_logo_is_present() 

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __sign_in_HPX(self):
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)

    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()