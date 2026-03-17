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
class Test_Suite_FeatureFlag2(object):
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
    @pytest.mark.testrail("S57581.C63796777")
    def test_01_hpx_rebranding_C63796777(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796777
        """
        self.fc.set_featureflags({"support-x-core": True, "support-x-case": True})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796778")
    def test_02_hpx_rebranding_C63796778(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796778
        """
        self.fc.set_featureflags({"support-x-core": True, "support-x-case": False})
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796779")
    def test_03_hpx_rebranding_C63796779(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796779
        """
        self.fc.set_featureflags({"support-x-va-intent": True})
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_page_title() == "What can we help you with?"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796780")
    def test_04_hpx_rebranding_C63796780(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796780
        """
        self.fc.set_featureflags({"support-x-va-intent": False})
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63796781")
    def test_05_hpx_rebranding_C63796781(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63796781
        """
        self.fc.set_featureflags({"support-x-diagnostic": True})
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797037")
    def test_06_hpx_rebranding_C63797037(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797037
        """
        self.fc.set_featureflags({"support-x-diagnostic": False})
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797038")
    def test_07_hpx_rebranding_C63797038(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797038
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-oscheck": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_run_system_test_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797039")
    def test_08_hpx_rebranding_C63797039(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797039
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-oscheck": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_run_system_test_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797040")
    def test_09_hpx_rebranding_C63797040(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797040
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == True
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797168")
    def test_10_hpx_rebranding_C63797168(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797168
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == False
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797424")
    def test_11_hpx_rebranding_C63797424(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797424
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_check_audio_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797440")
    def test_12_hpx_rebranding_C63797440(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797440
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_check_audio_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797441")
    def test_13_hpx_rebranding_C63797441(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797441
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-hardwarediagnostics": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_run_hardware_diagnostic_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797442")
    def test_14_hpx_rebranding_C63797442(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797442
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-hardwarediagnostics": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_run_hardware_diagnostic_btn() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797443")
    def test_15_hpx_rebranding_C63797443(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797443
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck-audiocontrol": True})
        self.fc.select_device()
        self.fc.fd["devices_details_pc_mfe"].click_audio_control_card()
        assert self.fc.fd["devices_support_pc_mfe"].verify_audio_setting_check_audio_button() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797571")
    def test_16_hpx_rebranding_C63797571(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797571
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck-audiocontrol": False})
        self.fc.select_device()
        self.fc.fd["devices_details_pc_mfe"].click_audio_control_card()
        assert self.fc.fd["devices_support_pc_mfe"].verify_audio_setting_check_audio_button() == False
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797572")
    def test_17_hpx_rebranding_C63797572(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797572
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup-systemcontrol": True})
        self.fc.select_device()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["devices_support_pc_mfe"].verify_system_control_optimize_performance_button() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797573")
    def test_18_hpx_rebranding_C63797573(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797573
        """
        self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup-systemcontrol": False})
        self.fc.select_device()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["devices_support_pc_mfe"].verify_system_control_optimize_performance_button() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797574")
    def test_19_hpx_rebranding_C63797574(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797574
        """
        self.fc.set_featureflags({"pc-x-specifications": True})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_info_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63797575")
    def test_20_hpx_rebranding_C63797575(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63797575
        """
        self.fc.set_featureflags({"pc-x-specifications": False})
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_info_btn() == False

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C73400016")
    # def test_21_hpx_rebranding_C73400016(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/73400016
    #     """
    #     self.fc.set_featureflags({"support-x-update": True})
    #     self.fc.select_device()
    #     import pdb 
    #     pdb.set_trace()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_view_available_updates_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C73400017")
    # def test_22_hpx_rebranding_C73400017(self):
    #     """
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/73400017
    #     """
    #     self.fc.set_featureflags({"support-x-update": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_view_available_updates_btn() == False

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
        self.__start_HPX()
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
