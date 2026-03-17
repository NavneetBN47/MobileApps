import time
import MobileApps.resources.const.windows.const as w_const
from datetime import datetime
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.web.virtual_agent.va_flow_container import VAFlowContainer
from selenium.webdriver.common.keys import Keys
import logging
import pytest
import re
from bs4 import BeautifulSoup

pytest.app_info = "HPX"
class Test_Suite_Support_Home(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup 
        cls.wmi = WmiUtilities(cls.driver.ssh)     
        cls.web_driver = utility_web_session      

        cls.fc = FlowContainer(cls.driver)  
        cls.logger=logging.getLogger()
        cls.hpid = cls.fc.fd["hpid"]   
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.home = cls.fc.fd["home"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.support_va = cls.fc.fd["support_va"]
        cls.support_account = cls.fc.fd["support_account"]
        cls.support_onedrive = cls.fc.fd["support_onedrive"]
        cls.support_connectivity = cls.fc.fd["support_connectivity"]
        cls.settings = cls.fc.fd["settings"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)   
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "support_home.json")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])   
    @pytest.mark.testrail("S57581.C32564743")    
    def test_01_Click_the_Support_from_navigation_menu(self):
        """
        verify the device information in the device card on the  Support home page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32564743
        """
        self.fc.restart_app()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        product_number_wmi = self.wmi.get_product_number()
        product_number_UI = self.support_device.get_product_number_value()
        assert product_number_wmi == product_number_UI
        serial_number_wmi = self.wmi.get_serial_number()
        serial_number_UI = self.support_device.get_serial_number_value()
        assert serial_number_wmi == serial_number_UI

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32048141")    
    def test_02_Transactional_Open_the_Support_home_page(self): 
        """
        verify sign in and sign out

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32048141
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(2)
        self.navigation_panel.verify_my_hp_sign_in()
        self.navigation_panel.select_my_hp_account_btn()
        self.navigation_panel.select_my_hp_sign_out_btn()

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C39537855")    
    def test_03_Switch_from_other_page_to_Support_Home_page(self):
        """
        verify user can switch to Support Home page
    
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/39537855
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.fc.navigate_to_settings()
        self.fc.navigate_to_support()

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32293269")    
    def test_04_Transactional_Click_the_Device_card(self):
        """
        verify it will turn to device details page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32293269
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.wmi.get_serial_number())

        assert self.support_device.get_nick_name_value() == "My PC"

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31899298")    
    def test_05_Click_the_close_button(self):
        """
        verify Support Home page should be closed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31899298
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.fc.navigate_to_support()
        self.navigation_panel.click_close_btn()

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31868423")       
    def test_06_HPOne_Click_all_clickable_elements(self): 
        """
        verify they should be launched without any problem

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31868423
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(10)
        self.fc.restart_app()     
        self.fc.navigate_to_support()  
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(10)
        self.support_home.click_account_card()
        assert self.support_account.get_start_va_btn_title() == "Start Virtual Assistant"
        self.support_account.click_close_btn()
        self.support_home.click_onedrive_card()
        assert self.support_onedrive.get_start_va_btn_title() == "Start Virtual Assistant"

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31866691")    
    def test_07_HPOne_Click_the_Device_card_without_sign_in(self):
        """
        verify the Sign in page should pop up

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31866691
        """
        self.fc.initial_simulate_file(self.file_path, "C31866691", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31866691"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.navigation_panel.verify_my_hp_sign_in()
        assert self.support_device.get_product_name_value() == "CUIYOU4"

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32330579")    
    def test_08_HPOne_Click_the_Cards_under_Guided_troubleshooting(self): 
        """
        verify the Sign in page should pop up

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32330579
        """
        self.fc.initial_simulate_file(self.file_path, "C32330579", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(10)
        self.fc.restart_app()
        self.fc.navigate_to_support()        
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(3)      
        self.fc.sign_out(self.web_driver)
        time.sleep(1)
        self.support_home.click_account_card()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        assert self.support_account.get_start_va_btn_title() == "Start Virtual Assistant"
        self.support_account.click_close_btn()
        self.navigation_panel.select_my_hp_account_btn()
        self.navigation_panel.select_my_hp_sign_out_btn()
        time.sleep(10)
        self.support_home.click_onedrive_card()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        assert self.support_onedrive.get_start_va_btn_title() == "Start Virtual Assistant"

    @pytest.mark.parametrize("country_code, region_code", [
        ("zh-CN", "45"),
        ("ja-JP", "81"),
        ("en-US", "244")
        # "ar-SA",
        # "bg-BG",
        # "ca-ES","cs-CZ",
        # "da-DK","de-DE",
        # "el-GR","en-GB","en-US","eu-ES","es-ES","es-MX","et-EE", 
        # "fi-FI","fr-CA","fr-FR",
        # "gl-ES",
        # "he-IL","hr-HR","hu-HU",
        # "id-ID","it-IT",
        # "ja-JP",
        # "ko-KR",
        # "lt-LT","lv-LV",
        # "nb-NO","nl-NL",
        # "pl-PL","pt-BR","pt-PT",
        # "ro-RO","ru-RU",
        # "sk-SK","sl-SI","sr-La",
        # "tn-rs",
        # "sv-SE",
        # "th-TH","tr-TR",
        # "uk-UA",
        # "zh-CN","zh-HK","zh-TW"
        ]
        )
    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31868417")    
    def test_09_Click_visit_your_online_dashboard_link(self, country_code, region_code): 
        """
        verify the link should turn to the Device web portals.

        https://hp-testrail.external.hp.com/index.php?/cases/view/31868417        
        """  
        self.fc.update_region(country_code.split('-')[1], region_code)
        self.fc.initial_simulate_file(self.file_path, "C31868417", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.support_home.click_visit_on_line_link()
        webpage = "VisitOnLine"
        time.sleep(3)
        self.web_driver.wait_for_new_window(timeout=15)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert "{}-{}".format(country_code.split('-')[1].lower(), country_code.split('-')[0].lower()) in current_url

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33343057")    
    def test_10_transacational_go_to_support_without_sign_in(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33343057
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(5)
        assert self.support_home.verify_refresh_btn_display() is False

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33349346")  
    def test_11_transactional_click_local_device(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33349346
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        local_pc_details = self.support_home.get_device_details(self.wmi.get_serial_number())

        assert "My PC" in local_pc_details
        assert self.wmi.get_product_number() in local_pc_details
        assert self.wmi.get_serial_number() in local_pc_details
        assert self.wmi.get_product_name() in local_pc_details

        self.support_home.select_device_card(self.wmi.get_serial_number())
        
        assert self.support_device.get_nick_name_value() == "My PC"

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "production"]) 
    @pytest.mark.testrail("S57581.C33349344")  
    def test_12_transactional_sign_in_account_less_than_two_machines(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33349344
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in("hpxtest002@gmail.com", "hpsa@rocks_335", self.web_driver)

        local_pc_details = self.support_home.get_device_details(self.wmi.get_serial_number())

        self.support_home.select_device_card(self.wmi.get_serial_number(), timeout=20)
        assert self.support_device.get_product_name_value() in local_pc_details
        assert self.support_device.get_product_number_value() in local_pc_details
        assert self.support_device.get_serial_number_value() in local_pc_details

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "production"]) 
    @pytest.mark.testrail("S57581.C33344158")  
    def test_13_transactional_sign_in_account_more_than_two_machines(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33344158
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        time.sleep(10)
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        assert self.support_home.verify_refresh_btn_display() is not False

        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        assert self.support_home.verify_refresh_btn_display() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33603544")
    def test_14_HPOne_Sign_in_on_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33603544
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        assert self.fc.verify_sign_in(self.web_driver) is not False
    
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33603545")
    def test_15_HPOne_Click_profile_on_Device_details_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33603545
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31868423"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)

    @pytest.mark.require_platform(["grogu"])
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie","stage", "production"]) 
    @pytest.mark.testrail("S57581.C33603546")
    def test_16_HPOne_Click_the_card_on_guide_troubleshooting(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33603546
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        time.sleep(10)
        self.fc.restart_app()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.click_account_card()
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        time.sleep(5)
        assert self.support_account.get_support_account_title() == "Account support"
        self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.click_onedrive_card()
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click=False)
        time.sleep(5)
        assert self.support_onedrive.get_MS_cloud_storage_title() == "MS cloud storage support"
        self.fc.sign_out(self.web_driver)

    @pytest.mark.require_platform(["grogu"]) 
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33344158")
    def test_17_HPOne_Click_the_Support_when_user_without_sign_in(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33646038
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()

        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False

    @pytest.mark.require_platform(["grogu"]) 
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33646042")
    def test_18_HPOne_Press_hotkey(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33646042
        """
        self.fc.initial_simulate_file(self.file_path, "C31868423", self.app_env, self.stack)
        self.fc.launch_myHP_hotkey()
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33603540")
    def test_19_Transactional_click_profile_on_support_home(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33603540
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()   
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33603542")
    def test_20_Transactional_click_profile_on_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33603542
        """
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33721260")
    def test_21_web_sign_in(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33721260
        """
        system_locale = self.fc.get_winsystemlocale().strip()
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/settingLocalization.json")[system_locale]["translation"]["Settings"]
        
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.navigation_panel.select_my_hp_account_btn()

        self.fc.navigate_to_support()
        
        assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not False
        
        self.navigation_panel.navigate_to_settings()

        assert self.settings.verify_settings_header() == lang_settings["navItem"]

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C35011494")   
    def test_22_external_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35011494
        """
        self.__launch_HPX()
        self.fc.click_pc_support()
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        diagnostics_tilte = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format(system_locale))['common']['diagnostics']
        assert self.support_device.get_diagnostic_title() == diagnostics_tilte
        # 
        # device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['supportHome']['deviceSupport']
        # hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['common']['hPOnePremiumDeviceSupport']

        # if not self.wmi.is_grogu():
        #     assert self.support_home.get_support_home_title() == device_support
        # else:
        #     assert self.support_home.get_support_home_title() == hp_one_device_support

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C35011493")  
    def test_23_external_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35011493
        """
        self.__launch_HPX()
        self.fc.click_support_control_card()
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('_')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith']
        hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['common']['hPOnePremiumDeviceSupport']

        if not self.wmi.is_grogu():
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        else:
            assert self.support_home.get_support_home_title() == hp_one_device_support

        

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32790549") 
    def test_24_click_back_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32790549
        """ 
        self.__select_device_card(self.wmi.get_serial_number())

        self.support_device.click_back_btn()

        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('_')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith']
        hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['common']['hPOnePremiumDeviceSupport']

        if not self.wmi.is_grogu():
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        else:
            assert self.support_home.get_support_home_title() == hp_one_device_support     

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35894753") 
    def test_25_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35894753
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__sign_in_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.double_click_serial_number()
        self.support_device.right_click_serial_number()  
        self.support_device.click_copy_menu_item()   
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "5CG02735RG"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card("MXL0362720")

        self.support_device.double_click_serial_number()
        self.support_device.right_click_serial_number()  
        self.support_device.click_copy_menu_item()    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "MXL0362720"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35895991") 
    def test_26_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35895991
        """  
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__sign_in_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.double_click_product_number()
        self.support_device.enter_keys_to_product_number(Keys.CONTROL + "c")     
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "158U3AA"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card("MXL0362720")

        self.support_device.double_click_product_number()
        self.support_device.enter_keys_to_product_number(Keys.CONTROL + "c")     
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "7HZ63UT"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35911676") 
    def test_27_selected_pn_or_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35911676
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__sign_in_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.double_click_product_number()  
        self.support_device.right_click_serial_number()

        assert self.support_device.verify_copy_menu_item() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35894954") 
    def test_28_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35894954
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__sign_in_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.double_click_serial_number()
        self.support_device.right_click_serial_number()  
        self.support_device.click_copy_menu_item()   
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "5CG02735RG"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card("MXL0362720")

        self.support_device.double_click_serial_number()
        self.support_device.right_click_serial_number()  
        self.support_device.click_copy_menu_item()    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "MXL0362720"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35911041") 
    def test_29_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35911041
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__sign_in_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.double_click_product_number()
        self.support_device.enter_keys_to_product_number(Keys.CONTROL + "c")     
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "158U3AA"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card("MXL0362720")

        self.support_device.double_click_product_number()
        self.support_device.enter_keys_to_product_number(Keys.CONTROL + "c")     
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in "7HZ63UT"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35893260")    
    def test_30_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35893260
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__launch_HPX()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_serial_number(sn_number)
        time.sleep(3)
        self.support_home.right_click_serial_number(sn_number)  
        self.support_home.click_copy_menu_item()   
        self.support_home.select_device_card(sn_number)
    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in sn_number
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35894951")   
    def test_31_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35894951
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        pn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["productNumberNoRegion"]
        self.__sign_in_HPX()
        
        self.support_home.select_product_number(sn_number)
        time.sleep(3)
        self.support_home.right_click_product_number(sn_number)  
        self.support_home.click_copy_menu_item()   
        self.support_home.select_device_card(sn_number)

        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in pn_number
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35894966")   
    def test_32_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35894966
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__launch_HPX()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_serial_number(sn_number)
        time.sleep(3)
        self.fc.press_ctrlkey('c')
        self.support_home.select_device_card(sn_number)
    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)

        if not self.support_device.verify_outside_hours_popup_display():
            
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in sn_number
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C35911040")      
    def test_33_copy_pn_and_sn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35911040
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        pn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["productNumberNoRegion"]
        self.__sign_in_HPX()

        time.sleep(3)
        self.support_home.select_product_number(sn_number)
        time.sleep(3)
        self.fc.press_ctrlkey('c')
        self.support_home.select_device_card(sn_number)
    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text() in pn_number
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 
    
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32796292")   
    def test_34_click_back_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32796292
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)

        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_minimize_button()

        self.support_device.click_back_btn()
        assert self.support_device.verify_warranty_details_popup_display() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32796293")   
    def test_35_click_back_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32796293
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(2)
        self.support_va.click_minimize_button()
        self.support_device.click_back_btn()
        self.support_va.click_close_confirm_button()
        assert self.support_device.verify_support_device_page() is True

        self.support_device.click_back_btn()
        self.support_va.click_close_cancel_button()
        assert self.support_home.verify_support_home_title() is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33488264")      
    def test_36_click_view_data_collected(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33488264
        """
        system_locale = self.fc.get_winsystemlocale().strip()
        language = "sr_Latn-RS" if system_locale == "sr-BA" else system_locale
        with open(ma_misc.get_abs_path("resources/test_data/hpsa/locale/view_data_collected/{}/HPSFCollectedData.html").format(language), "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml")
            title_tag = soup.find("title")
            header = title_tag.text.strip()
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        
        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(2)
        self.support_va.click_minimize_button()

        self.support_device.click_warranty_details_link()        
        self.support_device.click_view_data_collected_link()

        assert self.support_device.get_warranty_details_content_title() == header

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32319191")          
    def test_37_when_leave_support_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32319191
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(2)
        self.support_va.click_minimize_button()
        self.navigation_panel.navigate_to_settings()
        
        assert self.support_device.verify_warranty_details_popup_display() is True

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32312930")        
    def test_38_click_keep_session_on_close_session_popup(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32312930
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(3)
        self.support_va.click_minimize_button()
        self.navigation_panel.navigate_to_settings()
        self.support_va.click_close_confirm_button()      

        assert self.support_va.verify_va_desc_window() is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32319193")   
    def test_39_click_close_session_on_close_session_popup(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32319193
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(2)
        self.support_va.click_minimize_button()
        self.navigation_panel.navigate_to_settings()
        self.support_va.click_close_cancel_button()

        assert self.support_va.verify_va_desc_window() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32319193")       
    def test_40_input_some_questions(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31867599
        """
        self.__sign_in_HPX()
        
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_va()
        time.sleep(5)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        url = self.support_va.get_va_link()

        self.web_fc = VAFlowContainer(self.web_driver)
        self.web_fc.navigate(url)
        self.web_fc.fd["home"].input_issue("black screen")
        self.web_fc.fd["home"].click_send_btn() 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32319193")         
    def test_41_click_other_buttons_on_device_pages(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32319878
        """  
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country('US')
        time.sleep(5)
        self.support_device.click_va()
        time.sleep(3)
        self.support_va.click_start_VA()
        self.support_va.verify_va_detail_page_opened()
        time.sleep(2)
        self.support_va.click_minimize_button()

        self.support_device.click_user_manuals_guide()
        self.__verify_redirect_link("UserManualAndGuide", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/hp-elitebook-830-g7-notebook-pc/31971702")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32790549")   
    def test_42_click_back_btn(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32790549
        """
        self.__select_device_card(self.wmi.get_serial_number())
        
        self.support_device.click_back_btn()
            
        assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C35011490")   
    def test_43_click_external_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/35011490
        """
        self.__launch_HPX()
        if self.home.verify_pc_diagtools_card_show():
            self.home.click_pc_diagtools_card()
            self.home.click_pc_visit_support_btn()
            
            assert self.support_device.verify_support_device_page() is not False
            # assert self.support_home.verify_device_display(self.wmi.get_serial_number()) is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C32378673")   
    def test_44_go_to_support_home_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32378673
        """
        self.__launch_HPX()
        self.fc.navigate_to_support()
        assert self.support_home.verify_support_banner_show() is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33721256")  
    def test_45_web_signin(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33721256
        """
        self.__sign_in_HPX()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C38593238")  
    def test_46_verify_UI_paas_printer(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38593238
        """
        self.__sign_in_HPX("xmmirza@outlook.com", "Hpsa2022!")
        self.support_home.select_device_card("TH24BHV0RP")
        assert self.support_device.get_allinplan_label_value() == "HP All-In Plan" 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C38593366")  
    def test_47_show_all_in_plan_banner_for_PAAS_printer(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38593366
        """
        self.__sign_in_HPX("xmmirza@outlook.com", "Hpsa2022!")
        self.support_home.select_device_card("TH24BHV0RP")
        assert self.support_device.get_paas_banner_value() == "Available 24/7 expert assistance from your All-In Plan"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C38593368")  
    def test_48_show_open_the_hp_smart_app(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38593368
        """
        self.__sign_in_HPX("xmmirza@outlook.com", "Hpsa2022!")
        self.support_home.select_device_card("TH24BHV0RP")
        self.support_device.click_hp_smart_btn() 
        self.__verify_process("WinStore.App.exe")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C38155254")  
    def test_49_click_Privacylink(self):
        """
        verify it opens correct page

        https://hp-testrail.external.hp.com/index.php?/cases/view/38155254
        """
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True")
        self.__launch_HPX()
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_view_data_collected_link()
        self.support_device.click_go_privacy_link()
        webpage = "PRIVACY_LINK"
        time.sleep(3)
        self.web_driver.wait_for_new_window(timeout=15)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://www.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hp.com/us-en/privacy/privacy.html"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"])
    @pytest.mark.testrail("S57581.C38200611")
    def test_50_copy_device_details_via_mouse(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38200611
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__sign_in_HPX()
        self.support_home.select_device_card(sn_number)
        self.support_device.select_warranty_info()
        self.support_device.right_click_warrenty_info()
        self.support_device.click_copy_menu_item()

        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "Expires 9/30/2024"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_nick_name()
        self.support_device.right_click_nick_name()
        self.support_device.click_copy_menu_item()    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "My Device"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn()     

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"])
    @pytest.mark.testrail("S57581.C38278021")
    def test_51_copy_device_details_via_keyboard(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38278021
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__sign_in_HPX()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_warranty_info()
        self.support_device.enter_keys_to_warrenty_info(Keys.CONTROL + "c")

        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "Expires 9/30/2024"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_nick_name()
        self.support_device.enter_keys_to_nick_text(Keys.CONTROL + "c")
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "My Device"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn()     

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"])
    @pytest.mark.testrail("S57581.C38278098")
    def test_52_copy_device_details_via_touch_pad(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38278098
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__sign_in_HPX()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_warranty_info()
        self.support_device.right_click_warrenty_info()
        self.support_device.click_copy_menu_item()

        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "Expires 9/30/2024"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_nick_name()
        self.support_device.right_click_nick_name()
        time.sleep(5)
        self.support_device.click_copy_menu_item()    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "My Device"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn()     

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie_NA", "stage_NA", "production_NA"])
    @pytest.mark.testrail("S57581.C38278100")
    def test_53_copy_device_details_via_touch_screen(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38278100
        """
        self.fc.initial_simulate_file(self.file_path, "C35894753", self.app_env, self.stack)
        sn_number = self.fc.load_simulate_file(self.file_path)["C35894753"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]
        self.__sign_in_HPX()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_warranty_info()
        self.support_device.right_click_warrenty_info()
        self.support_device.click_copy_menu_item()

        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()
        
        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "Expires 9/30/2024"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn() 

        self.support_device.click_back_btn()
        self.support_home.select_device_card(sn_number)

        self.support_device.select_nick_name()
        self.support_device.right_click_nick_name()
        time.sleep(5)
        self.support_device.click_copy_menu_item()    
        self.fc.select_country("US")
        self.support_device.click_chat_with_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.enter_keys_to_problem_text(Keys.CONTROL + "v")
            time.sleep(3)
            assert self.support_device.get_problem_text().strip("\r\n") in "My Device"
            self.support_device.click_close_btn()
        else:
            self.support_device.click_close_btn()     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31899325")  
    def test_54_when_no_case_in_account(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31899325
        """
        self.__sign_in_HPX()
        self.support_home.select_device_card("CND7304VTB")
        self.__select_country("US")
        self.support_device.get_open_case_desc() == "There are currently no open cases"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31905572")
    def test_55_go_to_devicedetailspage(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31905572
        """
        self.__sign_in_HPX()
        self.support_home.select_device_card("5CG02735RG")
        self.__select_country("US")
        case_cards_opens = self.support_device.get_open_cases_cards()
        case_cards_closed = self.support_device.get_close_cases_cards()

        self.__verify_case_order(case_cards_opens)
        self.__verify_case_order(case_cards_closed)

        # case_created_times = []
        # card_counts = int(len(case_cards_opens) / 2)
        # for index in range(card_counts):
        #     current_case_card = re.search("\d{10}", case_cards_opens[index]).group(0)
        #     case_created_time = self.support_device.get_case_created_time(current_case_card)
        #     logging.info("get case {} created time: {}".format(current_case_card, case_created_time))
        #     x = re.search("\d+/\d+/\d+", case_created_time)
        #     case_created_times.append(datetime.strptime(x.group(0), '%m/%d/%Y'))

        # assert case_created_times == sorted(case_created_times, reverse=True)

        # card_counts = int(len(case_cards_closed) / 2)
        # for index in range(card_counts):
        #     current_case_card = re.search("\d{10}", case_cards_closed[index]).group(0)
        #     case_created_time = self.support_device.get_case_created_time(current_case_card)
        #     logging.info("get case {} created time: {}".format(current_case_card, case_created_time))
        #     x = re.search("\d+/\d+/\d+", case_created_time)
        #     case_created_times.append(datetime.strptime(x.group(0), '%m/%d/%Y'))
        
        # assert case_created_times == sorted(case_created_times, reverse=True)       

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31899225")
    def test_56_click_dropdownarrow(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31899225
        """
        self.__sign_in_HPX()
        self.support_home.select_device_card("5CG02735RG")
        self.__select_country("US")
        case_cards = self.support_device.get_case_cards()
        for index in range(len(case_cards)):
            current_case_id = case_cards[index][-10:]
            self.support_device.click_case_dropdown(current_case_id)
            time.sleep(3) 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31867183")   
    def test_57_switch_from_external_page(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/31867183
        """
        self.__launch_HPX()

        if self.home.verify_get_help_anytime_card_show():
            self.home.click_get_help_anytime_card()
            self.home.click_pc_visit_support_btn()
            
            assert self.support_device.verify_support_device_page() is not False  

            self.fc.navigate_to_welcome()        
            self.fc.navigate_to_support()

            assert self.support_home.verify_support_home_title() is not False
    
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

    def __select_country(self, country_index, current_locale=None):
        self.fc.select_country(country_index, current_locale)

    def __select_device_card(self, serial_number):
        self.__launch_HPX()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)

    def __sign_in_HPX(self, username="shhpxtest005@outlook.com", password="hpsa@rocks_335"):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in(username, password,self.web_driver)

    def __verify_redirect_link(self, webpage, url_contains, url_current):
        webpage = webpage
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        assert url_current in current_url

    def __verify_process(self, process_name):
        if self.process_util.check_process_running(process_name):
            assert self.process_util.check_process_running(process_name) is True
            self.process_util.kill_process(process_name)

    def __test_is_grogu(self):
        """
        POC for test one machine if is a grogu
        """
        is_grogu = self.wmi.is_grogu()
        if is_grogu:
            print("it is a grogu machine")
        else:
            print("it is not a grogu machine")

    def __verify_case_order(self, case_cards):
        case_created_times = []
        card_counts = int(len(case_cards) / 2)
        for index in range(card_counts):
            current_case_card = re.search("\d{10}", case_cards[index]).group(0)
            case_created_time = self.support_device.get_case_created_time(current_case_card)
            logging.info("get case {} created time: {}".format(current_case_card, case_created_time))
            x = re.search("\d+/\d+/\d+", case_created_time)
            case_created_times.append(datetime.strptime(x.group(0), '%m/%d/%Y'))

        assert case_created_times == sorted(case_created_times, reverse=True)      
   
