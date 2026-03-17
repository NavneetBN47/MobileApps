import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
from MobileApps.resources.const.android.const import TEST_DATA
import time
from MobileApps.resources.const.android.const import *

pytest.app_info = "HPX"

class Test_Suite_06_Print_Source:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN]
        cls.digital_copy = cls.fc.fd[FLOW_NAMES.DIGITAL_COPY]
        cls.photos = Photos(cls.driver)
        cls.fc.hpx = True
        cls.jpg_fn = TEST_DATA.JPG_TEXT

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        cls.fc.transfer_test_data_to_device([cls.jpg_fn])

        yield None
        # Clean up Download and Pictures folders after testing
        cls.fc.clean_up_download_and_pictures_folders()

    def test_10_verify_layout_screen(self):
        """
        Description: C56339819
        Steps:
            Perform the steps under Pre-conditons case
            Tap on Scan and scan a file to print and proceed to landing page.
            On the Preview landing page, tap on 'Print Preview'
            On Print Preview page, tap on Print and submit a print job
        Expected Result:
            Verify that the print is successfuls
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_print_btn() == True

    def test_11_cancel_btn_on_verify_layout_screen(self):
        """
        Description: C56339820
        Steps:
            Launch the HP Smart app
            Tap on Print Photos and select a photo to print and proceed
            On the Print Preview page, tap on Layout
            apply some changes using rotate or Resize
            Tap on CANCEL on top bar and Observe
        Expected Result: Verify that the print is successfuls
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_preview_fill_btn()
        self.print_preview.click_print_preview_rotate_btn()
        self.driver.back()
        self.digital_copy.verify_are_you_sure_popup()
        self.driver.back()
        self.print_preview.select_leave_button()
        assert self.hpx_printer_details.verify_print_photos_tile(raise_e=False)
    
    def test_12_preview_screen_on_jpg(self):
        """
        Description: C56339844
        Steps:
            Launch the Smart app and add a printer to home screen
            select an image file (,jpg or .png)
            Tap on Print button on the bottom navigation bar of Preview screen
            Observe the Print preview screen
        Expected Result: Verify that the print page options are displayed correctly
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_documents_tile(raise_e=False)
        self.camera_scan.click_photos_pdfs_btn()
        self.print_preview.click_recent_files_grid_view()
        self.print_preview.click_downloads_grid_view()
        self.print_preview.select_pdf_file()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        assert self.print_preview.verify_printer_item()
        assert self.print_preview.verify_copies_item()
        assert self.print_preview.verify_color_mode_item()
        assert self.print_preview.verify_print_quality_item()
        assert self.print_preview.verify_orientation_item()

    def test_13_preview_screen_on_singlepage_pdf(self):
        """
        Description: C56339846
        Steps:
            Launch the Smart app and add a printer to home screen
            select a single sheet .Pdf file
            Tap on Print button on the bottom navigation bar of Preview screen
            Observe the Print preview screen
        Expected Result:  verify the print preview UI elements are displayed correctly
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_documents_tile(raise_e=False)
        self.camera_scan.click_photos_pdfs_btn()
        self.print_preview.click_recent_files_grid_view()
        self.print_preview.click_downloads_grid_view()
        self.print_preview.select_pdf_file()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        assert self.print_preview.verify_printer_item()
        assert self.print_preview.verify_copies_item()
        assert self.print_preview.verify_color_mode_item()
        assert self.print_preview.verify_print_quality_item()
        assert self.print_preview.verify_orientation_item()