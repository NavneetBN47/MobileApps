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
class Test_Suite_Device_Unification(object):
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
    @pytest.mark.testrail("S57581.C64746472")    
    def test_01_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_device(0)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_02_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_device(1)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_03_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_device(2)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_04_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_device(3)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_05_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_device(4)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_06_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(0)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_07_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(1)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_08_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(2)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_09_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(3)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_10_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(4)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_11_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(5)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_12_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(6)
        
    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_13_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(7)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_14_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(8)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_15_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(9)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C64746472")    
    def test_16_hpx_rebranding_C64746472(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746472
        """ 
        self.fc.select_device()
        self.__sign_in_HPX("shhpxtest008@gmx.com", "hpsa@rocks_335")
        self.__back_to_device_page()
        self.__verify_secondary_device(10)

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

    def __verify_device(self, index):
        self.fc.select_device(index)
        sn  = self.fc.fd["devices_support_pc_mfe"].get_sn()
        assert sn in [
            "8CG7200VNY", "4CE444B50B", "TH437CY0CH", "5CG14593SS", "5CD2167ZJF", 
            "CN463AP059", "9CP13740NT", "5CG135Z0QJ", "PHA91106GW", "2LTEWL", 
            "3CB0320023", "5CD116K82S", "8CC102Z1BZ", "5CD030KTTW", "214603463", 
            "EE6PWG",     "CZ72301111"]
    
    def __verify_secondary_device(self, index):
        self.__select_secondary_device(index)
        sn  = self.fc.fd["devices_support_pc_mfe"].get_sn()
        assert sn in [
            "8CG7200VNY", "4CE444B50B", "TH437CY0CH", "5CG14593SS", "5CD2167ZJF", 
            "CN463AP059", "9CP13740NT", "5CG135Z0QJ", "PHA91106GW", "2LTEWL", 
            "3CB0320023", "5CD116K82S", "8CC102Z1BZ", "5CD030KTTW", "214603463", 
            "EE6PWG",     "CZ72301111"]

    def __select_device(self, index=1):
        self.fc.fd["devicesMFE"].click_device_card_by_index(index)

    def __select_secondary_device(self, index=1):
        self.fc.fd["devicesMFE"].click_secondary_device_card_by_index(index)

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

    def __back_to_device_page(self):
        self.fc.fd["devicesMFE"].click_back_button_rebranding()

    def __sign_in_HPX(self, username, password, sign_in_from_profile=False):
         self.fc.sign_in(username, password, self.web_driver, sign_in_from_profile=sign_in_from_profile)