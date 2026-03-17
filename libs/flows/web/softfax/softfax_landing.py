from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
import time


class SoftfaxLanding(SoftFaxFlow):
    flow_name = "softfax_landing"

    #*********************************************************************************
    #                               ACTION FLOWS                                     *
    #*********************************************************************************
    def select_get_started_btn(self):
        """
        Click Get Started button on Mobile Fax Landing page.
        """
        time.sleep(3)
        self.driver.click("get_started_btn")
        if self.driver.wait_for_object("get_started_btn_2", timeout=10, raise_e=False):
            self.driver.click("get_started_btn_2")

    def select_no_thanks_btn(self):
        """
        Click No Thanks button on Mobile Fax Landing page.
        """
        self.driver.click("no_thanks_btn")

    def select_already_a_mobile_fax_user_sign_in_btn(self):
        """
        Click Already a mobile fax user?Sign in button on Mobile Fax Landing page.
        """
        self.driver.click("already_a_mobile_fax_user_sign_in_btn")

    def skip_landing_screen(self):
        """
        Skip mobilefax landing screen, go to mobilefax home
        """
        if self.verify_mobile_fax_landing_screen(raise_e=False):
            self.select_get_started_btn()

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_mobile_fax_landing_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("get_started_btn", timeout=timeout, raise_e=raise_e)

    