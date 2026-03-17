import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc import saf_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_01_Personalize_On_Off_Toggle(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        time.sleep(3)

        cls.main_tiles_list = ["get_supplies_tile", "scan_tile", "shortcuts_tile", "printables_tile", "print_documents_tile", "mobile_fax_tile", "help_and_support_tile", "print_photos_tile", "printer_settings_tile"]
        cls.per_tiles_list = ["get_supplies_option", "scan_option", "shortcuts_option", "printables_option", "print_documents_option", "mobile_fax_option", "help_support_option", "print_photos_option", "printer_settings_option"]
        cls.toggle_btns_list = ["get_supplies_toggle", "scan_toggle", "shortcuts_toggle", "printables_toggle", "print_documents_toggle", "mobile_fax_toggle", "help_support_toggle", "print_photos_toggle", "printer_settings_toggle"]
       
    def test_01_personalize_tiles_no_printer(self):
        """
        Do not add printer
        Open Personalized tile screen
        Check the toggle of Mobile Fax tile

        Verify Mobile Fax tile toggle is ON
        Verify the "Printables" tile is listed on the personalize Tiles.
        Verify "Play & Learn" tile is changed to "Printables" on Personalized tile screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/27835397
        https://hp-testrail.external.hp.com/index.php?/cases/view/24809586
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864792
        """
        self.fc.go_home()
        self.home.verify_play_learn_tile_not_exist()
        self.home.verify_main_page_tiles()
        self.home.select_app_settings_btn()
        el = self.home.verify_app_settings_items_by_index(1)
        assert el.text == "Personalize Tiles"
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()
        for toggle_btn in self.toggle_btns_list:   
            self.per_tiles.verify_personalize_tile_on(toggle_btn)

    def test_02_add_a_printer(self):
        self.home.select_navbar_back_btn()
        self.fc.select_a_printer(self.p)
        
    def test_03_personalize_tiles_with_printer(self):
        """
        Click Settings on the left bar of main UI 
        Click "Personalize Tiles" option.

        Verify "Personalize Tiles" page shows.
        Verify all tiles shows up on main UI are toggled On on the screen.
        Verify the "Mobile Fax" option is listed under the personalize tile.
        Verify Mobile Fax tile toggle is ON

        https://hp-testrail.external.hp.com/index.php?/cases/view/16965513
        https://hp-testrail.external.hp.com/index.php?/cases/view/16932051
        https://hp-testrail.external.hp.com/index.php?/cases/view/17361145
        https://hp-testrail.external.hp.com/index.php?/cases/view/27835408
        https://hp-testrail.external.hp.com/index.php?/cases/view/16965515
        """
        self.home.verify_main_page_tiles()
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        for toggle_btn in self.toggle_btns_list:   
            self.per_tiles.verify_personalize_tile_on(toggle_btn)
        
    def test_04_compare_main_personalize_tiles(self):
        """
        Click "Personalize Tiles" option.
        Click the Back arrow on the "Personalize Tiles" page
        Tips: The tiles on "Personalize Tiles" screen should be consistent with main UI.

        Verify user navigates to main UI.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16965585
        https://hp-testrail.external.hp.com/index.php?/cases/view/16968270
        """
        main_tile_name_list = per_tiles_name_list =[]
        self.home.select_navbar_back_btn()
        for main_tile in self.main_tiles_list:
           main_tile_name_list.append(self.home.get_main_page_tile_name(main_tile))
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        for per_tile in self.per_tiles_list:
           per_tiles_name_list.append(self.per_tiles.get_personalize_tile_name(per_tile))
        assert main_tile_name_list == per_tiles_name_list

    def test_05_toggle_off(self):
        """
        Click toggle On/Off on "Personalize Tiles" screen.
        Go to main UI to check the tiles.
        Go to Personalize tile page to disable Mobile Fax tile
        Go home

        Verify once you enable the tiles in "Personalize Tiles" screen, main UI shows the tile as well.
        Verify once you disable the tile in in "Personalize Tiles" screen, main UI does not show the tiles either.
        Verify Mobile Fax tile is not seen on home screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16965585
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840977
        """
        for toggle_btn in self.toggle_btns_list:   
            self.per_tiles.click_tile_toggle(toggle_btn) 
            self.per_tiles.verify_personalize_tile_off(toggle_btn) 
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_menu_btn()
        cur_img = saf_misc.load_image_from_base64(self.home.capture_main_tiles_img())
        cur_img = saf_misc.img_crop(cur_img, 0.0, 0.65, 0.0, 0.0)
        toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + 'personalize_tiles/' + 'main_tiles.png'))
        assert saf_misc.img_comp(cur_img, toggle_img) < 0.32

    def test_06_check_sorted_tiles_file(self):
        """
        Enable and disable a tile
        Go to home page
        Go to local state folder [Win]
        Repeat step until each tile is checked.

        Verify what ever tile you disable, you will see this line after the tile name "IsFeatureChangedByUser="true"/> " in sortedtiles.xml
        Verify Main UI also show the updated tile order
        Verify updated tile order shows on the sortedtiles.xml under tile sections

        https://hp-testrail.external.hp.com/index.php?/cases/view/16932052
        https://hp-testrail.external.hp.com/index.php?/cases/view/16932053
        """ 
        sorted_tiles_list = ['Dsp', 'ScanCapture', 'SmartTasks', 'FunTile', 'PrintDoc', 'SoftFax', 'Help', 'PrintPhotos', 'PrinterInfo']
        for sorted_tile in sorted_tiles_list:
            check_data = 'SortId="{}"([A-Za-z\s="]*)IsFeatureChangedByUser="true"'.format(sorted_tile)
            self.per_tiles.check_sorted_tiles_data(check_data)
        
    def test_07_toggle_on(self):
        """
        Click toggle On/Off on "Personalize Tiles" screen.
        Go to main UI to check the tiles.

        Verify once you enable the tiles in "Personalize Tiles" screen, main UI shows the tile as well.
        Verify once you disable the tile in in "Personalize Tiles" screen, main UI does not show the tiles either.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16965585
        """ 
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        for toggle_btn in self.toggle_btns_list[0:4]:   
            self.per_tiles.click_tile_toggle(toggle_btn) 
            self.per_tiles.verify_personalize_tile_on(toggle_btn)
        for toggle_btn in self.toggle_btns_list[4:]:
            self.per_tiles.verify_personalize_tile_off(toggle_btn)
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_menu_btn()
        for main_tile in self.main_tiles_list[0:4]:
            self.home.verify_main_page_each_tile(main_tile)
        for main_tile in self.main_tiles_list[4:]:
            assert self.home.verify_main_page_each_tile(main_tile, raise_e=False) is False

    def test_08_restart_app(self):
        """
        Go to "Personalize Tiles" screen
        Turn on and off a few different tiles.
        Re-order a few tiles.
        Go to home page
        Check the order of the tiles
        Close the app
        Relaunch the app

        Verify the correct order remains the same.
        Verify the correct tiles are displayed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16932054
        """   
        self.driver.restart_app()
        for main_tile in self.main_tiles_list[0:4]:
            self.home.verify_main_page_each_tile(main_tile)
        for main_tile in self.main_tiles_list[4:]:
            assert self.home.verify_main_page_each_tile(main_tile, raise_e=False) is False

