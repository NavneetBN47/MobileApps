from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class PresenceSensing(HPXFlow):
    flow_name = "presence_sensing"

    def verify_presence_sensing_module_on_home_page(self):
        return self.driver.wait_for_object("presence_sensing_module_on_home_page", timeout=10)

    def navigate_to_settings_page(self):
        self.driver.click("navigate_settings_module")
        time.sleep(3)