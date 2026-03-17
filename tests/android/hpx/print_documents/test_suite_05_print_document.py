import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.flows.android.photos.photos import Photos
from MobileApps.resources.const.android.const import TEST_DATA
import time
from MobileApps.resources.const.android.const import *

pytest.app_info = "HPX"

class Test_Suite_05_Print_Source:
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
        cls.pdf_fn = TEST_DATA.PDF_4PAGES_12MB

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        yield None
        # Clean up Download and Pictures folders after testing
        cls.fc.clean_up_download_and_pictures_folders()
    
    def test_01_verify_page_range_option_C66651678(self):
        """
        Description: C66651678
        Steps:
            Select a multi-page document file to print and proceed to landing screen
            Tap on the Print button to proceed to Print preview screen
            Expand the Print settings by swiping up above the printer name
            Tap on page Range Tap on Manual option
            Enter any page range. Page numbers should be separated by comma(x,x) and page range should be given in this format : x-x
            Tap on Done Submit a print job
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
        self.hpx_printer_details.click_print_documents_tile(raise_e=False)
        self.camera_scan.click_photos_pdfs_btn()
        self.print_preview.click_recent_files_grid_view()
        self.print_preview.click_downloads_grid_view()
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.driver.click("page_range_dropdown_btn")
        self.driver.click("page_option_range")
        self.print_preview.click_printer_preview_swipe_up()
        self.print_preview.select_range_page_option(self.print_preview.SPECIFIC_RANGE_PAGE_OPTION, "2")
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_print_btn() == True

    def test_02_verify_invalid_page_range_option_C66651679(self):
        """
        Description: C66651679
        Steps:
            Launch the HPX app
            Select a multi-page document file to print and proceed to landing screen
            Tap on the Print button to proceed to Print preview screen
            Expand the Print settings by swiping up above the printer name
            Tap on page Range, Tap on Manual option
            Enter any invalid/blank page range (page range not in correct format)
            Observe (For Android)
            Enter the correct range and observe (For Android)
        Expected Result:
            verify that the range is shown in red text as an alert and the Print button is grayed out on the Print Preview screen
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
        self.print_preview.click_print_preview_button()
        self.driver.click("page_range_dropdown_btn")
        self.driver.click("page_option_range")
        self.print_preview.click_printer_preview_swipe_up()
        self.print_preview.select_range_page_option(self.print_preview.SPECIFIC_RANGE_PAGE_OPTION, "-2")
        assert self.print_preview.verify_print_btn() == False

    def test_03_verify_page_quality_as_normal_C66651680(self):
        """
        Description: C66651680
        Steps:
            Launch the HPX app
            Tap on Scan scanner and scan a file and proceed to landing page.
            On the Preview landing page, tap on 'Print'
            Drag the Print setting menu up to see the Print settings
            Tap on Print Quality option to open the 'Print Quality' screen
            Select 'Normal' option and tap on back button
            tap on print and submit a print job
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
        self.print_preview.click_print_preview_button()
        self.print_preview.click_printer_preview_swipe_up()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.driver.click("automatic_option")
        self.driver.click(self.print_preview.QUALITY_NORMAL_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.QUALITY_NORMAL_OPTION) == True

    def test_04_verify_page_quality_as_draft_C66651681(self):
        """
        Description: C66651681
        Steps:
            Launch the HPX app
            Tap on Scan scanner and scan a file and proceed to landing page.
            On the Preview landing page, tap on 'Print'
            Drag the Print setting menu up to see the Print settings
            Tap on Print Quality option to open the 'Print Quality' screen
            Select 'Draft' option and tap on back button
            tap on print and submit a print job
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
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_printer_preview_swipe_up()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.driver.click("automatic_option")
        self.driver.click(self.print_preview.QUALITY_DRAFT_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.QUALITY_DRAFT_OPTION) == True

    def test_05_verify_page_quality_as_best_C66651682(self):
        """
        Description: C66651682
        Steps:
            Launch the HP Smart app
            Tap on Scan scanner and scan a file and proceed to landing page.
            On the Preview landing page, tap on 'Print'
            Drag the Print setting menu up to see the Print settings
            Tap on Print Quality option to open the 'Print Quality' screen
            Select 'Best' option and tap on back button
            tap on print and submit a print job
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
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.driver.click("automatic_option")
        self.driver.click(self.print_preview.QUALITY_BEST_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.QUALITY_BEST_OPTION) == True

    def test_06_verify_orientation_as_automatic_C66651687(self):
        """
        Description: C66651687
        Steps:
            Launch HP Smart app & navigate to homescreen
            select a pdf file
            Navigate to Print Preview screen
            Set Orientation to "Automatic"
            Proceed with printing
        Expected Result:
            Verify the preview and output are in correct orientation
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.driver.click("orientation_auto_option")
        self.driver.click(self.print_preview.QUALITY_BEST_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.QUALITY_BEST_OPTION) == True

    def test_07_verify_orientation_as_portrait_C66651688(self):
        """
        Description: C66651688
        Steps:
            Launch HPX app & navigate to homescreen
            select a pdf file
            Navigate to Print Preview screen
            Set Orientation to "Portrait"
            Proceed with printing
        Expected Result:
            Verify the preview and output are in Portrait
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.driver.click("orientation_auto_option")
        self.driver.click(self.print_preview.ORIENTATION_PORTRAIT_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.ORIENTATION_PORTRAIT_OPTION) == True

    def test_08_verify_orientation_as_landscape_C66651690(self):
        """
        Description: C66651690
        Steps:
            Launch HPX app & navigate to homescreen
            Print -> select a file
            Navigate to Print Preview screen
            Set Orientation to "landscape"
            Proceed with printing
        Expected Result:
            Verify the preview and output are in Landscape
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.driver.click("orientation_auto_option")
        self.driver.click(self.print_preview.ORIENTATION_LANDSCAPE_OPTION)
        assert self.print_preview.verify_print_quality_selected_value(self.print_preview.ORIENTATION_LANDSCAPE_OPTION) == True

    def test_09_preview_screen_on_multipage_pdf(self):
        """
        Description: C56339845
        Steps:
            Launch the Smart app and add a printer to home screen
            select a multi page .Pdf file
            Tap on Print button on the bottom navigation bar of Preview screen
            Observe the Print preview screen
        Expected Result: verify the print preview UI elements
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
        assert self.print_preview.verify_more_options_screen()
        assert self.print_preview.verify_printer_item()
        assert self.print_preview.verify_copies_item()
        assert self.print_preview.verify_color_mode_item()
        assert self.print_preview.verify_print_quality_item()
        assert self.print_preview.verify_orientation_item()