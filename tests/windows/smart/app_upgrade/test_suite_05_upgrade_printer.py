import pytest
from time import sleep
import logging
from SAF.misc import saf_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_05_Upgrade_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.search_app = 'HP Smart'

        if "DunePrinterInfo" in str(cls.p.p_obj):
            cls.p.set_software_completion_state_to_completed()
        elif not cls.p.get_ows_setup_completed_status():
            pytest.skip("SKIP - The selected printer does not been set up completed!")

        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]

        if "Windows 11" not in cls.gotham_utility.verify_windows_version():
            pytest.skip("This Test only can be run on Windows 11 currently (GOTH-25938)")

        cls.login_info = ma_misc.get_hpid_account_info(stack="production", a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('start-process "ms-windows-store://home"')

        cls.version_info = {}
        cls.version_info["expected_app_version"] = cls.install_app_path[-10:]

    def test_01_install_ms_store_hp_smart(self):
        """
        Upgrade to the latest app as a returned user, verify "Set up" button does not show on main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17463972
        """    
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()        

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))

        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        self.fc.go_home()

        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_finish_setup_btn(invisible=True)
        
    def test_02_install_latest_hp_smart(self):
        """
        Upgrade to the latest app as a returned user, verify "Set up" button does not show on main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17463972
        """
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.version_info["actual_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Test build Version after upgrade - {}'.format(self.version_info["actual_app_version"]))

        self.fc.change_stack_server(stack='production', restart=False)
        self.driver.launch_app(launch_activity)
        assert self.welcome.verify_welcome_screen(timeout=10, raise_e=False) is False
        self.home.verify_home_screen()
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_finish_setup_btn(invisible=True)




