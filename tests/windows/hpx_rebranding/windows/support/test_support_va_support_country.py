from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_VA_Support_Country(object):
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

    # @pytest.mark.require_stack(["dev", "itg", "production"])    
    # @pytest.mark.testrail("S57581.C59373358")
    # @pytest.mark.parametrize("country, country_code, language", [
    #                                     ("US",  244,  "en-US"),
    #                                     ("GB",  242,  "en-GB"),
    #                                     ("SA",  205,  "ar-SA"),
    #                                     ("BG",  35,   "bg"),
    #                                     ("CZ",  75,   "cs"),
    #                                     ("DK",  61,   "da"),
    #                                     ("DE",  94,   "de-DE"),
    #                                     ("GR",  98,   "el"),
    #                                     ("ES",  128,  "es-ES"),
    #                                     ("EE",  233,  "et"),
    #                                     ("FI",  77,   "fi"),
    #                                     ("CA",  39,   "fr-CA"),
    #                                     ("FR",  84,   "fr-FR"),
    #                                     ("IL",  117,  "he"),
    #                                     ("HR",  108,  "hr-HR"),
    #                                     ("HU",  109,  "hu"),
    #                                     ("IT",  118,  "it-IT"),
    #                                     ("JP",  122,  "ja"),
    #                                     ("KR",  134,  "ko"),
    #                                     ("LT",  141,  "lt"),
    #                                     ("LV",  140,  "lv"),
    #                                     ("NO",  177,  "nb"),
    #                                     ("NL",  176,  "nl-NL"),
    #                                     ("PL",  191,  "pl"),
    #                                     ("BR",  55,   "pt-BR"),
    #                                     ("PT",  193,  "pt-PT"),
    #                                     ("RO",  200,  "ro"),
    #                                     ("RU",  202,  "ru"),
    #                                     ("SK",  143,  "sk"),
    #                                     ("SI",  212,  "sl"),
    #                                     ("SE",  221,  "sv-SE"),
    #                                     ("TH",  227,  "th"),
    #                                     ("TR",  235,  "tr"),
    #                                     ("UA",  241,  "uk"),
    #                                     ("CN",  45,   "zh-Hans-CN"),
    #                                     ("TW",  237,  "zh-Hant-TW")
    #                                     ]
    #                                     )
    # def test_01_hpx_rebranding_C59373358(self, country, country_code, language): 
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/59373358
    #     """ 
    #     self.__verify_va_support_country(country, country_code, language)
    
    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919583")    
    def test_01_hpx_rebranding_C63919583(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919583
        """ 
        self.__verify_va_support_country("US", 244, "en-US")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919584")   
    def test_02_hpx_rebranding_C63919584(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919584
        """ 
        self.__verify_va_support_country("GB", 242, "en-GB")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919585")
    def test_03_hpx_rebranding_C63919585(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919585
        """
        self.__verify_va_support_country("SA", 205, "ar-SA")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919586")
    def test_04_hpx_rebranding_C63919586(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919586
        """
        self.__verify_va_support_country("BG", 35, "bg")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919587")
    def test_05_hpx_rebranding_C63919587(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919587
        """
        self.__verify_va_support_country("CZ", 75, "cs")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919588")
    def test_06_hpx_rebranding_C63919588(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919588
        """
        self.__verify_va_support_country("DK", 61, "da")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919592")
    def test_07_hpx_rebranding_C63919592(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919592
        """
        self.__verify_va_support_country("DE", 94, "de-DE")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919593")
    def test_08_hpx_rebranding_C63919593(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919593
        """
        self.__verify_va_support_country("GR", 98, "el")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919594")
    def test_09_hpx_rebranding_C63919594(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919594
        """
        self.__verify_va_support_country("ES", 128, "es-ES")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919595")
    def test_10_hpx_rebranding_C63919595(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919595
        """
        self.__verify_va_support_country("EE", 233, "et")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919596")
    def test_11_hpx_rebranding_C63919596(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919596
        """
        self.__verify_va_support_country("FI", 77, "fi")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919600")
    def test_12_hpx_rebranding_C63919600(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919600
        """
        self.__verify_va_support_country("CA", 39, "fr-CA")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919601")
    def test_13_hpx_rebranding_C63919601(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919601
        """
        self.__verify_va_support_country("FR", 84, "fr-FR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919602")
    def test_14_hpx_rebranding_C63919602(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919602
        """
        self.__verify_va_support_country("IL", 117, "he")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919603")
    def test_15_hpx_rebranding_C63919603(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919603
        """
        self.__verify_va_support_country("HR", 108, "hr-HR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919604")
    def test_16_hpx_rebranding_C63919604(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919604
        """
        self.__verify_va_support_country("HU", 109, "hu")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919605")
    def test_17_hpx_rebranding_C63919605(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919605
        """
        self.__verify_va_support_country("IT", 118, "it-IT")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919613")
    def test_18_hpx_rebranding_C63919613(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919613
        """
        self.__verify_va_support_country("JP", 122, "ja")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919614")
    def test_19_hpx_rebranding_C63919614(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919614
        """
        self.__verify_va_support_country("KR", 134, "ko")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919615")
    def test_20_hpx_rebranding_C63919615(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919615
        """
        self.__verify_va_support_country("LT", 141, "lt")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919616")
    def test_21_hpx_rebranding_C63919616(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919616
        """
        self.__verify_va_support_country("LV", 140, "lv")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919617")
    def test_22_hpx_rebranding_C63919617(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919617
        """
        self.__verify_va_support_country("NO", 177, "nb")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919618")
    def test_23_hpx_rebranding_C63919618(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919618
        """
        self.__verify_va_support_country("NL", 176, "nl-NL")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919619")
    def test_24_hpx_rebranding_C63919619(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919619
        """
        self.__verify_va_support_country("PL", 191, "pl")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63919620")
    def test_25_hpx_rebranding_C63919620(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63919620
        """
        self.__verify_va_support_country("BR", 55, "pt-BR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920644")
    def test_26_hpx_rebranding_C63920644(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920644
        """
        self.__verify_va_support_country("PT", 193, "pt-PT")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920645")
    def test_27_hpx_rebranding_C63920645(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920645
        """
        self.__verify_va_support_country("RO", 184, "ro")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920653")
    def test_28_hpx_rebranding_C63920653(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920653
        """
        self.__verify_va_support_country("RU", 202, "ru")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920654")
    def test_29_hpx_rebranding_C63920654(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920654
        """
        self.__verify_va_support_country("SK", 143, "sk")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920655")
    def test_30_hpx_rebranding_C63920655(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920655
        """
        self.__verify_va_support_country("SI", 212, "sl")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920656")
    def test_31_hpx_rebranding_C63920656(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920656
        """
        self.__verify_va_support_country("SE", 221, "sv-SE")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920657")
    def test_32_hpx_rebranding_C63920657(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920657
        """
        self.__verify_va_support_country("TH", 227, "th")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920658")
    def test_33_hpx_rebranding_C63920658(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920658
        """
        self.__verify_va_support_country("TR", 235, "tr")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920659")
    def test_34_hpx_rebranding_C63920659(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920659
        """
        self.__verify_va_support_country("UA", 241, "uk")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920660")
    def test_35_hpx_rebranding_C63920660(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920660
        """
        self.__verify_va_support_country("CN", 45, "zh-Hans-CN")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63920661")
    def test_36_hpx_rebranding_C63920661(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63920661
        """
        self.__verify_va_support_country("TW", 237, "zh-Hant-TW")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self):
        self.fc.restart_app()
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

    def __verify_va_support_country(self, country, country_code, language):
        print("LANG={}".format(language))
        print("COUNTRY={}".format(country))
        print("NATION={}".format(country_code))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Name", country)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Nation", country_code)
        self.__set_prefered_language(language)
        self.fc.select_device()
        #['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pl', 'pt', 'sv', 'tr', 'zh-CN']
        if language in ["en-US", "en-GB", "es-ES", "fr-CA", "fr-FR",
                        "it-IT", "ja", "ko", "nl-NL", "pl", 
                        "pt-BR", "pt-PT", "sv-SE", "tr", "zh-Hans-CN"]:
            assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        else:
            assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == False