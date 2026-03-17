import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_Copy_Preview:
    @pytest.fixture(scope="class", autouse=True)
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

    def test_01_verify_manual_button(self):
        """
        Description: C51924648
        Verify Auto button is disabled, Click on Capture button and Verify the app behaviour.
        Expected Result:
            Manual image capture should be performed
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
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.verify_manual_button()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_02_verify_auto_button_enable_disable(self):
        """
        Description: C51924646 
        Verify Auto button is disabled, click Auto to enable, and verify Auto button is enabled.
        Expected Result:
             Auto button should be enabled.
        """
        assert self.copy.verify_manual_button() == True, "Auto button should be disabled initially"
        self.copy.select_auto_capture()
        assert self.copy.verify_auto_button()== True, "Auto button should be enabled after clicking"

    def test_03_image_scan_in_auto_mode(self):
        """
        Description: C51924647
        Verify Auto button is disabled, click Auto to enable, and erify the app behaviour.
        Expected Result:
            Automatically image should be scanned and captured without any error.
        """
        self.copy.select_auto_capture()
        self.camera.verify_batch_ui()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_04_object_size_window_in_manual_mode(self):
        """
        Description: C51924649
        Verify Auto button is disabled, click Auto to enable, and erify the app behaviour.
        Expected Result:
            Automatically image should be scanned and captured without any error.
        """
        self.copy.select_manual_button()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_LETTER)

    def test_05_object_size_fileds_in_manual_mode(self):
        """
        Description: C51924651
        Verify Auto button is disabled, click Auto to enable, and erify the app behaviour.
        Expected Result:
            Automatically image should be scanned and captured without any error.
        """
        self.copy.select_manual_button()
        obj_sizes = [attr for attr in dir(i_const.OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(i_const.OBJECT_SIZE, size))

    def test_06_add_page_and_verify_thumbnail(self):
        """
        Test Steps: C51924655
        1. Click on Copy tile.
        2. Capture the image.
        3. In preview screen, click on Add button.
        4. Click on thumbnail.
        5. Verify the captured image in scan thumbnail of camera screen.
        """
        self.copy.select_manual_button()
        self.camera.select_capture_btn()
        self.preview.select_add_page()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_07_auto_mode_capture_and_verify_scanned_image(self):
        """
        Test Steps: C51924656
        1. Click on Auto button.
        2. Capture the image.
        3. Click on scanned pages.
        4. Verify the scanned image.
        """
        self.copy.select_auto_capture()
        self.copy.select_copy_scanned_pages()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_08_capture_and_verify_preview_screen(self):
        """
        Test Steps: C51924657
        1. Click on Capture button.
        2. Verify the preview screen is displayed.
        """
        self.copy.select_manual_button()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_09_verify_popup_in_preview_screen(self):
        """
        Description: C51924658
        click on capture button, verify preview screen, click on back and verify popup.
        Expected Result:
            "Your captured images will be lost if you leave this screen now" Do you wish to continue? popup message should be displayed with Yes and No buttons.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.preview.select_yes_btn()

    def test_10_click_no_on_preview_screen_popup(self):
        """
        Test Steps: C51924659
        1. Click on Capture button.
        2. Verify the preview screen is displayed.
        3. Click on Back button in preview screen.
        4. Click on No button in confirmation dialog.
        5. Verify the preview screen is still displayed.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.verify_an_element_and_click(self.preview.NO_BTN)
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_11_click_yes_on_preview_screen_popup(self):
        """
        Test Steps: C51924660
        1. Capture the image.
        2. Click on back button in preview screen.
        3. Click on Yes button in pop up window.
        4. Verify the screen after exiting preview.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()
        assert self.camera.verify_camera_screen(), "Camera screen was not displayed after exiting preview."