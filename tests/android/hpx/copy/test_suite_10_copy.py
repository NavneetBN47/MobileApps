import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_10_Copy:
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
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_13_select_fit_to_page_resize(self):
        """
        C53014631 - Verify the 'Copy' feature when the user selects the 'Fit to Page' option from the 'Resize' option.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        3.Then click on the 'Start black/color button to print. Observe the screen.
        Expected Result:The captured image should be resized to 'Fit to Page' on the 'Print preview' screen. The document should be printed successfully using the 'Fit to Page' size.
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
        self.camera_scan.toggle_capture_mode(manual=True)
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_option("fit_to_page")
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_14_select_fill_page_resize(self):
        """
        C53017732 - Verify the 'Copy' feature, when the user 'Deletes' all the pages.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        3.Then click on the Add button in preview screen.
        4.Repeat the step 2 for 2 or 3 times.
        5.Delete all the pages on the 'Print Preview' screen. Verify the behavior.
        Expected Result:The user should be redirected to the 'Camera' screen.
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
        for _ in range(3):
            self.preview.select_delete_page_icon_in_print_preview()
        assert self.camera_scan.verify_capture_screen()

    def test_15_copy_using_auto_mode(self):
        """
        C52928428 - Verify the 'Copy' feature when the user captures an image using 'Auto' mode.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        3.Then click on the 'Start black/color button to print. Observe the screen.
        Expected Result: The user should be able to print successfully without any error in 'Auto' mode.
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
        self.camera_scan.toggle_capture_mode(manual=False)
        self.camera_scan.verify_auto_is_selected()
        self.camera_scan.click_auto_capture_image()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_16_copy_multiple_copies_multiple_pages(self):
        """
        C53016348 - Verify the functionality of the 'Start Black' button in multiple copies and on Multiple pages.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        3, Repeat step 1 & 2 for adding more images.Tap on copies and select No.of Copies Ex:- 3 or 4
        5, Click on "Start Black" button.Observe the screen.
        Expected Result: User is able to see multiple copies and pages printed successfully. User sees a message stating "Sent".
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
        self.camera_scan.toggle_capture_mode(manual=True)
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()