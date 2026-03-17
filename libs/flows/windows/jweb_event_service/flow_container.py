from MobileApps.libs.flows.windows.jweb.event_service_plugin import EventServicePlugin
from MobileApps.libs.flows.windows.jweb_event_service.home import Home

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "event_service_plugin": EventServicePlugin(driver)}