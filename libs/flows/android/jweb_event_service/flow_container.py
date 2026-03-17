from MobileApps.libs.flows.android.jweb_event_service.home import Home
from MobileApps.libs.flows.android.jweb_event_service.event_service_dev_settings import EventServiceDevSettings
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.web.jweb.event_service_plugin import EventServicePlugin
from MobileApps.resources.const.android.const import *
from MobileApps.resources.const.web.const import *

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "event_service_dev_settings": EventServiceDevSettings(driver),
                   "web_home": WebHome(driver, context={'url': WEBVIEW_URL.JWEB}),
                   "event_service_plugin": EventServicePlugin(driver, context={'url': WEBVIEW_URL.JWEB})}

    @property
    def flow(self):
        return self.fd

    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.wdvr.start_activity(PACKAGE.JWEB_EVENT_SERVICE, LAUNCH_ACTIVITY.JWEB_EVENT_SERVICE)