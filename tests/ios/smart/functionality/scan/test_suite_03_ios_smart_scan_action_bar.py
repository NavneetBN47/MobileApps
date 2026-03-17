import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_03_Ios_Smart_Scan_Action_Bar(object):
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.camera = cls.fc.fd["camera"]
        cls.scan = cls.fc.fd["scan"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])

    def test_01_verify_scan_pop_up_printer_scan_tile(self):
        """
        C31299433 - Coach Mark (X) button behavior
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_SCAN)
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_adjust_scan_coach_mark(raise_e=False):
            self.camera.select_second_close_btn()
        assert self.scan.verify_scanner_or_camera_popup_displayed(popup=True) is False
        self.scan.select_close()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        assert self.scan.verify_scanner_or_camera_popup_displayed(popup=True) is False
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_close()

    def test_02_verify_scan_pop_up_camera_tile(self):
        """
        C31298928 - Verify scan pop up after fresh app install Camera tile
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_adjust_scan_coach_mark(raise_e=False):
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.scan.select_close()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        assert self.scan.verify_scanner_or_camera_popup_displayed(popup=True) is False
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.scan.select_close()

    def test_03_verify_last_selected_scan_source_preserved_scanner(self):
        """
        C31299397 - Verify last selected printer scan source is preserved
        """
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.select_close()
        self.home.close_smart_task_awareness_popup()
        self.home.select_scan_icon()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_close()
    
    def test_04_verify_last_selected_scan_source_preserved_camera(self):
        """
        C31299180 - Verify last selected camera scan source is preserved
        """
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.scan.select_close()
        self.home.close_smart_task_awareness_popup()
        self.home.select_scan_icon()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.scan.select_close()