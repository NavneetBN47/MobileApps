import logging

from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.support_dashboard.support_dashboard_flow import SupportDashboardFlow

class Dashboard(SupportDashboardFlow):
    flow_name = "dashboard"

    def click_add_device_btn(self):
        self.driver.click("add_device_btn", timeout=60)

    def click_submit_btn(self):
        self.driver.wait_for_object("submit_btn", timeout=20, clickable=True)
        self.driver.click("submit_btn")

    def input_device(self, text):
        self.driver.wait_for_object("add_device_edit", timeout=20)
        self.driver.send_keys("add_device_edit", text)

    def click_sign_in_icon(self):
        self.driver.click("wpr_signin", timeout=10)
    
    def click_sign_out_btn(self):
        self.driver.click("sign_out_btn")
