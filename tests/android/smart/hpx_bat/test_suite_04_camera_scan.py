from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"


class Test_Suite_04_Camera_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.cpreview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    @pytest.mark.testrail("S159.C371358")
    def test_01_camera_scan_multiple_pages(self):
        """
        Description: C31299181
            1/ Load Camera screen via Camera Scan from tile
            2/ Capture 2 pages with Batch mode

        Expected Result:
            2/ Verify Landing Page:
                 - Navigation bar: Back, Edit, and 3dots icon buttons, and  Camera Scan title
                 - There are at least 3 icons at bottom navigation bar
                 - Total page is "2"
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages(number_pages=2)
        self.cpreview.verify_preview_screen()
        assert self.cpreview.verify_preview_page_info()[1] == 2, "Page count should be 2"
        self.cpreview.verify_bottom_nav(btns=[self.cpreview.SHARE_BTN, self.cpreview.SAVE_BTN, self.cpreview.PRINT_PREVIEW_BTN])

    @pytest.mark.testrail("S159.C371359")
    def test_02_camera_scan_pdf_share_gmail(self):
        """
        Description: C31299781, C31297310
            1/ Load Home screen
            2/ Connect to target printer and make single page via Camera Scan tile on Home screen with manual capture (If scan tile is not on Home screen, then enable it in Personalize screen)
            3/ At Landing Page, click on Share button on bottom navigation bar
            4/ Select File Size button
            5/ Select Small File Size
            6/ Select Basic PDF
            7/ Rename File
            8/ Select Share button
            9/ Go through Share flow to send an email via Gmail

        Expected Result:
            2/ Verify Landing Page:
                 - Navigation bar: Back, Edit, and 3dots icon buttons, and  Scan title
                 - Main button is "Share"
            3/ Share Option screen display
            4/ Verify Small, Medium, Large, Actual file sizes
            9/ Verify that the email is sent to Gmail account.
        """
        file_name = self.test_02_camera_scan_pdf_share_gmail.__name__
        self.__camera_scan_load_landing_page(is_printer=False)
        self.cpreview.select_bottom_nav_btn(self.cpreview.SHARE_BTN)
        self.cpreview.select_file_size()
        self.cpreview.verify_file_size([self.cpreview.FILE_SIZE_ACTUAL, self.cpreview.FILE_SIZE_SMALL, self.cpreview.FILE_SIZE_MEDIUM])
        self.cpreview.select_file_size(self.cpreview.FILE_SIZE_SMALL)
        self.cpreview.verify_title(self.cpreview.SHARE_TITLE)
        self.cpreview.select_file_type(self.cpreview.BASIC_PDF)
        self.cpreview.rename_file(file_name)
        self.cpreview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    @pytest.mark.testrail("S159.C371360")
    def test_03_camera_scan_verify_print_settings_trapdoor_ui(self):
        """
        Description: C31299784, C31299876, C31297389
            1/ If current screen is not Landing Page from test 02, implement 2 first steps of test 02
            2/ At Landing Page, click on Print button on bottom navigation bar
            3/ If App Permission display, dismiss it.
            4/ Make a printing job via HPPS trapdoor ui

        Expected Result:
            4/ Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui
        """
        self.__camera_scan_load_landing_page(is_printer=True)
        self.fc.flow_preview_make_printing_job(self.p)

    @pytest.mark.testrail("S159.C371361")
    def test_04_camera_scan_jpg_save(self):
        """
        Description:
            1/ Continue test 03 by pressing Back key of mobile device.  If current screen is not Landing Page from test 02, implement 2 first steps of test 02
            2/ At Landing Page, click on Save button on bottom navigation bar
            4/ Rename and toggle pdf off. Then, click on action button on bottom

        Expected Result:
            3/ Save Option screen
            4/ Verify Landing Page
        """
        # Not affect by previous test
        self.fc.reset_app()
        file_name = self.test_04_camera_scan_jpg_save.__name__
        self.__camera_scan_load_landing_page(is_printer=False)
        self.cpreview.select_bottom_nav_btn(self.cpreview.SAVE_BTN)
        self.cpreview.rename_file(file_name)
        self.cpreview.select_action_btn()
        self.cpreview.dismiss_file_saved_popup()
        self.cpreview.verify_preview_screen()
        self.fc.verify_existed_file("{}/{}.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))

    @pytest.mark.testrail("S159.C371362")
    def test_05_camera_scan_pdf_save(self):
        """
        Description: C31297711, C31297717
            As test 04, but toggle pdf on

        Expected Result:
            3/ Save Option screen
            4/ Verify Landing Page
        """
        file_name = self.test_05_camera_scan_pdf_save.__name__
        self.__camera_scan_load_landing_page(is_printer=False)
        self.cpreview.select_bottom_nav_btn(self.cpreview.SAVE_BTN)
        self.cpreview.select_file_type(self.cpreview.BASIC_PDF)
        self.cpreview.select_action_btn()
        self.local_files.save_file_to_downloads_folder(file_name)
        self.cpreview.dismiss_file_saved_popup()
        self.cpreview.verify_preview_screen()
        self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))

    # ---------------     PRIVATE FUNCTIONS     ----------------------
    def __camera_scan_load_landing_page(self, is_printer=False):
        """
         If current screen is not Landing Page, call flow_capture_single_photo
        """
        self.fc.flow_load_home_screen()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p)
            self.home.dismiss_print_anywhere_popup()
        self.fc.flow_home_camera_scan_pages()
        self.cpreview.verify_preview_screen()