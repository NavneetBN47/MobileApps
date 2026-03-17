from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_02_Camera_Scan_With_Smart_Advance_Feature(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define the variable
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_camera_scan_screen(self):
        """
        Description: C31299176, C31299178
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar

        Expected Results:
        2. Verify Advanced Scan modes are available
            - Multi-Item
            - Book
            - ID Card
         Verify Camera Scan screen
          - Enhancements button
          - Exit button
          - Flash button
        """
        self.__load_camera_capture_screen()
        self.scan.select_capture_mode("photo")
        self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT)
        self.scan.select_capture_mode("batch")
        self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT)

    def test_02_camera_scan_top_menu_button(self):
        """
        Description: C31299186, C31299188, C31299189, C31299197, C31299198
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. btn_name == x_btn: Click on X button
           btn_name == settings_btn: Click on Settings button

        Expected Results:
        4. btn_name == x_btn: App will go to Home screen
           btn_name == settings_btn: Verify Preference screen with option:
            + Title
            + Auto-Enhancements item
            + Auto-Heal item
            + Auto-Orientation item
            + Flatten Book Pages item
        """
        self.__load_camera_capture_screen()
        self.scan.select_capture_mode("photo")
        self.scan.select_enhancements_btn()
        self.scan.verify_enhancements_screen(advanced=True)
        self.fc.select_back()
        self.scan.select_exit_btn()
        self.home.verify_home_nav()

    def test_03_camera_scan_with_photo_mode_replace_option(self):
        """
        Description: C31298944
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. Click on Photo mode
        5. Click on Capture button
        6. Click on Next button
        7. Click on 3 dots icon -> Replace button

        Expected Results:
        6. Verify Preview screen with:
           + Title
           + Print / Share / Shortcuts /Save / Fax button
        7. App go back to Camera screen with Auto option displays
        """
        self.__load_camera_capture_screen()
        self.scan.select_capture_mode("document")
        self.scan.start_capture()
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_page_options_btn(btn=self.preview.REPLACE_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT)

    # ---------------     PRIVATE FUNCTIONS     ----------------------
    def __load_camera_capture_screen(self):
        """
        1. Click on Camera Scan tile on Home screen
        2. Allow Access to camera
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.fc.flow_grant_camera_scan_permissions():
            self.scan.dismiss_coachmark()
        self.scan.verify_scan_screen(source=self.scan.SOURCE_CAMERA_OPT)
