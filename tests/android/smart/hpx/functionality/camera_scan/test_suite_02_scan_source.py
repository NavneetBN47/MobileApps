import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "Smart"

class Test_Suite_02_Scan_Source(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.hpx_local_photos = cls.fc.flow[FLOW_NAMES.HPX_LOCAL_PHOTOS]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_source_ui_when_scan_supported_printer_added(self):
        """
        Description: C44018857
            Install and launch the app
            Add a scan supported printer to the device list
            Navigate to Device detail page
            Tap on camera scan or Printer Scan
            Tap on Source icon
        Expected Result:
            Verify the Source UI is as per the Figma
            Source menu should have Camera, Printer and Files& Photos option
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_camera_scan_source()
        assert self.camera_scan.verify_source_files_and_photos()
        assert self.camera_scan.verify_source_camera()
        assert self.camera_scan.verify_source_camera_printer()

    def test_02_verify_user_can_select_source_options_successfully_and_proceed(self):
        """
        Description: C44018859
        Click Scan tile on printer detail page
        Observe the allow access UI
        Tap on the allow option on the screen
        Tap on "Allow" option on the system pop to take pictures and videos
        Expected Result:
            Verify that the camera access screen should be displayed for the first time install and the UI is as per Figma
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.scan.dismiss_coachmark()
        self.camera_scan.click_camera_scan_source()
        self.camera_scan.click_source_camera()
        self.camera_scan.verify_no_camera_access_title()
        assert self.camera_scan.verify_camera_access_allow_txt()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        assert self.camera_scan.get_capture_mode_text() == "Auto", f"Expected 'Auto' but got {self.camera_scan.get_capture_mode_text()}"
        assert self.camera_scan.get_camera_scan_flash_mode() == "Auto Flash", f"Expected 'Flash Off' but got {self.camera_scan.get_camera_scan_flash_mode()}"

    def test_03_verify_default_source_when_user_taps_on_printer_camera_scan(self):
        """
        Description: C44018860
        Click Scan tile on printer detail page
        Observe the allow access UI
        Tap on the allow option on the screen
        Tap on "Allow" option on the system pop to take pictures and videos
        Expected Result:
        verify that camera scan screen should be displayed with manual capture mode option chosen by default and flash mode chosen as Auto by default       
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.scan.dismiss_coachmark()
        self.camera_scan.click_camera_scan_source()
        self.camera_scan.click_source_camera()
        self.camera_scan.verify_no_camera_access_title()
        assert self.camera_scan.verify_camera_access_allow_txt()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        assert self.camera_scan.get_capture_mode_text() == "Auto", f"Expected 'Auto' but got {self.camera_scan.get_capture_mode_text()}"
        assert self.camera_scan.get_camera_scan_flash_mode() == "Auto Flash", f"Expected 'Flash Off' but got {self.camera_scan.get_camera_scan_flash_mode()}"

    def test_04_verify_files_photos_flow(self):
        """
        Description: C44018861
        Click Scan tile on printer detail page
        Observe the allow access UI
        Expected Result:
        verify the Figma design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.scan.dismiss_coachmark()
        self.camera_scan.click_camera_scan_source()
        self.camera_scan.click_files_and_photos()
        assert self.hpx_local_photos.verify_album_name()