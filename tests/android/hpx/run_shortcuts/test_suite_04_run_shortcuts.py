import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_04_Run_Shortcuts:
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
        cls.fc.hpx = True

    def test_06_verify_settings_button_printer_scan(self):
        """
        TestRail: C51953852
        Verify the functionality Settings button in Printer Scan

        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5. .Select source as Printer Scan
        6.Tap on Settings button In the screen right-side top
        7.Click on done button and Observe
        Expected: User able to navigate to printer Scan page
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
        self.camera_scan.select_settings_button()
        assert self.camera_scan.verify_preference_screen()

    def test_07_verify_close_button_printer_scan(self):
        """
        TestRail: C51953853
        Verify the functionality Close button in Printer Scan

        Steps:
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5. Select source as Printer Scan
        6. Tap on Close button In the screen left side top
        7. Observe the behavior
        Expected: User navigate to shortcuts page
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
        self.camera_scan.select_back_button()
        assert self.hpx_printer_details.verify_shortcuts_tile()

    def test_08_verify_camera_access_in_auto_mode(self):
        """
        TestRail: C51953854
        Verify the behavior when the user allows access to the camera in Auto
        Steps:  
        1. Launch app and sign in
        2. Click on the printer icon on the root view screen
        3. Click on Existing Shortcuts
        4. Tap on the "Camera Scan" tile.
        5. Click on Allow option (if your access the camera first time)
        6. Tap on select auto mode.
        7. In auto mode Camera captures the image as searching, scanning and processing
        Expected: The Camera screen should be displayed, and the user should be allowed to access the camera in Auto mode to capture the images.
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
        assert self.camera_scan.verify_auto_is_selected()
        
def test_09_verify_camera_access_auto_mode(self):
        """
        TestRail: C51953855
        Verify the behavior when the user allows access to the camera in Auto mode
        PreConditions:
        1. Install and launch the HPX app
        2. Ensure that the user is logged into the account  
        3. Created shortcut should available
        Steps:
        1. Click on Existing Shortcut
        2. Select the source from the screen  
        3. Tap on Camera Scan
        4. Click on Allow option (if your access the camera first time)
        5. Capture a file and observe
        Expected: The Camera screen should be displayed, and the user should be allowed to access 
                the camera in Auto mode to capture the images
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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()

def test_10_verify_detect_edges_screen_auto_mode(self):
        """
        TestRail: C51953856
        Verify the behavior of detect edges screen under Camera scan in Auto mode
        PreConditions:
        1. Install and launch the HPX app
        2. Ensure that the user is logged into the account
        3. Created shortcut should available
        Steps:
        1. Click on Existing Shortcut
        2. Tap on the "Camera Scan" tile
        3. Capture a file
        4. Click on Auto or full
        5. Tap on "Next" button in the detect edges screen and observe
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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.camera_scan.get_camera_scan_flash_mode()
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()
        