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
class Test_Suite_Contact_Option(object):
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
    @pytest.mark.testrail("S57581.C59696586")
    def test_01_hpx_rebranding_C59696586(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59696586
        """     
        self.fc.select_device()
        self.__click_contact_us_btn()
        self.fc.select_country("US")
        element_chat = self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn()
        element_call = self.fc.fd["devices_support_pc_mfe"].verify_speak_agent_btn()
        element_community = self.fc.fd["devices_support_pc_mfe"].verify_community_btn()
        assert element_call.location['y'] > element_chat.location['y'], "Speak Agent button is not below Chat Agent button"
        assert element_community.location['y'] > element_call.location['y'], "Community button is not below Speak Agent button"

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59696977")
    def test_02_hpx_rebranding_C59696977(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59696977
        """
        self.fc.select_device()
        element_manual_guided = self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn()
        element_find_repair = self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn()
        element_virtual_repair = self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn()
        element_product_support = self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn()
        assert element_find_repair.location['y'] > element_manual_guided.location['y'], "Find Repair Center button is not below Manual Guided button"
        assert element_virtual_repair.location['y'] > element_find_repair.location['y'], "Virtual Repair Center button is not below Find Repair Center button"
        assert element_product_support.location['y'] > element_virtual_repair.location['y'], "Product Support Center button is not below Virtual Repair Center button"

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

    def __click_contact_us_btn(self):
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()

        