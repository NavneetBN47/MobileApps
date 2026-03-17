"""
Scan flow and functionality smoke test suite for iOS
"""
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_Smoke_08_Scan:
    """
    Scan flow class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.camera = cls.fc.fd["camera"]
        cls.scan = cls.fc.fd["scan"]

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

    def test_01_verify_last_selected_scan_source_preserved_scanner(self):
        """
        C31299397 - Verify last selected printer scan source is preserved
        """
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.select_source_button()
        self.camera.select_source_option(
            self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.select_close()
        self.home.close_smart_task_awareness_popup()
        self.home.select_scan_icon()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_close()
