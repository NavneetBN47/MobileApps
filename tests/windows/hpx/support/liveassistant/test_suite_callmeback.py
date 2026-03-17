import time
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_CallMeBack(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session

        cls.stack = request.config.getoption("--stack")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)    
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]

        cls.fc = FlowContainer(cls.driver)  
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.hpid = cls.fc.fd["hpid"]  
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.settings = cls.fc.fd["settings"]
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "call_me_back.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C31860773")  
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_01_Verify_the_Call_Me_Back(self):
        """
        verify before redirector URL and after redirector URL

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31860773
        """
        self.fc.initial_simulate_file(self.file_path, "C31860773", self.app_env,  self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860773"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        time.sleep(5)
        self.support_device.click_country_list()
        self.support_device.select_country("199")
        self.support_device.click_call_me_back()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            if self.app_env == "itg":
                self.web_driver.wait_url_contains("https://uat.support.hp.com", timeout=30)
            else:
                self.web_driver.wait_url_contains("https://support.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()

            if self.app_env == "itg":
                assert "https://uat.support.hp.com/jp-ja/contact/product/" + "hp-stream-11-laptop-pc-11-ak2000" in current_url
            else:
                assert "https://support.hp.com/jp-ja/contact/product/" + 'hp-stream-11-laptop-pc-11-ak2000' in current_url           
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie_NA"]) 
    @pytest.mark.testrail("S57581.C33703372")  
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_02_click_Call_Me_Back(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33703372
        """
        self.fc.initial_simulate_file(self.file_path, "C31860773", self.app_env,  self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860773"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_country_list()
        self.support_device.select_country("199")
        self.support_device.click_call_me_back()
        if not self.support_device.verify_outside_hours_popup_display():
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
            time.sleep(5)
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            if self.app_env == "itg":
                self.web_driver.wait_url_contains("https://uat.support.hp.com", timeout=30)
            else:
                self.web_driver.wait_url_contains("https://support.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()
            if self.app_env == "itg":
                assert "https://uat.support.hp.com/jp-ja" in current_url
            else:
                assert "https://support.hp.com/jp-ja" in current_url           
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie_NA"]) 
    @pytest.mark.testrail("S57581.C33726604")  
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_03_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33726604
        """
        self.fc.initial_simulate_file(self.file_path, "C31860773", self.app_env,  self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860773"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_country_list()
        self.support_device.select_country("199")
        self.support_device.click_call_me_back()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            time.sleep(3)
            self.web_driver.close_window(self.web_driver.current_window)   
        else:
            self.support_device.click_close_btn()
        time.sleep(2)
        self.support_device.click_call_me_back()
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
            time.sleep(5)
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            if self.app_env == "itg":
                self.web_driver.wait_url_contains("https://uat.support.hp.com", timeout=30)
            else:
                self.web_driver.wait_url_contains("https://support.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()
            if self.app_env == "itg":
                assert "https://uat.support.hp.com/jp-ja" in current_url
            else:
                assert "https://support.hp.com/jp-ja" in current_url           
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["pie_NA"]) 
    @pytest.mark.testrail("S57581.C33703372")  
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_04_sign_in_website(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33726605
        """
        self.fc.initial_simulate_file(self.file_path, "C31860773", self.app_env,  self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860773"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_country_list()
        self.support_device.select_country("199")
        self.navigation_panel.select_my_hp_account_btn()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            time.sleep(3)
            self.web_driver.close_window(self.web_driver.current_window)   
        else:
            self.support_device.click_close_btn()
        time.sleep(2)
        self.support_device.click_call_me_back()
        time.sleep(3)
        if not self.support_device.verify_outside_hours_popup_display():
            self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
            time.sleep(5)
            webpage = "CallMeBack"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            if self.app_env == "itg":
                self.web_driver.wait_url_contains("https://uat.support.hp.com", timeout=30)
            else:
                self.web_driver.wait_url_contains("https://support.hp.com", timeout=30)
            current_url = self.web_driver.get_current_url()
            if self.app_env == "itg":
                assert "https://uat.support.hp.com/jp-ja" in current_url
            else:
                assert "https://support.hp.com/jp-ja" in current_url           
        else:
            self.support_device.click_close_btn()
