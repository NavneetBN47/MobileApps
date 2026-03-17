import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import FLASH_MODE
pytest.app_info = "SMART"

class Test_Suite_01_Shortcuts(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        """Class-level setup for Shortcuts test suite 05."""
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.hpxshortcuts = cls.fc.fd["hpx_shortcuts"]
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        
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

        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Click on Existing Shortcut
        self.hpxshortcuts.click_existing_shortcuts()
        # Step 4: Select source from screen
        self.hpxshortcuts.verify_select_source_from_screen_popup()
        # Step 5: Tap on Camera Scan
        self.driver.click("camera_scan_option")
        self.camera.select_allow_access_to_camera_on_popup()
        # Step 6: Allow camera access if first time
        self.hpxshortcuts.select_firsttime_scan_setting_permission_popup()
        # Step 7: Capture image
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        # Step 8: Verify image captured successfully
        self.preview.select_first_document_to_preview_on_shortcuts()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_finish_shortcut_btn()

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
        self.hpxshortcuts.verify_printing_status_btn_changes()

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
        self.hpxshortcuts.verify_printing_status_btn_changes()

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
        # Step 1: Launch app and sign in
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        # Step 2: Click on the printer icon on the root view screen
        self.home.click_to_view_device_page_from_home()
        self.hpxshortcuts.select_pop_up_ok_btn()
        self.driver.swipe()
        self.driver.swipe()
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        # Step 3: Click on Existing Shortcut
        self.hpxshortcuts.click_existing_shortcuts()
        # Step 4: Select source from screen
        self.hpxshortcuts.verify_select_source_from_screen_popup()
        # Step 5: Tap on Camera Scan
        self.driver.click("camera_scan_option")
        self.camera.select_allow_access_to_camera_on_popup()
        # Step 6: Allow camera access if first time
        self.hpxshortcuts.select_firsttime_scan_setting_permission_popup()
        # Step 7: Capture a file and observe
        self.camera.verify_and_select_flash_mode("flash_on")

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
        self.camera.verify_and_select_flash_mode("flash_off")

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
        self.camera.verify_gear_setting_btn()
        self.camera.select_gear_setting_btn()
        self.preview.select_preview_back()

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
        self.camera.select_close_x_btn()
        self.hpxshortcuts.verify_shortcuts_screen()

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
        self.hpxshortcuts.click_existing_shortcuts()
        self.driver.click("camera_scan_option")
        self.camera.select_auto_option()

def test_09_verify_camera_access_auto_mode(self):
        """
        TestRail: C5195855
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
        self.camera.verify_batch_ui(single_element=True)


def test_10_verify_detect_edges_screen_auto_mode(self):
        """
        TestRail: C5195856
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
        self.camera.capture_multiple_photos_by_auto_mode()
        self.camera.select_adjust_boundaries_next()
