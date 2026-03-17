import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_08_Run_Shortcuts:
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

    def test_13_Verify_the_functionality_Settings_button_in_Printer_Scan_Auto_mode(self):
        """
        TestRail: C51953869
        Verify the functionality Settings button in Printer Scan Auto mode
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1. Click on Existing Shortcut
        2.Tap on the "Printer Scan" tile.
        3.Click on Settings icon in Printer Scan screen and Observe the screen

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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.camera_scan.get_camera_scan_flash_mode()
        self.camera_scan.select_settings_button()
        assert self.camera_scan.verify_preference_screen()

    def test_14_Verify_the_functionality_Close_button_in_Printer_Scan_Auto_mode(self):
        """
        TestRail: C51953870
        Verify the functionality Close button in Printer Scan Auto mode
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1. Click on Existing Shortcut
        2.Tap on the "Printer Scan" tile.
        3..Select source as Printer Scan
        4.Tap on Close button In the screen left side top
        5.Observe
        Expected: User navigate to shortcuts page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.shortcuts.click_scanner_btn()
        self.scan.dismiss_coachmark()
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        assert self.scan.verify_successful_scan_job()

    def test_15_Verify_the_behavior_of_the_Run_this_Shortcut_button_after_selecting_the_source_as_Files_and_Photos(self):
        """
        TestRail: C51953871
        Verify the behavior of the Run this Shortcut button after selecting the source as Files and Photos
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1. Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Tap on Files and Photos
        4.User can select the files from photos or folders
        5.Click on Next and observe the Screen
        Expected: The selected photo or File successfully imported
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_printer_details.click_default_shortcuts()
        self.driver.click("File_and_Photo_btn")
        self.driver.click("select_my_photos_btn")
        self.photos.select_single_photo()
        assert self.hpx_printer_details.verify_your_shortcut_is_running_title()