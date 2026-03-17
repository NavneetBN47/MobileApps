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
class Test_Suite_CCLS2(object):
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
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 244)
        self.__set_prefered_language("en-US")
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201228")  
    def test_01_hpx_rebranding_C52201228(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201228
        """
        self.__start_HPX()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.fc.fd["devices_support_pc_mfe"].click_find_repair_center_btn()
        self.__verify_redirect_link("service_center", "https://support.hp.com/", "/help/service-center", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201230")  
    def test_02_hpx_rebranding_C52201230(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201230
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.fc.fd["devices_support_pc_mfe"].click_product_support_center_btn()
        self.__verify_redirect_link("product_support_center","https://support.hp.com/", "https://support.hp.com/us-en/product/details/model", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201231")  
    def test_03_hpx_rebranding_C52201231(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201231
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.fc.fd["devices_support_pc_mfe"].click_manual_guided_btn()
        self.__verify_redirect_link("manual_guided", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/model", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201233")  
    def test_04_hpx_rebranding_C52201233(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201233
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.__click_contact_us_btn()   
        assert self.fc.fd["devices_support_pc_mfe"].verify_country_list() == True 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201234")  
    def test_05_hpx_rebranding_C52201234(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201234
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.fc.fd["devices_support_pc_mfe"].click_virtual_repair_center_btn()
        self.__verify_redirect_link("virtual_repair_center", "https://support.hp.com/", "/help/repair?jumpid=in_r11839_us/en/repr/hpsa", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52200937")  
    def test_06_hpx_rebranding_C52200937(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52200937
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_find_repair_center_btn()
        self.__verify_redirect_link("service_center", "https://support.hp.com/", "/help/service-center", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52200938")  
    def test_07_hpx_rebranding_C52200938(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52200938
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_virtual_repair_center_btn()
        self.__verify_redirect_link("virtual_repair_center", "https://support.hp.com/", "/help/repair?jumpid=in_r11839_us/en/repr/hpsa", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977425")  
    def test_08_hpx_rebranding_C51977425(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977425
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_product_support_center_btn()
        self.__verify_redirect_link("product_support_center","https://support.hp.com/", "https://support.hp.com/us-en/product/details/model", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977440")  
    def test_09_hpx_rebranding_C51977440(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977440
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:    
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_manual_guided_btn()
        self.__verify_redirect_link("manual_guided", "https://support.hp.com/", "https://support.hp.com/us-en/product/setup-user-guides/model", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C51977508")  
    def test_10_hpx_rebranding_C51977508(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/51977508
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.__click_contact_us_btn()   
        assert self.fc.fd["devices_support_pc_mfe"].verify_country_list() == True 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201240")  
    def test_11_hpx_rebranding_C52201240(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201240
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:    
            self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.__click_contact_us_btn()   
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_community_btn()
        self.__verify_redirect_link("community", "https://h30434.www3.hp.com/", "https://h30434.www3.hp.com/", False)

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201239")  
    def test_12_hpx_rebranding_C52201239(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201239
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.__click_contact_us_btn()   
        self.fc.select_country('US')
        self.fc.fd["devices_support_pc_mfe"].click_community_btn()
        self.__verify_redirect_link("community", "https://h30434.www3.hp.com/", "https://h30434.www3.hp.com/", False)

    # @pytest.mark.testrail("S57581.C52201332")  
    # def test_13_hpx_rebranding_C52201332(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201332
    #     """
    #     self.fc.select_device()
    #     self.__sign_in_HPX()
    #     if self.stack not in ["dev", "itg"]:
    #         self.fc.fd["devicesMFE"].click_device_card_by_index(1)
    #     self.__click_contact_us_btn()   
    #     self.fc.select_country('KR')
    #     self.fc.fd["devices_support_pc_mfe"].click_kakaotalk_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("kakao_talk", "https://support.hp.com/", "https://support.hp.com/kr-ko/document/c02068647")  

    # @pytest.mark.testrail("S57581.C52201331")  
    # def test_14_hpx_rebranding_C52201331(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201331
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.__click_top_profile_icon()
    #     self.__click_support_option()
    #     self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
    #     self.__click_contact_us_btn()   
    #     self.fc.select_country('KR')
    #     self.fc.fd["devices_support_pc_mfe"].click_kakaotalk_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("kakao_talk", "https://support.hp.com/", "https://support.hp.com/kr-ko/document/c02068647")  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201398")  
    def test_15_hpx_rebranding_C52201398(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201398
        """
        self.__start_HPX()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()   
        self.fc.select_country('CN')
        self.fc.fd["devices_support_pc_mfe"].click_webchat_btn()
        self.fc.select_country('US')
        self.__verify_redirect_link("webchat", "https://www.hp.com/", "https://www.hp.com/cn-zh/contact-hp/webchat-support.html?src=csptwechat")  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52201397")  
    def test_16_hpx_rebranding_C52201397(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52201397
        """
        self.__start_HPX()
        self.__sign_in_HPX()
        self.__click_top_profile_icon()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(3)
        self.__click_contact_us_btn()  
        self.fc.select_country('CN')
        self.fc.fd["devices_support_pc_mfe"].click_webchat_btn()
        self.fc.select_country('US')
        self.__verify_redirect_link("webchat", "https://www.hp.com/", "https://www.hp.com/cn-zh/contact-hp", False) 

    # @pytest.mark.testrail("S57581.C52201400")  
    # def test_17_hpx_rebranding_C52201400(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201400
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     if self.stack not in ["dev", "itg"]:
    #         self.fc.fd["devicesMFE"].click_device_card_by_index(1)
    #     self.__click_contact_us_btn()  
    #     self.fc.select_country('VN')
    #     self.fc.fd["devices_support_pc_mfe"].click_zalo_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("zalo", "https://id.zalo.me/", "https://id.zalo.me/account?", False)   

    # @pytest.mark.testrail("S57581.C52201399")  
    # def test_18_hpx_rebranding_C52201399(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201399
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.__click_top_profile_icon()
    #     self.__click_support_option()
    #     self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
    #     self.__click_contact_us_btn()  
    #     self.fc.select_country('VN')
    #     self.fc.fd["devices_support_pc_mfe"].click_zalo_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("zalo", "https://id.zalo.me/", "https://id.zalo.me/account?", False)  

    # @pytest.mark.testrail("S57581.C52201404")  
    # def test_19_hpx_rebranding_C52201404(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201404
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     if self.stack not in ["dev", "itg"]:
    #         self.fc.fd["devicesMFE"].click_device_card_by_index(1)
    #     self.__click_contact_us_btn()  
    #     self.fc.select_country('AU')
    #     self.fc.fd["devices_support_pc_mfe"].click_whatsapp_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("whatsapp", "https://web.whatsapp.com/", "https://web.whatsapp.com/")   

    # @pytest.mark.testrail("S57581.C52201402")  
    # def test_20_hpx_rebranding_C52201402(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201402
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.__click_top_profile_icon()
    #     self.__click_support_option()
    #     self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
    #     self.__click_contact_us_btn()
    #     self.fc.select_country('AU')
    #     self.fc.fd["devices_support_pc_mfe"].click_whatsapp_btn()
    #     self.fc.select_country('US')
    #     self.__verify_redirect_link("whatsapp", "https://web.whatsapp.com/", "https://web.whatsapp.com/")   

    # @pytest.mark.testrail("S57581.C52201408")  
    # def test_21_hpx_rebranding_C52201408(self):
    #     """ 
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201408
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     if self.stack not in ["dev", "itg"]:
    #         self.fc.fd["devicesMFE"].click_device_card_by_index(1)
    #     self.__click_contact_us_btn()  
    #     self.fc.select_country("JP")    
    #     self.fc.fd["devices_support_pc_mfe"].click_line_btn()
    #     self.fc.select_country("US")
    #     self.__verify_redirect_link("line", "https://support.hp.com/", "https://support.hp.com/jp-ja/document", False) 

    # @pytest.mark.testrail("S57581.C52201409")  
    # def test_22_hpx_rebranding_C52201409(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201409
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.__click_top_profile_icon()
    #     self.__click_support_option()
    #     self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
    #     self.__click_contact_us_btn()
    #     self.fc.select_country("JP")    
    #     self.fc.fd["devices_support_pc_mfe"].click_line_btn()
    #     self.fc.select_country("US")
    #     self.__verify_redirect_link("line", "https://support.hp.com/", "https://support.hp.com/jp-ja/document", False) 

    # @pytest.mark.testrail("S57581.C52201403")  
    # def test_23_hpx_rebranding_C52201403(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201403
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     if self.stack not in ["dev", "itg"]:
    #         self.fc.fd["devicesMFE"].click_device_card_by_index(1)
    #     self.__click_contact_us_btn()  
    #     self.fc.select_country("JP")    
    #     self.fc.fd["devices_support_pc_mfe"].click_twitter_btn()
    #     self.fc.select_country("US")
    #     self.__verify_redirect_link("twitter", "https://x.com/HPSupportJPN", "https://x.com/HPSupportJPN") 

    # @pytest.mark.testrail("S57581.C52201401")  
    # def test_24_hpx_rebranding_C52201401(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52201401
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.__click_top_profile_icon()
    #     self.__click_support_option()
    #     self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
    #     self.__click_contact_us_btn()
    #     self.fc.select_country("JP")    
    #     self.fc.fd["devices_support_pc_mfe"].click_twitter_btn()
    #     self.fc.select_country("US")
    #     self.__verify_redirect_link("twitter", "https://x.com/HPSupportJPN", "https://x.com/HPSupportJPN") 

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

    def __get_language_list(self):
        languages = self.registry.get_registry_value(
            "HKEY_CURRENT_USER\\Control Panel\\International\\User Profile", 
            "Languages"
            )
        if languages:
            languages = languages['stdout']
            languages = languages.strip()
            languages = languages.replace('\r\n', '')
            languages = languages.split('REG_MULTI_SZ')[1]
            languages = languages.strip()
            languages = languages.split('\\0')
            return languages
        return []
    
    def __set_language_list(self, language_list):
        reg_multi_sz_value = "@(" + ",".join([f'"{lang}"' for lang in language_list]) + ")"
        path = self.registry.format_registry_path("HKEY_CURRENT_USER\\Control Panel\\International\\User Profile")
        key_name = "Languages"
        key_value = reg_multi_sz_value
        self.driver.ssh.send_command('Set-Itemproperty -path \"{}\" -Name \"{}\" -Value {}'.format(path, key_name, key_value), raise_e=False)

    def __set_prefered_language(self, language):
        language_list = self.__get_language_list()
        if language in language_list:
            language_list.remove(language)
            language_list.insert(0, language)
        self.__set_language_list(language_list)

    def __close_all_windows(self):
        if len(self.web_driver.wdvr.window_handles) > 1:
            for i in range(len(self.web_driver.wdvr.window_handles)) :
                if (i != 0):
                    self.web_driver.wdvr.switch_to.window(self.web_driver.wdvr.window_handles[i])
                    self.web_driver.wdvr.close()
