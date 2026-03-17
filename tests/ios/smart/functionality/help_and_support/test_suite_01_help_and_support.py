import pytest
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.libs.flows.mac.smart.utility import smart_utilities


pytest.app_info = "SMART"

class Test_Suite_01_Help_And_Support(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.help_support = cls.fc.fd["help_support"]
        if pytest.platform == "IOS":
            cls.safari = cls.fc.fd["safari"]
            cls.ios_system = cls.fc.fd["ios_system"]
        cls.stack = request.config.getoption("--stack")

    @pytest.mark.skip("Unexpected 'BAD REQUEST-WWW HOST NOT ALLOWED' - AIOI-22523")
    def test_01_help_page(self):
        """
        Requirements:
            C31297212 - Verify Help & Support tile behavior.
        Steps: 
            1. Install and launch app.
            2. Go through the consents, sign in and navigate to Home screen.
            3. Tap on Help and Support Tile
        Expected Results:
            1. Verify Support page opens
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.app_settings.select_create_account_btn()
        self.fc.create_new_user_account(timeout=30)
        self.app_settings.verify_bottom_navigation_bar_icons() 
        self.home.select_home_icon()
        self.fc.clear_popups_on_first_login(smart_task=True)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_HELP_AND_SUPPORT)
        try:
            self.help_support.verify_help_center_screen()
        except TimeoutException:
            self.help_support.native_verify_help_center_screen()

    def test_03_help_page_print_document(self):
        """
        IOS & MAC:
        Requirements:
            C37971702 - Verify new online help content displays the specified help page
        Steps:
            1. Add the printer with scanner on the home screen
            2. Click on 'Print documents' or 'Files & Photos' on the app.
            3. Click on HP Smart Files
            4. Click on 'Learn More'
        Expected Results:
            1. Verify Support page displays on screen
        """
        self.fc.go_home(reset=True, stack=self.stack)
        if pytest.platform == "IOS":
            self.ios_system.handle_allow_tracking_popup(raise_e=False)
            self.home.verify_home()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        if pytest.platform == "MAC":
            smart_utilities.delete_all_hp_smart_files(self.driver.session_data["ssh"])
        else:
            self.fc.go_hp_smart_files_and_delete_all_files()
        self.fc.go_hp_smart_files_screen_from_home(select_tile=True)
        self.files.select_learn_more_link_on_empty_files_screen()
        try:
            self.help_support.verify_help_center_screen()
        except TimeoutException:
            self.help_support.native_verify_help_center_screen()
    
    @pytest.mark.skip("Unexpected 'BAD REQUEST-WWW HOST NOT ALLOWED' - AIOI-22523")
    def test_04_virtual_agent(self):
        """
        Requirements:
            C31297217 - Verify behavior when user tap on "Help & Support"
        Steps:
            1. Launch the app
            2. Tap on "Help and Support" tile on Home.
            3. Tap on Chat with Virtual Agent
        Expected Results:
            1. Verify that Support page opens up in a separate web browser. 
            2. Verify chatbot in external browser
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_HELP_AND_SUPPORT)
        self.safari.verify_help_center_container(back_btn=False)
        try:
            self.help_support.verify_help_center_screen()
        except TimeoutException:
            self.help_support.native_verify_help_center_screen()
        self.help_support.select_accept_cookies()
        # https://github.com/appium/appium/issues/10612
        self.help_support.select_chat_with_virtual_agent()
        assert self.driver.wdvr.query_app_state("com.apple.mobilesafari") == 4
        self.help_support.verify_virtual_agent()
