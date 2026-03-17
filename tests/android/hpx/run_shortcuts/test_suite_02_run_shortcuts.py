import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.smart.flow_container import FlowContainer
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_02_Run_Shortcuts:
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

    def test_06_verify_back_arrow_with_go_home(self):
        """
        TestRail: C51953842
        Verify the functionality of back arrow in preview page and when user selects on "Yes, Go Home" in Camera Manual mode
        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on "Yes, Go Home" button and Observe the screen
        Expected: User able to navigate to the device details page
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
        self.driver.back()
        self.hpx_printer_details.click_exit_scan_btn()

    def test_07_verify_back_arrow_with_no_add_images(self):
        """
        TestRail: C51953843
        Verify the functionality of back arrow in preview page and when user selects on "No Add images" in Camera Manual mode
        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on "No, Add Images" button and Observe the screen
        Expected: User able to navigate to the camera page for capturing the images.
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
        self.driver.back()
        self.hpx_printer_details.click_add_image_btn()
        assert self.camera_scan.verify_capture_screen()

    def test_08_verify_back_arrow_with_cancel(self):
        """
        TestRail: C51953844
        Verify the functionality of back arrow in preview page and when user selects on "Cancel" in Camera Manual mode
        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on "Cancel" button and Observe the screen
        Expected: User remains in preview page
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
        # Step 6: Allow camera access if first time
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        # Step 7: Click on back button in preview screen
        self.driver.back()
        self.hpx_printer_details.click_add_image_btn()
        assert self.camera_scan.verify_capture_screen()

    def test_09_verify_add_button_functionality(self):
        """
        TestRail: C51953845
        Verify the functionality of "+" Add button in preview page in Manual Mode
        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on "+" Add button and Observe the screen
        Expected: User able to add more images successfully
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
        # Step 7: Tap on "+" Add button
        self.hpx_printer_details.click_add_device_btn_if_exist(raise_e=False)

    def test_10_verify_rotate_button_in_preview(self):
        """
        TestRail: C51953846
        Verify the functionality of Rotate button in preview page in Manual Mode
        Steps:
            1.Click on Existing Shortcut
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Click on Auto or full
            5.Tap on "Next" button in the detect edges screen and observe
            6.click on back button in preview screen
            7.Tap on Rotate button and Observe the screen
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
        # Step 7: Tap on Rotate button
        self.hpx_printer_details.click_rotate_btn()
        assert self.camera_scan.verify_image_rotated_successfully()
        
        