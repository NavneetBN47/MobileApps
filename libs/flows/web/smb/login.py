import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow

class Login(SMBFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for SMB
    """
    flow_name = "login"

    def select_an_organization_to_sign_in(self,tenantID):
        #selecting the organization name based on tenantID
        for _ in range(2): 
            #selecting the organization name if organization count is <= 5
            if self.driver.wait_for_object("organization_radio_btn", timeout=60, raise_e=False) is not False:
                if len(self.driver.find_object("organization_radio_btn_count",multiple=True)) > 1:
                    self.driver.js_click("organization_radio_btn_value",format_specifier=[tenantID])
                    self.driver.click("continue_btn")
                    #sleep included to wait for the page to reload 
                    sleep(15)
                    logging.info("Organization selection radio button is handled")
                else:    
                    self.driver.click("continue_btn")

            #selecting the organization name if organization count is greater than 5
            elif self.driver.wait_for_object("organization_dropdown", timeout=30, raise_e=False) is not False:
                    self.driver.click("organization_dropdown")
                    self.driver.click("organization_dropdown_value",format_specifier=[tenantID], timeout=20)
                    self.driver.click("continue_btn")
                    sleep(10)
                    logging.info("Organization selection dropdown is handled")

    def verify_smb_login_label(self):
        return self.driver.wait_for_object("signin_hp_label",timeout=30)

    def handle_intercept_survey_modal(self, timeout=60):
        for _ in range(2):
            intercept_survey_frame = self.driver.wait_for_object("intercept_survey_modal", timeout=timeout, raise_e=False)
            if intercept_survey_frame is not False:
                self.driver.switch_frame("intercept_survey_modal")
                self.driver.wait_for_object("intercept_survey_modal_form_close_btn", timeout=30, raise_e=False)
                self.driver.js_click("intercept_survey_modal_form_close_btn")
                self.driver.wdvr.switch_to_default_content()
                logging.info("intercept survey modal is handled")
            else:
                logging.info("intercept survey modal is not found")

    def verify_organization_page(self):
        self.driver.wait_for_object("organization_selector_page")
        
    def verify_oraganization_name_in_list(self, company_name):
        if company_name not in self.driver.wait_for_object("organization_selector_list").text:
            raise AssertionError("Organization Name not shown in List to select from")
        
    def click_continue_btn(self):
        self.driver.click("continue_btn")