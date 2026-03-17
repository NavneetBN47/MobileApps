from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_06_Home_Navigation_Bar(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_home_nav_notification_btn(self):
        """
        Description: C31297227
         1. Load Home screen without HPID login
         2. Click on notification button on Home top navigation bar

        Expected Results:
         1. Verify Sign In /Create Account / App Settings button display on Home screen
            Verify Scanner / View & Print / Camera Scan button doesn't display on Home screen
         2. Verify notification screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN, invisible=False)
        self.home.verify_bottom_nav_btn(self.home.NAV_SIGN_IN_BTN, invisible=False)
        self.home.select_notifications_icon()
        self.home.verify_notification_screen()

    def test_02_home_nav_capture_btn(self):
        """
        Description: C31297226, C31297233
         1. Load Home screen with HPID login
         2. Click on Capture button on Home bottom navigation bar
         3. Click on back button on notification screen

        Expected Results:
        1. Verify Camera Scan / Printer Scanner / View & Print / App Settings bottom displays on Home screen
            Verify Create Account / Sign In button doesn't show on Home screen
         2. Verify No Camera Access screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, invisible=False)
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN, invisible=False)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN, invisible=False)
        self.home.verify_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN, invisible=False)
        self.home.verify_bottom_nav_btn(self.home.NAV_SIGN_IN_BTN, invisible=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, is_permission=False)
        self.scan.verify_no_camera_access_screen()

    def test_03_home_nav_view_print_btn(self):
        """
        Description: C31297234
         1. Load Home screen
         2. Click on View and Print button button on Home bottom navigation bar

        Expected Results:
         2. Verify Files and Photos screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN, is_permission=False)
        self.file_photos.verify_limited_access_popup()
        self.file_photos.select_continue_btn()
        self.file_photos.verify_files_photos_screen()

    def test_04_home_nav_app_settings_account_btn(self):
        """
        Description: C31297235,
         1. Load Home screen
         2. Click on App Settings button on Home bottom navigation bar

        Expected Results:
         2. Verify Files and Photos screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN, is_permission=False)
        self.app_settings.verify_app_settings()

    def test_05_home_nav_scan_btn(self):
        """
        Description: C31297232
         1. Load Home screen
         2. Click on Printer Scanner button on Home bottom navigation bar
         3. Click on Close button to dismiss feature unavailable button

        Expected Results:
         2. Verify Feature Unavailable popup screen
         3. Verify Home screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN, is_permission=True)
        self.home.dismiss_feature_unavailable_popup()
        self.home.verify_home_nav()