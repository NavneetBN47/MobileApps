import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import TEST_DATA


pytest.app_info = "SMART"

class Test_suite_01_app_background_test(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        #Define Variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_verify_print_with_app_background(self):
        """
        verify print functionality with app backgrounding multiple times
        Description:

            1.launch the App
            2.Navigate to app home screen
            3.Add the test printer to carosual
            4.Select a file to print
            5.Proceed to preview page
            6.Tap on Print Button
            7.When user is on print preview screen, background the app for about 10 secs
            8.Come back to the app
            9.Repeat step 7 and 8 for about 2-3 times.
            10.Submit the print job

        Expected results:

            1.The print button should work as expected after app is backgrounded.
            2.Verify the print job should be successful.
            """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.file_photos.verify_files_photos_screen()
        self.file_photos.select_local_item(self.file_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        if self.preview.verify_title(self.preview.PRINT_SIZE_TITLE, raise_e=False):
            self.preview.select_print_size(self.preview.PRINT_SIZE_4x6)
        for _ in range(3):
            self.fc.run_app_background(timeout=10)
            self.preview.verify_preview_screen()
        self.fc.flow_preview_make_printing_job(self.p)

    def test_02_app_background_during_printer_scan(self):
        
        """
        Description: C31299866
        1.Launch the app
        2.Navigate to app home screen
        3.Add the test printer to the carousal that supports scan
        4.Tap on Printer scan and scan a file
        5.Navigate back to home screen
        6.Again tap on Printer scan option
        7.Background the app for about 10 seconds
        8.Come back to the app
        9.Repeat step 7 and 8 2 more times.
        10.Perform the scan again

        Expected result:
        1.The scan button should work as expected after app is backgrounded.
        2.Verify the scan job is successful.
        """
        self.fc.reset_app()
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.fc.select_back()
        self.preview.verify_exit_popup()
        self.preview.select_exit_popup_btn("home")
        if self.home.verify_feature_popup(raise_e=False):
            self.home.select_feature_popup_close()
        self.home.verify_home_nav()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        for _ in range(2):
            self.fc.run_app_background(timeout=10)
            self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()

    def test_03_app_background_during_camera_scan(self):

        """
        Description:
        1.Launch the app
        2.Navigate to app home screen
        3.Tap on Camera scan
        4.Scan a file and navigate back to home
        5.Again tap on camera scan.
        6.Before capturing the photo, background the app for about 10 seconds
        7.Come back to the app
        8.Repeat step 6 and 7 two more times.
        9.Now capture the image and finish scan

        Expected Results:
        9. Verify scan job is successful.
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages()
        self.fc.flow_load_home_screen(verify_signin=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, is_permission=False)
        for _ in range(3):
            self.fc.run_app_background(timeout=10)
            self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT)
        self.fc.flow_camera_scan_capture_photo()

    def test_04_app_background_during_share_save(self):

        """
        Description:
        1.Launch the app
        2.Navigate to app home screen
        3.Capture a photo and proceed to preview screen
        4.Tap Share/Save option
        5.Background the app for about 10 sec
        6.Come back to the app
        7.Repeat step 6 and 7 two more times.
        8.Now finish the share or save

        Expected:
        Verify file can be shared/saved successfully
        """
        file_name = "{}".format(self.test_04_app_background_during_share_save.__name__)
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        for _ in range(2):
            self.fc.run_app_background(timeout=10)
            self.preview.verify_title(self.preview.SHARE_TITLE)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)