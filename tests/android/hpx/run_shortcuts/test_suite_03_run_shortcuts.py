import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_03_Run_Shortcuts:
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
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_camera_access_in_manual_mode(self):
        """
        TestRail: C51953847
        Verify the behavior when the user allows access to the camera in Manual
        PreConditions:
        1. Install and launch the HPX app
        2. Ensure that the user is logged into the account
        3. Created shortcut should available
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5.Capture a file.
        6.Tap "Next" on the Adjust Boundaries screen.
        7.Navigate to the Preview page.
        8.Tap on "Start email(Shortcut Mail)"
        9.Observe the behavior.
        Expected: The shortcut starts successfully.
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
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.hpx_printer_details.click_start_email_btn()
        self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        self.hpx_shortcuts.click_view_status_btn()
        

    def test_02_verify_page_processing_dialog(self):
        """
        TestRail: C51953848
        Verify the behavior of print, save and email page is processing in Manual Mode
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5.Capture a file.
        6.Tap "Next" on the Adjust Boundaries screen.
        7.Navigate to the Preview page.
        8.Tap on "Start email(Shortcut Mail)"
        9.Observe the behavior.
        Expected: The shortcut starts successfully.
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
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        self.hpx_shortcuts.click_view_status_btn()

    def test_03_verify_page_not_processing_dialog(self):
        """
        TestRail: C51953849
        Verify the behavior of print, save and email page is not processing in Manual Mode
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5.Capture a file.
        6.Tap "Next" on the Adjust Boundaries screen.
        7.Navigate to the Preview page.
        8.Tap on "Start email(Shortcut Mail)"
        9.Observe the behavior.
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
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.hpx_printer_details.click_start_email_btn()
        self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        self.hpx_shortcuts.click_view_status_btn()

    def test_04_verify_flash_mode_on(self):
        """
        TestRail: C51953850
        Verify the flash mode functionality on the Manual mode camera screen when the user selects the "ON" option
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5. Choose flash mode option to "ON" in camera screen.
        6. Capture the image.
        7. Observe the behavior.
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
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()

    def test_05_verify_flash_mode_off(self):
        """
        TestRail: C51953851
        Verify the flash mode functionality on the Manual mode camera screen when the user selects the "OFF" option

        Steps:  
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5. Choose flash mode option to "OFF" in camera screen.
        6. Capture the image.
        7. Observe the behavior.
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
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()