from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.web.support_document.support_flow_container import SupportFlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression_6033(object):
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

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897210")
    def test_01_hpx_rebranding_C65897210(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897210
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show()
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show() == b_show

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897211")
    def test_02_hpx_rebranding_C65897211(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897211
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page() == True
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page() == b_show

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897247")
    def test_03_hpx_rebranding_C65897247(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897247
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show()
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show() == b_show

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897248")
    def test_04_hpx_rebranding_C65897248(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897248
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show()
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show() == b_show

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897255")
    def test_05_hpx_rebranding_C65897255(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897255
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_video_lone_page()
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_video_lone_page() == b_show

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C65897262")
    def test_06_hpx_rebranding_C65897262(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65897262
        """
        self.fc.select_device()
        b_show = self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up()
        self.__click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up() == b_show

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

    def __click_profile_button(self):
        self.fc.click_profile_button()

    def __click_support_option(self):
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()

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