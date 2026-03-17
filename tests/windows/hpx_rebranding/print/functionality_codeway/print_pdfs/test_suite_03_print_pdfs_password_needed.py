import pytest
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_03_Print_Pdfs_Password_Needed(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        file = cls.driver.ssh.send_command("Test-Path " + w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF)
        file_path = ma_misc.get_abs_path(w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF_PATH)
        if "True" not in file:
            cls.driver.ssh.send_file(file_path, w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF)

        
    @pytest.mark.regression
    def test_01_verify_print_pdfs_tile(self):
        """
        Click on print PDFs tile.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.regression
    def test_02_select_password_protected_pdf_file_c44253701(self):
        """
        Verify the Password needed dialog box, when user prints the password protected pdf file.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253701
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF)
        self.fc.fd["print"].verify_password_needed_dialog()

    @pytest.mark.regression
    def test_03_verify_placeholder_c44253702(self):
        """
        The placeholder should be displayed within the text box.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253702
        """
        path = (w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF).replace('\\\\', '\\')
        self.fc.fd["print"].verify_display_text(path)

    @pytest.mark.regression
    def test_04_click_cancel_btn_without_password_c44253761(self):
        """
        In password needed dialog box, click on cancel button.
        User should be navigated to printer device page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253761
        """
        self.fc.fd["print"].select_dialog_cancel_btn()
        assert self.fc.fd["print"].verify_password_needed_dialog(raise_e=False) is False
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.regression
    def test_05_click_cancel_btn_with_password_c44255489(self):
        """
        In dialog box enter password into password field.
        Click on cancel button.
        User should be navigated to printer device page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255489
        """
        # self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF)
        self.fc.fd["print"].verify_password_needed_dialog()
        self.fc.fd["print"].input_password('1234')
        sleep(2)
        self.fc.fd["print"].select_dialog_cancel_btn()
        assert self.fc.fd["print"].verify_password_needed_dialog(raise_e=False) is False
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
    
    @pytest.mark.regression
    def test_06_verify_enter_password_is_masked_c44253703(self):
        """
        In dialog box enter the password into the textbox.
        The entered password field should be masked.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253703
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.PASSWORD_PROTECTED_1_PDF)
        self.fc.fd["print"].verify_password_needed_dialog()
        self.fc.fd["print"].input_password('12345678')
        assert self.fc.fd["print"].verify_display_text('12345678', raise_e=False) is False

    @pytest.mark.regression
    def test_07_enter_incorrect_password_c44253743(self):
        """
        In password protected dialog box, enter the incorrect password into the textbox->Click on OK button.
        "The Password is incorrect. Try again" error message should be displayed with red color on the password needed dialog box.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253743
        """
        self.fc.fd["print"].select_dialog_ok_btn()
        self.fc.fd["print"].verify_password_incorrect_text()

    @pytest.mark.regression
    def test_08_enter_empty_password_c44253760(self):
        """
        In password needed dialog box do not enter the password->Click on OK button.
        "The Password is incorrect. Try again" error message should be displayed with red color on the dialog box.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253760
        """
        self.fc.fd["print"].input_password('')
        self.fc.fd["print"].select_dialog_ok_btn()
        self.fc.fd["print"].verify_password_incorrect_text()

    @pytest.mark.regression
    def test_09_enter_correct_password_c44253711(self):
        """
        In password needed dialog box, enter the correct password into the textbox->Click on OK button.
        User should be navigated to driver window screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253711
        """
        self.fc.fd["print"].input_password('1234')
        sleep(2)
        self.fc.fd["print"].select_dialog_ok_btn()
        self.fc.fd["print"].verify_simple_print_dialog()

    @pytest.mark.regression
    def test_10_close_simple_print_dialog(self):
        """
        Close the driver window screen
        """
        if self.fc.fd["print"].verify_simple_print_dialog(raise_e=False):
            self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
            self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

