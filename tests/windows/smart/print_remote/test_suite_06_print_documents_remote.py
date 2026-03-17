import pytest
from time import sleep
import random

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_06_Print_Documents_Remote(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.activity_center = cls.fc.fd["activity_center"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

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

    @pytest.fixture()
    def restore_remote_printer_state(self):
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_01_add_remote_printer(self):
        """
        In App Print Dialog(IPP)_Print Documents Happy Path
        [POTG not enable, PA enabled] Send a print job to a remote printer, verify legacy remote print experience is seen	
        Check features on a remote printer that was added directly from device picker, verify remote printer experience is seen 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061772
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894527
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/19535796
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843581
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843672
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_check_back_flow(self):
        """
        Click the back arrow from print preview, verify user returns to Main UI
        *Navigate to the remote print screen with supported printers, verify "2 Sided Printing" is listed on the settings 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061778
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24810631
        """
        self.__start_a_remote_print_via_print_documents(w_const.TEST_DATA.ONE_PAGE_DOC)
        self.print.verify_ipp_print_screen_two_sided_printing_item()
        self.home.select_navbar_back_btn()

    def test_03_check_sending_file_dialog(self, restore_remote_printer_state):
        """
        Click Print button from Preview screen, verify 'sending file' dialogue appears 
        Click Cancel button from Preview screen, verify sending file dialogue disappears and user returns to Print Documents screen 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061783
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061784
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072316
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27959505
        """
        self.__start_a_remote_print_via_print_documents(w_const.TEST_DATA.COLOR_PDF)

        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()

        self.print.verify_sending_file_dialog()
        if self.print.verify_dialog_cancel_btn(raise_e=False):
            self.print.select_dialog_cancel_btn()
        self.print.verify_print_job_canceled_dialog()
        self.print.select_dialog_ok_btn()
        self.print.verify_ipp_print_screen_document_preview_image()

    @pytest.mark.parametrize("buttons", ["OK", "JOB_STATUS"])
    def test_04_check_file_sent_dialog(self, buttons, restore_remote_printer_state):
        """
        Click Print button from Preview screen, verify 'File Sent' dialogue appears
        Click OK button on 'File Sent' dialog, verify the user return to main UI
        Click Job Status button on 'File Sent' dialog, verify the activity center opens in the popup window
	    Toggle Printer settings on preview screen, verify functionality
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061788
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061785
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061789
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14590938
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061779
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072320
        """
        self.__start_a_remote_print_via_print_documents(w_const.TEST_DATA.ONE_PAGE_DOC)
        quality_list = ['normal', 'best', 'draft']
        self.print.change_ipp_print_quality(random.choice(quality_list))
        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=120)
        if buttons == "OK":
            self.print.select_dialog_ok_btn()
        else:
            self.print.select_file_sent_dialog_job_status_btn()
            self.activity_center.verify_print_flyout_with_job()
            self.activity_center.click_close_btn()
        self.home.verify_home_screen()
        
    def test_05_send_incorrect_file(self, restore_remote_printer_state):
        """
        Print a PDF that is in an error state, verify error dialogue indicating invalid file format 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061812
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072340
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.CORRUPTED_PDF)

        self.print.verify_file_format_error_dialog(remote_printer=True, file_path=w_const.TEST_DATA.CORRUPTED_PDF)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_06_send_password_protected_file(self, restore_remote_printer_state):
        """
        Print a password protected file, verify error dialogue indicating that protected files are not supported

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061813
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072346
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.PASSWORD_PROTECTED_PDF)

        self.print.verify_password_protected_pdf_dialog(w_const.TEST_DATA.PASSWORD_PROTECTED_PDF)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()
        self.fc.sign_out()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __start_a_remote_print_via_print_documents(self, file_name):
        """
        Start a cloud print job, verify generic preview while loading file
        Start a cloud print job from Print Document screen, verify 'Getting Remote Printer Status' with loading icon 	
        Start a cloud print job from Print Document screen, verify 'Creating preview' with loading icon

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061774
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061777
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061780
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072239
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072306
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061837
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061892
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(file_name)
        self.print.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        self.print.verify_ipp_print_screen_document_preview_image()


