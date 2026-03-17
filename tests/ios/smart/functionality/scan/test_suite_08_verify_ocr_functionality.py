import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_08_Verify_Ocr_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.photos = cls.fc.fd["photos"]
        cls.scan = cls.fc.fd["scan"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(reset=True, stack=cls.stack, username=cls.username, password=cls.password, remove_default_printer=False)
    
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)
    
    def test_02_verify_ocr_options(self):
        """
        C31299460 - Verify 'Convert to Text' page
        C31299462 - Verify default 'Language' behavior
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.verify_preset_mode(self.scan.DOCUMENT)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.select_file_types_dropdown()
        self.common_preview.verify_an_element_and_click(self.common_preview.SEARCHABLE_PDF)
        self.common_preview.verify_an_element_and_click(self.common_preview.WORD_DOCUMENT, click=False)
        self.common_preview.verify_an_element_and_click(self.common_preview.PLAIN_TXT, click=False)
        self.common_preview.select_navigate_back()
        self.common_preview.verify_file_type_selected("Searchable PDF", raise_e=True)
        self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_SAVE_BTN, click=False)    
        self.common_preview.verify_an_element_and_click(self.common_preview.LANGUAGE_OPTION)
        self.common_preview.verify_language_selected("English (US)")
        self.common_preview.select_navigate_back()

    def test_03_verify_end_to_end_scan_files_photos(self):
        """
        C31299479 - End to End Files&Photos
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_source_button()
        self.scan.select_files_photos_option()
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_albums_tab()
        self.photos.verify_albums_screen()
        self.photos.select_recents_or_first_option()
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=1)
        self.photos.select_next_button()
        self.photos.select_next_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.select_file_types_dropdown()
        self.common_preview.verify_an_element_and_click(self.common_preview.SEARCHABLE_PDF)
        self.common_preview.verify_an_element_and_click(self.common_preview.WORD_DOCUMENT)
        self.common_preview.verify_an_element_and_click(self.common_preview.PLAIN_TXT)
        self.common_preview.select_navigate_back()
    
    def test_04_verify_save_original_to_hp_smart(self):
        """
        C31299485 - End to End Printer Scan OCR
        C31299464 - Verify behavior by tapping on 'i' button on language section
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.select_file_type(self.common_preview.SEARCHABLE_PDF)
        self.common_preview.verify_an_element_and_click(self.common_preview.LANGUAGE_INFO_ICON)
        self.common_preview.verify_language_info_btn(displayed=False)
        self.common_preview.verify_an_element_and_click(self.common_preview.LANGUAGE_INFO_ICON)
    
    @pytest.mark.parametrize("option", ["home", "ok"])
    def test_05_verify_share_save_btn(self, option):
        """
        C31299484, C31299831 - End to End Camera Scan OCR
        """
        file_name = "test_05_verify_share_save_btn"
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.rename_file(file_name)
        self.common_preview.select_file_type(self.common_preview.SEARCHABLE_PDF)
        self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_SAVE_BTN)
        self.common_preview.select_save_to_hp_smart_btn()
        if option == "ok":
            self.common_preview.dismiss_file_saved_popup()
            self.common_preview.verify_preview_screen()
        else:
            self.common_preview.click_go_to_home_button()
            self.home.close_organize_documents_pop_up(timeout=5)
            self.fc.go_hp_smart_files_screen_from_home()
            self.files.verify_file_name_exists(f"{file_name}.pdf")
    
    def test_07_verify_file_saved(self):
        """
        C31299459, C31299461 - Verify 'Save Document As' page (iOS only) and "File Type" section
        C31299469, C31299833 - Verify text files job is saved on hp smart files
        """
        file_formats = ["pdf", "docx","txt"]
        files = []
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        
        for format in file_formats:
            self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
            self.common_preview.dismiss_file_types_coachmark()
            self.common_preview.rename_file("test_file_" + format)
            files.append("test_file_" + format + "." + format)
            if format == "pdf":
                self.common_preview.select_file_type(self.common_preview.SEARCHABLE_PDF)
            elif format == "docx":
                self.common_preview.select_file_type(self.common_preview.WORD_DOCUMENT)
            else:
                self.common_preview.select_file_type(self.common_preview.PLAIN_TXT)
            self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_SAVE_BTN)
            self.common_preview.select_save_to_hp_smart_btn()
            self.common_preview.dismiss_file_saved_popup()
            self.common_preview.verify_preview_screen()
        
        self.fc.go_to_home_screen()
        self.fc.go_hp_smart_files_screen_from_home()
        for file in files:
            self.files.verify_file_name_exists(file)
    
    def test_08_ocr_unavailable_for_basic(self):
        """
        C31299586 - Base Account flow
         1. Launch Smart app and sign in with ucde hpid account
         2. Take a Scan
         3. Select Share
        Expected Results:
         3. Verify Below file types are available
          - JPG IMAGE
        """
        self.fc.go_to_home_screen()
        self.home.select_app_settings()
        self.app_settings.select_sign_out_btn()
        self.app_settings.verify_sign_out_confirmation_popup()
        self.app_settings.dismiss_sign_out_popup()
        account = ma_misc.get_hpid_account_info(stack=self.stack, a_type="basic")
        self.fc.go_home(reset=True, stack=self.stack, username=account["email"], password=account["password"])
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.select_file_types_dropdown()
        self.common_preview.verify_file_types([self.common_preview.IMAGE_JPG])