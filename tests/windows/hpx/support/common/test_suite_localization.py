from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import MobileApps.resources.const.windows.const as w_const
from selenium.webdriver.common.keys import Keys
import pytest
import time

pytest.app_info = "HPX"
language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

class Test_Suite_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "localization.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822650")  
    def test_01_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822650
        """
        system_locale = self.fc.get_winsystemlocale().strip()
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        if system_locale == "zh-CN":
            system_locale = "zh-Hans"
        elif system_locale == "zh-TW":
            system_locale = "zh-Hant"
        elif system_locale == "zh-HK":
            system_locale = "zh-Hant-HK"
        elif system_locale == "sr-BA":
            system_locale = "sr-Latn-RS"
        
        if system_locale in ["ca-ES", "es-ES", "eu-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translations']['common']['hPOnePremiumDeviceSupport']
        else:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith'] 
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['hPOnePremiumDeviceSupport']

        is_grogu = self.wmi.is_grogu()
        self.fc.navigate_to_support()

        if is_grogu:
            assert self.support_home.get_support_home_title() == hp_one_device_support
        else:
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        self.support_home.select_device_card(self.wmi.get_serial_number())
        #this case will run first after install, so need some loading time
        time.sleep(20)
        diagnostics_tilte = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format(system_locale.replace("-", "_")))['common']['diagnostics']
        assert self.support_device.get_diagnostic_title() == diagnostics_tilte

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822651")  
    def test_02_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822651        
        """
        self.fc.update_hpx_support_locale("yo-NG")
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")['en']['translation']['common']['whatDeviceCanWeHelpYouWith']
        hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")['en']['translation']['common']['hPOnePremiumDeviceSupport']
        is_grogu = self.wmi.is_grogu()
        self.fc.navigate_to_support()
        if is_grogu:
            assert self.support_home.get_support_home_title() == hp_one_device_support
        else:
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        self.support_home.select_device_card(self.wmi.get_serial_number())
        diagnostics_tilte = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format("en_US"))['common']['diagnostics']
        assert self.support_device.get_diagnostic_title() == diagnostics_tilte

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822653")  
    def test_03_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822653
        """
        self.fc.update_hpx_support_locale("zh-Hans")
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.click_visit_on_line_link()
        webpage = "VisitOnLine"
        time.sleep(3)
        self.web_driver.wait_for_new_window()
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert "cn-zh" in current_url

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822660")  
    def test_04_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822660
        """
        self.__test_localization("zh-Hans")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822660")  
    def test_05_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822662
        """
        self.__test_localization("zh-Hant-HK")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822660")  
    def test_06_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822662
        """
        self.__test_localization("zh-Hant")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822664")  
    def test_07_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822664
        """
        self.__test_localization("sr-Latn-RS")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822665")  
    def test_08_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822665
        """
        self.__test_localization("pt-PT")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822666") 
    def test_09_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822666
        """
        self.__test_localization("pt-BR")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822666")    
    def test_10_localization(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822642        
        """
        self.__test_localization("ja-JP")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822652")   
    def test_11_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822652
        """
        self.__test_localization("ca-ES")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_12_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225947
        """
        self.__test_localization("eu-ES")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_13_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225948
        """
        self.__test_localization("es-MX")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_14_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225947
        """
        self.__test_localization("fr-CA")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_15_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225947
        """
        self.__test_localization("gl-ES")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_16_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225947
        """
        self.__test_localization("id-ID")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32225947")   
    def test_17_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32225947
        """
        self.__test_localization("en-GB")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822654")      
    def test_18_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822654
        """
        self.fc.update_hpx_support_locale("zz-ZZ")
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.click_visit_on_line_link()
        webpage = "VisitOnLine"
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://support.hp.com/us-en/dashboard"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822659") 
    @pytest.mark.exclude_platform(["grogu"])     
    def test_19_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822659
        """
        self.fc.initial_simulate_file(self.file_path,"C31822659", self.app_env, self.stack, use_system_locale=False)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31822659"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "หมดอายุ 22/1/2568"
        else:  
            assert self.support_device.get_warranty_value(timeout = 20) == "หมดอายุ 23/3/2568"

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822658")  
    @pytest.mark.exclude_platform(["grogu"]) 
    def test_20_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822658
        """
        self.fc.initial_simulate_file(self.file_path,"C31822658", self.app_env, self.stack, use_system_locale=False)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        self.fc.navigate_to_support()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C31822658"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if self.app_env == "itg":
            assert self.support_device.get_warranty_value(timeout = 20) == "انتهاء مدة الصلاحية ٢٢‏/٧‏/١٤٤٦ هـ"
        else:  
            assert self.support_device.get_warranty_value(timeout = 20) == "انتهاء مدة الصلاحية ٢٣‏/٩‏/١٤٤٦ هـ"     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822657")   
    def test_21_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822657
        """  
        self.__test_localization("ar-SA")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C31822655")     
    def test_22_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/31822655
        """
        system_locale = self.fc.get_winsystemlocale().strip()

        self.fc.restart_app()
        self.fc.maximize_window()    

        self.fc.navigate_to_support()

        if system_locale in ["ca-ES", "es-ES", "eu-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['visitOnlineDashboard']
            hp_support_web = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['HPSupportWeb']
            dont_see_your_device = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['dontSeeYourDevice'].replace("[{{HPSupportWebText}}]({{HPSupportWeb}})", hp_support_web)
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale]['translations']['common']['hPOnePremiumDeviceSupport']
        else:
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['visitOnlineDashboard']
            hp_support_web = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['HPSupportWeb']
            dont_see_your_device = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['dontSeeYourDevice'].replace("[{{HPSupportWebText}}]({{HPSupportWeb}})", hp_support_web)
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[system_locale.split('-')[0]]['translation']['common']['hPOnePremiumDeviceSupport']

        is_grogu = self.wmi.is_grogu()
        assert visit_on_line_dashboard in self.support_home.get_visit_link_title()
        assert self.support_home.get_support_dashboard_desc().strip(".").strip() == dont_see_your_device.strip(".").strip()
        if is_grogu:
            assert self.support_home.get_support_home_title() == hp_one_device_support
        else:
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        self.support_home.select_device_card(self.wmi.get_serial_number())

        guide_troubleshooting = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/{}.json".format(system_locale))['common']['guidedTroubleShooting']
        
        assert self.support_device.get_troubleshooting_title() == guide_troubleshooting

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973034")   
    def test_23_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973034
        """
        self.__test_localization("bg-BG")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973035")   
    def test_24_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973035
        """
        self.__test_localization("cs-CZ")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973036")   
    def test_25_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973036
        """
        self.__test_localization("de-DE")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973037")      
    def test_26_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973037
        """
        self.__test_localization("da-DK")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973038")   
    def test_28_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973038
        """
        self.__test_localization("el-GR")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973039")   
    def test_29_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973039
        """
        self.__test_localization("es-ES")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973040")   
    def test_30_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973040
        """
        self.__test_localization("en-US")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973041")   
    def test_31_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973041
        """
        self.__test_localization("et-EE")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973042")   
    def test_32_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973042
        """
        self.__test_localization("fr-FR")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973043")   
    def test_33_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973043
        """
        self.__test_localization("fi-FI")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973044")   
    def test_34_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973044
        """
        self.__test_localization("he-IL")    

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973045")   
    def test_35_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973045
        """
        self.__test_localization("hr-HR")     

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973046")   
    def test_36_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973046
        """
        self.__test_localization("hu-HU")      

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973083")   
    def test_37_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973083
        """
        self.__test_localization("it-IT") 

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973085")   
    def test_38_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973085
        """
        self.__test_localization("ko-KR")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973086")   
    def test_39_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973086
        """
        self.__test_localization("lt-LT")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973087")   
    def test_40_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973087
        """
        self.__test_localization("lv-LV")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973088")   
    def test_41_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973088
        """
        self.__test_localization("nb-NO")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973089")   
    def test_42_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973089
        """
        self.__test_localization("nl-NL")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973090")   
    def test_43_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973090
        """
        self.__test_localization("pl-PL")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973091")   
    def test_44_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973091
        """
        self.__test_localization("ro-RO")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973092")   
    def test_45_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973092
        """
        self.__test_localization("sk-SK")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973094")   
    def test_46_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973094
        """
        self.__test_localization("sl-SI")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973096")   
    def test_47_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973096
        """
        self.__test_localization("sv-SE")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973097")   
    def test_48_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973097
        """
        self.__test_localization("tr-TR")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973098")   
    def test_49_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973098
        """
        self.__test_localization("uk-UA")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973099")   
    def test_50_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973099
        """
        self.__test_localization("ca-ES")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973099")   
    def test_51_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973100
        """
        self.__test_localization("ar-SA")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973099")   
    def test_52_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973101
        """
        self.__test_localization("he-IL")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973099")   
    def test_53_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973102
        """
        self.__test_localization("th-TH")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C34973099")   
    def test_54_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34973256
        """
        self.__test_localization("ru-RU")   

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"]) 
    @pytest.mark.testrail("S57581.C33343057")   
    def test_55_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33343057
        """
        self._test_visit_on_line_translation("en-US")
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"]) 
    @pytest.mark.testrail("S57581.C33343057")   
    def test_56_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33343057
        """
        self._test_visit_on_line_translation_signin("en-US")

    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"]) 
    @pytest.mark.testrail("S57581.C33343057")   
    def test_57_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33343057
        """
        self._test_visit_on_line_translation("en-GB")
        
    @pytest.mark.require_priority(["Medium"])  
    @pytest.mark.require_stack(["stage_NA", "pie", "production_NA"]) 
    @pytest.mark.testrail("S57581.C33343057")   
    def test_58_localization(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33343057
        """
        self._test_visit_on_line_translation_signin("en-GB")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __test_localization(self, language):
        """
        test localization for every locale
        """
        self.fc.update_hpx_support_locale(language)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        language_mapped = language
        if language == 'zh-Hans':
            language_mapped = 'zh-CN'
        elif language == 'zh-Hant':
            language_mapped = 'zh-TW'
        elif language == 'zh-Hant-HK':
            language_mapped = 'zh-HK'
        elif language == "sr-Latn-RS":
            language_mapped = 'sr-BA'

        if language in ["ca-ES", "es-ES", "eu-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['hPOnePremiumDeviceSupport']
        else:
            whatDeviceCanWeHelpYouWith = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['whatDeviceCanWeHelpYouWith']
            hp_one_device_support = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['hPOnePremiumDeviceSupport']            

        is_grogu = self.wmi.is_grogu()
        self.fc.navigate_to_support()
        if is_grogu:
            assert self.support_home.get_support_home_title() == hp_one_device_support
        else:
            assert self.support_home.get_support_home_title() == whatDeviceCanWeHelpYouWith
        self.support_home.select_device_card(self.wmi.get_serial_number())
        diagnostics_tilte = ma_misc.load_json_file("resources/test_data/hpsa/locale/diagnostics/{}.json".format("sr_Latn-RS" if language_mapped == "sr-BA" else language_mapped.replace("-","_")))['common']['diagnostics']
        assert self.support_device.get_diagnostic_title() == diagnostics_tilte
        
    def __sign_in_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.fc.navigate_to_support()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver)
        
    def _test_visit_on_line_translation(self,language):
        """
        test localization for every locale
        """
        self.fc.update_hpx_support_locale(language)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)

        if language in ["ca-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            hp_support_web = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['HPSupportWeb']
            dont_see_your_device = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['dontSeeYourDevice'].replace("[{{HPSupportWebText}}]({{HPSupportWeb}})", hp_support_web)
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['visitOnlineDashboard']
        else:
            hp_support_web = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['HPSupportWeb']
            dont_see_your_device = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['dontSeeYourDevice'].replace("[{{HPSupportWebText}}]({{HPSupportWeb}})", hp_support_web)
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['visitOnlineDashboard']

        self.fc.navigate_to_support()
        assert self.support_home.get_visit_link_title() == visit_on_line_dashboard
        assert self.support_home.get_support_dashboard_desc().strip(".").strip() == dont_see_your_device.strip(".").strip()

    def _test_visit_on_line_translation_signin(self,language):
        """
        test localization for every locale
        """
        self.fc.update_hpx_support_locale(language)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        self.__sign_in_HPX()
        if language in ["ca-ES", "fr-CA", "gl-ES", "nb-NO", "pt-BR", "pt-PT", "sr-Latn-RS", "sr-BA", "zh-Hans", "zh-Hant-HK", "zh-Hant"]:
            visit_online_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['toAddOrRemoveDeviceVisitYourOnlineDashboard1']
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language]['translation']['common']['visitOnlineDashboard']
        else:
            visit_online_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['toAddOrRemoveDeviceVisitYourOnlineDashboard1']
            visit_on_line_dashboard = ma_misc.load_json_file("resources/test_data/hpsa/locale/support_dashboard/translations.json")[language.split('-')[0]]['translation']['common']['visitOnlineDashboard']

        visit_online_dashboard.replace("{{visitOnlineDashboard}}",visit_on_line_dashboard)
        self.fc.navigate_to_support()
        assert self.support_home.get_support_dashboard_desc().replace(" .",".") == visit_online_dashboard.replace("{{visitOnlineDashboard}}",visit_on_line_dashboard)
        assert self.support_home.get_visit_link_title() == visit_on_line_dashboard