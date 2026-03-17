from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare

class PortalErrorModal(OWSFlow):
    """
        Contains all of the elements and flows associated poobe error modal
    """
    file_path = __file__
    flow_name = "portal_oobe_error_modal"

     ####################### Printer Activation Error modal #########################
    
    @screenshot_compare(root_obj="activation_error_overlay")
    def verify_activation_error_overlay(self, timeout=15):
        """
        Verify activation error overlay with try again button
        """
        self.driver.wait_for_object("activation_error_overlay", timeout=timeout)
        self.driver.wait_for_object("try_again_btn")
    
    def verify_error_modal(self, timeout=10, raise_e=True):
        """
        Verify Error modal on Printer Activation screen and partner . (url: 'https://smb.pie.portalshell.int.hp.com/us/en/activating'), (https://onboardingcenter.stage.portalshell.int.hp.com/us/en/partner-link)
        """
        return self.driver.wait_for_object("error_modal", timeout=timeout, raise_e=raise_e)
    
    def click_hp_plus_support_btn(self):
        """ Click HP+ Support button on error modal."""
        self.driver.wait_for_object("hp_plus_support")
        self.driver.click("hp_plus_support")

    def wait_for_error_modal(self, timeout=10):
        """
        Wait for Error Modal and Throw an Exception with Error Description.
        """
        if self.verify_error_modal(timeout=timeout, raise_e=False)  is not False:
            raise AssertionError("Printer Activation Error : {} {}".format(self.driver.wait_for_object("error_modal").text.split('\n')[2], self.driver.wait_for_object("error_modal").text.split('\n')[3]))
    
    def click_try_again_btn(self):
        """
        Click try again button on activation error overlay
        """
        self.driver.click("try_again_btn")

    def click_hp_plus_support_link(self):
        self.driver.click("unable_to_activate_hp_plus_support_link")

    def verify_issue_connecting_your_printer_error_modal(self):
        self.driver.wait_for_object("issue_connecting_printer")
        self.driver.wait_for_object("incorrect_modal_change_setup_btn")
        self.driver.wait_for_object("incorrect_modal_try_again_btn")
    
    def verify_are_you_sure_cancel_web_based_onboarding(self):
        self.driver.wait_for_object("are_you_sure_cancel_web_based_onboarding")

    def verify_are_you_sure_web_based_onboarding_modal_cancel_btn(self):
        self.driver.wait_for_object("are_you_sure_web_based_onboarding_modal_cancel_btn")

    def verify_are_you_sure_web_based_onboarding_modal_continue_btn(self):
        self.driver.wait_for_object("are_you_sure_web_based_onboarding_modal_continue_btn")    
    
    def click_cancel_and_setup_manually(self):
        self.driver.click("cancel_and_setup_manually")
    
    ####################### Pairing Code Error modal #########################
    
    def click_change_setup_button(self):
        """
        Click Continue setup button on incorrect flow modal error.
        """
        self.driver.click("incorrect_modal_change_setup_btn")
    
    def click_incorrect_modal_try_again_btn(self):
        """
        Verify Re-try button on incorrect flow modal overlay.
        """
        self.driver.click("incorrect_modal_try_again_btn")
    
    def verify_incorrect_flow_modal(self, raise_e=True, timeout=10):
        """
        Verify incorrect flow modal error overlay can be seen after entering E2E printer pairing code in Flex flow.
        """
        return self.driver.wait_for_object("incorrect_flow_model", raise_e=raise_e, timeout=timeout)
    
    def verify_incorrect_modal_change_setup_btn(self):
        """
        Verify Continue button on Incorrect flow error modal.
        """
        self.driver.wait_for_object("incorrect_modal_change_setup_btn")

    def verify_incorrect_modal_try_again_btn(self):
        """
        Verify Re-try button on incorrect flow modal overlay.
        """
        self.driver.wait_for_object("incorrect_modal_try_again_btn")
    
    @screenshot_compare()
    def verify_unable_to_pair_error_modal(self, timeout=10):
        """
        Verify Unable to pair: New Apiring code required error modal. seen after a Expired pairing code was entered.
        """
        self.driver.wait_for_object("Unable_to_pair_error_modal", timeout=timeout)
        self.driver.wait_for_object("header")

    def verify_invalid_pairing_code_error_msg(self, raise_e=True):
        """
        Verify "Invalid Code. Please Try Again" message after inputing invalid code on Enter your printers's pairing code page
        """
        return self.driver.wait_for_object("invalid_pairing_code", timeout=25, raise_e=raise_e)

    @screenshot_compare(root_obj="paring_code_too_manay_attempts_error")
    def verify_too_many_pairing_code_attempt_error_modal(self, raise_e=True, timeout=10):
        """
        Verify too many pairing code attempts error modal. Overlay will pop after entering 6 invalid pairing code.
        """
        return self.driver.wait_for_object("paring_code_too_manay_attempts_error", timeout=timeout, raise_e=raise_e)
    
    @screenshot_compare(root_obj="scan_to_email_not_enable_error_modal")
    def verify_scan_to_email_not_enabled_error_modal(self, raise_e=True, timeout=10):
        """
        Verify scan to email not enabled error modal.
        """
        return self.driver.wait_for_object("scan_to_email_not_enable_error_modal", timeout=timeout, raise_e=raise_e)
    
    def verify_too_many_pairing_code_attempt_and_body(self, raise_e=True):
        return self.driver.wait_for_object("paring_code_too_manay_attempts_error_description", raise_e=raise_e)
    
    def verify_too_many_pairing_code_attempt_header(self, raise_e=True, timeout=10, invisible=False):
        return self.driver.wait_for_object("header", raise_e=raise_e, timeout=timeout, invisible=invisible)
    

    ####################### unsupported language Error modal #########################

    @screenshot_compare(root_obj="incorrect_flow_model", include_param=["--locale"])
    def verify_unsupported_language_modal_header(self):
        self.driver.wait_for_object("unsupported_language_modal_header")

    @screenshot_compare(root_obj="error_modal", include_param=["--locale"])
    def verify_language_selector_dropbox(self):
        self.driver.wait_for_object("language_selector_dropbox")

    def click_language_selector_dropbox(self):
        self.driver.click("language_selector_dropbox")

    def click_unsupported_language_modal_continue_btn(self):
        self.driver.click("unsupported_language_modal_continue_btn")

    def select_language_from_dropbox(self, format_specifier=['us/en']):
        self.driver.click("language_from_dropbox", format_specifier=format_specifier)

    def get_language_from_dropdown_list(self):
        return self.driver.get_text("select_a_differnet_language_dropdown_list").split("\n")
    

    ####################### unsupported language Error modal #########################

    @screenshot_compare(root_obj="error_modal", include_param=["--locale"])
    def verify_unable_to_connect_to_hp_partner_link_pay_per_use_modal(self):
        self.verify_error_modal()
        self.driver.wait_for_object("header")
        self.driver.wait_for_object("body")
        self.driver.wait_for_object("secondary_button_text")
        self.driver.wait_for_object("primary_button_text")