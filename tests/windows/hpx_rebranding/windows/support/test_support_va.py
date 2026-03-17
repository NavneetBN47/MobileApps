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
class Test_Suite_VA(object):
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
    @pytest.mark.testrail("S57581.C59373358")
    def test_01_hpx_rebranding_C59373358(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59373358
        """ 
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_endsession_btn()
        self.fc.fd["devices_support_pc_mfe"].click_keep_on_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")
        self.fc.fd["devices_support_pc_mfe"].send_keys("webchat_input", "PC")
        self.fc.fd["devices_support_pc_mfe"].click_send_btn()
        self.fc.fd["devices_support_pc_mfe"].click_endsession_btn()
        self.fc.fd["devices_support_pc_mfe"].click_close_btn()

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52215070")  
    def test_02_hpx_rebranding_C52215070(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52215070
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")
        self.fc.fd["devices_support_pc_mfe"].click_feedback_link()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("We appreciate your feedback!") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52216156")          
    def test_03_hpx_rebranding_C52216156(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52216156
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")    
        self.fc.fd["devices_support_pc_mfe"].click_startover_link()  
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("Would you like to start over?") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52216157")  
    def test_04_hpx_rebranding_C52216157(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52216157
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")    
        self.fc.fd["devices_support_pc_mfe"].click_privacy_link()
        self.__verify_redirect_link("privacy_link", "https://www.hp.com/", "privacy/privacy-central.html", False)

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52213605")  
    def test_05_hpx_rebranding_C52213605(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52213605
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()    
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("PC")    
        self.fc.fd["devices_support_pc_mfe"].click_va_message("PC")
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Performance")    
        self.fc.fd["devices_support_pc_mfe"].click_va_message("Performance")
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("I can help you improve performance of your computer.")
        self.fc.fd["devices_support_pc_mfe"].click_va_message("Yes")
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("HP PCs - Updating drivers using Windows Update (Windows 11, 10)")
        assert "https://support.hp.com/" in self.fc.fd["devices_support_pc_mfe"].get_va_message("HP PCs - Updating drivers using Windows Update (Windows 11, 10)")
        # self.fc.fd["devices_support_pc_mfe"].click_va_message("HP PCs - Updating drivers using Windows Update (Windows 11, 10)")
        # https://support.hp.com/document/ish_2850716-2380434-16
        # self.__verify_redirect_link("HP_Support", "https://support.hp.com/", "https://support.hp.com/", False) 

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52215051")  
    def test_06_hpx_rebranding_C52215051(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52215051
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()   
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")
        self.fc.fd["devices_support_pc_mfe"].send_keys("webchat_input", "sound issue")
        self.fc.fd["devices_support_pc_mfe"].click_send_btn()  
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("I can help you with sound issues.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52213603")  
    def test_07_hpx_rebranding_C52213603(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52213603
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_endsession_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("Are you sure?") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("Are you sure you want to close your Virtual Assistant session? You will need to start a new session if you still need help.") == True
        self.fc.fd["devices_support_pc_mfe"].click_keep_on_btn()
        self.fc.fd["devices_support_pc_mfe"].click_endsession_btn()
        self.fc.fd["devices_support_pc_mfe"].click_close_btn()

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C42891136")  
    def test_08_hpx_rebranding_C42891136(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/42891136
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with your") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("I can help with your HP ProBook 445 14inch G9 Notebook PC.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C52218787")  
    def test_09_hpx_rebranding_C52218787(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52218787
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_start_virtual_assist_btn()
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("\"Hi! I'm HP's Virtual Assistant.\"") == True 
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with your") == True 

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

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()   
        self.fc.fd["devices_support_pc_mfe"].click_otherspc_btn()  

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

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)      

    def __verify_redirect_link(self, web_page, url_contains, url_expect, full_match=True):
        webpage = web_page
        self.web_driver.wait_for_new_window(timeout=20)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        self.web_driver.close_window(webpage)
        if full_match:
            assert current_url == url_expect
        else:
            assert url_expect in current_url
    
    #http://web-proxy.sgp.hp.com:8080
    def __set_proxy_on_remote_windows(self, http_proxy, https_proxy=None, bypass_list=None):
        https_proxy = https_proxy or http_proxy
        proxy_string = f"http={http_proxy};https={https_proxy}"
        # WinHTTP
        cmd1 = f'netsh winhttp set proxy proxy-server="{proxy_string}"'
        self.driver.ssh.send_command(cmd1, timeout=30)
        self.driver.ssh.send_command(
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f',
            timeout=30
        )
        self.driver.ssh.send_command(
            f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyServer /t REG_SZ /d "{http_proxy}" /f',
            timeout=30
        )
        if bypass_list:
            self.driver.ssh.send_command(
                f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyOverride /t REG_SZ /d "{bypass_list}" /f',
                timeout=30
            )
        print("Remote system and WinINET proxy set successfully.")
        return True

