import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_HPOne(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.support_account = cls.fc.fd["support_account"]
        cls.support_onedrive = cls.fc.fd["support_onedrive"]
        cls.support_va = cls.fc.fd["support_va"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "hp_one.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)    

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_01_click_change_bill_infomation(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655923
        """
        self.__click_account_card()

        self.support_account.click_change_bill_info_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_02_click_credit_denail(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655939
        """
        self.__click_account_card()
        
        self.support_account.click_denial_credit_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    def test_03_click_understanding_my_bill_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655940
        """
        self.__click_account_card()

        self.support_account.click_understanding_my_bill_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])         
    def test_04_click_change_email_address_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655941
        """
        self.__click_account_card()

        self.support_account.click_change_email_address_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])    
    def test_05_click_change_shipping_address_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655942
        """
        self.__click_account_card()

        self.support_account.click_change_shipping_address_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])        
    def test_06_click_cancel_my_account_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655943
        """
        self.__click_account_card()
        
        self.support_account.click_cancel_my_account_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_07_click_account_error_message_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655975
        """
        self.__click_account_card()

        self.support_account.click_account_error_message_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_08_click_login_issues_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655976
        """
        self.__click_account_card()

        self.support_account.click_login_issues_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    def test_09_click_subscription_information_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655977
        """
        self.__click_account_card()

        self.support_account.click_subscription_information_link()

        self.__verify_link("https://support.hp.com/")

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    def test_10_click_contact_hp_support_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655978
        """
        self.__click_account_card()

        self.support_account.click_contact_hp_support_link()

        product_number_wmi = self.wmi.get_product_number()
        product_number_UI = self.support_device.get_product_number_value()
        assert product_number_wmi == product_number_UI

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    def test_11_click_start_va_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35655979
        """
        self.__click_account_card()
        
        self.support_account.click_start_va_btn()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_12_click_start_va_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35656010
        """
        self.__click_MS_cloud_storage()
        
        self.support_onedrive.click_using_MS_cloud_storage_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_13_click_active_MS_cloud_storage_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35656007
        """
        self.__click_MS_cloud_storage()

        self.support_onedrive.click_active_MS_cloud_storage_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_14_click_install_MS_cloud_storage_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35656008
        """
        self.__click_MS_cloud_storage()

        self.support_onedrive.click_install_MS_cloud_storage_link()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"])
    def test_15_click_M365_account_link(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35656009
        """
        self.__click_MS_cloud_storage()

        self.support_onedrive.click_M365_account_link()

        self.__verify_link("https://setup.office.com/")

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    def test_16_click_network_check(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35699829
        """
        self.__select_device_card(self.wmi.get_serial_number())
        self.support_device.click_network_check_btn()
        self.__verify_process("HPNetworkCheck.exe")     
        
    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    def test_17_click_fix_audio_issues(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35699878
        """
        self.__select_device_card(self.wmi.get_serial_number())
        self.support_device.click_fix_audio_issues_btn()
        self.__verify_process("HPAudioCheck.exe")

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    def test_18_click_check_reporting_system(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35699879
        """
        self.__select_device_card(self.wmi.get_serial_number())
        self.support_device.click_check_os_btn()
        self.__verify_process("HPOSCheck.exe")

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C33646038")  
    def test_19_click_support_user_without_sign_in(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33646038
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.navigation_panel.navigate_to_support()

        assert self.__verify_login_page() is not False

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C35492615")  
    def test_21_press_hotkey(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35492615
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.launch_hotkey("myhp://support/device")

        assert self.__verify_login_page() is not False

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C35492619")  
    def test_22_click_support_option(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35492619
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.click_pc_support()
        assert self.__verify_login_page() is not False

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    def test_23_click_MS_cloud_storage(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35699619
        """
        self.__click_MS_cloud_storage()

        self.__verify_virtual_agent_display()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33510012") 
    def test_24_click_chat_with_agent_options(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510012
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US")  
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn()    

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33510013") 
    def test_25_sign_in_from_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510013
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver)
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US")
        self.support_device.verify_speak_to_agent()
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33510014") 
    def test_26_sign_in_from_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510014
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        self.support_device.verify_speak_to_agent()
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()   

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33510015") 
    def test_27_sign_in_from_pcdevice_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510015
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.click_pc_support()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        self.support_device.verify_speak_to_agent()
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()   

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33529211") 
    def test_28_support_consent_is_yes(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33529211
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        chat_with_an_agent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        assert self.support_device.verify_chat_with_agent_display() is not False
        self.support_device.click_chat_with_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_support_model_sub_title() == chat_with_an_agent
        else: 
            self.support_device.click_close_btn()  

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33526200") 
    def test_29_device_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33526200
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        title = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['title']
        description = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['chatWithAgent']['description']
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        self.support_device.verify_chat_with_agent_display()
        assert title in self.support_device.get_chat_with_agent_title()
        assert description in self.support_device.get_chat_with_agent_title()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33698715") 
    def test_30_no_optinwindow_popup(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33698715
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        availableNow = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']['availableNow']
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        self.support_device.verify_speak_to_agent()
        assert availableNow in self.support_device.get_speak_to_agent_title()    

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33510214") 
    def test_31_goto_liveassistant_section(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33510214
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        availableNow = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']['availableNow']
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("US") 
        self.support_device.verify_speak_to_agent()
        assert availableNow in self.support_device.get_speak_to_agent_title()    

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35529431") 
    def test_32_click_getphonenumber_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35529431
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver)
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.fc.select_country("US") 
        self.__verify_phonecase_done()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35534249") 
    def test_33_click_getphonenumber_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35534249
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver)
        self.support_home.verify_device_display("WBW7S6GHCP")
        self.support_home.select_device_card("WBW7S6GHCP") 
        self.fc.select_country("US") 
        self.__verify_phonecase_done()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35539607") 
    def test_34_gotoliveassistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35539607
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        speakToAgent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']["title"]
        self.__launch_HPX()
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.support_device.verify_speak_to_agent()
        assert speakToAgent in self.support_device.get_speak_to_agent_title()    
        assert "1-866-204-8618" in self.support_device.get_speak_to_agent_title()
        assert "7 days a week 24 hours a day" in self.support_device.get_speak_to_agent_title()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35539854") 
    def test_35_gotoliveassistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35539854
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        speakToAgent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']["title"]
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.support_device.verify_speak_to_agent()
        assert speakToAgent in self.support_device.get_speak_to_agent_title()    
        assert "1-866-204-8618" in self.support_device.get_speak_to_agent_title()
        assert "7 days a week 24 hours a day" in self.support_device.get_speak_to_agent_title()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C36115087") 
    def test_36_gotoliveassistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/36115087
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        speakToAgent = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']["title"]
        self.__launch_HPX()
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.support_device.verify_speak_to_agent()
        assert speakToAgent in self.support_device.get_speak_to_agent_title()    
        assert "1-866-204-8618" in self.support_device.get_speak_to_agent_title()
        assert "7 days a week 24 hours a day" in self.support_device.get_speak_to_agent_title()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C33526306") 
    def test_37_click_getphonenumber_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33526306
        """
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.__verify_phonecase_done() 

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C33640888") 
    def test_38_only_usermanualsandguides(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33640888
        """
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.support_device.verify_resources_card_display()
        resources_cards = self.support_device.get_resources_cards()
        assert "User manuals and guides Review product manuals and user guides" in resources_cards
        assert "HP community Find answers in our searchable online forum" in resources_cards
        assert resources_cards.count == 2

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C33640889") 
    def test_39_all_the_support_resourcelinks_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33640889
        """
        self.__launch_HPX()
        self.fc.sign_in("boffocresefro-5213@yopmail.com", "P@ssw0rd", self.web_driver, user_icon_click=False)
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417") 
        self.fc.select_country("US")
        self.support_device.verify_resources_card_display()
        self.support_device.click_user_manuals_guide()
        self.__verify_redirect_link("UserManualAndGuide", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/hp-dragonfly-pro-one/model/2101746239")
        self.support_device.click_HP_support_forum()
        self.__verify_redirect_link("HPCommunity", "https://h30434.www3.hp.com", "https://h30434.www3.hp.com/t5/Notebooks/ct-p/Notebook")

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C32331706") 
    def test_40_click_device_card_with_VA_conversation(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32331706
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        self.support_home.click_account_card()
        self.support_account.click_start_va_btn()
        self.__verify_virtual_agent_display()
        self.support_va.click_minimize_button()
        self.support_home.verify_device_display("CND9091417")
        self.support_home.select_device_card("CND9091417")
        self.support_va.click_close_cancel_button()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35347996")     
    def test_41_click_lanuch_account_support_card(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35347996
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        accountSupport = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']["accountSupport"]
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        self.support_home.click_account_card()
        assert self.support_account.get_support_account_title() == accountSupport

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C35607315")        
    def test_42_click_launch_account_support_card(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35607315
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        accountSupport = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']["accountSupport"]
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        self.support_home.click_account_card()
        assert self.support_account.get_support_account_title() == accountSupport

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"])
    @pytest.mark.testrail("S57581.C36759112")    
    def test_43_check_no_guided_troubleshooting_options(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/36759112
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        accountSupport = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']["accountSupport"]
        self.__launch_HPX()
        self.support_home.click_account_card()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        assert self.support_account.get_support_account_title() == accountSupport

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C36834997")    
    def test_44_hide_chat_with_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/36834997
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.__sign_in_hpone_account()
        self.fc.select_country("US")  
        assert self.support_device.verify_chat_with_agent_display() is not False
        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        assert self.support_device.verify_chat_with_agent_display() is False
        self.__sign_in_hpone_account()
        self.fc.select_country("US")
        assert self.support_device.verify_chat_with_agent_display() is not False

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"])
    @pytest.mark.testrail("S57581.C33640886")    
    def test_45_socialmessagingchannels(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33640886
        """
        self.__sign_in_hpone_account()
        self.fc.select_country("ID")
        self.support_device.click_whatsapp()
        self.__verify_redirect_link("WhatsApp", "whatsapp.com", "whatsapp.com")
        # self.fc.select_country("TR")
        # self.support_device.click_fbmessenger()
        # self.__verify_redirect_link("Messenger", "https://www.messenger.com/", "https://www.messenger.com/")
        self.fc.select_country("CN")
        self.support_device.click_wechat()
        self.__verify_redirect_link("WeChat", "https://www.hp.com/", "https://www.hp.com/cn-zh/contact-hp/webchat-support.html?src=csptwechat")
        self.fc.select_country("JP")
        self.support_device.click_line()
        self.__verify_redirect_link("Line", "https://support.hp.com/", "https://support.hp.com/jp-ja/document/")
        self.fc.select_country("KR")
        self.support_device.click_kakaotalk()
        self.__verify_redirect_link("KaKaoTalk", "https://support.hp.com/", "https://support.hp.com/kr-ko/document/")
        self.fc.select_country("VN")
        self.support_device.click_zalo()
        self.__verify_redirect_link("Zalo", "https://zalo.me", "https://zalo.me")         

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_device_card(self, sn):
        self.__sign_in_HPX()
        time.sleep(10)
        self.support_home.verify_device_display(sn)
        self.support_home.select_device_card(sn)     

    def __verify_link(self, url):
        webpage = "HP_ONE"
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url, timeout=30)
        current_url = self.web_driver.get_current_url()
        assert url in current_url

    def __verify_redirect_link(self, webpage, url_contains, url_current):
        webpage = webpage
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        assert url_current in current_url

    def __verify_phonecase_done(self):
        self.support_device.verify_speak_to_agent()
        self.support_device.click_speak_to_agent()
        self.support_device.click_category_cbx()
        self.support_device.click_category_opt(3)
        self.support_device.edit_problem("auto test")
        self.support_device.click_privacy_checkbox()
        assert self.support_device.verify_get_phone_number_btn_state() == "true"
        self.support_device.click_get_phone_number()
        assert self.support_device.verify_phonecasedonebtn_show() is not False

    def __verify_virtual_agent_display(self):
        assert self.support_va.get_va_page_title() == "myHP -Virtual Assistant"

    def __verify_process(self, process_name):
        if self.process_util.check_process_running(process_name):
            assert self.process_util.check_process_running(process_name) is True
            self.process_util.kill_process(process_name)

    def __click_MS_cloud_storage(self):
        self.__sign_in_HPX()
        self.support_home.click_onedrive_card()

    def __click_account_card(self):
        self.__sign_in_HPX()
        self.support_home.click_account_card()

    def __sign_in_HPX(self):
        self.__launch_HPX()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)

    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()

    def __verify_login_page(self):
        return self.fc.verify_hp_id_sign_in(self.web_driver)
    
    def __sign_in_hpone_account(self, username="boffocresefro-5213@yopmail.com", password="P@ssw0rd"):
        self.__launch_HPX()
        self.fc.sign_in(username, password, self.web_driver, user_icon_click=True)
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
