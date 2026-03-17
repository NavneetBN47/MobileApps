from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow

class SoftfaxWelcome(SoftFaxFlow):
    flow_name = "softfax_welcome"

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def skip_welcome_screen(self, is_hipaa=False, is_fist_time=True):
        """
            - Check Term of Agreement
            - Check No/Yes of HIPAA
            - CLick Continue button
        """
        if is_fist_time:
            # Your trial starts now screen takes some time to load it on Welcome to Mobile Fax! screen
            self.driver.click("agree_term_service_cb", timeout=15)
        hipaa_cb = "hipaa_yes_cb" if is_hipaa else "hipaa_no_cb"
        self.driver.click(hipaa_cb)
        self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn", "invisible": True})

    def verify_welcome_screen(self, raise_e=True):
        """
        Note: using continue_btn because the welcome screen takes a while 
              to load
        """
        self.driver.wait_for_object("welcome_title", raise_e=raise_e)
        return self.driver.wait_for_object("continue_btn", raise_e=raise_e)

    def verify_your_trial_starts_screen(self, raise_e=True):
        return self.driver.wait_for_object("continue_btn", raise_e=raise_e)

    def verify_continue_btn_is_disabled(self):
        """
        The Continue button is display but can not to click
        """
        assert self.driver.get_attribute("continue_btn", attribute="IsEnabled").lower() == "false"

class MobileSoftfaxWelcome(SoftfaxWelcome):
    context = "NATIVE_APP"

    def skip_welcome_screen(self, is_hipaa=False, is_fist_time=True):
        """
            - Check Term of Agreement
            - Check No/Yes of HIPAA 
            - CLick Continue button
        """
        if is_fist_time:
            # Your trial starts now screen takes some time to load it on Welcome to Mobile Fax! screen
            self.driver.click("agree_term_service_cb", timeout=15)
        hipaa_cb = "hipaa_yes_cb" if is_hipaa else "hipaa_no_cb"
        # Todo: wait for confirmation from devloper. Temprarily, skip it if it is not displayed instead of rasing NoSuchElementException
        self.driver.click(hipaa_cb, raise_e=False)
        self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn", "invisible": True})

