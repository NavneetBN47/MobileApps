"""
This test suite verifies the installation and successful
launch of the HP Smart app from the HP website
and Microsoft Store on a Windows desktop.
"""
from time import sleep
import pytest
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"


class Test_Suite_01_Install_App_From_HP_Com:
    """
    This class contains test methods to verify the installation
    and successful launch of the HP Smart app
    from the HP website and Microsoft Store on a Windows desktop.
    """
    @pytest.fixture(scope="class", autouse="true")
    # pass the 'install_app' parameter to class_setup fixture to install the app
    # before running the test cases in this class
    def class_setup(cls, request, windows_smart_setup, utility_web_session, install_app):
        """
        Initializing the test class by setting up the necessary drivers, sessions,
        and page objects required for the test cases.
        """
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.sf = SystemFlow(cls.driver)
        # Defining the install_app_path variable to use in the test cases
        cls.install_app_path = install_app
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.sp = cls.sf.sp
        # Defining the stack variable to use in the test cases
        cls.stack = request.config.getoption("--stack")
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command(
            'Get-AppXPackage -AllUsers -Name Microsoft.Services.Store* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($_.InstallLocation)\AppXManifest.xml” -Verbose}')

    def test_01_launch_app_via_webpage(self):
        """
        Go to 123.hp.com
        Enter printer serial name
        Click "Get the app" button

        Verify app launches to Main UI directly.
        Verify the latest live HP Smart gets installed automatically.
        Verify the app is installed and launched successfully

        https://hp-testrail.external.hp.com/index.php?/cases/view/27090160
        https://hp-testrail.external.hp.com/index.php?/cases/view/16929210
        """
        self.web_driver.set_size("max")
        self.sf.install_app_on_123_hp_web('9010')
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
        self.driver.ssh.send_command(
            self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(self.stack, restart=False)