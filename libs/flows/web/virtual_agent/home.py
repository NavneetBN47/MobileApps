import logging

from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.virtual_agent.va_flow import VAFlow

class Home(VAFlow):
    flow_name = "home"

    def click_solve_issue_btn(self):
        self.driver.click("solve_issue_btn", timeout=20)

    def click_pc_btn(self):
        self.driver.click("pc_btn")

    def input_issue(self, text):
        if self.driver.wait_for_object("input_edit", timeout=20, raise_e=False, clickable=True):
            self.driver.send_keys("input_edit", text, clear_text=True)

    def click_send_btn(self):
        self.driver.click("send_btn")

    def get_solve_issue_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("solve_issue_lbl", raise_e=raise_e, timeout=timeout).text

    def get_pc_btn_title(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("pc_btn", raise_e=raise_e, timeout=timeout).text