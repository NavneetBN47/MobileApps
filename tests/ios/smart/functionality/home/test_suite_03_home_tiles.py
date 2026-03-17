import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "SMART"

class Test_Suite_03_Home_Tiles_Without_Onboarding(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.personalize = cls.fc.fd["personalize"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.printables = cls.fc.fd["printables"]
        cls.photos = cls.fc.fd["photos"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]

    def test_01_verify_locked_tile(self):
        """
        C27654941 select Explore HP Smart during OWS Value prop and select a locked tile
        Verify value prop screen
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, timeout=60)

    def test_02_verify_locked_tile_without_printer(self):
        """
        C27654937 select Explore HP Smart during OWS Value prop and select a Printer Scan or Copy tile
        Verify "Feature Unavailable" pop-up shows up with "OK" button
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SCAN)
        self.home.verify_feature_unavailable_popup("no_printer_msg")

    def test_03_login_on_locked_tiles(self):
        """
        C27654935
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SMART_TASK)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, timeout=60)
        self.ows_value_prop.select_value_prop_buttons(1)
        self.driver.wait_for_context(self.fc.hpid_url, timeout=45)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.username, self.password)
        sleep(20)
        self.shortcuts.verify_shortcuts_screen()

    def test_04_printable_tile(self):
        '''
        special offer tile renamed to printables
        C30717211: Special Offers tile can be enabled from Personalize Tiles
        C30717212: Special Offers tile redirection
        '''
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PLAY_LEARN)
        sleep(20)
        self.printables.verify_printables_title()

    def test_06_verify_print_photos_tile(self):
        """
         Description: C31379926
            1. Load to Home screen
            2. Click on Print Photos tile
            3. Click on Cancel button
            4. Click on Print Photos tile
            5. Click on Continue button
            6. Allow permission to access Photos

         Expected Result:
            3. Verify Home screen
            6. Verify Photo select screen
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.verify_limited_access_screen()
        self.home.select_cancel()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.select_continue()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        assert self.photos.verify_0_selected_title(), "0 Selected Title not shown"

    def test_07_verify_print_documents_tile(self):
        """
         Description:
            1. Load to Home screen
            2. Click on Print Document tile
            3. Click on Cancel button
            4. Click on Continue button

        Expected Result:
            3. Verify Home screen
            4. Verify View and Print screen
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.home.verify_limited_access_screen()
        self.home.select_cancel()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.home.select_continue()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.files.verify_files_screen()
