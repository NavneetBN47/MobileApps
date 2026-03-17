from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression2(object):
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
    @pytest.mark.testrail("S57581.C65574245")
    def test_01_hpx_rebranding_C65574245(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574245
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show():
            self.fc.fd["devices_support_pc_mfe"].click_audio_control_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574247")
    def test_02_hpx_rebranding_C65574247(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574247
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page():
            self.fc.fd["devices_support_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574253")
    def test_03_hpx_rebranding_C65574253(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574253
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_system_control_card_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574254")
    def test_04_hpx_rebranding_C65574254(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574254
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_wellbeing_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574255")
    def test_05_hpx_rebranding_C65574255(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574255
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up():
            self.fc.fd["devices_support_pc_mfe"].click_hppk_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574263")
    def test_06_hpx_rebranding_C65574263(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574263
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show():
            self.fc.fd["devices_support_pc_mfe"].click_audio_control_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574265")
    def test_07_hpx_rebranding_C65574265(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574265
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page():
            self.fc.fd["devices_support_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574266")
    def test_08_hpx_rebranding_C65574266(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574266
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_system_control_card_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False    
        
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574267")
    def test_09_hpx_rebranding_C65574267(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574267
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_wellbeing_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574268")
    def test_10_hpx_rebranding_C65574268(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574268
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up():
            self.fc.fd["devices_support_pc_mfe"].click_hppk_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574269")
    def test_11_hpx_rebranding_C65574269(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574269
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show():
            self.fc.fd["devices_support_pc_mfe"].click_audio_control_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574271")
    def test_12_hpx_rebranding_C65574271(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574271
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page():
            self.fc.fd["devices_support_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574272")
    def test_13_hpx_rebranding_C65574272(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574272
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_system_control_card_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574273")
    def test_14_hpx_rebranding_C65574273(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574273
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_wellbeing_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574274")
    def test_15_hpx_rebranding_C65574274(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574274
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up():
            self.fc.fd["devices_support_pc_mfe"].click_hppk_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False    

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574276")
    def test_16_hpx_rebranding_C65574276(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574276
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show():
            self.fc.fd["devices_support_pc_mfe"].click_audio_control_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574281")
    def test_17_hpx_rebranding_C65574281(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574281
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page():
            self.fc.fd["devices_support_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574282")
    def test_18_hpx_rebranding_C65574282(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574282
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_system_control_card_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574283")
    def test_19_hpx_rebranding_C65574283(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574283
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_wellbeing_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574284")
    def test_20_hpx_rebranding_C65574284(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574284
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up():
            self.fc.fd["devices_support_pc_mfe"].click_hppk_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574285")
    def test_21_hpx_rebranding_C65574285(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574285
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_audio_control_card_show():
            self.fc.fd["devices_support_pc_mfe"].click_audio_control_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574287")
    def test_22_hpx_rebranding_C65574287(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574287
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_display_control_lone_page():
            self.fc.fd["devices_support_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574288")
    def test_23_hpx_rebranding_C65574288(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574288
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_system_control_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_system_control_card_lone_page()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574289")
    def test_24_hpx_rebranding_C65574289(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574289
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_wellbeing_card_lone_page_show():
            self.fc.fd["devices_support_pc_mfe"].click_wellbeing_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C65574299")
    def test_25_hpx_rebranding_C65574299(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/65574299
        """
        self.fc.select_device()
        if self.fc.fd["devices_support_pc_mfe"].verify_hppk_card_show_up():
            self.fc.fd["devices_support_pc_mfe"].click_hppk_card()
            self.fc.fd["devices_support_pc_mfe"].click_back_devices_button()
            assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() is not False

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

