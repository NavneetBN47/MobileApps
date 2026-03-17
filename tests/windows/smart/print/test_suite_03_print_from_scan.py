import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_03_Print_From_Scan(object):
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
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        

    def test_01_print_from_scan_preview_screen(self):
        """
        Print from scan with driver already installed, verify happy path
        Click "Print" button on Scan Preview screen with driver installed, verify scan files are added to print dialog
        Validate print preview after click "Print" on Preview screen, verify it's consistent with the scan results 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/194462d44
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446253
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446257
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894499
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
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.scan.verify_scan_result_screen()  

    def test_02_cancel_from_scan_preview_screen(self):
        """
        Enter print flow from Scan, cancel print job before sending, verify print job is canceled

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446255
        """

        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()

        self.print.select_print_dialog_cancel_btn()
        self.scan.verify_scan_result_screen()

    def test_03_print_with_settings_modified(self):
        """
        Print from Scan with a few different print settings modified, verify results
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446256
        """
        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)

        self.print.change_orientation_setting(w_const.ORIENTATION.LANDSCAPE)

        self.print.select_print_dialog_print_btn()
        self.scan.verify_scan_result_screen()

