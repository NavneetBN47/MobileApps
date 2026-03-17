import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import FLASH_MODE
pytest.app_info = "SMART"

class Test_Suite_01_Run_Shortcuts(object):

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

    def test_02_verify_camera_shortcut(self):
        """
        TestRail: C5195837
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
        # Step 7: Capture image
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()

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
        # Step 4: Click on Auto or full
        self.camera.verify_adjust_boundaries_nav()
        # Step 5: Tap on "Next" button in the detect edges screen
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

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
        # Step 6: Click on back button in preview screen
        self.preview.select_preview_back()
        # Step 7: Observe the screen
        self.preview.verify_preview_navigate_back_popup()

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
        # Step 7: Tap on "Yes, Start New Scan" button
        self.preview.select_yes_new_scan_btn()

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
        # Step 6: Click on back button in preview screen
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.select_preview_back()
        # Step 7: Tap on "Yes, Go Home" button
        self.preview.select_yes_go_home_btn()
        # Verify the device details page
        self.home.verify_device_details_page()

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
        # Step 6: Click on back button in preview screen
        self.driver.scroll("_shared_smart_task_tile", click_obj=True)
        self.hpxshortcuts.click_existing_shortcuts()
        self.hpxshortcuts.verify_select_source_from_screen_popup()
        self.driver.click("camera_scan_option")
        self.camera.select_allow_access_to_camera_on_popup()
        self.hpxshortcuts.select_firsttime_scan_setting_permission_popup()
        # self.camera.select_camera_option_to_scan()
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.select_preview_back()
        # Step 7: Tap on "No, Add Images" button
        self.preview.select_no_add_img_btn()
        # Verify the camera page for capturing images
        # self.camera.verify_default_capture_mode(capture_mode="manual")

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
        # Step 6: Click on back button in preview screen
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.select_preview_back()
        # Step 7: Tap on "Cancel" button
        self.preview.select_cancel_btn()
        # Verify the user remains in preview page
        self.preview.verify_preview_screen()

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
        # Step 7: Tap on "+" Add button
        self.preview.select_add_page()
        self.camera.select_capture_btn()

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
        # Step 7: Tap on Rotate button
        self.camera.verify_adjust_boundaries_nav()
        self.preview.select_rotate_btn()
        # Verify the image is rotated successfully
        