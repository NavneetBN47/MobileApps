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
class Test_Suite_Rebranding(object):
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

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C48559713")  
    # def test_01_hpx_rebranding_C48559713(self):
    #     """
    #     https://hp-testrail.external.hp.com//index.php?/cases/view/48559713
    #     """
    #     self.fc.set_featureflags({"support-x-va": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == False
    #     self.fc.set_featureflags({"support-x-va": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C48559684")  
    # def test_02_hpx_rebranding_C48559684(self):
    #     """
    #     https://hp-testrail.external.hp.com//index.php?/cases/view/48559684
    #     """
    #     self.fc.set_featureflags({"support-x-contact": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == False
    #     self.fc.set_featureflags({"support-x-contact": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C48558873")  
    # def test_03_hpx_rebranding_C48558873(self):
    #     """
    #     https://hp-testrail.external.hp.com//index.php?/cases/view/48558873
    #     """
    #     self.fc.set_featureflags({"devices-x-adddevice": True, "support-x-adddevice": False})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     self.fc.click_profile_button()
    #     time.sleep(5)
    #     self.fc.fd["devices_support_pc_mfe"].select_support_option()
    #     assert self.fc.fd["devices_support_pc_mfe"].get_add_device_btn_text() == "Go to support.hp.com"
    #     self.fc.set_featureflags({"devices-x-adddevice": True, "support-x-adddevice": True})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     self.fc.click_profile_button()
    #     time.sleep(5)
    #     self.fc.fd["devices_support_pc_mfe"].select_support_option()
    #     assert self.fc.fd["devices_support_pc_mfe"].get_add_device_btn_text() == "Add a device"

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C48931576")  
    # def test_04_hpx_rebranding_C48931576(self):
    #     """
    #     https://hp-testrail.external.hp.com//index.php?/cases/view/48931576
    #     """
    #     self.fc.set_featureflags({"support-x-warrantydetail": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_detail_btn() == False
    #     self.fc.set_featureflags({"support-x-warrantydetail": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_detail_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59372870")
    # def test_05_hpx_rebranding_C59372870(self):
    #     self.fc.set_featureflags({"support-x-core": True, "support-x-case": False})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False
    #     self.fc.set_featureflags({"support-x-core": True, "support-x-case": True})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59372966")
    def test_06_hpx_rebranding_C59372966(self):
        self.__set_featureflags(False)
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(True) == False
    
    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59372991")
    # def test_07_hpx_rebranding_C59372991(self):
    #     self.fc.set_featureflags({"support-x-devicedetails": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(True) == False
    #     self.fc.set_featureflags({"support-x-devicedetails": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59372999")
    # def test_08_hpx_rebranding_C59372999(self):
    #     self.fc.set_featureflags({"support-x-menu": False})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     # self.fc.fd["hpx_fuf"].click_accept_all_button()
    #     time.sleep(10)
    #     self.fc.click_profile_button()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == False
    #     self.fc.set_featureflags({"support-x-menu": True})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     # self.fc.fd["hpx_fuf"].click_accept_all_button()
    #     time.sleep(10)
    #     self.fc.click_profile_button()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == True

    @pytest.mark.require_stack(["dev", "itg", "production"])     
    @pytest.mark.testrail("S57581.C59373142")
    def test_09_hpx_rebranding_C59373142(self):
        self.__start_HPX()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(10)
        if self.stack in ["dev", "itg"]:
            assert len(self.fc.fd["devices_support_pc_mfe"].get_device_list()) / 2 == 2
        else:
            assert len(self.fc.fd["devices_support_pc_mfe"].get_device_list()) / 2 == 4

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373147")
    def test_10_hpx_rebranding_C59373147(self):
        self.__start_HPX()
        time.sleep(10)
        self.fc.click_profile_button()
        self.__sign_in_HPX(sign_in_from_profile=True)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(10)
        if self.stack in ["dev", "itg"]:
            assert len(self.fc.fd["devices_support_pc_mfe"].get_device_list()) / 2 == 2
        else:
            assert len(self.fc.fd["devices_support_pc_mfe"].get_device_list()) / 2 == 4

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373133")
    def test_11_hpx_rebranding_C59373133(self):
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.select_country('US')
        self.fc.select_country("CN")
        self.fc.select_country("JP")
        self.fc.select_country("KR")
        self.fc.select_country("US")

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59373130")
    # def test_12_hpx_rebranding_C59373130(self):
    #     self.fc.set_featureflags({"support-x-adddevice": False, "support-x-weblink": False})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     time.sleep(10)
    #     self.fc.click_profile_button()
    #     self.fc.fd["devices_support_pc_mfe"].select_support_option()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_add_device_btn() == False
    #     self.fc.set_featureflags({"support-x-adddevice": False, "support-x-weblink": True})
    #     self.fc.restart_app()
    #     self.fc.maximize_window()
    #     self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
    #     time.sleep(10)
    #     self.fc.click_profile_button()
    #     self.fc.fd["devices_support_pc_mfe"].select_support_option()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_add_device_btn() == True     

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373149")
    def test_13_hpx_rebranding_C59373149(self):
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_detail_btn() == True       

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373153")
    def test_14_hpx_rebranding_C59373153(self):
        self.__remove_file()
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        # self.fc.fd["hpx_fuf"].click_accept_all_button()
        time.sleep(10)
        self.fc.click_profile_button()
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].verify_add_device_btn() == True     

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373171")
    def test_15_hpx_rebranding_C59373171(self):
        self.__remove_file()
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True       

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373174")
    def test_16_hpx_rebranding_C59373174(self):
        self.__remove_file()
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373259")
    def test_17_hpx_rebranding_C59373259(self):
        self.__remove_file()
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(False) == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373348")
    def test_18_hpx_rebranding_C59373348(self):
        self.__remove_file()
        self.fc.restart_app()
        self.fc.maximize_window()
        # self.fc.fd["hpx_fuf"].click_continue_as_guest_btn()
        # self.fc.fd["hpx_fuf"].click_accept_all_button()
        time.sleep(10)
        self.fc.click_profile_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C52200942")  
    def test_19_hpx_rebranding_C52200942(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52200942
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        self.fc.select_country('US')
        assert self.fc.fd["devices_support_pc_mfe"].verify_country_list() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59373349")
    def test_20_hpx_rebranding_C59373349(self):
        """
        https://hp-jira.external.hp.com/browse/HPXAPPS-29154
        """
        self.__start_HPX(maximize=False)
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index()
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].send_key_to_support_card()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_card(True) == True
        self.__click_profile_btn()
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].send_key_to_support_option()
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_option() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59373350")
    # def test_21_hpx_rebranding_C59373350(self):
    #     """
    #     https://hp-jira.external.hp.com/browse/HPXSUP-4124
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.fc.set_featureflags({"support-x-phone": False})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()
    #     #https://support.hp.com/us-en/contact/product/hp-probook-445-14-inch-g9-notebook-pc/2100971150/model/2100971157?sku=61K71AA
    #     if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
    #         self.__verify_redirect_link("call_an_agent", "https://support.hp.com",  "https://support.hp.com/us-en/contact", False)
    #         assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == False
    #     self.fc.set_featureflags({"support-x-phone": True})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn() 
    #     if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
    #         assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # @pytest.mark.testrail("S57581.C59373351")
    # def test_22_hpx_rebranding_C59373351(self):
    #     """
    #     https://hp-jira.external.hp.com/browse/HPXSUP-4125
    #     """
    #     self.__start_HPX()
    #     self.__sign_in_HPX()
    #     self.fc.set_featureflags({"support-x-chat": False})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
    #     if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
    #         assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == False
    #     self.fc.set_featureflags({"support-x-chat": True})
    #     self.fc.select_device()
    #     self.__click_contact_us_btn()
    #     self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()
    #     if not self.fc.fd["devices_support_pc_mfe"].verify_support_center_operating_hours_title():
    #         assert self.fc.fd["devices_support_pc_mfe"].verify_create_case_profile_name() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_23_hpx_rebranding(self):
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-oscheck": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_run_system_test_btn() == False
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-oscheck": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_run_system_test_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_24_hpx_rebranding(self):
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == False
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-performancetuneup": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_optimize_performance_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_25_hpx_rebranding(self):
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_check_audio_btn() == False
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-audiocheck": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_check_audio_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_26_hpx_rebranding(self):
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-hardwarediagnostics": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_run_hardware_diagnostic_btn() == False
    #     self.fc.set_featureflags({"support-x-diagnostic": True, "support-x-diagnostic-hardwarediagnostics": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_run_hardware_diagnostic_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_27_hpx_rebranding(self):
    #     self.fc.set_featureflags({"pc-x-specifications": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_product_info_btn() == False
    #     self.fc.set_featureflags({"pc-x-specifications": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_support_pc_mfe"].verify_product_info_btn() == True

    # @pytest.mark.require_stack(["dev", "itg", "production"]) 
    # def test_28_hpx_rebranding(self):
    #     self.fc.set_featureflags({"support-x-diagnostic-performancetuneup-systemcontrol": False})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() == False
    #     self.fc.set_featureflags({"support-x-diagnostic-performancetuneup-systemcontrol": True})
    #     self.fc.select_device()
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    def test_29_hpx_rebranding_C59373349(self):
        """
        https://hp-jira.external.hp.com/browse/HPXAPPS-50030
        """
        self.__start_HPX(maximize=False)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].right_click_device_card(0) 
        assert self.fc.fd["devices_support_pc_mfe"].verify_submenu_view() == False

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
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()   
        self.fc.fd["devices_support_pc_mfe"].click_otherspc_btn()    

    def __select_device(self):
        self.__start_HPX()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

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
