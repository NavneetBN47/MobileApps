import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_01_Print_Documents(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_supported_document_file_types_dialog(self):
        """
        Verify Supported Document File Types dialog shows after clicking Print Document tile with printer (printer driver installed)
        'HP+' + not claimed printer, verify local print UI shows for local printers 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12341708
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894499
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_print_documents_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            self.home.verify_home_screen()
            self.home.select_print_documents_tile()
        
        self.print.verify_supported_document_file_types_dialog()

    def test_02_file_picker_dialog(self):
        """
        Verify Supported Document File Types dialog shows after clicking Print Document tile with printer (printer driver installed)
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12341708
        """
        self.print.select_supported_document_file_types_dialog_ok_btn()

        self.print.verify_file_picker_dialog()

    def test_03_simple_print_dialog(self):
        """
        Click "Print Documents" tile to print, verify native dialog shows

        Verify the "Optimize for fasting remote printing" dialog does not show
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585792
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28389632
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072364
        """
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        assert self.print.verify_optimize_for_faster_remote_printing_dialog(raise_e=False) is False

    def test_04_cancel_flow_on_simple_print_dialog(self):
        """
        Click "Cancel" on native print dialog, verify print job is cancelled

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585803
        """
        self.print.select_print_dialog_cancel_btn()
        assert self.print.verify_simple_print_dialog(raise_e=False) is False
        self.home.verify_home_screen()
        
    def test_05_select_printer(self):
        """
        Click printer selection drop down on native print dialog, verify installed printers show on the list
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585794
        """
        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_do_not_show_this_message_checkbox()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()

        hostname = self.p.get_printer_information()["host name"][:-1]
        self.print.select_printer(hostname)
        self.print.verify_simple_pdf_print_dialog()

    def test_06_check_native_dialog_settings(self):
        """
        View the value in the dropdown on native dialog, verify settings show correctly 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585795
        """
        self.print.verify_orientation_setting()
        self.print.verify_paper_size_setting()
        self.print.verify_paper_type_setting()
        self.print.verify_output_quality_setting()
        self.print.verify_duplex_printing_setting()
        self.print.verify_page_range_setting()

    def test_07_change_printer_setting(self):
        """
        Change values in the dropdown on native dialog, verify settings can be changed
        Send a print job with print settings changed, verify print is successful
        send a few print jobs to printer with various print settings, verify print output matches print preview.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585796
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585800
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13258916
        """
        self.print.change_orientation_setting(w_const.ORIENTATION.LANDSCAPE)
        self.print.change_output_quality_setting(w_const.OUTPUT_QUALITY.HIGHQUALITY)

    def test_08_print_document(self):
        """
        Select a document to print, verify print preview shows
        Click "Print" on native dialog, verify print job is sent
        select multiple pages PDF to print, verify print is successful
        Do a print after printer is newly installed, verify print is successful
        Print document locally, verify Simple PDF Print dialogue is received
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585793
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585804
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585805
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585808
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061791
        """
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_09_print_password_protected_document(self):
        """
        Load a password protected file to print, verify proper error dialog shows
        Enter incorrect password on "Password needed" screen, verify proper error shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585855
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585856
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281790
        """
        self.home.select_print_documents_tile()
        assert self.print.verify_supported_document_file_types_dialog(raise_e=False) is False

        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.PASSWORD_PROTECTED_PDF)
        self.print.verify_password_needed_dialog()

        self.print.select_dialog_ok_btn()
        self.print.verify_password_incorrect_text()

        self.print.select_dialog_cancel_btn()
        self.home.verify_home_screen()

    def test_10_print_format_error_document(self):
        """
        Load an error format file to print, verify proper error dialog shows
        Click "OK" button on "File format error" dialog, verify dialog is dis missed and main UI shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585806
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585807
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281787
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894497
        """
        self.home.select_print_documents_tile()

        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.CORRUPTED_PDF)
        self.print.verify_file_format_error_dialog()

        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()
