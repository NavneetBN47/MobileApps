import time
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.support_dashboard.support_flow_container import SupportFlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from selenium.webdriver.common.keys import Keys
import pytest

pytest.app_info = "HPX"
class Test_Suite_Speak(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)  
        cls.stack = request.config.getoption("--stack")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)    
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]

        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.hpid = cls.fc.fd["hpid"]    
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.devices = cls.fc.fd["devices"]
        cls.home = cls.fc.fd["home"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "speak.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31866697")  
    def test_01_Set_to_unsupported_regions_and_languages(self): 
        """
        verify 'Speak to an agent' option is not shown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31866697
        """
        self.fc.initial_simulate_file(self.file_path, "C31866697", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31866697"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("GM")
        assert self.support_device.verify_speak_to_agent() is False

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31909678")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_02_Click_Speak_to_an_agent_option(self): 
        """
        verify the display of profile name and Email are correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31909678
        """
        self.fc.initial_simulate_file(self.file_path, "C31909678", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31909678"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31871254")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_03_Click_Speak_to_an_agent_option(self): 
        """
        verify the function of Privacy Agreement check box is proper

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31871254
        """
        self.fc.initial_simulate_file(self.file_path, "C31871254", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31871254"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.is_privacy_status_selected() == "0"
            self.support_device.click_privacy_checkbox()
            assert self.support_device.is_privacy_status_selected() == "1"
            self.support_device.click_privacy_checkbox()
            assert self.support_device.is_privacy_status_selected() == "0"
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31871300")  
    def test_04_Click_Speak_to_an_agent_option(self): 
        """
        verify the function of Cancel button is proper

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31871300
        """
        self.fc.initial_simulate_file(self.file_path, "C31871300", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31871300"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.edit_problem("auto test")
            self.support_device.click_case_cancel_button()
            self.support_device.click_speak_to_agent()
            assert self.support_device.get_problem_value() == "Provide a short description of your problem"
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32085865") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_05_Click_Speak_to_an_agent_option(self):
        """
        Verify a message will popup if user haven't opted in

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32085865  
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C32085865", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(1)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32085865"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        time.sleep(2)
        self.support_device.click_speak_to_agent()
        self.support_device.click_no_button()
        self.support_device.click_speak_to_agent()
        self.support_device.click_yes_button()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32595946")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_06_without_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595946
        """
        self.fc.initial_simulate_file(self.file_path, "C32595946", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32595946"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        self.support_device.click_no_button()
        self.support_device.click_speak_to_agent()
        self.support_device.click_yes_button()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33443483")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_07_without_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443483
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        time.sleep(3)
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32085865") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_08_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32085865
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        self.support_device.click_no_button()
        self.support_device.click_speak_to_agent()
        self.support_device.click_yes_button()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33443485") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_09_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443485
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        time.sleep(3)
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["production"]) 
    @pytest.mark.testrail("S57581.C32595950") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_10_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595950
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        self.fc.click_dialog_close_btn(self.web_driver)
        self.support_device.click_speak_to_agent()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33443087") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_11_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443087
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.navigation_panel.verify_welcome_module_show()
        self.navigation_panel.navigate_to_welcome()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.home.click_support_control_card()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High", "BVT"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33443087") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_12_sign_in_from_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443264       
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33443429") 
    def test_13_sign_in_PC_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443429
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.click_pc_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.devices.click_support_btn()
        time.sleep(10)
        # self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else: 
            self.support_device.click_close_btn()    

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32318628") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_14_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32318628
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_speak_to_agent()
        assert self.support_device.verify_add_device_popup_display() is False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33642095") 
    @pytest.mark.exclude_platform(["grogu"])
    def test_15_click_speak_to_an_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33642095
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
            time.sleep(5)
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33642530") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_16_close_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33642530
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "hpx_login"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            time.sleep(3)
            self.web_driver.close_window(self.web_driver.current_window)   
        else:
            self.support_device.click_close_btn()
        time.sleep(2)
        self.support_device.click_speak_to_agent()
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33642738") 
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_17_close_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33642738
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.navigation_panel.select_my_hp_account_btn()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "hpx_login"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            time.sleep(3)
            self.web_driver.close_window(self.web_driver.current_window)   
        else:
            self.support_device.click_close_btn()
        time.sleep(2)
        self.support_device.click_speak_to_agent()
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie_NA"]) 
    @pytest.mark.testrail("S57581.C33698715") 
    def test_18_hpone_no_opt_in_windows_popup(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33698715
        """
        self.fc.initial_simulate_file(self.file_path, "C33698715", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.navigation_panel.navigate_to_settings()
        self.settings.click_privacy_tab()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_no_button()
        self.settings.click_done_button()
        self.fc.navigate_to_support()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33698715"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32595951") 
    def test_19_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595951
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        assert self.support_device.verify_add_device_popup_display() is not False
        self.support_device.click_no_button()
        self.support_device.click_chat_with_agent()
        assert self.support_device.verify_add_device_popup_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33443488")   
    def test_20_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443488
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        assert self.support_device.verify_add_device_popup_display() is not False
        self.support_device.click_no_button()
        self.support_device.click_chat_with_agent()
        assert self.support_device.verify_add_device_popup_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33443487")      
    def test_21_support_consent_is_no(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443487
        """
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        self.support_device.click_yes_button()
        self.fc.sign_in("hpxtest003@gmail.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        assert self.support_device.verify_add_device_popup_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33443494")    
    def test_22_support_consent_is_no(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443494
        """
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        self.support_device.click_yes_button()
        assert self.support_device.verify_add_device_popup_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33443492")   
    def test_23_support_consent_is_yes(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443492
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        self.fc.sign_in("hpxtest003@gmail.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)
        assert self.support_device.verify_add_device_popup_display() is not False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33443503")       
    def test_24_support_consent_is_yes(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33443503
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_speak_to_agent()
        assert self.support_device.verify_add_device_popup_display() is not False   

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31867521")   
    def test_25_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31867521
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/case_create/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            
            self.support_device.click_category_cbx()

            for n in range(0, 8):
                assert self.support_device.get_catetory(n) == common["typeDropdown"]["type" + str(n + 1)]

            self.support_device.click_category_opt(3)
            self.support_device.click_category_cbx()
            assert self.support_device.verify_category_selected(3) == "true"

            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.click_case_cancel_button()
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31867531")   
    def test_26_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31867531
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/case_create/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['common']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            
            assert self.support_device.get_problem_helptext() == common["problemInput"]["text"]
            
            self.support_device.edit_problem("auto test")

            self.support_device.enter_keys_to_problem_text(Keys.ENTER)

            for _ in range(10):
                self.support_device.enter_keys_to_problem_text(Keys.BACKSPACE)       
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31871255")   
    def test_27_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31871255
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.verify_get_phone_number_btn_state() == "false"
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_get_phone_number_btn_state() == "true"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32595954") 
    def test_28_click_privacy_terms_and_conditions(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595954
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_pravicy_link()
            webpage = "PRIVACY_LINK"
            self.web_driver.wait_for_new_window(timeout=20)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)
            self.web_driver.wait_url_contains("https://www.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://www.hp.com/us-en/privacy/privacy.html"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32595955") 
    def test_29_click_cancel_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595955
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():

            self.support_device.click_case_cancel_button()
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33526000") 
    def test_30_click_get_phone_number_button(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33526000
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_get_phone_number_btn_state() == "true"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31911281")        
    def test_31_click_using_keyboard(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31911281
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        get_phone_call = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['speakToAgent']['getPhoneNumber']
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.enter_keys_to_speak_to_agent(Keys.ENTER)
      
        if not self.support_device.verify_outside_hours_popup_display():
            assert self.support_device.get_phone_number_btn_value() == get_phone_call
        else:
            self.support_device.click_close_btn()  

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C31866689")   
    def test_32_click_speak_to_agent(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31866689
        """
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"], self.hpid_username, self.hpid_password)
        self.support_device.click_speak_to_agent()

        if self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_close_btn()        
    
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)

    def __select_device_card(self, serial_number, user_name="hpxtest003@gmail.com", pass_word="hpsa@rocks_335"):
        self.__launch_HPX()
        time.sleep(3)
        self.fc.sign_in(user_name, pass_word, self.web_driver)
        time.sleep(10)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)
        self.fc.select_country("US")
    
    # @pytest.mark.require_priority(["Low"])      
    # @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    # @pytest.mark.testrail("S57581.C32595951")     
    # def test_19_click_speak_to_agent(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/32595951
    #     """
    #     window_name = "main"
    #     self.web_fc = SupportFlowContainer(self.web_driver, window_name)
    #     self.web_fc.navigate(self.stack)
    #     self.web_fc.click_sign_in_btn()
    #     time.sleep(3)
    #     print('current url={}'.format(self.web_driver.get_current_url()))
    #     self.web_fc.login("hpxtest001@gmail.com", self.hpid_password)
    #     self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
    #     self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.navigate_to_support()
    #     """
    #     To do
    #     """

    # def test_20_click_test(self):
    #     self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack)
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.sign_out(self.web_driver)
    #     self.fc.navigate_to_support()
    #     self.support_home.click_visit_on_line_link()
    #     webpage = "visit_link"
    #     time.sleep(3)
    #     window_name = self.web_driver.add_window(webpage)
    #     self.web_driver.switch_window(webpage)  
    #     self.web_fc = SupportFlowContainer(self.web_driver, window_name)   
    #     self.web_fc.click_sign_in_btn()
    #     time.sleep(3)
    #     print('current url={}'.format(self.web_driver.get_current_url()))
    #     self.web_fc.login("hpxtest001@gmail.com", self.hpid_password)
