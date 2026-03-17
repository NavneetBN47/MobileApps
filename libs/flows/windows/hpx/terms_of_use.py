from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class TermsOfUse(HPXFlow):
    flow_name = "terms_of_use"

    def click_accept_button(self):
        self.driver.click("accept_button")

    def verify_accept_button(self):
        return self.driver.wait_for_object("accept_button", raise_e=False)