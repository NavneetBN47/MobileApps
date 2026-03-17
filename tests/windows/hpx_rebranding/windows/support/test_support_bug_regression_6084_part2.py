from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.web.support_document.support_flow_container import SupportFlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression_6084_part2(object):
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
    #                                     ("PL",  191,  "pl",      "https://support.hp.com/pl-pl/dashboard"),
    #                                     ("RU",  203,  "ru-RU",   "https://support.hp.com/kz-ru"),
    #                                     ("SK",  143,  "sk",      "https://support.hp.com/sk-sk/dashboard"),
    #                                     ("SI",  212,  "sl",      "https://support.hp.com/si-en/dashboard"),
    #                                     ("SE",  221,  "sv-SE",   "https://support.hp.com/se-sv/dashboard"),
    #                                     ("TH",  227,  "th",      "https://support.hp.com/th-th/dashboard"),
    #                                     ("TR",  235,  "tr",      "https://support.hp.com/tr-tr/dashboard"),
    #                                     ("UA",  241,  "uk",      "https://support.hp.com/ua-uk/dashboard"),
    #                                     ("CN",  45,   "zh-Hans-CN", "https://support.hp.com/cn-zh/dashboard"),
    #                                     ("TW",  237,  "zh-Hant-TW", "https://support.hp.com/tw-zh/dashboard"),
    #                                     ("GR",  98,   "el",      "https://support.hp.com/gr-el/dashboard"),
    #                                     ("GB",  242,  "en-GB",   "https://support.hp.com/gb-en/dashboard"),
    #                                     ("NO",  177,  "nb",      "https://support.hp.com/no-nb/dashboard"),
    #                                     ("NL",  176,  "nl-NL",   "https://support.hp.com/nl-nl/dashboard"),
    #                                     ("BR",  55,   "pt-BR",   "https://support.hp.com/br-pt/dashboard"),
    #                                     ("PT",  193,  "pt-PT",   "https://support.hp.com/pt-pt/dashboard"),
    #                                     ("RO",  200,  "ro",      "https://support.hp.com/ro-ro/dashboard")
    #                                     ]
    #                                     )
    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300054")
    def test_01_hpx_rebranding_C66300054(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300054
        """
        self.__verify_nickname("KR", 134, "ko")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300055")
    def test_02_hpx_rebranding_C66300055(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300055
        """
        self.__verify_nickname("LT", 141, "lt")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300056")
    def test_03_hpx_rebranding_C66300056(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300056
        """
        self.__verify_nickname("LV", 140, "lv")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300060")
    def test_04_hpx_rebranding_C66300060(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300060
        """
        self.__verify_nickname("PL", 191, "pl")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300065")
    def test_05_hpx_rebranding_C66300065(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300065
        """
        self.__verify_nickname("RU", 203, "ru-RU")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300129")
    def test_06_hpx_rebranding_C66300129(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300129
        """
        self.__verify_nickname("SK", 143, "sk")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300130")
    def test_07_hpx_rebranding_C66300130(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300130
        """
        self.__verify_nickname("SI", 212, "sl")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300131")
    def test_08_hpx_rebranding_C66300131(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300131
        """
        self.__verify_nickname("SE", 221, "sv-SE")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300132")
    def test_09_hpx_rebranding_C66300132(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300132
        """
        self.__verify_nickname("TH", 227, "th")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300133")
    def test_10_hpx_rebranding_C66300133(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300133
        """
        self.__verify_nickname("TR", 235, "tr")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300134")
    def test_11_hpx_rebranding_C66300134(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300134
        """
        self.__verify_nickname("UA", 241, "uk")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300150")
    def test_12_hpx_rebranding_C66300150(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300150
        """
        self.__verify_nickname("CN", 45, "zh-Hans-CN")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300265")
    def test_13_hpx_rebranding_C66300265(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300265
        """
        self.__verify_nickname("NO", 177, "nb")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300329")
    def test_14_hpx_rebranding_C66300329(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300329
        """
        self.__verify_nickname("NL", 176, "nl-NL")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300330")
    def test_15_hpx_rebranding_C66300330(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300330
        """
        self.__verify_nickname("BR", 55, "pt-BR")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300458")
    def test_16_hpx_rebranding_C66300458(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300458
        """
        self.__verify_nickname("PT", 193, "pt-PT")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300459")
    def test_17_hpx_rebranding_C66300459(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300459
        """
        self.__verify_nickname("RO", 184, "ro")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C66300459")
    def test_18_hpx_rebranding_C66300459(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66300459
        """
        self.__verify_nickname("HK", 184, "zh-Hant-HK")

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

    def __verify_nickname(self, country_code, country_nation, language):
        print("COUNTRY={}".format(country_code))
        print("NATION={}".format(country_nation))
        print("LANG={}".format(language))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device() 
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_device_name_by_back_devices_button() == "My Computer"

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