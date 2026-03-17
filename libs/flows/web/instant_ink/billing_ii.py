from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow
from MobileApps.libs.ma_misc import ma_misc
import time

class BillingII(InstantinkFlow):
    flow_name="billing_ii"
    
    def select_payment_method(self):
        self.driver.click("select_creditcard_btn")

    def verify_creditcard_iframeload(self, timeout=20):
        self.driver.wait_for_object("creditcard_iframe", timeout=timeout)

    def load_card_details(self,cardtype):
        billing_info = ma_misc.load_json_file("resources/test_data/instant_ink/billing_info.json")[cardtype]

        # iframe=self.driver.wdvr.find_element_by_id("pgs-iframe-credit")
        # self.driver.wdvr.switch_to_frame(iframe)
        self.driver.switch_frame("creditcard_iframe")

        self.driver.click("creditcard_number_txt")
        self.driver.send_keys("creditcard_number_txt", billing_info["cardnumber"])
        time.sleep(2) # The Billing iframe sometimes shows loading spinner after cardnumber is entered not static enough to use wait call. 
        self.driver.select("exp_month_dropdown", option_text=billing_info["month"])
        self.driver.select("exp_year_dropdown", option_text=billing_info["year"])
        self.driver.wait_for_object("cvv_txt")
        self.driver.send_keys("cvv_txt",billing_info["cvv"])
        self.driver.click("next_btn")
        # if frame_name == "default":
        #     self.wdvr.switch_to_default_content()
        self.driver.switch_frame()

    def click_add_billing_btn(self):
        if self.driver.wait_for_object("add_billing_btn", clickable=True, timeout=20):
            self.driver.click("add_billing_btn")

    def verify_billing_overlay_modal(self):
        self.driver.wait_for_object("billing_overlay_modal", timeout=15)

    def click_continue_btn(self, change_check=False):
        if self.driver.wait_for_object("continue_btn", timeout=15):
            self.driver.click("continue_btn", change_check=change_check)