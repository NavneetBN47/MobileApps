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
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_01_verify_poly_device_headset(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35701272
        """
        self.__select_device_card("2KW5RR")

        assert self.support_device.get_nick_name_value() == "My headset"
        assert self.support_device.get_product_name_value() == "Voyager FOCUS UC B825 M USB-A"
        assert self.support_device.get_product_number_value() == "202652-102"
        assert self.support_device.get_serial_number_value() == "2KW5RR"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])  
    def test_02_verify_poly_device_deskphone(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35701282
        """
        self.__select_device_card("EE6PWG")

        assert self.support_device.get_nick_name_value() == "My desk phone"
        assert self.support_device.get_product_name_value() == "Sync 40 M"
        assert self.support_device.get_product_number_value() == "216875-01"
        assert self.support_device.get_serial_number_value() == "EE6PWG"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    def test_03_click_on_a_remote_poly_headset(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35701285
        """
        system_locale = self.fc.get_winsystemlocale().strip()

        self.__verify_redirector("2KW5RR", system_locale)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    def test_04_click_on_a_remote_poly_deskphone(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861323
        """
        system_locale = self.fc.get_winsystemlocale().strip()

        self.__verify_redirector("EE6PWG", system_locale)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_05_click_chat_on_poly_headset(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35701285
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        self.__verify_chat_agent_page_title()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])  
    def test_06_click_chat_on_poly_deskphone(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861317
        """
        self.__select_device_card("EE6PWG")   
        self.__select_country("US") 
        self.__verify_chat_agent_page_title() 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_07_click_speak_on_poly_headset(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861319
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        self.__verify_hp_call_display()
    
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_08_click_speak_on_poly_deskphone(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861319
        """
        self.__select_device_card("EE6PWG")
        self.__select_country("US")
        self.__verify_hp_call_display()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_09_click_on_a_remote_poly_headset(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861321
        """
        web_pages = ["SUPPORT_FORUM"]

        page_links = {"SUPPORT_FORUM": self.support_device.SUPPORT_FORUM}

        page_urls = {"SUPPORT_FORUM": "https://h30434.www3.hp.com/"}     

        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "2KW5RR") 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_10_click_on_a_remote_poly_deskphone(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861324
        """
        web_pages = ["SUPPORT_FORUM"]

        page_links = {"SUPPORT_FORUM": self.support_device.SUPPORT_FORUM}

        page_urls = {"SUPPORT_FORUM": "https://h30434.www3.hp.com/"}     

        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "EE6PWG") 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_11_verify_phone_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861326
        """
        self.fc.update_hpx_support_locale("en-US")

        self.__select_device_card("2KW5RR")
        
        self.__select_country("US", "en-US")
        
        assert self.support_device.verify_speak_to_agent() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    def test_12_verify_phone_not_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861333
        """
        self.fc.update_hpx_support_locale("zh-CN")

        self.__select_device_card("2KW5RR")

        self.__select_country("CN", "zh-CN")

        assert self.support_device.verify_speak_to_agent() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_13_verify_chat_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861328
        """
        self.fc.update_hpx_support_locale("en-US")

        self.__select_device_card("2KW5RR")

        self.__select_country("US", "en-US")

        assert self.support_device.verify_chat_with_agent_display() is not False


    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_14_verify_chat_not_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861334
        """
        self.fc.update_hpx_support_locale("zh-CN")

        self.__select_device_card("2KW5RR")

        self.__select_country("CN", "zh-CN")

        assert self.support_device.verify_chat_with_agent_display() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_15_verify_hp_community_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861336
        """
        self.fc.update_hpx_support_locale("en-US")

        self.__select_device_card("2KW5RR")
        
        self.__select_country("US", "en-US")

        assert self.support_device.verify_support_forum() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_16_verify_hp_community_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35861337
        """
        self.fc.update_hpx_support_locale("zh-CN")

        self.__select_device_card("2KW5RR")

        self.__select_country("CN", "zh-CN")

        assert self.support_device.verify_support_forum() is not False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34965265") 
    def test_17_verify_contact_options(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34965265
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        chat_with_hp_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']['chatWithHPSupport']
        hp_community_title = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['HPCommunity']['title']
        hp_comminity_des = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['HPCommunity']['description']
        
        self.__select_device_card("2KW5RR")
        self.__select_country("US")

        self.support_device.get_chat_with_agent_title() == "{} {}".format(chat_with_an_agent, chat_with_hp_support)
        # self.support_device.get_speak_to_agent_title() == "Phone In warranty products receive free phone support. Out of warranty products may require a fee for phone support."
        self.support_device.get_support_form_card_value() == "{} {}".format(hp_community_title, hp_comminity_des)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35012578") 
    def test_18_verify_the_order(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35012578
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        x_pos_chat = self.support_device.verify_chat_with_agent_display().rect['x']
        x_pos_speak = self.support_device.verify_speak_to_agent().rect['x']
        assert x_pos_speak > x_pos_chat 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35015277") 
    def test_19_click_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35015277
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        self.__verify_chat_agent_page_title()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C35025124") 
    def test_20_click_speak_to_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35025124
        """
        self.__select_device_card("2KW5RR")
        self.__select_country("US")
        self.__verify_hp_call_display()

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
