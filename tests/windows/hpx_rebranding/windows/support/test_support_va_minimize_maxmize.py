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
class Test_Suite_VA_Minimize_Maxmize(object):
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
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Nation", 244)
        self.__set_prefered_language("en-US")
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62531658")
    def test_01_hpx_rebranding_C62531658(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62531658
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_assistant_btn()

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62533617")
    def test_02_hpx_rebranding_C62533617(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62533617
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_assistant_btn() == True, "Assistant button is not displayed"

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62534320")
    def test_03_hpx_rebranding_C62534320(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62534320
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].click_assistant_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62534339")
    def test_04_hpx_rebranding_C62534339(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62534339
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn() 
        self.fc.fd["devices_support_pc_mfe"].click_keep_open_btn()
        self.fc.fd["devices_support_pc_mfe"].click_assistant_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62534403")
    def test_05_hpx_rebranding_C62534403(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62534403
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn() 
        self.fc.fd["devices_support_pc_mfe"].click_start_new_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_assistant_btn() != True, "Assistant button is displayed when it should not be"

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C62536804")
    def test_06_hpx_rebranding_C62536804(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62536804
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_chat_now_btn()
        self.fc.fd["devices_support_pc_mfe"].click_chat_minimize_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_live_agent_btn() == True, "Live Agent button is not displayed"
        assert self.fc.fd["devices_support_pc_mfe"].verify_assistant_btn() == True, "Assistant button is not displayed"

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C66302175")
    def test_07_hpx_rebranding_C66302175(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66302175
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.driver.swipe(direction="down", distance=15)
        self.fc.fd["device_card"].verify_product_information()
        self.fc.fd["device_card"].verify_warrenty_status()

    @pytest.mark.require_stack(["dev", "itg"])    
    @pytest.mark.testrail("S57581.C68231283")
    def test_08_hpx_rebranding_C68231283(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68231283
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_minimize_btn()
        self.driver.swipe(direction="down", distance=15)
        self.fc.fd["device_card"].verify_product_information()
        self.fc.fd["device_card"].verify_warrenty_status()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self, maxmized=False):
        self.fc.restart_app()
        if maxmized:
            self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self, maxmized=False):
        self.__start_HPX(maxmized=maxmized)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)       

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