import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_04_SMB_Personalize_Main_Menu(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup  

        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.stack = request.config.getoption("--stack")
        if cls.stack == "stage":
            login_info = ma_misc.get_smb_account_info("stage_journey_testing")
        else:
            login_info = ma_misc.get_smb_account_info(cls.stack)
        cls.username, cls.password = login_info["email"], login_info["password"]

        cls.main_tiles_list = ["get_supplies_tile", "printables_tile"]
        cls.per_tiles_list = ["get_supplies_option", "printables_option"]
        cls.toggle_btns_list = ["get_supplies_toggle", "printables_toggle"]

    def test_01_check_some_tile_with_personal_org(self):
        """
        User must be signed in with SMB account and personal org
        launch the app to the main UI
        complete the sign in with personal org from any available sign in entry
        Go to personalized option
        Observe the Supplies tile on the Main UI
        Observe the Printable tile on the Main UI
        Observe the Supplies tile option
        Observe the Printable tile option
        Verify Printable tile/Supplies tile is available on main UI and user can use it without any issue.
        Verify Supplies tile is available and user can turn on and off from there
        Verify Printable tile is available and user can turn on and off from there
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010201
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010202
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010226
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010227
        """
        self.fc.go_home()
        self.fc.sign_in(self.username, self.password)
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item(4)
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen()
        for main_tile in self.main_tiles_list:
            self.home.verify_main_page_each_tile(main_tile)
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen()
        for toggle_btn in self.toggle_btns_list:   
            self.per_tiles.verify_personalize_tile_on(toggle_btn)

    def test_02_check_some_tile_with_business_org(self):
        """
        User must be signed in with SMB account and Business org
        launch the app to the main UI
        complete the sign in with Business org from any available sign in entry
        Go to personalized option
        Observe the Supplies tile on the Main UI
        Observe the Printable tile on the Main UI
        Observe the Supplies tile option
        Observe the Printable tile option
        Verify Supplies tile/Printable tile is not available on Main UI
        Verify Supplies tile option is not available under personalized menu
        Verify Printable tile option is not available under personalized menu
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010203
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010204
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010228
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32010229
        """
        self.home.select_navbar_back_btn()
        self.home.select_my_hp_account_btn()
        self.home.select_an_organization_list_item(2)
        self.home.verify_home_screen()
        for main_tile in self.main_tiles_list:
            self.home.verify_main_page_each_tile(main_tile, raise_e=False) is False
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        for per_tile in self.per_tiles_list:
            self.per_tiles.verify_personalize_tile(per_tile, raise_e=False) is False
            