"""
 This test suite is designed to automate the testing of the process of searching for
 and installing the HP Smart app from the Microsoft Store.
 This test suite includes methods to set up the test environment, search for the app, install it,
 and verify that the app is installed and configured correctly.
"""
from time import sleep
import pytest
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_04_Search_And_Install_App_On_MS_Store(object):
    """This class is defined to contain test cases related to searching for
    and installing the HP Smart app from the Microsoft Store.
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.search_app = 'HP Smart'
        cls.install_app_path = install_app
        # Defining the stack variable to use in the test cases
        cls.stack = request.config.getoption("--stack")
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.sp = cls.sf.sp

        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('Stop-Process -Name "*chrome*"')
        sleep(2)
        cls.driver.ssh.send_command('start-process "ms-windows-store://home"')
        sleep(2)
        cls.driver.ssh.send_command(
            'Get-AppXPackage -AllUsers -Name Microsoft.Services.Store* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($_.InstallLocation)\AppXManifest.xml” -Verbose}')


    def test_01_install_ms_store_hp_smart(self):
        """
        Install app from MS store, verify result

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16929209
        """
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()

    def test_02_install_latest_build(self):
        """
        This test case verifies the installation of the latest build of the HP Smart app
        by removing the existing app and running the installation script.
        """
        self.sf.settings_and_store_cleanup()
        self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(self.stack, restart=False)