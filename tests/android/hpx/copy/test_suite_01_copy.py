import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_01_Copy:
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

    def test_01_add_more_pages_to_copy(self):
        """
        C51924675 - Verify the Functionality of Add More Pages to Copy in Manual/Auto
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        Expected Result:
        1, User able to add multiple images Successfully.
        2, All added images should be displayed in the print preview screen and user will swipe right and left to see the added images in the screen.
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
        assert self.print_preview.verify_print_preview_screen()
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.driver.swipe(direction="left")
        self.driver.swipe(direction="right")

    def test_02_delete_single_image_from_two_images(self):
        """
        C51924676 - Verify the functionality to delete a single image out of 2 images in Manual/Auto
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding another image.
        4, Click on the "X"(Remove/Delete) button on the image and keep only single image in print preview screen.
        5, Observe the screen
        Expected Result:
        The user should be able to successfully delete the image, page options should become invisible.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_app_page_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.preview.select_delete_page_icon_in_print_preview()
        assert self.print_preview.verify_more_page_numbers_display() == False, "Print preview does not show page option for only one image after removal."

    def test_03_delete_single_image_from_multiple(self):
        """
        C51924677 - Verify the functionality to delete a single page from multiple copied pages.
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Click on the "X"(Remove/Delete) button on the image and remove single image from multiple images in print preview screen.
        5, Observe the screen
        Expected Result:
        The user is able to delete the image, and the number of pages is updated and visible. The swipe option is also available.
        Number of pages = Number of pages - 1
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
        self.preview.select_delete_page_icon_in_print_preview()
        assert self.print_preview.get_no_pages_from_print_preview() == 2, "Print preview does not show only one image after removal."

    def test_04_delete_all_pages_from_multiple_pages(self):
        """
        C51924678 - Verify the functionality to delete all pages in a multiple copied pages in Manual/Auto
        1, Click on the "Add" button in the print preview screen.
        2, Click on the "Capture" button in manual or auto mode.
        3, Repeat step 1 & 2 for adding more images.
        4, Click on the "X"(Remove/Delete) button for all added images and for final image click on back button popup will come as "Yes & No ".
        5, Click "Yes" Observe the screen
        Expected Result:
        The user lands on the Camera Capture screen with the following options:
        Auto/Manual button, Capture button, Object Size button and Flash button, both of which are clickable
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
        for _ in range(2):
            self.preview.select_delete_page_icon_in_print_preview()
        self.driver.back()
        assert self.print_preview.verify_popup_button()