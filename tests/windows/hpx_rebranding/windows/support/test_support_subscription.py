from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.powershell_wmi_utilities import PowershellWmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
import re

pytest.app_info = "HPX"
class Test_Suite_Subscription(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = PowershellWmiUtilities(cls.driver.ssh)

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
    @pytest.mark.testrail("S57581.C83274525")
    def test_01_hpx_rebranding_C83274525(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83274525
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(4)
        assert self.fc.fd["devices_support_pc_mfe"].get_subscription_info() == "Subscription"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C83274526")
    def test_02_hpx_rebranding_C83274526(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83274526
        """
        self.__add_device("TH45VF6216")
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
        assert self.fc.fd["devices_support_pc_mfe"].get_sign_in_to_view_coverage_status_text() == "Arrow Right"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C83274527")
    def test_03_hpx_rebranding_C83274527(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83274527
        """
        self.__add_device("TH45VF6216")
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
        self.fc.fd["devices_support_pc_mfe"].click_sign_in_to_view_coverage_status_text()
        self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, user_icon_click=False)'
        assert self.fc.fd["devices_support_pc_mfe"].get_subscription_not_associated_text() == "Subscription not associated with this account"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __select_device(self, maxmized=False, index=0):
        self.__start_HPX(maxmized=maxmized)  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("rxplatt22@gmail.com", "HP_@ll_in_ONE", self.web_driver, sign_in_from_profile=sign_in_from_profile)

    def __add_device(self, sn):
        self.fc.select_device()
        time.sleep(20)
        self.fc.click_profile_button()
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_device_add_btn()  
        self.fc.fd["devices_support_pc_mfe"].click_search_by_sn_button()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].input_sn(sn)
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_add_device_link()