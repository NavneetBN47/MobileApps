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
class Test_Suite_VA_AIP_intents(object):
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
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C60030640")
    def test_01_hpx_rebranding_C60030640(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/60030640
        """     
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_aip_intents_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_page_title() == "What can we help you with?"
        assert self.fc.fd["devices_support_pc_mfe"].verify_what_is_hp_all_in_plan_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_trouble_logging_in_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_change_email_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_change_billing_info_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_change_shipping_address_btn() == True
        self.fc.fd["devices_support_pc_mfe"].click_show_more_aip_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_add_a_printer_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_where_is_my_paper_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_where_is_my_ink_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_account_error_message_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_cancel_my_account_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_others_aip_btn() == True
        self.fc.fd["devices_support_pc_mfe"].click_show_less_aip_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True, "Start Virtual Assist button is not displayed"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C60031355")
    def test_02_hpx_rebranding_C59892623(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/60031355
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_aip_intents_btn_text() == "HP All-In PlanReview your billing, subscriptions, and more"
        assert self.fc.fd["devices_support_pc_mfe"].get_printer_intents_btn_text() == "Printer Printer Solve paper jams, scan issues, and more Arrow Right"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C60031414")
    def test_03_hpx_rebranding_C60031414(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/60031414
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_intents_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True, "Start Virtual Assist button is not displayed"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C61957136")
    def test_04_hpx_rebranding_C61957136(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/61957136
        """
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "CN")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 45)
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_page_title() != "Select a category to get started"
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "GB")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 242)
        self.fc.select_device()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_page_title() != "Select a category to get started"
        
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self, maxmized=False):
        self.fc.restart_app()
        if maxmized:
            self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self, maxmized=False, index=0):
        self.__start_HPX(maxmized=maxmized)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index(index)

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("dtodxte2eseponboarded100@yopmail.com", "P@ssw0rd", self.web_driver, sign_in_from_profile=sign_in_from_profile)
        