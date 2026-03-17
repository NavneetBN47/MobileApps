import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class Login(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "login"

    def verify_ecp_login(self):
        return self.driver.wait_for_object("email_txt_box",timeout=20)

    def enter_email_address(self, email):
        return self.driver.send_keys("email_txt_box", email)
    
    def click_next_btn(self):
        self.driver.verify_object_string("next_btn")
        return self.driver.click("next_btn")

    def enter_email_login(self, email):
        self.verify_ecp_login()
        self.enter_email_address(email)
        self.click_next_btn()

    def select_an_organization_to_sign_in(self):
        # Selects the default organization, if there is more than one
        if self.driver.wait_for_object("_shared_organization_selection_radio_btn", timeout=30, raise_e=False) is not False:
            return self.driver.click("_shared_organization_selection_continue_btn")
        return True