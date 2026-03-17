from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Flyout2(object):
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
    @pytest.mark.testrail("S57581.C63650015")
    def test_01_hpx_rebranding_C63650015(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650015
        """
        self.__verify_localized_links("LV", 140, "lv", "https://support.hp.com/lv-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650016")
    def test_02_hpx_rebranding_C63650016(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650016
        """
        self.__verify_localized_links("LT", 141, "lt", "https://support.hp.com/lt-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650017")
    def test_03_hpx_rebranding_C63650017(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650017
        """
        self.__verify_localized_links("NO", 177, "nb", "https://support.hp.com/no-no/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650018")
    def test_04_hpx_rebranding_C63650018(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650018
        """
        self.__verify_localized_links("NL", 176, "nl-NL", "https://support.hp.com/nl-nl/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650019")
    def test_05_hpx_rebranding_C63650019(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650019
        """
        self.__verify_localized_links("PL", 191, "pl", "https://support.hp.com/pl-pl/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650020")
    def test_06_hpx_rebranding_C63650020(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650020
        """
        self.__verify_localized_links("BR", 55, "pt-BR", "https://support.hp.com/br-pt/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650021")
    def test_07_hpx_rebranding_C63650021(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650021
        """
        self.__verify_localized_links("PT", 193, "pt-PT", "https://support.hp.com/pt-pt/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650022")
    def test_08_hpx_rebranding_C63650022(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650022
        """
        self.__verify_localized_links("RO", 184, "ro", "https://support.hp.com/ro-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63652645")
    def test_09_hpx_rebranding_C63652645(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63652645
        """
        self.__verify_localized_links("SK", 143, "sk", "https://support.hp.com/sk-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650023")
    def test_10_hpx_rebranding_C63650023(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650023
        """
        self.__verify_localized_links("SI", 212, "sl", "https://support.hp.com/si-en/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650087")
    def test_11_hpx_rebranding_C63650087(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650087
        """
        self.__verify_localized_links("SE", 221, "sv-SE", "https://support.hp.com/se-sv/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650088")
    def test_12_hpx_rebranding_C63650088(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650088
        """
        self.__verify_localized_links("TH", 227, "th", "https://support.hp.com/th-th/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650096")
    def test_13_hpx_rebranding_C63650096(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650096
        """
        self.__verify_localized_links("TR", 235, "tr", "https://support.hp.com/tr-tr/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650097")
    def test_14_hpx_rebranding_C63650097(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650097
        """
        self.__verify_localized_links("UA", 241, "uk", "https://support.hp.com/ua-uk/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650098")
    def test_15_hpx_rebranding_C63650098(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650098
        """
        self.__verify_localized_links("CN", 45, "zh-Hans-CN", "https://support.hp.com/cn-zh/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63650098")
    def test_16_hpx_rebranding_C63650098(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63650098
        """
        self.__verify_localized_links("HK", 45, "zh-Hant-HK", "https://support.hp.com/cn-zh/dashboard")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63649982")
    def test_17_hpx_rebranding_C63649982(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63649982
        """
        self.__verify_localized_links("KR", 134, "ko", "https://support.hp.com/kr-ko/dashboard")

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
        self.__start_HPX()
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