from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression(object):
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
    @pytest.mark.testrail("S57581.C59295967")
    def test_01_hpx_rebranding_C59295967(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59295967
        """
        # self.__start_HPX()
        self.fc.select_device()
        self.__sign_in_HPX()
        time.sleep(5)
        assert bool(self.fc.fd["devicesMFE"].verify_bell_icon_show_up()) is True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59295998")
    def test_02_hpx_rebranding_C59295998(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59295998
        """
        # self.__start_HPX()
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon() 
        self.__click_settings_option()   
        self.fc.fd["devices_support_pc_mfe"].click_signout_btn()
        time.sleep(5)
        assert bool(self.fc.fd["devicesMFE"].verify_bell_icon_show_up()) is True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296003")
    def test_03_hpx_rebranding_C59296003(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296003
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_settings_option()
        self.fc.fd["devices_support_pc_mfe"].click_signout_btn()
        # time.sleep(5)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_warranty_detail_btn()
        # assert "My Computer" in self.fc.fd["devicesMFE"].verify_back_button_rebranding_text() 
        assert self.fc.fd["devicesMFE"].verify_back_button_rebranding_text() != "" 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296007")
    def test_04_hpx_rebranding_C59296007(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296007
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_warranty_detail_btn()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_settings_option()
        self.fc.fd["devices_support_pc_mfe"].click_signout_btn()
        time.sleep(5)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        # assert "My Computer" in self.fc.fd["devicesMFE"].verify_back_button_rebranding_text()
        assert self.fc.fd["devicesMFE"].verify_back_button_rebranding_text() != ""

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296009")
    def test_05_hpx_rebranding_C59296009(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296009
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.__sign_in_HPX()
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_panel() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296010")
    def test_06_hpx_rebranding_C59296010(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296010
        """
        self.fc.select_device()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=50)
        self.fc.fd["devices_support_pc_mfe"].click_warranty_detail_btn()
        self.__sign_in_HPX()
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_page_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296012")
    def test_07_hpx_rebranding_C59296012(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296012
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.__sign_in_HPX()
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296013")
    def test_08_hpx_rebranding_C59296013(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296013
        """
        self.fc.select_device()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=50)
        self.fc.fd["devices_support_pc_mfe"].click_warranty_detail_btn()
        self.__sign_in_HPX()
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296159")
    def test_09_hpx_rebranding_C59296159(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296159
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.select_country("CN")
        time.sleep(10)
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        country_code = self.fc.fd["devices_support_pc_mfe"].get_country()
        assert country_code == "China"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59296164")
    def test_10_hpx_rebranding_C59296164(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59296164
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()
        self.__sign_in_HPX(user_icon_click=False)
        assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59483037")
    def test_11_hpx_rebranding_C59483037(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59483037
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_chat_page_title() == "Chat with an agent"
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C66302175")
    def test_12_hpx_rebranding_C66302175(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/66302175
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn()
        self.fc.fd["profile"].maximize_hp()
        time.sleep(5)
        self.fc.fd["profile"].maximize_hp()
        time.sleep(5)
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

    def __click_top_profile_icon(self):
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_top_profile_icon()
    
    def __click_settings_option(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].select_settings_option()

    def __select_device(self):
        self.__start_HPX()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __sign_in_HPX(self, user_icon_click=True, sign_in_from_profile=False):
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=user_icon_click, sign_in_from_profile=sign_in_from_profile)  

    def __verify_product_page_title_localize(self, country_code, country_nation, language):
        print("COUNTRY={}".format(country_code))
        print("NATION={}".format(country_nation))
        print("LANG={}".format(language))
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device()
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

