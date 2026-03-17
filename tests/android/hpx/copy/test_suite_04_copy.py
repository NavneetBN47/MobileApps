import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_04_Copy:
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

    def test_13_start_black_with_multiple_copies_single_page(self):
        """
        C51924687, C51949479 - Verify the functionality of Start Black button in multiple copies with a Single page.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Tap on copies and select No.of Copies Ex:- 3 or 4
        4, Click on "Start Black" button.
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
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_14_start_black_with_multiple_copies_multiple_pages(self):
        """
        C51924688, C51949480 - Verify the functionality of Start Black button in multiple copies with a Multiple pages.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Tap on copies and select No.of Copies Ex:- 3 or 4
        5, Click on "Start Black" button.
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
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_15_add_images_print_and_go_home(self):
        """
        C51924689, C51949481 - Verify that the user is navigated to the Home screen once the copy is done
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, if required Repeat step 1 & 2 for adding more images.
        4, Click on "Start Colour/Start Black" button.
        5, Click on "Done" button and Tap "Yes, Go Home" from popup window and observe the screen.
        Expected Result:
        1.Step 4: User sees a message stating "Sent".
        2.Step 5: User navigated to "Home Screen"(Tiles Page).
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

    def test_16_add_images_and_cancel_popup(self):
        """
        C51924690, C51949482 - Verify that the user is navigated to the Print Preview Page once the copy is done and Clicks on "Cancel".
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, if required Repeat step 1 & 2 for adding more images.
        4, Click on "Start Colour/Start Black" button.
        5, Click on "Done" button and Tap "Cancel" Button from popup window and observe the screen.
        Expected Result:
        1.Step 4: User sees a message stating "Sent".
        2.Step 5: User navigated to "Print Preview Page".
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