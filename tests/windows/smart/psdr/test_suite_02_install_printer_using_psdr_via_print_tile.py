import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_02_Install_Print_Driver_Via_Print_Tile(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_install_printer_via_print_tile(self):
        """
        Install print driver using PSDr via Print tile, verify flow
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14062584  
        """
        self.fc.disable_printer_driver_auto_install()
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        sleep(10)
        self.home.select_print_documents_tile()
        self.home.verify_install_to_print_dialog()
        self.home.select_install_printer_btn()
        self.home.verify_installing_printer_dialog()
        self.home.verify_success_printer_installed_dialog(timeout=120)
        self.home.select_printer_settings_tile()
        assert self.printer_settings.verify_printer_settings_page(raise_e=False) is False
        self.home.select_success_printer_installed_ok_btn()
        assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
        self.home.verify_home_screen()
