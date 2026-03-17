import json
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from MobileApps.libs.flows.ios.jweb_auth.home import Home
from MobileApps.libs.flows.ios.jweb_auth.jweb_auth_settings import JWebAuthSettings
from MobileApps.libs.flows.ios.jweb.system import System
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.web.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)
        self.fd = {"system": System(driver),
                   "ios_system": ios_system_flow_factory(driver),
                   "home": Home(driver),
                   "jweb_auth_settings": JWebAuthSettings(driver), 
                   "web_home": WebHome(driver),
                   "auth_plugin": AuthPlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "hpid": HPID(driver, context={'url':'login'})}

    @property
    def flow(self):
        return self.fd

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

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.restart_app(i_const.BUNDLE_ID.JWEB_AUTH)
        sleep(5)

    def reset_app(self):
        """
        Reset App
        """
        self.driver.reset(i_const.BUNDLE_ID.JWEB_AUTH)

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.JWEB_AUTH)

    def call_auth_interaction_entry_point(self, entry_point):
        """
        Go to home screen; Navigate to auth plugin, then; Select specifically entry point.
        """
        self.fd['auth_plugin'].select_user_interaction_entry_point(entry_point)
