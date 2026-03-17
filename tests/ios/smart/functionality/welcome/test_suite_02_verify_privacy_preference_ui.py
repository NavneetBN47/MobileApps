import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_02_Verify_Privacy_Preference_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        if pytest.platform == "IOS":
            cls.ios_system = cls.fc.fd["ios_system"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.fc.reset_hp_smart()
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        if pytest.platform == "IOS":
            self.ios_system.clear_safari_cache()
            self.driver.launch_app(BUNDLE_ID.SMART)
            self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
    
    def accept_values():
        if pytest.platform == "IOS":
            for val in [True, False]:
                yield val
        else:
            yield True
    
    @pytest.mark.parametrize("accept", accept_values())
    def test_01_verify_behavior_tapping_accept_all_btn(self, accept):
        """
        IOS & MAC:
        C31298102 - Verify new Welcome screen
        C31298103 - Verify behavior by tapping "Accept All"
        IOS:
        C31298104 - Verify behavior by tapping "Allow Tracking"
        C31298105 - Verify behavior by tapping "Ask App Not to Track"
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_click_btn()
        self.welcome_web.verify_manage_options()
        self.welcome_web.click_accept_all_btn()
        if pytest.platform == "IOS":
            if self.welcome_web.verify_permission_for_advertising_screen():
                self.welcome_web.click_continue_btn()
            self.ios_system.handle_allow_tracking_popup(option=accept, raise_e=False)
            self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.ows_value_prop.verify_ows_value_prop_screen(timeout=60)
    
    def test_02_verify_behavior_tapping_manage_options_and_selecting_different_privacy_preferences(self):
        """
        IOS & MAC:
        C31298106 - Verify behavior by tapping "Manage Options"
        C31298107 - Verify behavior by tapping on "Continue" button
        C31298108 - Verify behavior by tapping on "Back" button
        C31298109 - Verify behavior after disabling "App Analytics" option
        C31298110 - Verify behavior after disabling "Advertising" option
        C31298111 - Verify behavior after disabling "Personalized Suggestions" option
        C31298112 - Verify behavior after disabling all options
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_manage_options()
        self.privacy_preferences.click_back_btn()
        self.welcome_web.click_manage_options()
        self.privacy_preferences.click_continue()
        if pytest.platform == "IOS":
            if self.welcome_web.verify_permission_for_advertising_screen():
                self.welcome_web.click_continue_btn()
            self.ios_system.handle_allow_tracking_popup(option=True, raise_e=False)
        self.ows_value_prop.verify_ows_value_prop_screen(timeout=60)