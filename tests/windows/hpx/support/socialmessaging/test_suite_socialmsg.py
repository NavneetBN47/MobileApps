import time
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest

pytest.app_info = "HPX"
class Test_Suite_SocialMsg(object):
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
        cls.hpid = cls.fc.fd["hpid"]    
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.devices = cls.fc.fd["devices"]
        cls.app_env = request.config.getoption("--app-env")
        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "social_message.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    @pytest.mark.require_priority(["Medium"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32300812")  
    def test_01_Set_to_unsupported_regions_and_languages(self): 
        """
        verify social channel section is not shown

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32300812
        """
        self.fc.initial_simulate_file(self.file_path, "C32300812", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        time.sleep(5)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300812"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("CZ")
        assert self.support_device.verify_fbmessenger_display() is False
        assert self.support_device.verify_kakaotalk_display() is False
        assert self.support_device.verify_line_display() is False
        assert self.support_device.verify_wechat_display() is False
        assert self.support_device.verify_whatsapp_display() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32300878")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_02_Click_on_WhatsApp_option(self):
        """
        verify the service URL is correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32300878
        """
        self.fc.initial_simulate_file(self.file_path, "C32300878", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300878"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        if self.app_env == "itg":
            self.fc.select_country("GB")
        else:
            self.fc.select_country("HK")
        self.support_device.click_whatsapp()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "WhatsApp"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.js_wait_complete()
            time.sleep(3)
            current_url = self.web_driver.get_current_url()
            if self.app_env == "itg":
                assert "https://api.whatsapp.com/send?phone=" in current_url
            else:
                assert "https://web.whatsapp.com/" in current_url
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production_NA"]) 
    @pytest.mark.testrail("S57581.C32300958")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_03_Click_on_Facebook_Messenger_option(self): 
        """
        verify the service URL is correct
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32300958
        """
        self.fc.initial_simulate_file(self.file_path, "C32300958", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300958"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        country_list = ["US", "ES", "FR", "GB", "IE", "IL", "MX", "TR", "NL", "SR", "BR"]
        for country_code in country_list:
            self.fc.select_country(country_code)
            self.support_device.click_fbmessenger()
            if not self.support_device.verify_outside_hours_popup_display():
                webpage = "Messenger"
                time.sleep(3)
                self.web_driver.add_window(webpage)
                self.web_driver.switch_window(webpage)  
                time.sleep(60)
                current_url = self.web_driver.get_current_url()
                print ("current curl=" +  current_url)
                self.web_driver.wait_url_contains("https://www.messenger.com/", timeout=30)
                current_url = self.web_driver.get_current_url()
                assert "https://www.messenger.com/" in current_url
            else:
                self.support_device.click_close_btn()

    # @pytest.mark.repeat(50)
    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32301434")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_04_Click_on_WeChat_option(self):
        """
        verify the service URL is correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32301434
        """
        self.fc.initial_simulate_file(self.file_path, "C32301434", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32301434"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("CN")
        self.support_device.click_wechat()
        webpage = "WeChat"
        time.sleep(3)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains("https://www.hp.com/", timeout=30)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hp.com/cn-zh/contact-hp/webchat-support.html?src=csptwechat"

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32456032")  
    @pytest.mark.exclude_platform(["grogu"])       
    def test_05_Click_on_KaKaoTalk_option(self): 
        """
        verify the service URL is correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32456032
        """
        self.fc.initial_simulate_file(self.file_path, "C32456032", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32456032"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("KR")
        self.support_device.click_kakaotalk()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "KaKaoTalk"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            assert current_url == "https://support.hp.com/kr-ko/document/c02068647"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32456390")  
    @pytest.mark.exclude_platform(["grogu"])
    def test_06_Click_on_Line_option(self): 
        """
        verify the service URL is correct

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32456390
        """
        self.fc.initial_simulate_file(self.file_path, "C32456390", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32456390"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country('JP')
        self.support_device.click_line()
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = "Line"
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains("https://support.hp.com/", timeout=30)
            current_url = self.web_driver.get_current_url()
            if self.app_env == "itg":
                assert current_url == "https://support.hp.com/jp-ja/document/c04895571"
            else:
                assert current_url == "https://support.hp.com/jp-ja/document/c08418781"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["pie"]) 
    @pytest.mark.testrail("S57581.C33640884") 
    @pytest.mark.require_platform(["grogu"]) 
    def test_07_HPOne_no_social_messaging_channels_show(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33640884 (to do)
        """
        self.fc.initial_simulate_file(self.file_path, "C33640884", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.sign_in(self.hpid_username, self.hpid_password, self.web_driver)
        self.navigation_panel.navigate_to_pc_device()
        self.devices.click_support_btn()
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C33640884"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("US")

        assert self.support_device.verify_social_messaging_label_display() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32300824")  
    def test_08_set_to_unsupported_scenarios(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32300824
        """
        self.fc.initial_simulate_file(self.file_path, "C32300824", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300824"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        self.fc.select_country("CN")
        assert self.support_device.verify_wechat_display() is not False
        self.fc.update_hpx_support_deviceinfo("@hp-support/deviceInfo", "productLineCode", "AN")
        self.fc.update_hpx_support_deviceinfo("@hp-support/deviceInfo", "productNumber", "158U3AA#ABA" )
        self.fc.update_hpx_support_deviceinfo("@hp-support/deviceInfo", "serialNumber", "5CG02735RG")
        self.fc.update_hpx_support_deviceinfo("@hp-af/localization/current-locale", None, "en-GB")
        self.fc.update_hpx_support_deviceinfo("@hp-support/region", None, "GB")
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.support_home.select_device_card("5CG02735RG")
        self.fc.select_country("GB",  "en-GB")
        assert self.support_device.verify_wechat_display() is False
        self.fc.update_hpx_support_deviceinfo("@hp-support/deviceInfo", "productLineCode", "KV")
        self.fc.update_hpx_support_deviceinfo("@hp-af/localization/current-locale", None, "pt-BR")
        self.fc.update_hpx_support_deviceinfo("@hp-support/region", None, "BR")                                     
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        self.support_home.select_device_card("5CG02735RG")
        self.fc.select_country("GB", "pt-BR")
        assert self.support_device.verify_wechat_display() is False

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32300864")     
    def test_09_click_on_the_social_channel_options(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32300864
        """
        self.fc.initial_simulate_file(self.file_path, "C32300824", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300824"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
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

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32301485")        
    def test_10_when_it_is_out_of_working_hour(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32301485
        """
        self.fc.initial_simulate_file(self.file_path, "C32300824", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300824"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
        self.fc.select_country("ID")
        self.support_device.click_whatsapp()
        self.__verify_outside_hours()
        # self.fc.select_country("TR")
        # self.support_device.click_fbmessenger()
        # self.__verify_outside_hours()
        self.fc.select_country("CN")
        self.support_device.click_wechat()
        self.__verify_outside_hours()
        self.fc.select_country("JP")
        self.support_device.click_line()
        self.__verify_outside_hours()
        self.fc.select_country("KR")
        self.support_device.click_kakaotalk()
        self.__verify_outside_hours()
        self.fc.select_country("VN")
        self.support_device.click_zalo()
        self.__verify_outside_hours()

    @pytest.mark.require_priority(["High"])
    @pytest.mark.require_stack(["stage", "pie", "production"]) 
    @pytest.mark.testrail("S57581.C32595506")   
    def test_11_go_to_social_messaging_channels_section(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595506
        """
        self.fc.initial_simulate_file(self.file_path, "C32300824", self.app_env, self.stack)
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.navigate_to_support()
        # self.fc.sign_out(self.web_driver)
        self.support_home.select_device_card(self.fc.load_simulate_file(self.file_path)["C32300824"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"]) 
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
        self.fc.select_country("JP")
        self.support_device.click_twitter()
        self.__verify_redirect_link("Twitter", "https://x.com/", "https://x.com/HPSupportJPN")
        self.fc.select_country("KR")
        self.support_device.click_kakaotalk()
        self.__verify_redirect_link("KaKaoTalk", "https://support.hp.com/", "https://support.hp.com/kr-ko/document/")
        self.fc.select_country("VN")
        self.support_device.click_zalo()
        self.__verify_redirect_link("Zalo", "https://zalo.me", "https://zalo.me")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __verify_redirect_link(self, webpage, url_contains, url_current):
        if not self.support_device.verify_outside_hours_popup_display():
            webpage = webpage
            time.sleep(3)
            self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)  
            self.web_driver.wait_url_contains(url_contains, timeout=30)
            current_url = self.web_driver.get_current_url()
            assert url_current in current_url
        else:
            self.support_device.click_close_btn()

    def __verify_outside_hours(self):
        if self.support_device.verify_outside_hours_popup_display():
            self.support_device.click_close_btn()
        
   
