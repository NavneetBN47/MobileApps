import pytest
import logging
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_04_Personalize_Tiles_Hover(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

    def test_01_go_to_personalize_tiles_screen(self):
        """
        Go to Personalized tile screen
        """
        self.fc.go_home()
        self.home.verify_main_page_tiles()
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()
     
    def test_02_personalize_tiles_with_printer(self):
        """
        Hover on any tile.

        Verify the string part of the line changes to light dark grey when hover and pressed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16977311
        """
        tile_list = ["supplies", "scan", "shortcuts", "printables", "documents", "fax", "help", "photos", "settings"]
        for i in range(1, 10):
            self.per_tiles.hover_tile(i)
            value = self.fc.check_element_background('tiles_list', 'personalize_tiles', 'personalize_tiles_org.png', value=0.15)
            logging.info("hover vs org: {}".format(value))
            assert 0.03 > value > 0.025
            value = self.fc.check_element_background('tiles_list', 'personalize_tiles', tile_list[i-1] + '_h.png', value=0.15)
            logging.info("hover vs hover: {}".format(value))
            assert value < 0.001
  