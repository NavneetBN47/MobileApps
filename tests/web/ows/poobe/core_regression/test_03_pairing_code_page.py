import pytest
import time
import datetime

pytest.app_info = "POOBE"
pytest.localization = []

class Test_03_Pairing_Code_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.request.config.getoption("--stack")
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.locale = self.request.config.getoption("--locale")
        if "us" not in self.locale:
            self.country, self.language = self.locale.split("_")[1], self.locale.split("_")[0]
        else:
            self.country, self.language = False, False
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.ecp, self.enroll = False, False
        self.pairing_code_page = self.fc.fd["pairing_code_page"]

        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.printer_profile in self.fc.dual_sku_printers:
            self.fc.add_translations_to_app_strings("pairing_code_page", self.biz_model)
        
        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True
        
    def test_01_pairing_code_page(self):
        if self.printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile) # raise_e=False is for the string validation
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        if self.p_oobe.locale not in self.driver.current_url:
            self.driver.navigate(self.driver.current_url.replace("us/en", self.p_oobe.locale))
        self.pairing_code_page.verify_pairing_code_screen()
        self.pairing_code_page.verify_pairing_code_page_header_description()
        self.pairing_code_page.verify_cant_find_pairing_code_madal_btn()
        self.pairing_code_page.click_cant_find_pairing_code_btn()
        self.pairing_code_page.verify_cant_find_pairing_code_modal()
        url = self.fc.fd["ecp"].url if self.ecp else self.p_oobe.poobe_url
        self.driver.navigate(url)
        self.fc.value_prop_page(self.biz_model, self.printer_profile, logged_in=True)
        self.fc.fd["value_prop_page"].click_landing_page_continue_btn()
        self.pairing_code_page.verify_pairing_code_screen()  
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp : self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.printer_profile != "beam" or self.ecp: self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E": self.p_oobe.click_continue_btn()
        if self.printer_profile == "beam" and self.ecp is False: self.fc.handle_printer_fw_page()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

        ################### Private Function ####################

    def verify_hp_support_redirect(self, url):
        if self.driver.check_if_browser_alert_present(raise_e=False):
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        if url not in self.driver.current_url:
            raise AssertionError("Incorrect Hp support website shown to user")