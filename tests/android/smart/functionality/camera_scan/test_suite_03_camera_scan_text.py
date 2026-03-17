from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Camera_Scan_Text(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.debug_settings = cls.fc.flow[FLOW_NAMES.DEBUG_SETTINGS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_camera_scan_text_extract_capture(self):
        """
        C31299599,C31299598,C31299618,C31299600,C31299601, C31299000, C31299615
        1. Launch the app
        2. Get to home page and sign in
        3. Tap on Camera Scan tile
        4. Select Text Extract option
        5.  Tap on Capture button
        Verify user is redirected to Text Extract screen
        Verify text language is English
        7. Tap on Continue button
        Verify "Text was not detected" dialog appears
        """   
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.scan.grant_camera_permissions():
            self.home.check_run_time_permission()
            self.scan.dismiss_coachmark()
        self.scan.select_capture_mode("text_extract")
        self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT,auto_btn_invisable=True)
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="text_extract", number_pages=1)
        self.scan.verify_text_extract_language("English")
        #press Continue
        self.scan.select_text_extract_continue_btn()
        if self.preview.verify_text_extract_edit_text_cancel_btn(raise_e = False) == False:
            # Verify not text extracted dialog is present
            self.preview.verify_no_text_extracted_dialog()

    def test_02_camera_scan_multi_item_capture_text_extract(self):
        """
        Description: C31299620, C31299621, C31299622
        Launch the app
        1. Get to home page and sign in
        2. Tap on Camera Scan
        3. Select Document option
        4. Scan a file > repeat 3 times
        5. Get to Preview page
        6. Select Text Extract option from the scrolling bar on the top
        7. Tap on Continue button
        Observe
        Verify success pop up show up and user is redirected to Text Edit screen with multiple pages file from scanned files:
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.scan.grant_camera_permissions():
            self.home.check_run_time_permission()
            self.scan.dismiss_coachmark()
        self.scan.select_capture_mode("document")
        # scan 3 times
        for i in range(0,3):
            self.scan.start_capture()
            self.scan.verify_adjust_screen()
            self.scan.select_adjust_next_btn()
            if i < 2:
                self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.preview.select_text_extract_btn()
        self.scan.verify_text_extract_title()
        #press Continue
        self.scan.select_text_extract_continue_btn()
        if self.preview.verify_text_extract_edit_text_cancel_btn(raise_e = False) == False:
            # Verify not text extracted dialog is present
            self.preview.verify_no_text_extracted_dialog()

    def test_03_printer_scan_text_extract(self):
        """
        Description: C31299619
        1. Launch the app
        2. Get to home page and sign in
        3. Add a printer to carousal
        4. Tap on Printer Scan
        5. Select Text Extract
        6. Capture a file from printer scanner

        Verify text extract from printer scanner works as expected and redirect user to Text Extract screen:
        """
        self.fc.flow_home_load_scan_screen(self.p)
        self.scan.select_capture_mode("text_extract")
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT,auto_btn_invisable=True)
        self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT, mode="text_extract", number_pages=1)
        #press Continue
        self.scan.select_text_extract_continue_btn()
        if self.preview.verify_text_extract_edit_text_cancel_btn(raise_e = False) == False:
            # Verify not text extracted dialog is present
            self.preview.verify_no_text_extracted_dialog()
