import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_01_create_account_home(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack, button_index=2)

    def test_01_verify_create_account_screen_home(self):
        self.fc.verify_create_account_screen(stack=self.stack, home=True)

    def test_02_verify_create_account_screen_tile(self):
        self.fc.go_to_home_screen()
        self.fc.add_mobile_fax_tile()
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=45)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=30)
        self.fc.fd["ows_value_prop"].select_value_prop_buttons(0)
        self.driver.wait_for_context(self.fc.hpid_url, timeout=30)
        # self.fc.fd["hpid"].click_create_account_link()
        self.fc.fd["hpid"].verify_hp_id_sign_up()

    def test_03_verify_create_account_home(self):
        self.fc.go_to_home_screen()
        self.fc.create_account_from_homepage()
        self.fc.clear_popups_on_first_login(smart_task=True)
        self.fc.fd["home"].verify_bottom_navigation_bar_icons()