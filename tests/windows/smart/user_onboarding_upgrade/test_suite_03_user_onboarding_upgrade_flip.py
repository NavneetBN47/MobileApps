import pytest
from time import sleep
import logging
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_User_Onboarding_Upgrade_Flip(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.search_app = 'HP Smart'

        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")
        
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)

        cls.version_info = {}

    def test_01_install_ms_store_hp_smart(self):
        """
        Install live build from Microsoft Store
        """
        self.sf.change_pc_region_to_flip_region()
        self.driver.ssh.send_command('start-process "ms-windows-store://home"')
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_install_latest_hp_smart(self):
        """
        (Flip) Upgrade app in SGP/HK, verify returned user (not signed in) is forced to signin/signup after app upgrade

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29903168
        """
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(stack=self.stack)
        self.welcome.verify_welcome_screen()
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.welcome.click_accept_all_btn()
        # OWS-69556:The OWS Flip value prop screen does NOT show after launching app for Flip region.
        self.ows_value_prop.verify_windows_ows_value_prop_screen(flip=True)
        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        assert self.home.verify_logged_in() is True

    def test_03_set_region_back_to_usa(self):
        self.sf.change_pc_region_to_us_region()
        self.fc.reset_hp_smart()