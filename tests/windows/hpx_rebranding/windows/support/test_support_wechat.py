from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
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
class Test_Suite_Wechat(object):
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
    @pytest.mark.testrail("S57581.C72731845")
    def test_01_hpx_rebranding_C72731845(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731845
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731846")
    def test_02_hpx_rebranding_C72731846(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731846
        """
        self.__set_region("US", 244)
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731847")
    def test_03_hpx_rebranding_C72731847(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731847
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_hp_service_with_wechat_btn() is not False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731848")
    def test_04_hpx_rebranding_C72731848(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731848
        """
        self.__set_region("US", 244)
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_hp_service_with_wechat_btn() is False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731849")
    def test_05_hpx_rebranding_C72731849(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731849
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        assert "HP Service with WeChat" in self.fc.fd["devices_support_pc_mfe"].get_hp_service_list()[1].text

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731852")
    def test_06_hpx_rebranding_C72731852(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731852
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_hp_service_with_wechat_btn()
        assert self.process_util.check_process_running("Weixin.exe") is True
        self.process_util.kill_process("Weixin.exe")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731854")
    def test_07_hpx_rebranding_C72731854(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731854
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_hp_service_with_wechat_btn()
        assert self.process_util.check_process_running("Weixin.exe") is True
        self.process_util.kill_process("Weixin.exe")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C72731855")
    def test_08_hpx_rebranding_C72731855(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/72731855
        """
        self.__set_region("CN", 45)
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_support_pc_mfe"].click_hp_service_with_wechat_btn()
        self.fc.fd["devices_support_pc_mfe"].click_redirect_failure_confirm_btn()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __set_region(self, country_code, country_nation):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\\International\\Geo", "Nation", country_nation)

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

    def __select_device(self, maxmized=False):
        self.__start_HPX(maxmized=maxmized)

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)       