import logging
from MobileApps.libs.flows.windows.jweb_service_routing.home import Home
from MobileApps.libs.flows.windows.jweb_service_routing.service_routing_plugin import ServiceRoutingPlugin
from MobileApps.libs.flows.windows.jweb.home import Home as WebletHome

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "service_routing": ServiceRoutingPlugin(driver),
                   "weblet_home": WebletHome(driver)}

    def reset_service_routing_state(self):
        """
        Reset Service Routing to clean state by clearing any active service instances.
        This prevents test interference from lingering app state.
        """
        try:
            logging.info("Resetting Service Routing state for clean test environment...")
            
            # Navigate to Service Routing plugin
            self.fd["home"].select_webview_engine("webview2_chromium_engine")
            self.fd["home"].select_settings_btn()
            self.fd["home"].change_stack('Mock')
            self.fd["home"].select_weblet_btn(raise_e=False)
            self.fd["weblet_home"].select_plugin_from_home("service routing")
            
            # Try to close any running service instances
            try:
                # Close any active service instances
                self.fd["service_routing"].select_close_service_instance_test_btn()
                logging.info("Closed active service instances.")
            except Exception as e:
                logging.debug(f"No service instances to close: {e}")
            
            # Reset to default settings
            try:
                self.fd["service_routing"].select_custom_plugin_from_side_menu()
                self.fd["service_routing"].select_setting_tab()
                self.fd["service_routing"].select_toggle_under_settings_tab(False)  # Reset enforce whitelist
                logging.info("Reset service routing settings to default.")
            except Exception as e:
                logging.debug(f"Settings reset not needed: {e}")
                
            logging.info("Service Routing state reset completed successfully.")
                
        except Exception as e:
            logging.warning(f"Failed to reset Service Routing state: {e}")
