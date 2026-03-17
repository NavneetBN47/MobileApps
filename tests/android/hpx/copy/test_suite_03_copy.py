import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_03_Copy:
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
        
    def test_09_start_color_with_multiple_copies_single_page(self):
        """
        C51924683, C51949475 - Verify the functionality of start colour button in multiple copies with a Single page.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Tap on copies and select No.of Copies Ex:- 3 or 4
        4, Click on "Start Colour" button.
        5, Click on "Done" button and Observe the screen.
        Expected Result:
        1.Step 4: User is able to see multiple copies and with single page printed successfully.
        2.Step 5: User sees a message stating "Sent".
        3.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
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
        self.digital_copy.select_num_of_copies(3) 
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_10_start_color_with_multiple_copies_multiple_pages(self):
        """
        C51924684, C51949476 - Verify the functionality of start colour button in multiple copies with a Multiple pages.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Tap on copies and select No.of Copies Ex:- 3 or 4
        5, Click on "Start Colour" button.
        6, Click on "Done" button and Observe the screen.
        Expected Result:
        1.Step 4: User is able to see multiple copies and pages printed successfully.
        2.Step 5: User sees a message stating "Sent".
        3.Step 6: User sees a popup with the options "Yes, Go Home" and "Cancel".
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
        self.digital_copy.select_num_of_copies(3)
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_11_start_black_in_copy_with_single_page(self):
        """
        C51924685, C51949477 - Verify the functionality of start Black button in copy with a single page.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Click on "Start Black" button.
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
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_12_start_black_in_copy_with_multiple_pages(self):
        """
        C51924686, C51949478 - Verify the functionality of start Black button in copy with a Multiple pages.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Click on "Start Black" button.
        5, Click on "Done" button and Observe the screen.
        Expected Result:
        1.Step 4: User sees a message stating "Sent".
        2.Step 5: User sees a popup with the options "Yes, Go Home" and "Cancel".
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
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()