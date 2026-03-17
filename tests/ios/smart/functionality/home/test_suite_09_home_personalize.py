import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_09_Home_Personalize(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        cls.personalize = cls.fc.fd["personalize"]
        cls.home = cls.fc.fd["home"]
        if pytest.platform == "MAC":
            cls.personalize.TILES = [tile for tile in cls.personalize.TILES if tile not in ["camera_scan", "copy"]]
            cls.personalize.SWITCHES = [switch for switch in cls.personalize.SWITCHES if switch not in ["camera_scan_switch", "copy_switch"]]

    @pytest.fixture(scope="function", autouse=True)
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)

    def test_01_personalize_ui(self):
        """
        TESTRAIL: IOS & MAC
        C31297057, C31298227 - Verify Personalize Tiles screen
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        self.personalize.verify_personalize_tiles_and_switches()
        self.personalize.select_done()
        self.home.verify_home()

    def test_02_compare_enabled_tiles(self):
        """
        TESTRAIL: IOS & MAC
        C31297058
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        self.personalize.toggle_all_tiles()
        tiles_on_personalize_screen = self.personalize.get_tile_names()
        if pytest.platform == "MAC":
            self.personalize.select_done()
        tiles_on_home_screen = self.home.get_all_tiles_titles()
        assert (len(set(tiles_on_personalize_screen)) == len(set(tiles_on_home_screen))), "The number of tiles toggled on and tiles on the home screen is different"

    def test_03_turn_off_all_tiles_except_one(self):
        """
        TESTRAIL: IOS & MAC
        C31297059
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        self.personalize.toggle_all_tiles(on=False)
        self.personalize.toggle_switch_by_index(index=random.randint(0, len(self.personalize.SWITCHES) - 1))
        self.personalize.select_done()
        self.home.verify_home()
        tiles_on_home_screen = self.home.get_all_tiles_titles()
        assert len(tiles_on_home_screen) == 1

    def test_04_turn_on_and_verify_default_disabled_tiles(self):
        """
        TESTRAIL: IOS & MAC
        C31297060
        C31298228
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        enabled_tiles = list(set(self.personalize.get_tile_names()) - set(self.personalize.get_enabled_tiles_names()))
        self.personalize.toggle_tiles_to_opposite_state()
        self.personalize.select_done()
        self.home.verify_home()
        tiles_on_home_screen = self.home.get_all_tiles_titles()
        assert tiles_on_home_screen == enabled_tiles