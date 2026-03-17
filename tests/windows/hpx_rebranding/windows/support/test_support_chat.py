from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
import datetime
import holidays
import pytz

pytest.app_info = "HPX"
class Test_Suite_Chat(object):
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
    @pytest.mark.testrail("S57581.C59446235")  
    def test_01_hpx_rebranding_C59446235(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446235
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_profile_email() == "shhpxtest005@outlook.com"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446236")  
    def test_02_hpx_rebranding_C59446236(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446236
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        assert self.fc.fd["devices_support_pc_mfe"].get_issue_type_option_count() / 2 == 4    

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446241")  
    def test_03_hpx_rebranding_C59446241(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446241
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].verify_chat_now_btn_enabled() == "false"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446243")
    def test_04_hpx_rebranding_C59446243(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446243
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].verify_chat_now_btn_enabled() == "false"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446245")
    def test_05_hpx_rebranding_C59446245(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446245
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        
        # Create a string with 1001 characters
        thousand_chars = "A" * 1024
        one_more_char = thousand_chars + "Z"  # 1001 characters
        
        # Try to input 1001 characters
        self.fc.fd["devices_support_pc_mfe"].input_issue_description(one_more_char)
        time.sleep(10)

        # Get the actual text entered in the field
        actual_text = self.fc.fd["devices_support_pc_mfe"].get_issue_description()

        # Verify if text is limited to 1000 characters
        assert len(actual_text) == 1024, f"Text length is {len(actual_text)}, expected 1024"
        assert actual_text == thousand_chars, "Text was not properly limited to 1024 characters"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446246")
    def test_06_hpx_rebranding_C59446246(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446246
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].verify_chat_now_btn_enabled() == "true"  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59446248")
    def test_07_hpx_rebranding_C59446248(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446248
        """    
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].clear_issue_description()
        assert self.fc.fd["devices_support_pc_mfe"].get_issue_description_tip() == "Tell us about your issue in a few words…"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59446249")
    def test_08_hpx_rebranding_C59446249(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446249
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        self.__click_chat_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_chat_now_btn()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].verify_endsession_btn_enabled() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C559446251")
    def test_09_hpx_rebranding_C59446251(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59446251
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59696050")
    def test_10_hpx_rebranding_C59696050(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59696050
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country("IE")   
        time.sleep(10)
        if self.__is_support_time(country='IE', timeZoneOffSet='+0100'):
            assert self.fc.fd["devices_support_pc_mfe"].get_chat_with_agent_description() == "The fastest option" 

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C59696068")
    def test_11_hpx_rebranding_C59696068(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59696068
        """
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country("IE")
        time.sleep(10)
        if not self.__is_support_time(country='IE', timeZoneOffSet='+0100'):
            assert self.fc.fd["devices_support_pc_mfe"].get_chat_with_agent_description() == "The support center is closed." 
        
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

    def __click_chat_agent_btn(self):
        self.fc.select_country("US")
        self.fc.fd["devices_support_pc_mfe"].click_chat_agent_btn()

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)      
        
    def __is_support_time(self, now=None, country='US', timeZoneOffSet='+0000'):
        """
        Returns True if current time is Monday-Friday, 8:00-18:00, and not a public holiday.
        :param now: datetime.datetime object (default: now)
        :param country: country code for holidays (default: 'US')
        :param timeZoneOffSet: string like '+0100'
        """
        if now is None:
            # Get UTC time and apply offset
            now_utc = datetime.datetime.utcnow()
            # Parse offset
            sign = 1 if timeZoneOffSet[0] == '+' else -1
            hours = int(timeZoneOffSet[1:3])
            minutes = int(timeZoneOffSet[3:5])
            delta = datetime.timedelta(hours=sign*hours, minutes=sign*minutes)
            now = now_utc + delta

        if now.weekday() >= 5:
            return False
        if not (8 <= now.hour < 18):
            return False
        holiday_list = holidays.country_holidays(country)
        if now.date() in holiday_list:
            return False
        return True
