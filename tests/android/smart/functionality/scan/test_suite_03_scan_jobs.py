from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Scan_Jobs(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.is_pdf = {"pdf": True, "jpg": False}
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)
        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("scan_settings", ["color,75,3.5x5",
                                               "color,100,4x6",
                                               "color,300,letter",
                                               "black,75,3.5x5",
                                               "black,200,5x7",
                                               "black,300,a4"
                                               ])
    def test_01_scan_with_settings(self, scan_settings):
        """
        Descriptions:C31299812, C31299843, C31299812
         1. Sign into hpid and load home screen
         2. Load printer
         3. Select Printer Scan on navbar
         4. Select Scan Settings button
         5. Set Scan Settings based on scan_settings param
         6. Select Capture button
         7. Select Next button
        Expected Result:
         7. Verify preview nav
        """
        scan_settings = scan_settings.split(",")
        self.fc.flow_home_load_scan_screen(self.p, from_tile=False)
        self.scan.select_scan_settings_btn()
        self.scan.select_scan_setting("source", option="scanner")
        self.driver.press_key_back()
        self.scan.select_scan_setting("color", option=scan_settings[0])
        self.driver.press_key_back()
        self.scan.select_scan_setting("resolution", option=scan_settings[1] + "_dpi")
        self.driver.press_key_back()
        self.scan.select_scan_setting("page_size", option=scan_settings[2])
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()

    def test_02_scan_multiple_pages_print(self):
        """
        Description: C31299856, C31299834
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement print
        Expected Result:
            4/ Print successfully
        """
        self.__home_make_scan_two_pages()
        self.fc.flow_preview_make_printing_job(self.p)

    @pytest.mark.parametrize("file_type", ["pdf", "jpg"])
    def test_03_scan_multiple_pages_share_gmail(self, file_type):
        """
        Description: C31299783, C31299819, C31299831, C31299832, C31299833, C31297313
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement Gmail sharing as PDF/JPG on landing page
        Expected Result:
            4/ Gmail sharing successfully successfully
        """
        file_name = "{}_{}".format(self.test_03_scan_multiple_pages_share_gmail.__name__, file_type)
        self.__home_make_scan_two_pages()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_title(self.preview.SHARE_TITLE)
        self.preview.select_file_type(self.preview.BASIC_PDF if file_type == "pdf" else self.preview.IMAGE_JPG)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                             file_name,
                                             from_email=self.email_address)

    @pytest.mark.parametrize("file_type", ["pdf", "jpg"])
    def test_04_scan_multiple_pages_save(self, file_type):
        """
        Description: C31299786, C31299787, C31299852, C31299869, C31299835, C31297324, C31297327
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement Save as PDF/JPG on landing page
        Expected Result:
            4/ Save successfully via checking file name in Print Document
        """
        file_name = "{}_{}".format(self.test_04_scan_multiple_pages_save.__name__, file_type)
        self.__home_make_scan_two_pages()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_title(self.preview.SAVE_TITLE)
        self.preview.select_file_type(self.preview.BASIC_PDF if file_type == "pdf" else self.preview.IMAGE_JPG)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        if self.is_pdf[file_type]:
            self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_file_saved_popup()
        self.preview.verify_preview_screen()
        if self.is_pdf[file_type]:
            self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))
        else:
            self.fc.verify_existed_file("{}/{}.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))

    @pytest.mark.parametrize("source,mode", [("scanner", "document"), ( "scanner", "multi_item"), ("camera", "photo"), ("camera", "multi_item")])
    def test_05_scan_modes(self, source, mode):
        """
        Description:
         1. Load Smart App and Signin with HP+
         2. Select Printer Scan or Camera Scan on bottom navbar
          - Load printer if source == "scanner"
          - Grant camera permissions if camera scan
         3. Select Desired Mode
         4. Select Capture Button
        Expected Resuts:
         3. if source == "camera" Verify "Center content in frame..." message
          - text is "Center 2-3 items in frame..." for multi-item mode
         4. Verify "Processing..." message
        """
        if source == "scanner":
            self.fc.flow_home_load_scan_screen(self.p)
        else:
            self.fc.flow_load_home_screen()
            self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
            if self.fc.flow_grant_camera_scan_permissions():
                self.scan.dismiss_coachmark()
        self.scan.select_capture_mode(mode)
        if source == "camera":
            self.scan.verify_bubble_msg(message="center_content" if mode != "multi_item" else "center_multiple")
        self.scan.start_capture()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __home_make_scan_two_pages(self):
        """
        Make a scan job with 2 pages from Home screen
            - At Home, select printer
            - Click on target tile name for scanning (scan, scan to email, scan to cloud)
            - At Scan screen, click on Scan
            - At Landing Page, click on Add icon
            - Click on Scan again on Scan screen
            - Verify Landing Page
        """
        self.fc.reset_app()
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.verify_preview_page_info()[1] == 2, "Page count should be 2"