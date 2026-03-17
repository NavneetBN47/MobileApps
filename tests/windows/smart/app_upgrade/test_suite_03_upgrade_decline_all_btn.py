import pytest
from time import sleep
import logging
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_Upgrade_Decline_All_Btn(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.search_app = 'HP Smart'

        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]

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
        self.welcome.click_decline_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.select_native_value_prop_buttons(index=3)
        self.home.verify_home_screen()

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_check_no_welcome_screen(self):
        """
        Opt out from welcome screen then upgrade a new release with no changes in welcome screen, verify welcome screen does not show 
        -- Verify the Welcome screen does NOT display again when the App stack is the same.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17118333
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(stack='production', restart=False)
        self.driver.launch_app(launch_activity)
        assert self.welcome.verify_welcome_screen(timeout=10, raise_e=False) is False
        self.home.verify_home_screen()

        self.version_info["actual_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Test build Version after upgrade - {}'.format(self.version_info["actual_app_version"]))

    def test_03_check_privacy_preference_screen_off(self):
        """
        Opt out from welcome screen then upgrade a new release with no changes in welcome screen, verify welcome screen does not show
        -- Verify the options listed in "Manage my Privacy Preferences and observe" are off status.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17118333
        """
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.fc.check_toggle_status(self.privacy_preference.ADVERTISING, "privacy_close_toggle.png")
        logging.info('The options listed in Manage your HP Privacy Preferences screen are OFF status')
