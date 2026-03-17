import time
import MobileApps.resources.const.windows.const as w_const
from urllib.parse import urlparse, parse_qs
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_User_Guide(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

        cls.fc = FlowContainer(cls.driver) 
        cls.registry = RegistryUtilities(cls.driver.ssh)
        cls.wmi = WmiUtilities(cls.driver.ssh)   
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.hpid = cls.fc.fd["hpid"] 

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "support_resource.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31857237")
    def test_01_Set_to_unsupported_regions_and_languages(self): 
        """
        verify 'User manuals and guides' card is not shown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31857237
        """
        self.fc.initial_simulate_file(self.file_path,"C31857237", self.app_env, self.stack, use_system_locale=False)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31857237"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        time.sleep(3)
        assert self.support_device.verify_user_manuals_guide() is False

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31857771")
    def test_02_Click_on_User_manuals_and_guides_card(self): 
        """
        verify the URL before redirecting and after redirecting

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31857771
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        user_manual_title = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['userManuals']['title']
        user_manual_des = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['userManuals']['description']
        self.fc.initial_simulate_file(self.file_path, "C31857771", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31857771"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if system_locale in ["en_US"]:
            assert self.support_device.get_user_manual_guide_value(timeout=20) == "{} {}".format(user_manual_title, user_manual_des)
            self.fc.select_country("US")
            webpage = "UserManualAndGuide"
            self.support_device.click_user_manuals_guide(timeout=20)
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/us-en/product/setup-user-guides/model/2101189384"
        else:
            assert self.support_device.verify_user_manuals_guide() == False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31860782")
    def test_03_Set_to_unsupported_regions_and_languages(self): 
        """
        verify 'HP community' card is not shown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31860782
        """
        self.fc.initial_simulate_file(self.file_path,"C31860782", self.app_env, self.stack, use_system_locale=False)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860782"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.support_device.click_country_list()
        self.support_device.select_country("199")
        time.sleep(5)
        assert self.support_device.verify_support_forum() is False

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31860788")
    def test_04_Click_on_HP_community_card(self):
        """
        verify the URL before redirecting and after redirecting

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31860788
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        hp_community_title = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['HPCommunity']['title']
        hp_comminity_des = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['HPCommunity']['description']
        self.fc.initial_simulate_file(self.file_path, "C31860788", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860788"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        assert self.support_device.get_support_form_card_value() == "{}{}".format(hp_community_title, hp_comminity_des)
        webpage = "HPCommunity"
        self.support_device.click_HP_support_forum()
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.web_driver.wait_url_contains("https://h30434.www3.hp.com", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://h30434.www3.hp.com/t5/Notebooks/ct-p/Notebook"

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["stage_NA", "pie_NA"]) 
    @pytest.mark.testrail("S57581.C31860865")
    def test_05_Set_to_unsupported_regions_and_languages(self):
        """
        verify 'Product support center' card is not shown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31860865
        """
        self.fc.initial_simulate_file(self.file_path, "C31860865", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860865"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.verify_product_support_center() is False

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31860905")
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_06_Click_on_Product_support_center_card(self):
        """
        verify the URL before redirecting and after redirecting, hpone not support product center card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31860905
        """
        system_locale = self.fc.get_winsystemlocale().strip().replace("-", "_")  
        psc_title = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['productSupportCenter']['title']
        psc_des = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if system_locale == "sr-BA" else system_locale.replace("-","_")))['productSupportCenter']['description']
        self.fc.initial_simulate_file(self.file_path, "C31860905", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860905"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")        
        assert self.support_device.get_support_center_card_value() == "{} {}".format(psc_title, psc_des)
        webpage = "SupportCenter"
        self.support_device.click_HP_product_support_center()
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://support.hp.com", timeout=30) 
        current_url = self.web_driver.get_current_url()
        if self.app_env == "itg":
            assert current_url == "https://support.hp.com/" + system_locale.split('_')[1].lower() + "-" + system_locale.split('_')[0].lower() + "/product/details/model/2101189384"
        else:
            assert current_url == "https://support.hp.com/" + system_locale.split('_')[1].lower() + "-" + system_locale.split('_')[0].lower() + "/product/details/model/2101189384"

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33353862")
    def test_07_click_on_a_remote_notebook(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33353862
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SERVICE_CENTER", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SERVICE_CENTER": self.support_device.SERVICE_CENTER, 
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/17053433",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SERVICE_CENTER": "https://support.hp.com/us-en/help/service-center", 
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/t5/Notebooks/ct-p/Notebook", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/17053433"}

        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "CND7304VTB")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33353947")
    def test_08_click_on_a_remote_desktop(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33353947
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SERVICE_CENTER", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SERVICE_CENTER": self.support_device.SERVICE_CENTER, 
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/25277898",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SERVICE_CENTER": "https://support.hp.com/us-en/help/service-center", 
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/t5/Desktops/ct-p/DesktopPC", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/25277898"}
        
        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "MXL0362720")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33354079")
    def test_09_click_on_a_remote_printer(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33354079
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/4323587",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/t5/Printers/ct-p/InkJet", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/4323587"}
        
        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "CN222191QR")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357064")
    def test_10_click_on_a_remote_tablet(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357064
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SERVICE_CENTER", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                #  "WARRANTY_DISPUTE": self.support_device.WARRANTY_DISPUTE,
                 "SERVICE_CENTER": self.support_device.SERVICE_CENTER,
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/6608625",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                # "WARRANTY_DISPUTE" : "https://support.hp.com/us-en/document/ish_2534210-1364541-16",
                "SERVICE_CENTER" : "https://support.hp.com/us-en/help/service-center",
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/6608625"}

        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "6CY435M08S")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357065")
    def test_11_click_on_a_remote_scanner(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357065
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/3723466",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/t5/Printers/ct-p/InkJet", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/3723466"}
        
        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "CN44OCA018")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357066")
    def test_12_click_on_a_remote_monitor(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357066
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SERVICE_CENTER", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SERVICE_CENTER": self.support_device.SERVICE_CENTER,
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/6809766",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SERVICE_CENTER" : "https://support.hp.com/us-en/help/service-center",
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/6809766"}
        
        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "3CQ511314R")

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357067")
    def test_13_click_on_a_remote_mobile(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357067
        """
        web_pages = ["USER_MAUNAL", "VIRTUAL_REPAIR", "SERVICE_CENTER", "SUPPORT_FORUM", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "VIRTUAL_REPAIR": self.support_device.VIRTUAL_REPAIR,
                 "SERVICE_CENTER": self.support_device.SERVICE_CENTER,
                 "SUPPORT_FORUM": self.support_device.SUPPORT_FORUM, 
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}

        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/10722033",
                "VIRTUAL_REPAIR": "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa",
                "SERVICE_CENTER" : "https://support.hp.com/us-en/help/service-center",
                "SUPPORT_FORUM": "https://h30434.www3.hp.com/", 
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/10722033"}
        
        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "9CU6350BTS") 

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.exclude_platform(["grogu"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357068")
    def test_14_click_on_a_remote_calculator(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357068
        """
        web_pages = ["USER_MAUNAL", "SUPPORT_CENTER"]
        
        page_links = {"USER_MAUNAL": self.support_device.USER_MAUNAL,
                 "SUPPORT_CENTER": self.support_device.SUPPORT_CENTER}
        
        page_urls = {"USER_MAUNAL": "https://support.hp.com/us-en/product/setup-user-guides/model/7298644",
                "SUPPORT_CENTER": "https://support.hp.com/us-en/product/details/model/7298644"}

        self.__click_remote_device_resource_link(web_pages, page_links, page_urls, "7CD524006F") 

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357076")
    def test_15_verify_dispute_warranty_not_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357076
        """
        self.__select_device_card("CN222191QR")
        
        assert self.support_device.verify_warranty_dispute_display() is False

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_device_card(self, serial_number):
        self.fc.update_hpx_support_locale("en-US")
        self.__launch_HPX()
        self.__sign_in_HPX("shhpxtest005@outlook.com", "hpsa@rocks_335")
        time.sleep(10)
        self.support_home.verify_device_display(serial_number)
        self.support_home.select_device_card(serial_number)
        time.sleep(5)
        self.fc.select_country("US")
    
    def __switch_to_device(self, serial_number):
        self.support_home.verify_device_display(serial_number)
        self.support_home.select_device_card(serial_number)

    def __switch_to_country(self, lang_country):
        self.fc.update_hpx_support_locale(lang_country)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.__switch_to_device("5CG02735RG")
        self.fc.select_country(lang_country.split('-')[1], lang_country)
    
    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)

    def __sign_in_HPX(self, user_name, pass_word):
        self.fc.sign_in(user_name, pass_word, self.web_driver)

    def __click_remote_device_resource_link(self, web_pages, page_links, page_urls, serial_number):
        self.__select_device_card(serial_number)
        time.sleep(10)
        for webpage in web_pages:
            time.sleep(5)
            self.support_device.click_link(page_links[webpage])
            time.sleep(3)
            self.web_driver.add_window(webpage)

            if webpage not in self.web_driver.session_data["window_table"].keys():
                self.support_device.click_link(page_links[webpage])
                time.sleep(3)
                self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)
            self.web_driver.wait_url_contains(page_urls[webpage], timeout=30) 

            current_url = self.web_driver.get_current_url()
            self.web_driver.close_window(webpage)
            for sub_url in page_urls[webpage]:
                assert sub_url in current_url 

    def __verify_redirect_link(self, webpage, url_contains, url_current):
        webpage = webpage
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        assert url_current in current_url

    def __verify_ccls_options(self, lang_country):
        ccls_services = self.fc.get_ccls_services(self.stack, "", "38462601", "31971702", lang_country)
        ccls_services = sorted(list(map(lambda x: x.lower(), ccls_services)))
        resources_cards = self.support_device.get_resources_cards()
        liveassistant_cards = self.support_device.get_liveassistant_cards()        
        services_cards = list(set(resources_cards).union(set(liveassistant_cards)))
        services_cards = sorted(list(map(lambda x: x.lower(), services_cards)))

        assert len(ccls_services) == len(services_cards)       
        for index in range(len(ccls_services)):
            assert ccls_services[index].lower() in services_cards[index].lower() 

