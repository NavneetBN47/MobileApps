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
class Test_Suite_Chat_Part2(object):
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
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32831924") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_21_click_back_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32831924
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False) 
        self.support_device.get_support_model_sub_title()
        self.support_device.click_close_btn()
        self.support_device.click_back_btn() 
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        self.support_device.click_back_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33554282") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_22_sign_in_from_device_detail_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33554282
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent() 
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33554243") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_23_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33554243
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        time.sleep(3)
        self.support_device.click_chat_with_agent() 
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33726767") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_24_close_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33726767
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        time.sleep(3)
        self.support_device.click_chat_with_agent() 
        self.fc.click_dialog_close_btn(self.web_driver)
        self.support_device.click_chat_with_agent()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33726768") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_25_close_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33726768
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.navigation_panel.select_my_hp_account_btn()
        self.fc.click_dialog_close_btn(self.web_driver)
        self.support_device.click_chat_with_agent()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33510036") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_26_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510036
        """
        self.fc.initial_simulate_file(self.file_path, "C33510036", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33510036"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.verify_add_device_popup_display() is not False
            self.support_device.click_no_button()
        else: 
            self.support_device.click_close_btn()  
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.verify_add_device_popup_display() is not False
        else: 
            self.support_device.click_close_btn()
            
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33510039") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_27_support_consent_is_yes(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510039
        """
        self.fc.initial_simulate_file(self.file_path, "C33510036", self.app_env, self.stack)
        self.__launch_HPX()
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33510036"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.verify_add_device_popup_display() is not False
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33510041") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_28_support_consent_is_yes(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510041
        """
        self.fc.initial_simulate_file(self.file_path, "C33510036", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33510036"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.verify_add_device_popup_display() is not False
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33492990") 
    def test_29_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33492990
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/case_create/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            
            self.support_device.click_category_cbx()

            assert self.support_device.get_catetory(0) == common["typeDropdown"]["type1"]
            assert self.support_device.get_catetory(1) == common["typeDropdown"]["type2"]
            assert self.support_device.get_catetory(2) == common["typeDropdown"]["type3"]
            assert self.support_device.get_catetory(3) == common["typeDropdown"]["type4"]
            assert self.support_device.get_catetory(4) == common["typeDropdown"]["type5"]
            assert self.support_device.get_catetory(5) == common["typeDropdown"]["type6"]
            assert self.support_device.get_catetory(6) == common["typeDropdown"]["type7"]
            assert self.support_device.get_catetory(7) == common["typeDropdown"]["type8"]  

            self.support_device.click_category_opt(3)
            self.support_device.click_category_cbx()
            assert self.support_device.verify_category_selected(3) == "true"

            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.click_chat_cancel_button()
        else:
            self.support_device.click_close_btn()
 
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33492991") 
    def test_30_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33492991
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/case_create/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            
            assert self.support_device.get_problem_helptext() == common["problemInput"]["text"]
            
            self.support_device.edit_problem("auto test")

            self.support_device.enter_keys_to_problem_text(Keys.ENTER)

            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE) 
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)
            self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE) 

            assert self.support_device.verify_promptinfo_chat_form() == common["checkTheProblemAndTryAgain"]            
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33492991") 
    def test_31_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33492993
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.verify_chat_now_btn_state() == "false"
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_chat_now_btn_state() == "true"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33492999") 
    def test_32_click_chat_now(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33492999 
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(0)
            self.support_device.edit_problem("HPX test")
            self.support_device.click_privacy_checkbox()
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33493000") 
    def test_33_click_privacy_terms_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33493000
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_pravicy_link()
            webpage = "PRIVACY_LINK"
            self.web_driver.wait_for_new_window(timeout=20)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)
            self.web_driver.wait_url_contains("https://www.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://www.hp.com/us-en/privacy/privacy.html"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33493001") 
    def test_34_click_cancel_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33493001
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_chat_cancel_button()
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31866687") 
    def test_35_minimum_close_and_cancel(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31866687
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/case_create/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        
        for _ in range(2):
        
            self.support_device.click_chat_with_agent()

            if not self.support_device.verify_outside_hours_popup_display():            

                self.support_device.click_minimize_btn()
                self.support_device.click_maximize_btn()
                self.support_device.click_category_cbx()
                self.support_device.click_category_opt(1)
                self.support_device.edit_problem("Test no connect")
                self.support_device.click_privacy_checkbox()

                assert self.support_device.verify_chat_now_btn_state() == "true"
                
                self.support_device.click_minimize_btn()
                self.support_device.click_maximize_btn()

                assert self.support_device.verify_category_type() == common["typeDropdown"]["type2"]          
                assert self.support_device.get_problem_text() == "Test no connect"            
                assert self.support_device.verify_chat_now_btn_state() == "true"
                
                self.support_device.click_close_btn()
            else:
                self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33517417")     
    def test_36_when_language_and_country_is_mix(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33517417
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            if system_locale in ["en_US", "en_CA", "en_GB", "fr_CA", "ja_JP", "es_MX"]:
                self.support_device.click_close_btn()
            else:
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
    @pytest.mark.testrail("S57581.C33518761")    
    def test_37_change_country_on_support(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33518761
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], "DE")
        assert self.support_device.verify_chat_with_agent_display() is False
        self.support_device.click_back_btn()
        self.support_home.select_device_card("MXL0362720")
        self.fc.select_country("DE")
        assert self.support_device.verify_chat_with_agent_display() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33493008")    
    def test_38_using_keyboard(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33493008
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.enter_keys_to_speak_to_agent(Keys.TAB)
        self.support_device.enter_keys_to_chat_with_agent(Keys.ENTER)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33535072")    
    def test_39_change_country_on_support(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33535072
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])        
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_chat_now_btn_state() == "true"
        else:
            self.support_device.click_close_btn()   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C33526069")   
    def test_40_click_chat_on_remote_device(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33526069
        """
        self.fc.initial_simulate_file(self.file_path, "C32564737", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C32564737"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])        
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_chat_now_btn_state() == "true"
            self.support_device.click_chatnow_btn()
            if self.process_util.check_process_running("OCChat.exe"):
                assert self.process_util.check_process_running("OCChat.exe") is True
                self.process_util.kill_process("OCChat.exe")            
        else:
            self.support_device.click_close_btn()   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33510020")  
    def test_41_verify_outofworkinghours(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510020
        """
        self.fc.update_hpx_support_locale("ja-JP")
        self.__select_device_card("5CG02735RG", lang_country="JP", current_locale="ja-JP")      
        self.support_device.click_chat_with_agent()

        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '08:00', '%Y-%m-%d%H:%M')
        d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '17:00', '%Y-%m-%d%H:%M')
        if d_time < datetime.datetime.now() < d_time1:
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_chat_now_btn_state() == "true"
            self.support_device.click_chatnow_btn()
            if self.process_util.check_process_running("OCChat.exe"):
                assert self.process_util.check_process_running("OCChat.exe") is True
                self.process_util.kill_process("OCChat.exe") 
        else:
            assert self.support_device.verify_outside_hours_popup_display() is not False    

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
