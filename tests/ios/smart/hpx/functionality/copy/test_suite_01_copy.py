import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import FLASH_MODE

pytest.app_info = "SMART"

class Test_Suite_01_Copy:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.camera = cls.fc.fd["camera"]
        cls.copy = cls.fc.fd["copy"]
        cls.preview = cls.fc.fd["preview"]

    def test_01_verify_allow_camera_access_popup(self):
        """
        Description: C51924631
                1. Click copy tile on printer detail page
                2. Observe
            Expected Result:
                2. No camera access dialog box will display.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.verify_allow_access_to_camera_popup()

    def test_02_verify_copy_tile(self):
        """
        Description: C51924004
                1. Click copy tile on printer detail page
                2. Observe
            Expected Result:
                2. User should be able to access the copy tile without any errors and issues.
        """
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.verify_copy_tile_screen()
        self.camera.verify_flash_btn()
        self.camera.verify_camera_btn()

    def test_03_copy_not_allow_camera_access_popup(self):
        """
        Description: C51924632
                1. Click copy tile on printer detail page
                2. Click on Allow camera access button in "No camera access" pop up window.
            Expected Result:
                2.Camera capture screen should be displayed after allowing the access
        """
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.verify_camera_btn()

    def test_04_verify_display_of_manual_button(self):
        """
        Description: C51924645 Verify the display of the manual button.
                1. Click on Copy tile.
                2. Verify on the manual button.
            Expected Result:
                2. User should be in manual mode under Camera screen
        """
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.copy.verify_manual_enabled()

    def test_05_click_and_verify_capture_button(self):
        """
        Description: C51924633
                1. Click copy tile on printer detail page
                2. Observe
            Expected Result:
                2. User should be able to access the copy tile without any errors and issues.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_06_verify_copy_screen_in_manual(self):
        """
        Description: C51924635
                1.Click on Copy tile. 
                2.Choose flash mode option to "ON" in camera screen. Capture the image.
                3.Verify the screen.
            Expected Result:
                3.The user should see that the Flash mode option is set to "ON," and the captured image should be a flashed image.
        """
        self.copy.select_manual_button()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_07_verify_copy_screen_flash_on(self):
        """
        Description: C51924636
                1.Click on Copy tile. 
                2.Choose flash mode option to "ON" in camera screen and click on Capture button.
                3.Verify the screen.
            Expected Result:
                3.The user should see that the Flash mode option is set to "ON," and the captured image should be a flashed image.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_ON)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_08_verify_copy_screen_flash_off(self):
        """
        Description: C51924637
                1.Click on Copy tile. 
                2.Choose flash mode option to "OFF" in camera screen and click on Capture button.
                3.Verify the screen.
            Expected Result:
                3.The user should see that the Flash mode option is set to "OFF," and the captured image should be a flashed image.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_OFF)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_09_verify_copy_screen_flash_torch(self):
        """
        Description: C51924638
                1.Click on Copy tile. 
                2.Choose flash mode option to "TORCH" in camera screen and click on Capture button.
                3.Verify the screen.
            Expected Result:
                3.The user should see that the Flash mode option is set to "TORCH," and the captured image should be a flashed image.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_TORCH)
        self.camera.select_capture_btn()    
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_10_verify_copy_screen_flash_auto(self):
        """
        Description: C51924639
                1.Click on Copy tile. 
                2.Choose flash mode option to "AUTO" in camera screen and click on Capture button.
                3.Verify the screen.
            Expected Result:
                3.The user should see that the Flash mode option is set to "AUTO," and the captured image should be a flashed image.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_AUTO)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_11_verify_flash_on_auto_capture(self):
        """
        Description: C51924640 Verify Flash On, Auto mode, and Capture functionality.
                1. Click on Copy tile.
                2. Set Flash mode to "Flash On".
                3. Set mode to "Auto".
                4. Click on Capture button.
                5. Verify the screen.
            Expected Result:
                5. The user should see that the Flash mode is set to "Flash On," Auto mode is active, and the captured image is displayed correctly.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_ON)
        self.copy.select_auto_capture()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_12_verify_flash_off_auto_capture(self):
        """
        Description: C51924641 Verify Flash Off, Auto mode, and Capture functionality.
                1. Click on Copy tile.
                2. Set Flash mode to "Flash Off".
                3. Set mode to "Auto".
                4. Click on Capture button.
                5. Verify the screen.
            Expected Result:
                5. The user should see that the Flash mode is set to "Flash Off," Auto mode is active, and the captured image is displayed correctly.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_OFF)
        self.copy.select_auto_capture()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_13_verify_flash_torch_auto_capture(self):
        """
        Description: C51924642 Verify Flash Torch, Auto mode, and Capture functionality.
                1. Click on Copy tile.
                2. Set Flash mode to "Flash Torch".
                3. Set mode to "Auto".
                4. Click on Capture button.
                5. Verify the screen.
            Expected Result:
                5. The user should see that the Flash mode is set to "Flash Torch," Auto mode is active, and the captured image is displayed correctly.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_TORCH)
        self.copy.select_auto_capture()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_14_verify_flash_auto_auto_capture(self):
        """
        Description: C51924643 Verify Flash Auto, Auto mode, and Capture functionality.
                1. Click on Copy tile.
                2. Set Flash mode to "Flash Auto".
                3. Set mode to "Auto".
                4. Click on Capture button.
                5. Verify the screen.
            Expected Result:
                5. The user should see that the Flash mode is set to "Flash Auto," Auto mode is active, and the captured image is displayed correctly.
        """
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_AUTO)
        self.copy.select_auto_capture()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_15_verify_copy_screen_in_auto(self):
        """
        Description: C51924634
                1.Click on Copy tile. 
                2.In auto mode Camera captures the image as searching, scanning and processing.
                3.Verify the screen.
            Expected Result:
                3.The Camera screen should be displayed, and the user should be allowed to access the camera in Auto mode to capture the images.
        """
        self.copy.select_auto_capture()
        self.camera.verify_batch_ui()
        self.camera.verify_camera_btn()
        self.copy.select_manual_button()

    def test_16_verify_close_button(self):
        """
        Description: C51924644 Verify the functionality of the Close button.
                1. Click on Copy tile.
                2. Click on the Close button.
                3. Verify the screen.
            Expected Result:
                3. The user should see that the screen is closed and navigated back to the previous screen.
        """
        self.copy.select_x_to_close()
        self.preview.select_yes_btn()
        self.home.verify_device_details_page()