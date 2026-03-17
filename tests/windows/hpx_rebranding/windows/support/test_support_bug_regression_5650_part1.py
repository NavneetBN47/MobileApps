from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression_5650_part1(object):
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
    @pytest.mark.testrail("S57581.C65751712")
    def test_01_hpx_rebranding_C65751712(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751712
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("SA", 205, "ar-SA")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65751715")
    def test_02_hpx_rebranding_C65751715(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751715
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("BG", 35, "bg")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65751799")
    def test_03_hpx_rebranding_C65751799(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751799
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("CZ", 75, "cs")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65751802")
    def test_04_hpx_rebranding_C65751802(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751802
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("DK", 61, "da")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65751805")
    def test_05_hpx_rebranding_C65751805(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751805
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("DE", 94, "de-DE")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65751807")
    def test_06_hpx_rebranding_C65751807(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65751807
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("GR", 98, "el")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65752220")
    def test_07_hpx_rebranding_C65752220(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65752220
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("GB", 242, "en-GB")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753077")
    def test_08_hpx_rebranding_C65753077(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753077
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("ES", 128, "es-ES")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753078")
    def test_09_hpx_rebranding_C65753078(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753078
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("EE", 233, "et")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753080")
    def test_10_hpx_rebranding_C65753080(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753080
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("FI", 77, "fi")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753082")
    def test_11_hpx_rebranding_C65753082(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753082
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("CA", 39, "fr-CA")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753086")
    def test_12_hpx_rebranding_C65753086(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753086
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("FR", 84, "fr-FR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753088")
    def test_13_hpx_rebranding_C65753088(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753088
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("IL", 117, "he")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753089")
    def test_14_hpx_rebranding_C65753089(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753089
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("HR", 108, "hr-HR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753091")
    def test_15_hpx_rebranding_C65753091(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753091
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("HU", 109, "hu")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753092")
    def test_16_hpx_rebranding_C65753092(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753092
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("IT", 118, "it-IT")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753093")
    def test_17_hpx_rebranding_C65753093(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753093
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("JP", 122, "ja")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C65753257")
    def test_18_hpx_rebranding_C65753257(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65753257
        """
        self.__verify_search_items_localize_when_click_region_list_mulitple_times("TW", 237, "zh-Hant-TW")

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

    def __verify_search_items_localize_when_click_region_list_mulitple_times(self, country_code, country_nation, language):
        print("COUNTRY={}".format(country_code))
        print("NATION={}".format(country_nation))
        print("LANG={}".format(language))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device() 
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].click_country_list()
        self.fc.fd["devices_support_pc_mfe"].click_country_list()
        self.fc.fd["devices_support_pc_mfe"].click_country_list()
        assert self.fc.fd["devices_support_pc_mfe"].get_country_select_edit_text() != "Search Items"

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