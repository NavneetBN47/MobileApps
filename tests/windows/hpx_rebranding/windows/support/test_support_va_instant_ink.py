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
class Test_Suite_VA_Instant_Ink(object):
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
    @pytest.mark.testrail("S57581.C73252874")
    def test_01_hpx_rebranding_C73252874(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252874
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_what_is_instant_ink_plan_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252875")
    def test_02_hpx_rebranding_C73252875(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252875
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_cartridge_troubleshooting_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252876")
    def test_03_hpx_rebranding_C73252876(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252876
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_change_credit_card_info_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252877")
    def test_04_hpx_rebranding_C73252877(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252877
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_my_bill_was_not_what_i_expected_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252878")
    def test_05_hpx_rebranding_C73252878(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252878
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_page_count_explanations_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252879")
    def test_06_hpx_rebranding_C73252879(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252879
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_account_related_errors_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252880")
    def test_07_hpx_rebranding_C73252880(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252880
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_print_quality_issues_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252881")
    def test_08_hpx_rebranding_C73252881(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252881
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_connect_printer_message_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252883")
    def test_09_hpx_rebranding_C73252883(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252883
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_cartridge_cannot_be_used_until_printer_is_enrolled_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252884")
    def test_10_hpx_rebranding_C73252884(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252884
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_change_shipping_address_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252885")
    def test_11_hpx_rebranding_C73252885(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252885
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_change_to_a_different_plan_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252886")   
    def test_12_hpx_rebranding_C73252886(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/73252886
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(1)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_show_more_instant_ink_btn()
        self.fc.fd["devices_support_pc_mfe"].click_trouble_logging_in_to_my_instant_ink_account_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_title() == "Virtual Assistant"

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

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("iiqa_zy90+251210b@outlook.com", "Aio1test!", self.web_driver, sign_in_from_profile=sign_in_from_profile)