import time
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import pytest
from bs4 import BeautifulSoup

pytest.app_info = "HPX"
class Test_Suite_Warranty(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.login_account = ma_misc.get_hpsa_account_info(cls.stack)    
        cls.hpid_username = cls.login_account["email"]
        cls.hpid_password = cls.login_account["password"]

        cls.fc = FlowContainer(cls.driver)     
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.hpid = cls.fc.fd["hpid"]    
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.settings = cls.fc.fd["settings"]

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "warranty.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_hpx_support_env()

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie_NA"])
    @pytest.mark.testrail("S57581.C31915938")
    def test_01_Sign_in_before_navigate(self):
        """
        verify the subscription data

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915938
        """
        self.fc.initial_simulate_file(self.file_path, "C31915938", "itg")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31915938"]["itg"]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_subcription_id_value() == "7875437443"
        assert self.support_device.get_state_date_value() == "9/7/2022"

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie_NA"])
    @pytest.mark.testrail("S57581.C32316801")
    def test_02_Sign_in_after_navigate(self):
        """
        verify the subscription data

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32316801
        """      
        self.fc.initial_simulate_file(self.file_path, "C32316801", "itg")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32316801"]["itg"]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_subcription_id_value() == "7875437443"
        assert self.support_device.get_state_date_value() == "9/7/2022"

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie_NA"])
    @pytest.mark.testrail("S57581.C32450357")
    def test_03_Click_the_host(self): 
        """
        Verify the subscription data on the device page

        Test Rails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32450357
        """
        self.fc.initial_simulate_file(self.file_path,"C32450357", "itg")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(2)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32450357"]["itg"]["@hp-support/deviceInfo"]["serialNumber"])
        self.navigation_panel.select_my_hp_account_btn()
        self.hpid.verify_login(self.hpid_username, self.hpid_password)
        assert self.support_device.get_subcription_id_value() == "7875437443"
        assert self.support_device.get_state_date_value() == "9/7/2022"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"])   
    @pytest.mark.testrail("S57581.C31915943")
    @pytest.mark.exclude_platform(["grogu"])
    def test_04_verify_warranty_expires(self):
        """
        Verify warranty expires

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915943   
        """
        self.fc.initial_simulate_file(self.file_path,"C31915943", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31915943"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "Expires 1/22/2025"
        else:  
            assert self.support_device.get_warranty_value(timeout = 20) == "Expires 3/23/2025"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C32288315")
    @pytest.mark.exclude_platform(["grogu"])
    def test_05_verify_warranty_expired(self):
        """
        Verify warranty expired

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32288315

        """
        self.fc.initial_simulate_file(self.file_path, "C32288315", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32288315"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 10/16/2022"
        else: 
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 9/2/2021"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"])    
    @pytest.mark.testrail("S57581.C32288359")
    @pytest.mark.exclude_platform(["grogu"])
    def test_06_verify_warranty_unknown(self):
        """
        Verify warranty unknown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32288359
        """
        self.fc.initial_simulate_file(self.file_path, "C32288359", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32288359"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_warranty_value(timeout = 20) == "Unknown"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C31915944")
    def test_08_Click_Get_details(self): 
        """
        verify warranty option can be shown up

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915944
        """            
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        get_details = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['getDetails']    
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.navigation_panel.navigate_to_settings()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_no_button()
        self.settings.click_done_button()   
        time.sleep(5)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        assert self.support_device.get_warranty_details_value(timeout = 20) == get_details

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C31915955")
    def test_09_Click_Get_details(self):
        """
        verify the contents on the warranty option popup

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915955
        """        
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        allow_personalized_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['allowPersonalizedSupport']   
        view_data_collected = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['viewDataCollected']    
        yes = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['yes']   
        no = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['no']   
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.navigation_panel.navigate_to_settings()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_no_button()
        self.settings.click_done_button() 
        time.sleep(5) 
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        assert self.support_device.get_warranty_details_popup_title(timeout = 20) == allow_personalized_support
        assert self.support_device.get_suppprt_dialog_link_value(timeout = 20) == view_data_collected
        assert self.support_device.get_yes_button_value(timeout = 20) == yes
        assert self.support_device.get_no_button_value(timeout = 20) == no

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C31915966")
    def test_10_Click_Yes_button(self):
        """
        verify it can start checking warranty

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915966
        """ 
        self.fc.close_app()
        self.fc.initial_simulate_file(self.file_path, "C31915966", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        # self.fc.sign_out(self.web_driver)
        # self.navigation_panel.navigate_to_settings()
        # self.settings.click_hp_privacy_settings()
        # self.settings.click_warranty_no_button()
        # self.settings.click_done_button()   
        time.sleep(5)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31915966"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_warranty_details_link()
        self.support_device.click_yes_button()
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 10/16/2022"
        else: 
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 9/2/2021"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C31915967")       
    def test_11_Click_No_button(self):
        """
        verify it can close the popup

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915967
        """  
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        get_details = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['getDetails']  
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.navigation_panel.navigate_to_settings()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_no_button()
        self.settings.click_done_button()   
        time.sleep(5)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_no_button()
        assert self.support_device.get_warranty_details_value(timeout = 20) == get_details

    @pytest.mark.require_priority(["Medium"]) 
    @pytest.mark.exclude_platform(["grogu"])  
    @pytest.mark.testrail("S57581.C31915969")
    @pytest.mark.require_stack(["stage","production"]) 
    def test_12_Click_View_data_collected(self):
        """
        verify it can show related contents

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915969
        """
        system_locale = self.fc.get_winsystemlocale().strip()
        language = "sr_Latn-RS" if system_locale == "sr-BA" else system_locale
        with open(ma_misc.get_abs_path("resources/test_data/hpsa/locale/view_data_collected/{}/HPSFCollectedData.html").format(language), "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml")
            title_tag = soup.find("title")
            header = title_tag.text.strip()
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.navigation_panel.navigate_to_settings()
        self.settings.click_hp_privacy_settings()
        self.settings.click_warranty_no_button()
        self.settings.click_done_button()   
        time.sleep(5)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_view_data_collected_link()
        assert self.support_device.get_warranty_details_content_title() == header

    @pytest.mark.require_priority(["Medium"])   
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"])     
    @pytest.mark.testrail("S57581.C32581515")
    def test_13_Privacy_settings(self):
        """
        verify it can start checking warranty

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32581515
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        get_details = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common']['getDetails']  
        self.fc.close_app()
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "Managed", "True")
        self.fc.launch_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.click_warranty_details_link()
        self.support_device.click_yes_button()
        self.navigation_panel.navigate_to_settings()
        self.fc.navigate_to_support()
        time.sleep(3)
        self.support_home.select_device_card(self.wmi.get_serial_number())
        assert self.support_device.get_warranty_details_value(timeout = 20) == get_details

    @pytest.mark.require_priority(["Medium"])   
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31915968")        
    def test_14_Sign_in_profile(self):
        """
        verify clicking the Get details

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915968
        """
        self.fc.initial_simulate_file(self.file_path, "C31915968", self.app_env, self.stack)
        self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") 
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.fc.navigate_to_support()
        time.sleep(10)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31915968"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_warranty_details_link()
        self.support_device.click_yes_button()
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 10/16/2022"
        else:
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 9/2/2021"

    @pytest.mark.require_priority(["Medium"])   
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32449909")   
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_15_Sign_in_profile(self):
        """
        verify the warranty for the transaction device

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32449909
        """
        self.fc.initial_simulate_file(self.file_path,"C32449909", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.navigate_to_support()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32449909"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])

        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "Expired 11/18/2022"
        else:
            assert self.support_device.get_warranty_value(timeout = 20) == "Expires 3/23/2025"

    @pytest.mark.require_priority(["Medium"])   
    @pytest.mark.require_stack(["stage", "production"]) 
    @pytest.mark.testrail("S57581.C33402476")    
    @pytest.mark.exclude_platform(["grogu"])
    def test_16_on_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33402476
        """
        self.fc.initial_simulate_file(self.file_path,"C33402476", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        """
        Currently, support device card's performance is not very good, so need sleep 10s to automate this feature.
        """
        time.sleep(10)
        local_pc_details = self.support_home.get_device_details(self.fc.load_simulate_file(self.file_path)["C33402476"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert "Care Pack" in local_pc_details
        assert "Expires 10/6/2025" in local_pc_details
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33402476"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_warranty_title_value() == "Care Pack"
        assert self.support_device.get_warranty_value() == "Expires 10/6/2025"

    @pytest.mark.require_priority(["Medium"])   
    @pytest.mark.require_stack(["stage", "production"]) 
    @pytest.mark.testrail("S57581.C33402477")   
    @pytest.mark.exclude_platform(["grogu"])
    def test_17_on_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33402477
        """
        self.fc.initial_simulate_file(self.file_path,"C33402477", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        """
        Currently, support device card's performance is not very good, so need sleep 10s to automate this feature.
        """
        time.sleep(10)
        local_pc_details = self.support_home.get_device_details(self.fc.load_simulate_file(self.file_path)["C33402477"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert "Care Pack" in local_pc_details
        assert "Expired 3/17/2023" in local_pc_details
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33402477"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.get_warranty_title_value() == "Care Pack"
        assert self.support_device.get_warranty_value() == "Expired 3/17/2023"
        
    @pytest.mark.require_priority(["Medium"]) 
    #@pytest.mark.require_platform(["grogu"])  
    @pytest.mark.testrail("S57581.C34117251")
    @pytest.mark.require_stack(["pie_NA"]) 
    def test_18_Click_View_data_collected_Grogu(self):
        """
        verify it can show related contents

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/34117251
        """
        self.fc.initial_simulate_file(self.file_path,"C34117251", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C34117251"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        time.sleep(5)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C34117251"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_warranty_details_link_subscription()
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver, user_icon_click = False)
        assert self.support_device.get_subcription_id_value() == "620187557888"
        assert self.support_device.get_state_date_value() == "5/29/2023"

    @pytest.mark.require_priority(["Medium"]) 
    @pytest.mark.testrail("S57581.C33402962")
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_19_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33402962
        """
        self.__select_device_card("3CQ511314R")
        assert self.support_device.get_warranty_value() == "Expired 8/3/2018"

    @pytest.mark.require_priority(["Medium"]) 
    @pytest.mark.testrail("S57581.C33403023")
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    def test_20_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33403023
        """
        self.__sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335")

    @pytest.mark.require_priority(["Medium"]) 
    @pytest.mark.testrail("S57581.C32466617")
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.exclude_platform(["grogu"])
    def test_21_on_the_device_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32466617
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/warranty/{}.json".format(system_locale))['common'] 

        self.__launch_HPX()

        self.support_home.select_device_card(self.wmi.get_serial_number())

        assert self.support_device.get_warranty_value().split(" ")[0] in [common["expires"], common["expired"], common["unknown"], common["pending"]]

    @pytest.mark.require_priority(["Medium"]) 
    @pytest.mark.testrail("S57581.C32455363")
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.exclude_platform(["grogu"])
    def test_22_sign_in_profile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32455363
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")
        
        common = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['common'] 

        # self.__launch_HPX()

        # local_pc_details = self.support_home.get_device_details(self.wmi.get_serial_number())

        
        
        # assert local_pc_details[local_pc_details.find("Warranty"):].split(" ")[1] in [common["expires"], common["expired"], common["unknown"], common["pending"]]
        self.__sign_in(self.hpid_username, self.hpid_password)
        self.support_home.select_device_card(self.wmi.get_serial_number())

        assert self.support_device.get_warranty_value().split(" ")[0] in [common["expires"], common["expired"], common["unknown"], common["pending"]]

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_device_card(self, serial_number):
        self.__sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335")
        self.support_home.select_device_card(serial_number)
    
    def __sign_in(self, user_name, pass_word):
        self.__launch_HPX()
        time.sleep(3)
        self.fc.sign_in(user_name, pass_word, self.web_driver)          

    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)

    # def test_19_Sign_in_profile(self):
    #     """
    #     verify clicking the Get details

    #     TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31915968
    #     """
    #     self.registry.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") 
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.sign_out(self.web_driver)
    #     time.sleep(3)
    #     self.fc.sign_in("hpxtest001@gmail.com", "hpsa@rocks_335", self.web_driver)
    #     self.fc.navigate_to_support()
    #     time.sleep(10)
