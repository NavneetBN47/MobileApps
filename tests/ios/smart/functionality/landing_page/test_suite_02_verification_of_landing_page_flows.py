import pytest
from time import sleep
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "SMART"

class Test_Suite_02_Verification_Of_Landing_Page_Flows(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.edit = cls.fc.fd["edit"]
        cls.photos = cls.fc.fd["photos"]
        cls.files = cls.fc.fd["files"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(reset=True, stack=cls.stack)

    @pytest.fixture(scope="function", autouse="true")
    def reset_to_home(self):
        self.fc.go_to_home_screen()

    @pytest.fixture(scope="class", autouse="true")
    def load_files(self):
        file_paths = ["pdf/4pages.pdf", "xlsx/4pages.xlsx", "docx/4pages.docx", "pptx/4pages.pptx"]
        file_names = [f"{path.split('/')[-1].split('.')[0]}_{path.split('/')[0]}.{path.split('/')[-1].split('.')[1]}" for path in file_paths]

        for file_path, file_name in zip(file_paths, file_names):
            full_path = f"resources/test_data/documents/{file_path}"
            self.driver.push_file(BUNDLE_ID.FIREFOX, ma_misc.get_abs_path(full_path), file_name=file_name)
            sleep(1)

        yield None

        for file_name in file_names:
            self.driver.delete_file(BUNDLE_ID.FIREFOX, file_name)

    def test_01_verify_ui_for_new_preview_landing_screen_single_photo(self):
        """
        C33560122: Verify the UI for new preview landing screen for single photo
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=2)
        self.common_preview.select_edit()
        self.edit.verify_edit_page_title()
        self.common_preview.select_cancel()
        self.common_preview.select_navigate_back()
        self.photos.verify_photos_screen()

    def test_02_verify_ui_for_new_preview_landing_screen_document(self):
        """
        C33560115: Verify the UI for new preview landing screen for document
        """
        self._navigate_to_documents_and_select_file("4pages_pdf")
        _, total_pages  = self.common_preview.verify_preview_page_info()
        assert total_pages == 4, "PDF fails to have of 4 pages in the preview screen."

    def test_03_verify_ui_for_new_preview_landing_screen_multiple_photos(self):
        """
        C33560120: Verify the UI for new preview landing screen for multiple photos
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=4)
        _, total_pages = self.common_preview.verify_preview_page_info()
        assert total_pages == 4, "Preview screen fails to have 4 pages for the 4 selected photos."
        for image in range(1,5):
            self.common_preview.verify_delete_page_x_icon()
            current_page, _ = self.common_preview.verify_preview_page_info()
            assert current_page == image, f"Preview screen fails to show the correct page number. Expected: {image}, Actual: {current_page}"
            self.driver.swipe(self.common_preview.PREVIEW_IMAGE, direction="right", per_offset=1)
        self.common_preview.select_navigate_back()
        self.photos.verify_photos_screen()

    def test_04_verify_the_preview_for_xlsx_formats(self):
        """
        C33560116: Verify the preview for xlsx files
        """
        self._navigate_to_documents_and_select_file("4pages_xlsx")
        assert self.common_preview.verify_preview_page_info(is_one_page=True), "XLSX file fails to have only 1 page in the preview screen."
    
    def test_05_verify_the_preview_for_docx_formats(self):
        """
        C33560118: Verify the preview for docx files
        """
        self._navigate_to_documents_and_select_file("4pages_docx")
        assert self.common_preview.verify_preview_page_info(is_one_page=True), "DOCX file fails to have only 1 page in the preview screen."

    def test_06_verify_the_preview_for_pptx_formats(self):
        """
        C33560117: Verify the preview for pptx files
        """
        self._navigate_to_documents_and_select_file("4pages_pptx")
        _, total_pages  = self.common_preview.verify_preview_page_info(timeout=55)
        assert total_pages == 4, "PPTX file fails to have 4 pages in the preview screen."

    def test_07_verify_choose_your_printer_button(self):
        """
        C33560124: Verify "Choose your printer" button on Print Preview page
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.common_preview.select_bottom_nav_btn(self.common_preview.PRINT_PREVIEW_BTN)
        self.common_preview.verify_no_printer_on_printer_preview_screen()

    def _navigate_to_documents_and_select_file(self, file_name):
        self.fc.go_to_home_screen()
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.files.select_all_files_image()
        self.files.navigate_to_application_folder("Firefox")
        self.files.select_item_cell(file_name)
        self.common_preview.verify_preview_screen()