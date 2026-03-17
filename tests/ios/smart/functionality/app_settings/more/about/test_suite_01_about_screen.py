import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from MobileApps.libs.flows.mac.smart.utility import smart_utilities
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_About_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        if pytest.platform == "MAC":
            cls.mac_browser_popup_flow = cls.fc.fd["mac_browser_popup_flow"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_about_screen_ui(self):
        """
        C31297662
        Verify all the UI elements on the About screen
        """
        self.go_to_about_screen()
        self.app_settings.verify_about_ui_elements()
        if pytest.platform == "MAC":
            self.app_settings.select_close()

    def test_02_verify_back_button_functionality(self):
        """
        C31297662
        Verify clicking back button on About screen goes back to App Settings screen
        """
        self.go_to_about_screen()
        if pytest.platform == "IOS":
            self.app_settings.select_navigate_back()
        else:
            self.app_settings.verify_an_element_and_click(self.app_settings.BUTTON_CLOSE)
            self.home.select_app_settings()
        self.app_settings.verify_app_settings_screen()

    def test_03_verify_rate_us_button_functionality(self):
        """
        C31297662
        Verify clicking rate us button redirects to app store
        """
        self.go_to_about_screen()
        self.app_settings.select_rate_us_button()
        if pytest.platform == "IOS":
            assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.AppStore") == 4)
        else:
            try:
                sleep(2)
                assert smart_utilities.verify_app_store_opened(self.driver)
                smart_utilities.close_app_store(self.driver)
            except Exception:
                self.driver.session_data["ssh"].send_command("pkill App\ Store")
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)

    def test_04_verify_privacy_link_functionality(self):
        """
        C31297662
        Verify clicking HP privacy link redirects to browser link
        """
        self.go_to_about_screen()
        self.app_settings.select_hp_privacy_link()
        if pytest.platform == "IOS":
            assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)
        else:
            self._verify_browser_window("hp_privacy_statement_browser_title")
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)

    def test_05_verify_eula_link_functionality(self):
        """
        C31297662
        Verify clicking EULA agreement link redirects to browser link
        """
        self.go_to_about_screen()
        self.app_settings.select_eula_link()
        if pytest.platform == "IOS":
            assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)
        else:
            self._verify_browser_window("hp_eula_browser_title", "hp_eula", False)
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)

    def test_06_verify_legal_info_link_functionality(self):
        """
        C31297662
        Verify clicking Legal Information link opens up legal info screen
        """
        self.go_to_about_screen()
        self.app_settings.select_legal_info_link()
        self.app_settings.verify_legal_information_ui_elements()
        self.app_settings.select_navigate_back()
        self.app_settings.verify_about_ui_elements()

    def go_to_about_screen(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.app_settings.select_about_cell()
    
    def _verify_browser_window(self, locator, window_name=None, update_main_window=True):
        """
        Verify the window is opened
        :param window_name: name of the window
        """
        if update_main_window:
            self.web_driver.update_window_table("main")
        else:
            self.fc.switch_window_and_modify_wn("mac_browser_popup_flow", window_name)
        self.mac_browser_popup_flow.verify_an_element_and_click(locator)