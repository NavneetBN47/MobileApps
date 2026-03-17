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
    @pytest.mark.require_stack(["pie", "stage", "production"]) 
    @pytest.mark.testrail("S57581.C33357078")
    def test_16_verify_dispute_warranty_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357078
        """
        self.__select_device_card("6CY435M08S")

        assert self.support_device.verify_warranty_dispute_display() is not False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32386948")       
    def test_17_go_to_resources_section(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32386948
        """
        self.fc.initial_simulate_file(self.file_path, "C31860905", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860905"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_user_manuals_guide()
        self.__verify_redirect_link("UserManualAndGuide", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/")
        self.support_device.click_HP_support_forum()
        self.__verify_redirect_link("HPCommunity", "https://h30434.www3.hp.com", "https://h30434.www3.hp.com/t5/Notebooks")
        self.support_device.click_service_center_locator()
        self.__verify_redirect_link("ServiceCenter", "https://support.hp.com", "https://support.hp.com/us-en/help/service-center")
        self.support_device.click_HP_product_support_center()
        self.__verify_redirect_link("SupportCenter", "https://support.hp.com", "https://support.hp.com")
        self.support_device.click_virtual_repair_center()
        self.__verify_redirect_link("VirtualRepair", "https://support.hp.com", "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa")
        # self.support_device.click_warranty_dispute()
        # self.__verify_redirect_link("WarrantyDispute", "https://support.hp.com", "https://support.hp.com/us-en/document/ish_2534210-1364541-16")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32386949")     
    def test_18_click_on_the_resources(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32386949
        """
        self.fc.initial_simulate_file(self.file_path, "C31860905", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860905"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        self.support_device.click_user_manuals_guide()
        self.__verify_redirect_link("UserManualAndGuide", "https://support.hp.com/", "/us-en/product/setup-user-guides/model/2101189384")
        self.support_device.click_HP_support_forum()
        self.__verify_redirect_link("HPCommunity", "https://h30434.www3.hp.com", "/t5/Notebooks/ct-p/Notebook")
        self.support_device.click_service_center_locator()
        self.__verify_redirect_link("ServiceCenter", "https://support.hp.com", "/us-en/help/service-center")
        self.support_device.click_HP_product_support_center()
        self.__verify_redirect_link("SupportCenter", "https://support.hp.com", "/us-en/product/details/model/2101189384")
        self.support_device.click_virtual_repair_center()
        self.__verify_redirect_link("VirtualRepair", "https://support.hp.com", "?jumpid=in_r11839_us/en/repr/hpsa")
        # self.support_device.click_warranty_dispute()
        # self.__verify_redirect_link("WarrantyDispute", "https://support.hp.com", "/us-en/document/ish_2534210-1364541-16")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33357069") 
    def test_19_go_to_resources_verify_ccls(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357069
        """
        self.__select_device_card("5CG02735RG")
        self.__verify_ccls_options("en-US")

    @pytest.mark.parametrize('lang', ["ar-SA", "en-US"])
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33628101") 
    def test_20_go_to_device_support_page(self, lang):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33628101
        """   
        self.fc.initial_simulate_file(self.file_path, "C31860788", self.app_env, self.stack)
        support_by_region = ma_misc.load_json_file("resources/test_data/hpsa/locale/support/{}.json".format("sr_Latn-RS" if lang == "sr-BA" else lang.replace("-","_")))['common']['supportByRegion']
        self.fc.update_hpx_support_deviceinfo("@hp-af/localization/current-locale", None, lang)
        self.fc.update_hpx_support_deviceinfo("@hp-support/region", None, lang.split("-")[1])    
        self.__launch_HPX()

        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860788"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        assert self.support_device.verify_country_list() is not False
        assert self.support_device.verify_support_by_region_value() == support_by_region

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33628036")      
    def test_21_go_to_liveassistant(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33628036
        """
        self.fc.initial_simulate_file(self.file_path, "C31860788", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860788"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        assert self.support_device.verify_country_list() is not False

        x_1 = self.support_device.verify_support_section().rect['x']
        width_1 = self.support_device.verify_support_section().rect['width']

        x_2 = self.support_device.verify_country_selector().rect['x']
        width_2 = self.support_device.verify_country_selector().rect['width']
        
        assert x_1 + width_1 - (x_2 + width_2) < 100
        
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33628039")         
    def test_22_go_to_social_messaging(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33628039
        """
        self.fc.initial_simulate_file(self.file_path, "C33628039", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33628039"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]),
        self.fc.select_country("US")
        assert self.support_device.verify_country_list() is not False

        x_1 = self.support_device.verify_support_section().rect['x']
        width_1 = self.support_device.verify_support_section().rect['width']

        x_2 = self.support_device.verify_country_selector().rect['x']
        width_2 = self.support_device.verify_country_selector().rect['width']
        
        assert x_1 + width_1 - (x_2 + width_2) < 100

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33628045")   
    def test_23_go_to_resources(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33628045
        """
        self.fc.initial_simulate_file(self.file_path, "C31860788", self.app_env, self.stack)
        self.__launch_HPX()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31860788"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")
        assert self.support_device.verify_country_list() is not False

        x_1 = self.support_device.verify_support_section().rect['x']
        width_1 = self.support_device.verify_support_section().rect['width']

        x_2 = self.support_device.verify_country_selector().rect['x']
        width_2 = self.support_device.verify_country_selector().rect['width']
        
        assert x_1 + width_1 - (x_2 + width_2) < 100 

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33628046")     
    def test_24_change_country(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33628046
        """
        self.__select_device_card("5CG02735RG")
        self.__verify_ccls_options("en-US")
    
        self.__switch_to_country("zh-CN")
        self.__verify_ccls_options("zh-CN")

        self.__switch_to_country("ar-SA")
        self.__verify_ccls_options("ar-SA")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33368080")   
    def test_25_verify_cclsoptions(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33368080
        """
        self.__select_device_card("5CG02735RG")
        self.__verify_ccls_options("en-US")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33538702")   
    def test_26_verify_searchbox(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33538702
        """
        self.__select_device_card("5CG02735RG")
        self.__verify_ccls_options("en-US")

        self.__switch_to_country("zh-CN")
        self.__verify_ccls_options("zh-CN")

        self.__switch_to_country("ja-JP")
        self.__verify_ccls_options("ja-JP")

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33368087")   
    def test_27_verify_the_flag(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33368087
        """
        self.__select_device_card("5CG02735RG")
        
        self.fc.select_country("JP")
        self.support_device.click_back_btn()
        self.__switch_to_device("CND7304VTB")
        self.fc.select_country("GB")

        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.__switch_to_device("5CG02735RG")
        
        country_name = self.support_device.get_country()
        assert country_name == "United Kingdom"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33368089")  
    def test_28_verify_postdevice(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33368089
        """
        self.__select_device_card("5CG3223M9M")
        
        self.fc.select_country("KR")
        webpage = "SUPPORT CENTER"
        self.support_device.click_HP_product_support_center()
        self.web_driver.wait_for_new_window(timeout=20)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()

        assert current_url == "https://support.hp.com/us-en/product/details/model/2101189384"


    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C33368093") 
    def test_29_verify_the_product_page(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33368093
        """
        self.__select_device_card("5CG3223M9M")
        
        webpage = "PRODUCT CENTER"
        
        self.support_device.click_HP_product_support_center()
        self.web_driver.wait_for_new_window(timeout=20)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)

        current_url = self.web_driver.get_current_url()

        assert current_url == "https://support.hp.com/us-en/product/details/model/2101189384"   

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

