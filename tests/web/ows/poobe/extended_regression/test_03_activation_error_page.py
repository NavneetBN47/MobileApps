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
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.ecp = False
        
        self.portal_oobe_error = self.fc.fd["portal_error_modal"]
        self.value_prop_page = self.fc.fd["value_prop_page"]
        
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.browser = self.request.config.getoption("--browser-type")
        
        if self.printer_profile not in self.fc.ecp_printers:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3324889
        """
    def test_01_activation_error(self):
        if self.printer_profile not in self.fc.dual_sku_printers: pytest.skip()
        self.username, self.pwd = self.navigate_to_printer_activation_page()
        self.portal_oobe_error.verify_error_modal(timeout=300)
        if self.biz_model == "Flex":
            self.portal_oobe_error.verify_issue_connecting_your_printer_error_modal()
            self.portal_oobe_error.click_change_setup_button() # Same locator for Hp support Button
            self.portal_oobe_error.click_cancel_and_setup_manually()
            """
            Rest of the flow not implemented yet 7/17/2023.
            self.portal_oobe_error.verify_are_you_sure_cancel_web_based_onboarding()
            self.portal_oobe_error.verify_are_you_sure_web_based_onboarding_modal_cancel_btn()
            self.portal_oobe_error.verify_are_you_sure_web_based_onboarding_modal_continue_btn()
            """
        else:
            self.portal_oobe_error.click_hp_plus_support_btn()
            self.driver.add_window("hp_plus_support")
            self.driver.switch_window("hp_plus_support")
            assert "hp-plus" in self.driver.current_url, "URL launched by clicking HP+ Support is not correct"
            self.driver.close_window("hp_plus_support")
            self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
            self.username, self.pwd = self.navigate_to_printer_activation_page(expire_pairing_code=True)
            self.portal_oobe_error.verify_activation_error_overlay()
            self.portal_oobe_error.click_hp_plus_support_link()
            self.portal_oobe_error.click_try_again_btn()
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

    ################################ Private Function ##################################

    def navigate_to_printer_activation_page(self, expire_pairing_code=False):
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.biz_model == "Flex" and not self.ecp: self.fc.handle_printer_fw_page()
        if self.printer_profile not in self.fc.smb_lf_printer or self.ecp: 
            self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E":
            if expire_pairing_code is True: self.driver.active_sleep(300)
            self.p_oobe.click_continue_btn()
        return self.email, self.pwd