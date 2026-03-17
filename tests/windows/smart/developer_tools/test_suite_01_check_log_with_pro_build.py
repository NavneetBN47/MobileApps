import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows import utility

pytest.app_info = "GOTHAM"
class Test_Suite_01_Check_Log_With_Pro_Build(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        if cls.stack != 'production':
            pytest.skip("This test is only for Production build")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_add_a_printer(self):
        """
        Go to the main page and select a printer    
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_perform_a_scan_job(self):
        """
        perform a scan job   
        """
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        sleep(1)
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_home_screen()

    def test_03_send_a_print_job(self):
        """
        Send a print job 
        """
        self.home.select_print_documents_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=300)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.verify_home_screen()
            self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_do_not_show_this_message_checkbox()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_04_relaunch_app(self):
        """
        Use some other features in the app
        Close and re-launch app
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        sleep(5)

    def test_05_check_log_files(self):
        """
        Go log folder to look for log files

        Verify there is no gotham log files generated.
        Verify OOBE log is created only

        https://hp-testrail.external.hp.com/index.php?/cases/view/17169914
        """
        gotham_log = w_const.TEST_DATA.HP_SMART_LOG_PATH
        assert utility.check_path_exist(self.driver.ssh, gotham_log) is False
        oobe_log = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\Logs\HPSmart_OOBE.log'
        assert utility.check_path_exist(self.driver.ssh, oobe_log) is True
