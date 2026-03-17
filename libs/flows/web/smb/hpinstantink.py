from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
import logging

class HPInstantInk(SMBFlow):
    flow_name = "hpinstantink"
    key_point_intelligence_url = "https://keypointintelligence.com/HPInstantInk"

    def verify_hpinstantink_title(self):
        return self.driver.verify_object_string("hpinstantink_title", timeout=40)

    def verify_hpinstantink_description(self):
        return self.driver.verify_object_string("hpinstantink_description")

    def verify_hpinstantink_never_run_out_title(self):
        return self.driver.verify_object_string("hpinstantink_never_run_out_title")

    def verify_hpinstantink_never_run_out_description(self):
        return self.driver.verify_object_string("hpinstantink_never_run_out_description")

    def verify_hpinstantink_savings_claim_ink_title(self):
        return self.driver.verify_object_string("hpinstantink_savings_claim_ink_title")

    def verify_hpinstantink_savings_claim_ink_description(self):
        return self.driver.verify_object_string("hpinstantink_savings_claim_ink_description")

    def verify_hpinstantink_savings_claim_ink_key_point_hyperlink(self):
        return self.driver.wait_for_object("hpinstantink_savings_claim_ink_key_point_hyperlink")

    def verify_hpinstantink_savings_claim_toner_title(self):
        return self.driver.verify_object_string("hpinstantink_savings_claim_toner_title")

    def verify_hpinstantink_savings_claim_toner_description(self):
        return self.driver.verify_object_string("hpinstantink_savings_claim_toner_description")

    def verify_hpinstantink_savings_claim_toner_key_point_hyperlink(self):
        return self.driver.wait_for_object("hpinstantink_savings_claim_toner_key_point_hyperlink")

    def click_hpinstantink_savings_claim_toner_key_point_hyperlink(self):
        return self.driver.click("hpinstantink_savings_claim_toner_key_point_hyperlink", timeout=30)

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    def verify_signup_now_button(self):
        return self.driver.wait_for_object("signup_now_button", raise_e=False,timeout=30)

    def click_signup_now_button(self):
        return self.driver.click("signup_now_button")

    def verify_enrolling_printer_title(self):
        return self.driver.verify_object_string("enrolling_printer_title", timeout=40)

    def verify_key_point_intelligence_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.key_point_intelligence_url