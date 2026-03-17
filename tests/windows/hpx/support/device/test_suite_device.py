import time
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.api_utility import APIUtility
from MobileApps.libs.flows.web.virtual_agent.va_flow_container import VAFlowContainer
from MobileApps.libs.flows.web.support_dashboard.support_flow_container import SupportFlowContainer
from MobileApps.libs.ma_misc import ma_misc
from urllib.parse import urlparse, parse_qs
import pytest
import random

pytest.app_info = "HPX"
class Test_Suite_Device(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session

        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)     
        cls.hpid = cls.fc.fd["hpid"]   
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.support_va = cls.fc.fd["support_va"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.exclude_platform(["grogu"])   
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C31909893")  
    def test_01_navigate_to_support_device_home_page(self):
        """
        verify device infomation

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31909893 
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        product_number_wmi = self.wmi.get_product_number()
        product_number_UI = self.support_device.get_product_number_value()
        assert product_number_wmi == product_number_UI
        serial_number_wmi = self.wmi.get_serial_number()
        serial_number_UI = self.support_device.get_serial_number_value()
        assert serial_number_wmi == serial_number_UI

    @pytest.mark.require_priority(["High"])   
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C32282771") 
    def test_02_navigate_to_the_device_page(self):
        """
        verify the product name for the host PC

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32282771
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        product_name_UI = self.support_device.get_product_name_value(timeout=20)
        assert self.registry.get_value("HKLM\\HARDWARE\\DESCRIPTION\\System\\BIOS", "SystemProductName", product_name_UI) == True

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C33383111") 
    def test_03_verify_nick_name(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33383111
        """
        self.__select_device_card("MXL0362720")
        self.support_device.edit_nickname("MY pc" + str(random.randint(0, 999)))
        self.support_device.click_save_nick_btn()
        self.support_device.edit_nickname("My PC")
        self.support_device.click_save_nick_btn()
        assert self.support_device.get_nick_name_value(timeout=20) == "My PC"

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C33403049") 
    def test_04_edit_nick_name(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33403049
        """
        self.__select_device_card("MXL0362720")
        self.support_device.click_edit_nick_btn()
        assert self.support_device.verify_save_nick_btn_state() == 'false'
        assert self.support_device.verify_cancel_nick_btn_state() == 'true'

        self.support_device.input_nickname("MY pc2")
        assert self.support_device.verify_save_nick_btn_state() == 'true'
        assert self.support_device.verify_cancel_nick_btn_state() == 'true'

        self.support_device.input_nickname("<")
        assert self.support_device.verify_save_nick_btn_state() == 'false'
        assert self.support_device.verify_cancel_nick_btn_state() == 'true'

        self.support_device.click_cancel_nick_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C34164386")    
    def test_05_Click_Back_button_in_Device_Support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34164386
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_back_btn()

        assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not False

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C34164427")  
    def test_06_start_virtual_agent_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34164427
        """
        if self.fc.get_winsystemlocale() in {"en-US", "es-ES", "fr-FR", "de-DE", "zh-CN", "ja-JP", "nl-NL", "pt-PT"}:
            
            system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
            myHPVA = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_root/{}.json".format(system_locale))['common']['myHPVA'] 
            hpVirtualAssistant = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_root/{}.json".format(system_locale))['common']['hpVirtualAssistant'] 

            self.fc.restart_app()
            self.fc.maximize_window()
            self.fc.navigate_to_support()
            time.sleep(3)
            self.support_home.select_device_card(self.wmi.get_serial_number())
            self.support_device.click_va()
            time.sleep(5)
            self.support_va.click_start_VA()
            self.support_va.verify_va_detail_page_opened()
            assert self.support_va.get_va_page_title() == myHPVA
            assert self.support_va.get_va_page_subtitle() == hpVirtualAssistant

            if system_locale in ["en_US"]:
                url = self.support_va.get_va_link()
                url_parse = urlparse(url)
                lc = parse_qs(url_parse.query)['lc'][0]
                cc = parse_qs(url_parse.query)['cc'][0]
                assert lc == "en"
                assert cc == "US"
                assert self.support_va.get_webchat_info() == "Bot said: Hi! I'm HP's Virtual Assistant."
                # assert self.support_va.get_webchat_info() == "Bot said: I am looking for additional information related to your device."
                # self.web_fc = VAFlowContainer(self.web_driver)
                # self.web_fc.navigate(url)
                # assert self.web_fc.fd['home'].get_start_va_tips() == "Hi! I'm HP's Virtual Assistant."

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])  
    @pytest.mark.testrail("S57581.C32466557")  
    def test_07_navigate_to_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32466557
        """
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        product_number_wmi = self.wmi.get_product_number()
        product_number_UI = self.support_device.get_product_number_value()
        assert product_number_wmi == product_number_UI
        serial_number_wmi = self.wmi.get_serial_number()
        serial_number_UI = self.support_device.get_serial_number_value()
        assert serial_number_wmi == serial_number_UI
        assert self.support_device.verify_product_image_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C33374370")  
    def test_08_edit_button_is_enabled(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33374370
        """
        self.__select_device_card("5CG02735RG")
        assert self.support_device.verify_edit_nick_btn_show() is not False
        self.support_device.click_edit_nick_btn()
        self.support_device.get_value_nick_edit_txt() == "My Device"
        self.support_device.enter_keys_to_nick_edit("MY pc" + str(random.randint(0, 999)), clear_text=True)
        self.support_device.click_save_nick_btn()
        self.support_device.edit_nickname("My Device")
        self.support_device.click_save_nick_btn()
        assert self.support_device.get_nick_name_value(timeout=20) == "My Device"

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C33383101")  
    def test_09_verify_the_edit_nickname_rule(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33383101
        """
        self.__select_device_card("CND7304VTB")

        self.support_device.edit_nickname(" < > % { } | \ ^ [ ]")

        assert self.support_device.verify_save_nick_btn_state() == 'false'

        self.support_device.enter_keys_to_nick_edit("abcdefghijklmnopqrstuvwxyz1234", clear_text=True)
        
        assert self.support_device.verify_save_nick_btn_state() == 'true'

        self.support_device.enter_keys_to_nick_edit("abcdefghijklmnopqrstuvwxyz12345", clear_text=True)

        assert self.support_device.get_value_nick_edit_txt() == "abcdefghijklmnopqrstuvwxyz1234"

    # @pytest.mark.require_priority(["High", "BVT"])  
    # @pytest.mark.require_stack(["pie", "production", "stage"])
    # @pytest.mark.testrail("S57581.C32283210")    
    # def test_10_navigate_to_the_device_page(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/32283210
    #     """
    #     self.__launch_HPX(),
    #     self.support_home.select_device_card(self.wmi.get_serial_number())     

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C32284095")   
    def test_11_on_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32284095
        """   
        self.__launch_HPX(),
        self.support_home.select_device_card(self.wmi.get_serial_number())    
        product_number_UI = self.support_device.get_product_number_value(timeout=20)
        assert self.registry.get_value("HKLM\\HARDWARE\\DESCRIPTION\\System\\BIOS", "SystemSKU", product_number_UI) == True

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production_NA", "stage_NA"])
    @pytest.mark.testrail("S57581.C33339394")  
    def test_12_add_a_remote_device(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33339394
        """  
        self.__sign_in_HPX("hpxtest003@gmail.com", "hpsa@rocks_335")      
        self.api_utility = APIUtility(self.stack)
        self.api_utility.get_access_token("hpxtest003@gmail.com", "hpsa@rocks_335")
        deviceId = self.api_utility.post_device_register("8CC7300CZV", "X0V56EA")   
        self.support_home.click_refresh_btn()
        self.support_home.verify_device_display("8CC7300CZV") is not False
        self.api_utility.post_device_unregister(deviceId)      

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.exclude_platform(["grogu"]) 
    @pytest.mark.testrail("S57581.C35546528")     
    def test_13_sign_in_from_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35546528
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver) 
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.exclude_platform(["grogu"]) 
    @pytest.mark.testrail("S57581.C35546545")  
    def test_14_sign_in_from_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35546545
        """
        self.__sign_in_HPX()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.exclude_platform(["grogu"]) 
    @pytest.mark.testrail("S57581.C35547205")      
    def test_15_sign_in_from_support_detail_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35547205
        """
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver) 
        self.support_device.click_back_btn()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C35547307")  
    def test_16_already_sign_in(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35547307
        """
        self.__sign_in_HPX()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.exclude_platform(["grogu"]) 
    @pytest.mark.testrail("S57581.C35547396")  
    def test_17_leave_and_back_to_the_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35547396
        """
        self.__sign_in_HPX()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env == "itg":
            assert count == 16
        else:
            assert count == 18

        self.navigation_panel.navigate_to_settings()
        self.fc.navigate_to_support()
        self.support_home.verify_device_display("5CD73931QW")
        count = self.support_home.get_device_count()
        if self.app_env != "itg":
            assert count == 18
        else:
            assert count == 18

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C32283210")  
    def test_18_navigate_to_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32283210
        """
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        assert self.support_device.verify_product_image_display() is not False

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "productio_NA", "stage_NA"])
    @pytest.mark.testrail("S57581.C33339398")  
    def test_19_add_a_remote_printer(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33339398
        """
        self.__sign_in_HPX("hpxtest003@gmail.com", "hpsa@rocks_335")      
        self.api_utility = APIUtility(self.stack)
        self.api_utility.get_access_token("hpxtest003@gmail.com", "hpsa@rocks_335")
        deviceId = self.api_utility.post_device_register("CN72N4N00G", "f5s46b")   
        self.support_home.click_refresh_btn()
        self.support_home.verify_device_display("CN72N4N00G") is not False
        self.api_utility.post_device_unregister(deviceId)  

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production_NA", "stage_NA"])
    @pytest.mark.testrail("S57581.C33339399")  
    def test_20_add_remote_chromebook(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33339399
        """
        self.__sign_in_HPX("hpxtest003@gmail.com", "hpsa@rocks_335")      
        self.api_utility = APIUtility(self.stack)
        self.api_utility.get_access_token("hpxtest003@gmail.com", "hpsa@rocks_335")
        deviceId = self.api_utility.post_device_register("5CD0450BG7", "2H7Q9UA")   
        self.support_home.click_refresh_btn()
        self.support_home.verify_device_display("5CD0450BG7") is not False
        self.api_utility.post_device_unregister(deviceId)  

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production_NA", "stage_NA"])
    @pytest.mark.testrail("S57581.C33339400")  
    def test_21_add_remote_tablet(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33339400
        """
        self.__sign_in_HPX("hpxtest003@gmail.com", "hpsa@rocks_335")      
        self.api_utility = APIUtility(self.stack)
        self.api_utility.get_access_token("hpxtest003@gmail.com", "hpsa@rocks_335")

        deviceId = self.api_utility.post_device_register("6CY3210FSF", "E0P96AA")   
        deviceId_2 = self.api_utility.post_device_register("CN44OCA018", "L2698A")
        deviceId_3 = self.api_utility.post_device_register("7CD524006F", "G8X92AA")
        deviceId_4 = self.api_utility.post_device_register("9CU6350BTS", "X9U42UT")
        deviceId_5 = self.api_utility.post_device_register("3CQ511314R", "3CQ511314R")
        self.support_home.click_refresh_btn()
        self.support_home.verify_device_display("6CY3210FSF") is not False
        self.support_home.verify_device_display("CN44OCA018") is not False
        self.support_home.verify_device_display("7CD524006F") is not False
        self.support_home.verify_device_display("9CU6350BTS") is not False
        self.support_home.verify_device_display("3CQ511314R") is not False
        self.api_utility.post_device_unregister(deviceId)  
        self.api_utility.post_device_unregister(deviceId_2)  
        self.api_utility.post_device_unregister(deviceId_3)  
        self.api_utility.post_device_unregister(deviceId_4)  
        self.api_utility.post_device_unregister(deviceId_5) 

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production_NA", "stage_NA"])
    @pytest.mark.testrail("S57581.C33349409")  
    def test_22_remove_remote_device(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33349409
        """
        self.__sign_in_HPX("hpxtest003@gmail.com", "hpsa@rocks_335")      
        self.api_utility = APIUtility(self.stack)
        self.api_utility.get_access_token("hpxtest003@gmail.com", "hpsa@rocks_335")
        deviceId = self.api_utility.post_device_register("CN72N4N00G", "f5s46b")   
        self.support_home.click_refresh_btn()
        assert self.support_home.verify_device_display("CN72N4N00G") is not False
        self.api_utility.post_device_unregister(deviceId)  
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        assert self.support_home.verify_device_display("CN72N4N00G") is False

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38322251")  
    def test_23_lanuch_VA_and_close(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38322251
        """
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.verify_support_device_page()
        self.support_device.click_va()
        time.sleep(5)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        self.support_va.click_close_button()
        self.support_va.click_close_cancel_button()
        time.sleep(10)
        assert self.support_device.verify_support_device_page() is True 

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_device_card(self, serial_number):
        self.__sign_in_HPX()
        self.support_home.select_device_card(serial_number)
        time.sleep(5)
    
    def __sign_in_HPX(self, username="shhpxtest005@outlook.com", password="hpsa@rocks_335"):
        self.__launch_HPX()
        time.sleep(3)
        self.fc.sign_in(username, password, self.web_driver) 
        time.sleep(5)

    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
    
    def __web_login(self, stack):
        self.web_fc = SupportFlowContainer(self.web_driver)  
        self.web_fc.clear_chrome_browsing_data()
        self.web_fc.navigate(stack)
        self.web_fc.click_sign_in_btn()
        self.web_fc.login("hpxtest003@gmail.com", "hpsa@rocks_335")

    def __web_add_device(self, sn):
        self.web_fc.add_device(sn)

    def __web_logout(self):
        self.web_fc.sign_out()
