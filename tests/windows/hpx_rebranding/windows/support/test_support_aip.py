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
class Test_Suite_AIP(object):
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
        self.fc.initial_hpx_support_env()
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59698638")
    def test_01_hpx_rebranding_C59698638(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59698638
        """     
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].click_aip_help_with_plan_btn()
        self.__verify_redirect_link("HPALLINPLAN", "https://support.hp.com/", "https://support.hp.com/us-en/service/all-in-plan/2101795773/yourhpallinplan")
        self.fc.fd["devices_support_pc_mfe"].click_aip_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_card() is True, "Contact Us page is not displayed"   

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59698644")
    def test_02_hpx_rebranding_C59698644(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59698644
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].click_aip_contact_us_btn()
        self.fc.fd["devices_support_pc_mfe"].click_speak_agent_btn()
        self.fc.fd["devices_support_pc_mfe"].click_issue_type_selector()
        self.fc.fd["devices_support_pc_mfe"].select_issue_type_option_by_index(0)
        self.fc.fd["devices_support_pc_mfe"].input_issue_description("Auto test")
        self.fc.fd["devices_support_pc_mfe"].click_get_phone_number_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_phone_number_text() == "1-888-447-0148" 

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59698681")
    def test_03_hpx_rebranding_C59698681(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59698681
        """
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "CN")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 45)
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(0)
        assert self.fc.fd["devices_support_pc_mfe"].verify_aip_help_with_plan_btn() is False, "AIP Help with Plan button is displayed when it should not be"
        assert self.fc.fd["devices_support_pc_mfe"].verify_aip_contact_us_btn() is False, "AIP Contact Us button is displayed when it should not be"
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "GB")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 242)
        self.fc.select_device()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        assert self.fc.fd["devices_support_pc_mfe"].verify_aip_help_with_plan_btn() is False, "AIP Help with Plan button is displayed when it should not be"
        assert self.fc.fd["devices_support_pc_mfe"].verify_aip_contact_us_btn() is False, "AIP Contact Us button is displayed when it should not be"
        
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self, maxmized=False):
        self.fc.select_device()
        # self.fc.restart_app()
        # if maxmized:
        #     self.fc.maximize_window()
        # if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
        #     self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        # if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
        #     self.fc.fd["hpx_fuf"].click_accept_all_button()
        # if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
        #     self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        # if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
        #     self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self, maxmized=False, index=0):
        self.__start_HPX(maxmized=maxmized)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index(index)

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("dtodxte2eseponboarded100@yopmail.com", "P@ssw0rd", self.web_driver, sign_in_from_profile=sign_in_from_profile)

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
        