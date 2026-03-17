import pytest
import logging
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA, BUNDLE_ID

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_02_Ios_Smart_Scan_Func(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.printer_name = cls.printer_info["bonjour name"]
        cls.stack = request.config.getoption("--stack")
        cls.edit = cls.fc.fd["edit"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.camera = cls.fc.fd["camera"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.go_home(stack=cls.stack)

    def test_01_validate_message_during_scan(self):
        """
        C31299843 - Validate scanning and scan finished messages
        C29728521 - Country selected Non-China - print features access - user sign-in
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button(verify_messages=False)
        self.scan.verify_scanning_messages()
        sleep(2)
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.dismiss_feedback_popup()
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)

    def test_02_background_app_during_printer_scan(self):
        """
        C31299866 - Verify Scan is available after backgrounding the app
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button(verify_messages=False)
        sleep(5)
        self.driver.launch_app(BUNDLE_ID.SETTINGS)
        sleep(2)
        self.driver.launch_app(BUNDLE_ID.SMART)
        assert self.common_preview.verify_adjust_boundaries_screen(), "Scanning was interrupted"

    def test_03_validate_message_during_previewing_scan(self):
        """
        C31299846 - Verify message when previewing scan job
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_scanning_messages()
        self.scan.verify_preview_button_on_scan_screen()

    @pytest.mark.parametrize("size", ["a4", "4x6", "letter", "5x7", "3_5x5"])
    def test_04_scan_with_settings(self, size):
        """
        C31299812 - Basic One page scan flow
        C31299815 - Verify preview (scanned document) selection area changed as per the value of document size
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_settings_wheel()
        self.scan.select_page_size_menu()
        self.scan.verify_page_size_options()
        self.scan.select_scan_size(size)
        self.scan.select_navigate_back()
        self.scan.select_input_source()
        self.scan.select_input_source_option(self.scan.SCANNER_GLASS)
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_scan_job_button(verify_messages=False)

    def test_05_lock_device_while_scanning(self):
        """
        C31299830 - Verify scan is not interrupted when device is locked
        Steps:
        1/ Load Scan screen via tile with selecting printer at Home screen
        2/ Click on Scan button
        3/ Click on Mobile Lock button while scanning
        4/ UnLock the Hardware
        Verify for following step:
        4/ The Application should be launch without error.
        - Scan Job should be completed
        - User should navigate to Landing page
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button(verify_messages=False)
        self.driver.lock_device()
        self.driver.unlock_device()
        assert self.common_preview.verify_adjust_boundaries_screen(timeout=15), "Scanning was interrupted"

    def test_06_duplex_scan(self):
        """
        C31299428 - [Duplex Scan] Document Feeder 2-Sided
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_settings_wheel()
        self.scan.select_input_source()
        is_option_displayed = self.scan.verify_an_element_and_click(self.scan.DOCUMENT_FEEDER_2_SIDED, raise_e=False)
        if not is_option_displayed:
            pytest.skip(f"Duplex scan is not supported on {self.printer_name}")
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_scan_job_button()
    
    def test_07_verify_preview_screen_add_page_delete_page_and_back_buttons(self):
        """
        C37667302 - Verify back button functionality from preview screen for scan source - scanner
        C31299236 - Add multi pages to preview through source scanner , verify X icon displays
            and clicking X deletes added images until last page
        C31299853 - Verify addition of scanned pages - source scanner
        """
        pages_scanned = 3
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(pages_scanned)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        assert self.common_preview.verify_preview_page_info()[1] == int(pages_scanned)
        assert self.common_preview.verify_delete_page_x_icon()
        self.common_preview.select_delete_pages_in_current_job()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_popup()
        self.common_preview.select_cancel()
        self.common_preview.go_home_from_preview_screen()

    def test_08_verify_printing_scanned_image(self):
        """
        C31299856 - Scan any file using scanner source and send the job to print and
        verify printed successfully
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.fc.select_print_button_and_verify_print_job(self.p)
        # Test Case clean up
        self.common_preview.select_done()

    def test_09_verify_edit_for_scan_with_source_scanner_new(self):
        """
        C31299857 - Verify edit for multiple scanned images- new
        """
        pages_scanned = 3
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(pages_scanned)
        self.fc.go_to_edit_screen_with_selected_photo()
        adjust_option_failed = []
        self.edit.apply_edits(self.edit.ADJUST, "Brightness")
        if self.edit.verify_undo_button_enabled() != 'true':
            adjust_option_failed.append("Brightness")
        self.edit.select_edit_done()
        sleep(1)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        # Added extra timeout to verify 3 prints complete successfully
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=180)
        # Test Case clean up
        self.common_preview.select_done()
    
    def test_10_verify_and_preview_custom_scan_job(self):
        """
        C31299848 - Verify custom scan when performing scan job
        C31299847 - Verify custom scan and preview scan job
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_settings_wheel()
        self.scan.select_page_size_menu()
        self.scan.select_scan_size("a4")
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_scanning_messages(timeout=20)
        uncustomized_img_preview = self.scan.screenshot_img_inside_selection_border()
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        uncustomized_img = self.common_preview.verify_preview_img()
        self.common_preview.select_navigate_back()
        self.common_preview.select_exit_popup_btn("scan")
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.customize_scan_using_elements("top_knob")
        assert saf_misc.img_comp(uncustomized_img_preview, self.scan.screenshot_img_inside_selection_border()) > 0.5, "Customized scan was unsuccessful"
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        assert saf_misc.img_comp(uncustomized_img, self.common_preview.verify_preview_img()) > 0.5, "Customized scan was unsuccessful"

    def test_11_verify_reorder_screen_functionality(self):
        """
        C31299382 - Do not discard changes on Reorder screen
        C31299381 - Discard changes on Reorder screen
        C31299404 - Verify new Location and Style for "Reorder" button on Landing Page
        """
        pages_scanned = 3
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(pages_scanned)
        self.common_preview.verify_an_element_and_click(self.common_preview.REORDER_BTN)
        self.common_preview.reorder_image(1, 2)
        self.common_preview.select_cancel()
        self.common_preview.verify_discard_changes_popup()
        self.common_preview.select_no()
        self.common_preview.verify_title(self.common_preview.REORDER_TITLE)
        self.common_preview.select_cancel()
        self.common_preview.select_yes()
        self.common_preview.verify_preview_screen()
    
    def test_12_verify_page_size_is_preserved(self):
        """
        C31299819 - Verify "Add more pages" has previous value for document size
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_settings_wheel()
        self.scan.select_page_size_menu()
        self.scan.select_scan_size("a4")
        self.scan.select_navigate_back()
        self.scan.select_input_source()
        self.scan.select_input_source_option(self.scan.SCANNER_GLASS)
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        init_image_a4 = self.common_preview.verify_preview_img()
        self.common_preview.select_add_page()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        assert "a4" in self.scan.get_area_size().lower(), "Page size is not preserved"
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_scanning_messages(timeout=20, raise_e=True)
        self.scan.select_scan_settings_wheel()
        self.scan.select_page_size_menu()
        self.scan.select_scan_size("4x6")
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        second_image_4x6 = self.common_preview.verify_preview_img(page_number=2)
        assert saf_misc.img_comp(init_image_a4, second_image_4x6) > 1, "Specified scan size is not applied"
        self.common_preview.select_add_page()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        assert "4x6" in self.scan.get_area_size().lower(), "Page size is not preserved"
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        assert saf_misc.img_comp(second_image_4x6, self.common_preview.verify_preview_img(page_number=3)) < 2, "Specified scan size is not applied"