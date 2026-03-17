import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_01_Print_Source:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN]
        cls.photos = cls.fc.fd[FLOW_NAMES.PHOTOS]
        cls.fc.hpx = True
    
    def test_01_pre_conditions(self):
        """
        Description: C41563543
        Steps:
            Install and launch the app.
            Accept consents
            sign in and navigate to rootview
            Add a printer as device
            Tap on the printer card and navigate to device detail page
        Expected Result:
            User should successfully navigate to the printer device detail page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
    
    def test_02_verify_tap_tile_print_documents(self):
        """
        Description: C56339520
        Steps:
            Perform the steps under Pre-conditons case
            Tap on Print Documents and select any file to print and proceed to landing page.
            On the Preview landing page, tap on 'Print Preview'
            On Print Preview page, tap on Print and submit a print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_btn()
    
    def test_03_verify_tap_tile_print_photos(self):
        """
        Description: C56339521
        Steps:
            Perform the steps under Pre-conditons case
            Tap on Print Photos and select any file/files to print and proceed to landing page.
            On the Preview landing page, tap on 'Print Preview'
            On Print Preview page, tap on Print and submit a print job
        Expected Result:
            Verify that the print is successful
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile()
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_print_btn()
    
    def test_04_verify_tap_tile_camera_scan(self):
        """
        Description: C56339522
        Steps:
            Perform the steps under Pre-conditons case
            Tap on Camera scan and capture a file to print and proceed to landing page.
            On the Preview landing page, tap on 'Print Preview'
            On Print Preview page, tap on Print and submit a print job
        Expected Result:
            Verify that the print is successful
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_btn()

    def test_05_verify_tap_scan_tile(self):
        """
        Description: C56339523
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
        self.hpx_printer_details.click_scan_tile()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_btn()

    def test_06_verify_tap_copy_tile(self):
        """
        Description: C56339524
        Steps:
            Perform the steps under Pre-conditons case
            Tap on Copy tile and capture an image to print and proceed to copy landing page.
            On the Preview screen, tap on 'Start Color' or 'Start Black'
            Observe
        Expected Result:
            Verify that the print is successful
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.click_start_color_button()
        self.print_preview.verify_print_sent_text()

    def test_07_verify_tap_copy_tile(self):
        """
        Description: C56339551
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Document and select a file
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_Letter()
        self.print_preview.click_print_btn()
    
    def test_08_verify_successful_print_with_a4_paper(self):
        """
        Description: C56339552
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Document and select a file
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_ISOA4()
        self.print_preview.click_print_btn()
    
    def test_09_verify_successful_print_with_legal_paper(self):
        """
        Description: C56339553
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Document and select a file
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_Legal()
        self.print_preview.click_print_btn()
    
    def test_10_verify_successful_photo_print_with_4x6_paper(self):
        """
        Description: C56339555
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Photo and select a file
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_4x6in()
        self.print_preview.click_print_btn()
    
    def test_11_verify_successful_photo_print_with_5x7_paper(self):
        """
        Description: C56339556
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Photo and select a file
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_5x7in()
        self.print_preview.click_print_btn()

    def test_12_verify_successful_photo_print_on_multiple_page_letter_4x6(self):
        """
        Description: C56339559
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Photo and select a file
            Proceed to Print Preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_4x6in()
        self.print_preview.click_print_btn()
    
    def test_13_verify_successful_photo_print_on_multiple_page_legal_5x7(self):
        """
        Description: C56339558
        Steps:
            Launch the HPX app
            Add any printer to the root
            Tap on printer card and navigate to device detail page
            Tap on Print Photo and select a file
            Make sure photo tray is selected on DS screen
            Proceed to Print preview screen
            Tap Print to submit the print job
        Expected Result:
            Verify that the print is successful.
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_paper_size_drop_down()
        self.print_preview.click_paper_size_5x7in()
        self.print_preview.click_print_btn()

    def test_14_verify_successful_print_of_multi_page_pdf(self):
        """
        Description: C56339532
        Steps:
            Launch the Smart app
            Add any printer on home screen
            Select a multi-page PDF document
            Proceed to landing screen
            Tap on the Print button to proceed to Print preview screen
            Again tap Print to submit the print job
        Expected Result:
            Verify that the print is successful
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
        self.print_preview.select_pdf_file()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_print_btn()
    
    def test_15_verify_successful_print_of_multi_page_txt_document(self):
        """
        Description: C56339733
        Steps:
            Launch the Smart app
            Add any printer on home screen
            Tap on View & Print and select a multi-page txt document
            Proceed to landing screen
            Tap on the Print button to proceed to Print preview screen
            Again tap Print to submit the print job
        Expected Results:
            Verify that the print is successful
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile()
        self.photos.select_hpx_multiple_photos()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_print_btn()
    
    def test_16_verify_navigation_to_preview_page_after_scan(self):
        """
        Description: C56339734
        Steps:
            Launch the smart app
            Tap on scan and scan a photo.
            Proceed to Preview landing page
            Verify the behavior
        Expected Result:
            Verify the user is navigated to the Preview landing page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_scan_btn()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.verify_print_preview_screen()
    
    def test_17_verify_navigation_to_adjust_screen_from_edit(self):
        """
        Description: C56339736
        Steps:
            Launch the Smart app
            Scan or Select a photo and proceed to the preview screen
            Tap on edit icon
            Tap on Adjust option
        Expected Result:
            Verify that user is on Adjust screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_adjust_btn()
        self.print_preview.verify_edit_screen_title()
    
    def test_18_verify_navigation_between_adjust_filters(self):
        """
        Description: C56339737
        Steps:
            Launch the Smart app
            Scan or Select a photo and proceed to the preview screen
            Tap on edit icon
            Tap on Adjust
            Tap on available Adjust options and move slider
            Tap on Done
        Expected Result:
            Verify that the user is able to navigate between the filters.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.click_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_adjust_btn()
        self.print_preview.verify_edit_screen_title()
    
    def test_19_verify_edit_screen_ui_options(self):
        """
        Description: C56339732
        Steps:
            Launch the Smart app
            Select any photo and navigate to preview screen
            Tap on edit icon
            Observe the screen
        Expected Result:
            Verify the edit screen has Adjust, Filters, Corp, Text, Markup options available.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile()
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_paper_mode_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_adjust_mode_btn()
        self.print_preview.click_text_mode_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()