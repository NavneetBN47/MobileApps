import pytest
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_01_Searchable_PDF_Without_Password(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session, logout_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.fc.web_password_credential_delete()
        cls.printer_name=cls.p.get_printer_information()["model name"]
        
    @pytest.mark.regression
    def test_01_login_with_adv_account(self):
        """
        Login with adv account to test scribble function in scan.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.hpx_sign_in_advanced_account(web_driver=self.web_driver)
        self.fc.add_a_printer(self.p)

    @pytest.mark.regression
    def test_02_verify_save_searchable_pdf_file_without_password_C49496775(self):
        """
        Save a searchable PDF file without password protection.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/49496775
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.INVERTED_JPG, w_const.TEST_DATA.INVERTED_JPG_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.INVERTED_JPG)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        self.fc.fd["scan"].select_file_type_listitem(self.fc.fd["scan"].SEARCHABLE_PDF)
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        # verify the saved searchable pdf file is saved.
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        sleep(2)
        #delete file
        self.driver.ssh.send_command("del " + file_path)

