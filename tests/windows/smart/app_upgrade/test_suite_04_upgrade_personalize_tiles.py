import pytest
from time import sleep
import logging
import random
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_04_Upgrade_Personalize_Tiles(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.search_app = 'HP Smart'

        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        if "Windows 11" not in cls.gotham_utility.verify_windows_version():
            pytest.skip("This Test only can be run on Windows 11 currently (GOTH-25938)")
        
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('start-process "ms-windows-store://home"')

        cls.version_info = {}
        cls.updated_tile_list = []
        cls.live_build_tiles = []
        cls.test_build_tiles = []
        cls.per_tiles_list = ["get_supplies_option", "scan_option", "shortcuts_option", "printables_option", "print_documents_option", "mobile_fax_option", "help_support_option", "print_photos_option", "printer_settings_option"]
        cls.toggle_btns_list_without_printables = ["get_supplies_toggle", "scan_toggle", "shortcuts_toggle", "print_documents_toggle", "mobile_fax_toggle", "help_support_toggle", "print_photos_toggle", "printer_settings_toggle"]
        cls.toggle_btns_list = ["get_supplies_toggle", "scan_toggle", "shortcuts_toggle", "printables_toggle", "print_documents_toggle", "mobile_fax_toggle", "help_support_toggle", "print_photos_toggle", "printer_settings_toggle"]

    def test_01_install_ms_store_hp_smart(self):
        """
        Install live build from Microsoft Store
        """    
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()
        self.fc.go_home()

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_modify_personalize_tiles_order(self):
        """
        Upgrade app to the latest version, verify personalize tile and main page tile order remains the same

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930934
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()

        original_tile_list = []
        for per_tile in self.per_tiles_list:
           original_tile_list.append(self.per_tiles.get_personalize_tile_name(per_tile))
        logging.info('The original personalize tiles: {}'.format(original_tile_list))
        
        toggle_btn = random.choice(self.toggle_btns_list_without_printables)
        self.per_tiles.click_tile_toggle(toggle_btn)
        self.per_tiles.verify_personalize_tile_off(toggle_btn)
        logging.info('Set {} Tile toggle turns OFF'.format(toggle_btn[:-7].capitalize()))
        self.per_tiles_list.remove(toggle_btn[:-6] + 'option')

        for per_tile in self.per_tiles_list:
           self.updated_tile_list.append(self.per_tiles.get_personalize_tile_name(per_tile))
        logging.info('The updated personalize tiles: {}'.format(self.updated_tile_list))

        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_menu_btn()
        for i in range(1, len(self.updated_tile_list)+1):
           self.live_build_tiles.append(self.home.get_main_page_tile_index(i))
        logging.info('[Live Build] The tiles on home page: {}'.format(self.live_build_tiles))

        assert self.updated_tile_list == self.live_build_tiles

    def test_03_check_tiles_latest_hp_smart(self):
        """
        Upgrade app to the latest version, verify personalize tile and main page tile order remains the same
        Turn off some tiles the live build and upgarde the app, verify correct tiles along with "Printables" tile is available
        Upgrade app from old release to new, verify "Printables" shows instead of "Play & Learn" in Main UI and Personalized tiles screen 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930934
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24810016
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997752
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27864793
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(stack='production', restart=False)
        self.driver.launch_app(launch_activity)
        assert self.welcome.verify_welcome_screen(timeout=10, raise_e=False) is False
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.verify_home_screen()
        self.home.verify_printables_tile()
        
        self.version_info["actual_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Test build Version after upgrade - {}'.format(self.version_info["actual_app_version"]))

        for i in range(1, len(self.updated_tile_list)+1):
           self.test_build_tiles.append(self.home.get_main_page_tile_index(i))
        logging.info('[Test Build] The tiles on home page: {}'.format(self.test_build_tiles))

        assert self.live_build_tiles == self.test_build_tiles

        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_printables_personalize_tile()