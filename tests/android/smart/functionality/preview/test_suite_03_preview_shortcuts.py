from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import *

pytest.app_info = "SMART"

class Test_Suite_03_Preview_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.softfax_offer = cls.fc.flow[FLOW_NAMES.SOFTFAX_OFFER]

        # Define variables
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF
        cls.smart_context = cls.fc.smart_context
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

    def test_01_shortcuts_through_camera_scan(self):
        """
        Requirements:
        1. C31461812	Scan first flow > Preview page
        2. C31461813	Scan first flow > "i" button behavior on Shortcuts preview page 
        3. C31461814	Scan first flow > Start shortcut behavior 
        4. C37412055

        Description:
        1. Load to Home screen with HPID account login
        2. Click on Camera Scan
        3. Capture a picture and lead to Preview screen
        4. Click on Shortcuts button on Preview screen

        Expected Results:
        4. Verify Shortcuts screen:
        """
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="document")
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHORTCUTS_BTN)
        self.preview.verify_shortcuts_popup()

    def test_02_shortcuts_through_files(self):
        """
        Description:
            1.	C31461815	"View&Print" first flow > Start Shortcut behavior
        Requirements:
        1.C31461816	Document name on landing page 
        Description:
        1. Load to Home screen
        2. Load to App Settings screen and login to an existed HPID account login
        3. Click on Print Document tile
        4. Click on PDF
        5. Select any .pdf file
        6. Click on Shortcuts

        Expected Results:
        6. Verify Shortcuts screen:
        """
        self.fc.flow_load_home_screen(verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.files.load_downloads_folder_screen()
        self.files.select_file(self.pdf_fn)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHORTCUTS_BTN)
        self.preview.verify_shortcuts_popup()

    def test_03_shortcuts_mobile_fax_sign_in_popup(self):
        """
        Description: C31297299, C31297307
        1. Load to Home screen without HPID login
        2. Click on Print Document tile
        3. Click on PDF
        4. Select any .pdf file
        5. Click on Mobile Fax

        Expected Results:
        5. Verify Mobile Fax Sign In screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(create_acc=True)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.files.load_downloads_folder_screen()
        self.files.select_file(self.pdf_fn)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.softfax_offer.verify_get_started_screen()