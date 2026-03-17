import pytest
import time
import datetime

pytest.app_info = "POOBE"

class Test_01_Already_Enrolled_Printer_Landing_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.ecp, self.enroll = False, False 
        
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.poobe_url = self.biz_model+'_'+self.stack
        
        if self.printer_profile in self.fc.dual_sku_printers:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)        
        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_id=3330697&group_order=asc&display_deleted_cases=0
        
        1. Needs to start with already enrolled printer HPID account.
        2. RE-start flow and check there is continue btn on Landing page and not Sign-in and Create Account button.
        3. Complete the rest onboarding Flow.        
        """


    def test_01_already_enrolled_printer_landing_value_prop_page(self):
        if self.printer_profile not in self.fc.dual_sku_printers: pytest.skip()
        # Test is supposed to be started with account that already has a Printer enrolled.
        self.email, self.pwd = self.complete_the_flow_to_have_account_with_enrolled_printer()
        # Re-start flow without clearing browser data
        self.driver.navigate(self.p_oobe.poobe_url)
        self.p_oobe.handle_browser_alert_present(accept=True)
        self.fc.landing_page(self.biz_model, logged_in=True)
        self.value_prop_page.click_landing_page_continue_btn()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.fc.remove_printer(self.printer_info, self.biz_model, timeout=120)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")


    ################################ Private Function ##################################


    def complete_the_flow_to_have_account_with_enrolled_printer(self):
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.biz_model == "Flex" and not self.ecp: self.fc.handle_printer_fw_page()
        if self.printer_profile not in self.fc.smb_lf_printer or self.ecp: # Beam LF /go flow does not includes Printer Name and Location page
            self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E": self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        return self.email, self.pwd