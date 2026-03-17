import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "SMART"


class Test_Suite_02_Mobile_Fax_Printer_Scanner(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.smart_context = cls.fc.smart_context

    @pytest.mark.parametrize("number", [1, 2])
    def test_01_send_fax_from_scanner(self, number):
        """
        Description: C31379770, C31379772, C31379771
        1. Launch app
        2. Perform single page scan from the printer or 2 pages scan from the printer
        3. Click on Fax button from Preview screen

        Expected Results:
        3. Verify that "Add Files" section should have the file captured from printer scanner
        """
        self.fc.flow_home_scan_single_page(printer_obj=self.p)
        self.scan.select_adjust_next_btn()
        if number == 2:
            self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
            self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
            self.scan.start_capture()
            self.scan.verify_successful_scan_job()
            self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.compose_fax.verify_compose_fax_screen()
        file_name, pages = self.compose_fax.get_added_file_information()
        assert bool(file_name), "file name should be displayed"
        assert pages == f"{number} page{'s' if number != 1 else ''}", f"Pages count should be {number} page{'s' if number != 1 else ''}"