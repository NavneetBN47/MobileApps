"""
Printables tile flow and functionality smoke test suite for iOS
"""
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"


class Test_Suite_Smoke_07_Printables:
    """
    Printables tile flow class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printables = cls.fc.fd["printables"]
        cls.stack = request.config.getoption("--stack")

    def test_01_printable_tile(self):
        '''
        special offer tile renamed to printables
        C30717211: Special Offers tile can be enabled from Personalize Tiles
        C30717212: Special Offers tile redirection
        '''
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PLAY_LEARN)
        self.printables.verify_printables_title()
