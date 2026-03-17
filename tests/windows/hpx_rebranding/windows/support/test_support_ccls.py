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
class Test_Suite_CCLS(object):
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
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        # self.remote_artifact_path = "{}\\{}\\LocalState\\".format(
        #     w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        # self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/support/properties.json"), self.remote_artifact_path+"properties.json")
        # self.__set_featureflags(True) 

    # @pytest.mark.testrail("S57581.C52200940")  
    # def test_01_hpx_rebranding_C52200940(self):
    #     self.fc.select_device()
    #     self.fc.fd["devices_support_pc_mfe"].click_manual_guided_btn()
    #     self.__verify_redirect_link("manual_guided", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/model/2100971157")

    # def test_02_hpx_rebranding(self):
    #     self.fc.select_device()
    #     self.fc.fd["devices_support_pc_mfe"].click_service_center_btn()  
    #     self.__verify_redirect_link("service_center", "https://support.hp.com/", "/help/service-center", False)

    # def test_03_hpx_rebranding(self):
    #     self.fc.select_device()
    #     self.fc.fd["devices_support_pc_mfe"].click_virtual_repair_center_btn()  
    #     self.__verify_redirect_link("virtual_repair_center", "https://support.hp.com/", "/help/repair?jumpid=in_r11839_us/en/repr/hpsa", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52200939")  
    def test_04_hpx_rebranding_C52200939(self):
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_support_center_btn()
        self.__verify_redirect_link("product_support_center","https://support.hp.com/", "https://support.hp.com/us-en/product/details/model/2100971157")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977535")  
    def test_05_hpx_rebranding_C51977535(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977535
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_community_btn()
        self.__verify_redirect_link("community", "https://h30434.www3.hp.com/", "https://h30434.www3.hp.com/t5/Notebooks/ct-p/Notebook")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977576")  
    def test_06_hpx_rebranding_C51977576(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977576
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977573")
    def test_07_hpx_rebranding_C51977573(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977573
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()
        assert self.fc.verify_hp_id_sign_in(self.web_driver) is not False

    # @pytest.mark.testrail("S57581.C52215070")  
    # def test_08_hpx_rebranding_C52215070(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52215070
    #     """
    #     self.fc.select_device()
    #     time.sleep(10)
    #     self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()
    #     self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")
    #     self.fc.fd["devices_support_pc_mfe"].click_feedback_link()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("We appreciate your feedback!") == True

    # @pytest.mark.testrail("S57581.C52216156")       
    # def test_09_hpx_rebranding_C52216156(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52216156
    #     """
    #     self.fc.select_device()
    #     time.sleep(10)
    #     self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()
    #     self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")    
    #     self.fc.fd["devices_support_pc_mfe"].click_startover_link()  
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("Would you like to start over?") == True

    # @pytest.mark.testrail("S57581.C52216157")  
    # def test_10_hpx_rebranding_C52216157(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52216157
    #     """
    #     self.fc.select_device()
    #     time.sleep(10)
    #     self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()
    #     self.fc.fd["devices_support_pc_mfe"].verify_va_message("How can I assist you?")    
    #     self.fc.fd["devices_support_pc_mfe"].click_privacy_link()
    #     self.__verify_redirect_link("privacy_link", "https://www.hp.com/", "privacy/privacy-central.html", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    def test_11_hpx_rebranding(self):
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        self.fc.click_profile_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_device_add_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_add_device_page_title() == "Add a device"
        # self.__verify_redirect_link("hp_suppot", "https://support.hp.com/us-en/dashboard", "https://support.hp.com/us-en/dashboard")    

    # @pytest.mark.testrail("S57581.C51977734")  
    # def test_12_hpx_rebranding_C51977734(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/51977734
    #     """
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.select_country('KR')
    #     self.fc.fd["devices_support_pc_mfe"].click_kakaotalk_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("kakao_talk", "https://support.hp.com/", "https://support.hp.com/kr-ko/document/c02068647")  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977735")  
    def test_13_hpx_rebranding_C51977735(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977735
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        time.sleep(10)
        self.fc.select_country('CN')
        self.fc.fd["devices_support_pc_mfe"].click_webchat_btn()
        self.fc.select_country('US')
        self.__verify_redirect_link("webchat", "https://www.hp.com/", "https://www.hp.com/cn-zh/contact-hp/contact.html")  

    # @pytest.mark.testrail("S57581.C51977741")  
    # def test_14_hpx_rebranding_C51977741(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/51977741
    #     """
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.select_country('VN')
    #     self.fc.fd["devices_support_pc_mfe"].click_zalo_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("zalo", "https://id.zalo.me/", "https://id.zalo.me/account?", False)          

    # def test_15_hpx_rebranding_C51977743(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/51977743
    #     """
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.select_country('JP')
    #     self.fc.fd["devices_support_pc_mfe"].click_line_btn()
    #     self.fc.select_country('US')
    #     # self.__verify_redirect_link("line", "https://support.hp.com/", "https://support.hp.com/jp-ja/document", False)     

    # @pytest.mark.testrail("S57581.C51977750")  
    # def test_16_hpx_rebranding_C51977750(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/51977750
    #     """
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.select_country('AU')
    #     self.fc.fd["devices_support_pc_mfe"].click_whatsapp_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("whatsapp", "https://web.whatsapp.com/", "https://web.whatsapp.com/")           

    # def test_17_hpx_rebranding_C52121831(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52121831
    #     """
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.select_country("JP")    
    #     self.fc.fd["devices_support_pc_mfe"].click_line_btn()
    #     self.fc.select_country("US")
    #     self.__verify_redirect_link("line", "https://support.hp.com/", "https://support.hp.com/jp-ja/document", False) 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977404")
    def test_18_hpx_rebranding_C51977404(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977404
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_find_repair_center_btn()  
        self.__verify_redirect_link("service_center", "https://support.hp.com/", "/help/service-center", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977423")
    def test_19_hpx_rebranding_C51977423(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977423
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_virtual_repair_center_btn()
        self.__verify_redirect_link("virtual_repair_center", "https://support.hp.com/", "https://support.hp.com/us-en/help/repair?jumpid=in_r11839_us/en/repr/hpsa", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52200940")
    def test_20_hpx_rebranding_C52200940(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52200940 
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_manual_guided_btn()
        self.__verify_redirect_link("manual_guided", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/model/2100971157")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59372869") 
    def test_21_hpx_rebranding_C59372869(self):
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country("CN")  
        time.sleep(10)
        self.fc.select_device()
        self.__click_contact_us_btn()     
        assert self.fc.fd["devices_support_pc_mfe"].get_country() == "China"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
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

    def __click_contact_us_btn(self):
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()

    def __click_top_profile_icon(self):
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_top_profile_icon()

    def __click_support_option(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)      

    def __verify_redirect_link(self, web_page, url_contains, url_expect, full_match=True):
        time.sleep(10)
        self.web_driver.wdvr.switch_to.window(self.web_driver.wdvr.window_handles[-1])
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        self.web_driver.wdvr.close()
        if full_match:
            assert current_url == url_expect
        else:
            assert url_expect in current_url
    
    def __close_all_windows(self):
        if len(self.web_driver.wdvr.window_handles) > 1:
            for i in range(len(self.web_driver.wdvr.window_handles)) :
                if (i != 0):
                    self.web_driver.wdvr.switch_to.window(self.web_driver.wdvr.window_handles[i])
                    self.web_driver.wdvr.close()

