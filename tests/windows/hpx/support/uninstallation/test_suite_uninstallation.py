import time
import re
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Uninstallation(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session        
        cls.fc = FlowContainer(cls.driver)  
        cls.sf = SystemFlow(cls.driver) 
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.sp = cls.sf.sp

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "speak.json")
        
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def closeapp():
            self.navigation_panel.click_close_btn()
        request.addfinalizer(closeapp)     

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32246647")  
    def test_01_click_uninstall(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32246647
        """
        self.fc.close_app()
        self.sf.click_start_btn()
        self.sf.click_search_box()
        time.sleep(3)
        self.sf.enter_text_search_box()
        self.sf.verify_win_hp_right_opt_display()
        self.sf.click_win_app_uninstall_btn()
        if self.sf.verify_win_app_uninstall_info_dialog():
            self.sf.click_win_app_uninstall_info_btn()
        time.sleep(20)
        assert self.sp.check_hp_app_exist("C:/Program Files (x86)/HP/HPX Support") is False

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32246723")  
    def test_02_click_uninstall(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32246723
        """
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")
        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            if self.fc.fd["hp_registration"].verify_skip_button_show():
                self.fc.fd["hp_registration"].click_skip_button()
            if self.fc.fd["hp_privacy_setting"].verify_accept_button_show():
                self.fc.fd["hp_privacy_setting"].click_accept_all_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        self.sf.click_start_btn()
        self.sf.click_search_box()
        time.sleep(3)
        self.sf.enter_text_search_box()
        self.sf.verify_win_hp_right_opt_display()
        self.sf.click_win_app_uninstall_btn()
        if self.sf.verify_win_app_uninstall_info_dialog():
            self.sf.click_win_app_uninstall_info_btn()
        time.sleep(20)
        assert self.sp.check_hp_app_exist("C:/Program Files (x86)/HP/HPX Support") is False   