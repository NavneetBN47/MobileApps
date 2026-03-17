import logging

from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.support_dashboard.support_dashboard_flow import SupportDashboardFlow

class Home(SupportDashboardFlow):
    flow_name = "home"

    def click_sign_in_btn(self):
        self.driver.click("sign_in_btn")

    def verify_sign_in_btn(self):
        self.driver.wait_for_object("sign_in_btn", timeout=30)