from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression_5315_part2(object):
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

        cls.stack = request.config.getoption("--stack")
        cls.__first_start_HPX(cls)
        
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 244)
        self.__set_prefered_language("en-US")
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    # @pytest.mark.testrail("S57581.C43091777")
    # @pytest.mark.parametrize("country, country_code, language, localize_links", [
    #                                     ("SA",  205,  "ar-SA",   "https://support.hp.com/emea_middle_east-ar/dashboard"),
    #                                     ("BG",  35,   "bg",      "https://support.hp.com/bg-en/dashboard"),
    #                                     ("CZ",  75,   "cs",      "https://support.hp.com/cz-cs/dashboard"),
    #                                     ("DK",  61,   "da",      "https://support.hp.com/dk-da/dashboard"),
    #                                     ("DE",  94,   "de-DE",   "https://support.hp.com/de-de/dashboard"),
    #                                     ("GR",  98,   "el",      "https://support.hp.com/gr-el/dashboard"),
    #                                     ("GB",  242,  "en-GB",   "https://support.hp.com/gb-en/dashboard"),
    #                                     ("ES",  128,  "es-ES",   "https://support.hp.com/es-es/dashboard"),
    #                                     ("EE",  233,  "et",      "https://support.hp.com/ee-et/dashboard"),
    #                                     ("FI",  77,   "fi",      "https://support.hp.com/fi-fi/dashboard"),
    #                                     ("CA",  39,   "fr-CA",   "https://support.hp.com/ca-fr/dashboard"),
    #                                     ("FR",  84,   "fr-FR",   "https://support.hp.com/fr-fr/dashboard"),
    #                                     ("IL",  117,  "he",      "https://support.hp.com/il-he/dashboard"),
    #                                     ("HR",  108,  "hr-HR",   "https://support.hp.com/hr-hr/dashboard"),
    #                                     ("HU",  109,  "hu",      "https://support.hp.com/hu-hu/dashboard"),
    #                                     ("IT",  118,  "it-IT",   "https://support.hp.com/it-it/dashboard"),
    #                                     ("JP",  122,  "ja",      "https://support.hp.com/jp-ja/dashboard"),
    #                                     ("KR",  134,  "ko",      "https://support.hp.com/kr-ko/dashboard"),
    #                                     ("LT",  141,  "lt",      "https://support.hp.com/lt-en/dashboard"),
    #                                     ("LV",  140,  "lv",      "https://support.hp.com/lv-lv/dashboard"),
    #                                     ("NO",  177,  "nb",      "https://support.hp.com/no-nb/dashboard"),
    #                                     ("NL",  176,  "nl-NL",   "https://support.hp.com/nl-nl/dashboard"),
    #                                     ("PL",  191,  "pl",      "https://support.hp.com/pl-pl/dashboard"),
    #                                     ("BR",  55,   "pt-BR",   "https://support.hp.com/br-pt/dashboard"),
    #                                     ("PT",  193,  "pt-PT",   "https://support.hp.com/pt-pt/dashboard"),
    #                                     ("RO",  200,  "ro",      "https://support.hp.com/ro-ro/dashboard"),
    #                                     ("RU",  203,  "ru-RU",   "https://support.hp.com/kz-ru"),
    #                                     ("SK",  143,  "sk",      "https://support.hp.com/sk-sk/dashboard"),
    #                                     ("SI",  212,  "sl",      "https://support.hp.com/si-en/dashboard"),
    #                                     ("SE",  221,  "sv-SE",   "https://support.hp.com/se-sv/dashboard"),
    #                                     ("TH",  227,  "th",      "https://support.hp.com/th-th/dashboard"),
    #                                     ("TR",  235,  "tr",      "https://support.hp.com/tr-tr/dashboard"),
    #                                     ("UA",  241,  "uk",      "https://support.hp.com/ua-uk/dashboard"),
    #                                     ("CN",  45,   "zh-Hans-CN", "https://support.hp.com/cn-zh/dashboard"),
    #                                     ("TW",  237,  "zh-Hant-TW", "https://support.hp.com/tw-zh/dashboard")
    #                                     ]
    #                                     )
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65791145")
    def test_01_hpx_rebranding_C65791145(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65791145
        """
        self.__verify_product_page_title_localize("KR", 134, "ko")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784713")
    def test_02_hpx_rebranding_C65784713(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784713
        """
        self.__verify_product_page_title_localize("LT", 141, "lt")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784729")
    def test_03_hpx_rebranding_C65784729(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784729
        """
        self.__verify_product_page_title_localize("LV", 140, "lv")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784734")
    def test_04_hpx_rebranding_C65784734(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784734
        """
        self.__verify_product_page_title_localize("NO", 177, "nb")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784742")
    def test_05_hpx_rebranding_C65784742(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784742
        """
        self.__verify_product_page_title_localize("NL", 176, "nl-NL")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65791146")
    def test_06_hpx_rebranding_C65791146(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65791146
        """
        self.__verify_product_page_title_localize("PL", 191, "pl")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784765")
    def test_07_hpx_rebranding_C65784765(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784765
        """
        self.__verify_product_page_title_localize("BR", 55, "pt-BR")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784779")
    def test_08_hpx_rebranding_C65784779(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784779
        """
        self.__verify_product_page_title_localize("PT", 193, "pt-PT")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784795")
    def test_09_hpx_rebranding_C65784795(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784795
        """
        self.__verify_product_page_title_localize("RO", 184, "ro")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784798")
    def test_10_hpx_rebranding_C65784798(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784798
        """
        self.__verify_product_page_title_localize("RU", 203, "ru-RU")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784807")
    def test_11_hpx_rebranding_C65784807(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784807
        """
        self.__verify_product_page_title_localize("SK", 143, "sk")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65791232")
    def test_12_hpx_rebranding_C65791232(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65791232
        """
        self.__verify_product_page_title_localize("SI", 212, "sl")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784820")
    def test_13_hpx_rebranding_C65784820(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784820
        """
        self.__verify_product_page_title_localize("SE", 221, "sv-SE")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65791233")
    def test_14_hpx_rebranding_C65791233(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65791233
        """
        self.__verify_product_page_title_localize("TH", 227, "th")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784834")
    def test_15_hpx_rebranding_C65784834(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784834
        """
        self.__verify_product_page_title_localize("TR", 235, "tr")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784874")
    def test_16_hpx_rebranding_C65784874(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784874
        """
        self.__verify_product_page_title_localize("UA", 241, "uk")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784890")
    def test_17_hpx_rebranding_C65784890(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784890
        """
        self.__verify_product_page_title_localize("CN", 45, "zh-Hans-CN")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65784895")
    def test_18_hpx_rebranding_C65784895(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65784895
        """
        self.__verify_product_page_title_localize("HK", 237, "zh-Hant-HK")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################    
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self):
        self.__start_HPX()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __verify_product_page_title_localize(self, country_code, country_nation, language):
        print("COUNTRY={}".format(country_code))
        print("NATION={}".format(country_nation))
        print("LANG={}".format(language))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device()
        # if country_code in ["GB", "CA", "HR", "NL", "RO", "RU", "TR", "TW"]:
        if country_code in ["GB"]:
            assert self.fc.fd["devices_support_pc_mfe"].get_product_support_center_btn_text() == "Get more help on our website"
        else:
            assert self.fc.fd["devices_support_pc_mfe"].get_product_support_center_btn_text() != "Get more help on our website"

    def __get_language_list(self):
        languages = self.registry.get_registry_value(
            "HKEY_CURRENT_USER\\Control Panel\\International\\User Profile", 
            "Languages"
            )
        if languages:
            languages = languages['stdout']
            languages = languages.strip()
            languages = languages.replace('\r\n', '')
            languages = languages.split('REG_MULTI_SZ')[1]
            languages = languages.strip()
            languages = languages.split('\\0')
            return languages
        return []
    
    def __set_language_list(self, language_list):
        reg_multi_sz_value = "@(" + ",".join([f'"{lang}"' for lang in language_list]) + ")"
        path = self.registry.format_registry_path("HKEY_CURRENT_USER\\Control Panel\\International\\User Profile")
        key_name = "Languages"
        key_value = reg_multi_sz_value
        self.driver.ssh.send_command('Set-Itemproperty -path \"{}\" -Name \"{}\" -Value {}'.format(path, key_name, key_value), raise_e=False)

    def __set_prefered_language(self, language):
        language_list = self.__get_language_list()
        if language in language_list:
            language_list.remove(language)
            language_list.insert(0, language)
        self.__set_language_list(language_list)