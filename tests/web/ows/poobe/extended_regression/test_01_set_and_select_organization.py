import pytest
import time
pytest.app_info = "POOBE"

class Test_01_set_and_select_organization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation") 
        self.browser = self.request.config.getoption("--browser-type")
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.assign_printer_organization = self.fc.fd["assign_printer_organization"]
        self.company_name = "yoyoma"
        self.company_name_1 = "yada yada"

        self.printer_info = None if self.printer_profile not in self.fc.dual_sku_printers else self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

    """ https://hp-testrail.external.hp.com/index.php?/cases/view/30044526 ONBP-223, ONBP-1042"""
        
    def test_01_set_and_select_organization(self):
        if self.printer_info is None: pytest.skip()
        self.navigate_to_assign_organization_page()        
        # Re-start flow again.
        self.driver.navigate(self.p_oobe.poobe_url)
        self.p_oobe.handle_browser_alert_present(accept=True)   
        # check the company name entered the first time
        self.fc.landing_page(self.biz_model, logged_in=True)
        self.value_prop_page.click_landing_page_continue_btn()
        time.sleep(5)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.assign_printer_organization.verify_existing_organization_page(self.company_name)
        
        # Clear Browser data Re-start flow and create new account.
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_assign_organization_page()        
        # Exit and Re-start Flow again
        self.driver.navigate(self.p_oobe.poobe_url)
        if self.driver.check_if_browser_alert_present(raise_e=False) is True:
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        self.fc.landing_page(self.biz_model, logged_in=True)
        self.value_prop_page.click_landing_page_continue_btn()
        time.sleep(5)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.assign_printer_organization.select_new_organization_option()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name_1)
        # Re-star Flow and navigate to assign printer owner page and verify 2 company name
        self.driver.navigate(self.p_oobe.poobe_url)
        self.p_oobe.handle_browser_alert_present(accept=True)
        self.fc.landing_page(self.biz_model, logged_in=True)
        self.value_prop_page.click_landing_page_continue_btn()
        time.sleep(5)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.assign_printer_organization.verify_existing_organization_page(name=self.company_name)
        self.assign_printer_organization.verify_existing_organization_page(name=self.company_name_1)

    #######################################################################################
    ################################# Private Function ####################################

    def navigate_to_assign_organization_page(self):
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)