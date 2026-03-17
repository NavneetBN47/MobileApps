import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_02_Copy:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.home = cls.fc.fd[FLOW_NAMES.HOME]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.system_flow = cls.fc.flow[FLOW_NAMES.SYSTEM_FLOW]
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_05_click_back_from_multiple_pages(self):
        """
        C51924679 - Verify the functionality of Back button when user added multiple pages by clicking on add button in Manual/Auto
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Click on back button popup will come as "Yes & No ".
        5, Click "Yes" Observe the screen
        6, Click "No" Observe the screen
        Expected Result:
        Step 5:The user lands on the Camera Capture screen with the following options:
        Auto/Manual button, Capture button, Object Size button and Flash button, both of which are clickable
        Step 6: User will see the preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.driver.back()
        self.print_preview.select_leave_button()
        assert self.hpx_printer_details.verify_camera_scan_tile()

    def test_06_click_back_from_single_page(self):
        """
        C51924680 - Verify the functionality of Back button when user add single page by clicking on add button in Manual/Auto
        1, Click on the "Capture" button in manual or auto mode for adding single page.
        2, Click on back button popup will come as "Yes & No ".
        3, Click "Yes" Observe the screen
        4, Click "No" Observe the screen
        Expected Result:
        Step 3:The user lands on the Camera Capture screen with the following options:
        Auto/Manual button, Capture button, Object Size button and Flash button, both of which are clickable
        Step 4: User should see the preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.driver.back()
        self.print_preview.select_leave_button()
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.print_preview.verify_copy_capture_screen()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.driver.back()
        self.print_preview.select_cancel_button()
        assert self.print_preview.verify_print_preview_screen()

    def test_07_start_color_from_copy_single_page(self):
        """
        C51924681, C51949473 - Verify the functionality of start colour button in copy with a single page
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Click on "Start Colour" button.
        4, Click on "Done" button and Observe the screen.
        Expected Result:
        1.Step 3: User sees a message stating "Sent".
        2.Step 4: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_08_start_color_from_copy_multiple_pages(self):
        """
        C51924682, C51949474 - Verify the functionality of start colour button in copy with a Multiple pages.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Click on "Start Colour" button.
        5, Click on "Done" button and Observe the screen.
        Expected Result:
        1,Step 4: User sees a message stating "Sent".
        2,Step 5: User sees a popup with the options "Yes, Go Home" and "Cancel".
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()