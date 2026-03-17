import time
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_Poly(object):
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

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35026283")        
    def test_21_click_hp_community(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35026283
        """
        system_locale = self.fc.get_winsystemlocale().strip()

        self.__verify_redirector("2KW5RR", system_locale)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35026855")     
    def test_22_verify_opened_community_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35026855
        """
        self.fc.update_hpx_support_locale("zh-CN")
        self.__select_device_card("2KW5RR")
        self.__select_country("CN","zh-CN")
        webpage = "HPCommunity"
        self.support_device.click_HP_support_forum()
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert "h30434.www3.hp.com" in current_url


    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35026858")     
    def test_23_verify_chat_offertime(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35026858
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        self.__verify_chat_agent_page_title()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876165")  
    def test_24_verify_chat_with_agent_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876165
        """
        # 2KW5RR->IW ->ZZ(SETTING->SUPPORT-nO)
        # NJ:212007199
        # XW:SN:EE08VY
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        assert self.support_device.verify_chat_with_agent_display() is not False

        if self.app_env != "itg":
            self.__select_device_card("EE08VY", False)
            self.__select_country("US")
            assert self.support_device.verify_chat_with_agent_display() is not False

        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.__select_device_card("2KW5RR", False)
        self.__select_country("US")
        assert self.support_device.verify_chat_with_agent_display() is not False    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876166")  
    def test_25_verify_speak_to_agent_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876166
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        assert self.support_device.verify_speak_to_agent() is not False

        if self.app_env != "itg":
            self.__select_device_card("EE08VY", False)
            self.__select_country("US")
            assert self.support_device.verify_speak_to_agent() is not False
        
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.__select_device_card("2KW5RR", False)
        self.__select_country("US")
        assert self.support_device.verify_speak_to_agent() is not False 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876168")  
    def test_26_verify_hp_community_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876168
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        assert self.support_device.verify_support_forum() is not False

        if self.app_env != "itg":
            self.__select_device_card("EE08VY", False)
            self.__select_country("US")
            assert self.support_device.verify_support_forum() is not False
        
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.__select_device_card("2KW5RR", False)
        self.__select_country("US")
        assert self.support_device.verify_support_forum() is not False 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876382")      
    def test_27_verify_contact_options(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876382
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")

        assert self.support_device.verify_chat_with_agent_display() is not False

        assert self.support_device.verify_speak_to_agent() is not False

        assert self.support_device.verify_support_forum() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876384")          
    def test_28_verify_chat_and_phone_not_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876384
        """
        self.__select_device_card("212007199")
        self.__select_country("US")

        assert self.support_device.verify_chat_with_agent_display() is False

        assert self.support_device.verify_speak_to_agent() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876387")   
    def test_29_verify_default_option(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876387
        """
        self.__select_device_card("212007199")
        self.__select_country("US")

        assert self.support_device.verify_support_forum() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35012574")  
    def test_30_click_get_phone_number(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35012574
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")

        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_get_phone_number_btn_state() == "true"
            # self.support_device.click_get_phone_number()
            # self.support_device.verify_get_phone_number() is not False          
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35409551")     
    def test_31_click_on_a_remote_poly(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35409551
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        
        self.support_device.click_va()
        time.sleep(5)
        assert self.support_va.verify_va_desc_window() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35348345")  
    def test_32_click_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35348345
        """
        self.__sign_in_HPX()
        assert self.support_home.verify_device_display("212007199") is not False
        if self.app_env != "itg":
            assert self.support_home.verify_device_display("EE08VY") is not False
        assert self.support_home.verify_device_display("2KW5RR") is not False
        assert self.support_home.verify_device_display("EE6PWG") is not False

        self.__sign_in_HPX()
        assert self.support_home.verify_device_display("212007199") is not False
        if self.app_env != "itg":
            assert self.support_home.verify_device_display("EE08VY") is not False
        assert self.support_home.verify_device_display("2KW5RR") is not False
        assert self.support_home.verify_device_display("EE6PWG") is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35876678")      
    def test_33_sign_in_and_check_the_remote_poly(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35876678
        """
        self.__sign_in_HPX()
        assert self.support_home.verify_device_display("212007199") is not False
        if self.app_env != "itg":
            assert self.support_home.verify_device_display("EE08VY") is not False
        assert self.support_home.verify_device_display("2KW5RR") is not False
        assert self.support_home.verify_device_display("EE6PWG") is not False

        self.support_home.click_refresh_btn()
        assert self.support_home.verify_device_display("212007199") is not False
        if self.app_env != "itg":
            assert self.support_home.verify_device_display("EE08VY") is not False
        assert self.support_home.verify_device_display("2KW5RR") is not False
        assert self.support_home.verify_device_display("EE6PWG") is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35077142")   
    def test_34_create_an_account(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35077142
        """
        self.__sign_in_HPX()
        
        assert self.support_home.verify_pn_label_display("2KW5RR") is not False
        assert self.support_home.verify_sn_label_display("2KW5RR") is not False
        assert self.support_home.verify_pname_label_display("2KW5RR") is not False

        assert self.support_home.verify_pn_label_display("EE6PWG") is not False
        assert self.support_home.verify_sn_label_display("EE6PWG") is not False
        assert self.support_home.verify_pname_label_display("EE6PWG") is not False

        assert self.support_home.verify_pn_label_display("212007199") is not False
        assert self.support_home.verify_sn_label_display("212007199") is not False
        assert self.support_home.verify_pname_label_display("212007199") is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35102570")   
    def test_35_add_different_poly_devices(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35102570
        """
        self.__select_device_card("2KW5RR")

        self.support_device.get_nick_name_value() == "My headset"
        self.support_device.click_back_btn()

        self.support_home.select_device_card("EE6PWG")
        self.support_device.get_nick_name_value() == "My desk phone"
        self.support_device.click_back_btn()

        self.support_home.select_device_card("212007199")
        self.support_device.get_nick_name_value() == "My conference device"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35936141")   
    def test_36_verify_the_phone_tooltips(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35936141
        """
        self.__select_device_card("2KW5RR")
        self.fc.select_country("US")
        assert self.support_device.get_phonehelptext() == "For Contract support, 24/7 English support is available. For Standard support, our hours are Monday – Friday from 5am till 5pm PST (excluding public holidays)."

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35013472")   
    def test_37_go_to_devicedetailspage(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35013472
        """
        self.__select_device_card("5CG02735RG")
        case_cards = self.support_device.get_case_cards()

        case_created_times = []
        for index in range(len(case_cards)):
            current_case_card = case_cards[index][-10:]
            case_created_time = self.support_device.get_case_created_time(current_case_card)
            case_created_times.append(datetime.strptime(case_created_time, '%m/%d/%Y'))

        assert case_created_times == sorted(case_created_times, reverse=True)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35014299")   
    def test_38_click_dropdownarrow(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35014299
        """
        self.__select_device_card("5CG02735RG")
        case_cards = self.support_device.get_case_cards()
        for index in range(len(case_cards)):
            current_case_id = case_cards[index][-10:]
            self.support_device.click_case_dropdown(current_case_id)
            time.sleep(3) 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35013466")     
    def test_39_when_no_case_in_account(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35013466
        """
        self.__select_device_card("CND7304VTB")
        self.__select_country("US")
        self.support_device.get_open_case_desc() == "There are currently no open cases"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_device_card(self, serial_number, sign_in_profile=True):
        self.__sign_in_HPX(sign_in_profile)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)

    def __sign_in_HPX(self, sign_in_profile=True):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        if sign_in_profile:
            self.fc.sign_out(self.web_driver)
            time.sleep(3)
            self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver) 
            time.sleep(5)
    
    def __create_phone_case(self):
        self.support_device.verify_speak_to_agent()
        self.support_device.click_speak_to_agent()
        self.support_device.click_category_cbx()
        self.support_device.click_category_opt(3)
        self.support_device.edit_problem("auto test")
        self.support_device.click_privacy_checkbox()
    
    def __select_country(self, country_index, current_locale=None):
        self.fc.select_country(country_index, current_locale)

    def __verify_redirector(self, serial_number, locale):
        self.__select_device_card(serial_number)
        self.__verify_website(locale)

    def __verify_website(self, locale):
        webpage = "HPCommunity"
        if locale in ["en-US", "zh-CN"]:
            self.support_device.click_HP_support_forum()
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)
            self.web_driver.wait_url_contains("https://hpsa-redirectors.hpcloud.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            url_parse = urlparse(current_url)
            country = parse_qs(url_parse.query)['Country'][0]
            lang = parse_qs(url_parse.query)['Lang'][0]
            assert '{}-{}'.format(lang, country) == locale
        else:
            assert self.support_device.verify_support_forum() == False

    def __verify_chat_agent_page_title(self):
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")               
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        if system_locale in ["en-US"]:
            self.support_device.click_chat_with_agent()
            if not self.support_device.verify_outside_hours_popup_display():
                assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
            else: 
                self.support_device.click_close_btn()  
        else:
            self.support_device.verify_chat_with_agent_display() == False        

    def __verify_hp_call_display(self):
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.support_device.click_speak_to_agent()      
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn() 

    def __click_remote_device_resource_link(self, web_pages, page_links, page_urls, serial_number):
        system_locale = self.fc.get_winsystemlocale().strip()
        self.__select_device_card(serial_number)
        self.__select_country("US")
        time.sleep(10)
        for webpage in web_pages:
            time.sleep(5)
            if system_locale in ["en-US", "zh-CN"]:
                self.support_device.click_link(page_links[webpage])
                time.sleep(3)
                self.web_driver.add_window(webpage)

                if webpage not in self.web_driver.session_data["window_table"].keys():
                    self.support_device.click_link(page_links[webpage])
                    time.sleep(3)
                    self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)
                self.web_driver.wait_url_contains(page_urls[webpage], timeout=30) 

                current_url = self.web_driver.get_current_url()
                self.web_driver.close_window(webpage)
                for sub_url in page_urls[webpage]:
                    assert sub_url in current_url 
            else:
                assert self.support_device.verify_link_display(page_links[webpage]) is False
