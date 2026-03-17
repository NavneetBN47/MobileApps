import pytest
import datetime

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.browser_type = self.request.config.getoption("--browser-type")
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.iris_fw_update_notice = self.fc.fd["iris_fw_update_notice"]
        self.enroll, self.ecp = False, False
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.invite_email = "qa.mobiauto+invite_e2e_{:%m%d%H%M%S}@gmail.com".format(datetime.datetime.now())
        
        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model) if self.printer_profile in self.fc.dual_sku_printers else None


        """
        testRail: C29699056, C29699057, C29699058, C29699060  C29699057 C29696191 C29699171
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&group_id=3444210&display_deleted_cases=0
        """
    
    def test_01_invite_user_behaviour(self):
        if self.printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        
        if self.biz_model == "Flex" and (self.printer_profile in self.fc.smb_lf_printer or self.printer_profile in self.fc.ecp_printers):
            self.iris_fw_update_notice.verify_fw_update_modal_page()
            self.iris_fw_update_notice.click_accept_auto_fw_updates()
        
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        
        if self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()
        
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        
        self.fc.navigate_users_tab_and_invite(self.invite_email)
        self.fc.get_invite_link_from_email_and_launch(self.invite_email, self.browser_type)
        self.hpid.click_create_account_button()
        self.hpid.create_account(firstname="invitee_test", email=self.invite_email)
        self.fc.navigate_users_tab_and_verify_users(self.invite_email, self.email)
        self.fc.logout_from_dashboard_and_login_to_verify_invitee_status(self.invite_email, self.biz_model, self.email, self.pwd)
        
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")