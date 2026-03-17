from MobileApps.libs.flows.android.jweb_service_routing.home import Home
from MobileApps.libs.flows.android.jweb_service_routing.service_routing_dev_settings import ServiceRoutingDevSettings
from MobileApps.libs.flows.android.jweb_service_routing.service_routing import ServiceRouting
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.web.jweb.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.resources.const.android.const import *
from MobileApps.resources.const.web.const import *
from time import sleep

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "service_routing": ServiceRouting(driver),
                   "service_routing_dev_settings": ServiceRoutingDevSettings(driver),
                   "web_home": WebHome(driver, context={'url':WEBVIEW_URL.JWEB_SERVICE_ROUTING}),
                   "service_routing_plugin": ServiceRoutingPlugin(driver, context={'url':WEBVIEW_URL.JWEB_SERVICE_ROUTING})}

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
        self.driver.start_activity(PACKAGE.JWEB_SERVICE_ROUTING, LAUNCH_ACTIVITY.JWEB_SERVICE_ROUTING)
        sleep(5)

    def navigate_and_change_stack_option(self, option):
        """
        Navigate to Service Routing Settings and change the stack option
        """
        self.flow_load_home_screen()
        self.fd['home'].select_service_routing_tab()
        self.fd['service_routing'].select_settings_btn()
        self.fd['service_routing'].select_service_routing_stack_btn()
        self.fd['service_routing'].select_stack(option)