import pytest
from time import sleep
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_Install_App_From_MS_Store(object):
    @pytest.fixture(scope="class", autouse="true")
    # pass the 'install_app' parameter to class_setup fixture to install the app
    # before running the test cases in this class
    def class_setup(cls, request, windows_smart_setup, utility_web_session, install_app):
    # def class_setup(cls, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        # Defining the stack variable to use in the test cases
        cls.stack = request.config.getoption("--stack")
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]

        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('Stop-Process -Name "*chrome*"')
        sleep(2)
        cls.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized')     
        sleep(2)
        cls.driver.ssh.send_command('Get-AppXPackage -AllUsers -Name Microsoft.Services.Store* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($_.InstallLocation)\AppXManifest.xml” -Verbose}')
    
    def test_01_open_app_via_Microsoft_store(self):
        """
        Go to Settings->Devices->Printers & Scanners
        Select the searched network printer and click Add device. 
        Wait the printer install successfully.

        Verify the latest live HP Smart gets installed automatically.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16929208
        https://hp-testrail.external.hp.com/index.php?/cases/view/16929214
        """    
        self.sf.get_app_on_win_settings()
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()

    def test_02_install_latest_build(self):
        self.sf.settings_and_store_cleanup()
        self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(self.stack, restart=False)