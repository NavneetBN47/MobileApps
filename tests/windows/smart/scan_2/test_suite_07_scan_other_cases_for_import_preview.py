import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_07_Scan_Other_Cases_For_Import_Preview(object):
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


    def test_01_dismiss_import_dialog(self):
        """
        Click Scan tile -> Import title.
        Click back arrow/forward arrow/home icon when "Import, edit,and share" dialog shows
        Click "Cancel" button on the files picker dialog.

        Verify back arrow is enabled and clickable and user navigates to main UI   
        Verify user remains on Scan screen intro.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24840986
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961404
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.select_file_picker_dialog_cancel_btn()
        self.scan.verify_scanner_screen()

    def test_02_check_preview_for_pic_switch(self):
        """
        Go to Preview screen
        Perform 2 or more scan job 

        Verify Preview screen shows
        Verify Thumbnail icon is hidden when only 1 scan result.
        Verify the message under the result files are now "x of y". (x is equal and less than y)
        The left arrow should be hidden if there is no more files on the left
        The right arrow should be hidden if there is no more files on the right
        Verify there is a right arrow displayed.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13900760 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235311
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13227895
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28735601
        """
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_thumbnail_icon_is_hidden()
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_multi_pages_scan_result_screen()
        self.scan.verify_left_arrow_btn_display()
        self.scan.verify_pages_num_value()
        self.scan.click_pic_item(1)
        self.scan.verify_right_arrow_btn_display()
        self.scan.verify_pages_num_value()
        self.scan.click_righ_arrow_btn()
        self.scan.verify_left_arrow_btn_display()

    def test_03_delete_job_by_right_click_thumbnail_btn(self):
        """
        Right click on the thumbnail in Preview screen.
        Click on Delete on the flyout.
        Click Cancel button on the "Delete the 1 selected image(s)?" dialog.
        Right click on the thumbnail in Preview screen again.
        Click Delete button on the "Delete the 1 selected image(s)?" dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235394 
        """
        self.scan.right_click_pic_item(1)
        self.scan.click_delete_image_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_cancel_btn_on_dialog()
        self.scan.right_click_pic_item(2)
        self.scan.click_delete_image_btn()
        self.scan.click_delete_btn_on_dialog()
        self.scan.verify_thumbnail_icon_is_hidden()

    def test_04_check_save_share_flyout(self):
        """
        Click on Save/Share button on Preview screen to bring up the Save/Share flyout
        Check the File Type

        Verify the JPG is selected as default file type if the files are recognized as photo.
        Verify the PDF is selected as default file type if the files are recognized as document.
        Verify the "Basic PDF" / Image*(.jpg) is able to selected
        Verify the following options shows and are selectable
        a. None
        b. Low
        c. Medium
        d. High

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235261 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29628417 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29628418 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29628419 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30229952 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30229953
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793681
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_file_type("jpg")
        self.scan.select_compression_dropdown()
        file_grade = ["None","Low","Medium","High"]
        for grade in file_grade:
            el = self.scan.verify_dropdown_listitem(grade)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.click_dialog_close_btn()
        self.scan.click_share_btn()
        self.scan.verify_share_dialog()
        self.scan.verify_file_type("jpg")
        self.scan.select_file_type_dropdown()
        file_type = ["Basic PDF", "Image(*.jpg)"]
        for type in file_type:
            el = self.scan.verify_dropdown_listitem(type)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.select_compression_dropdown()
        for grade in file_grade:
            el = self.scan.verify_dropdown_listitem(grade)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.click_dialog_close_btn()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_file_type("pdf")
        self.scan.click_dialog_close_btn()
        self.scan.click_share_btn()
        self.scan.verify_share_dialog()
        self.scan.verify_file_type("pdf")
        