from MobileApps.libs.flows.web.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.jweb.settings_plugin import SettingsPlugin
from MobileApps.libs.flows.web.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.jweb.browser_plugin import BrowserPlugin
from MobileApps.libs.flows.web.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.web.jweb.event_service_plugin import EventServicePlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.device_plugin import DevicePlugin
from MobileApps.libs.flows.web.jweb.printable_plugin import PrintablePlugin
from MobileApps.libs.flows.web.jweb.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.libs.flows.ios.jweb_service_routing.weblet import Weblet
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.ios.jweb.console import Console
from MobileApps.libs.flows.ios.jweb.system import System
from MobileApps.libs.flows.ios.smart.preview import Preview
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from MobileApps.libs.ma_misc import ma_misc
import json

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)
        self.fd = {"system":System(driver),
                   "ios_system": ios_system_flow_factory(driver),
                   "console": Console(driver),
                   "weblet": Weblet(driver),
                   "web_home": WebHome(driver, context={'url':'jweb-reference-weblet'}),
                   "hpid": HPID(driver, context={'url':'login'}),
                   "home": Home(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "settings_plugin": SettingsPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "auth_plugin": AuthPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "browser_plugin": BrowserPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "event_plugin": EventingPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "event_service_plugin": EventServicePlugin(driver, context=w_const.WEBVIEW_URL.JWEB),
                   "device_plugin": DevicePlugin(driver, context={'url': w_const.WEBVIEW_URL.JWEB}),
                   "service_routing_plugin": ServiceRoutingPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "printable_plugin": PrintablePlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "printer": Preview(driver),
                   "security_gateway": SecurityGateway(driver, context={'url':w_const.WEBVIEW_URL.JWEB_SECURITY})}
    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    #   -----------------------         AUTH PLUGIN       -----------------------------
    def navigate_to_auth_plugin(self):
        self.fd["console"].select_toggle_expand_console()
        if not self.fd["auth_plugin"].verify_at_auth_plugin():
            self.fd["home"].select_plugin_from_home("auth")

    def login_to_hpid(self, username, password):
        self.fd["auth_plugin"].select_auth_logged_in_test()
        if not self.fd["auth_plugin"].auth_logged_in_result()["value"]:
            self.call_auth_interaction_entry_point("signIn")
            self.fd["auth_plugin"].control_auth_token_switches([True, True, True, True, True])
            self.fd["auth_plugin"].select_auth_get_token_test()
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.stack))
            self.fd["hpid"].login(username, password)
        elif "tokenValue" not in self.fd["auth_plugin"].auth_get_token_result():
            self.call_auth_interaction_entry_point("signIn")
            self.fd["auth_plugin"].select_auth_get_token_test()

    def logout_from_hpid(self):
        self.fd["auth_plugin"].select_auth_logged_in_test()
        if self.fd["auth_plugin"].auth_logged_in_result()["value"]:
            self.fd["auth_plugin"].select_auth_logout_test()

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        pkg_name = i_const.BUNDLE_ID.JWEB
        for _ in range(3):
            self.driver.restart_app(pkg_name)
            if len(self.driver.detailed_contexts) > 1:
                return True
        else:
            Exception("Application failed to launch")

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.JWEB)

    def call_auth_interaction_entry_point(self, entry_point):
        """
        Go to home screen; Navigate to auth plugin, then; Select specifically entry point.
        """
        if not self.fd['auth_plugin'].verify_at_auth_plugin():
            self.fd['home'].select_plugin_from_home("auth")
        self.fd['auth_plugin'].select_user_interaction_entry_point(entry_point)

    def get_jweb_auth_test_data(self, stack):
        """
        Get Jweb Auth test data based on stack
        :param stack: stack of the test data
        :return: test data
        """
        with open(ma_misc.get_abs_path("resources/test_data/jweb/ios_auth_accounts.json")) as test_data:
            jweb_auth_test_data = json.loads(test_data.read())
            if stack in ["stage", "pie"]:
                return jweb_auth_test_data[stack]
            elif stack == "dev":
                return jweb_auth_test_data["pie"]
            else:
                raise ValueError("Stack must be one of 'stage', 'pie', or 'dev'. Received: {}".format(stack))
