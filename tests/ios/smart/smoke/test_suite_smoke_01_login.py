"""
Login flow and Functionality smoke test suite for iOS
"""
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.web.const import WEBVIEW_URL
import pytest

pytest.app_info = "SMART"


class Test_Suite_Smoke_01_Login:
    """
    Login Functionality class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        """
        Fresh install of HP SMART app
        """
        self.fc.reset_hp_smart()
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        if pytest.platform == "IOS":
            self.ios_system.clear_safari_cache()
            self.driver.launch_app(BUNDLE_ID.SMART)
            self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME(
                self.driver.driver_type), timeout=30)

    def accept_values():
        """
        Defining pytest parameters for handle_allow_tracking_popup
        """
        if pytest.platform == "IOS":
            for val in [True, False]:
                yield val
        else:
            yield True

    def test_01_verify_terms_and_conditions_page(self):
        """
        C27796362 Precondition: fresh install
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_click_btn()
        self.welcome_web.verify_hp_privacy_statement_link()
        self.welcome_web.verify_terms_of_use_link()
        self.welcome_web.verify_eula_link()

    @pytest.mark.parametrize("accept", accept_values())
    def test_02_verify_behavior_tapping_accept_all_btn(self, accept):
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
            self.ios_system.handle_allow_tracking_popup(
                option=accept, raise_e=False)
            self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=5)
        self.ows_value_prop.verify_ows_value_prop_screen(timeout=5)
