import pytest
import time

pytest.app_info = "GOTHAM"
class Test_Suite_02_Personalize_Tiles_Drag_Drop_Toggle(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session  

        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        cls.tile_dic = {}

    def test_01_compare_tiles_before_change(self):
        """
        Before drag and drop tiles:
        Go to Main UI, get all the tiles.
        Go to the "Personalize Tiles" page, get all the tiles. 
        """
        main_tile_list = []
        per_tile_list = []
        self.fc.go_home()
        main_tile_list = self.__get_all_the_tiles(home_page=True)
        self.home.select_app_settings_btn()
        self.home.verify_personalize_tiles_listview()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()
        per_tile_list = self.__get_all_the_tiles(home_page=False)
        assert main_tile_list == per_tile_list
        self.tile_dic['before_drag'] = main_tile_list        

    def test_02_drag_and_drop_tiles(self):
        """
        Click "Personalize Tiles" option.
        Drag & drop the tile on the "Personalize Tiles" page.

        Verify Main UI shows the same tile order as the "Personalize Tiles" page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16968271   
        """

        self.per_tiles.drag_and_drop_tile_option('get_supplies_option', 'scan_option')
        self.per_tiles.drag_and_drop_tile_option('print_documents_option', 'print_photos_option')
        self.per_tiles.drag_and_drop_tile_option('printables_option', 'printer_settings_option')

    def test_03_compare_tiles_after_change(self):
        """
        After drag and drop tiles:
        Go to Main UI, get all the tiles.
        Go to the "Personalize Tiles" page, get all the tiles. 
        """
        main_tile_list = []
        per_tile_list = []
        per_tile_list = self.__get_all_the_tiles(home_page=False)
        self.home.select_navbar_back_btn()
        main_tile_list = self.__get_all_the_tiles(home_page=True)
        assert main_tile_list == per_tile_list
        self.tile_dic['after_drag'] = main_tile_list
        assert self.tile_dic['before_drag'] != self.tile_dic['after_drag']
    
    def test_04_check_sortedtiles_created(self):
        """
        Visit the "Personalize Tile" screen
        Change tile order from the Personalize by dragging up and down.
        Go to home page
        Go to local state folder

        Verify sortedtiles.xml file is created.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16932049
        """   
        self.per_tiles.check_sorted_tiles_path()

    def __get_all_the_tiles(self, home_page=True):
        """
        Get all the tiles
        """
        tiles_list = []
        for i in range(1, 10):
            if home_page:
                each_tile = self.home.get_main_page_tile_index(i)
            else:
                each_tile = self.per_tiles.get_personalize_tile_index(i)
            if each_tile is not False:
                tiles_list.append(each_tile)
        return tiles_list
