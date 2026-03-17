import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_07_Printer_Scan_Hpplus(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup,load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(reset=True, stack=cls.stack, username=cls.username, password=cls.password, remove_default_printer=False)
    
    def test_01_verify_gear_btn_functionality_hpplus(self):
        """
        C31299406 - Verify 'Gear' button functionality from top bar
        C31299396 - Printer Scan UI (HP+ user)
        """
        self.fc.go_scan_screen_from_home(self.p)
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_preset_sliders()
        self.scan.select_gear_setting_btn()
        self.scan.verify_an_element_and_click(self.scan.AUTO_ENHANCEMENT, click=False, raise_e=True)
        self.scan.verify_an_element_and_click(self.scan.AUTO_ORIENTATION, click=False, raise_e=True)
        self.scan.verify_an_element_and_click(self.scan.AUTO_HEAL_SWITCH, click=False, raise_e=True)
        self.scan.verify_an_element_and_click(self.scan.FLATTEN_PAGES_SWITCH, click=False, raise_e=True)
    
    def test_02_verify_id_card_option(self):
        """
        (No testcases for printer scan, only found for camera scan)
        Verify "ID Card" option on printer scan carousal
        "X" button behavior on ID Card screen
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_preset_mode(self.scan.ID_CARD)
        self.scan.verify_an_element_and_click("id_card_mode_text", click=False, raise_e=True)
        self.scan.verify_an_element_and_click("close_btn", click=False, raise_e=True)
    
    def test_03_verify_back_btn_capture_screen(self):
        """
        (No testcases for printer scan, only found for camera scan)
        ← (back) Button behavior on New ID Card Back Capture
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_preset_mode(self.scan.ID_CARD)
        self.scan.verify_an_element_and_click("id_card_mode_text", click=True, raise_e=True)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_job_button()
        # printer scan requires longer time
        time.sleep(10)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_job_button()
        # printer scan requires longer time
        time.sleep(10)
        self.common_preview.verify_id_card_front_screen(timeout=20)
        self.common_preview.select_navigate_back()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_scanner_screen()