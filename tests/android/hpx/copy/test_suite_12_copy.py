import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_12_Copy:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_06_verify_flash_mode_functionality_on_camera_screen_when_user_selects_on_option_and_captures_image_manually(self):
        """
        Description: C51949426
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Choose flash mode option to ON in camera screen.
            4.Capture the image.
            5.Verify the app behavior.
        Expected Result:
            Flash mode option should be set to 'ON' and captured image should be flashed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_camera_scan_flash_mode()
        assert self.camera_scan.get_camera_scan_flash_mode() == "Fill Flash", "Flash mode is not set to Fill Flash"
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()

    def test_07_verify_flash_mode_functionality_in_camera_screen_when_user_chooses_off_option_and_captures_image_manually(self):
        """
        Description: C51949427
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Choose flash mode option to 'OFF' in camera screen.
            4.Capture the image
            5.Verify the app behavior.
        Expected Result:
            Flash mode option should be set to 'OFF' and captured image should not be flashed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        for _ in range(4):
            self.camera_scan.click_camera_scan_flash_mode()
            if self.camera_scan.get_camera_scan_flash_mode() == "Flash Off":
                break
        assert self.camera_scan.get_camera_scan_flash_mode() == "Flash Off", "Flash mode is not set to Flash Off"
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()

    def test_08_verify_flash_mode_functionality_in_camera_screen_when_user_chooses_auto_option_and_captures_image_manually(self):
        """
        Description: C51949428
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Choose flash mode option to Auto in camera screen.
            4.Capture the image
            5.Verify the app behavior.
        Expected Result:
            Flash mode option should be set to 'Auto'.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        for _ in range(4):
            self.camera_scan.click_camera_scan_flash_mode()
            if self.camera_scan.get_camera_scan_flash_mode() == "Auto Flash":
                break
        assert self.camera_scan.get_camera_scan_flash_mode() == "Auto Flash", "Flash mode is not set to Auto Flash"
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()

    def test_09_verify_flash_mode_functionality_in_camera_screen_when_user_chooses_torch_option_and_captures_image_manually(self):
        """
        Description: C51949429
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Choose flash mode option to Torch in camera screen.
            4.Capture the image.
            5.Verify the app behavior.
        Expected Result:
            Flash mode option should be set to "Torch" mode.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        for _ in range(4):
            self.camera_scan.click_camera_scan_flash_mode()
            if self.camera_scan.get_camera_scan_flash_mode() == "Torch Flash":
                break
        assert self.camera_scan.get_camera_scan_flash_mode() == "Torch Flash", "Flash mode is not set to Torch Flash"
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()

    def test_10_verify_behavior_when_user_clicks_on_back_button_in_preview_screen(self):
        """
        Description: C51949430
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Choose flash mode option to ON in camera screen.
            4.Capture the image.
            5.Click on the back button on the preview screen.
            6.Verify the app behavior.
        Expected Result:
            The Flash mode should be set to 'ON' again when it is redirected to the camera screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        for _ in range(4):
            self.camera_scan.click_camera_scan_flash_mode()
            if self.camera_scan.get_camera_scan_flash_mode() == "Fill Flash":
                break
        assert self.camera_scan.get_camera_scan_flash_mode() == "Fill Flash", "Flash mode is not set to Fill Flash"
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.driver.back()
        self.print_preview.verify_popup_button()
        self.print_preview.select_leave_button()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        assert self.camera_scan.get_camera_scan_flash_mode() == "Fill Flash", "Flash mode is not set to Fill Flash"