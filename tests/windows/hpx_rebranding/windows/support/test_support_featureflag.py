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
class Test_Suite_FeatureFlag(object):
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
        self.__remove_file()
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796060")  
    def test_01_hpx_rebranding_C63796060(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63796060
        """
        self.fc.set_featureflags({"support-x-core": True, "support-x-case": False})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796061")  
    def test_02_hpx_rebranding_C63796061(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63796061
        """
        self.fc.set_featureflags({"support-x-core": False, "support-x-case": True})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796062")  
    def test_03_hpx_rebranding_C63796062(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796062
        """
        self.fc.set_featureflags({"devices-x-adddevice": True, "support-x-adddevice": True})
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        self.fc.click_profile_button()
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].get_add_device_btn_text() == "Add a device"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796063")  
    def test_04_hpx_rebranding_C63796063(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796063
        """
        self.fc.set_featureflags({"devices-x-adddevice": True, "support-x-adddevice": False})
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        time.sleep(10)
        self.fc.click_profile_button()
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].get_add_device_btn_text() == "Go to support.hp.com"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796064")
    def test_05_hpx_rebranding_C63796064(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796064
        """
        self.fc.set_featureflags({"support-x-core": True, "support-x-case": True})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796065")
    def test_06_hpx_rebranding_C63796065(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796065
        """
        self.fc.set_featureflags({"support-x-core": True, "support-x-case": False})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796232")  
    def test_07_hpx_rebranding_C63796232(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796232
        """
        self.fc.set_featureflags({"support-x-contact": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796360")  
    def test_08_hpx_rebranding_C63796360(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796360
        """
        self.fc.set_featureflags({"support-x-contact": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796367")
    def test_09_hpx_rebranding_C63796367(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796367
        """
        self.fc.set_featureflags({"support-x-devicedetails": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796368")
    def test_10_hpx_rebranding_C63796368(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796368
        """
        self.fc.set_featureflags({"support-x-devicedetails": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(True) == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796369")
    def test_11_hpx_rebranding_C63796369(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796369
        """
        self.fc.set_featureflags({"support-x-menu": True})
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        time.sleep(10)
        self.fc.click_profile_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796370")
    def test_12_hpx_rebranding_C63796370(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796370
        """
        self.fc.set_featureflags({"support-x-menu": False})
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        time.sleep(10)
        self.fc.click_profile_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796371")  
    def test_13_hpx_rebranding_C63796371(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796371
        """
        self.fc.set_featureflags({"support-x-va": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796387")  
    def test_14_hpx_rebranding_C63796387(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796387
        """
        self.fc.set_featureflags({"support-x-va": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796643")  
    def test_15_hpx_rebranding_C63796643(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796643
        """
        self.fc.set_featureflags({"support-x-warrantydetail": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_detail_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796771")  
    def test_16_hpx_rebranding_C63796771(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796771
        """
        self.fc.set_featureflags({"support-x-warrantydetail": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_detail_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796772")
    def test_17_hpx_rebranding_C63796772(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796772
        """
        self.fc.set_featureflags({"support-x-chat": True})
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
        if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
            assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796773")
    def test_18_hpx_rebranding_C63796773(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796773
        """
        self.fc.set_featureflags({"support-x-chat": False})
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
        if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
            assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796774")
    def test_19_hpx_rebranding_C63796774(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796774
        """
        self.fc.set_featureflags({"support-x-phone": True})
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn() 
        if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
            assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == True
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796775")
    def test_20_hpx_rebranding_C63796775(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796775
        """
        self.fc.set_featureflags({"support-x-phone": False})
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()
        if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
            # self.__verify_redirect_link("call_an_agent", "https://support.hp.com",  "https://support.hp.com/us-en/contact", False)
            assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == False

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __remove_file(self):
        self.fc.close_app()
        time.sleep(5)
        remote_artifact_path = "{}\\{}\\LocalState\\".format(
            w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if self.driver.ssh.check_directory_exist(remote_artifact_path, create=False, raise_e=False):
            self.driver.ssh.remove_file_with_suffix(remote_artifact_path, ".json") 
        if self.driver.ssh.check_directory_exist(remote_artifact_path, create=False, raise_e=False):
            self.driver.ssh.remove_file_with_suffix(remote_artifact_path, ".dat")
        # if self.driver.ssh.check_directory_exist(remote_artifact_path, create=False, raise_e=False):
        #     self.driver.ssh.remove_file_with_suffix(remote_artifact_path, ".db")
    
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self, maximize=True):
        self.fc.restart_app()
        if maximize:
            self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __click_profile_btn(self):
        time.sleep(10)
        self.fc.click_profile_button()

    def __click_top_profile_icon(self):
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_top_profile_icon()
    
    def __click_settings_option(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].select_settings_option()

    def __click_contact_us_btn(self):
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __select_device(self, index=0):
        self.fc.select_device()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index(index)

    def __sign_in_HPX(self, user_icon_click=True, sign_in_from_profile=False):
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=user_icon_click, sign_in_from_profile=sign_in_from_profile)      

    def __verify_redirect_link(self, web_page, url_contains, url_expect, full_match=True):
        webpage = web_page
        self.web_driver.wait_for_new_window(timeout=20)
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)  
        self.web_driver.wait_url_contains(url_contains, timeout=30)
        current_url = self.web_driver.get_current_url()
        self.web_driver.close_window(webpage)
        if full_match:
            assert current_url == url_expect
        else:
            assert url_expect in current_url

    def __set_featureflags(self, featureflags):
        self.fc.set_featureflags({"support-x-core": featureflags, 
                                  "support-x-devicedetails": featureflags,
                                  "support-x-va": featureflags,
                                  "support-x-case": featureflags,
                                  "support-x-contact": featureflags,
                                  "support-x-menu": featureflags,
                                  "support-x-warrantydetail": featureflags, 
                                  "support-x-weblink": featureflags,
                                  "support-x-adddevice": featureflags,
                                  "support-x-phone": featureflags,
                                  "support-x-chat": featureflags,
                                  "devices-x-adddevice": featureflags})
