from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from MobileApps.libs.flows.ios.jweb_service_routing.home import Home
from MobileApps.libs.flows.ios.jweb_service_routing.weblet import Weblet
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.web.jweb.settings_plugin import SettingsPlugin
from MobileApps.libs.flows.web.jweb.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const
from time import sleep

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"ios_system": ios_system_flow_factory(driver),
                   "home": Home(driver),
                   "weblet": Weblet(driver),
                   "web_home": WebHome(driver, context={'url':'jweb-reference-weblet'}),
                   "settings_plugin": SettingsPlugin(driver, context={'url':'jweb-reference-weblet'}),
                   "service_routing": ServiceRoutingPlugin(driver, context={'url':'/service_routing'})}

    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def navigate_and_change_stack_option(self, option):
        self.flow_load_home_screen()
        self.fd['home'].select_service_routing_tab_btn()
        self.fd['home'].select_service_routing_settings_btn()
        self.fd['home'].select_service_routing_stack_btn()
        self.fd['home'].change_service_routing_stack(option)

    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch JWeb Logger App
        """
        self.driver.restart_app(i_const.BUNDLE_ID.JWEB_SERVICE_ROUTING)
        sleep(3)

    def open_app(self):
        """
        opens JWeb Logger App
        """
        self.driver.launch_app(i_const.BUNDLE_ID.JWEB_SERVICE_ROUTING)

    def close_app(self):
        """
        closes JWeb Logger App
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.JWEB_SERVICE_ROUTING)