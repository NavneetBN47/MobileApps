import pytest
import datetime

pytest.app_info = "POOBE"

class TestECPartnerLinkPage(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.enroll, self.ecp = False, False
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.ecp_flow = self.fc.fd["ecp"]
        self.partner_link_page = self.fc.fd["partner_link_page"]
        self.portal_oobe_error_modal = self.fc.fd["portal_error_modal"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts


        if self.biz_model == "Flex" and self.printer_profile in self.fc.ecp_printers:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True

        self.printer_info = None if not self.ecp else self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=5456356
        """
    
    def test_01_partner_link_page(self):
        if not self.ecp: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        if self.printer_profile in self.fc.dual_sku_printers or self.printer_profile in self.fc.smb_flex_printer:
            self.fc.select_how_to_setup_printer_company_or_personal(self.biz_model, self.printer_type)
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.printer_profile != "beam" or self.ecp: self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.ecp_flow.verify_ecp_finish_setup_page()
        self.ecp_flow.verify_get_software_and_drivers()
        self.ecp_flow.click_connect_to_partner_button()
        self.partner_link_page.verify_partner_link_page()
        self.partner_link_page.verify_partner_link_id_input_box()
        assert self.ecp_flow.verify_connect_button(clickable=True, raise_e=False) is False, "Connect button should not be clickable"
        self.partner_link_page.enter_partner_link_id(self.company_name)
        self.ecp_flow.click_connect_button()
        self.portal_oobe_error_modal.verify_unable_to_connect_to_hp_partner_link_pay_per_use_modal()
        self.portal_oobe_error_modal.click_cancel_and_setup_manually() # Clicks connect later button
        self.ecp_flow.click_hp_command_center_button()
        self.ecp_flow.verify_command_center_login_page()
        self.ecp_flow.enter_username_hp_command_center_login(self.email)
        self.ecp_flow.click_hp_command_center_login_continue_btn()
        self.fc.verify_ecp_command_center_dashboard(timeout=20)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")