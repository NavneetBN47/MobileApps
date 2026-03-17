import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "SMART"

class Test_Suite_01_User_Onboarding(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.mark.parametrize("tile_name", [HOME_TILES.TILE_MOBILE_FAX, HOME_TILES.TILE_SMART_TASK, HOME_TILES.TILE_COPY,
                                           HOME_TILES.TILE_CAMERA_SCAN, HOME_TILES.TILE_PRINT_PHOTOS,
                                           HOME_TILES.TILE_PRINT_DOCUMENTS, HOME_TILES.TILE_SCAN])
    def test_01_tiles_without_onboarding(self, tile_name):
        """
        C27212767 any tile,     C27864735 Print documents
        C27864736 Print Photos, C27864728 Printer scan
        C27864729 Camera Scan,  C27864730 Copy
        C27864738 Mobile Fax,   C27864740 Smart Task
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        if tile_name == HOME_TILES.TILE_MOBILE_FAX and self.fc.fd["home"].verify_tile_displayed(HOME_TILES.TILE_MOBILE_FAX) is False:
            self.fc.add_mobile_fax_tile()
        if tile_name in [HOME_TILES.TILE_COPY, HOME_TILES.TILE_SCAN]:
             self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.fd["home"].select_tile_by_name(tile_name)
        if tile_name in [HOME_TILES.TILE_PRINT_PHOTOS, HOME_TILES.TILE_PRINT_DOCUMENTS]:
            self.fc.fd["home"].select_continue()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)

    def test_02_sign_in_from_tile(self):
        """
        C28073477 sign in from any tile
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.login_value_prop_screen()
        sleep(3)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=True)
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
    
    def test_03_close_button(self):
        """
        C28073479 tap close on tile user onboarding
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        self.fc.fd["ows_value_prop"].select_value_prop_buttons(index=2)
        self.fc.fd["home"].verify_home_tile()

    def test_04_user_onboarding_not_offered_again(self):
        """
        C27212766 sign in and tap on any tile to make sure value prop isn't shown again
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=True)
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()

    def test_05_create_account(self):
        """
        C27864743 User On-boarding from Create Account on the bottom bar
        C28799999 Verify New Create Account screen
        C28073476 Create Account
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)    
        self.fc.fd["home"].verify_bottom_navigation_bar_icons(signed_in=False) 
        self.fc.create_account_from_homepage()
        self.fc.clear_popups_on_first_login(smart_task=True)
        self.fc.fd["home"].verify_bottom_navigation_bar_icons()

    def test_06_create_account_via_settings(self):
        """
        C27212800 User On-boarding from Sign In button in App Settings
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)    
        self.fc.fd["home"].verify_bottom_navigation_bar_icons(signed_in=False) 
        self.fc.fd["home"].select_app_settings()
        self.fc.fd['app_settings'].select_create_account_btn()
        self.fc.create_new_user_account(timeout=30)
        self.fc.fd["app_settings"].verify_bottom_navigation_bar_icons() 
        self.fc.fd["home"].select_home_icon()
        self.fc.clear_popups_on_first_login(smart_task=True)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_PRINT_PHOTOS)
        self.fc.fd["photos"].select_allow_access_to_photos_popup()