"""
Help and Support flow and functionality smoke test suite for iOS
"""
import pytest
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.libs.flows.mac.smart.utility import smart_utilities

pytest.app_info = "SMART"


class Test_Suite_Smoke_06_Help_And_Support:
    """
    Help and Support flow class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.help_support = cls.fc.fd["help_support"]
        if pytest.platform == "IOS":
            cls.ios_system = cls.fc.fd["ios_system"]
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        """
        Fixture setup for autouse of go_home function
        Verify navigation to home page after:
        1. App installation on the mobile device
        2. Clicking on Sign In on the ows screen and navigating to home page
        """
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_help_and_support_tile(self):
        """
        Verify the help and support tile is present on home screen
        """
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_HELP_AND_SUPPORT)

    def test_02_help_page_print_document(self):
        """
        IOS & MAC:
        Requirements:
            C37971702 - Verify new online help content displays the specified help page
        Steps:
            1. Add the printer with scanner on the home screen
            2. Click on 'Print documents' or 'Files & Photos' on the app.
            3. Click on HP Smart Files
            4. Click on 'Learn More'
        Expected Results:
            1. Verify Support page displays on screen
        """
        if pytest.platform == "IOS":
            self.ios_system.handle_allow_tracking_popup(raise_e=False)
            self.home.verify_home()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        if pytest.platform == "MAC":
            smart_utilities.delete_all_hp_smart_files(
                self.driver.session_data["ssh"])
        else:
            self.fc.go_hp_smart_files_and_delete_all_files()
        self.fc.go_hp_smart_files_screen_from_home(select_tile=True)
        self.files.select_learn_more_link_on_empty_files_screen()
        try:
            self.help_support.verify_help_center_screen()
        except TimeoutException:
            self.help_support.native_verify_help_center_screen()
