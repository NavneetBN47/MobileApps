import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_01_Ios_Smart_Scan_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.go_home(stack=cls.stack)
        cls.camera = cls.fc.fd["camera"]
        cls.scan = cls.fc.fd["scan"]
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.edit = cls.fc.fd["edit"]
        cls.files = cls.fc.fd["files"]

    def test_01_verify_first_time_scan_popup(self):
        """
        IOS & MAC:
        C31299892 - verify bottom action bar scan button and first time pop_up
        C31299398 - Verify 'Document' is default option for preset
        C31297233 - verify Camera Scan icon from bottom action bar
        C31297232 - verify Printer Scan icon from bottom action bar
        """
        self.home.select_scan_icon()
        if pytest.platform == "IOS":
            self.camera.select_allow_access_to_camera_on_popup()
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.camera.verify_preset_mode(self.camera.DOCUMENT)

    def test_02_verify_scan_screen_ui_elements(self):
        """
        C31299839 - Verifies all UI elements on scan screen
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.verify_scan_screen_ui_elements()

    def test_03_verify_source_tray_ui_elements(self):
        """
        C31299840 - Verifies different options of source tray
        C31299841 - Verify Scan area elements for printer with scanner
        """
        self.fc.go_scan_screen_from_home(self.p)
        # Verifies photo screen navigates through source button
        self.scan.select_source_button()
        self.scan.verify_source_all_options(self.printer_name)
        self.scan.select_files_photos_option()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_files_screen()
        self.files.select_close()
        # Verifies camera screen navigates through from source button
        self.scan.select_source_button()
        self.scan.select_camera_option()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        # Verifies scanner screen navigates through from source button
        self.scan.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_settings_wheel()
        self.scan.select_page_size_menu()
        self.scan.verify_page_size_options()

    def test_04_verify_input_source(self):
        """
        C31299844 - Verify message when trying to preview scan from ADF
        C35464275 - "Source" page (iOS)
        C31299427 - [Duplex Scan] Document Feeder (iOS only)
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_settings_wheel()
        self.scan.select_input_source()
        self.scan.verify_input_source_options()
        self.scan.select_input_source_option(self.scan.DOCUMENT_FEEDER)
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_preview_not_supported_message()
        self.scan.select_scan_job_button(verify_messages=False)
        self.scan.verify_document_feeder_scan()

    def test_05_verify_scan_preview_screen_ui_elements(self):
        """
        C31299814 - Verify screen when we tap on Preview icon
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.verify_scanner_screen()
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_scanning_screen()
        self.scan.verify_scanning_messages()

    def test_06_verify_scan_job_print_and_share_preview_screen_ui_elements(self):
        """
        C31299893 - Verifies ui elements of share/save screen after scanning a document
        """
        if pytest.platform == "MAC":
            pytest.skip("Verifying a defect for MAC")
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        sleep(2)
        self.common_preview.nav_detect_edges_screen()
        assert self.common_preview.verify_preview_screen()
        self.common_preview.select_print_btn()
        self.common_preview.verify_print_preview_ui_elements(self.p.get_printer_information()["bonjour name"])
        self.common_preview.select_navigate_back(delay=2)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.verify_array_of_elements(self.common_preview.SHARE_PREVIEW_UI_ELEMENTS)

    def test_07_verify_scan_edit_ui_elements(self):
        """
        C31299863 - Verifies ui elements of scan_edit screen after scanning a document
        """
        self.fc.go_to_edit_screen_with_printer_scan_image(self.p)
        self.edit.verify_edit_page_title()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)

    def test_08_verify_scan_job_preview_screen_ui_elements(self):
        """
        C31299236, C31956361 - Verifies preview screen UI elements after scanning a document and delete option
        """
        self.fc.go_scan_screen_from_home(self.p)
        no_of_pages = 2
        self.fc.add_multi_pages_scan(no_of_pages)
        assert self.common_preview.verify_preview_screen()
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        assert self.common_preview.verify_preview_page_info()[1] == no_of_pages
        assert self.common_preview.verify_delete_button()
        self.common_preview.verify_array_of_elements(self.common_preview.PREVIEW_UI_ELEMENTS)

    def test_09_verify_disabled_buttons_while_scanning(self):
        """
        C31299820, C31299826 - Verify disable button while performing Scan
        Steps:
        1.Tap on Printer Scan tile from Home Screen
        2.Tap on scan  button;
        3.Tap all the buttons when preview in progress, including those disable buttons.
         (Do not tap on Back button or cancel button. Verify other buttons present on the screen)
        Expected Result:
        - No error occur when tapping the invalid buttons.
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button(verify_messages=False)
        self.scan.verify_scanning_screen()
        self.scan.select_source_button()
        self.scan.select_scan_settings_wheel()
        self.scan.select_preview_on_scanner_screen()
        assert self.common_preview.verify_adjust_boundaries_screen(), "Scanning was interrupted"
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_scanning_messages(timeout=20)