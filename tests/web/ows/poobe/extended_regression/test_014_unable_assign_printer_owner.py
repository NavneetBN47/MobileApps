import time
import pytest
import datetime

pytest.app_info = "POOBE"

class Test_014_Unable_Assign_printer_Owner(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.browser = self.request.config.getoption("--browser-type")
        self.printer_type = self.request.config.getoption("--printer-operation") 
        
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) 
        self.company_name_1 = "MIS{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        
        self.assign_printer_organization = self.fc.fd["assign_printer_organization"]
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.portal_error_modal = self.fc.fd["portal_error_modal"]
        self.ecp, self.enroll = False, False
        
        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True
        
        """
        TestRail: C31186722
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3291724 
        """
        
    def test_01_unable_to_assign_printer_owner(self):
        if self.printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        self.driver.request_interceptor = lambda request: self.driver.block_request_call(request, "ucde/ucde/v2/ecosystem/accountmgtsvc/accounts")
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.verify_assign_organization_step(self.biz_model, self.company_name, ecp=self.ecp)
        self.p_oobe.click_continue_btn()
        self.portal_error_modal.verify_error_modal(timeout=30)
        del self.driver.request_interceptor
        time.sleep(2)
        self.p_oobe.click_try_again_btn()
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.biz_model == "Flex" and self.printer_profile not in self.fc.smb_flowers and not self.ecp: self.fc.handle_printer_fw_page()
        if self.printer_profile != "beam" or self.ecp: self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E": self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")