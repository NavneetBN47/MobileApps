from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class OPD(HPXFlow):
        flow_name = "opd"

        def verify_minimize_button_visible(self):
                return self.driver.wait_for_object("Minimize_Button", raise_e=False, timeout=10) is not False
        
        def verify_maximize_button_visible(self):
                return self.driver.wait_for_object("Maximize_Button", raise_e=False, timeout=10) is not False

        def verify_close_button_visible(self):
                return self.driver.wait_for_object("Close_Button", raise_e=False, timeout=10) is not False

        def click_minimize_button(self):
                self.driver.click("Minimize_Button")

        def click_maximize_button(self):
                self.driver.click("Maximize_Button")

        def click_close_button(self):
                self.driver.click("Close_Button")

        def verify_app_maximized(self):
                return self.driver.wait_for_object("app_state_maximized", raise_e=False, timeout=3) is not False