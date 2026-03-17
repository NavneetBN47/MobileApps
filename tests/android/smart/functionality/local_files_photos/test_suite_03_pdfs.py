from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Pdfs(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Defines flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.flow[FLOW_NAMES.PRINT_PREVIEW]
        cls.job_notification = cls.fc.flow[FLOW_NAMES.JOB_NOTIFICATION]

        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer files for testing
        cls.fc.transfer_test_data_to_device([TEST_DATA.ONE_PAGE_PDF,
                                             TEST_DATA.PDF_3PAGES_WORD_IMAGE,
                                             TEST_DATA.PDF_5PAGES_EMAIL,
                                             TEST_DATA.PDF_6PAGES_FORMATTED_DOC])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("file_name", [TEST_DATA.PDF_3PAGES_WORD_IMAGE,
                                           TEST_DATA.PDF_5PAGES_EMAIL,
                                           TEST_DATA.PDF_6PAGES_FORMATTED_DOC])
    def test_01_pdf_printing(self, file_name):
        """
        Descriptions: C31297709, C31299479, C31297387, C35855648, C35855647, C31297397
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, click on View and Print button on bottom navigation
         4. Click on PDF's button on Files screen.
         5. select  <file_name.pdf>
         6. click on Print button
         7. Go through Print flow in PSP
        Expected Result:
         7. Verify printing job successfully
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name)
        self.preview.select_print_size(self.preview.PRINT_SIZE_4x6, raise_e=False)
        self.fc.flow_preview_make_printing_job(self.p)

    def test_02_pdf_selection(self):
        """
        Description: C31297707, C31297712, C31297713, C31297714
         1. Load home screen and sign into HPID
         2. Select View & Print on bottom navbar
         3. Select PDFs
         4. Tap on a non-pdf file
         5. Long press a PDF
         6. Long press a PDF
         7. Press back
         8. Select PDFs
         9. Select a PDF
         10. Click on Share button
         11. Share via Gmail
        Expected Results:
         4. Verify no files are selected
         5. Verify 1 item is selected
         5. Verify 1 item is selected
         9. Verify preview screen
         11. Verify preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(create_acc=True, verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(TEST_DATA.PDF_3PAGES_WORD_IMAGE, long_press=True)
        self.local_files.verify_selected_file_count(1)
        self.local_files.select_file(TEST_DATA.ONE_PAGE_PDF, long_press=True)
        self.local_files.verify_selected_file_count(1)
        self.driver.press_key_back()
        self.local_files.select_file(TEST_DATA.ONE_PAGE_PDF)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address, TEST_DATA.ONE_PAGE_PDF, from_email=self.email_address)

    def test_03_saved_pdf_in_view_print(self):
        """
        Description: C31297710, C31297715, CC31297716
         1. Load home screen and sign into HPID
         2. Capture image based on img_source param
         3. Select Save
         4. Select PDF file format
         5. Rename file
         6. Select Save
         7. Dismiss Save popup
         8. Navigate to home screen
         9. Select View & Print on bottom navbar
         10. Select PDFs
         11. Select the new PDF file
        Expected Results:
         7. Verify save popup message
         11. Verify preview screen
        """
        self.fc.reset_app()
        file_name = self.test_03_saved_pdf_in_view_print.__name__
        self.fc.flow_load_home_screen(create_acc=True, verify_signin=False)
        self.fc.flow_home_select_network_printer(self.p)
        self.home.dismiss_print_anywhere_popup()
        self.home.select_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.scan.dismiss_coachmark(screen="scanner")
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.verify_adjust_screen(timeout=30)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.rename_file(file_name)
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.select_action_btn()
        self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.click_go_to_home_button()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name + ".pdf")
        self.preview.verify_preview_screen()

    @pytest.mark.parametrize("paper_size", ["a4", "letter", "4_6_in", "5_7_in", "legal"])
    def test_04_pdf_printing_by_media_size(self, paper_size):
        """
        Descriptions: C31297406, C31297407, C31297408, C31297410, C31297411
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, click on View and Print button on bottom navigation
         4. Click on PDF's button on Files screen.
         5. Select  <file_name.pdf>
         6. Click on Print Preview button
         7. Select the paper size
         8. Click on Print button

        Expected Result:
         8. Verify printing job successfully
        """
        paper_size_types = {
            "a4": self.print_preview.PAPER_SIZE_A4,
            "letter": self.print_preview.PAPER_SIZE_LETTER,
            "4_6_in": self.print_preview.PAPER_SIZE_4x6,
            "5_7_in": self.print_preview.PAPER_SIZE_5x7,
            "legal":  self.print_preview.PAPER_SIZE_LEGAL
        }
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(TEST_DATA.ONE_PAGE_PDF)
        self.preview.select_print_size(self.preview.PRINT_SIZE_4x6, raise_e=False)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.print_preview.verify_print_preview_screen()
        self.print_preview.select_paper_size_dropdown()
        if self.print_preview.verify_paper_size_option(paper_size_types[paper_size], invisible=True, raise_e=False):
            pytest.skip("currently printer doesn't support currently paper size {}".format(paper_size))
        self.print_preview.select_paper_size_option(paper_size_types[paper_size])
        self.print_preview.verify_print_preview_screen()
        self.print_preview.select_print_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.print_preview.select_print_job_list_btn()
        self.job_notification.verify_print_jobs_screen()
        self.job_notification.verify_print_job_on_the_list()