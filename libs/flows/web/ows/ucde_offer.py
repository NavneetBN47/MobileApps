from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class UCDEOffer(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/program-offer/
    """
    flow_name = "ucde_offer"

    @screenshot_compare()
    def verify_ucde_offer(self):
        self.driver.wait_for_object("offer_page_div", timeout=20, displayed=False)

    @screenshot_compare()
    def verify_ucde_hp_plus_benefits_page(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("hp_plus_benefits_page",timeout=timeout, displayed=False, raise_e=raise_e)

    def verify_printer_dynamic_security_notice(self, timeout=10):
        """
        Verify Printer Dynamic security notice overlay after clicking decline HP+ offer on HP Plus requirments page.
        """
        self.driver.wait_for_object("printer_dynamic_security_notice", timeout=timeout)
        self.driver.wait_for_object("printer_dynamic_security_notice_continue_btn")
        self.driver.wait_for_object("back_to_offer_btn")
    
    def verify_hp_plus_offer_page(self, timeout=10):
        self.driver.wait_for_object("hp_plus_offer_page", timeout=timeout)
        self.driver.wait_for_object("hp_plus_offer_page_activate_btn")
        self.driver.wait_for_object("back_to_offer_btn")
    
    def click_hp_plus_offer_page_activate_btn(self):
        self.driver.click("hp_plus_offer_page_activate_btn")
    
    def click_printer_dynamic_security_notice_continue_btn(self):
        self.driver.click("printer_dynamic_security_notice_continue_btn")
    
    def verify_learn_more_btn(self):
        self.driver.wait_for_object("learn_more_btn")
    
    def verify_continue_btn(self):
        self.driver.wait_for_object("offer_page_continue_btn")
    
    def verify_do_not_activate_hp_plus_btn(self, timeout=10):
        return self.driver.wait_for_object("decline_offer_btn", displayed=False, timeout=timeout)
    
    def verify_learn_more_page(self, timeout=10):
        self.driver.wait_for_object("learn_more_page", timeout=timeout)
        self.driver.wait_for_object("learn_more_back_btn")
    
    def click_learn_more_back_btn(self):
        self.driver.click("learn_more_back_btn")
    
    def click_learn_more_btn(self):
        self.driver.click("learn_more_btn")

    def click_flex_sign_in_btn(self):
        self.driver.click("flex_sign_in_btn")

    def click_continue(self, change_check=False, timeout=10):
        self.driver.click("offer_page_continue_btn", timeout=timeout, change_check=change_check)

    @screenshot_compare()
    def verify_requirement_popup(self):
        self.driver.wait_for_object("requirement_popup_div")

    @screenshot_compare()
    def verify_confirm_requirements_page(self):
        self.driver.wait_for_object("requirements_content")

    @screenshot_compare(root_obj="requirements_footer_continue_back_btn")
    def verify_confirm_requirments_footer(self):
        self.driver.wait_for_object("requirements_footer_continue_back_btn")

    def click_requirement_popup_continue(self):
        self.driver.click("requirement_popup_continue_btn")

    def click_decline_account_btn(self):
        self.driver.click("decline_account_btn")

    def click_decline_offer_btn(self):
        self.driver.click("decline_offer_btn")

    def click_confirm_button(self):
        self.driver.click("confirm_button")

    @screenshot_compare()
    def verify_decline_offer_popup(self):
        self.driver.wait_for_object("decline_popup")

    def verify_decline_hp_plus_offer_btn(self):
        self.driver.wait_for_object("decline_hp+_btn")
    
    def click_decline_hp_plus_offer_btn(self):
        self.driver.click("decline_hp+_btn")
    
    def click_back_to_offer_btn(self):
        self.driver.click("decline_popup_back_to_offer_btn")
