from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow
from selenium.common.exceptions import ElementClickInterceptedException

class ValueProposition(InstantinkFlow):
    #URL: https://instantink-pie1.hpconnectedpie.com/us/en/n/v2/woobe/value_proposition
    
    flow_name="value_proposition"
    file_path = __file__
    
    def verify_value_proposition_page(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("value_proposition_div", timeout=timeout, raise_e=raise_e)

    def skip_value_proposition_page(self, timeout=10):
        """
        Skip Value Proposition screen:
            - Click on 
            - CLick on Yes, Skip Offer button 
        """
        self.verify_value_proposition_page(timeout=timeout)
        self.driver.click("skip_button", timeout=timeout)
        self.handle_instant_ink_survey_when_offer_skipped()
        self.driver.click("yes_skip_offer_btn")
    
    def click_i_try_btn(self):
        """
        Click on I'll try button on Instant Ink page
        """
        self.driver.click("i_try_it_btn")
    
    def verify_enroll_instant_ink_page(self, timeout=25):
        """
        Verify current screen is the enroll instant ink information page
        """
        self.driver.wait_for_object("Enroll_in_instant_ink_info_page", timeout=timeout)

    def verify_value_proposition_title(self, timeout=10):
        """
        Verify Instant ink title (Only verified for Instant Ink page in Portal OOBE(SMB) flow)
        """
        return self.driver.wait_for_object("value_prop_title", timeout=timeout)

    def verify_learn_more(self):
        """
        Verify learn more overlay button
        """
        return self.driver.wait_for_object("learn_more_overlay_btn")

    def click_skip_trial_offer(self):
        """
        click skip trial offer button on Instant ink page
        """
        return self.driver.click("skip_button")

    def click_yes_skip_offer_btn(self):
        """
        Click skip button on Are you sure overlay
        """
        return self.driver.click("yes_skip_offer_btn")

    def click_continue_btn(self, clickable=False, timeout=10):
        """
        click continue button on for SMB onboarding flow 2 months free toner delivery (software-completion) page.
        """
        if clickable:
            self.driver.wait_for_object("continue_btn", clickable=True, timeout=timeout)
        self.driver.click("continue_btn", timeout=timeout)

    def click_continue_on_automatic_printer_updates(self):
        """
        Click Continue if Autoamtic printer updates overlay are present.
        """
        if self.driver.wait_for_object("automatic_printer_updates", raise_e=False):
            self.driver.click("automatic_printer_updates_continue_btn")

    def click_do_not_enable_ink_btn(self):
        """
        Click Do not enable ink delivery button 
        """
        return self.driver.click("do_not_enable_ink_btn")

    def click_notify_opt(self):
        """
        Click notify option
        """
        return self.driver.click("notify_opt")
    
    def click_Apply_btn(self):
        """
        Click Apply button
        """
        return self.driver.click("Apply_btn")

    def handle_automatic_renewal_notice(self):
        """
        Verify reneweal notice and select checkbox for I have read terms of service.
        """
        if self.driver.wait_for_object("automatic_renewal_notice_disclaimer"):
            try:
                self.driver.click("terms_of_agreement_checkbox")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", self.driver.wait_for_object("terms_of_agreement_checkbox"))
            self.driver.click("redeem_btn")

    def handle_instant_ink_terms_of_service(self):
        # very similar to handle automatic above, different ids work for this in-app flow.
        if self.driver.wait_for_object("automatic_renewal_notice_disclaimer", raise_e=False):
            if self.driver.wait_for_object("disclaimer_show_more_button", raise_e=False):    # Sometimes all part of the disclaimer notice is not visible so have to click down arrow button for visibility
                self.driver.click("disclaimer_show_more_button")
            self.driver.click("agree_ink_terms_of_service_checkbox", displayed=False)
            self.driver.click("redeem_btn")

    def verify_toner_is_on_the_way(self):
        self.driver.wait_for_object("toner_is_on_the_way")
    
    def handle_instant_ink_survey_when_offer_skipped(self):
        """
        Handle Instant Ink suryey pops-up when you skip instant ink offer after sucessfull printer activation.
        """
        if self.driver.wait_for_object("survey_modal_iframe",timeout=10, raise_e=False):
            self.driver.switch_frame("survey_modal_iframe")
            self.driver.wait_for_object("survey_modal_overlay")
            self.driver.click("close_btn_survey_modal")
            self.driver.wdvr.switch_to_default_content()