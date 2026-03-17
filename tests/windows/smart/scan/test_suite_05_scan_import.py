import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_05_Scan_Import(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        
    def test_01_verify_import_dialog(self):
        """
        Click Scan on main UI.
        Click the Import title on scan screen.

        Verify dialog "Import,edit,and share" displayed
        Verify "get started" button on the dialog leads to the file picker window (files pick dialog).
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961402  
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14555250
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572537
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_learn_more_link()
        self.home.verify_help_and_support_page()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.scan.verify_import_dialog()

    def test_02_import_file_to_scan(self):
        """
        Click Import titile again.
        Select one image and click "Open" button the files picker dialog

        Verify Detect Edges screen displays.
        Verify the image opens and is added.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961654
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961733 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29707828 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961729
        """
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

    def test_03_import_file_by_add_btn(self):
        """
        Click "Add +" link.
        Click Import tab and picker a image file.
        Click "Apply" button on the Detect Edges screen.

        Verify pages are added to Preview screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961727
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961403
        """
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.scan.click_import_apply_btn()
        self.scan.verify_multi_pages_scan_result_screen()

    def test_04_delete_page(self):
        """
        Click "x" on the right top corner of one image.
        Click "Delete" button on the Delete dialog.
        Click "Cancel" button on the Delete dialog.

        Verify page is removed from Preview screen after click on "Delete" button on the 
        Delete dialog and user navigate to Preview screen with deleted page
        Verify user navigate back to Preview screen with 2 pages displayed after click on 
        "Cancel" button on the Delete dialog
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961728
        """
        self.scan.click_multi_menu_btn()
        self.scan.click_multi_delete_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_delete_btn_on_dialog()
        self.scan.verify_scan_result_screen()
        
    def test_05_verify_format_error(self):
        """
        Rename a .txt file to .jpg (this will cause an error format error)
        Select the above saved .jpg file and then click "Open" button.

        Verify file format error warning dialog displays.
        Verify there is a "Close" button on the dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961655
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27362065
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27387088
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.CORRUPTED_JPEG)
        self.scan.verify_file_format_error_dialog()

    def test_06_verify_large_file_error(self):
        """
        Select the above very large file and then click "Open" button.

        Verify file is too large error warning dialog displays.
        Verify there is a "Close" button on the dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25695749
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27362067
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846482
        """
        self.scan.click_close_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.LARGE_JPG)
        self.scan.verify_large_file_error_dialog()
        self.scan.click_close_btn()
        self.scan.verify_scanner_screen()
