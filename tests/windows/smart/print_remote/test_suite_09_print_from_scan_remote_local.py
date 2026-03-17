import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


# pytest.app_info = "DESKTOP"
# pytest.set_info = "GOTHAM"
pytest.app_info = "GOTHAM"
class Test_Suite_09_Print_From_Scan_Remote_Local(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_add_local_and_remote_printers(self):
        """
        Precondition - Login in HP Account, And then add a local printer and one claimed remote printer to Main Page.
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.fc.select_a_remote_printer()

    def test_02_switch_to_local_printer(self):
        """
        Switch to printer to local and print a photo, verify Simple Photo Print screen shows 
        

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064125
        """
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "false"

        self.home.click_previous_device_btn()
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "true"

        printer = self.driver.ssh.send_command('Get-Printer -Name "*hp*"')
        if not printer["stdout"]:
            self.home.select_print_documents_tile()
            self.home.verify_install_to_print_dialog()
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False

        self.home.select_scan_tile()
        self.scan.verify_new_scan_auto_enhancements_dialog()

        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_print_dialog_cancel_btn()

