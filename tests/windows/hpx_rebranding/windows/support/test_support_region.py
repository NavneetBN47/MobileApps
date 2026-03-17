from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import logging
import time

pytest.app_info = "HPX"
class Test_Suite_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup

        cls.logger=logging.getLogger()
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Nation", 244)
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        def set_default_language():
            self.__set_default_language()
        request.addfinalizer(set_default_language)

    # @pytest.mark.parametrize("country_code, country_nation, country_name",
    #                          [
    #                             ("MF", "31706", "Saint Martin"),
    #                             ("GU", "322", "Guam"),
    #                             ("AX", "10028789", "Åland Islands"),
    #                             ("RU", "203", "Russian Federation"),
    #                             ("SX", "30967", "Sint Maarten"),
    #                             ("NR", "180", "Nauru"), 
    #                             ("TV", "236", "Tuvalu"),
    #                             ("HM", "325", "Heard Island and McDonald Islands"),
    #                             ("BV", "306", "Bouvet Island"),
    #                             ("IO", "114", "British Indian Ocean Territory"),
    #                             ("PW", "195", "Palau"),
    #                             ("PN", "339", "Pitcairn Islands"),
    #                             ("BY", "29", "Belarus"),
    #                             ("JE", "328", "Jersey"),
    #                             ("FK", "315", "Falkland Islands"),
    #                             ("GS", "342", "South Georgia and the South Sandwich Islands"),
    #                             ("MP", "52", "Northern Mariana Islands")
    #                         ])
    # def test_01_hpx_rebranding(self, country_code, country_nation, country_name):
    #     """
    #     https://hp-jira.external.hp.com/browse/HPXSUP-3927
    #     """
    #     self.__test_region(country_code, country_nation, country_name)

    # @pytest.mark.parametrize("country_code, country_nation, country_name",  
    #                          [
    #                             ("RU", "203", "Russian Federation"),
    #                             ("BY", "29", "Belarus")                         
    #                         ])  
    # @pytest.mark.require_stack(["dev", "itg", "production"])    
    # @pytest.mark.testrail("S57581.C63919614")
    # def test_02_hpx_rebranding(self, country_code, country_nation, country_name):    
    #     """
    #     https://hp-jira.external.hp.com/browse/HPXSUP-3926
    #     """
    #     self.__test_region(country_code, country_nation, country_name)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63982253")
    def test_01_hpx_rebranding_C63982253(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63982253
        """
        self.__test_region("RU", "203", "Russian Federation", "ru-RU")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C63982254")
    def test_02_hpx_rebranding_C63982254(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63982254
        """
        self.__test_region("BY", "29", "Belarus", "be-BY")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C68095577")
    def test_03_hpx_rebranding_C68095577(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68095577
        """
        self.__test_region("IR", "116", "Iran", "fa-IR")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C68095578")
    def test_04_hpx_rebranding_C68095578(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68095578
        """
        self.__test_region("KP", "131", "North Korea", "ko-KP")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C68095579")
    def test_05_hpx_rebranding_C68095579(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68095579
        """
        self.__test_region("CU", "56", "Cuba", "es-CU")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C68095675")
    def test_06_hpx_rebranding_C68095675(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68095675
        """
        self.__test_region("SD", "219", "Sudan", "ar-SD")

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C68095676")
    def test_07_hpx_rebranding_C68095676(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/68095676
        """
        self.__test_region("SY", "222", "Syria", "ar-SY")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __test_region(self, country_code, country_nation, country_name, language):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        if country_code in ["RU", "BY", "IR", "KP", "CU", "SD", "SY"]:
            self.fc.select_device()
            time.sleep(10)
            self.__verify_embargo_country()
            # assert _country_code == "Kazakhstan"
        else:
            # self.__reinstall_HPX()
            self.fc.select_device()
            time.sleep(15)
            self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
            _country_code = self.fc.fd["devices_support_pc_mfe"].get_country()
            logging.info("=====country_code: {}".format(_country_code))
            assert _country_code == country_name

    def __reinstall_HPX(self):
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        time.sleep(60)
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build)  

    def __start_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self):
        self.__start_HPX()

    def __verify_embargo_country(self):
        assert self.fc.fd["devices_support_pc_mfe"].verify_embargo_country_closed_btn() == True

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

    def __set_default_language(self):
        default_language = "en-US"
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 244)
        self.__set_prefered_language(default_language)