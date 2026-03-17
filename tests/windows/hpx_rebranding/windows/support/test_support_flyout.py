from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Flyout(object):
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

    @pytest.mark.require_stack(["dev", "itg", "production"])     
    @pytest.mark.testrail("S57581.C63649930")
    def test_01_hpx_rebranding_C63649930(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649930
        """
        self.__verify_localized_links("SA", 205, "ar-SA", "https://support.hp.com/emea_middle_east-ar/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649931")
    def test_02_hpx_rebranding_C63649931(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649931
        """
        self.__verify_localized_links("BG", 35, "bg", "https://support.hp.com/bg-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649932")
    def test_03_hpx_rebranding_C63649932(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649932
        """
        self.__verify_localized_links("CZ", 75, "cs", "https://support.hp.com/cz-cs/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649933")
    def test_04_hpx_rebranding_C63649933(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649933
        """
        self.__verify_localized_links("DK", 61, "da", "https://support.hp.com/dk-da/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649934")
    def test_05_hpx_rebranding_C63649934(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649934
        """
        self.__verify_localized_links("DE", 94, "de-DE", "https://support.hp.com/de-de/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649935")
    def test_06_hpx_rebranding_C63649935(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649935
        """
        self.__verify_localized_links("GR", 98, "el", "https://support.hp.com/gr-el/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649939")
    def test_07_hpx_rebranding_C63649939(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649939
        """
        self.__verify_localized_links("GB", 242, "en-GB", "https://support.hp.com/gb-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649971")
    def test_08_hpx_rebranding_C63649971(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649971
        """
        self.__verify_localized_links("US", 244, "en-US", "https://support.hp.com/us-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649972")
    def test_09_hpx_rebranding_C63649972(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649972
        """
        self.__verify_localized_links("ES", 128, "es-ES", "https://support.hp.com/es-es/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649973")
    def test_10_hpx_rebranding_C63649973(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649973
        """
        self.__verify_localized_links("EE", 233, "et", "https://support.hp.com/ee-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649974")
    def test_11_hpx_rebranding_C63649974(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649974
        """
        self.__verify_localized_links("FI", 77, "fi", "https://support.hp.com/fi-fi/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649975")
    def test_12_hpx_rebranding_C63649975(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649975
        """
        self.__verify_localized_links("CA", 39, "fr-CA", "https://support.hp.com/ca-fr/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649976")
    def test_13_hpx_rebranding_C63649976(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649976
        """
        self.__verify_localized_links("FR", 84, "fr-FR", "https://support.hp.com/fr-fr/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649977")
    def test_14_hpx_rebranding_C63649977(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649977
        """
        self.__verify_localized_links("IL", 117, "he", "https://support.hp.com/il-he/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649978")
    def test_15_hpx_rebranding_C63649978(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649978
        """
        self.__verify_localized_links("HR", 108, "hr-HR", "https://support.hp.com/hr-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649979")
    def test_16_hpx_rebranding_C63649979(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649979
        """
        self.__verify_localized_links("HU", 109, "hu", "https://support.hp.com/hu-hu/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649980")
    def test_17_hpx_rebranding_C63649980(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649980
        """
        self.__verify_localized_links("IT", 118, "it-IT", "https://support.hp.com/it-it/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649981")
    def test_18_hpx_rebranding_C63649981(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649981
        """
        self.__verify_localized_links("JP", 122, "ja", "https://support.hp.com/jp-ja/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650099")
    def test_19_hpx_rebranding_C63650099(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650099
        """
        self.__verify_localized_links("TW", 237, "zh-Hant-TW", "https://support.hp.com/tw-zh/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C43091713")
    def test_20_hpx_rebranding_C43091713(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/43091713
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_profile_sign_in_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True, "Start Virtual Assist button is not displayed"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C43091727")
    def test_21_hpx_rebranding_C43091727(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/43091727
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_profile_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_device(), "Support device card is not displayed"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C43091729")
    def test_22_hpx_rebranding_C43091729(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/43091729
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_profile_sign_in_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) , "'Get Help' is not displayed"
        # self.fc.fd["devices_support_pc_mfe"].click_profile_sign_in_button()
        # self.fc.fd["devices_support_pc_mfe"].select_support_option()
        # self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
        # assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) , "'Get Help' is not displayed"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C43091776")
    def test_23_hpx_rebranding_C43091776(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/43091776
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_profile_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_link() == True, "'Support' link is not displayed"

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

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)  

    def __verify_redirect_link(self, web_page, url_contains, url_expect, full_match=True):
        time.sleep(10)
        self.web_driver.wdvr.switch_to.window(self.web_driver.wdvr.window_handles[-1])
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        print("current_url={}".format(current_url))
        self.web_driver.wdvr.close()
        if full_match:
            assert current_url == url_expect
        else:
            assert url_expect in current_url

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

    def __verify_localized_links(self, country, country_code, language, localize_links):
        """
        Verify that the localized links redirect to the expected URL.
        """
        print("LANG={}".format(language))
        print("COUNTRY={}".format(country))
        print("NATION={}".format(country_code))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_code)
        self.__set_prefered_language(language)
        self.fc.select_device()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_profile_button()
        time.sleep(20)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_device_add_btn() 
        if country in ["US", "GB"] : 
            assert self.fc.fd["devices_support_pc_mfe"].get_add_device_page_title() == "Add a device"
        else:
            assert self.fc.fd["devices_support_pc_mfe"].get_add_device_page_title() != "Add a device"
        # self.fc.fd["profile"].click_support_link()
        # self.__verify_redirect_link("hp_support", "https://support.hp.com/", localize_links)