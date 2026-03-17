import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_01_Layout:
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

    def test_01(self):
        """
        Description: C51949431
        Steps:
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

    def test_02(self):
        """
        Description: C51949432
        Steps:
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

    def test_03(self):
        """
        Description: C51949433
        Steps:
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

    def test_04(self):
        """
        Description: C51949434
        Steps:
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

    def test_05(self):
        """
        Description: C51949435
        Steps:
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
        self.driver.back()
        self.print_preview.verify_popup_button()
        self.print_preview.select_leave_button()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        assert self.camera_scan.get_camera_scan_flash_mode() == "Torch Flash", "Flash mode is not set to Torch Flash"

    def test_06(self):
        """
        Description: C51949438
        Steps:
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
        self.camera_scan.click_capture_mode()
        assert self.camera_scan.verify_auto_capture_image()