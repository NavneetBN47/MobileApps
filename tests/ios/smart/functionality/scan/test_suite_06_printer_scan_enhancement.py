import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_06_Printer_Scan_Enhancement(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.scan = cls.fc.fd["scan"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.home = cls.fc.fd["home"]
        cls.camera = cls.fc.fd["camera"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.fc.go_home(reset=True,stack=cls.stack)
    
    def test_01_verify_all_scan_setting_options(self):
        """
        C31299411 - Scan Settings page
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_settings_wheel()
        self.scan.verify_array_of_elements(self.scan.SCAN_SETTINGS)
        self.scan.verify_an_element_and_click(self.scan.QUALITY)
        self.scan.verify_an_element_and_click(i_const.SCAN_QUALITY.BEST, click=False)
        self.scan.verify_an_element_and_click(i_const.SCAN_QUALITY.DRAFT, click=False)
        self.scan.verify_an_element_and_click(i_const.SCAN_QUALITY.NORMAL, click=False)
        self.scan.select_navigate_back()
        self.scan.verify_an_element_and_click(self.scan.COLOR)
        self.scan.verify_an_element_and_click(i_const.SCAN_COLOR.COLOR, click=False)
        self.scan.verify_an_element_and_click(i_const.SCAN_COLOR.GRAYSCALE, click=False)
    
    def test_02_verify_transform(self):
        """
        C31299201 - "Transform" button on print preview (iOS only)
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.fc.navigate_to_transform_screen()
    
    def test_03_verify_photo_n_document_scan(self):
        """
        C31299400 - Photo and Document scan
        """
        self.fc.go_scan_screen_from_home(self.p)
        for _ in range (4):
            self.scan.select_scan_job_button()
            self.common_preview.verify_adjust_boundaries_screen()
            self.scan.select_navigate_back()
    
    def test_04_verify_replace_option(self):
        """
        C31299403 - Verify new Location and Style for "Add" button on Landing Page
        C35948894 - Verify Replace option from Landing page
        """
        self.fc.go_scan_screen_from_home(self.p)
        no_of_pages = 2
        self.fc.add_multi_pages_scan(no_of_pages)
        self.common_preview.verify_an_element_and_click(self.common_preview.DELETE_PAGE_ICON)
        self.common_preview.verify_array_of_elements(self.common_preview.PREVIEW_EDIT_OPTIONS)
        self.common_preview.select_replace_btn()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_scanner_screen()
    
    def test_05_verify_scan_coachmarks(self):
        """
        C31299429 - Coach Mark on printer scan
        C31299430 - Coach Mark 2-nd page
        C31299431 - Coach Mark 3-rd page
        C31299432 - Coach Mark 4-th page
        C31299437 - Verify "<" back button on coach mark
        C31299435 - Coach Mark shows up only 1 time
        C31299434 - Coach Mark (tapping anywhere on screen) behavior
        """
        self.fc.go_home(reset=True, stack=self.stack)
        p = self.p.get_printer_information()
        # Screen scrolled down on launch causing element not found.
        self.driver.scroll(i_const.HOME_TILES.TILE_INSTANT_INK, direction="up", scroll_object="tile_collection_view")
        if self.home.verify_printer_added() is False:
            self.fc.add_printer_by_ip(printer_ip=p["ip address"])
            sleep(2)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        assert self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_COACH_MARK, raise_e=False) is not False
        self.driver.click_by_coordinates(area="mm")
        self.fc.go_to_home_screen()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK)
        self.scan.select_next_on_coachmark()
        self.scan.verify_coachmark_on_scan_page(self.scan.START_SCAN_COACHMARK)
        self.scan.select_navigate_back()
        self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK)
        for coachmark in self.scan.SCAN_COACH_MARKS:
            self.scan.verify_coachmark_on_scan_page(coachmark)
            self.scan.select_next_on_coachmark()
        self.scan.verify_scanner_screen()
        self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        sleep(2)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        assert not self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK, raise_e=False)
        assert not self.scan.verify_coachmark_on_scan_page(self.scan.START_SCAN_COACHMARK, raise_e=False)
        assert not self.scan.verify_coachmark_on_scan_page(self.scan.SCAN_SOURCE_COACHMARK, raise_e=False)

    def test_06_verify_gear_btn_functionality(self):
        """
        C31299406 - Verify 'Gear' button functionality from top bar
        C31299417 - Printer Scan UI (Base user)
        C31299408 - Auto-Orientation functionality
        C31299407 - Auto Enhancement functionality
        C31299401 - Batch mode
        C31299439 - Batch Mode should not detect edges
        """
        self.fc.go_scan_screen_from_home(self.p)
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_preset_sliders()
        self.scan.select_gear_setting_btn()
        self.scan.verify_an_element_and_click(self.scan.AUTO_ENHANCEMENT, click=False)
        self.scan.verify_an_element_and_click(self.scan.AUTO_ORIENTATION, click=False)
        self.scan.verify_is_toggled(self.scan.AUTO_ENHANCEMENT_SWITCH)
        self.scan.verify_is_toggled(self.scan.AUTO_ORIENTATION_SWITCH, is_toggled=False)
        self.scan.select_done()
        self.scan.select_preset_mode(self.camera.BATCH)
        self.scan.select_scan_job_button()
        self.scan.verify_scanner_screen()
        self.scan.verify_batch_scan_message()
        self.scan.select_scan_job_button()
        self.scan.verify_scanner_screen()
        self.scan.verify_batch_scan_message()
        assert self.camera.return_number_of_images() == 2
        self.camera.select_auto_image_collection_view()
        self.common_preview.verify_preview_screen()