import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_11_Copy:
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

    def test_01_verify_app_behavior_when_user_clicks_on_copy_tile(self):
        """
        Description: C51949418
        Steps:
            Navigate to device details page.
            Click on Copy tile.
            Verify the behavior.
        Expected Result:
            Camera access allow text is displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        assert self.camera_scan.verify_camera_access_allow_txt()

    def test_02_verify_access_screen_to_camera_when_user_clicks_on_copy_tile_for_first_time_after_logging_in(self):
        """
        Description: C51949421
        Steps:
            Navigate to device details page.
            Click on Copy tile.
            Verify the pop up message.
        Expected Result:
            "No camera access" title is displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.verify_no_camera_access_title()
        assert self.camera_scan.verify_camera_access_allow_txt()

    def test_03_verify_popup_when_user_clicks_on_allow_camera_access_button(self):
        """
        Description: C51949422
        Steps:
            Navigate to device details page.
            Click on Copy tile.
            Click on Allow camera access button in dialog screen.
            Verify the screen.
        Expected Result:
            'Allow HP Smart' pop up should be displayed as per the below screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.click_camera_access_allow()
        assert self.camera_scan.verify_camera_permission_access_screen()

    def test_04_verify_behavior_when_user_allows_access_to_camera(self):
        """
        Description: C51949423
        Steps:
            1.Navigate to device details page.
            2.Click on Copy tile.
            3.Click on Allow camera access button in No camera access pop up window.
            4.Click on "WHILE USING THE APP" from the pop up window.
            5.Verify the app behavior.
        Expected Result:
            Verify Camera capture screen is displayed.
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
        self.print_preview.verify_copy_capture_screen(invisible=False)

    def test_05_verify_capture_button_when_user_captures_any_image_manually(self):
        """
        Description: C51949424
        Steps:
            1.Navigate to device details page.
            2.Click on the Copy tile.
            3.Click on Capture button.
            4.Verify the screen.
        Expected Result:
            Verify that camera scan is redirected to print preview screen
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
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()