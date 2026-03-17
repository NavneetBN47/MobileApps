import pytest
from time import sleep
import logging
import random
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_01_Home_Upgrade_Tiles(object):
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
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        cls.stack = request.config.getoption("--stack")

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
        self.welcome.verify_welcome_screen()
        self.fc.go_home()

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_turn_off_shortcuts_tile(self):
        """
        (+)Disable the Shortcuts from the personalized tile and upgrade the app from latest live build to latest test build, verify Shortcuts is still disable for test build

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16929163
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()

        self.per_tiles.click_tile_toggle("shortcuts_toggle")
        self.per_tiles.verify_personalize_tile_off("shortcuts_toggle")

        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_menu_btn()

    def test_03_check_tiles_latest_hp_smart(self):
        """
        (+)Disable the Shortcuts from the personalized tile and upgrade the app from latest live build to latest test build, verify Shortcuts is still disable for test build

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16929163
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(stack=self.stack, restart=False)
        self.driver.launch_app(launch_activity)
        sleep(2)
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        if self.stack != "production":
            self.welcome.verify_welcome_screen()
            self.fc.go_home()
        else:
            assert self.welcome.verify_welcome_screen(timeout=10, raise_e=False) is False
            self.home.verify_home_screen()
        self.home.verify_shortcuts_tile(invisible=True)