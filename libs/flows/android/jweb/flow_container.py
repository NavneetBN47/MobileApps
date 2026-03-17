import logging
from time import sleep

from MobileApps.libs.flows.web.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.jweb.browser_plugin import BrowserPlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.web.jweb.event_service_plugin import EventServicePlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.libs.flows.web.jweb.device_plugin import DevicePlugin
from MobileApps.libs.flows.web.jweb.app_plugin import AppPlugin
from MobileApps.libs.flows.web.jweb.printable_plugin import PrintablePlugin
from MobileApps.libs.flows.android.jweb.console import Console
from MobileApps.libs.flows.android.jweb.jweb_dev_settings import JwebDevSettings
from MobileApps.libs.flows.android.hpps.system_ui import System_UI
from MobileApps.libs.flows.android.android_flow import android_system_ui_flow
from MobileApps.libs.flows.android.hpps.hp_print_service import HP_Print_Service
from MobileApps.libs.flows.android.google_chrome.google_chrome import GoogleChrome
from MobileApps.resources.const.android import const as a_const
from MobileApps.resources.const.web import const as w_const

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)

        self.fd = { "system": android_system_ui_flow(driver),
                    "print": System_UI(driver),
                    "hpps": HP_Print_Service(driver),
                    "hpid": HPID(driver, context={'url': self.hpid_url}),
                    "chrome": GoogleChrome(driver),
                    "console": Console(driver),
                    "jweb_dev_settings": JwebDevSettings(driver),
                    "home": Home(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "browser_plugin": BrowserPlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "auth_plugin": AuthPlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "service_routing_plugin": ServiceRoutingPlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "event_plugin": EventingPlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "event_service_plugin": EventServicePlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "device_plugin": DevicePlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "app_plugin": AppPlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "printable_plugin": PrintablePlugin(driver, context=a_const.WEBVIEW_CONTEXT.JWEB),
                    "security_gateway": SecurityGateway(driver, context={'url':'?redirect_to=jwebsample://auth-browser'})}

    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.terminate_app(a_const.PACKAGE.JWEB)
        self.driver.start_activity(a_const.PACKAGE.JWEB, a_const.LAUNCH_ACTIVITY.JWEB)