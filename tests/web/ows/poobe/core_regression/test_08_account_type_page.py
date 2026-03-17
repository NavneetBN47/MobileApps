import time
import pytest
import datetime

pytest.app_info = "POOBE"

class Test_08_Account_Type_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.browser = request.config.getoption("--browser-type")
        
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts

        if self.printer_profile in self.fc.dual_sku_printers and self.biz_model == "E2E":
            self.sim_printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
            time.sleep(2)
            self.sim_printer_info_1 = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
            time.sleep(2)
            self.sim_printer_info_2 = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
            time.sleep(2)
            self.ecp, self.enroll = False, False

    def test_01_account_type_page(self):
        if self.printer_profile not in self.fc.dual_sku_printers or self.biz_model != "E2E":
            pytest.skip()
        """ Select Personal Printer and complete the OOBE Flow."""
        self.navigate_to_how_to_setup_this_printer_page("personal", self.sim_printer_info)
        self.complete_onboarding_flow(self.sim_printer_info)

        """ OOBE Reset and Re-start the flow and create a new account. Select Manage by Company or organization and activate Printer. """
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_how_to_setup_this_printer_page("company", self.sim_printer_info_1)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.complete_onboarding_flow(self.sim_printer_info_1)
        
        """ Re-launch the Flow with the same account and this time select Personal Printer. Activate Printer and complete the Flow."""
        self.driver.navigate(self.p_oobe.poobe_url)
        if self.driver.check_if_browser_alert_present(raise_e=False) is True:
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        self.fc.fd["resume_session_modal"].verify_resume_session_modal()
        self.fc.fd["resume_session_modal"].click_start_new_session_btn()
        self.fc.landing_page(self.biz_model, logged_in=True)
        self.fc.fd["value_prop_page"].click_landing_page_continue_btn()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.sim_printer_info_2, biz = self.biz_model)
        self.complete_onboarding_flow(self.sim_printer_info_2)
        self.fc.remove_printer(self.sim_printer_info, self.biz_model)
        self.fc.remove_printer(self.sim_printer_info_1, self.biz_model)
        self.fc.remove_printer(self.sim_printer_info_2, self.biz_model)
                
        #########################################################
        ################### Private Function ####################

    def navigate_to_how_to_setup_this_printer_page(self, printer_type, printer_details):
        self.fc.landing_page(biz = self.biz_model)
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        if self.hpid.verify_hp_id_sign_in(raise_e=False):
            self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, printer_details, biz = self.biz_model)

    def complete_onboarding_flow(self, printer_details):
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.biz_model == "Flex":
            self.fc.fd["iris_fw_update_notice"].click_accept_auto_fw_updates()
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()  
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, printer_details, self.device_code, self.enroll, self.ecp)