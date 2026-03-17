import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_07_Run_Shortcuts:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup,load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN]
        cls.print_quality_tools = cls.fc.fd[FLOW_NAMES.PRINT_QUALITY_TOOLS]
        cls.photos = Photos(cls.driver)
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.home = cls.fc.fd[FLOW_NAMES.HOME]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.photos = Photos(cls.driver)
        cls.fc.hpx = True

    def test_09_Verify_the_behavior_of_print_save_and_email_page_is_processing_in_Auto_Mode(self):
        """
        TestRail: C51953865
        Verify the behavior of print, save and email page is processing in Auto Mode
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1. Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Capture a file.
        4.Click on Auto or full
        5.Tapon "Next" button in the detect edges screen and observe"
        6.Navigate to the Preview page.
        7.Tap on "Start Print/Save/Email(Shortcut Print/Save/Email)"
        8.Observe the behavior.
        Expected: User will see the dialog box says as "your shortcuts running" with options Done, View status and shortcuts
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.toggle_capture_mode(manual=False)
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()

    def test_10_Verify_the_behavior_of_print_save_and_email_page_is_not_processing_in_Auto_Mode(self):
        """
        TestRail: C51953866
        Verify the behavior of print, save and email page is not processing in Auto Mode
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1. Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Capture a file.
        4.Click on Auto or full
        5.Tapon "Next" button in the detect edges screen and observe"
        6.Navigate to the Preview page.
        7.Tap on "Start Print/Save/Email(Shortcut Print/Save/Email)"
        8.Observe the behavior.
        Expected: User will see the dialog box says as "There was problem running with your shortcut" with options Skip Printing and Cancel
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.toggle_capture_mode(manual=False)
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()

    def test_11_verify_the_flash_mode_functionality_on_the_Auto_mode_camera_screen_when_the_user_selects_the_ON_option_and_captures_an_image(self):
        """
        TestRail: C51953867
        Verify the flash mode functionality on the Auto mode camera screen when the user selects the "ON" option and captures an image.
        PreConditions:
        1. Install and launch the HPX app.
        2. Ensure that the user is logged into the account.
        3. Created shortcut should be available
        Steps:
        1. Click on Existing Shortcut
        2. Tap on the "Camera Scan" tile.
        3. Choose flash mode option to "ON" in camera screen.
        4. Capture the image.
        5. Observe
        Expected: The user should see that the Flash mode option is set to "ON" and the captured image should be a flashed image.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.toggle_capture_mode(manual=False)
        self.camera_scan.get_camera_scan_flash_mode()
        assert self.camera_scan.verify_auto_is_selected()

    def test_12_Verify_the_flash_mode_functionality_on_the_Auto_mode_camera_screen_when_the_user_selects_the_OFF_option_and_captures_an_image(self):
        """
        TestRail: C51953868
        Verify the flash mode functionality on the Auto mode camera screen when the user selects the "OFF" option and captures an image.
        PreConditions:
        1. Install and launch the HPX app.
        2. Ensure that the user is logged into the account.
        3. Created shortcut should be available
        Steps:
        1. Click on Existing Shortcut
        2. Tap on the "Camera Scan" tile.
        3. Choose flash mode option to "OFF" in camera screen.
        4. Capture the image.
        5. Observe
        Expected: The user should see that the Flash mode option is set to "OFF" and the captured image should be a non-flashed image.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.get_camera_scan_flash_mode()
        assert self.camera_scan.verify_auto_is_selected()
        self.camera_scan.toggle_capture_mode(manual=False)
        assert self.camera_scan.verify_auto_is_selected()