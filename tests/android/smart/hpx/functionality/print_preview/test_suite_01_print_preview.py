import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_01_print_preview:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN]
        cls.print_quality_tools = cls.fc.fd[FLOW_NAMES.PRINT_QUALITY_TOOLS]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_allow_camera_scan_pop_up(self):
        """
        Description: C44018744
        Steps:
            Fresh install the HPX App
            Tap on Camera Scan tile under Device Detail
            Observe
        Expected Result:
            A pop-up should be displayed asking the user for permission to allow camera access
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.verify_camera_access_allow_txt()
    
    def test_02_fle_marks_for_camera_scan_screen(self):
        """
        Description: C44018745
        Steps:
            1. Four FLE marks are displayed as shown in image
            2. It should be possible to navigate forward/backward using the arrows on the FLE Marks
            3. The numbering on the marks should be correct
            4. It should be possible to close the marks at any step
            5. If user taps the checkmark button on the last FLW mark, the marks will be dismissed.
            6. The FLE marks will only be shown once. If user returns to camera scan screen a second time, the marks will NOT be shown.
        Expected Result:
            All FLE marks should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        # Verifying the 1st coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Adjust scan settings and auto enhancements.', f"Expected 'Adjust scan settings and auto enhancements.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '1 of 4', f"Expected '1 of 4' but got {self.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 2nd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Select the preset you would like to use.', f"Expected 'Select the preset you would like to use.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '2 of 4', f"Expected '2 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 3rd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap here to capture a camera scan.', f"Expected 'Tap here to capture a camera scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '3 of 4', f"Expected '3 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 4th coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap to change the source of your scan.', f"Expected 'Tap to change the source of your scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '4 of 4', f"Expected '4 of 4' but got {self.camera_scan.get_coarchmark_status()}"

    def test_03_fle_marks_for_printer_scan_screen(self):
        """
        Description: C51953679
        Steps:
            1. Four FLE marks are displayed as shown in image
            2. It should be possible to navigate forward/backward using the arrows on the FLE Marks
            3. The numbering on the marks should be correct
            4. It should be possible to close the marks at any step
            5. If user taps the checkmark button on the last FLW mark, the marks will be dismissed.
            6. The FLE marks will only be shown once. If user returns to camera scan screen a second time, the marks will NOT be shown.
        Expected Result:
            All FLW marks should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile()
        # Verifying the 1st coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Adjust scan settings and auto enhancements.', f"Expected 'Adjust scan settings and auto enhancements.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '1 of 4', f"Expected '1 of 4' but got {self.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 2nd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Select the preset you would like to use.', f"Expected 'Select the preset you would like to use.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '2 of 4', f"Expected '2 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 3rd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap here to capture a camera scan.', f"Expected 'Tap here to capture a camera scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '3 of 4', f"Expected '3 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 4th coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap to change the source of your scan.', f"Expected 'Tap to change the source of your scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '4 of 4', f"Expected '4 of 4' but got {self.camera_scan.get_coarchmark_status()}"