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
class Test_Suite_Call(object):
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

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446208")  
    def test_01_hpx_rebranding_C59446208(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446208
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_profile_email() == "shhpxtest005@outlook.com"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446210")  
    def test_02_hpx_rebranding_C59446210(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446210
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        assert self.fc.fd["devices_support_pc_mfe"].get_issue_type_option_count()/2 == 4 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446218")  
    def test_03_hpx_rebranding_C59446218(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446218
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].verify_get_phone_number_btn_enabled() == "false"   

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446219")
    def test_04_hpx_rebranding_C59446219(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446219
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].verify_get_phone_number_btn_enabled() == "false"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446225")
    def test_05_hpx_rebranding_C59446225(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446225
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        
        # Create a string with 1001 characters
        thousand_chars = "A" * 1024
        one_more_char = thousand_chars + "Z"  # 1001 characters
        
        # Try to input 1001 characters
        self.fc.fd["devices_support_pc_mfe"].input_issue_description(one_more_char)

        # Get the actual text entered in the field
        actual_text = self.fc.fd["devices_support_pc_mfe"].get_issue_description()

        # Verify if text is limited to 1000 characters
        assert len(actual_text) == 1024, f"Text length is {len(actual_text)}, expected 1024"
        assert actual_text == thousand_chars, "Text was not properly limited to 1024 characters"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446227")
    def test_06_hpx_rebranding_C59446227(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446227
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].verify_get_phone_number_btn_enabled() == "true"  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446228")
    def test_07_hpx_rebranding_C59446228(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446228
        """    
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].clear_issue_description()
        assert self.fc.fd["devices_support_pc_mfe"].get_issue_description_tip() == "Tell us about your issue in a few words…"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59446230")
    def test_08_hpx_rebranding_C59446230(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446230
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_get_phone_number_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_phone_number_text() == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59446231")
    def test_09_hpx_rebranding_C59446231(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446231
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_get_phone_number_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_issue_type_text() == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59446234")
    def test_10_hpx_rebranding_C59446234(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446234
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_get_phone_number_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_issue_description_text() == True

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

    def __click_speak_agent_btn(self):
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)      

