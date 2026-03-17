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
class Test_Suite_Warranty(object):
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

    @pytest.mark.require_stack(["dev", "itg"])   
    @pytest.mark.testrail("S57581.C52152918")      
    def test_01_hpx_rebranding_C52152918(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52152918
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        assert "Active" in self.fc.fd["devices_support_pc_mfe"].get_warranty_status()

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C52156966")
    def test_02_hpx_rebranding_C52156966(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52156966
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        time.sleep(10)
        assert "Coverage expiring" in self.fc.fd["devices_support_pc_mfe"].get_warranty_status()

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C52156127")
    def test_03_hpx_rebranding_C52156127(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52156127
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(4)
        time.sleep(10)
        assert "Unknown" in self.fc.fd["devices_support_pc_mfe"].get_warranty_status()

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C52156125")
    def test_04_hpx_rebranding_C52156125(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52156125
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)
        assert "Unknown" in self.fc.fd["devices_support_pc_mfe"].get_warranty_status()

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
        self.fc.select_device()
        # if self.stack not in ["dev", "itg"]:
        # self.fc.fd["devicesMFE"].click_device_card_by_index()

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
         self.fc.sign_in("bubradeidifo-1342@yopmail.com", "1qaz@WSX", self.web_driver, sign_in_from_profile=sign_in_from_profile)      

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