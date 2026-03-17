import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_06_Run_Shortcuts:
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

    def test_05_Verify_the_functionality_of_back_arrow_in_preview_page_and_when_user_selects_on_Cancel_in_Camera_Auto_mode(self):
        """
        TestRail: C51953861
        Verify the functionality of back arrow in preview page and when user selects on "Cancel" in Camera Auto mode
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
        6.click on back button in preview screen
        7.Tap on "Cancel" button and Observe the screen
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
        assert self.hpx_printer_details.verify_printer_device_card()

    def test_06_Verify_the_functionality_of_add_button_in_preview_page_in_auto_mode(self):
        """
        TestRail: C51953862
        Verify the functionality of "+" Add button in preview page in auto mode
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
        6.click on "+" Add button in preview screen and Observe the screen
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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.hpx_printer_details.click_add_device_btn_if_exist(raise_e=False)

    def test_07_Verify_the_functionality_of_Rotate_button_in_preview_page_in_Auto_mode(self):
        """
        TestRail: C51953863
        Verify the functionality of Rotate button in preview page in Auto mode
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
        6.click on Rotate button in preview screen and Observe the screen
        Expected: User able to see the image rotated in preview screen.
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
        self.hpx_printer_details.click_rotate_btn()
        assert self.camera_scan.verify_image_is_rotated_in_preview_screen()

    def test_08_verify_the_behavior_of_the_camera_flow_with_the_start_email_option_in_auto_mode(self):
        """
        TestRail: C51953864
        Verify the behavior of the Camera flow with the Start Email option in Auto Mode
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
        7.Tap on "Start email(Shortcut Mail)"
        8.Observe the behavior.
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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()