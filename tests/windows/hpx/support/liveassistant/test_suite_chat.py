import time
import MobileApps.resources.const.windows.const as w_const
import datetime
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from selenium.webdriver.common.keys import Keys
import pytest

pytest.app_info = "HPX"
class Test_Suite_Chat(object):
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
    def function_setup(self):
        self.fc.initial_hpx_support_env()       

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31866696")  
    @pytest.mark.exclude_platform(["grogu"])     
    def test_01_Check_in_or_check_out_Privacy_Agreement(self):
        """
        verify the UI of check box is expected

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31866696
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        self.fc.initial_simulate_file(self.file_path, "C31866696", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31866696"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.is_privacy_status_selected() == "0"
                self.support_device.click_privacy_checkbox()
                assert self.support_device.is_privacy_status_selected() == "1"
                self.support_device.click_privacy_checkbox()
                assert self.support_device.is_privacy_status_selected() == "0"
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()          

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32562259")  
    @pytest.mark.exclude_platform(["grogu"])     
    def test_02_Click_Chat_with_an_agent_option(self):
        """
        According to feature owner, this case not supported anymore, so NA
        verify a message will popup if user haven't opted-in
        TestRails ->https://hp-testrail.external.hp.com/index.php?/cases/view/32562259
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C32562259", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32562259"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        # if self.stack in ['pie']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalised support"
        # elif self.stack in ['stage', 'production']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalized support"
        # self.support_device.click_no_button()
        # self.support_device.click_chat_with_agent()
        # self.support_device.click_yes_button()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else:
            self.support_device.click_close_btn()   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32564735")  
    def test_03_Live_assistant(self):
        """
        Verify the live assistant options when opt-in disabled.

        TestRails-> https://hp-testrail.external.hp.com/index.php?/cases/view/32564735
        """
        self.fc.initial_simulate_file(self.file_path, "C32564735", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564735"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        assert self.support_device.get_warranty_details_popup_title() == "Allow personalized support"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510005")
    @pytest.mark.exclude_platform(["grogu"])           
    def test_04_click_chat_with_agent_option(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510005
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510006")  
    def test_05_sign_in_from_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510006
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.navigation_panel.verify_welcome_module_show()
        self.navigation_panel.navigate_to_welcome()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.home.click_support_control_card()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], displayed=True)
        time.sleep(3)
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510007")  
    @pytest.mark.exclude_platform(["grogu"])  
    def test_06_sign_in_from_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510007
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510008")  
    def test_07_sign_in_from_PC_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510008
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_PC_device()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(10)
        self.devices.click_support_btn()
        time.sleep(10)
        # self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.exclude_platform(["grogu"])        
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510024")     
    def test_08_without_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510024
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:           
        # if self.stack in ['pie']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalised support"
        # elif self.stack in ['stage', 'production']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalized support"
        # self.support_device.click_no_button()
        # self.support_device.click_chat_with_agent()
        # if self.stack in ['pie']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalised support"
        # elif self.stack in ['stage', 'production']:
        #     assert self.support_device.get_warranty_details_popup_title() == "Allow personalized support"
        # self.support_device.click_yes_button()
            assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False        
            # if self.stack in ['production']:
            #     self.hpid.click_popup_close_btn()
            assert self.registry.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is True
        else:
            #https://support.hp.com/us-en/contact?openCLC=true
            webpage = "Chat"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510025")   
    @pytest.mark.exclude_platform(["grogu"])
    def test_09_without_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510025
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.verify_warranty_details_popup_display() is False
                assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true" 
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510023") 
    @pytest.mark.exclude_platform(["grogu"])      
    def test_10_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510023
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        # self.support_device.click_no_button()
        # self.support_device.click_chat_with_agent()
        # self.support_device.click_yes_button()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510026")  
    @pytest.mark.exclude_platform(["grogu"])  
    def test_11_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510026
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33510035") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_12_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510035
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
            assert self.support_device.verify_add_device_popup_display() is False
        else:
            #https://support.hp.com/us-en/contact?openCLC=true
            webpage = "Chat"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie_NA"]) 
    @pytest.mark.testrail("S57581.C33526200") 
    def test_13_hp_one_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33526200
        """
        self.fc.initial_simulate_file(self.file_path, "C33526200", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33526200"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_banner_lbl_title() == "Available 24/7 expert assistance from your HP One subscription"    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564733") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_14_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564733
        """  
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.support_device.click_no_button()
        self.support_device.click_chat_with_agent()
        self.support_device.click_yes_button()
        assert self.support_device.verify_warranty_details_popup_display() == False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564734")
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_15_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564734
        """ 
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True")
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.support_device.click_done_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564735")
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_16_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564735
        """
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        for _ in range(5):
            self.support_device.click_chat_with_agent()
            self.support_device.click_no_button()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564736") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_17_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564736
        """ 
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True")
        self.fc.initial_simulate_file(self.file_path, "C33510005", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510005"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        for _ in range(5):
            self.support_device.click_chat_with_agent()
            self.support_device.click_done_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564737") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_18_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564737
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()
        self.support_device.click_no_button()
        self.navigation_panel.navigate_to_settings()
        self.settings.click_privacy_tab()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_yes_button()
        self.settings.click_done_button()   
        time.sleep(5)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32564740") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_19_live_assistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32564740
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else:
                #https://support.hp.com/us-en/contact?openCLC=true
                webpage = "Chat"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert current_url == "https://support.hp.com/us-en/contact?openCLC=true"
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32831923") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_20_click_back_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32831923 
        """
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        time.sleep(3)
        self.support_device.click_chat_with_agent() 
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        self.support_device.get_support_model_sub_title()
        self.support_device.click_close_btn()  
        assert self.navigation_panel.get_user_initials_icon_text() == "AA"
        self.support_device.click_back_btn()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)

    def __select_device_card(self, serial_number, lang_country="US", current_locale=None):
        self.__launch_HPX()
        time.sleep(3)
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        time.sleep(10)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)
        self.fc.select_country(lang_country, current_locale=current_locale)
