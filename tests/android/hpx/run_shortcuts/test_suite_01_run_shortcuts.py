import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.smart.flow_container import FlowContainer
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_01_Run_Shortcuts:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup,load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.fc_hpx = FlowContainer(cls.driver)
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
        cls.fc.hpx = True

    def test_01_verify_camera_access_in_manual_mode(self):
        """
        TestRail: C51953838
        Verify the behavior when the user allows access to the camera in Manual
        PreConditions:
        1. Install and launch the HPX app
        2. Ensure that the user is logged into the account
        3. Created shortcut should available
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Select the source from the screen
        5. Tap on Camera Scan
        6. Click on Allow option (if your access the camera first time)
        7. Capture a file and observe
        Expected: The Camera screen should be displayed, and the user should be allowed to access the camera in Manual mode to capture the images.
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

    def test_02_verify_camera_shortcut(self):
        """
        TestRail: C51953837
        Verify the behavior of Run this Shortcut button for Camera
        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Select source from screen
        5. Tap on Camera Scan
        6. Allow camera access if first time
        7. Capture image
        8. Verify image captured successfully
        Expected: The file or image is successfully captured using the camera
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

    def test_03_verify_detect_edges_screen_in_manual_mode(self):
        """
        TestRail: C51953839
        Verify the behavior of detect edges screen under Camera scan in manual mode

        Steps:
        1.Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Capture a file.
        4.Click on Auto or full
        5.Tap on "Next" button in the detect edges screen and observe
        Expected: User able to select the adjust boundaries in detect edges screen and navigate to preview screen
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

    def test_04_verify_back_arrow_in_preview_page(self):
        """
        TestRail: C51953840
        Verify the functionality of back arrow in preview page in Camera Manual mode

        Steps:
        1.Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Capture a file.
        4.Click on Auto or full
        5.Tap on "Next" button in the detect edges screen and observe
        6.click on back button in preview screen
        7.Observe the screen
        Expected: User able to click on back button in preview Screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        # Step 4: Select source from screen
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        # Step 5: Tap on Camera Scan
        self.camera_scan.click_shutter()
        # Step 6: Allow camera access if first time
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        # Step 7: Click on back button in preview screen
        self.driver.back()
        assert self.camera_scan.verify_capture_screen()

    def test_05_verify_back_arrow_with_start_new_scan(self):
        """
        TestRail: C51953841
        Verify the functionality of back arrow in preview page and when user selects on "Yes, Start New Scan" in Camera Manual mode

        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on "Yes, Start New Scan" button and Observe the screen
        Expected: User able to see the camera screen for new Scan
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        # Step 4: Select source from screen
        self.hpx_printer_details.click_select_source_as_camera_scan_btn()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        # Step 5: Tap on Camera Scan
        self.camera_scan.click_shutter()
        # Step 6: Allow camera access if first time
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        # Step 7: Click on back button in preview screen
        self.driver.back()
        # Step 8: Tap on "Yes, Start New Scan" button
        self.hpx_printer_details.click_start_new_scan_btn()
        assert self.camera_scan.verify_capture_screen()