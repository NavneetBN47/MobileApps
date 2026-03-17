import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_02_Open_Printer_App(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Stop-Process -Name "*chrome*"')
        sleep(2)
        cls.driver.ssh.send_command('Stop-Process -Name "*HP.Smart*"')
        sleep(2)
        cls.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized')     
        sleep(2)
        cls.driver.ssh.send_command('Get-AppXPackage -AllUsers -Name Microsoft.Services.Store* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($_.InstallLocation)\AppXManifest.xml” -Verbose}')
        
    def test_01_launch_app_via_win_settings(self):   
        """
        Go to Settings->Devices->Printers & Scanners
        Select the searched network printer and click Add device. 
        Wait the printer install successfully.
        Select the installed printer
        Click on "Open printer app"

        Verify the Gotham app is launched with the same printer.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/17117176
        https://hp-testrail.external.hp.com/index.php?/cases/view/27731315
        """
        printer_info = self.sf.launch_app_on_win_settings()
        self.fc.go_home()
        sleep(2)
        self.home.select_printer_settings_tile()
        printer_model_name = self.printer_settings.get_model_name_text().strip()
        printer_host_name = printer_model_name.split(' ')[0]
        assert printer_host_name in printer_info

    def test_02_settings_and_store_cleanup(self):
        self.sf.settings_and_store_cleanup()
