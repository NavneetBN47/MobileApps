"""
Print documents flow and functionality smoke test suite for iOS
"""
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import pytest

pytest.app_info = "SMART"


class Test_Suite_Smoke_03_Print_Documents:
    """
    Print documents flow class for smoke testing for iOS
    """

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        """
        Fixture setup for autouse of go_home add_printer_by_ip functions
        Verify navigation to home page after:
        1. App installation on the mobile device
        2. Clicking on Sign In on the ows screen and navigating to home page
        3. Add printer from the home page by adding IP address
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])

    def test_01_simplified_flow_with_printer_connected(self):
        """
        Description: C33416532, C33416534, C33568582, C33569062, C33569066
            1. Load to Home screen, and select a printer to carousel
            2. Click on Print Documents icon
            3. Allow permission to access Photos
            4. Select a photo from Recent album
            5. Click on Print Preview button from Preview screen
            6. Click on the image from Print Preview screen
            7. Click on Done button
            8. Click on Paper Size option from Print Preview screen

         Expected Result:
            3. Verify user only can select one photo from the Photos list screen
            4. Verify Print size screen if novelli printer gets selected to carousel
            5. Verify Print Preview screen
            6. Verify Image layout screen
            8. Verify  Paper size list screen with items:
               - Paper ready to use
               - Additional paper options
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next_button()
        self.common_preview.select_print_size(
            self.common_preview.DOCUMENT_SIZE_8x11, raise_e=False)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        self.common_preview.select_bottom_nav_btn(
            self.common_preview.PRINT_PREVIEW_BTN)
        self.common_preview.verify_title(
            self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.select_preview_image()
        self.common_preview.verify_transform_screen()
        self.common_preview.select_done()
        self.common_preview.select_print_preview_pan_option_screen()
        self.common_preview.verify_an_element_and_click(
            self.common_preview.PAPER)
        self.common_preview.verify_paper_screen()

    def test_02_verify_printing_from_print_documents_tile(self):
        """
        IOS & MAC:
        verify_printing_from_print_documents- C31297387
        """
        file_name = "test_pdf_file"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name)
        self.fc.select_a_file_and_go_to_print_preview(file_name)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()
        self.fc.go_hp_smart_files_and_delete_all_files()
