import pytest

from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT


pytest.app_info = "SMART"

class Test_Suite_01_Preview_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.smart_context = cls.fc.smart_context

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)
        
    def test_01_softfax_screen_by_login_hpid(self):
        """
        Description: C31297308
        1. Load to Home screen with user onboarding account login
        2. Go to Home screen to click on View & Print button
        3. Click on PDFs
        4. Select any .pdf file
        5. Click on Softfax button

        Expected Results:
        5. Verify Compose Softfax screen:
           + Title
           + button
        """
        # There are multiple test suites under Preview folder. So add clear cache here to make sure no get affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.select_file(TEST_DATA.ONE_PAGE_PDF)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.compose_fax.verify_compose_fax_screen()