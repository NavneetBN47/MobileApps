import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_09_Print_From_Scan_20Pages(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        

    def test_01_go_through_flow_to_scan_results_screen(self):
        """
        Precondition
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

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

        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

    def test_02_add_more_pages_and_print(self):
        """
        Print from Scan with a large amount of scanned files, verify success

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446262
        """
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_multi_pages_scan_result_screen()

        for i in range(20):
            self.scan.click_multi_add_pages_btn()
            self.scan.verify_scanner_screen()
            self.scan.select_import_btn()
            self.print.verify_file_picker_dialog()
            self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
            self.scan.verify_import_screen()
            self.scan.click_import_apply_btn()
            self.scan.verify_multi_pages_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.scan.verify_multi_pages_scan_result_screen()  
