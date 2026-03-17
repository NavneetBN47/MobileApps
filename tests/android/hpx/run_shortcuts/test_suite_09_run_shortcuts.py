import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
import time

pytest.app_info = "HPX"

class Test_Suite_09_Run_Shortcuts:
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

    def test_01_Verify_the_functionality_of_back_arrow_in_preview_page(self):
        """
        TestRail: C51953872
        Verify the functionality of back arrow in preview page
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1.Click on Existing Shortcut
        2.Tap on the "Files & Photos".
        3. Click on albums and Select the image
        4.click on back button in preview screen
        5.Observe the screen
        Expected: User able to click on back button in Files&photos Screen will navigate to previous page
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
        self.driver.back()
        assert self.driver.wait_for_object("select_my_photos_btn", timeout=5)

    def test_02_Verify_the_behavior_of_the_preview_screen_user_able_to_document_name(self):
        """
        TestRail: C51953873
        Verify user is able to navigate to previous screen on tapping back arrow in Print Quality Tools
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1.Click on Existing Shortcut
        2.Select the source from the screen
        3.Tap on Files and Photos
        4.User can select the files from photos or folders
        5.Click on Next
        6.In preview screen provide document name
        7.click on Start button.
        Expected: User able to click on back button in Print Quality Tools Screen will navigate to previous page
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
        self.hpx_printer_details.click_start_email_btn()

    def test_03_Verify_the_behavior_of_finish_shortcut_button(self):
        """
        TestRail: C51953874
        Verify the behavior of finish shortcut button
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1.Click on Existing Shortcut
        2.Select the source from the screen
        3.Tap on Files and Photos
        4.User can select the files from photos or folders
        5.Click on Next
        6.In preview screen provide document name
        7.click on Start button.
        8.Click on Finish Shortcut button

        Expected: User should be navigated to home screen after clicking on Finish Shortcut button
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
        self.hpx_printer_details.click_start_email_btn()

    def test_04_Verify_the_behavior_of_print_save_and_email_page_processing_in_Files_and_Photos(self):
        """
        TestRail: C51953875
        Verify the behavior of print, save, and email page processing in Files and Photos
        PreConditions:
        1.Install and launch the HPX app.
        2.Ensure that the user is logged into the account.
        3.Created shortcut should available
         Steps:
        1.Click on Existing Shortcut
        2.Tap on the "Camera Scan" tile.
        3.Capture a file.
        4.Tap "Next" on the Adjust Boundaries screen.
        5.Navigate to the Preview page.
        6.Tap on "Start email(Shortcut Mail).
        7.User will select desired options(Paper Size, No of Copies,etc) and clicks on Finish Shortcut.
        8.Observe the screen

        Expected: User should be navigated to home screen after clicking on Finish Shortcut button
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
        self.hpx_printer_details.click_start_email_btn()
        assert self.hpx_shortcuts.verify_your_shortcut_is_running_title()

