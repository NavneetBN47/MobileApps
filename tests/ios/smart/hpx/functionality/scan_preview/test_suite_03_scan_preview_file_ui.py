import pytest
import logging
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_03_Scan_Preview_File_UI:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        cls.cpreview = cls.fc.fd["common_preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.photos = cls.fc.fd["photos"]
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_share_save_screen_ui(self):
        """
        C44018915: Verify Share/Save screen UI after scan
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Check the "Share/Save" UI.
        Expected:
        1. The "Share/Save" screen shows as per design. (If HP+ advance scan or HP Pro account, "Smart File name" option displays under file name area)
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.preview.verify_file_size_option()
        self.preview.verify_file_type_option()

    def test_02_file_type_screen_ui(self):
        """
        C44018916: Verify File Type screen UI after scan
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap "File Type" option.
        5. Check the "File Type" UI.
        Expected:
        1. The "File Type" screen shows as per design. (If HP+ advance scan account or HP Pro account, more file types will display)
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.cpreview.select_file_types_dropdown()
        self.cpreview.verify_file_types([self.cpreview.IMAGE_JPG, self.cpreview.BASIC_PDF, self.cpreview.IMAGE_PNG, self.cpreview.IMAGE_TIF, self.cpreview.IMAGE_HEIF])

    def test_03_file_size_screen_ui(self):
        """
        C44018918: Verify File Size screen UI after scan
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap "File Size" option.
        5. Check the "File Size" UI.
        Expected:
        1. The "File Size" screen shows as per design (options: Actual, Large, Medium, Small).
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.cpreview.select_file_size()
        self.cpreview.verify_file_types([self.cpreview.FILE_SIZE_ACTUAL, self.cpreview.FILE_SIZE_SMALL, self.cpreview.FILE_SIZE_LARGE, self.cpreview.FILE_SIZE_MEDIUM])

    def test_04_share_save_processing_modal(self):
        """
        C44018919: (iOS) Share/Save - Processing
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap Continue button.
        Verify:
        1. The "Processing..." modal pops up and shows as per design.
        2. The OS share list displays after the "Processing..." pop up.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.preview.select_continue_btn()
        assert self.preview.verify_airdrop_icon(), 'OS share list did not display after processing modal.'

    def test_05_share_save_cancel_processing(self):
        """
        C44018920: (iOS) Share/Save - Cancel Processing
        Steps:
        1. Click Printer Scan tile.
        2.Scan or import file to preview screen.
        3. Click "Save"/"Share" button.
        4. Click Gear button.
        5. Choose "Save Image As" drop list.
        6. Choose "Save Document As" drop list.
        Verify the following options show and are selectable:
        a. Image (*.jpg)
        b. Basic PDF
        c. PNG
        d. TIF
        f. HEIF
        g. Searchable PDF
        h. Word Document (*.docx)
        i. Plain Text (*.txt)
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.home.select_settings_icon()
        self.preview.select_save_image_as_btn()
        for file_type in [self.cpreview.BASIC_PDF, self.cpreview.IMAGE_JPG, self.cpreview.IMAGE_PNG, self.cpreview.IMAGE_TIF, self.cpreview.IMAGE_HEIF]:
            self.cpreview.select_file_type_option_in_file_type_screen(file_type)
            self.cpreview.verify_file_type_option_in_file_type_screen(file_type, raise_e=True)
        self.preview.select_save_document_as_btn()

    def test_06_file_saving_defaults_screen_ui(self):
        """
        C44018921: Verify File Saving Defaults screen UI
        Pre-conditions:
        - Enable Web MFE and Reskin UI for HPX in Settings > HP Smart > HPX.
        - App is installed, user is signed in, printer is added, and device details page is open.
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap the gear button.
        5. Check the "File Saving Defaults" UI.
        Expected:
        1. The "File Saving Defaults" screen shows as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.home.select_settings_icon()
        self.preview.verify_file_saving_defaults_screen()
        self.preview.verify_default_save_image_as_option()
        self.preview.verify_default_save_document_as_option()

    def test_07_save_image_as_screen_ui(self):
        """
        C44018922: Verify Save Image As screen UI
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap the gear button.
        5. Tap "Save Image As" option.
        6. Check the "Save Image As" UI.
        Expected:
        1. The "Save Image As" screen shows as per design (should display: Image (*.jpg), Basic PDF, PNG, TIF, HEIF).
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.home.select_settings_icon()
        self.preview.select_save_image_as_btn()
        self.cpreview.verify_file_types([self.cpreview.IMAGE_JPG, self.cpreview.BASIC_PDF, self.cpreview.IMAGE_PNG, self.cpreview.IMAGE_TIF, self.cpreview.IMAGE_HEIF])

    def test_08_save_document_as_screen_ui(self):
        """
        C44018922: Verify Save document As screen UI
        Steps:
        1. Tap "Camera Scan" tile.
        2. Capture a photo and go to preview screen.
        3. Tap "Share/Save" button.
        4. Tap the gear button.
        5. Tap "Save document As" option.
        6. Check the "Save document As" UI.
        Expected:
        1. The "Save document As" screen shows as per design (should display: Image (*.jpg), Basic PDF, PNG, TIF, HEIF).
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.home.select_settings_icon()
        self.preview.select_save_document_as_btn()
        self.cpreview.verify_file_types([self.cpreview.IMAGE_JPG, self.cpreview.BASIC_PDF, self.cpreview.IMAGE_PNG, self.cpreview.IMAGE_TIF, self.cpreview.IMAGE_HEIF])

    def test_09_printing_from_scan_preview(self):
        """
        C44018926: Verify printing is successful from Scan preview screen
        Steps:
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print preview" button.
        4. Tap "Print" button.
        Expected:
        - The job can be printed out successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_print_preview_button()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_print_btn()

    def test_10_shortcuts_from_scan_preview(self):
        """
        C44018928: Verify Shortcuts is successful from Scan preview screen
        Steps:
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Shortcuts" button.
        4. Select a shortcut from the list.
        Expected:
        - Verify the shortcut job can be sent out successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_shortcuts_on_preview_screen()
        self.preview.select_swipe_up_documents_on_shortcuts()
        self.preview.select_first_document_to_preview_on_shortcuts()
        self.preview.select_finish_shortcut_btn()
        
    def test_11_rotate_icon_at_bottom(self):
        """
        C44018929: Rotate icon at bottom
        Steps:
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap the rotate icon at the bottom right corner of the image.
        Expected:
        - Verify the image can be rotated correctly.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_rotate_btn()
        self.cpreview.select_auto_rotate_image(index=1)
        self.cpreview.verify_is_image_selected()
        self.preview.select_rotate_btn()

    def test_12_print_preview_ui(self):
        """
        C44018930: Scan First Flow: Verify Print Preview UI
        Steps:
        1. Tap scan tile.
        2. Perform a scan job and go to preview screen.
        3. Tap "Print Preview" button.
        Expected:
        1. The print preview screen is shown as per Figma (design).
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_print_preview_button()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_print_btn()
        self.preview.verify_print_preview_screen()

    def test_13_mobile_fax_ui_from_scan_preview(self):
        """
        C44018931: Scan First Flow: Verify Mobile Fax UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Mobile Fax" button.
        4. Tap "Continue to Fax" (iOS only).
        Expected:
        - For iOS, the Fax preview can display after tapping "Mobile Fax" button.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_mobile_fax_on_preview()
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.preview.verify_mobile_fax_screen()

    def test_14_shortcuts_ui_from_scan_preview(self):
        """
        C44018932: Scan First Flow: Verify Shortcuts UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Shortcuts" button.
        Expected:
        1. When user is not signed in, the "Save time with shortcuts" UI can display.
        2. When user is signed in, the available shortcuts UI is displayed as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_shortcuts_on_preview_screen()
        self.preview.select_swipe_up_documents_on_shortcuts()
        self.preview.select_first_document_to_preview_on_shortcuts()
        self.preview.select_finish_shortcut_btn()

    def test_15_send_print_job_flow_ui(self):
        """
        C44018933: (iOS) Send print job flow UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print Preview" button.
        4. Tap "Print" button.
        Expected:
        - Verify the job can be sent out and the UI is shown as per Figma.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_print_preview_button()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_print_btn()
        self.preview.verify_print_screen()

    def test_16_print_settings_ui_from_print_preview(self):
        """
        C44018935: Print Settings UI from Print Preview
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print Preview" button.
        4. Tap each option of print settings to check the UI.
        Expected:
        - Verify the print settings can be shown as per Figma (design).
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_print_preview_button()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_printer_name(self.printer_name)
        self.preview.verify_printer_name_ui(self.printer_name)
        self.preview.select_print_preview_button()
        self.preview.select_paper_option_btn()
        self.preview.verify_paper_screen_in_print_page()
        self.preview.select_print_preview_button()
        self.driver.scroll("print_quality_txt", click_obj=True)
        self.preview.verify_paper_quality_in_print_page()
        self.preview.select_print_preview_button()
        self.driver.scroll("color_option_txt", click_obj=True)
        self.preview.verify_color_options_in_print_page()
        self.preview.select_print_preview_button()
        
    def test_17_transform_ui_from_print_preview(self):
        """
        C44018936: (iOS) Verify scan flow print preview - transform UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print Preview" button.
        4. Tap the image to show Transform UI.
        Expected:
        - Verify the transform UI is shown as per Figma/design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_print_preview_button()
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_page_cell(0)
        self.cpreview.verify_transform_screen()
        self.cpreview.verify_resize_move_screen()
        self.cpreview.select_resize_move_btn()
        self.preview.verify_resize_and_move_options()
        self.preview.select_cancel_btn_on_delete()
        self.preview.select_rotate_btn()
        self.cpreview.verify_rotate_options_on_print_screen()

    def test_18_verify_addition_of_scanned_pages_source_scanner(self):
        """
        C44018937: Verify addition of scanned pages - source scanner
        1. Tap scan tile.
        2. Perform a scan job and go to preview screen.
        3. Tap "+ Add" button.
        4. Perform another scan job.
        5. Repeat steps 3 and 4 to add several scan jobs and continue to Preview landing screen.
        Expected Result:
        - Verify each scan job can be completed successfully and all scanned pages are present in the preview.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        for _ in range(3):
            self.preview.select_add_page()
            self.scan.select_scan_job_button()
            self.preview.nav_detect_edges_screen()
            self.preview.verify_preview_screen()

    def test_19_verify_addition_of_scanned_pages_source_files_photos(self):
        """
        C44018938: Verify addition of scanned pages - source Files & Photos
        1. Tap scan tile.
        2. Perform a scan job and go to preview screen.
        3. Tap "+ Add" button.
        4. Tap the source button and change source to "Files & Photo".
        5. Select a photo and go to preview screen.
        6. Repeat steps 3 to 5 and add several scan jobs and continue to Preview landing screen.
        Expected Result:
        - Verify each scan job can be completed successfully and all scanned pages are present in the preview.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.camera.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_FILES)
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next()
        self.photos.select_next()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        for _ in range(3):
            self.preview.select_add_page()
            self.scan.select_scan_job_button()
            self.preview.nav_detect_edges_screen()
            self.preview.verify_preview_screen()
