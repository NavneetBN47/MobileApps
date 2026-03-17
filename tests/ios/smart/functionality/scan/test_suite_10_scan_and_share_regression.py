import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_10_Scan_And_Share_Regression(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.scan = cls.fc.fd["scan"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.files = cls.fc.fd["files"]
        cls.photos = cls.fc.fd["photos"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")

    def test_09_verify_add_photos_image_to_a_scanned_image_preview(self):
        """
        Scan any file, tap add in preview, select files and photos source, select a photo and
        verify photo added to preview successfully - C31299854
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.fc.go_home(stack=self.stack)
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        assert self.common_preview.verify_preview_page_info(is_one_page=True)
        self.common_preview.select_add_page()
        self.select_photos(no_of_photos=2)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE, timeout=12)
        assert self.common_preview.verify_preview_page_info()[1] == 3

    def test_10_verify_addition_of_files_and_photos_to_preview(self):
        """
        Navigate to scan screen, select Files & Photos source, select multiple files and import,
        and verify files opened in preview - C31299855
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.fc.go_home(stack=self.stack)
        self.fc.go_scan_screen_from_home(self.p)
        self.select_photos(no_of_photos=2)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE, timeout=12)
        assert self.common_preview.verify_preview_page_info()[1] == 2

    def test_01_verify_save_share_with_diff_file_types(self):
        """
        Scan image, change file name and format in share/save screen, save and
        verify image saved accordingly - C31297710, C31299835
        """
        file_types = [(self.common_preview.IMAGE_JPG, "jpg"), (self.common_preview.BASIC_PDF, "PDF"), (self.common_preview.IMAGE_PNG, "PNG"), (self.common_preview.IMAGE_TIF, "TIF"), (self.common_preview.IMAGE_HEIF, "HEIF")]
        file_names = []
        file_type_missing = []
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.navigate_to_share_save_screen(self.p)
        btn = self.common_preview.SHARE_SAVE_TITLE if pytest.platform == "IOS" else self.scan.SHARE_BTN
        for file_type in file_types:
            file_name = "scan_image_format_changed_" + file_type[1]
            if self.common_preview.select_file_type(file_type[0]):
                self.fc.save_file_to_hp_smart_files_and_go_home(file_name, btn, file_type[1],
                                                                go_home=False)
                file_names.append(file_name + "." + file_type[1].lower())
            else:
                file_type_missing.append(file_type[0])
            if pytest.platform == "IOS":
                self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
            else:
                self.scan.verify_top_navbar_button_and_click(self.scan.SHARE_BTN)
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.files.verify_file_name_exists(file_name)
        logging.info("File type - {} is missing".format(file_type_missing))
        # cleanup and verify delete all scenarios
        self.fc.go_hp_smart_files_and_delete_all_files()
        assert self.files.is_empty_screen()

    def select_photos(self, no_of_photos=1):
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.select_source_button()
        self.scan.select_files_photos_option()
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_albums_tab()
        assert self.photos.verify_albums_screen()
        self.photos.select_recents_or_first_option()
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=no_of_photos)
        self.photos.verify_multi_selected_photos_screen()
        self.photos.select_next_button()