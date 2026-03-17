import pytest
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.libs.flows.mac.smart.utility import smart_utilities

pytest.app_info = "SMART"

class Test_Suite_08_Help_And_Support:

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

    def test_01_verify_help_and_support_tile(self):
        """
        Description: C50698969
            Verify Help & Support tile behavior.
                Install and launch app.
                Go through the consents, sign in and navigate to Home screen.
                Tap on Help & Support tile
            Expected Result:
                Verify Support page opens.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.ios_system.handle_allow_tracking_popup(raise_e=False)
        self.home.verify_home()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_HELP_AND_SUPPORT)
        self.help_support.verify_help_center_screen()