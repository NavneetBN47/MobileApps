import pytest
from time import sleep
import logging
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_10_Privacy_Upgrade_Decline_All_Btn(object):
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

        if "Windows 11" not in cls.gotham_utility.verify_windows_version():
            pytest.skip("This Test only can be run on Windows 11 currently (GOTH-25938)")
        
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('start-process "ms-windows-store://home"')

        cls.version_info = {}

    def test_01_install_ms_store_hp_smart(self):
        """
        Install live build from Microsoft Store
        """    
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen(timeout=120)
        self.fc.go_home()

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_check_app_go_to_home_screen(self):
        """
        [Upgrade only]Click "Decline All" button on the welcome screen after upgrade, verify user is taken to home page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223910
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        # self.fc.change_stack_server(stack='stage', restart=False)
        self.driver.launch_app(launch_activity)
        self.welcome.verify_welcome_screen()
        self.welcome.click_decline_all_btn()
        self.home.verify_home_screen()

        self.version_info["actual_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Test build Version after upgrade - {}'.format(self.version_info["actual_app_version"]))