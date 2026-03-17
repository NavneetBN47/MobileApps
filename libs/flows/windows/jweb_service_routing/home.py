from MobileApps.libs.flows.windows.jweb_service_routing.jweb_service_routing_flow import JwebServiceRoutingFlow
from time import sleep
import logging
import time

class Home(JwebServiceRoutingFlow):
    flow_name = "home"

    def select_weblet_btn(self, raise_e=True, max_wait_time=30, check_interval=2):
        """
        From the home page, select the 'Show Weblet' btn towards the top of the screen
        """
        self.driver.click("show_weblet_btn", raise_e=raise_e)

        start_time = time.time()
        attempt = 1
    
        while time.time() - start_time < max_wait_time:
            try:
                logging.info(f"Checking for service routing header (attempt {attempt})")

                if self.driver.wait_for_object("service_routing_header", timeout=1, displayed=True, raise_e=False):
                    logging.info(f"✓ Service routing header loaded successfully on attempt {attempt}")
                    return True
                else:
                    elapsed_time = time.time() - start_time
                    logging.info(f"Header not found yet. Elapsed time: {elapsed_time:.1f}s, waiting {check_interval}s before next check...")

                    time.sleep(check_interval)
                    attempt += 1

            except Exception as e:
                logging.warning(f"Error during attempt {attempt}: {e}")
                time.sleep(check_interval)
                attempt += 1

        total_elapsed = time.time() - start_time
        error_msg = f"Service routing header failed to appear within {total_elapsed:.1f} seconds after clicking 'Show Weblet' button (checked {attempt-1} times)"

        if raise_e:
            raise TimeoutError(error_msg)
        else:
            logging.error(error_msg)
            return False

    def select_webview_engine(self, engine_name):
        """
        Once reference app is launched, select webview engine "WebView 1 (Default)" or "WebView2" to proceed further
        """
        if engine_name not in ["webview1_edge_engine", "webview2_chromium_engine"]:
            raise ValueError("{} not an engine available in the select webview engine pop-up".format(engine_name))
        self.driver.click(engine_name)

    def change_stack(self, option):
        """
        From the change stack page, select the stack option provided as a parameter 
        """
        option = option.upper()
        
        if option not in ["MOCK", "LOCAL", "DEV", "PIE", "STAGING", "PRODUCTION"]:
            raise ValueError("stack option:{} not present within options".format(option))
        
        self.driver.click("stack_list")
        self.driver.click("stack_option", format_specifier=[option])

    def select_settings_btn(self, raise_e=True):
        """
        From the home page, select the 'Show Weblet' btn towards the top of the screen
        """
        try:
            self.driver.wait_for_object("settings_top_menu", timeout=10, raise_e=False)
            self.driver.click("settings_top_menu", raise_e=raise_e)
        except TimeoutError:
            raise TimeoutError("Settings menu did not appear in time.")

    def select_home_btn(self, raise_e=True):
        """
        From the home page, select the 'Show Weblet' btn towards the top of the screen
        """
        self.driver.click("home_btn", raise_e=raise_e)