from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from selenium.common.exceptions import NoSuchElementException

class DedicatedSuppliesPage(SmartFlow):
    flow_name = "dedicated_supplies_page"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_try_instant_ink_free_link(self):
        self.driver.click("try_instant_ink_free_link")

    def select_back_btn(self):
        self.driver.click("back_btn")

    def select_get_started_now_link(self):
        self.driver.swipe(distance=10)
        self.driver.click("get_started_now_link")

    def select_get_started_with_hp_instant_ink_link(self):
        self.driver.swipe(distance=10, script_swipe=True)
        self.driver.click("get_started_with_hp_instant_ink")

    def select_not_now_btn(self):
        self.driver.click("not_now_btn")

    def select_finish_setup_link(self):
        self.driver.click("finish_setup_link")

    def select_sign_in_link(self):
        self.driver.click("sign_in_link")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_not_now_dialog(self, raise_e=False):
        return self.driver.wait_for_object("not_now_btn", raise_e=raise_e)

    def verify_hp_instant_ink_page(self):
        if self.driver.wait_for_object("i_accept_btn", timeout=15, raise_e=False):
            self.driver.click("i_accept_btn")
        return self.verify_dsp_p2_page_title() or self.verify_try_instant_ink_free_link() or self.verify_finish_setup_link()

    def verify_dsp_p2_page_title(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("dsp_p2_page_title", raise_e=raise_e, timeout=timeout)

    def verify_get_started_now_link(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("get_started_now_link", raise_e=raise_e, timeout=timeout)
       
    def verify_try_instant_ink_free_link(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("try_instant_ink_free_link", raise_e=raise_e, timeout=timeout)

    def verify_finish_setup_link(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("finish_setup_link", raise_e=raise_e, timeout=timeout)

    def verify_sign_in_link(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("sign_in_link", raise_e=raise_e, timeout=timeout)
        
    def verify_estimated_supply_levels_text(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("estimated_supply_levels_text", raise_e=raise_e, timeout=timeout)
    
    def verify_your_privacy_popup(self, timeout=10, raise_e=False):
        return self.driver.wait_for_object("your_privacy_popup", timeout=timeout, raise_e=raise_e)